#!/usr/bin/env python3
"""Inject one contextual internal link from every /posts/*.html (except the hero
itself) into the hero page best-ai-video-tools-2026.html.

Idempotent: uses AVP_HERO_LINK_v1 marker and also skips any file that already
contains a href to best-ai-video-tools-2026.html.

Insertion strategy: add a small paragraph right before the closing </main> or,
failing that, right before the first </article> or </footer>. This keeps the
link inside the article body without disturbing existing layout.
"""
from pathlib import Path
import re

POSTS = Path("/home/tom/ai-video-tools-blog/posts")
HERO = "best-ai-video-tools-2026.html"
MARK = "AVP_HERO_LINK_v1"

SNIPPET = (
    '<p class="hero-backlink" data-marker="' + MARK + '" '
    'style="margin:28px 0;padding:14px 18px;background:#f0f4ff;'
    'border-left:3px solid #155DFC;border-radius:6px;font-size:15px;">'
    'Still deciding which platform to use? See <a href="best-ai-video-tools-2026.html" '
    'style="color:#155DFC;text-decoration:underline;font-weight:600;">'
    'our top 10 AI video tools for 2026</a> &mdash; ranked after 80+ hours of hands-on testing.'
    '</p>'
)

# Insert before the first of these closers we can find.
CLOSERS = ["</main>", "</article>", "<!-- Footer -->", "<footer"]

updated = 0
already = 0
no_anchor = 0
total = 0

for f in sorted(POSTS.glob("*.html")):
    if f.name == HERO:
        continue
    total += 1
    src = f.read_text()
    if MARK in src:
        already += 1
        continue
    # Skip if the post already links to the hero (contextual link already exists).
    if 'href="best-ai-video-tools-2026.html"' in src or "href='best-ai-video-tools-2026.html'" in src:
        already += 1
        continue

    inserted = False
    for closer in CLOSERS:
        idx = src.find(closer)
        if idx != -1:
            src = src[:idx] + SNIPPET + "\n" + src[idx:]
            inserted = True
            break
    if not inserted:
        no_anchor += 1
        print(f"NO_ANCHOR: {f.name}")
        continue
    f.write_text(src)
    updated += 1

print(f"Scanned {total} posts (excluding hero).")
print(f"  Updated: {updated}")
print(f"  Already linked / already had marker: {already}")
print(f"  No insert anchor found: {no_anchor}")
