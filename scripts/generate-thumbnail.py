#!/usr/bin/env python3
"""
Generate a branded 600x340 PNG thumbnail for an aivideopicks blog post.

Two-step workflow:
  1. Agent calls Figma MCP `use_figma` to clone the master template (1:2),
     overrides title/badge/color, and returns the new node ID.
  2. This script takes that node ID, exports the PNG via Figma REST API,
     and saves it to assets/images/<slug>-thumbnail.png.

Usage:
  python3 scripts/generate-thumbnail.py <node-id> <slug>
  # e.g. python3 scripts/generate-thumbnail.py 5:42 kling-3-review-2026

Reads token from ~/.claude/secrets/figma.env
"""
import os
import sys
import urllib.request
import json
from pathlib import Path

ENV_PATH = Path.home() / ".claude" / "secrets" / "figma.env"
REPO_ROOT = Path(__file__).resolve().parent.parent


def load_env():
    if not ENV_PATH.exists():
        sys.exit(f"Missing {ENV_PATH} — generate at https://www.figma.com/settings")
    env = {}
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
    return env


def export_node(token: str, file_key: str, node_id: str) -> bytes:
    api_url = f"https://api.figma.com/v1/images/{file_key}?ids={node_id}&format=png&scale=1"
    req = urllib.request.Request(api_url, headers={"X-Figma-Token": token})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    if data.get("err"):
        sys.exit(f"Figma API error: {data['err']}")
    s3_url = data["images"].get(node_id)
    if not s3_url:
        sys.exit(f"No image returned for node {node_id}")
    with urllib.request.urlopen(s3_url, timeout=30) as resp:
        return resp.read()


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: generate-thumbnail.py <node-id> <slug>")
    node_id, slug = sys.argv[1], sys.argv[2]
    env = load_env()
    token = env["FIGMA_TOKEN"]
    file_key = env["FIGMA_FILE_KEY"]

    png_bytes = export_node(token, file_key, node_id)
    out_path = REPO_ROOT / "assets" / "images" / f"{slug}-thumbnail.png"
    out_path.write_bytes(png_bytes)

    size_kb = len(png_bytes) // 1024
    print(f"Saved {out_path.relative_to(REPO_ROOT)} ({size_kb} KB)")


if __name__ == "__main__":
    main()
