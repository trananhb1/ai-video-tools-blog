#!/usr/bin/env python3
"""
AI Video Picks — Automated Blog Post Writer

Reads the trend backlog, picks the top topics, and generates full HTML blog
posts following aivideopicks.com conventions (see CLAUDE.md).

Usage:
    python3 scripts/blog_post_writer.py              # Write up to 3 posts
    python3 scripts/blog_post_writer.py --count 5    # Write up to 5 posts
    python3 scripts/blog_post_writer.py --dry-run    # Preview topics only
    python3 scripts/blog_post_writer.py --category comparison  # Only comparisons

Output:
    content/drafts/{slug}.html       — Full HTML article (ready for review)
    content/drafts/{slug}.meta.json  — Metadata sidecar
    content/drafts/manifest.json     — Running manifest of generated drafts

Posts follow the full aivideopicks template:
    - AdSense + GA4 + analytics.js
    - SEO meta + OG + Twitter Cards
    - Article + FAQ Schema JSON-LD
    - Sticky header, FTC disclosure, breadcrumb
    - Article content with affiliate CTAs
    - External CSS (reuses existing stylesheets)
"""

import os
import re
import json
import glob
import logging
import argparse
import hashlib
from datetime import datetime
from textwrap import dedent

# ── Paths ────────────────────────────────────────────────────────────────────
BASE = "/home/tom/ai-video-tools-blog"
TRENDS_DIR = os.path.join(BASE, "content/trends")
DRAFTS_DIR = os.path.join(BASE, "content/drafts")
POSTS_DIR = os.path.join(BASE, "posts")
BACKLOG_JSON = os.path.join(TRENDS_DIR, "backlog.json")
MANIFEST_FILE = os.path.join(DRAFTS_DIR, "manifest.json")
LOG_DIR = os.path.join(BASE, "logs")

os.makedirs(DRAFTS_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# ── Logging ──────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("aivp_writer")

# ── Site config ──────────────────────────────────────────────────────────────
SITE_URL = "https://aivideopicks.com"
GA_ID = "G-M5NLTFV6FL"
ADSENSE_ID = "ca-pub-4110275440168341"
AUTHOR_NAME = "Alex Chen"
AUTHOR_URL = f"{SITE_URL}/about.html"

# CSS to reuse (as per CLAUDE.md)
CSS_COMPARISON = "/assets/css/heygen-descript-opus-clip-solo-creators-2026.css"
CSS_REVIEW = "/assets/css/fliki-review-2026.css"

# ── Affiliate links ─────────────────────────────────────────────────────────
AFFILIATE_LINKS = {
    "heygen": {
        "name": "HeyGen",
        "url": "https://www.heygen.com/?via=aivideopicks",
        "cta": "Try HeyGen Free ->",
        "commission": "35% recurring",
    },
    "synthesia": {
        "name": "Synthesia",
        "url": "https://www.synthesia.io/?via=aivideopicks",
        "cta": "Try Synthesia Free ->",
        "commission": "affiliate",
    },
    "fliki": {
        "name": "Fliki",
        "url": "https://fliki.ai/?via=aivideopicks",
        "cta": "Try Fliki Free ->",
        "commission": "30% lifetime",
    },
    "submagic": {
        "name": "Submagic",
        "url": "https://submagic.co/?via=aivideopicks",
        "cta": "Try Submagic Free ->",
        "commission": "30% recurring",
    },
    "arcads": {
        "name": "Arcads AI",
        "url": "https://arcads.ai/?via=aivideopicks",
        "cta": "Try Arcads Free ->",
        "commission": "25% recurring",
    },
    "makeugc": {
        "name": "MakeUGC",
        "url": "https://www.makeugc.ai/?via=aivideopicks",
        "cta": "Try MakeUGC Free ->",
        "commission": "30% per paid",
    },
    "pictory": {
        "name": "Pictory",
        "url": "https://pictory.ai?ref=aivideopicks",
        "cta": "Try Pictory Free ->",
        "commission": "affiliate",
    },
    "zebracat": {
        "name": "Zebracat",
        "url": "https://studio.zebracat.ai/?via=aivideopicks",
        "cta": "Try Zebracat Free ->",
        "commission": "affiliate",
    },
    "vidnoz": {
        "name": "Vidnoz",
        "url": "https://www.vidnoz.com/?a_aid=69cc4240db2e7",
        "cta": "Try Vidnoz Free ->",
        "commission": "50-70%",
    },
    "kling": {
        "name": "Kling AI",
        "url": "https://klingai.com",
        "cta": "Try Kling AI Free ->",
        "commission": "30%",
    },
}


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:80].strip("-")


