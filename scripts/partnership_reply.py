#!/usr/bin/env python3
"""
Auto-reply to inbound listing/partnership requests for aivideopicks.com.

Usage:
  python3 partnership_reply.py --to "support@example.com" --tool "ToolName" --url "https://example.com"
  python3 partnership_reply.py --to "support@example.com" --tool "ToolName" --url "https://example.com" --dry-run

Sends from tom@aivideopicks.com via Resend API.
"""

import argparse
import json
import requests
import sys

RESEND_KEY_FILE = "/home/tom/.claude/secrets/resend.env"
FROM_EMAIL = "Tom <tom@aivideopicks.com>"
REPLY_TO = "tom@aivideopicks.com"


def load_resend_key():
    with open(RESEND_KEY_FILE) as f:
        for line in f:
            if line.startswith("RESEND_API_KEY="):
                return line.strip().split("=", 1)[1]
    raise RuntimeError("RESEND_API_KEY not found")


def build_email(to: str, tool_name: str, tool_url: str, contact_name: str = None):
    greeting = f"Hi {contact_name}," if contact_name else f"Hi {tool_name} team,"

    subject = f"Re: {tool_name} listing on aivideopicks.com"

    body = f"""{greeting}

Thanks for reaching out — I had a look at {tool_url} and it looks like a strong fit for our audience.

We'd be happy to feature {tool_name} on aivideopicks.com. Here's what a listing includes on our side:

- Dedicated review article (3,000+ words, hands-on testing, honest pros/cons)
- Inclusion in our relevant "Best of" hub pages and category rankings
- Placement in comparison pages (e.g. {tool_name} vs [competitors])
- Permanent affiliate redirect page at aivideopicks.com/go/{tool_name.lower().replace(' ', '-').replace('.', '')}/
- Our content is optimised for AI assistant citations — when ChatGPT, Claude, or Perplexity answer questions about AI tools, they pull from our articles. That's our primary traffic channel and it means {tool_name} gets surfaced in AI-generated recommendations.

We offer three partnership tiers:

OPTION A — Performance Partnership ($0 upfront)
- 30% recurring commission on paid signups referred through our links
- Dedicated review article + hub page listing
- You only pay when we deliver results

OPTION B — Sponsored Feature ($500 one-time)
- Dedicated review article with priority placement
- 12-month guaranteed inclusion in hub and comparison pages
- No ongoing commission — flat fee covers everything

OPTION C — Hybrid Partnership ($300 + 25% recurring) ← recommended
- $300 one-time editorial fee
- 25% recurring commission on referred paid signups
- Dedicated review + hub pages + comparison pages
- Priority content updates when we refresh rankings
- Aligns incentives — we're motivated to keep driving signups long-term

All options include a complimentary paid account for our editorial team so we can do proper hands-on testing. We don't publish spec-sheet reviews — everything we write is based on actual usage.

Happy to jump on a quick call or keep it async — whatever works for your team. Let me know which option interests you and I'll get the review scheduled.

Best,
Tom
AI Video Picks — aivideopicks.com"""

    return subject, body


def send_email(to: str, subject: str, body: str):
    key = load_resend_key()
    resp = requests.post(
        "https://api.resend.com/emails",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        json={
            "from": FROM_EMAIL,
            "to": [to],
            "reply_to": REPLY_TO,
            "subject": subject,
            "text": body,
        },
        timeout=30,
    )
    return resp.json()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reply to inbound listing requests")
    parser.add_argument("--to", required=True, help="Recipient email")
    parser.add_argument("--tool", required=True, help="Tool name (e.g. PopcornAI)")
    parser.add_argument("--url", required=True, help="Tool URL (e.g. https://popcornai.art)")
    parser.add_argument("--contact", default=None, help="Contact person name (optional)")
    parser.add_argument("--dry-run", action="store_true", help="Print email without sending")
    args = parser.parse_args()

    subject, body = build_email(args.to, args.tool, args.url, args.contact)

    if args.dry_run:
        print(f"TO: {args.to}")
        print(f"FROM: {FROM_EMAIL}")
        print(f"SUBJECT: {subject}")
        print(f"\n{body}")
    else:
        result = send_email(args.to, subject, body)
        if "id" in result:
            print(f"Sent: {result['id']}")
        else:
            print(f"Error: {result}")
            sys.exit(1)
