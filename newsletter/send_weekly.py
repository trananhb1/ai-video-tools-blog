#!/usr/bin/env python3
"""
AI Video Picks — Weekly Newsletter Generator & Sender (Resend)

Scans recent posts, builds a branded HTML email, sends via Resend Batch API.
Run every Saturday: python3 newsletter/send_weekly.py

Env vars (or .env):
  RESEND_API_KEY   — Resend API key
  AUDIENCE_ID      — Resend audience ID
  DRY_RUN          — "true" to print email without sending
"""

import os, re, json, glob, datetime, textwrap
from pathlib import Path
from html.parser import HTMLParser

RESEND_API_KEY = os.environ["RESEND_API_KEY"]
AUDIENCE_ID = os.getenv("AUDIENCE_ID", "efccec02-9c7f-484e-99db-53319d9287dc")
DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"
SITE_URL = "https://aivideopicks.com"
FROM_EMAIL = "Tom from AI Video Picks <newsletter@aivideopicks.com>"
REPLY_TO = "trananhb1@gmail.com"
BLOG_DIR = Path(__file__).resolve().parent.parent / "posts"


class MetaExtractor(HTMLParser):
    """Extract title, description, og:image from a post HTML file."""
    def __init__(self):
        super().__init__()
        self.title = ""
        self.description = ""
        self.image = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            if d.get("property") == "og:description" or (d.get("name") == "description" and not self.description):
                self.description = d.get("content", "")
            elif d.get("property") == "og:image":
                self.image = d.get("content", "")

    def handle_data(self, data):
        if self._in_title:
            self.title += data

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False


def extract_post_meta(filepath: Path) -> dict:
    text = filepath.read_text(encoding="utf-8", errors="ignore")
    parser = MetaExtractor()
    parser.feed(text)

    date_match = re.search(r'datetime="(\d{4}-\d{2}-\d{2})"', text)
    pub_date = date_match.group(1) if date_match else None
    if not pub_date:
        date_match = re.search(r'Published:\s*(\w+ \d{1,2},\s*\d{4})', text)
        if date_match:
            try:
                pub_date = datetime.datetime.strptime(date_match.group(1), "%B %d, %Y").strftime("%Y-%m-%d")
            except ValueError:
                pub_date = None

    slug = filepath.stem
    return {
        "title": parser.title.split("|")[0].strip() if parser.title else slug,
        "description": parser.description,
        "image": parser.image or f"{SITE_URL}/assets/images/{slug}-thumbnail.png",
        "url": f"{SITE_URL}/posts/{filepath.name}",
        "date": pub_date,
        "slug": slug,
    }


def get_recent_posts(days=7) -> list:
    cutoff = (datetime.datetime.now() - datetime.timedelta(days=days)).strftime("%Y-%m-%d")
    posts = []
    for f in sorted(BLOG_DIR.glob("*.html")):
        meta = extract_post_meta(f)
        if meta["date"] and meta["date"] >= cutoff:
            posts.append(meta)
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def get_all_posts_sorted() -> list:
    posts = []
    for f in sorted(BLOG_DIR.glob("*.html")):
        meta = extract_post_meta(f)
        if meta["date"]:
            posts.append(meta)
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


AFFILIATE_PICKS = [
    {"name": "HeyGen", "url": "https://www.heygen.com/?via=aivideopicks", "tagline": "Best for marketing videos & avatars", "offer": "Free plan available", "color": "#6C5CE7", "icon": "HG"},
    {"name": "Synthesia", "url": "https://www.synthesia.io/?via=aivideopicks", "tagline": "Enterprise training & L&D", "offer": "160+ AI avatars, 130+ languages", "color": "#00B894", "icon": "Sy"},
    {"name": "Zebracat", "url": "https://studio.zebracat.ai/?via=aivideopicks", "tagline": "Fast social & ad video creation", "offer": "Use code 6YAZM9V5 for 15% off", "color": "#FDCB6E", "icon": "Zc"},
    {"name": "Pika", "url": "https://pika.style/?via=aivideopicks", "tagline": "Creative text-to-video generation", "offer": "Free tier available", "color": "#E17055", "icon": "Pk"},
    {"name": "Fliki", "url": "https://fliki.ai/?via=aivideopicks", "tagline": "Blog-to-video in minutes", "offer": "Free plan + paid from $28/mo", "color": "#0984E3", "icon": "Fk"},
    {"name": "Pictory", "url": "https://pictory.ai?ref=aivideopicks", "tagline": "Turn scripts & blogs into videos", "offer": "New 2.0 with AI avatars!", "color": "#A29BFE", "icon": "Pc"},
    {"name": "InVideo", "url": "https://invideo.sjv.io/aivideopicks", "tagline": "AI video editor for social content", "offer": "Free plan available", "color": "#00CEC9", "icon": "IV"},
    {"name": "Creatify", "url": "https://app.creatify.ai/?via=Aivideopicks", "tagline": "AI ad video generator", "offer": "$49 off first month", "color": "#FF7675", "icon": "Cr"},
]


