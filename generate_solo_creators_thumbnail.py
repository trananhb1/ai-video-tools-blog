#!/usr/bin/env python3
"""Generate thumbnail for HeyGen vs Descript vs Opus Clip solo creators post."""
from PIL import Image, ImageDraw, ImageFont

W, H = 600, 340
OUT = "/home/tom/ai-video-tools-blog/assets/images/heygen-descript-opus-clip-thumbnail.png"

FONT_BOLD = "/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf"
FONT_REG = "/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf"


def gradient_bg(draw, c1, c2):
    for y in range(H):
        t = y / H
        r = int(c1[0] + (c2[0] - c1[0]) * t)
        g = int(c1[1] + (c2[1] - c1[1]) * t)
        b = int(c1[2] + (c2[2] - c1[2]) * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))


def main():
    img = Image.new("RGBA", (W, H), (26, 26, 46, 255))
    d = ImageDraw.Draw(img)
    # deep navy to electric blue gradient
    gradient_bg(d, (20, 20, 50), (21, 93, 252))

    # top-right accent circles
    for cx, cy, r, a in [(W - 40, 30, 60, 28), (W + 20, 90, 40, 22), (40, H - 40, 55, 20)]:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255, a))

    # badge
    badge_font = ImageFont.truetype(FONT_BOLD, 14)
    bt = "SOLO CREATOR STACK  \u00b7  2026"
    bb = d.textbbox((0, 0), bt, font=badge_font)
    bw = bb[2] - bb[0] + 28
    bx = (W - bw) // 2
    d.rounded_rectangle((bx, 28, bx + bw, 60), radius=10, fill=(77, 157, 255, 235))
    d.text((bx + 14, 32), bt, font=badge_font, fill="white")

    # Title (wrapped)
    title_font = ImageFont.truetype(FONT_BOLD, 36)
    lines = ["HeyGen  +  Descript", "+  Opus Clip"]
    y = 92
    for ln in lines:
        tb = d.textbbox((0, 0), ln, font=title_font)
        tx = (W - (tb[2] - tb[0])) // 2
        d.text((tx, y), ln, font=title_font, fill="white")
        y += 46

    # divider
    d.rectangle([(120, y + 8), (W - 120, y + 11)], fill=(77, 157, 255, 255))

    # Subtitle
    sub_font = ImageFont.truetype(FONT_REG, 19)
    sub = "Best AI Video Stack for Solo Creators"
    sb = d.textbbox((0, 0), sub, font=sub_font)
    sx = (W - (sb[2] - sb[0])) // 2
    d.text((sx, y + 24), sub, font=sub_font, fill=(207, 216, 232, 255))

    # Brand footer
    brand_font = ImageFont.truetype(FONT_BOLD, 16)
    brand = "AI VIDEO PICKS"
    bf = d.textbbox((0, 0), brand, font=brand_font)
    bx = (W - (bf[2] - bf[0])) // 2
    d.text((bx, H - 38), brand, font=brand_font, fill=(77, 157, 255, 255))

    # bottom accent bar
    d.rectangle([(0, H - 6), (W, H)], fill=(77, 157, 255, 255))

    img.convert("RGB").save(OUT)
    print(f"Created {OUT}")


if __name__ == "__main__":
    main()
