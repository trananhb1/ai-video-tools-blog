#!/usr/bin/env python3
"""
AI Video Picks — Trend Discovery Engine

Monitors trending AI tool launches, updates, and comparisons. Identifies
content gaps where no article exists yet. Outputs a prioritized backlog
of blog post topics.

Sources:
    1. Google Trends (pytrends) — rising AI-related queries
    2. Reddit JSON API — r/aivideo, r/artificial, r/ChatGPT, etc.
    3. Existing content audit — gap analysis against published articles
    4. Competitor keyword patterns — common AI video tool queries

Usage:
    python3 scripts/trend_discovery.py               # Full scan
    python3 scripts/trend_discovery.py --quick        # Google Trends + Reddit only
    python3 scripts/trend_discovery.py --dry-run      # Preview without writing files

Output:
    content/trends/trend_report_{date}.json
    content/topics_backlog.md (updated)
"""

import os
import re
import sys
import json
import time
import random
import hashlib
import logging
import argparse
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime, timedelta
from collections import Counter

# ── Paths ────────────────────────────────────────────────────────────────────
BASE = "/home/tom/ai-video-tools-blog"
TRENDS_DIR = os.path.join(BASE, "content/trends")
CACHE_DIR = os.path.join(TRENDS_DIR, ".cache")
POSTS_DIR = os.path.join(BASE, "posts")
BACKLOG_FILE = os.path.join(BASE, "content/topics_backlog.md")
BACKLOG_JSON = os.path.join(TRENDS_DIR, "backlog.json")
LOG_DIR = os.path.join(BASE, "logs")