def build_post_card(post: dict) -> str:
    utm = "?utm_source=newsletter&utm_medium=email&utm_campaign=weekly"
    return f"""
    <tr><td style="padding:0 0 20px 0;">
      <table width="100%" cellpadding="0" cellspacing="0" style="background:#f8f9fc;border-radius:12px;overflow:hidden;">
        <tr><td>
          <a href="{post['url']}{utm}">
            <img src="{post['image']}" alt="{post['title']}" width="552" style="width:100%;height:auto;display:block;border-radius:12px 12px 0 0;" />
          </a>
        </td></tr>
        <tr><td style="padding:20px 24px 24px;">
          <a href="{post['url']}{utm}" style="color:#155DFC;font-size:18px;font-weight:700;text-decoration:none;line-height:1.3;">{post['title']}</a>
          <p style="color:#4a4a68;font-size:14px;line-height:1.5;margin:8px 0 16px;">{post['description'][:150]}{'...' if len(post['description']) > 150 else ''}</p>
          <a href="{post['url']}{utm}" style="display:inline-block;background:#155DFC;color:#ffffff;font-size:13px;font-weight:700;padding:10px 24px;border-radius:6px;text-decoration:none;">Read More →</a>
        </td></tr>
      </table>
    </td></tr>"""


def _utm(url: str) -> str:
    sep = "&" if "?" in url else "?"
    return f"{url}{sep}utm_source=newsletter&utm_medium=email&utm_campaign=weekly"


def build_affiliate_section() -> str:
    import random
    picks = random.sample(AFFILIATE_PICKS, min(4, len(AFFILIATE_PICKS)))
    rows = ""
    for p in picks:
        rows += f"""
        <tr><td style="padding:6px 0;">
          <table width="100%" cellpadding="0" cellspacing="0" style="background:#ffffff;border:1px solid #e2e4eb;border-radius:10px;">
            <tr>
              <td width="56" style="padding:14px 0 14px 14px;vertical-align:middle;">
                <div style="width:44px;height:44px;border-radius:10px;background:{p['color']};text-align:center;line-height:44px;color:#ffffff;font-size:16px;font-weight:800;">{p['icon']}</div>
              </td>
              <td style="padding:14px 16px;vertical-align:middle;">
                <a href="{_utm(p['url'])}" style="color:#155DFC;font-size:15px;font-weight:700;text-decoration:none;">{p['name']}</a>
                <span style="color:#4a4a68;font-size:13px;"> — {p['tagline']}</span>
                <p style="color:#7a7a96;font-size:12px;margin:4px 0 0;">{p['offer']}</p>
              </td>
              <td width="80" style="padding:14px 14px 14px 0;vertical-align:middle;text-align:right;">
                <a href="{_utm(p['url'])}" style="display:inline-block;background:#f0f2f5;color:#155DFC;font-size:12px;font-weight:700;padding:6px 12px;border-radius:6px;text-decoration:none;">Try Free →</a>
              </td>
            </tr>
          </table>
        </td></tr>"""
    return rows


def build_email_html(recent_posts: list, all_posts: list) -> str:
    today = datetime.datetime.now()
    week_label = today.strftime("%B %d, %Y")
    issue_num = (today - datetime.datetime(2026, 5, 1)).days // 7 + 1

    post_cards = ""
    if recent_posts:
        for p in recent_posts[:5]:
            post_cards += build_post_card(p)
    else:
        for p in all_posts[:3]:
            post_cards += build_post_card(p)

    affiliate_rows = build_affiliate_section()

    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
