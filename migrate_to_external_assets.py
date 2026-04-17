#!/usr/bin/env python3
"""
Migrate aivideopicks from inline CSS/JS to external assets.

Saves ~660KB across 56 HTML files by:
1. Extracting ALL inline <style> blocks to external CSS files (deduped by hash)
2. Replacing inline gtag+tracker JS with a single <script src>
3. Naming CSS files by slug (shared hashes get a common name)

Run: python3 migrate_to_external_assets.py [--dry-run]
"""

import hashlib
import os
import re
import sys
from pathlib import Path

REPO = Path("/home/tom/ai-video-tools-blog")
CSS_DIR = REPO / "assets" / "css"
JS_FILE = "/assets/js/analytics.js"
DRY_RUN = "--dry-run" in sys.argv

# Regex: match the gtag config script + tracker script (two consecutive <script> blocks)
# Pattern 1: separate blocks
GTAG_PATTERN = re.compile(
    r'<script>\s*\n?\s*window\.dataLayer.*?</script>\s*\n*'
    r'<script>\s*\n?\s*/\* AVP_OUTBOUND_TRACKER_v1 \*/.*?</script>',
    re.DOTALL
)
# Pattern 2: combined in one block
GTAG_COMBINED = re.compile(
    r'<script>\s*\n?\s*window\.dataLayer.*?/\* AVP_OUTBOUND_TRACKER_v1 \*/.*?</script>',
    re.DOTALL
)

STYLE_RE = re.compile(r'<style>(.*?)</style>', re.DOTALL)

# Track deduplication
css_hash_map = {}  # hash -> filename
stats = {"files": 0, "bytes_saved": 0, "css_files": 0, "js_replacements": 0}


def get_css_filename(css_text: str, slug: str) -> str:
    """Get or create a CSS filename for this content."""
    h = hashlib.md5(css_text.strip().encode()).hexdigest()[:10]
    if h in css_hash_map:
        return css_hash_map[h]
    fname = f"{slug}.css"
    # Avoid collisions
    if (CSS_DIR / fname).exists() or fname in css_hash_map.values():
        fname = f"{slug}-{h[:6]}.css"
    css_hash_map[h] = fname
    if not DRY_RUN:
        (CSS_DIR / fname).write_text(css_text.strip() + "\n")
    stats["css_files"] += 1
    return fname


def replace_js(content: str) -> tuple[str, bool]:
    """Replace inline gtag+tracker with external script reference."""
    tag = f'<script src="{JS_FILE}"></script>'
    new, n = GTAG_PATTERN.subn(tag + "\n", content, count=1)
    if n:
        return new, True
    new, n = GTAG_COMBINED.subn(tag + "\n", content, count=1)
    if n:
        return new, True
    return content, False


def process_file(filepath: Path, slug: str) -> list[str]:
    """Process one HTML file. Returns list of change descriptions."""
    content = filepath.read_text(encoding="utf-8")
    original_size = len(content)
    changes = []

    # 1. Replace JS
    content, js_changed = replace_js(content)
    if js_changed:
        changes.append("JS externalized")
        stats["js_replacements"] += 1

    # 2. Replace ALL style blocks with external CSS
    style_blocks = list(STYLE_RE.finditer(content))
    if style_blocks:
        # Process in reverse order to preserve offsets
        for i, match in enumerate(reversed(style_blocks)):
            block_idx = len(style_blocks) - 1 - i
            css_text = match.group(1)
            suffix = f"-extra{block_idx}" if block_idx > 0 else ""
            css_fname = get_css_filename(css_text, f"{slug}{suffix}")
            css_link = f'<link rel="stylesheet" href="/assets/css/{css_fname}">'
            content = content[:match.start()] + css_link + content[match.end():]
            changes.append(f"CSS -> {css_fname}")

    saved = original_size - len(content)
    stats["bytes_saved"] += saved

    if changes and not DRY_RUN:
        filepath.write_text(content, encoding="utf-8")

    stats["files"] += 1
    return changes


def main():
    mode = "DRY RUN" if DRY_RUN else "LIVE"
    print(f"[{mode}] Migrating aivideopicks to external assets\n")

    CSS_DIR.mkdir(parents=True, exist_ok=True)

    # Posts
    posts = sorted((REPO / "posts").glob("*.html"))
    print(f"--- {len(posts)} posts ---")
    for p in posts:
        slug = p.stem
        changes = process_file(p, slug)
        if changes:
            print(f"  {p.name}: {', '.join(changes)}")

    # Non-post pages
    others = []
    for pattern in ["*.html", "landing/*.html", "legal/*.html", "tools/*.html"]:
        others.extend(REPO.glob(pattern))
    others = sorted(set(others))

    print(f"\n--- {len(others)} other pages ---")
    for p in others:
        slug = p.stem
        if p.parent != REPO:
            slug = f"{p.parent.name}-{slug}"
        changes = process_file(p, slug)
        if changes:
            print(f"  {p.relative_to(REPO)}: {', '.join(changes)}")

    print(f"\n=== SUMMARY ===")
    print(f"Files processed: {stats['files']}")
    print(f"JS replacements: {stats['js_replacements']}")
    print(f"CSS files created: {stats['css_files']} (in {CSS_DIR.relative_to(REPO)}/)")
    print(f"Total bytes saved: {stats['bytes_saved']:,} ({stats['bytes_saved']/1024:.0f} KB)")

    if DRY_RUN:
        print("\nDRY RUN complete. Run without --dry-run to apply.")


if __name__ == "__main__":
    main()
