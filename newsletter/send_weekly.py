#!/usr/bin/env python3
"""
AI Video Picks — Weekly Newsletter Generator & Sender

Two send modes:
  1. Personalized (default): POST to Worker /admin/send-personalized
     - Worker handles per-subscriber click tracking + affiliate personalization
     - Requires WORKER_URL and ADMIN_TOKEN env vars
  2. Direct Resend: POST to Resend batch API (fallback if Worker is down)
     - Requires RESEND_API_KEY env var

Run every Saturday: python3 newsletter/send_weekly.py
Env vars (or .env):
  WORKER_URL     — Newsletter worker URL (default: aivideopicks-newsletter.trananhb1.workers.dev)
  ADMIN_TOKEN    — Worker admin bearer token
  RESEND_API_KEY — Resend API key (only needed for direct mode)
  AUDIENCE_ID    — Resend audience ID
  DRY_RUN        — "true" to save preview without sending
  SEND_MODE      — "personalized" (default) or "direct"
"""

import os, re, json, datetime
from pathlib import Path
from html.parser import HTMLParser

WORKER_URL = os.getenv("WORKER_URL", "https://aivideopicks-newsletter.trananhb1.workers.dev")
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "")
RESEND_API_KEY = os.getenv("RESEND_API_KEY", "")
AUDIENCE_ID = os.getenv("AUDIENCE_ID", "efccec02-9c7f-484e-99db-53319d9287dc")
DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"
SEND_MODE = os.getenv("SEND_MODE", "personalized")
SITE_URL = "https://aivideopicks.com"
FROM_EMAIL = "Tom from AI Video Picks <newsletter@aivideopicks.com>"
REPLY_TO = "trananhb1@gmail.com"
BLOG_DIR = Path(__file__).resolve().parent.parent / "posts"


class MetaExtractor(HTMLParser):
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


def _utm(url: str) -> str:
    sep = "&" if "?" in url else "?"
    return f"{url}{sep}utm_source=newsletter&utm_medium=email&utm_campaign=weekly"


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


def build_subject(recent: list, all_posts: list) -> str:
    posts = recent if recent else all_posts[:3]
    if not posts:
        return "This week in AI video tools"
    lead = posts[0]["title"].split(":")[0].split("|")[0].strip()
    others = len(posts) - 1
    if others > 0:
        return f"{lead} + {others} more reviews"
    return lead


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
    <p style="color:#1a1a2e;font-size:15px;line-height:1.6;margin:0;">Hey {{{{NAME}}}}! 👋</p>
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

  <!-- Affiliate Picks (personalized by worker) -->
  <tr><td style="background:#ffffff;padding:8px 24px;">
    <h2 style="color:#1a1a2e;font-size:16px;font-weight:700;margin:0 0 12px;padding-bottom:8px;border-bottom:2px solid #155DFC;">Recommended for You</h2>
    <table width="100%" cellpadding="0" cellspacing="0">
      {{{{AFFILIATE_SECTION}}}}
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


def send_personalized(html_template: str, subject: str, test_email: str = None):
    import urllib.request
    payload = {"subject": subject, "html_template": html_template}
    if test_email:
        payload["test_email"] = test_email

    body = json.dumps(payload).encode()
    req = urllib.request.Request(
        f"{WORKER_URL}/admin/send-personalized",
        data=body,
        headers={
            "Authorization": f"Bearer {ADMIN_TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "AIVideoPicksNewsletter/1.0",
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read())
            print(f"Personalized send: {result}")
    except urllib.request.HTTPError as e:
        error_body = e.read().decode() if e.fp else "no body"
        print(f"HTTP {e.code}: {error_body}")
        raise


def send_direct(html: str, subject: str):
    import urllib.request
    payload = {"subject": subject, "html": html}
    body = json.dumps(payload).encode()
    req = urllib.request.Request(
        f"{WORKER_URL}/admin/send",
        data=body,
        headers={
            "Authorization": f"Bearer {ADMIN_TOKEN}",
            "Content-Type": "application/json",
        },
        method="POST"
    )
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
        print(f"Direct send: {result}")


def main():
    recent = get_recent_posts(days=7)
    all_posts = get_all_posts_sorted()

    print(f"Found {len(recent)} posts from last 7 days, {len(all_posts)} total")

    html = build_email_html(recent, all_posts)
    subject = build_subject(recent, all_posts)

    if DRY_RUN:
        preview_path = Path(__file__).parent / "preview.html"
        preview_path.write_text(html)
        print(f"DRY RUN — preview saved to {preview_path}")
        print(f"Subject: {subject}")
        return

    if SEND_MODE == "personalized":
        print("Sending personalized newsletter via worker...")
        send_personalized(html, subject)
    else:
        print("Sending direct newsletter via worker...")
        send_direct(html, subject)

    print("Newsletter sent!")


if __name__ == "__main__":
    main()
