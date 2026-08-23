#!/usr/bin/env python3
"""Generate thumbnail for heygen-streaming-avatar-api-background-guide post."""

from PIL import Image, ImageDraw, ImageFont

W, H = 600, 340
OUT = "/home/tom/ai-video-tools-blog/assets/images"

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_LIGHT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"


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


# Create the thumbnail
img = Image.new("RGBA", (W, H))
draw = ImageDraw.Draw(img)

# Dark tech gradient (navy to near-black)
gradient_bg(draw, (21, 93, 252), (26, 26, 46))
circles(draw)

# Badge
badge(draw, "DEVELOPER GUIDE", (0, 180, 100))

# Title text
main_font = ImageFont.truetype(FONT_BOLD, 36)
center_text(draw, "HeyGen API", 62, main_font)

sub_font = ImageFont.truetype(FONT_BOLD, 32)
center_text(draw, "Background Colors", 105, sub_font)

# Code snippet visual
mono_font = ImageFont.truetype(FONT_MONO, 18)
code_text = '{ type: "color", value: "#hex" }'
bb = draw.textbbox((0, 0), code_text, font=mono_font)
code_w = bb[2] - bb[0] + 32
code_x = (W - code_w) // 2
draw.rounded_rectangle(
    (code_x, 160, code_x + code_w, 195),
    radius=6,
    fill=(30, 30, 46, 200)
)
center_text(draw, code_text, 164, mono_font, fill=(205, 214, 244))

# Color swatches
swatch_colors = [
    (250, 250, 250),  # #FAFAFA
    (26, 26, 46),     # #1a1a2e
    (21, 93, 252),    # #155DFC
    (0, 128, 0),      # #008000
    (0, 0, 0),        # #000000
]
swatch_y = 215
swatch_size = 30
total_w = len(swatch_colors) * (swatch_size + 12) - 12
sx = (W - total_w) // 2
for i, color in enumerate(swatch_colors):
    x = sx + i * (swatch_size + 12)
    draw.rounded_rectangle(
        (x, swatch_y, x + swatch_size, swatch_y + swatch_size),
        radius=6,
        fill=color,
        outline=(255, 255, 255, 100),
        width=2
    )

# Subtitle
info_font = ImageFont.truetype(FONT_REG, 18)
center_text(draw, "Studio API + LiveAvatar Workaround", 268, info_font, fill=(200, 210, 240))

# Year badge
year_font = ImageFont.truetype(FONT_BOLD, 16)
draw.rounded_rectangle((W - 70, H - 45, W - 20, H - 20), radius=6, fill=(255, 255, 255, 50))
draw.text((W - 60, H - 43), "2026", font=year_font, fill="white")

# Accent bar
accent_bar(draw, (0, 180, 100))

# Save
img.convert("RGB").save(f"{OUT}/heygen-streaming-avatar-api-background-guide-thumbnail.png")
print("Created heygen-streaming-avatar-api-background-guide-thumbnail.png")
