#!/usr/bin/env python3
"""Generate thumbnail for Google Vids Veo 3.1 free tutorial post."""

from PIL import Image, ImageDraw, ImageFont

W, H = 600, 340
OUT = "/home/tom/ai-video-tools-blog/assets/images"

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_LIGHT = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


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


def wrap_text(text, font, max_width, draw):
    words = text.split()
    lines, current = [], ""
    for w in words:
        test = f"{current} {w}".strip()
        bb = draw.textbbox((0, 0), test, font=font)
        if bb[2] - bb[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = w
    if current:
        lines.append(current)
    return lines


def accent_bar(draw, color):
    draw.rectangle([(0, H - 6), (W, H)], fill=color)


img = Image.new("RGBA", (W, H))
draw = ImageDraw.Draw(img)

# Google-inspired gradient: green to blue
gradient_bg(draw, (30, 120, 60), (10, 50, 120))
circles(draw)

# Badge
badge(draw, "FREE TUTORIAL", (76, 175, 80))

# Main title
main_font = ImageFont.truetype(FONT_BOLD, 44)
center_text(draw, "Google Vids", 62, main_font)

# Veo 3.1 highlight
sub_font = ImageFont.truetype(FONT_BOLD, 32)
center_text(draw, "Veo 3.1 — FREE", 115, sub_font, fill=(144, 238, 144))

# Divider
draw.line([(180, 165), (420, 165)], fill=(255, 255, 255, 100), width=2)

# Details
detail_font = ImageFont.truetype(FONT_REG, 20)
center_text(draw, "10 Free Videos/Month", 178, detail_font, fill=(200, 230, 210))
center_text(draw, "720p | 8s Clips | Any Google Account", 208, detail_font, fill=(180, 215, 195))

# Year badge bottom-right
year_font = ImageFont.truetype(FONT_BOLD, 16)
draw.rounded_rectangle((W - 70, H - 45, W - 20, H - 20), radius=6, fill=(255, 255, 255, 50))
draw.text((W - 60, H - 43), "2026", font=year_font, fill="white")

# "FREE" badge bottom-left
draw.rounded_rectangle((20, H - 50, 100, H - 22), radius=6, fill=(76, 175, 80, 220))
free_font = ImageFont.truetype(FONT_BOLD, 18)
draw.text((38, H - 48), "FREE", font=free_font, fill="white")

accent_bar(draw, (76, 175, 80))
img.convert("RGB").save(f"{OUT}/google-vids-veo-free-2026-thumbnail.png")
print("Created google-vids-veo-free-2026-thumbnail.png")
