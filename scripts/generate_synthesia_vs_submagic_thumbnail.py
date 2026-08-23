#!/usr/bin/env python3
"""Generate thumbnail for posts/synthesia-vs-submagic-2026.html (600x340 branded PNG)."""

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

    # Background: brand gradient #4361ee -> #1a1a2e
    gradient_bg(draw, (67, 97, 238), (26, 26, 46))

    # Top badge
    badge(draw, "MAY 2026 COMPARISON", (220, 38, 38), y=18)

    # Title — "Synthesia vs Submagic" with brand-coloured words
    title_font = ImageFont.truetype(FONT_BOLD, 38)
    vs_font = ImageFont.truetype(FONT_BOLD, 26)

    syn_color = (16, 185, 129)   # Synthesia green
    sub_color = (196, 167, 255)  # Submagic light-purple (visible on dark bg)

    bb_syn = draw.textbbox((0, 0), "Synthesia", font=title_font)
    syn_w = bb_syn[2] - bb_syn[0]

    bb_sub = draw.textbbox((0, 0), "Submagic", font=title_font)
    sub_w = bb_sub[2] - bb_sub[0]

    bb_vs = draw.textbbox((0, 0), "vs", font=vs_font)
    vs_w = bb_vs[2] - bb_vs[0]

    total = syn_w + 26 + vs_w + 26 + sub_w
    start = (W - total) // 2
    y_title = 78

    draw.text((start, y_title), "Synthesia", font=title_font, fill=syn_color)
    draw.text((start + syn_w + 26, y_title + 8), "vs", font=vs_font, fill=(220, 220, 235))
    draw.text((start + syn_w + 26 + vs_w + 26, y_title), "Submagic", font=title_font, fill=sub_color)

    # Subtitle
    sub_font = ImageFont.truetype(FONT_BOLD, 22)
    center_text(draw, "Create vs Caption  -  2026", W // 2, 138, sub_font, fill=(255, 215, 0))

    # Divider rule
    draw.line([(80, 185), (W - 80, 185)], fill=(120, 130, 180), width=1)

    # Quick stat strip
    stat_font = ImageFont.truetype(FONT_BOLD, 17)
    label_font = ImageFont.truetype(FONT_REG, 12)

    # Left column (Synthesia)
    left_x = 90
    draw.text((left_x, 200), "230+ avatars", font=stat_font, fill=syn_color)
    draw.text((left_x, 224), "140+ languages", font=label_font, fill=(200, 210, 240))
    draw.text((left_x, 241), "SOC 2 + SCORM", font=label_font, fill=(200, 210, 240))
    draw.text((left_x, 258), "From $18/mo annual", font=label_font, fill=(200, 210, 240))

    # Right column (Submagic)
    right_x = 350
    draw.text((right_x, 200), "Viral captions", font=stat_font, fill=sub_color)
    draw.text((right_x, 224), "Magic B-Roll", font=label_font, fill=(200, 210, 240))
    draw.text((right_x, 241), "Magic Clips", font=label_font, fill=(200, 210, 240))
    draw.text((right_x, 258), "From $9/mo annual", font=label_font, fill=(200, 210, 240))

    # Hook strip
    hook_font = ImageFont.truetype(FONT_REG, 14)
    center_text(draw, "Create AI video from text  -or-  caption + clip your existing video",
                W // 2, 292, hook_font, fill=(220, 225, 245))

    # Branding
    brand_font = ImageFont.truetype(FONT_BOLD, 12)
    center_text(draw, "AI VIDEO PICKS", W // 2, 314, brand_font, fill=(140, 200, 255))

    # Bottom accent bar split
    draw.rectangle([(0, H - 6), (W // 2, H)], fill=syn_color)
    draw.rectangle([(W // 2, H - 6), (W, H)], fill=(124, 58, 237))

    out_name = "synthesia-vs-submagic-2026-thumbnail.png"
    img.convert("RGB").save(f"{OUT}/{out_name}")
    print(f"Created {out_name}")


if __name__ == "__main__":
    make_thumbnail()
