#!/usr/bin/env python3
"""
Site-wide search-and-replace for AI-writing tells per brand-steward audit Apr 21, 2026.

Runs across posts/*.html. Preserves CSS transform rules and any content inside
<style> or <script> blocks. Only touches body prose and JSON-LD string fields.

Usage:
    python3 scripts/humanize-tone.py [--dry-run]
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
POSTS = REPO / "posts"

# (pattern, replacement, case-insensitive)
# Patterns ordered longest-match-first to avoid partial overlaps.
REPLACEMENTS = [
    # Hype vocabulary (word boundaries to avoid substrings)
    (r"\brobust API\b", "API", False),
    (r"\brobust (integration|platform|solution|toolkit|workflow)\b", r"\1", False),
    (r"\bcomprehensive (guide|ranking|feature set|toolkit|analysis)\b", r"full \1", False),
    (r"\bseamless (integration|workflow|experience)\b", r"\1", False),
    (r"\bcutting-edge ", "", False),
    (r"\bincredibly powerful\b", "powerful", False),
    (r"\bextremely powerful\b", "powerful", False),
    (r"\btruly remarkable\b", "notable", False),
    (r"\bwide range of\b", "many", False),
    # Hype action verbs — only strip when clearly marketing voice, leave neutral uses
    (r"\btransform your (video|content|workflow|business)\b", r"upgrade your \1", False),
    (r"\btransform a script into\b", "turn a script into", False),
    (r"\btransform scripts into\b", "turn scripts into", False),
    # Filler openings (start of sentence, after period or opening tag)
    (r"(?<=[.!?>]\s)In today's (digital landscape|fast-paced world|AI-driven world),?\s*", "", False),
    (r"(?<=^)In today's (digital landscape|fast-paced world|AI-driven world),?\s*", "", True),
    (r"(?<=[.!?>]\s)When it comes to ", "For ", False),
    (r"(?<=[.!?>]\s)It's important to note that ", "", False),
    (r"\bLet's dive in[.!]?\s*", "", False),
    (r"\bdive into ", "go through ", False),
    (r"\bdelve into ", "go through ", False),
    # Transition crutches (start of sentence)
    (r"(?<=[.!?>]\s)Moreover,\s*", "", False),
    (r"(?<=[.!?>]\s)Furthermore,\s*", "", False),
    (r"(?<=[.!?>]\s)Additionally,\s*", "", False),
]


def should_skip_block(html, start):
    """Return True if position `start` is inside a <script>, <style>, or CSS block."""
    # Find the nearest preceding <script> or <style> opening tag
    preceding = html[:start].lower()
    last_script_open = preceding.rfind("<script")
    last_script_close = preceding.rfind("</script>")
    last_style_open = preceding.rfind("<style")
    last_style_close = preceding.rfind("</style>")
    if last_script_open > last_script_close:
        return True
    if last_style_open > last_style_close:
        return True
    return False


def apply_replacements(html, dry_run=False):
    """Apply all replacements. Returns (new_html, total_hits)."""
    total = 0
    new = html
    for pattern, replacement, ci in REPLACEMENTS:
        flags = re.IGNORECASE if ci else 0
        compiled = re.compile(pattern, flags)
        hits = 0

        # Build new string skipping matches inside script/style blocks
        out = []
        pos = 0
        for m in compiled.finditer(new):
            if should_skip_block(new, m.start()):
                continue
            out.append(new[pos:m.start()])
            out.append(m.expand(replacement) if "\\" in replacement else replacement)
            pos = m.end()
            hits += 1
        out.append(new[pos:])
        if hits > 0:
            new = "".join(out)
            total += hits
            if not dry_run:
                print(f"    {pattern!r}: {hits}")
    return new, total


def main():
    dry = "--dry-run" in sys.argv
    grand_total = 0
    touched = 0
    for post in sorted(POSTS.glob("*.html")):
        text = post.read_text(encoding="utf-8")
        new_text, hits = apply_replacements(text, dry)
        if hits > 0:
            print(f"{post.name}: {hits} replacement(s)")
            if not dry:
                post.write_text(new_text, encoding="utf-8")
            touched += 1
            grand_total += hits
    print(f"\n{'DRY-RUN: would change' if dry else 'Changed'} {touched} files, {grand_total} total replacements.")


if __name__ == "__main__":
    main()
