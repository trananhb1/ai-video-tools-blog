#!/usr/bin/env python3
"""Generate thumbnail for Arcads vs Creatify vs MakeUGC comparison post."""

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


def center_text(draw, text, y, font, fill="white"):
    bb = draw.textbbox((0, 0), text, font=font)
    x = (W - (bb[2] - bb[0])) // 2
    draw.text((x, y), text, font=font, fill=fill)


def main():
    img = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(img)

    # Deep purple to dark blue gradient
    gradient_bg(draw, (99, 102, 241), (30, 27, 75))
    circles(draw)

    # Badge
    font_badge = ImageFont.truetype(FONT_BOLD, 13)
    badge_text = "COMPARISON  |  AI UGC ADS  |  2026"
    bb = draw.textbbox((0, 0), badge_text, font=font_badge)
    bw = bb[2] - bb[0] + 24
    bx = (W - bw) // 2
    draw.rounded_rectangle((bx, 22, bx + bw, 48), radius=8, fill=(30, 27, 75, 200))
    draw.text((bx + 12, 25), badge_text, font=font_badge, fill="white")

    # "VS" circles with tool names
    font_vs = ImageFont.truetype(FONT_BOLD, 18)
    font_tool = ImageFont.truetype(FONT_BOLD, 16)

    # Three tool badges
    positions = [(100, 100), (300, 100), (500, 100)]
    colors = [(99, 102, 241), (21, 93, 252), (16, 185, 129)]
    names = ["Arcads", "Creatify", "MakeUGC"]

    for (cx, cy), color, name in zip(positions, colors, names):
        # Circle
        r = 36
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color, 255))
        # Letter
        letter = name[0]
        font_letter = ImageFont.truetype(FONT_BOLD, 28)
        lbb = draw.textbbox((0, 0), letter, font=font_letter)
        lx = cx - (lbb[2] - lbb[0]) // 2
        ly = cy - (lbb[3] - lbb[1]) // 2 - 2
        draw.text((lx, ly), letter, font=font_letter, fill="white")
        # Name below
        nbb = draw.textbbox((0, 0), name, font=font_tool)
        nx = cx - (nbb[2] - nbb[0]) // 2
        draw.text((nx, cy + r + 8), name, font=font_tool, fill="white")

    # "VS" between tools
    font_vs_small = ImageFont.truetype(FONT_BOLD, 14)
    for i in range(2):
        x1 = positions[i][0]
        x2 = positions[i + 1][0]
        mid_x = (x1 + x2) // 2
        vsbb = draw.textbbox((0, 0), "VS", font=font_vs_small)
        draw.text((mid_x - (vsbb[2] - vsbb[0]) // 2, 95), "VS", font=font_vs_small, fill=(255, 255, 255, 180))

    # Main title
    font_title = ImageFont.truetype(FONT_BOLD, 22)
    center_text(draw, "Best AI UGC Video Ad Generator", 190, font_title)

    # Subtitle
    font_sub = ImageFont.truetype(FONT_REG, 14)
    center_text(draw, "Pricing  |  Actor Quality  |  Automation  |  Which to Pick", 222, font_sub, fill=(200, 200, 255))

    # Bottom badges (key stats)
    font_stat = ImageFont.truetype(FONT_BOLD, 11)
    stats = ["From $33/mo", "1,000+ AI Actors", "90-98% Cost Savings"]
    total_w = sum(draw.textbbox((0, 0), s, font=font_stat)[2] - draw.textbbox((0, 0), s, font=font_stat)[0] + 24 for s in stats) + 16
    sx = (W - total_w) // 2
    for stat in stats:
        sbb = draw.textbbox((0, 0), stat, font=font_stat)
        sw = sbb[2] - sbb[0] + 24
        draw.rounded_rectangle((sx, 268, sx + sw, 292), radius=6, fill=(30, 27, 75, 200))
        draw.text((sx + 12, 272), stat, font=font_stat, fill="white")
        sx += sw + 8

    # Brand footer
    font_brand = ImageFont.truetype(FONT_BOLD, 12)
    center_text(draw, "aivideopicks.com", 310, font_brand, fill=(180, 180, 220))

    out_path = f"{OUT}/arcads-creatify-makeugc-thumbnail.png"
    img.save(out_path, "PNG")
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
