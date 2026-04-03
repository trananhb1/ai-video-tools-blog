#!/usr/bin/env python3
"""Generate thumbnails for all 12 new blog posts on aivideopicks.com."""

from PIL import Image, ImageDraw, ImageFont

W, H = 600, 340
OUT = "/home/tom/ai-video-tools-blog/assets/images"

FONT_BOLD = "/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf"
FONT_REG = "/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf"
FONT_LIGHT = "/usr/share/fonts/truetype/ubuntu/Ubuntu-L.ttf"
FONT_STAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


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


def save(img, name):
    img.convert("RGB").save(f"{OUT}/{name}")
    print(f"  Created {name}")


def stars(draw, rating, y):
    font = ImageFont.truetype(FONT_STAR, 28)
    total_w = 5 * 36
    sx = (W - total_w) // 2
    full = int(rating)
    for i in range(5):
        color = (255, 215, 0) if i < full else (255, 215, 0, 80)
        draw.text((sx + i * 36, y), "\u2605", font=font, fill=color)
    rf = ImageFont.truetype(FONT_BOLD, 22)
    center_text(draw, f"{rating} / 10", y + 38, rf, fill=(255, 215, 0))


# ── REVIEW TEMPLATE ──────────────────────────────────────────────────
def make_review(name, filename, rating, grad_c1, grad_c2, bar_color, badge_color):
    img = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(img)
    gradient_bg(draw, grad_c1, grad_c2)
    circles(draw)
    badge(draw, "IN-DEPTH REVIEW", badge_color)
    main_font = ImageFont.truetype(FONT_BOLD, 60)
    center_text(draw, name, 65, main_font)
    stars(draw, rating, 145)
    sub_font = ImageFont.truetype(FONT_REG, 20)
    center_text(draw, "AI Video Platform Review", 225, sub_font, fill=(200, 220, 255))
    year_font = ImageFont.truetype(FONT_BOLD, 16)
    draw.rounded_rectangle((W - 70, H - 45, W - 20, H - 20), radius=6, fill=(255, 255, 255, 50))
    draw.text((W - 60, H - 43), "2026", font=year_font, fill="white")
    accent_bar(draw, bar_color)
    save(img, filename)


# ── COMPARISON TEMPLATE ──────────────────────────────────────────────
def make_comparison(tools, filename, grad_c1, grad_c2, bar_color):
    img = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(img)
    gradient_bg(draw, grad_c1, grad_c2)
    circles(draw)
    badge(draw, "HEAD-TO-HEAD COMPARISON", (255, 140, 0))

    # Tool names with "vs" between them
    vs_font = ImageFont.truetype(FONT_LIGHT, 24)
    if len(tools) == 3:
        main_font = ImageFont.truetype(FONT_BOLD, 38)
        center_text(draw, tools[0], 62, main_font)
        center_text(draw, "vs", 105, vs_font, fill=(255, 215, 0))
        center_text(draw, tools[1], 132, main_font)
        center_text(draw, "vs", 175, vs_font, fill=(255, 215, 0))
        center_text(draw, tools[2], 202, main_font)
    else:
        main_font = ImageFont.truetype(FONT_BOLD, 44)
        center_text(draw, tools[0], 75, main_font)
        center_text(draw, "vs", 125, vs_font, fill=(255, 215, 0))
        center_text(draw, tools[1], 155, main_font)

    sub_font = ImageFont.truetype(FONT_REG, 18)
    center_text(draw, "Which One Wins in 2026?", H - 80, sub_font, fill=(200, 210, 255))
    accent_bar(draw, bar_color)
    save(img, filename)


# ── GUIDE/TUTORIAL TEMPLATE ──────────────────────────────────────────
def make_guide(title, subtitle, filename, grad_c1, grad_c2, bar_color, badge_text="COMPLETE GUIDE", badge_color=(100, 100, 255)):
    img = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(img)
    gradient_bg(draw, grad_c1, grad_c2)
    circles(draw)
    badge(draw, badge_text, badge_color)

    # Wrap title text
    main_font = ImageFont.truetype(FONT_BOLD, 42)
    lines = wrap_text(title, main_font, W - 60, draw)
    y_start = 70 if len(lines) <= 2 else 55
    for i, line in enumerate(lines):
        center_text(draw, line, y_start + i * 52, main_font)

    # Divider
    div_y = y_start + len(lines) * 52 + 10
    draw.line([(180, div_y), (420, div_y)], fill=(255, 255, 255, 100), width=2)

    # Subtitle
    sub_font = ImageFont.truetype(FONT_REG, 20)
    sub_lines = wrap_text(subtitle, sub_font, W - 60, draw)
    for i, line in enumerate(sub_lines):
        center_text(draw, line, div_y + 18 + i * 28, sub_font, fill=(200, 210, 240))

    accent_bar(draw, bar_color)
    save(img, filename)


