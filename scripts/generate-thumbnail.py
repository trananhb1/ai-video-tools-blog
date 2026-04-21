#!/usr/bin/env python3
"""
Generate a branded 600x340 PNG thumbnail for an aivideopicks blog post.

Pure Python (Pillow + Inter font bundled in scripts/fonts/) — no external API.
Mirrors the Figma master template at file wjQh4PNW6yeK10rhprpxCM, node 1:2.

Usage (CLI):
  python3 scripts/generate-thumbnail.py \\
      --slug sora-alternatives \\
      --title "Sora Shutting Down: 7 Best Alternatives" \\
      --badge URGENT \\
      --tools HeyGen Synthesia Kling Runway Pika Fliki Zebracat

Usage (Python):
  from scripts.generate_thumbnail import render
  render(slug="kling-3-review-2026", title="Kling AI 3.0 Review",
         badge="REVIEW", tools=["Kling"])
"""
import argparse
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = Path(__file__).resolve().parent.parent
FONTS_DIR = Path(__file__).resolve().parent / "fonts"
LOGOS_DIR = Path(__file__).resolve().parent / "logos"
FONT_BOLD = str(FONTS_DIR / "Inter-Bold.ttf")
FONT_SEMI = str(FONTS_DIR / "Inter-SemiBold.ttf")

W, H = 600, 340

# Brand palette (matches CSS in repo + Figma master)
NAVY = (21, 25, 46)             # #15192e
BLUE = (22, 93, 252)            # #155DFC
RED = (220, 38, 38)             # #dc2626
YELLOW = (245, 197, 24)         # #f5c518
ORANGE = (249, 115, 22)         # #f97316
PURPLE = (147, 51, 234)         # #9333ea
GREEN = (34, 197, 94)           # #22c55e
WHITE = (255, 255, 255)

# Badge -> (background color, text color) and accompanying gradient end color
BADGE_PRESETS = {
    "REVIEW":     {"bg": YELLOW,  "fg": NAVY,  "grad": BLUE},
    "COMPARISON": {"bg": BLUE,    "fg": WHITE, "grad": BLUE},
    "GUIDE":      {"bg": GREEN,   "fg": WHITE, "grad": (16, 110, 90)},
    "URGENT":     {"bg": RED,     "fg": WHITE, "grad": RED},
    "DEAL":       {"bg": ORANGE,  "fg": WHITE, "grad": ORANGE},
    "NEW":        {"bg": PURPLE,  "fg": WHITE, "grad": PURPLE},
    "TUTORIAL":   {"bg": (14, 165, 233), "fg": WHITE, "grad": BLUE},
}

# Tool logo chip colors (background, text). Approximate brand palettes.
TOOL_CHIPS = {
    "HeyGen":     {"bg": (100, 64, 245),  "fg": WHITE},
    "Synthesia":  {"bg": (247, 57, 57),   "fg": WHITE},
    "Kling":      {"bg": (15, 15, 20),    "fg": WHITE},
    "Runway":     {"bg": (15, 15, 20),    "fg": WHITE},
    "Pika":       {"bg": (66, 59, 244),   "fg": WHITE},
    "Fliki":      {"bg": (0, 126, 248),   "fg": WHITE},
    "Zebracat":   {"bg": (0, 0, 0),       "fg": WHITE},
    "Pictory":    {"bg": (58, 127, 241),  "fg": WHITE},
    "Submagic":   {"bg": (115, 73, 243),  "fg": WHITE},
    "Movavi":     {"bg": (102, 180, 0),   "fg": WHITE},
    "Vidnoz":     {"bg": (251, 79, 79),   "fg": WHITE},
    "Arcads":     {"bg": NAVY,            "fg": WHITE},
    "MakeUGC":    {"bg": (15, 15, 20),    "fg": WHITE},
    "Descript":   {"bg": (87, 96, 241),   "fg": WHITE},
    "Veo":        {"bg": (66, 133, 244),  "fg": WHITE},
    "Sora":       {"bg": (15, 15, 20),    "fg": WHITE},
    "ElevenLabs": {"bg": (15, 15, 20),    "fg": WHITE},
    "InVideo":    {"bg": (255, 80, 76),   "fg": WHITE},
    "Veed":       {"bg": (159, 76, 244),  "fg": WHITE},
    "CapCut":     {"bg": (0, 0, 0),       "fg": WHITE},
    "OpusClip":   {"bg": (0, 199, 130),   "fg": WHITE},
    "Hedra":      {"bg": (255, 100, 50),  "fg": WHITE},
    "Arcads":     {"bg": NAVY,            "fg": WHITE},
}


