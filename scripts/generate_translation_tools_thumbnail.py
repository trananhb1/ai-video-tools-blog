#!/usr/bin/env python3
"""Generate thumbnail for best-ai-video-translation-tools-2026.html."""

import sys
sys.path.insert(0, "/home/tom/ai-video-tools-blog")

from PIL import Image, ImageDraw, ImageFont

# Reuse helpers by inlining (the source file uses top-level constants)
W, H = 600, 340
OUT = "/home/tom/ai-video-tools-blog/assets/images"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_LIGHT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


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


def make_translation_thumbnail():
    img = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(img)

    # Gradient: deep blue → indigo (translation/global theme)
    gradient_bg(draw, (12, 28, 78), (54, 31, 121))
    circles(draw)

    # Badge
    badge(draw, "6 TOOLS TESTED", (255, 140, 0))

    # Main title
    title_font = ImageFont.truetype(FONT_BOLD, 44)
    center_text(draw, "Best AI Video", 70, title_font)
    center_text(draw, "Translation Tools", 120, title_font)

    # Year emphasis
    year_font = ImageFont.truetype(FONT_BOLD, 52)
    center_text(draw, "2026", 175, year_font, fill=(255, 215, 0))

    # Tool list strip
    tools_font = ImageFont.truetype(FONT_REG, 14)
    tools = "HeyGen  •  ElevenLabs  •  Synthesia  •  Rask  •  Submagic  •  Kapwing"
    center_text(draw, tools, 245, tools_font, fill=(200, 210, 255))

    # Subtitle / hook
    sub_font = ImageFont.truetype(FONT_LIGHT, 18)
    center_text(draw, "Lip-sync + voice cloning in 175+ languages", 280, sub_font, fill=(255, 255, 255))

    # Bottom accent bar — gold to match year
    accent_bar(draw, (255, 200, 0))

    out_name = "best-ai-video-translation-tools-2026-thumbnail.png"
    img.convert("RGB").save(f"{OUT}/{out_name}")
    print(f"Created {out_name}")


if __name__ == "__main__":
    make_translation_thumbnail()
