#!/usr/bin/env python3
"""
Batch-regenerate every post's thumbnail using the Pillow renderer.

For each posts/<slug>.html, extracts the <title>, infers badge type from
the slug pattern, infers tool list from the post body (matching against
the chip catalog), and renders a fresh 600x340 PNG to assets/images/.

Slug → output PNG mapping must match the existing CSS rules in
assets/css/index.css. We probe both <slug>.png and the legacy short names.

Run from repo root:
    python3 scripts/batch-regen-thumbnails.py [--dry-run]
"""
import html
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
import importlib.util
spec = importlib.util.spec_from_file_location("gen", REPO_ROOT / "scripts" / "generate-thumbnail.py")
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)

POSTS_DIR = REPO_ROOT / "posts"
IMG_DIR = REPO_ROOT / "assets" / "images"

# slug → existing thumbnail filename (when CSS rule uses a short name)
SLUG_TO_PNG = {
    "best-ai-video-tools-2026":            "top10",
    "ai-video-pricing-compared-2026":      "pricing-compared",
    "best-free-ai-video-generators-2026":  "free-ai-video",
    "heygen-vs-synthesia-2026":            "heygen-vs-synthesia",
    "kling-vs-veo-vs-runway":              "kling-veo-runway",
    "veed-vs-kapwing-vs-descript":         "veed-kapwing-descript",
    "d-id-vs-elai-vs-hourone":             "did-elai-hourone",
    "heygen-descript-opus-clip-solo-creators-2026": "heygen-descript-opus-clip",
    "best-ai-talking-head-tools-2026":     "talking-head-tools",
    "best-ai-video-tools-beginners-2026":  "beginners-guide",
    "ai-tools-youtube-creators-2026":      "youtube-creators",
    "ai-training-onboarding-videos":       "ai-training",
    "ai-video-for-ecommerce":              "ecommerce",
    "ai-video-social-media-marketing-2026":"ai-video-social-media",
    "ai-video-glossary-2026":              "ai-video-glossary",
    "ai-video-deals-coupons-2026":         "deals-coupons",
    "save-15-percent-movavi-april-2026":   "save-15-movavi-april-2026",
    "what-is-text-to-video-ai":            "text-to-video-explainer",
    "cheapest-ai-video-generator-2026":    "cheapest-ai-video",
    "turn-long-videos-into-shorts-ai":     "shorts-repurpose",
    "best-gear-ai-video-creators-2026":    "gear-guide",
    "how-to-make-faceless-youtube-heygen-submagic": "faceless-youtube-heygen-submagic",
    "how-to-add-viral-captions-tiktok-submagic": "tiktok-captions-submagic",
    "how-to-create-ai-videos-heygen":      "tutorial",
    "submagic-vs-capcut-2026":             "comparison",
    "heygen-vs-synthesia-vs-pictory":      "comparison",
    "sora-alternatives-2026":              "sora-alternatives",
    # Review slugs → existing CSS rules use no-year naming
    "heygen-review-2026":     "heygen-review",
    "synthesia-review-2026":  "synthesia-review",
    "runway-review-2026":     "runway-review",
    "fliki-review-2026":      "fliki-review",
    "pictory-review-2026":    "pictory-review",
    "movavi-review-2026":     "movavi-review",
    "vidnoz-review-2026":     "vidnoz-review",
    "submagic-review-2026":   "submagic-review",
    "zebracat-review-2026":   "zebracat-review",
    "elevenlabs-review-2026": "elevenlabs-review",
    "descript-review-2026":   "descript-review",
    "colossyan-review-2026":  "colossyan-review",
    "invideo-review-2026":    "invideo-review",
    "opus-clip-review-2026":  "opus-clip-review",
    "murf-ai-review-2026":    "murf-ai-review",
    "deepbrain-ai-review-2026": "deepbrain-ai-review",
}

# Review post slug prefix → tool name to feature in review card
REVIEW_TOOL = {
    "heygen-review-2026":     "HeyGen",
    "synthesia-review-2026":  "Synthesia",
    "runway-review-2026":     "Runway",
    "fliki-review-2026":      "Fliki",
    "pictory-review-2026":    "Pictory",
    "movavi-review-2026":     "Movavi",
    "vidnoz-review-2026":     "Vidnoz",
    "submagic-review-2026":   "Submagic",
    "zebracat-review-2026":   "Zebracat",
    "elevenlabs-review-2026": "ElevenLabs",
    "descript-review-2026":   "Descript",
    "colossyan-review-2026":  "Colossyan",
    "invideo-review-2026":    "InVideo",
    "opus-clip-review-2026":  "OpusClip",
    "murf-ai-review-2026":    "Murf",
    "deepbrain-ai-review-2026": "DeepBrain",
}

REVIEW_PATTERN = re.compile(r"-review(-\d+)?$")
COMPARISON_HINTS = ("-vs-", "best-", "alternatives", "compared")
GUIDE_HINTS = ("how-to-", "what-is-", "guide", "glossary", "explainer")
DEAL_HINTS = ("deal", "deals-coupons", "save-", "-percent-")
URGENT_HINTS = ("shutting-down", "deadline", "ending", "alternatives-")

