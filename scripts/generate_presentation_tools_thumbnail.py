#!/usr/bin/env python3
"""Generate thumbnail for best-ai-presentation-tools-2026.html."""

import sys
sys.path.insert(0, "/home/tom/ai-video-tools-blog")

from PIL import Image, ImageDraw, ImageFont

W, H = 600, 340
OUT = "/home/tom/ai-video-tools-blog/assets/images"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def gradient_bg(draw, c1, c2):
    for y in range(H):
        t = y / H
        r = int(c1[0] + (c2[0] - c1[0]) * t)
        g = int(c1[1] + (c2[1] - c1[1]) * t)
        b = int(c1[2] + (c2[2] - c1[2]) * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))


def circles(draw, color=(255, 255, 255), alpha=18):
    positions = [(-20, -15, 45), (W - 30, -20, 35), (W + 10, H // 2, 40),
                 (-15, H - 20, 30), (W - 60, H + 10, 35), (50, H + 15, 25)]
    for cx, cy, r in positions:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color, alpha))


def badge(draw, text, color, y=20):
    font = ImageFont.truetype(FONT_BOLD, 14)
    bb = draw.textbbox((0, 0), text, font=font)
    bw = bb[2] - bb[0] + 24
    bx = (W - bw) // 2
    draw.rounded_rectangle((bx, y, bx + bw, y + 28), radius=8, fill=(*color, 220))
    draw.text((bx + 12, y + 3), text, font=font, fill="white")


def center_text(draw, text, y, font, fill="white"):
    bb = draw.textbbox((0, 0), text, font=font)
    x = (W - (bb[2] - bb[0])) // 2
    draw.text((x, y), text, font=font, fill=fill)


def accent_bar(draw, color):
    draw.rectangle([(0, H - 6), (W, H)], fill=color)


def make_presentation_thumbnail():
    img = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(img)

    # Gradient: indigo → purple (presentation/creative theme)
    gradient_bg(draw, (21, 93, 252), (124, 58, 237))
    circles(draw)

    # Badge
    badge(draw, "2026 RANKINGS", (245, 158, 11), y=22)

    # Title
    font_title = ImageFont.truetype(FONT_BOLD, 28)
    center_text(draw, "Best AI Presentation", 65, font_title)
    center_text(draw, "Tools 2026", 100, font_title)

    # Subtitle
    font_sub = ImageFont.truetype(FONT_REG, 15)
    center_text(draw, "5 Tools Tested & Ranked", 145, font_sub, fill=(255, 255, 255, 200))

    # Tool names in a row
    tools = ["Gamma", "Beautiful.ai", "Tome", "Slidesgo", "Google Slides"]
    font_tool = ImageFont.truetype(FONT_BOLD, 13)
    # Calculate total width
    tool_widths = []
    for t in tools:
        bb = draw.textbbox((0, 0), t, font=font_tool)
        tool_widths.append(bb[2] - bb[0] + 20)
    total_w = sum(tool_widths) + 8 * (len(tools) - 1)
    sx = (W - total_w) // 2
    y_tool = 185

    colors = [
        (34, 197, 94),    # green for #1
        (59, 130, 246),   # blue
        (168, 85, 247),   # purple
        (251, 146, 60),   # orange
        (100, 116, 139),  # gray
    ]
    for i, (t, tw) in enumerate(zip(tools, tool_widths)):
        c = colors[i]
        draw.rounded_rectangle((sx, y_tool, sx + tw, y_tool + 30), radius=6, fill=(*c, 200))
        draw.text((sx + 10, y_tool + 5), t, font=font_tool, fill="white")
        sx += tw + 8

    # Winner callout
    font_win = ImageFont.truetype(FONT_BOLD, 16)
    font_det = ImageFont.truetype(FONT_REG, 13)
    center_text(draw, "#1 Gamma — 9.0/10 — From $8/mo", 235, font_win, fill=(34, 197, 94))
    center_text(draw, "One-click redesign | Embed anywhere | Viewer analytics", 260, font_det, fill=(255, 255, 255, 180))

    # Brand
    font_brand = ImageFont.truetype(FONT_BOLD, 12)
    center_text(draw, "aivideopicks.com", 300, font_brand, fill=(255, 255, 255, 140))

    # Accent bar
    accent_bar(draw, (245, 158, 11))

    # Save
    out = img.convert("RGB")
    path = f"{OUT}/best-ai-presentation-tools-2026-thumbnail.png"
    out.save(path, quality=95)
    print(f"Saved: {path}")
    return path


if __name__ == "__main__":
    make_presentation_thumbnail()
