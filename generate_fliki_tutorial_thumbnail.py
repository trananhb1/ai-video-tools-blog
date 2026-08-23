#!/usr/bin/env python3
"""Generate thumbnail for How to Turn Blog Posts Into Videos with Fliki AI tutorial."""

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


# ── Generate tutorial thumbnail ──
img = Image.new("RGBA", (W, H))
draw = ImageDraw.Draw(img)

# Green gradient: #1b5e20 to #004d40
gradient_bg(draw, (27, 94, 32), (0, 77, 64))
circles(draw)

# Badge
badge(draw, "BLOG TO VIDEO", (76, 175, 80))

# Main text: "Fliki"
main_font = ImageFont.truetype(FONT_BOLD, 64)
center_text(draw, "Fliki", 65, main_font)

# Subtitle
sub_font = ImageFont.truetype(FONT_REG, 22)
center_text(draw, "Turn Blog Posts Into Videos", 145, sub_font, fill=(200, 255, 210))

# Workflow icons / step indicators
step_font = ImageFont.truetype(FONT_BOLD, 16)
step_y = 195
steps = ["1. Paste URL", "2. AI Scenes", "3. Voice", "4. Export"]
total_w = sum(draw.textbbox((0, 0), s, font=step_font)[2] - draw.textbbox((0, 0), s, font=step_font)[0] for s in steps)
gap = 28
total_w += gap * (len(steps) - 1)
sx = (W - total_w) // 2

for i, step in enumerate(steps):
    bb = draw.textbbox((0, 0), step, font=step_font)
    sw = bb[2] - bb[0]
    # Draw pill background
    draw.rounded_rectangle((sx - 8, step_y - 4, sx + sw + 8, step_y + 22), radius=6, fill=(255, 255, 255, 40))
    draw.text((sx, step_y), step, font=step_font, fill="white")
    sx += sw + gap

# "Step-by-Step Tutorial" line
tut_font = ImageFont.truetype(FONT_REG, 18)
center_text(draw, "Step-by-Step Tutorial", 240, tut_font, fill=(180, 255, 200))

# Year badge
year_font = ImageFont.truetype(FONT_BOLD, 16)
draw.rounded_rectangle((W - 70, H - 45, W - 20, H - 20), radius=6, fill=(255, 255, 255, 50))
draw.text((W - 60, H - 43), "2026", font=year_font, fill="white")

# Brand
brand_font = ImageFont.truetype(FONT_LIGHT, 12)
center_text(draw, "aivideopicks.com", 290, brand_font, fill=(200, 255, 210))

# Green accent bar
accent_bar(draw, (76, 175, 80))

# Save
img.convert("RGB").save(f"{OUT}/how-to-turn-blog-into-video-fliki-2026-thumbnail.png")
print("Created how-to-turn-blog-into-video-fliki-2026-thumbnail.png")