# Tool name → keyword variants to scan for in post HTML
TOOL_KEYWORDS = {
    "HeyGen":     ("heygen",),
    "Synthesia":  ("synthesia",),
    "Kling":      ("kling",),
    "Runway":     ("runway",),
    "Pika":       ("pika labs", "pika "),
    "Fliki":      ("fliki",),
    "Zebracat":   ("zebracat",),
    "Pictory":    ("pictory",),
    "Submagic":   ("submagic",),
    "Movavi":     ("movavi",),
    "Vidnoz":     ("vidnoz",),
    "Arcads":     ("arcads",),
    "MakeUGC":    ("makeugc", "make ugc"),
    "Descript":   ("descript",),
    "Veo":        ("google veo", "veo 3", "veo 4"),
    "Sora":       ("openai sora", "sora 2", "sora alternative"),
    "ElevenLabs": ("elevenlabs", "eleven labs"),
    "InVideo":    ("invideo",),
    "Veed":       ("veed.io", "veed "),
    "CapCut":     ("capcut",),
    "OpusClip":   ("opus clip", "opusclip"),
    "Hedra":      ("hedra",),
}


def slug_from_path(p):
    return p.stem


def title_from_html(text):
    m = re.search(r"<title>([^<]+)</title>", text)
    if not m:
        return "Untitled"
    raw = m.group(1).strip()
    raw = re.sub(r"\s*\|\s*AI Video Picks.*$", "", raw, flags=re.I)
    raw = re.sub(r"\s*-\s*aivideopicks.*$", "", raw, flags=re.I)
    return html.unescape(raw)[:80]


def badge_for(slug):
    s = slug.lower()
    if any(h in s for h in DEAL_HINTS):
        return "DEAL"
    if any(h in s for h in URGENT_HINTS):
        return "URGENT"
    if REVIEW_PATTERN.search(s):
        return "REVIEW"
    if any(h in s for h in GUIDE_HINTS):
        return "GUIDE"
    if any(h in s for h in COMPARISON_HINTS):
        return "COMPARISON"
    return "GUIDE"


def tools_in_post(text, slug):
    """Detect tools mentioned in the post body.

    For REVIEW posts (slug like `<tool>-review-2026`), prioritize the
    reviewed tool first so it leads the chip strip.
    For VS comparison posts (slug like `a-vs-b-vs-c`), prioritize those
    in the order they appear in the slug.
    """
    body = text.lower()

    priority = []
    s = slug.lower()
    if "-review" in s:
        head = s.split("-review")[0]
        for name in TOOL_KEYWORDS:
            if head == name.lower() or head.startswith(name.lower() + "-"):
                priority.append(name)
                break
    if "-vs-" in s:
        for token in re.split(r"-vs-|-(?=\d)", s):
            for name in TOOL_KEYWORDS:
                if name.lower() in token and name not in priority:
                    priority.append(name)
                    break

    found = list(priority)
    for name, kws in TOOL_KEYWORDS.items():
        if name in found:
            continue
        if any(kw in body for kw in kws):
            found.append(name)
        if len(found) >= 7:
            break
    return found[:7]


def output_slug_for(post_slug):
    """Return the bare filename root the existing CSS expects (without -thumbnail.png)."""
    return SLUG_TO_PNG.get(post_slug, post_slug)


def extract_rating(text):
    """Pull rating values out of the post HTML.

    Returns (rating_5, rating_text) where rating_5 is on 0-5 scale and
    rating_text is the display string (e.g. '8.5 / 10' or '4.5 / 5').
    Returns (None, None) if no rating found.
    """
    # JSON-LD ratingValue (most reliable, already on 5-scale by convention)
    m = re.search(r'"ratingValue"\s*:\s*"?([\d.]+)"?', text)
    if m:
        v = float(m.group(1))
        # Look for matching X/10 score in body for the display
        score10 = re.search(r"(\d+\.?\d*)\s*/\s*10", text)
        if score10:
            return v, f"{score10.group(1)} / 10"
        return v, f"{v} / 5"
    # Fallback: scan for "X.X / 10" or "X out of 10" in body
    m = re.search(r"(\d+\.?\d*)\s*/\s*10", text)
    if m:
        v10 = float(m.group(1))
        return v10 / 2, f"{v10} / 10"
    m = re.search(r"(\d+\.?\d*)\s*out\s*of\s*10", text, re.I)
    if m:
        v10 = float(m.group(1))
        return v10 / 2, f"{v10} / 10"
    return None, None


def main():
    dry = "--dry-run" in sys.argv
    posts = sorted(POSTS_DIR.glob("*.html"))
    print(f"Found {len(posts)} posts. Dry-run: {dry}\n")

    for post in posts:
        slug = slug_from_path(post)
        text = post.read_text(encoding="utf-8", errors="ignore")
        title = title_from_html(text)
        badge = badge_for(slug)
        tools = tools_in_post(text, slug)
        out_slug = output_slug_for(slug)

        review_tool = REVIEW_TOOL.get(slug)
        if review_tool:
            rating_5, rating_text = extract_rating(text)
            if rating_5 is None:
                rating_5, rating_text = 4.0, "8.0 / 10"  # safe default
            print(f"  {slug} [REVIEW CARD]")
            print(f"    tool: {review_tool}, rating: {rating_5}/5 ({rating_text})")
            print(f"    -> assets/images/{out_slug}-thumbnail.png")
            if not dry:
                gen.render_review(slug=out_slug, title=title, tool=review_tool,
                                  rating_5=rating_5, rating_text=rating_text)
        else:
            print(f"  {slug}")
            print(f"    title: {title!r}")
            print(f"    badge: {badge}")
            print(f"    tools: {tools or '(none detected)'}")
            print(f"    -> assets/images/{out_slug}-thumbnail.png")
            if not dry:
                gen.render(slug=out_slug, title=title, badge=badge, tools=tools)
        print()


if __name__ == "__main__":
    main()