def make_gradient(end_color):
    img = Image.new("RGBA", (W, H), NAVY)
    draw = ImageDraw.Draw(img)
    # Diagonal gradient: blend NAVY to end_color across the diagonal
    for y in range(H):
        for x in range(W):
            t = (x * 0.6 + y * 0.6) / (W * 0.6 + H * 0.6)
            r = int(NAVY[0] + (end_color[0] - NAVY[0]) * t)
            g = int(NAVY[1] + (end_color[1] - NAVY[1]) * t)
            b = int(NAVY[2] + (end_color[2] - NAVY[2]) * t)
            draw.point((x, y), (r, g, b))
    return img


def make_gradient_fast(end_color):
    """Vectorized linear gradient for speed (~50x faster than per-pixel)."""
    import numpy as np
    nx = np.linspace(0, 1, W).reshape(1, W)
    ny = np.linspace(0, 1, H).reshape(H, 1)
    t = np.clip((nx * 0.6 + ny * 0.6) / 1.2, 0, 1)
    r = (NAVY[0] + (end_color[0] - NAVY[0]) * t).astype("uint8")
    g = (NAVY[1] + (end_color[1] - NAVY[1]) * t).astype("uint8")
    b = (NAVY[2] + (end_color[2] - NAVY[2]) * t).astype("uint8")
    a = np.full_like(r, 255)
    arr = np.dstack([r, g, b, a])
    return Image.fromarray(arr, "RGBA")


def gradient(end_color):
    try:
        return make_gradient_fast(end_color)
    except ImportError:
        return make_gradient(end_color)


def draw_circle_accent(img):
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.ellipse((380, -100, 660, 180), fill=(255, 255, 255, 15))
    return Image.alpha_composite(img, overlay)


def draw_logo(draw):
    font = ImageFont.truetype(FONT_BOLD, 14)
    # Track letter-spacing manually via per-char draw
    text = "AI VIDEO HUB"
    x = 32
    y = 28
    for ch in text:
        draw.text((x, y), ch, font=font, fill=YELLOW)
        bbox = draw.textbbox((0, 0), ch, font=font)
        x += (bbox[2] - bbox[0]) + 1.5


def draw_badge(img, badge_text, bg, fg):
    bw, bh = 100, 28
    bx = W - bw - 32
    by = 24
    badge_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    bd = ImageDraw.Draw(badge_layer)
    bd.rounded_rectangle((bx, by, bx + bw, by + bh), radius=14, fill=bg)
    font = ImageFont.truetype(FONT_BOLD, 11)
    tb = bd.textbbox((0, 0), badge_text, font=font)
    tw = tb[2] - tb[0]
    th = tb[3] - tb[1]
    tx = bx + (bw - tw) // 2
    ty = by + (bh - th) // 2 - 1
    bd.text((tx, ty), badge_text, font=font, fill=fg)
    return Image.alpha_composite(img, badge_layer)


def wrap_title(title, font, max_width):
    words = title.split()
    lines = []
    cur = ""
    dummy = Image.new("RGB", (10, 10))
    dd = ImageDraw.Draw(dummy)
    for w in words:
        cand = (cur + " " + w).strip()
        bb = dd.textbbox((0, 0), cand, font=font)
        if bb[2] - bb[0] <= max_width:
            cur = cand
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines[:3]


def draw_title(draw, title):
    # Try 32px first; if 4+ lines, drop to 28; if still too long, drop to 24
    for size in (32, 28, 24):
        font = ImageFont.truetype(FONT_BOLD, size)
        lines = wrap_title(title, font, W - 64)
        if len(lines) <= 3:
            break
    line_h = int(size * 1.15)
    y = 80
    for line in lines:
        draw.text((32, y), line, font=font, fill=WHITE)
        y += line_h


def slug_for_tool(tool):
    """Map display name to icon filename."""
    return {
        "OpusClip": "opus",
        "Veo": "veo",
        "Sora": "sora",
    }.get(tool, tool.lower())