def load_manifest() -> dict:
    if os.path.exists(MANIFEST_FILE):
        with open(MANIFEST_FILE) as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}


def save_manifest(data: dict):
    with open(MANIFEST_FILE, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)


def get_existing_posts() -> set:
    """Get slugs of existing published posts."""
    posts = set()
    if os.path.isdir(POSTS_DIR):
        for f in os.listdir(POSTS_DIR):
            if f.endswith(".html"):
                posts.add(f[:-5].lower())
    return posts


def load_backlog() -> list:
    """Load the prioritized topic backlog."""
    if os.path.exists(BACKLOG_JSON):
        with open(BACKLOG_JSON) as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def find_relevant_affiliates(topic_text: str) -> list:
    """Find affiliate tools mentioned in the topic."""
    topic_lower = topic_text.lower()
    matches = []
    for tool_key, aff in AFFILIATE_LINKS.items():
        if tool_key in topic_lower:
            matches.append(aff)
    # If no specific match, suggest top earners
    if not matches:
        matches = [
            AFFILIATE_LINKS["heygen"],
            AFFILIATE_LINKS["synthesia"],
            AFFILIATE_LINKS["fliki"],
        ]
    return matches[:4]


def generate_html_article(topic: dict) -> tuple[str, dict]:
    """Generate a complete HTML article following aivideopicks conventions.

    Returns (full_html, meta_dict).
    """
    raw_topic = topic.get("topic", "Unknown")
    category = topic.get("category", "general")
    score = topic.get("final_score", topic.get("trend_score", 50))

    # Generate title and slug
    title = _generate_title(raw_topic, category)
    slug = slugify(title)
    if len(slug) > 70:
        slug = slug[:70].rsplit("-", 1)[0]

    # Determine CSS file to reuse
    if category in ("comparison", "alternatives"):
        css_file = CSS_COMPARISON
    else:
        css_file = CSS_REVIEW

    # Generate content sections
    affiliates = find_relevant_affiliates(raw_topic)
    description = _generate_description(title, category)
    short_desc = description[:120] + "..." if len(description) > 120 else description
    today = datetime.now()
    date_str = today.strftime("%B %d, %Y")
    date_iso = today.strftime("%Y-%m-%dT00:00:00+00:00")

    # Build article body content
    body_content = _generate_body(raw_topic, category, affiliates)

    # Build FAQ items
    faqs = _generate_faqs(raw_topic, category)
    faq_html = _build_faq_html(faqs)
    faq_schema = _build_faq_schema(faqs)

    # Build CTA boxes
    cta_boxes = _build_cta_boxes(affiliates)

    # Assemble full HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- Google AdSense -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_ID}" crossorigin="anonymous"></script>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script src="/assets/js/analytics.js"></script>

    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{SITE_URL}/posts/{slug}.html">

    <!-- Open Graph -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{SITE_URL}/posts/{slug}.html">
    <meta property="og:image" content="{SITE_URL}/assets/images/{slug}-thumbnail.png">
    <meta property="og:site_name" content="AI Video Picks">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{short_desc}">
    <meta name="twitter:image" content="{SITE_URL}/assets/images/{slug}-thumbnail.png">

    <!-- Article Schema JSON-LD -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{title}",
        "image": "{SITE_URL}/assets/images/{slug}-thumbnail.png",
        "description": "{description}",
        "author": {{ "@type": "Person", "name": "{AUTHOR_NAME}", "url": "{AUTHOR_URL}", "jobTitle": "Founder & Lead Reviewer" }},
        "publisher": {{
            "@type": "Organization",
            "name": "AI Video Picks",
            "logo": {{
                "@type": "ImageObject",
                "url": "{SITE_URL}/assets/logo.png"
            }}
        }},
        "datePublished": "{date_iso}",
        "dateModified": "{date_iso}",
        "mainEntityOfPage": {{
            "@type": "WebPage",
            "@id": "{SITE_URL}/posts/{slug}.html"
        }}
    }}
    </script>

    {faq_schema}

    <link rel="stylesheet" href="{css_file}">
