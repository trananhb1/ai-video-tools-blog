#!/usr/bin/env python3
"""Generate thumbnail for posts/synthesia-vs-fliki-2026.html (600x340 branded PNG)."""

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


def half_bg(draw, color, x_start, x_end):
    """Solid color block on one half (for split versus design)."""
    draw.rectangle([(x_start, 70), (x_end, H - 8)], fill=color)


def center_text(draw, text, x, y, font, fill="white", anchor=None):
    """Draw text centered horizontally around x."""
    bb = draw.textbbox((0, 0), text, font=font)
    w = bb[2] - bb[0]
    draw.text((x - w // 2, y), text, font=font, fill=fill)


def left_text(draw, text, x, y, font, fill="white"):
    draw.text((x, y), text, font=font, fill=fill)


def badge(draw, text, color, y=18, text_color="white"):
    font = ImageFont.truetype(FONT_BOLD, 13)
    bb = draw.textbbox((0, 0), text, font=font)
    bw = bb[2] - bb[0] + 22
    bx = (W - bw) // 2
    draw.rounded_rectangle((bx, y, bx + bw, y + 26), radius=8, fill=color)
    draw.text((bx + 11, y + 4), text, font=font, fill=text_color)


def accent_bar(draw, color):
    draw.rectangle([(0, H - 6), (W, H)], fill=color)


def make_thumbnail():
    img = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(img)

    # Background: dark navy
    gradient_bg(draw, (15, 23, 60), (32, 18, 75))

    # Top badge
    badge(draw, "MAY 2026 COMPARISON", (220, 38, 38), y=18)

    # Main heading: "Synthesia vs Fliki"
    title_font = ImageFont.truetype(FONT_BOLD, 42)
    sub_year_font = ImageFont.truetype(FONT_BOLD, 30)

    # Split the title across the horizontal — Synthesia (left, green) / Fliki (right, orange)
    # First line: composite "Synthesia"  vs  "Fliki"
    syn_color = (16, 185, 129)   # Synthesia green
    fli_color = (255, 107, 53)   # Fliki orange

    # "Synthesia" on left
    bb_syn = draw.textbbox((0, 0), "Synthesia", font=title_font)
    syn_w = bb_syn[2] - bb_syn[0]

    # "Fliki" on right
    bb_fli = draw.textbbox((0, 0), "Fliki", font=title_font)
    fli_w = bb_fli[2] - bb_fli[0]

    # "vs" in the middle
    vs_font = ImageFont.truetype(FONT_BOLD, 28)
    bb_vs = draw.textbbox((0, 0), "vs", font=vs_font)
    vs_w = bb_vs[2] - bb_vs[0]

    # Layout: total width = syn_w + 30 + vs_w + 30 + fli_w
    total = syn_w + 30 + vs_w + 30 + fli_w
    start = (W - total) // 2
    y_title = 80

    draw.text((start, y_title), "Synthesia", font=title_font, fill=syn_color)
    draw.text((start + syn_w + 30, y_title + 8), "vs", font=vs_font, fill=(200, 200, 220))
    draw.text((start + syn_w + 30 + vs_w + 30, y_title), "Fliki", font=title_font, fill=fli_color)

    # Year
    center_text(draw, "2026", W // 2, 140, sub_year_font, fill=(255, 215, 0))

    # Divider rule
    draw.line([(80, 195), (W - 80, 195)], fill=(80, 90, 130), width=1)

    # Quick stat strip — two-column
    stat_font = ImageFont.truetype(FONT_BOLD, 18)
    label_font = ImageFont.truetype(FONT_REG, 12)

    # Left column (Synthesia)
    left_x = 100
    draw.text((left_x, 210), "230+ avatars", font=stat_font, fill=syn_color)
    draw.text((left_x, 235), "SOC 2 + SCORM", font=label_font, fill=(180, 190, 220))
    draw.text((left_x, 252), "From $18/mo annual", font=label_font, fill=(180, 190, 220))

    # Right column (Fliki)
    right_x = 360
    draw.text((right_x, 210), "2,000+ voices", font=stat_font, fill=fli_color)
    draw.text((right_x, 235), "75+ languages", font=label_font, fill=(180, 190, 220))
    draw.text((right_x, 252), "From $21/month", font=label_font, fill=(180, 190, 220))

    # Hook strip
    hook_font = ImageFont.truetype(FONT_REG, 15)
    center_text(draw, "Avatars vs voiceover — which wins for your workflow?",
                W // 2, 290, hook_font, fill=(220, 225, 245))

    # Bottom accent bar — gradient look split
    draw.rectangle([(0, H - 6), (W // 2, H)], fill=syn_color)
    draw.rectangle([(W // 2, H - 6), (W, H)], fill=fli_color)

    out_name = "synthesia-vs-fliki-2026-thumbnail.png"
    img.convert("RGB").save(f"{OUT}/{out_name}")
    print(f"Created {out_name}")


if __name__ == "__main__":
    make_thumbnail()