<body style="margin:0;padding:0;background:#f0f2f5;font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f0f2f5;padding:20px 0;">
<tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;">

  <!-- Header -->
  <tr><td style="background:linear-gradient(135deg,#155DFC 0%,#1a1a2e 100%);padding:32px 24px;border-radius:12px 12px 0 0;text-align:center;">
    <h1 style="color:#ffffff;font-size:22px;font-weight:800;margin:0;">AI Video <span style="color:#60a5fa;">Picks</span></h1>
    <p style="color:#94a3b8;font-size:13px;margin:8px 0 0;">Weekly Digest — Issue #{issue_num} · {week_label}</p>
  </td></tr>

  <!-- Intro -->
  <tr><td style="background:#ffffff;padding:28px 24px 16px;">
    <p style="color:#1a1a2e;font-size:15px;line-height:1.6;margin:0;">Hey there! 👋</p>
    <p style="color:#4a4a68;font-size:14px;line-height:1.6;margin:12px 0 0;">Here's what's new in AI video this week — fresh reviews, tutorials, and the tools worth your time.</p>
  </td></tr>

  <!-- This Week's Posts -->
  <tr><td style="background:#ffffff;padding:8px 24px 0;">
    <h2 style="color:#1a1a2e;font-size:16px;font-weight:700;margin:0 0 16px;padding-bottom:8px;border-bottom:2px solid #155DFC;">{'This Week on the Blog' if recent_posts else 'Top Picks for You'}</h2>
  </td></tr>
  <tr><td style="background:#ffffff;padding:0 24px;">
    <table width="100%" cellpadding="0" cellspacing="0">
      {post_cards}
    </table>
  </td></tr>

  <!-- Affiliate Picks -->
  <tr><td style="background:#ffffff;padding:8px 24px;">
    <h2 style="color:#1a1a2e;font-size:16px;font-weight:700;margin:0 0 12px;padding-bottom:8px;border-bottom:2px solid #155DFC;">Tools Worth Checking Out</h2>
    <table width="100%" cellpadding="0" cellspacing="0">
      {affiliate_rows}
    </table>
  </td></tr>

  <!-- CTA -->
  <tr><td style="background:#ffffff;padding:20px 24px 28px;text-align:center;">
    <a href="{SITE_URL}?utm_source=newsletter&utm_medium=email&utm_campaign=weekly" style="display:inline-block;background:#155DFC;color:#ffffff;font-size:14px;font-weight:700;padding:12px 32px;border-radius:8px;text-decoration:none;">Browse All Reviews →</a>
  </td></tr>

  <!-- Footer -->
  <tr><td style="background:#1a1a2e;padding:24px;border-radius:0 0 12px 12px;text-align:center;">
    <p style="color:#94a3b8;font-size:12px;line-height:1.6;margin:0;">You're receiving this because you subscribed at <a href="{SITE_URL}" style="color:#60a5fa;">aivideopicks.com</a>.</p>
    <p style="color:#94a3b8;font-size:12px;margin:8px 0 0;"><a href="{{{{RESEND_UNSUBSCRIBE_URL}}}}" style="color:#60a5fa;">Unsubscribe</a> · <a href="{SITE_URL}/legal/privacy.html" style="color:#60a5fa;">Privacy</a> · <a href="{SITE_URL}/legal/ftc-disclosure.html" style="color:#60a5fa;">FTC Disclosure</a></p>
    <p style="color:#64748b;font-size:11px;margin:12px 0 0;">AI Video Picks · aivideopicks.com</p>
  </td></tr>

</table>
</td></tr>
</table>
</body>
</html>"""


def get_contacts() -> list:
    import urllib.request
    req = urllib.request.Request(
        f"https://api.resend.com/audiences/{AUDIENCE_ID}/contacts",
        headers={"Authorization": f"Bearer {RESEND_API_KEY}"}
    )
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
    return [c for c in data.get("data", []) if not c.get("unsubscribed")]


def send_broadcast(html: str, subject: str, contacts: list):
    import urllib.request
    emails = [{"from": FROM_EMAIL, "to": [c["email"]], "reply_to": REPLY_TO,
               "subject": subject, "html": html,
               "headers": {"List-Unsubscribe": "{{RESEND_UNSUBSCRIBE_URL}}"}}
              for c in contacts]

    # Resend batch API: max 100 per call
    for i in range(0, len(emails), 100):
        batch = emails[i:i+100]
        body = json.dumps(batch).encode()
        req = urllib.request.Request(
            "https://api.resend.com/emails/batch",
            data=body,
            headers={
                "Authorization": f"Bearer {RESEND_API_KEY}",
                "Content-Type": "application/json",
            },
            method="POST"
        )
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read())
            print(f"Batch {i//100+1}: sent {len(batch)} emails — {result}")


def main():
    recent = get_recent_posts(days=7)
    all_posts = get_all_posts_sorted()

    print(f"Found {len(recent)} posts from last 7 days, {len(all_posts)} total")

    html = build_email_html(recent, all_posts)
    today = datetime.datetime.now()
    subject = f"AI Video Weekly #{(today - datetime.datetime(2026, 5, 1)).days // 7 + 1}: {len(recent) if recent else len(all_posts[:3])} New {'Posts' if len(recent) != 1 else 'Post'} This Week"

    if DRY_RUN:
        preview_path = Path(__file__).parent / "preview.html"
        preview_path.write_text(html)
        print(f"DRY RUN — preview saved to {preview_path}")
        print(f"Subject: {subject}")
        return

    contacts = get_contacts()
    print(f"Sending to {len(contacts)} subscribers")

    if not contacts:
        print("No subscribers yet — skipping send")
        return

    send_broadcast(html, subject, contacts)
    print("Newsletter sent!")


if __name__ == "__main__":
    main()
