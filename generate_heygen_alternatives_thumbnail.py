#!/usr/bin/env python3
"""Generate thumbnail for HeyGen Alternatives 2026 post."""
from PIL import Image, ImageDraw, ImageFont

W, H = 600, 340
OUT = "/home/tom/ai-video-tools-blog/assets/images/heygen-alternatives-2026-thumbnail.png"

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


def main():
    img = Image.new("RGBA", (W, H), (26, 26, 46, 255))
    d = ImageDraw.Draw(img)
    # deep navy to electric blue gradient
    gradient_bg(d, (15, 20, 55), (21, 93, 252))

    # soft circle accents
    for cx, cy, r, a in [(W - 40, 30, 70, 26),
                         (W + 20, 110, 50, 22),
                         (40, H - 50, 60, 22),
                         (-10, 90, 55, 18)]:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255, a))

    # badge
    badge_font = ImageFont.truetype(FONT_BOLD, 13)
    bt = "6 TOOLS TESTED  \u00b7  APR 2026"
    bb = d.textbbox((0, 0), bt, font=badge_font)
    bw = bb[2] - bb[0] + 28
    bx = (W - bw) // 2
    d.rounded_rectangle((bx, 26, bx + bw, 58), radius=10, fill=(255, 140, 0, 235))
    d.text((bx + 14, 31), bt, font=badge_font, fill="white")

    # "HeyGen" header - small on top
    small_font = ImageFont.truetype(FONT_LIGHT, 24)
    header = "HeyGen"
    hb = d.textbbox((0, 0), header, font=small_font)
    hx = (W - (hb[2] - hb[0])) // 2
    d.text((hx, 80), header, font=small_font, fill=(200, 220, 255))

    # Main title "ALTERNATIVES"
    title_font = ImageFont.truetype(FONT_BOLD, 56)
    main = "ALTERNATIVES"
    tb = d.textbbox((0, 0), main, font=title_font)
    tx = (W - (tb[2] - tb[0])) // 2
    d.text((tx, 112), main, font=title_font, fill="white")

    # Year
    year_font = ImageFont.truetype(FONT_BOLD, 48)
    year = "2026"
    yb = d.textbbox((0, 0), year, font=year_font)
    yx = (W - (yb[2] - yb[0])) // 2
    d.text((yx, 180), year, font=year_font, fill=(255, 215, 0))

    # divider
    d.rectangle([(150, 245), (W - 150, 248)], fill=(77, 157, 255, 255))

    # Subtitle
    sub_font = ImageFont.truetype(FONT_REG, 18)
    sub = "Synthesia  \u00b7  Vidnoz  \u00b7  Pictory  \u00b7  Colossyan"
    sb = d.textbbox((0, 0), sub, font=sub_font)
    sx = (W - (sb[2] - sb[0])) // 2
    d.text((sx, 260), sub, font=sub_font, fill=(207, 216, 232, 255))

    # Brand footer
    brand_font = ImageFont.truetype(FONT_BOLD, 14)
    brand = "AI VIDEO PICKS"
    bf = d.textbbox((0, 0), brand, font=brand_font)
    bx2 = (W - (bf[2] - bf[0])) // 2
    d.text((bx2, H - 32), brand, font=brand_font, fill=(77, 157, 255, 255))

    # bottom accent bar
    d.rectangle([(0, H - 6), (W, H)], fill=(255, 140, 0, 255))

    img.convert("RGB").save(OUT)
    print(f"Created {OUT}")


if __name__ == "__main__":
    main()
