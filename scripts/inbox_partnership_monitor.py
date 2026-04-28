#!/usr/bin/env python3
"""
Scan Gmail for inbound listing/partnership/sponsorship requests to aivideopicks.com.
Logs new requests to a tracker file. Does NOT auto-reply — flags for review.

Run daily via cron or manually:
  python3 inbox_partnership_monitor.py

Requires: Gmail API access via Composio MCP (run from Claude Code session)
          OR manual scan via Gmail search: "to:tom@aivideopicks.com (listing OR review OR feature OR sponsor OR partnership OR submit)"

Tracker: /home/tom/ai-video-tools-blog/content/partnerships/inbox.json
"""

import json
import os
from datetime import datetime

TRACKER_FILE = "/home/tom/ai-video-tools-blog/content/partnerships/inbox.json"
os.makedirs(os.path.dirname(TRACKER_FILE), exist_ok=True)

GMAIL_SEARCH_QUERY = (
    "to:tom@aivideopicks.com "
    "(listing OR review OR feature OR sponsor OR partnership OR submit OR affiliate) "
    "newer_than:7d"
)


def load_tracker():
    if os.path.exists(TRACKER_FILE):
        with open(TRACKER_FILE) as f:
            return json.load(f)
    return {"processed": [], "pending": [], "replied": []}


def save_tracker(data):
    with open(TRACKER_FILE, "w") as f:
        json.dump(data, f, indent=2)


def add_request(sender: str, tool_name: str, tool_url: str, subject: str,
                thread_id: str = None, contact_name: str = None):
    """Manually add a partnership request to the tracker."""
    tracker = load_tracker()

    if any(r["sender"] == sender and r["tool_name"] == tool_name
           for r in tracker["pending"] + tracker["replied"]):
        print(f"Already tracked: {tool_name} from {sender}")
        return

    entry = {
        "sender": sender,
        "tool_name": tool_name,
        "tool_url": tool_url,
        "subject": subject,
        "contact_name": contact_name,
        "thread_id": thread_id,
        "received_date": datetime.now().strftime("%Y-%m-%d"),
        "status": "pending",
        "reply_date": None,
        "option_chosen": None,
        "notes": None,
    }
    tracker["pending"].append(entry)
    save_tracker(tracker)
    print(f"Added: {tool_name} ({sender}) — status: pending")


def mark_replied(sender: str, tool_name: str, option: str = None):
    """Mark a request as replied."""
    tracker = load_tracker()
    for i, r in enumerate(tracker["pending"]):
        if r["sender"] == sender or r["tool_name"] == tool_name:
            r["status"] = "replied"
            r["reply_date"] = datetime.now().strftime("%Y-%m-%d")
            r["option_chosen"] = option
            tracker["replied"].append(r)
            tracker["pending"].pop(i)
            save_tracker(tracker)
            print(f"Marked replied: {tool_name} — option: {option}")
            return
    print(f"Not found in pending: {tool_name}")


def status():
    """Print current partnership pipeline."""
    tracker = load_tracker()
    print(f"\n=== Partnership Pipeline ===")
    print(f"Pending: {len(tracker['pending'])}")
    for r in tracker["pending"]:
        print(f"  {r['tool_name']} ({r['sender']}) — received {r['received_date']}")
    print(f"Replied: {len(tracker['replied'])}")
    for r in tracker["replied"]:
        print(f"  {r['tool_name']} — option: {r['option_chosen']} — replied {r['reply_date']}")
    print()


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "status":
        status()
    else:
        print(f"Gmail search query for manual scan:")
        print(f"  {GMAIL_SEARCH_QUERY}")
        print()
        print("Usage:")
        print("  python3 inbox_partnership_monitor.py status")
        print()
        print("From Claude Code, use:")
        print("  mcp__claude_ai_Gmail__search_threads with query above")
        print("  Then: add_request() for each new match")
