#!/usr/bin/env python3
"""Rewrite /go/<slug>/index.html redirects to fire GA4 affiliate_click event before redirect."""
import os, re, html
from pathlib import Path

GO = Path("/home/tom/ai-video-tools-blog/go")
GA = "G-M5NLTFV6FL"

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="robots" content="noindex,nofollow">
<title>Redirecting to {name}...</title>
<link rel="canonical" href="{url}">
<meta http-equiv="refresh" content="1;url={url}">
<script async src="https://www.googletagmanager.com/gtag/js?id={ga}"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', '{ga}', {{transport_type: 'beacon'}});
gtag('event', 'affiliate_click', {{
  event_category: 'affiliate',
  event_label: '{slug}',
  affiliate_partner: '{slug}',
  affiliate_url: '{url}',
  transport_type: 'beacon'
}});
setTimeout(function(){{ window.location.replace('{url_js}'); }}, 200);
</script>
</head><body>
<p>Redirecting to <a href="{url}" rel="nofollow sponsored">{name}</a>...</p>
</body></html>
"""

REFRESH_RE = re.compile(r'<meta http-equiv="refresh" content="0;url=([^"]+)">', re.I)
TITLE_RE = re.compile(r'<title>Redirecting to ([^<]+?)\.\.\.</title>', re.I)

updated = []
for d in sorted(GO.iterdir()):
    if not d.is_dir():
        continue
    f = d / "index.html"
    if not f.exists():
        continue
    src = f.read_text()
    m_url = REFRESH_RE.search(src)
    m_name = TITLE_RE.search(src)
    if not (m_url and m_name):
        print(f"SKIP {d.name}: cannot parse")
        continue
    url = html.unescape(m_url.group(1))
    name = m_name.group(1).strip()
    slug = d.name
    out = TEMPLATE.format(
        name=html.escape(name),
        url=html.escape(url, quote=True),
        url_js=url.replace("'", "\\'"),
        slug=slug,
        ga=GA,
    )
    f.write_text(out)
    updated.append(slug)

print(f"Updated {len(updated)} redirects: {', '.join(updated)}")
