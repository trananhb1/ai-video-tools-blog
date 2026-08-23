#!/usr/bin/env python3
"""Generate thumbnail for posts/synthesia-vs-arcads-2026.html (600x340 branded PNG)."""

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


def center_text(draw, text, x, y, font, fill="white"):
    bb = draw.textbbox((0, 0), text, font=font)
    w = bb[2] - bb[0]
    draw.text((x - w // 2, y), text, font=font, fill=fill)


def badge(draw, text, color, y=18, text_color="white"):
    font = ImageFont.truetype(FONT_BOLD, 13)
    bb = draw.textbbox((0, 0), text, font=font)
    bw = bb[2] - bb[0] + 22
    bx = (W - bw) // 2
    draw.rounded_rectangle((bx, y, bx + bw, y + 26), radius=8, fill=color)
    draw.text((bx + 11, y + 4), text, font=font, fill=text_color)


def make_thumbnail():
    img = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(img)

    # Brand gradient: blue (#4361ee) to navy (#1a1a2e)
    gradient_bg(draw, (67, 97, 238), (26, 26, 46))

    # Top badge
    badge(draw, "MAY 2026 COMPARISON", (220, 38, 38), y=18)

    # Title split: Synthesia (blue accent) vs Arcads (green accent)
    title_font = ImageFont.truetype(FONT_BOLD, 42)
    vs_font = ImageFont.truetype(FONT_BOLD, 28)
    sub_year_font = ImageFont.truetype(FONT_BOLD, 30)

    syn_color = (133, 173, 255)   # light blue (Synthesia)
    arc_color = (16, 185, 129)    # green (Arcads)

    bb_syn = draw.textbbox((0, 0), "Synthesia", font=title_font)
    syn_w = bb_syn[2] - bb_syn[0]
    bb_arc = draw.textbbox((0, 0), "Arcads", font=title_font)
    arc_w = bb_arc[2] - bb_arc[0]
    bb_vs = draw.textbbox((0, 0), "vs", font=vs_font)
    vs_w = bb_vs[2] - bb_vs[0]

    total = syn_w + 30 + vs_w + 30 + arc_w
    start = (W - total) // 2
    y_title = 80

    draw.text((start, y_title), "Synthesia", font=title_font, fill=syn_color)
    draw.text((start + syn_w + 30, y_title + 8), "vs", font=vs_font, fill=(220, 225, 245))
    draw.text((start + syn_w + 30 + vs_w + 30, y_title), "Arcads", font=title_font, fill=arc_color)

    # Year / subtitle
    center_text(draw, "2026 Comparison", W // 2, 140, sub_year_font, fill=(255, 215, 0))

    # Divider
    draw.line([(80, 195), (W - 80, 195)], fill=(120, 140, 200), width=1)

    # Stats columns
    stat_font = ImageFont.truetype(FONT_BOLD, 18)
    label_font = ImageFont.truetype(FONT_REG, 12)

    left_x = 90
    draw.text((left_x, 210), "230+ avatars", font=stat_font, fill=syn_color)
    draw.text((left_x, 235), "Training & L&D", font=label_font, fill=(200, 210, 240))
    draw.text((left_x, 252), "From $18/mo annual", font=label_font, fill=(200, 210, 240))

    right_x = 360
    draw.text((right_x, 210), "1,000+ AI actors", font=stat_font, fill=arc_color)
    draw.text((right_x, 235), "UGC ads (Meta/TikTok)", font=label_font, fill=(200, 210, 240))
    draw.text((right_x, 252), "From $110/mo", font=label_font, fill=(200, 210, 240))

    # Hook line
    hook_font = ImageFont.truetype(FONT_REG, 15)
    center_text(draw, "Training avatars vs UGC ad actors — which wins?",
                W // 2, 290, hook_font, fill=(220, 225, 245))

    # AI Video Picks branding (small bottom-right)
    brand_font = ImageFont.truetype(FONT_BOLD, 12)
    brand_text = "AI Video Picks"
    bb_b = draw.textbbox((0, 0), brand_text, font=brand_font)
    bw_b = bb_b[2] - bb_b[0]
    draw.text((W - bw_b - 16, H - 26), brand_text, font=brand_font, fill=(180, 195, 230))

    # Accent bar split
    draw.rectangle([(0, H - 6), (W // 2, H)], fill=syn_color)
    draw.rectangle([(W // 2, H - 6), (W, H)], fill=arc_color)

    out_name = "synthesia-vs-arcads-2026-thumbnail.png"
    img.convert("RGB").save(f"{OUT}/{out_name}")
    print(f"Created {out_name}")


if __name__ == "__main__":
    make_thumbnail()