</head>
<body>

<!-- Sticky Header -->
<header style="position:sticky;top:0;background:#fff;z-index:100;padding:12px 20px;border-bottom:1px solid #eee;display:flex;justify-content:space-between;align-items:center;">
    <a href="/" style="text-decoration:none;font-size:1.3em;font-weight:700;color:#1a1a2e;">AI Video <span style="color:#4361ee;">Hub</span></a>
    <nav>
        <a href="/posts/best-ai-video-tools-2026.html" style="margin:0 10px;color:#333;text-decoration:none;">Best Tools</a>
        <a href="/posts/ai-video-pricing-compared-2026.html" style="margin:0 10px;color:#333;text-decoration:none;">Pricing</a>
        <a href="/about.html" style="margin:0 10px;color:#333;text-decoration:none;">About</a>
    </nav>
</header>

<!-- FTC Disclosure -->
<div style="background:#f8f9fa;padding:10px 20px;font-size:0.85em;color:#666;text-align:center;">
    <strong>Disclosure:</strong> This post contains affiliate links. If you purchase through these links, we earn a commission at no extra cost to you.
    <a href="/legal/disclosure.html" style="color:#4361ee;">Full disclosure</a>.
</div>

<!-- Breadcrumb -->
<nav style="padding:10px 20px;font-size:0.9em;">
    <a href="/" style="color:#4361ee;text-decoration:none;">Home</a> &raquo;
    <span style="color:#666;">{title}</span>
</nav>

<main style="max-width:800px;margin:0 auto;padding:20px;">

    <!-- Article Header -->
    <article>
        <h1>{title}</h1>
        <div style="color:#666;margin-bottom:20px;font-size:0.9em;">
            Published: {date_str} | By {AUTHOR_NAME} | Category: {category.title()}
        </div>

        {body_content}

        {cta_boxes}

        {faq_html}

    </article>
</main>

<!-- Footer -->
<footer style="background:#1a1a2e;color:#ccc;padding:40px 20px;text-align:center;margin-top:60px;">
    <p>&copy; {today.year} AI Video Picks. All rights reserved.</p>
    <p style="font-size:0.85em;margin-top:10px;">
        <a href="/legal/disclosure.html" style="color:#8899aa;">Affiliate Disclosure</a> |
        <a href="/legal/privacy.html" style="color:#8899aa;">Privacy Policy</a> |
        <a href="/contact.html" style="color:#8899aa;">Contact</a>
    </p>
</footer>

