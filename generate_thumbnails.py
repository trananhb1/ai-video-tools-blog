#!/usr/bin/env python3
"""Generate 3 blog card thumbnails for ai-video-tools-blog."""

from PIL import Image, ImageDraw, ImageFont
import math

W, H = 600, 340
OUT = "/home/tom/ai-video-tools-blog/assets/images"

FONT_BOLD = "/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf"
FONT_REG = "/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf"
FONT_LIGHT = "/usr/share/fonts/truetype/ubuntu/Ubuntu-L.ttf"


def gradient(draw, w, h, c1, c2):
    """Draw a diagonal gradient from top-left c1 to bottom-right c2."""
    for y in range(h):
        for x in range(w):
            t = (x / w * 0.4 + y / h * 0.6)
            r = int(c1[0] + (c2[0] - c1[0]) * t)
            g = int(c1[1] + (c2[1] - c1[1]) * t)
            b = int(c1[2] + (c2[2] - c1[2]) * t)
            draw.point((x, y), fill=(r, g, b))


def draw_rounded_rect(draw, xy, fill, radius=12):
    """Draw a rounded rectangle."""
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill)


def draw_text_centered(draw, text, y, font, fill="white"):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (W - tw) // 2
    draw.text((x, y), text, font=font, fill=fill)
    return tw


def add_decorative_circles(draw, color, alpha=18):
    """Add subtle decorative circles at edges for visual interest."""
    positions = [
        (-20, -15, 45), (W - 30, -20, 35), (W + 10, H // 2, 40),
        (-15, H - 20, 30), (W - 60, H + 10, 35), (50, H + 15, 25),
    ]
    for cx, cy, r in positions:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r],
                      fill=(*color, alpha))