# ── GENERATE ALL 12 THUMBNAILS ───────────────────────────────────────

print("Generating thumbnails for 12 new posts...\n")

# 1. Sora Alternatives (urgent/timely - red/orange theme)
img = Image.new("RGBA", (W, H))
draw = ImageDraw.Draw(img)
gradient_bg(draw, (180, 30, 20), (40, 10, 10))
circles(draw)
badge(draw, "BREAKING NEWS", (220, 50, 30))
main_font = ImageFont.truetype(FONT_BOLD, 42)
center_text(draw, "SORA IS DEAD", 62, main_font, fill=(255, 100, 80))
sub_font = ImageFont.truetype(FONT_BOLD, 36)
center_text(draw, "7 Best Alternatives", 125, sub_font)
divider_y = 180
draw.line([(180, divider_y), (420, divider_y)], fill=(255, 255, 255, 100), width=2)
detail_font = ImageFont.truetype(FONT_REG, 22)
center_text(draw, "Veo \u2022 Kling \u2022 Runway \u2022 Pika", 195, detail_font, fill=(255, 180, 170))
center_text(draw, "Wan \u2022 Seedance \u2022 Vidu", 225, detail_font, fill=(255, 180, 170))
year_font = ImageFont.truetype(FONT_BOLD, 16)
draw.rounded_rectangle((W - 90, H - 45, W - 20, H - 20), radius=6, fill=(255, 255, 255, 50))
draw.text((W - 80, H - 43), "MAR 2026", font=year_font, fill="white")
accent_bar(draw, (220, 50, 30))
save(img, "sora-alternatives-thumbnail.png")

# 2. Runway Review
make_review("RUNWAY", "runway-review-thumbnail.png", 8.5,
            (20, 20, 80), (10, 10, 30), (100, 80, 220), (100, 80, 220))

# 3. Turn Long Videos into Shorts (Opus Clip)
make_guide("Turn Long Videos", "Into Viral Shorts with AI",
           "shorts-repurpose-thumbnail.png",
           (200, 50, 120), (30, 10, 40),
           (200, 50, 120), "STEP-BY-STEP TUTORIAL", (200, 50, 120))

# 4. Kling vs Veo vs Runway
make_comparison(["Kling 3.0", "Google Veo 3.1", "Runway Gen-4.5"],
                "kling-veo-runway-thumbnail.png",
                (20, 50, 100), (10, 15, 40), (50, 130, 220))

# 5. Best Free AI Video Generators
img = Image.new("RGBA", (W, H))
draw = ImageDraw.Draw(img)
gradient_bg(draw, (20, 130, 80), (10, 30, 20))
circles(draw)
badge(draw, "ACTUALLY TESTED", (16, 185, 129))
main_font = ImageFont.truetype(FONT_BOLD, 48)
center_text(draw, "BEST FREE", 65, main_font)
center_text(draw, "AI VIDEO TOOLS", 120, main_font)
free_font = ImageFont.truetype(FONT_BOLD, 72)
center_text(draw, "$0", 185, free_font, fill=(16, 220, 140))
sub_font = ImageFont.truetype(FONT_REG, 20)
center_text(draw, "8 Tools Ranked \u2022 2026 Edition", H - 75, sub_font, fill=(180, 240, 210))
accent_bar(draw, (16, 185, 129))
save(img, "free-ai-video-thumbnail.png")

# 6. Fliki Review
make_review("FLIKI", "fliki-review-thumbnail.png", 7.8,
            (130, 50, 20), (30, 15, 5), (200, 120, 50), (200, 120, 50))

# 7. VEED vs Kapwing vs Descript
make_comparison(["VEED.io", "Kapwing", "Descript"],
                "veed-kapwing-descript-thumbnail.png",
                (80, 20, 120), (20, 10, 40), (140, 60, 200))

# 8. AI Training & Onboarding Videos
make_guide("AI Training Videos", "Create Onboarding Content Without a Camera",
           "ai-training-thumbnail.png",
           (30, 60, 130), (10, 20, 50),
           (50, 100, 200), "BUSINESS USE CASE", (50, 100, 200))