def draw_chip_strip(img, tools):
    """Render a row of icon chips: white rounded square + brand icon centered + small label below."""
    if not tools:
        return img
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    font = ImageFont.truetype(FONT_BOLD, 10)

    chip_w, chip_h = 56, 56          # white square
    icon_size = 38                   # icon inside
    label_y_offset = 4               # gap between chip and text label
    gap = 10
    y = 218

    n = min(len(tools), 7)
    total = n * chip_w + (n - 1) * gap
    x = (W - total) // 2             # center the strip horizontally

    for tool in tools[:7]:
        # White rounded chip background
        ld.rounded_rectangle((x, y, x + chip_w, y + chip_h), radius=10, fill=(255, 255, 255, 245))
        # Subtle border
        ld.rounded_rectangle((x, y, x + chip_w, y + chip_h), radius=10, outline=(0, 0, 0, 25), width=1)
        # Icon centered
        icon_path = LOGOS_DIR / f"{slug_for_tool(tool)}.png"
        if icon_path.exists():
            icon = Image.open(icon_path).convert("RGBA")
            icon.thumbnail((icon_size, icon_size), Image.LANCZOS)
            ix = x + (chip_w - icon.width) // 2
            iy = y + (chip_h - icon.height) // 2
            layer.paste(icon, (ix, iy), icon)
        else:
            # Fallback: brand color circle with first letter
            cfg = TOOL_CHIPS.get(tool, {"bg": NAVY, "fg": WHITE})
            ld.ellipse((x + 8, y + 8, x + chip_w - 8, y + chip_h - 8), fill=cfg["bg"])
            init_font = ImageFont.truetype(FONT_BOLD, 18)
            bb = ld.textbbox((0, 0), tool[0], font=init_font)
            tw = bb[2] - bb[0]
            th = bb[3] - bb[1]
            ld.text((x + (chip_w - tw) // 2, y + (chip_h - th) // 2 - 2), tool[0],
                    font=init_font, fill=cfg["fg"])
        # Text label below
        bb = ld.textbbox((0, 0), tool, font=font)
        tw = bb[2] - bb[0]
        ld.text((x + (chip_w - tw) // 2, y + chip_h + label_y_offset), tool,
                font=font, fill=(255, 255, 255, 230))
        x += chip_w + gap
    return Image.alpha_composite(img, layer)


def draw_footer(img):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    fd = ImageDraw.Draw(layer)
    font = ImageFont.truetype(FONT_SEMI, 14)
    fd.text((32, 290), "aivideopicks.com", font=font, fill=(255, 255, 255, 217))
    fd.rounded_rectangle((508, 296, 568, 300), radius=2, fill=YELLOW)
    return Image.alpha_composite(img, layer)


def draw_stars(layer, cx, y, rating_5, size=22, gap=4):
    """Draw 5 stars centered on cx with `rating_5` filled (0-5, fractional ok).
    Yellow filled portion + dark unfilled outline."""
    ld = ImageDraw.Draw(layer)
    n = 5
    total_w = n * size + (n - 1) * gap
    start_x = cx - total_w // 2
    for i in range(n):
        x = start_x + i * (size + gap)
        fill_amount = max(0, min(1, rating_5 - i))  # fraction of this star to fill
        # Background star (unfilled, dark)
        _draw_star(ld, x, y, size, fill=(255, 255, 255, 60))
        if fill_amount > 0:
            # Clip mask for partial fill
            star_layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
            sd = ImageDraw.Draw(star_layer)
            _draw_star(sd, 0, 0, size, fill=YELLOW)
            mask = Image.new("L", (size, size), 0)
            md = ImageDraw.Draw(mask)
            md.rectangle((0, 0, int(size * fill_amount), size), fill=255)
            layer.paste(star_layer, (x, y), mask)


def _draw_star(draw, x, y, size, fill):
    """Draw a 5-pointed star inscribed in a size×size box."""
    import math
    cx, cy = x + size / 2, y + size / 2
    outer = size / 2
    inner = outer * 0.45
    points = []
    for i in range(10):
        r = outer if i % 2 == 0 else inner
        angle = math.pi / 2 - i * math.pi / 5  # start at top
        px = cx + r * math.cos(angle)
        py = cy - r * math.sin(angle)
        points.append((px, py))
    draw.polygon(points, fill=fill)


def render_review(slug, title, tool, rating_5, rating_text, output_dir=None):
    """Review-card layout: big tool icon center, name, stars + rating, footer.

    `rating_5` is 0-5 (fractional ok), `rating_text` is e.g. '8.5 / 10' shown below stars.
    """
    img = gradient(BLUE)
    img = draw_circle_accent(img)
    draw = ImageDraw.Draw(img)
    draw_logo(draw)
    img = draw_badge(img, "REVIEW", YELLOW, NAVY)

    # Big tool icon centered horizontally, near top-middle
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    icon_path = LOGOS_DIR / f"{slug_for_tool(tool)}.png"
    icon_size = 96
    if icon_path.exists():
        icon = Image.open(icon_path).convert("RGBA")
        icon.thumbnail((icon_size, icon_size), Image.LANCZOS)
        # White rounded backdrop
        pad = 14
        bx = (W - icon.width) // 2 - pad
        by = 70
        bd = ImageDraw.Draw(layer)
        bd.rounded_rectangle((bx, by, bx + icon.width + pad * 2, by + icon.height + pad * 2),
                             radius=18, fill=(255, 255, 255, 245))
        layer.paste(icon, (bx + pad, by + pad), icon)

    # Tool name (large)
    name_font = ImageFont.truetype(FONT_BOLD, 32)
    nd = ImageDraw.Draw(layer)
    bb = nd.textbbox((0, 0), tool, font=name_font)
    nx = (W - (bb[2] - bb[0])) // 2
    nd.text((nx, 200), tool, font=name_font, fill=WHITE)

    # Stars
    draw_stars(layer, W // 2, 246, rating_5, size=22, gap=4)

    # Rating text below stars
    rt_font = ImageFont.truetype(FONT_BOLD, 16)
    rd = ImageDraw.Draw(layer)
    bb = rd.textbbox((0, 0), rating_text, font=rt_font)
    rd.text(((W - (bb[2] - bb[0])) // 2, 278), rating_text, font=rt_font, fill=YELLOW)

    img = Image.alpha_composite(img, layer)
    img = draw_footer(img)

    out = Path(output_dir or REPO_ROOT / "assets" / "images") / f"{slug}-thumbnail.png"
    img.convert("RGB").save(out, "PNG", optimize=True)
    print(f"Saved {out.relative_to(REPO_ROOT)} (review card)")
    return out


def render(slug, title, badge="REVIEW", tools=None, gradient_end=None, output_dir=None):
    badge = badge.upper()
    preset = BADGE_PRESETS.get(badge, BADGE_PRESETS["REVIEW"])
    end = gradient_end or preset["grad"]

    img = gradient(end)
    img = draw_circle_accent(img)
    draw = ImageDraw.Draw(img)
    draw_logo(draw)
    img = draw_badge(img, badge, preset["bg"], preset["fg"])
    draw = ImageDraw.Draw(img)
    draw_title(draw, title)
    img = draw_chip_strip(img, tools or [])
    img = draw_footer(img)

    out = Path(output_dir or REPO_ROOT / "assets" / "images") / f"{slug}-thumbnail.png"
    img.convert("RGB").save(out, "PNG", optimize=True)
    print(f"Saved {out.relative_to(REPO_ROOT)}")
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--slug", required=True)
    p.add_argument("--title")
    p.add_argument("--badge", default="REVIEW")
    p.add_argument("--tools", nargs="*", default=[])
    # Review card mode
    p.add_argument("--review-tool", help="Tool name for review-card layout")
    p.add_argument("--rating-5", type=float, help="Rating on 0-5 scale (fractional ok)")
    p.add_argument("--rating-text", default="", help="Display text e.g. '8.5 / 10'")
    args = p.parse_args()
    if args.review_tool and args.rating_5 is not None:
        render_review(slug=args.slug, title=args.title or args.review_tool,
                      tool=args.review_tool, rating_5=args.rating_5,
                      rating_text=args.rating_text)
    else:
        render(slug=args.slug, title=args.title, badge=args.badge, tools=args.tools)


if __name__ == "__main__":
    main()
