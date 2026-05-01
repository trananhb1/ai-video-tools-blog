#!/usr/bin/env python3
"""
AI Video Picks — Welcome Email Sender (Resend)

Called by the Cloudflare Worker after a new subscriber is added.
Can also be run standalone: python3 newsletter/send_welcome.py <email> [first_name]
"""

import os, sys, json, urllib.request

RESEND_API_KEY = os.getenv("RESEND_API_KEY", "re_KmjrEgRS_Cn9jtt4CGxgRpzE8SG5wmYrW")
SITE_URL = "https://aivideopicks.com"
FROM_EMAIL = "Tom from AI Video Picks <newsletter@aivideopicks.com>"
REPLY_TO = "trananhb1@gmail.com"


def build_welcome_html(first_name: str) -> str:
    name = first_name or "there"
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
<body style="margin:0;padding:0;background:#f0f2f5;font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f0f2f5;padding:20px 0;">
<tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;">

  <tr><td style="background:linear-gradient(135deg,#155DFC 0%,#1a1a2e 100%);padding:32px 24px;border-radius:12px 12px 0 0;text-align:center;">
    <h1 style="color:#ffffff;font-size:22px;font-weight:800;margin:0;">AI Video <span style="color:#60a5fa;">Hub</span></h1>
    <p style="color:#94a3b8;font-size:13px;margin:8px 0 0;">Welcome to AI Video Picks!</p>
  </td></tr>

  <tr><td style="background:#ffffff;padding:28px 24px;">
    <p style="color:#1a1a2e;font-size:16px;line-height:1.6;margin:0;">Hey {name}! 👋</p>
    <p style="color:#4a4a68;font-size:14px;line-height:1.7;margin:16px 0;">Welcome to <strong>AI Video Picks</strong> — your weekly shortcut to the best AI video tools, tips, and honest reviews.</p>

    <p style="color:#4a4a68;font-size:14px;line-height:1.7;margin:16px 0;">Here's what you'll get from me:</p>
    <ul style="color:#4a4a68;font-size:14px;line-height:1.8;padding-left:20px;">
      <li><strong>Weekly digest</strong> — new reviews, tutorials, and trending tools every weekend</li>
      <li><strong>Honest takes</strong> — what works, what's overhyped, and what's worth your money</li>
      <li><strong>Exclusive deals</strong> — discount codes I negotiate with tools I actually recommend</li>
    </ul>

    <h3 style="color:#1a1a2e;font-size:15px;margin:24px 0 12px;">Your quick win for today</h3>
    <p style="color:#4a4a68;font-size:14px;line-height:1.7;">If you're trying to figure out which AI video tool to use, start here — I put together a detailed comparison of the biggest players:</p>

    <table cellpadding="0" cellspacing="0" style="margin:20px 0;"><tr><td>
      <a href="{SITE_URL}/posts/best-ai-video-tools-2026.html?utm_source=welcome&utm_medium=email" style="display:inline-block;background:#155DFC;color:#ffffff;font-size:14px;font-weight:700;padding:12px 28px;border-radius:8px;text-decoration:none;">Read the Top 10 Comparison →</a>
    </td></tr></table>

    <p style="color:#4a4a68;font-size:14px;line-height:1.7;">Or if you're brand new to AI video, this step-by-step tutorial gets you from zero to your first video in 10 minutes:</p>

    <table cellpadding="0" cellspacing="0" style="margin:20px 0;"><tr><td>
      <a href="{SITE_URL}/posts/how-to-create-ai-videos-heygen.html?utm_source=welcome&utm_medium=email" style="display:inline-block;background:#ffffff;color:#155DFC;font-size:14px;font-weight:700;padding:10px 28px;border-radius:8px;text-decoration:none;border:2px solid #155DFC;">Create Your First AI Video →</a>
    </td></tr></table>

    <p style="color:#4a4a68;font-size:14px;line-height:1.7;margin:20px 0 0;">Hit reply and tell me what you're hoping to create with AI video — I read every response and it helps me send you the most relevant stuff.</p>

    <p style="color:#1a1a2e;font-size:14px;margin:24px 0 0;">Talk soon,<br><strong>Tom</strong><br><span style="color:#7a7a96;">AI Video Picks</span></p>
  </td></tr>

  <tr><td style="background:#1a1a2e;padding:20px 24px;border-radius:0 0 12px 12px;text-align:center;">
    <p style="color:#94a3b8;font-size:12px;margin:0;"><a href="{SITE_URL}" style="color:#60a5fa;">aivideopicks.com</a> · <a href="{{{{RESEND_UNSUBSCRIBE_URL}}}}" style="color:#60a5fa;">Unsubscribe</a></p>
  </td></tr>

</table>
</td></tr>
</table>
</body>
</html>"""


def send_welcome(email: str, first_name: str = ""):
    html = build_welcome_html(first_name)
    payload = json.dumps({
        "from": FROM_EMAIL,
        "to": [email],
        "reply_to": REPLY_TO,
        "subject": "Welcome to AI Video Picks — here's your first win",
        "html": html,
    }).encode()

    req = urllib.request.Request(
        "https://api.resend.com/emails",
        data=payload,
        headers={
            "Authorization": f"Bearer {RESEND_API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST"
    )
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
        print(f"Welcome email sent to {email}: {result}")
    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 send_welcome.py <email> [first_name]")
        sys.exit(1)
    email = sys.argv[1]
    name = sys.argv[2] if len(sys.argv) > 2 else ""
    send_welcome(email, name)
