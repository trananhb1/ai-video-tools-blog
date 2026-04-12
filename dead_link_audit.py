#!/usr/bin/env python3
"""Audit internal links in posts/, index.html, landing/. Report any href that
points to a missing local file or anchor target."""
import re
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT = Path("/home/tom/ai-video-tools-blog")
HREF = re.compile(r'href=["\']([^"\']+)["\']', re.I)

def is_local(href):
    if not href: return False
    if href.startswith(("http://", "https://", "mailto:", "tel:", "javascript:", "#")): return False
    return True

def resolve(src_file: Path, href: str) -> Path | None:
    href = unquote(href.split("#")[0].split("?")[0])
    if not href: return None
    if href.startswith("/"):
        target = ROOT / href.lstrip("/")
    else:
        target = (src_file.parent / href).resolve()
    return target

bad = []
files = list((ROOT / "posts").glob("*.html")) + [ROOT / "index.html", ROOT / "about.html", ROOT / "contact.html"]
files += list((ROOT / "landing").glob("*.html"))
files = [f for f in files if f.exists()]

for f in files:
    src = f.read_text(errors="ignore")
    for href in HREF.findall(src):
        if not is_local(href): continue
        target = resolve(f, href)
        if target is None: continue
        # if it points at a directory, treat as <dir>/index.html
        if target.is_dir():
            target = target / "index.html"
        if not target.exists():
            bad.append((f.relative_to(ROOT), href))

if not bad:
    print("OK — 0 broken internal links across", len(files), "files.")
else:
    print(f"BROKEN: {len(bad)} links across {len(files)} files")
    for src, href in bad:
        print(f"  {src}  ->  {href}")
