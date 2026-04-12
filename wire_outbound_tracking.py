#!/usr/bin/env python3
"""Inject a delegated outbound-click tracker into every /posts/*.html page (idempotent).

Fires gtag('event','affiliate_click', ...) on click of any anchor whose href is
external OR points to /go/<slug>/ — covers both routed and direct affiliate links.
"""
from pathlib import Path
import re

POSTS = Path("/home/tom/ai-video-tools-blog/posts")
MARK = "/* AVP_OUTBOUND_TRACKER_v1 */"

SNIPPET = f"""<script>
{MARK}
(function(){{
  if (typeof gtag !== 'function') return;
  document.addEventListener('click', function(e){{
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var isGo = href.indexOf('/go/') === 0 || href.indexOf('https://aivideopicks.com/go/') === 0;
    var isExt = /^https?:\\/\\//.test(href) && href.indexOf('aivideopicks.com') === -1;
    if (!isGo && !isExt) return;
    var slug = '';
    var m = href.match(/\\/go\\/([^\\/?#]+)/);
    if (m) slug = m[1];
    else try {{ slug = (new URL(href)).hostname.replace(/^www\\./,''); }} catch(_) {{ slug = href.slice(0,80); }}
    gtag('event','affiliate_click', {{
      event_category: 'affiliate',
      event_label: slug,
      affiliate_partner: slug,
      affiliate_url: href,
      link_text: (a.innerText||'').trim().slice(0,80),
      page_path: location.pathname,
      transport_type: 'beacon'
    }});
  }}, true);
}})();
</script>
"""

INSERT_AFTER = re.compile(r"(gtag\('config',\s*'G-M5NLTFV6FL'[^)]*\);\s*</script>)", re.I)

count = 0
skipped = 0
for f in sorted(POSTS.glob("*.html")):
    src = f.read_text()
    if MARK in src:
        skipped += 1
        continue
    if not INSERT_AFTER.search(src):
        print(f"NO_GTAG_CONFIG: {f.name}")
        continue
    new_src = INSERT_AFTER.sub(lambda m: m.group(1) + "\n" + SNIPPET, src, count=1)
    f.write_text(new_src)
    count += 1

print(f"Injected into {count} posts; {skipped} already had tracker.")