os.makedirs(TRENDS_DIR, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# ── Logging ──────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("aivp_trends")

CACHE_TTL_HOURS = 6

# ── Seed Terms ───────────────────────────────────────────────────────────────
SEED_TERMS = [
    "AI video generator", "text to video AI", "AI avatar video",
    "AI video editor", "AI video tools", "AI talking head",
    "HeyGen", "Synthesia", "Runway", "Pika", "Kling AI",
    "Veo AI", "Sora alternative", "AI UGC video",
    "AI video marketing", "AI video for business",
    "AI video pricing", "AI subtitle generator",
    "AI video free", "deepfake video maker",
    "AI video generator 2026", "best AI video tool",
]

# AI video subreddits and related communities
REDDIT_SUBS = [
    "aivideo", "artificial", "ChatGPT", "StableDiffusion",
    "singularity", "OpenAI", "DefunctMedia", "VideoEditing",
]

# Known AI video tools for tracking
KNOWN_TOOLS = [
    "heygen", "synthesia", "runway", "pika", "kling", "veo",
    "sora", "fliki", "descript", "pictory", "invideo", "opus clip",
    "submagic", "colossyan", "murf", "zebracat", "vidnoz",
    "d-id", "elai", "hourone", "kapwing", "veed", "movavi",
    "elevenlabs", "luma", "pixverse", "seedance", "wan",
    "vidu", "vizard", "arcads", "makeugc", "deepbrain",
    "happyhorse", "minimax", "hailuo",
]

# ── Affiliate Programs (for prioritizing monetizable topics) ─────────────────
AFFILIATE_TOOLS = {
    "heygen": {"commission": "35% recurring", "priority": 10},
    "synthesia": {"commission": "via=aivideopicks", "priority": 8},
    "fliki": {"commission": "30% lifetime", "priority": 8},
    "submagic": {"commission": "30% recurring", "priority": 7},
    "arcads": {"commission": "25% recurring", "priority": 7},
    "makeugc": {"commission": "30% per paid", "priority": 6},
    "pictory": {"commission": "ref=aivideopicks", "priority": 6},
    "zebracat": {"commission": "via=aivideopicks", "priority": 6},
    "vidnoz": {"commission": "50-70%", "priority": 5},
    "kling": {"commission": "30%", "priority": 7},
}


def _cache_path(key: str) -> str:
    h = hashlib.md5(key.encode()).hexdigest()
    return os.path.join(CACHE_DIR, f"{h}.json")


def _read_cache(key: str) -> dict | None:
    path = _cache_path(key)
    if not os.path.exists(path):
        return None
    try:
        with open(path) as f:
            data = json.load(f)
        cached_at = datetime.fromisoformat(data.get("_cached_at", "2000-01-01"))
        if datetime.now() - cached_at > timedelta(hours=CACHE_TTL_HOURS):
            return None
        return data
    except (json.JSONDecodeError, ValueError):
        return None


def _write_cache(key: str, data: dict):
    data["_cached_at"] = datetime.now().isoformat()
    with open(_cache_path(key), "w") as f:
        json.dump(data, f)


# ── Google Trends ────────────────────────────────────────────────────────────
def scan_google_trends(use_cache: bool = True) -> list:
    """Pull rising queries from Google Trends for AI video terms."""
    results = []

    try:
        from pytrends.request import TrendReq
    except ImportError:
        log.warning("pytrends not installed — skipping Google Trends")
        return results

    # Check cache
    cache_key = "google_trends_ai_video"
    if use_cache:
        cached = _read_cache(cache_key)
        if cached:
            log.info("Google Trends: using cache (%d items)", len(cached.get("results", [])))
            return cached.get("results", [])

    log.info("Google Trends: scanning %d seed terms...", len(SEED_TERMS))

    try:
        pytrends = TrendReq(hl="en-US", tz=360, timeout=(10, 25))
    except Exception as e:
        log.error("Failed to init pytrends: %s", e)
        return results

    # Process in batches of 5 (pytrends limit)
    for i in range(0, min(len(SEED_TERMS), 15), 5):
        batch = SEED_TERMS[i : i + 5]
        try:
            pytrends.build_payload(batch, timeframe="now 7-d", geo="")
            time.sleep(random.uniform(2, 5))

            # Related queries
            related = pytrends.related_queries()
            for term, data in related.items():
                if data and data.get("rising") is not None:
                    df = data["rising"]
                    for _, row in df.iterrows():
                        query = str(row.get("query", "")).strip()
                        value = row.get("value", 0)
                        if query and _is_relevant(query):
                            results.append({
                                "topic": query,
                                "source": "google_trends",
                                "trend_score": min(95, int(value / 100) + 60) if value else 60,
                                "growth": f"{value}% rising",
                                "region": "global",
                                "category": _categorize_ai_topic(query),
                                "seed_term": term,
                            })

                if data and data.get("top") is not None:
                    df = data["top"]
                    for _, row in df.head(5).iterrows():
                        query = str(row.get("query", "")).strip()
                        value = row.get("value", 0)
                        if query and _is_relevant(query):
                            results.append({
                                "topic": query,
                                "source": "google_trends",
                                "trend_score": min(85, int(value / 2) + 40),
                                "growth": f"top query (value: {value})",
                                "region": "global",
                                "category": _categorize_ai_topic(query),
                                "seed_term": term,
                            })

        except Exception as e:
            log.warning("Google Trends batch %d error: %s", i, e)
            time.sleep(5)
            continue

        time.sleep(random.uniform(3, 7))

    # Deduplicate
    seen = set()
    deduped = []
    for r in results:
        key = r["topic"].lower().strip()
        if key not in seen:
            seen.add(key)
            deduped.append(r)

    log.info("Google Trends: found %d unique topics", len(deduped))
    _write_cache(cache_key, {"results": deduped})
    return deduped


# ── Reddit ───────────────────────────────────────────────────────────────────
def scan_reddit(use_cache: bool = True) -> list:
    """Scan AI-related subreddits for trending AI video topics."""
    results = []

    cache_key = "reddit_ai_video"
    if use_cache:
        cached = _read_cache(cache_key)
        if cached:
            log.info("Reddit: using cache (%d items)", len(cached.get("results", [])))
            return cached.get("results", [])

    log.info("Reddit: scanning %d subreddits...", len(REDDIT_SUBS))

    for sub in REDDIT_SUBS:
        url = f"https://www.reddit.com/r/{sub}/hot.json?limit=25&t=week"
        try:
            req = urllib.request.Request(
                url,
                headers={
                    "User-Agent": "AIVideoPicksTrendBot/1.0 (trend research)",
                    "Accept": "application/json",
                },
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode("utf-8"))

            posts = data.get("data", {}).get("children", [])
            for post in posts:
                pd = post.get("data", {})
                title = pd.get("title", "").strip()
                score = pd.get("score", 0)
                num_comments = pd.get("num_comments", 0)

                if not title or score < 50:
                    continue

                # Check if it's about AI video tools
                if not _is_relevant(title):
                    continue

                trend_score = min(95, 50 + int(score / 100) + int(num_comments / 20))

                results.append({
                    "topic": title,
                    "source": "reddit",
                    "subreddit": sub,
                    "trend_score": trend_score,
                    "growth": f"{score} upvotes, {num_comments} comments",
                    "region": "global",
                    "category": _categorize_ai_topic(title),
                    "url": f"https://reddit.com{pd.get('permalink', '')}",
                })

        except Exception as e:
            log.warning("Reddit r/%s error: %s", sub, e)

        time.sleep(random.uniform(1, 3))

    log.info("Reddit: found %d relevant topics", len(results))
    _write_cache(cache_key, {"results": results})
    return results


# ── Content Gap Analysis ─────────────────────────────────────────────────────
def analyze_content_gaps() -> list:
    """Compare known tools against existing articles to find gaps."""
    results = []

    # Get list of existing article slugs
    existing_slugs = set()
    if os.path.isdir(POSTS_DIR):
        for f in os.listdir(POSTS_DIR):
            if f.endswith(".html"):
                existing_slugs.add(f[:-5].lower())

    log.info("Content gap analysis: %d existing articles", len(existing_slugs))

    # Check for missing reviews
    for tool in KNOWN_TOOLS:
        tool_slug = tool.lower().replace(" ", "-").replace(".", "")
        review_slug = f"{tool_slug}-review-2026"
        if review_slug not in existing_slugs:
            priority = 70
            aff = AFFILIATE_TOOLS.get(tool_slug, {})
            if aff:
                priority += aff.get("priority", 0)

            results.append({
                "topic": f"{tool.title()} Review 2026",
                "source": "content_gap",
                "trend_score": priority,
                "growth": "missing review",
                "region": "global",
                "category": "review",
                "gap_type": "missing_review",
                "tool": tool,
                "has_affiliate": bool(aff),
            })

    # Check for missing comparisons between affiliate tools
    affiliate_tools_list = list(AFFILIATE_TOOLS.keys())
    for i, tool_a in enumerate(affiliate_tools_list):
        for tool_b in affiliate_tools_list[i + 1 :]:
            comp_slug_1 = f"{tool_a}-vs-{tool_b}"
            comp_slug_2 = f"{tool_b}-vs-{tool_a}"
            # Check various slug patterns
            found = False
            for slug in existing_slugs:
                if (tool_a in slug and tool_b in slug) or (tool_b in slug and tool_a in slug):
                    found = True
                    break
            if not found:
                priority_a = AFFILIATE_TOOLS[tool_a].get("priority", 0)
                priority_b = AFFILIATE_TOOLS[tool_b].get("priority", 0)
                combined = 60 + priority_a + priority_b

                results.append({
                    "topic": f"{tool_a.title()} vs {tool_b.title()} 2026",
                    "source": "content_gap",
                    "trend_score": min(95, combined),
                    "growth": "missing comparison",
                    "region": "global",
                    "category": "comparison",
                    "gap_type": "missing_comparison",
                    "tools": [tool_a, tool_b],
                    "has_affiliate": True,
                })

    # Common query patterns that might be missing
    query_patterns = [
        "best ai video generator for {use_case}",
        "ai video tools for {use_case}",
        "{tool} pricing 2026",
        "{tool} alternatives 2026",
        "how to use {tool}",
        "{tool} free tier",
    ]

    use_cases = [
        "marketing", "ecommerce", "real estate", "education",
        "social media", "youtube", "tiktok", "linkedin",
        "sales", "training", "presentations", "ads",
    ]

    for uc in use_cases:
        slug_check = f"ai-video-{uc.replace(' ', '-')}"
        found = any(slug_check in s for s in existing_slugs)
        if not found:
            results.append({
                "topic": f"Best AI Video Tools for {uc.title()} 2026",
                "source": "content_gap",
                "trend_score": 65,
                "growth": "missing use-case guide",
                "region": "global",
                "category": "guide",
                "gap_type": "missing_use_case",
            })

    # Check for missing pricing pages (high commercial intent)
    for tool in affiliate_tools_list:
        pricing_slug = f"{tool}-pricing-2026"
        if pricing_slug not in existing_slugs:
            results.append({
                "topic": f"{tool.title()} Pricing 2026: Plans, Costs, Free Tier",
                "source": "content_gap",
                "trend_score": 75 + AFFILIATE_TOOLS[tool].get("priority", 0),
                "growth": "missing pricing page",
                "region": "global",
                "category": "pricing",
                "gap_type": "missing_pricing",
                "tool": tool,
                "has_affiliate": True,
            })

    log.info("Content gaps: found %d opportunities", len(results))
    return results


# ── Helpers ──────────────────────────────────────────────────────────────────
def _is_relevant(text: str) -> bool:
    """Check if a query/title is relevant to AI video tools."""
    text_lower = text.lower()
    ai_keywords = [
        "ai video", "ai tool", "text to video", "video generator",
        "avatar", "talking head", "ai edit", "deepfake",
        "ai subtitle", "ai caption", "text-to-video",
        "video ai", "ai film", "ai movie", "ugc ai",
        "ai ad", "ai marketing video",
    ]
    tool_match = any(tool in text_lower for tool in KNOWN_TOOLS)
    keyword_match = any(kw in text_lower for kw in ai_keywords)
    return tool_match or keyword_match


def _categorize_ai_topic(text: str) -> str:
    """Categorize an AI video topic."""
    text_lower = text.lower()

    if any(w in text_lower for w in ["vs", "versus", "compared", "comparison", "better"]):
        return "comparison"
    if any(w in text_lower for w in ["price", "pricing", "cost", "plan", "free", "cheap"]):
        return "pricing"
    if any(w in text_lower for w in ["review", "honest", "worth it", "tried"]):
        return "review"
    if any(w in text_lower for w in ["how to", "tutorial", "guide", "step", "create"]):
        return "tutorial"
    if any(w in text_lower for w in ["best", "top", "ranking"]):
        return "roundup"
    if any(w in text_lower for w in ["new", "launch", "update", "release", "announce"]):
        return "news"
    if any(w in text_lower for w in ["alternative", "replace", "instead", "switch"]):
        return "alternatives"
    return "general"


def prioritize_topics(all_topics: list) -> list:
    """Score and rank all discovered topics."""
    for topic in all_topics:
        score = topic.get("trend_score", 50)

        # Boost topics with affiliate potential
        topic_lower = topic.get("topic", "").lower()
        for tool, aff in AFFILIATE_TOOLS.items():
            if tool in topic_lower:
                score += aff.get("priority", 0) * 2
                topic["monetizable"] = True
                break

        # Boost comparisons (high commercial intent)
        if topic.get("category") == "comparison":
            score += 10
        elif topic.get("category") == "pricing":
            score += 8
        elif topic.get("category") == "review":
            score += 5

        # Penalize very generic topics
        if len(topic.get("topic", "")) < 15:
            score -= 10

        topic["final_score"] = min(100, score)

    all_topics.sort(key=lambda x: x.get("final_score", 0), reverse=True)
    return all_topics


def update_backlog_md(topics: list):
    """Update the markdown backlog file with new discovered topics."""
    today = datetime.now().strftime("%Y-%m-%d")

    # Load existing backlog to preserve manually-added items
    existing_content = ""
    if os.path.exists(BACKLOG_FILE):
        with open(BACKLOG_FILE) as f:
            existing_content = f.read()

    # Extract existing topic titles to avoid duplicates
    existing_titles = set()
    for line in existing_content.split("\n"):
        m = re.match(r"###\s+\d+\.\s+(.+)", line)
        if m:
            existing_titles.add(m.group(1).strip().lower())

    # Find new topics not already in backlog
    new_topics = []
    for t in topics[:30]:  # Top 30
        title = t.get("topic", "").strip()
        if title.lower() not in existing_titles:
            new_topics.append(t)

    if not new_topics:
        log.info("No new topics to add to backlog")
        return

    # Build new section
    section = f"\n\n## Auto-Discovered ({today})\n\n"
    for i, t in enumerate(new_topics[:15], 1):
        score = t.get("final_score", t.get("trend_score", 0))
        category = t.get("category", "general")
        source = t.get("source", "unknown")
        monetizable = "Yes" if t.get("monetizable") else "No"
        topic = t.get("topic", "Unknown")

        section += f"### {i}. {topic}\n"
        section += f"- **Added**: {today} (auto-discovered)\n"
        section += f"- **Source**: {source} | **Category**: {category}\n"
        section += f"- **Score**: {score} | **Monetizable**: {monetizable}\n"
        section += f"- **Status**: QUEUED\n\n"

    # Append to existing backlog
    with open(BACKLOG_FILE, "a") as f:
        f.write(section)

    log.info("Added %d new topics to %s", len(new_topics[:15]), BACKLOG_FILE)


def write_report(all_topics: list) -> str:
    """Write the full trend report JSON."""
    today = datetime.now().strftime("%Y-%m-%d")
    report_path = os.path.join(TRENDS_DIR, f"trend_report_{today}.json")

    report = {
        "generated": today,
        "sources_checked": list({t.get("source") for t in all_topics}),
        "total_topics": len(all_topics),
        "high_score_topics": len([t for t in all_topics if t.get("final_score", 0) >= 70]),
        "monetizable_topics": len([t for t in all_topics if t.get("monetizable")]),
        "trending_topics": all_topics[:50],
        "categories": dict(Counter(t.get("category", "general") for t in all_topics)),
    }

    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)

    # Also write JSON backlog
    with open(BACKLOG_JSON, "w") as f:
        json.dump(all_topics[:50], f, indent=2)

    log.info("Report written: %s", report_path)
    return report_path