# ── 1. TOP 10 THUMBNAIL ─────────────────────────────────────────────
def make_top10():
    img = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(img)

    # Gradient background
    for y in range(H):
        t = y / H
        r = int(0x1a + (0x15 - 0x1a) * t)
        g = int(0x1a + (0x5D - 0x1a) * t)
        b = int(0x2e + (0xFC - 0x2e) * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

    # Decorative circles
    add_decorative_circles(draw, (255, 255, 255))

    # "2026 RANKING" badge at top
    badge_font = ImageFont.truetype(FONT_BOLD, 14)
    badge_text = "2026 RANKING"
    bb = draw.textbbox((0, 0), badge_text, font=badge_font)
    bw = bb[2] - bb[0] + 24
    bx = (W - bw) // 2
    draw_rounded_rect(draw, (bx, 20, bx + bw, 48), fill=(255, 215, 0, 220), radius=8)
    draw.text((bx + 12, 23), badge_text, font=badge_font, fill=(26, 26, 46))

    # "TOP" text
    top_font = ImageFont.truetype(FONT_BOLD, 72)
    bb = draw.textbbox((0, 0), "TOP", font=top_font)
    top_w = bb[2] - bb[0]
    # "10" text in gold
    ten_font = ImageFont.truetype(FONT_BOLD, 90)
    bb10 = draw.textbbox((0, 0), "10", font=ten_font)
    ten_w = bb10[2] - bb10[0]
    total = top_w + 15 + ten_w
    sx = (W - total) // 2
    draw.text((sx, 65), "TOP", font=top_font, fill="white")
    draw.text((sx + top_w + 15, 52), "10", font=ten_font, fill=(255, 215, 0))

    # Subtitle
    sub_font = ImageFont.truetype(FONT_REG, 28)
    draw_text_centered(draw, "Best AI Video Tools", 170, sub_font, fill="white")

    # Divider line
    draw.line([(180, 215), (420, 215)], fill=(255, 255, 255, 120), width=2)

    # Year
    year_font = ImageFont.truetype(FONT_LIGHT, 22)
    draw_text_centered(draw, "Complete Guide & Reviews", 230, year_font, fill=(200, 200, 255))

    # Bottom accent bar
    draw.rectangle([(0, H - 6), (W, H)], fill=(255, 215, 0))

    img.convert("RGB").save(f"{OUT}/top10-thumbnail.png")
    print("Created top10-thumbnail.png")


# ── 2. ZEBRACAT REVIEW THUMBNAIL ────────────────────────────────────
def make_zebracat():
    img = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(img)

    # Gradient background (teal to dark)
    for y in range(H):
        t = y / H
        r = int(0x0d + (0x1a - 0x0d) * t)
        g = int(0x94 + (0x1a - 0x94) * t)
        b = int(0x88 + (0x2e - 0x88) * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

    add_decorative_circles(draw, (255, 255, 255))

    # "REVIEW" badge top-right
    badge_font = ImageFont.truetype(FONT_BOLD, 14)
    badge_text = "IN-DEPTH REVIEW"
    bb = draw.textbbox((0, 0), badge_text, font=badge_font)
    bw = bb[2] - bb[0] + 24
    bx = (W - bw) // 2
    draw_rounded_rect(draw, (bx, 20, bx + bw, 48), fill=(16, 185, 129, 220), radius=8)
    draw.text((bx + 12, 23), badge_text, font=badge_font, fill="white")

    # "ZEBRACAT" large text
    main_font = ImageFont.truetype(FONT_BOLD, 64)
    draw_text_centered(draw, "ZEBRACAT", 65, main_font, fill="white")

    # Star rating (4.2/5) - use DejaVu Sans for star glyph support
    star_y = 150
    star_size = 28
    star_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", star_size)
    total_stars_w = 5 * (star_size + 8)
    sx = (W - total_stars_w) // 2
    for i in range(5):
        color = (255, 215, 0) if i < 4 else (255, 215, 0, 100)
        draw.text((sx + i * (star_size + 8), star_y), "\u2605", font=star_font, fill=color)

    # Rating text
    rating_font = ImageFont.truetype(FONT_BOLD, 22)
    draw_text_centered(draw, "4.2 / 5.0", 188, rating_font, fill=(255, 215, 0))

    # Subtitle
    sub_font = ImageFont.truetype(FONT_REG, 20)
    draw_text_centered(draw, "AI Video Generation Platform", 225, sub_font, fill=(200, 230, 225))

    # "2026" year tag bottom
    year_font = ImageFont.truetype(FONT_BOLD, 16)
    year_text = "2026"
    bb = draw.textbbox((0, 0), year_text, font=year_font)
    yw = bb[2] - bb[0] + 20
    yx = W - yw - 20
    draw_rounded_rect(draw, (yx, H - 45, yx + yw, H - 20), fill=(255, 255, 255, 50), radius=6)
    draw.text((yx + 10, H - 43), year_text, font=year_font, fill="white")

    # Bottom accent bar
    draw.rectangle([(0, H - 6), (W, H)], fill=(16, 185, 129))

    img.convert("RGB").save(f"{OUT}/zebracat-review-thumbnail.png")
    print("Created zebracat-review-thumbnail.png")


# ── 3. E-COMMERCE THUMBNAIL ─────────────────────────────────────────
def make_ecommerce():
    img = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(img)

    # Gradient background (purple to dark)
    for y in range(H):
        t = y / H
        r = int(0x7c + (0x1a - 0x7c) * t)
        g = int(0x3a + (0x1a - 0x3a) * t)
        b = int(0xed + (0x2e - 0xed) * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

    add_decorative_circles(draw, (255, 255, 255))

    # "AI VIDEO GUIDE" badge
    badge_font = ImageFont.truetype(FONT_BOLD, 14)
    badge_text = "AI VIDEO GUIDE"
    bb = draw.textbbox((0, 0), badge_text, font=badge_font)
    bw = bb[2] - bb[0] + 24
    bx = (W - bw) // 2
    draw_rounded_rect(draw, (bx, 20, bx + bw, 48), fill=(167, 100, 255, 220), radius=8)
    draw.text((bx + 12, 23), badge_text, font=badge_font, fill="white")

    # "$" symbols as subtle background decoration
    dollar_font = ImageFont.truetype(FONT_BOLD, 120)
    draw.text((15, 180), "$", font=dollar_font, fill=(255, 255, 255, 18))
    draw.text((W - 110, 170), "$", font=dollar_font, fill=(255, 255, 255, 18))

    # "E-COMMERCE" large text
    main_font = ImageFont.truetype(FONT_BOLD, 52)
    draw_text_centered(draw, "E-COMMERCE", 65, main_font, fill="white")

    # "+80% Sales" callout
    callout_font = ImageFont.truetype(FONT_BOLD, 36)
    callout_text = "+80% Sales"
    bb = draw.textbbox((0, 0), callout_text, font=callout_font)
    cw = bb[2] - bb[0] + 40
    cx = (W - cw) // 2
    draw_rounded_rect(draw, (cx, 140, cx + cw, 190), fill=(16, 185, 129, 220), radius=10)
    draw.text((cx + 20, 143), callout_text, font=callout_font, fill="white")

    # Subtitle
    sub_font = ImageFont.truetype(FONT_REG, 20)
    draw_text_centered(draw, "Boost Your Online Store with AI Video", 210, sub_font, fill=(220, 210, 255))

    # Bottom accent bar
    draw.rectangle([(0, H - 6), (W, H)], fill=(124, 58, 237))

    img.convert("RGB").save(f"{OUT}/ecommerce-thumbnail.png")
    print("Created ecommerce-thumbnail.png")


if __name__ == "__main__":
    make_top10()
    make_zebracat()
    make_ecommerce()
    print("All thumbnails generated!")
