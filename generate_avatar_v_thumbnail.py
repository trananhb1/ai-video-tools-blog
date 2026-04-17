#!/usr/bin/env python3
"""Generate thumbnail for HeyGen Avatar V guide post."""

from PIL import Image, ImageDraw, ImageFont

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


def center_text(draw, text, y, font, fill="white"):
    bb = draw.textbbox((0, 0), text, font=font)
    x = (W - (bb[2] - bb[0])) // 2
    draw.text((x, y), text, font=font, fill=fill)


def accent_bar(draw, color):
    draw.rectangle([(0, H - 6), (W, H)], fill=color)


img = Image.new("RGBA", (W, H))
draw = ImageDraw.Draw(img)

# Deep blue to purple gradient (premium feel)
gradient_bg(draw, (21, 93, 252), (88, 28, 135))
circles(draw)

# Badge
badge_font = ImageFont.truetype(FONT_BOLD, 14)
badge_text = "NEW — APRIL 2026"
bb = draw.textbbox((0, 0), badge_text, font=badge_font)
bw = bb[2] - bb[0] + 24
bx = (W - bw) // 2
draw.rounded_rectangle((bx, 20, bx + bw, 48), radius=8, fill=(255, 140, 0, 220))
draw.text((bx + 12, 23), badge_text, font=badge_font, fill="white")

# Main title
main_font = ImageFont.truetype(FONT_BOLD, 52)
center_text(draw, "HeyGen", 60, main_font)

sub_main = ImageFont.truetype(FONT_BOLD, 48)
center_text(draw, "Avatar V", 118, sub_main, fill=(255, 215, 0))

# Subtitle
sub_font = ImageFont.truetype(FONT_REG, 20)
center_text(draw, "Full Guide + What's New", 185, sub_font, fill=(200, 210, 255))

# Key stat
stat_font = ImageFont.truetype(FONT_BOLD, 18)
center_text(draw, "0.840 Face Similarity | 15-Sec Setup", 225, stat_font, fill=(180, 200, 255))

# Bottom info
info_font = ImageFont.truetype(FONT_REG, 16)
center_text(draw, "Seedance 2.0 | Multi-Angle | 30+ Min Stability", 265, info_font, fill=(160, 180, 220))

# Year badge bottom right
year_font = ImageFont.truetype(FONT_BOLD, 16)
draw.rounded_rectangle((W - 70, H - 45, W - 20, H - 20), radius=6, fill=(255, 255, 255, 50))
draw.text((W - 60, H - 43), "2026", font=year_font, fill="white")

# Accent bar
accent_bar(draw, (255, 140, 0))

img.convert("RGB").save(f"{OUT}/heygen-avatar-v-guide-2026-thumbnail.png")
print("Created heygen-avatar-v-guide-2026-thumbnail.png")