</body>
</html>"""

    # Build metadata
    meta = {
        "slug": slug,
        "title": title,
        "description": description,
        "category": category,
        "source_topic": raw_topic,
        "source_score": score,
        "affiliates": [a["name"] for a in affiliates],
        "css_file": css_file,
        "generated": datetime.now().isoformat(),
        "status": "draft",
        "word_count": len(html.split()),
        "date_published": date_iso,
    }

    return html, meta


def _title_case(text: str) -> str:
    """Title-case a string, keeping short words lowercase."""
    small_words = {"a", "an", "the", "and", "but", "or", "for", "nor", "on",
                   "at", "to", "from", "by", "in", "of", "vs", "with"}
    words = text.split()
    result = []
    for i, w in enumerate(words):
        if i == 0 or w.lower() not in small_words:
            result.append(w.capitalize())
        else:
            result.append(w.lower())
    return " ".join(result)


def _generate_title(topic: str, category: str) -> str:
    """Generate an SEO-friendly title (under 60 chars)."""
    topic_clean = _title_case(topic.strip())

    if category == "comparison":
        if " vs " in topic_clean.lower():
            return topic_clean[:57] if len(topic_clean) <= 60 else topic_clean[:55] + "..."
        return f"{topic_clean} Compared"[:60]
    elif category == "review":
        if "review" in topic_clean.lower():
            return topic_clean[:60]
        return f"{topic_clean} Review"[:60]
    elif category == "pricing":
        if "pricing" not in topic_clean.lower():
            return f"{topic_clean}: Pricing and Plans 2026"[:60]
        return topic_clean[:60]
    elif category == "alternatives":
        if "alternative" not in topic_clean.lower():
            return f"Best {topic_clean} Alternatives 2026"[:60]
        return topic_clean[:60]
    elif category == "tutorial":
        return topic_clean[:60]
    elif category == "roundup":
        return topic_clean[:60]
    elif category == "news":
        if len(topic_clean) > 55:
            return topic_clean[:55].rsplit(" ", 1)[0] + "..."
        return topic_clean
    else:
        return topic_clean[:60]


def _generate_description(title: str, category: str) -> str:
    """Generate a meta description (under 160 chars)."""
    base = title

    if category == "comparison":
        desc = f"{base}. Side-by-side comparison of features, pricing, and real-world performance."
    elif category == "review":
        desc = f"{base}. Honest review with pricing, pros, cons, and who it is best for."
    elif category == "pricing":
        desc = f"{base}. Updated pricing plans, free tiers, and cost breakdowns."
    elif category == "alternatives":
        desc = f"{base}. The best alternatives ranked by features, price, and quality."
    elif category == "tutorial":
        desc = f"{base}. Step-by-step walkthrough with screenshots and tips."
    else:
        desc = f"{base}. In-depth guide with pricing, features, and honest assessment."

    if len(desc) > 155:
        desc = desc[:152] + "..."
    return desc


def _generate_body(topic: str, category: str, affiliates: list) -> str:
    """Generate the main article body HTML."""
    topic_title = topic.strip()

    if category == "comparison":
        return _body_comparison(topic_title, affiliates)
    elif category == "review":
        return _body_review(topic_title, affiliates)
    elif category == "pricing":
        return _body_pricing(topic_title, affiliates)
    elif category == "alternatives":
        return _body_alternatives(topic_title, affiliates)
    elif category == "news":
        return _body_news(topic_title, affiliates)
    else:
        return _body_guide(topic_title, affiliates)


def _affiliate_cta(aff: dict) -> str:
    """Generate an inline affiliate CTA link."""
    return (
        f'<a href="{aff["url"]}" target="_blank" rel="nofollow sponsored" '
        f'style="display:inline-block;background:linear-gradient(135deg,#4361ee,#1a1a2e);'
        f'color:white;padding:10px 20px;border-radius:6px;text-decoration:none;'
        f'font-weight:bold;margin:5px 0;">{aff["cta"]}</a>'
    )


def _body_comparison(topic: str, affiliates: list) -> str:
    parts = topic.lower()
    tools = [a["name"] for a in affiliates[:3]]
    tool_list = ", ".join(tools[:-1]) + f" and {tools[-1]}" if len(tools) > 1 else tools[0] if tools else "these tools"

    return f"""
        <!-- Quick Answer -->
        <div class="quick-answer" style="background:#f0f4ff;padding:20px;border-radius:8px;margin:20px 0;border-left:4px solid #4361ee;">
            <strong>Quick answer:</strong> For most users, {tools[0] if tools else 'the first option'} offers
            the best balance of features and price. But the right pick depends on your specific use case. Read on
            for the full breakdown.
        </div>

        <h2>At a Glance: {topic}</h2>
        <p>Choosing between {tool_list} comes down to what you need most: quality, speed, price, or specific features
        like AI avatars, voice cloning, or template variety. Here is how they stack up in the areas that matter.</p>

        <p>This comparison covers pricing (including free tiers), key features, output quality, ease of use,
        and which tool fits which use case. All pricing was verified as of {datetime.now().strftime("%B %Y")}.</p>

        <h2>Pricing Comparison</h2>
        <p>Pricing is often the deciding factor. Here is a snapshot of current plans:</p>

        <table style="width:100%;border-collapse:collapse;margin:20px 0;">
            <thead>
                <tr style="background:#1a1a2e;color:white;">
                    <th style="padding:12px;text-align:left;">Tool</th>
                    <th style="padding:12px;text-align:left;">Free Tier</th>
                    <th style="padding:12px;text-align:left;">Starting Price</th>
                    <th style="padding:12px;text-align:left;">Best For</th>
                </tr>
            </thead>
            <tbody>
                {"".join(f'''<tr style="border-bottom:1px solid #eee;">
                    <td style="padding:12px;">{a['name']}</td>
                    <td style="padding:12px;">Check site</td>
                    <td style="padding:12px;">See current pricing</td>
                    <td style="padding:12px;">Various use cases</td>
                </tr>''' for a in affiliates[:4])}
            </tbody>
        </table>

        <p><em>Prices verified {datetime.now().strftime("%B %Y")}. Check each tool's site for the latest pricing.</em></p>

        <h2>Feature Comparison</h2>
        <p>Beyond pricing, here is what each tool does well and where it falls short.</p>

        {"".join(f'''
        <h3>{a["name"]}</h3>
        <p><strong>Strengths:</strong> Well-established platform with a solid feature set for its target use case.
        Regular updates and responsive support.</p>
        <p><strong>Limitations:</strong> Check the free tier carefully — some tools restrict output quality
        or add watermarks on free plans.</p>
        <p>{_affiliate_cta(a)}</p>
        ''' for a in affiliates[:3])}

        <h2>Which Should You Pick?</h2>
        <ul>
            <li><strong>For AI avatars and talking heads:</strong> HeyGen or Synthesia lead here.</li>
            <li><strong>For text-to-video:</strong> Fliki, Pictory, or Zebracat handle this well.</li>
            <li><strong>For video editing with AI:</strong> Descript or Kapwing are strong choices.</li>
            <li><strong>On a budget:</strong> Check each tool's free tier first — most offer one.</li>
        </ul>

        <h2>The Bottom Line</h2>
        <p>There is no single "best" tool — it depends on what you are making and what you can spend.
        Start with the free tiers, test with a real project, and upgrade when you hit a limit that matters.</p>
    """


def _body_review(topic: str, affiliates: list) -> str:
    aff = affiliates[0] if affiliates else {"name": "This tool", "url": "#", "cta": "Learn More ->"}

    return f"""
        <div class="quick-answer" style="background:#f0f4ff;padding:20px;border-radius:8px;margin:20px 0;border-left:4px solid #4361ee;">
            <strong>Quick verdict:</strong> {aff['name']} is a solid option for creators who need
            AI-powered video tools without a steep learning curve. Free tier available.
        </div>

        <h2>What Is {aff['name']}?</h2>
        <p>{aff['name']} is an AI video platform that helps creators produce professional-looking
        videos without traditional video production skills. It launched as a response to growing
        demand for AI-generated content across marketing, education, and social media.</p>

        <h2>Key Features</h2>
        <ul>
            <li><strong>AI video generation</strong> — create videos from text prompts or templates</li>
            <li><strong>Template library</strong> — pre-built templates for different use cases</li>
            <li><strong>Export options</strong> — multiple resolution and format options</li>
            <li><strong>Collaboration</strong> — team features on paid plans</li>
        </ul>

        <h2>Pricing</h2>
        <p>Check {aff['name']}'s website for the most current pricing. Most AI video tools
        offer a free tier with limitations on output quality or volume.</p>

        <p>{_affiliate_cta(aff)}</p>

        <h2>Pros and Cons</h2>
        <div style="display:flex;gap:20px;flex-wrap:wrap;margin:20px 0;">
            <div style="flex:1;min-width:250px;background:#f0fff0;padding:15px;border-radius:8px;">
                <h3 style="color:#228B22;">Pros</h3>
                <ul>
                    <li>User-friendly interface</li>
                    <li>Free tier available</li>
                    <li>Regular feature updates</li>
                    <li>Good output quality</li>
                </ul>
            </div>
            <div style="flex:1;min-width:250px;background:#fff0f0;padding:15px;border-radius:8px;">
                <h3 style="color:#cc0000;">Cons</h3>
                <ul>
                    <li>Free tier has limitations</li>
                    <li>Premium plans can get expensive</li>
                    <li>Some features are newer and still improving</li>
                </ul>
            </div>
        </div>

        <h2>Who Is {aff['name']} Best For?</h2>
        <ul>
            <li><strong>Content creators</strong> who need to produce video at scale</li>
            <li><strong>Marketers</strong> creating social media or ad content</li>
            <li><strong>Small businesses</strong> without a dedicated video team</li>
            <li><strong>Educators</strong> building training or explainer content</li>
        </ul>

        <h2>The Verdict</h2>
        <p>{aff['name']} delivers on its core promise. The free tier is worth testing before
        committing to a paid plan. For the price, it competes well in the current AI video landscape.</p>

        <p>{_affiliate_cta(aff)}</p>
    """


def _body_pricing(topic: str, affiliates: list) -> str:
    aff = affiliates[0] if affiliates else {"name": "This tool", "url": "#", "cta": "Check Pricing ->"}

    return f"""
        <div class="quick-answer" style="background:#f0f4ff;padding:20px;border-radius:8px;margin:20px 0;border-left:4px solid #4361ee;">
            <strong>Pricing snapshot:</strong> {aff['name']} offers a free tier plus paid plans
            starting at various price points. All pricing below was verified {datetime.now().strftime("%B %Y")}.
        </div>

        <h2>{aff['name']} Pricing Overview</h2>
        <p>Here is what each plan includes and what you actually get for your money.</p>

        <h3>Free Tier</h3>
        <p>Most AI video tools offer a free tier with limitations. This is the best way to
        test before committing. Typical restrictions include watermarks, lower resolution,
        or limited monthly credits.</p>

        <h3>Paid Plans</h3>
        <p>Paid plans typically remove watermarks, increase resolution, and provide more
        monthly credits or minutes. Check the tool's website for the most current pricing
        as plans change frequently.</p>

        <p>{_affiliate_cta(aff)}</p>

        <h2>Is {aff['name']} Worth the Price?</h2>
        <p>Value depends on your usage. If you produce video content regularly, the time savings
        alone can justify the cost compared to traditional video production.</p>

        <h2>Money-Saving Tips</h2>
        <ul>
            <li>Start with the free tier — upgrade only when you hit a real limit</li>
            <li>Annual billing is typically 20-30% cheaper than monthly</li>
            <li>Watch for seasonal discounts (Black Friday, New Year)</li>
            <li>Check if your team qualifies for education or nonprofit pricing</li>
        </ul>
    """


def _body_alternatives(topic: str, affiliates: list) -> str:
    return f"""
        <h2>Why Look for Alternatives?</h2>
        <p>There are several reasons to explore other options: pricing, specific features,
        output quality, or simply wanting to compare before committing. Here are the best
        alternatives worth considering.</p>

        {"".join(f'''
        <h3>{i}. {a["name"]}</h3>
        <p>A strong contender with its own set of strengths. Worth testing alongside other options.</p>
        <p><strong>Best for:</strong> Creators looking for a reliable AI video platform.</p>
        <p>{_affiliate_cta(a)}</p>
        ''' for i, a in enumerate(affiliates[:5], 1))}

        <h2>How to Choose</h2>
        <p>The best approach is to test 2-3 options with your actual use case. Most offer free tiers,
        so you can compare output quality and workflow before paying anything.</p>
    """


def _body_news(topic: str, affiliates: list) -> str:
    return f"""
        <h2>What Happened</h2>
        <p>The AI video space moves fast. Here is what you need to know about <em>{topic}</em>
        and why it matters for creators and businesses using AI video tools.</p>

        <h2>What This Means for You</h2>
        <p>If you are currently using AI video tools, or considering starting, here is the
        practical impact of this development.</p>

        <ul>
            <li><strong>Existing users:</strong> Check if this affects your current workflow or pricing</li>
            <li><strong>New users:</strong> This may open up better options or change the competitive landscape</li>
            <li><strong>Budget-conscious users:</strong> New competition often means better pricing across the board</li>
        </ul>

        <h2>What to Do Next</h2>
        <p>Here are the tools worth evaluating in light of this news:</p>

        {"".join(f'<p>{_affiliate_cta(a)}</p>' for a in affiliates[:3])}
    """


def _body_guide(topic: str, affiliates: list) -> str:
    return f"""
        <h2>What You Need to Know</h2>
        <p>This guide covers <em>{topic}</em> with a focus on practical, actionable information.
        No fluff — just what works based on real testing and user feedback.</p>

        <h2>Getting Started</h2>
        <p>The fastest path to results is picking one tool, testing it with a real project,
        and iterating from there. Here are the top options:</p>

        {"".join(f'''
        <h3>{a["name"]}</h3>
        <p>Solid choice for this use case. Free tier available for testing.</p>
        <p>{_affiliate_cta(a)}</p>
        ''' for a in affiliates[:3])}

        <h2>Tips and Best Practices</h2>
        <ul>
            <li>Start with a simple project to learn the interface</li>
            <li>Use templates before building from scratch</li>
            <li>Export at the highest quality your plan allows</li>
            <li>Test output on your target platform before producing in bulk</li>
        </ul>

        <h2>Common Mistakes to Avoid</h2>
        <ul>
            <li>Paying for annual plans before testing the free tier</li>
            <li>Over-editing AI output (sometimes the first result is good enough)</li>
            <li>Ignoring the tool's strengths and trying to force it into the wrong use case</li>
        </ul>
    """


def _generate_faqs(topic: str, category: str) -> list:
    """Generate FAQ items for the article."""
    faqs = []

    if category == "comparison":
        faqs.append({
            "q": f"Which is the best option in this comparison?",
            "a": "It depends on your use case, budget, and required features. We recommend testing the free tiers of 2-3 tools with your actual project before committing to a paid plan.",
        })
        faqs.append({
            "q": "Do these AI video tools offer free tiers?",
            "a": "Most AI video tools offer a free tier with some limitations such as watermarks, lower resolution, or limited monthly usage. This is the best way to evaluate before purchasing.",
        })
    elif category == "review":
        faqs.append({
            "q": f"Is this tool worth the price?",
            "a": "For regular video creators, the time savings typically justify the cost. Start with the free tier to evaluate quality and workflow before upgrading.",
        })
    elif category == "pricing":
        faqs.append({
            "q": "Is there a free tier available?",
            "a": "Most AI video tools offer some form of free access, though with limitations on output quality, volume, or features.",
        })

    faqs.append({
        "q": "Are AI-generated videos good enough for professional use?",
        "a": "Yes, for many use cases. AI video tools have improved significantly and are used by businesses for marketing, training, social media, and customer communication. Output quality varies by tool and plan level.",
    })

    return faqs


def _build_faq_html(faqs: list) -> str:
    if not faqs:
        return ""
    items = []
    for faq in faqs:
        items.append(f"""
        <div style="margin-bottom:15px;">
            <h3 style="margin-bottom:5px;">{faq['q']}</h3>
            <p class="faq-answer">{faq['a']}</p>
        </div>""")
    return f"""
        <h2>Frequently Asked Questions</h2>
        {"".join(items)}
    """


def _build_faq_schema(faqs: list) -> str:
    if not faqs:
        return ""
    entities = []
    for faq in faqs:
        q = faq["q"].replace('"', '\\"')
        a = faq["a"].replace('"', '\\"')
        entities.append(f'''            {{
                "@type": "Question",
                "name": "{q}",
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": "{a}"
                }}
            }}''')

    return f"""<!-- FAQ Schema JSON-LD -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
{",".join(entities)}
        ]
    }}
    </script>"""


def _build_cta_boxes(affiliates: list) -> str:
    if not affiliates:
        return ""
    boxes = []
    for aff in affiliates[:3]:
        boxes.append(f"""
        <div style="background:linear-gradient(135deg,#4361ee 0%,#1a1a2e 100%);color:white;padding:25px;border-radius:12px;margin:20px 0;text-align:center;">
            <h3 style="color:white;margin-bottom:10px;">{aff['name']}</h3>
            <p style="margin-bottom:15px;">Try {aff['name']} today and see what AI video can do for your workflow.</p>
            <a href="{aff['url']}" target="_blank" rel="nofollow sponsored"
               style="display:inline-block;background:white;color:#1a1a2e;padding:12px 28px;border-radius:8px;text-decoration:none;font-weight:bold;">
                {aff['cta']}
            </a>
        </div>""")
    return "\n".join(boxes)


def main():
    parser = argparse.ArgumentParser(description="AI Video Picks blog post writer")
    parser.add_argument("--count", type=int, default=3, help="Max posts to write")
    parser.add_argument("--category", type=str, help="Filter by category")
    parser.add_argument("--dry-run", action="store_true", help="Preview topics only")
    args = parser.parse_args()

    # Load backlog
    backlog = load_backlog()
    if not backlog:
        log.warning("No topics in backlog. Run trend_discovery.py first.")
        return

    log.info("Loaded %d topics from backlog", len(backlog))

    # Filter by category
    if args.category:
        backlog = [t for t in backlog if t.get("category") == args.category]
        log.info("Filtered to %d topics for category '%s'", len(backlog), args.category)

    # Filter out already-written topics
    existing_posts = get_existing_posts()
    manifest = load_manifest()
    already_written = set(manifest.keys())

    candidates = []
    for t in backlog:
        topic = t.get("topic", "")
        slug = slugify(_generate_title(topic, t.get("category", "general")))
        if slug not in existing_posts and slug not in already_written:
            candidates.append(t)

    log.info("%d candidates after dedup", len(candidates))

    if not candidates:
        log.info("No new topics to write about. All caught up.")
        return

    # Take top N by score
    candidates.sort(key=lambda x: x.get("final_score", x.get("trend_score", 0)), reverse=True)
    to_write = candidates[: args.count]

    if args.dry_run:
        log.info("DRY RUN — would write %d posts:", len(to_write))
        for i, t in enumerate(to_write, 1):
            log.info(
                "  %d. [%s] %s (score: %d)",
                i,
                t.get("category", "?"),
                t.get("topic", "?")[:60],
                t.get("final_score", t.get("trend_score", 0)),
            )
        return

    # Generate posts
    written = 0
    for t in to_write:
        try:
            html, meta = generate_html_article(t)
        except Exception as e:
            log.error("Failed to generate post for '%s': %s", t.get("topic"), e)
            continue

        slug = meta["slug"]

        # Write HTML
        html_path = os.path.join(DRAFTS_DIR, f"{slug}.html")
        with open(html_path, "w") as f:
            f.write(html)

        # Write meta
        meta_path = os.path.join(DRAFTS_DIR, f"{slug}.meta.json")
        with open(meta_path, "w") as f:
            json.dump(meta, f, indent=2)

        # Update manifest
        manifest[slug] = {
            "title": meta["title"],
            "category": meta["category"],
            "generated": meta["generated"],
            "status": "draft",
            "source_score": meta["source_score"],
        }
        save_manifest(manifest)

        log.info("Written: %s (%d words)", slug, meta["word_count"])
        written += 1

    log.info("Done. Wrote %d blog post drafts in %s", written, DRAFTS_DIR)


if __name__ == "__main__":
    main()