# 9. D-ID vs Elai vs HourOne
make_comparison(["D-ID", "Elai", "HourOne"],
                "did-elai-hourone-thumbnail.png",
                (60, 20, 90), (15, 10, 30), (120, 60, 180))

# 10. AI Video Pricing Compared
img = Image.new("RGBA", (W, H))
draw = ImageDraw.Draw(img)
gradient_bg(draw, (30, 80, 30), (10, 25, 10))
circles(draw)
badge(draw, "PRICING BREAKDOWN", (40, 160, 80))
main_font = ImageFont.truetype(FONT_BOLD, 44)
center_text(draw, "AI VIDEO PRICING", 62, main_font)
dollar_font = ImageFont.truetype(FONT_BOLD, 80)
center_text(draw, "$$$", 120, dollar_font, fill=(80, 220, 120))
sub_font = ImageFont.truetype(FONT_BOLD, 28)
center_text(draw, "10 Tools Compared", 210, sub_font, fill=(160, 240, 180))
detail_font = ImageFont.truetype(FONT_REG, 18)
center_text(draw, "Hidden Costs \u2022 Credits vs Subs \u2022 Best Value", H - 75, detail_font, fill=(150, 220, 170))
accent_bar(draw, (40, 160, 80))
save(img, "pricing-compared-thumbnail.png")

# 11. AI Tools for YouTube Creators
make_guide("AI Tools for", "Complete 2026 YouTube Creator Workflow",
           "youtube-creators-thumbnail.png",
           (180, 20, 20), (50, 5, 5),
           (220, 40, 40), "CREATOR WORKFLOW", (220, 40, 40))

# 12. What Is Text-to-Video AI
make_guide("What Is", "A Beginner's Guide to How It Works",
           "text-to-video-explainer-thumbnail.png",
           (50, 30, 100), (15, 10, 35),
           (100, 70, 180), "BEGINNER'S GUIDE", (100, 70, 180))
# Fix: add "Text-to-Video AI?" as large text
img = Image.new("RGBA", (W, H))
draw = ImageDraw.Draw(img)
gradient_bg(draw, (50, 30, 100), (15, 10, 35))
circles(draw)
badge(draw, "BEGINNER'S GUIDE", (100, 70, 180))
q_font = ImageFont.truetype(FONT_BOLD, 28)
center_text(draw, "What Is", 62, q_font, fill=(180, 180, 255))
main_font = ImageFont.truetype(FONT_BOLD, 44)
center_text(draw, "Text-to-Video AI?", 100, main_font)
draw.line([(180, 165), (420, 165)], fill=(255, 255, 255, 100), width=2)
sub_font = ImageFont.truetype(FONT_REG, 22)
center_text(draw, "How It Works \u2022 Key Terms", 180, sub_font, fill=(180, 180, 240))
center_text(draw, "Getting Started \u2022 2026 Guide", 210, sub_font, fill=(180, 180, 240))
# Tech icons represented as text
icon_font = ImageFont.truetype(FONT_LIGHT, 16)
center_text(draw, "Diffusion \u2022 Transformers \u2022 Neural Networks", H - 70, icon_font, fill=(150, 150, 220))
accent_bar(draw, (100, 70, 180))
save(img, "text-to-video-explainer-thumbnail.png")

# 13. Opus Clip Review
make_review("OPUS CLIP", "opus-clip-review-thumbnail.png", 8.5,
            (160, 30, 90), (40, 10, 25), (200, 50, 120), (200, 50, 120))

# 14. Synthesia Review
make_review("SYNTHESIA", "synthesia-review-thumbnail.png", 8.0,
            (20, 60, 120), (10, 20, 40), (40, 100, 200), (40, 100, 200))

# 15. Murf AI Review
make_review("MURF AI", "murf-ai-review-thumbnail.png", 8.0,
            (80, 30, 130), (25, 10, 45), (120, 60, 200), (120, 60, 200))

# 16. AI Video for Social Media (Guide)
make_guide("AI Video for", "How to Create Scroll-Stopping Social Content",
           "ai-video-social-media-thumbnail.png",
           (20, 80, 140), (10, 25, 50),
           (30, 120, 200), "SOCIAL MEDIA GUIDE", (30, 120, 200))

print("\nAll 16 thumbnails generated!")