def main():
    parser = argparse.ArgumentParser(description="AI Video Picks trend discovery")
    parser.add_argument("--quick", action="store_true", help="Google Trends + Reddit only")
    parser.add_argument("--no-cache", action="store_true", help="Ignore cache")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    args = parser.parse_args()

    use_cache = not args.no_cache
    all_topics = []

    # Source 1: Google Trends
    log.info("=== Source 1: Google Trends ===")
    trends = scan_google_trends(use_cache=use_cache)
    all_topics.extend(trends)

    # Source 2: Reddit
    log.info("=== Source 2: Reddit ===")
    reddit = scan_reddit(use_cache=use_cache)
    all_topics.extend(reddit)

    # Source 3: Content gap analysis (skip on --quick)
    if not args.quick:
        log.info("=== Source 3: Content Gap Analysis ===")
        gaps = analyze_content_gaps()
        all_topics.extend(gaps)

    # Deduplicate by topic text
    seen = set()
    deduped = []
    for t in all_topics:
        key = t.get("topic", "").lower().strip()
        if key and key not in seen:
            seen.add(key)
            deduped.append(t)

    log.info("Total unique topics: %d", len(deduped))

    # Prioritize
    prioritized = prioritize_topics(deduped)

    if args.dry_run:
        log.info("DRY RUN — top 15 topics:")
        for i, t in enumerate(prioritized[:15], 1):
            log.info(
                "  %2d. [%3d] [%s] %s %s",
                i,
                t.get("final_score", 0),
                t.get("category", "?"),
                t.get("topic", "?")[:60],
                "($$)" if t.get("monetizable") else "",
            )
        return

    # Write report
    report_path = write_report(prioritized)

    # Update markdown backlog
    update_backlog_md(prioritized)

    log.info("Done. Report: %s", report_path)
    log.info("Top 5 topics:")
    for i, t in enumerate(prioritized[:5], 1):
        log.info(
            "  %d. [%d] %s (%s)",
            i, t.get("final_score", 0), t.get("topic", "?")[:50], t.get("category", "?"),
        )


if __name__ == "__main__":
    main()
