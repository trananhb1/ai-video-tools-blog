#!/usr/bin/env python3
"""Generate thumbnail and social media images for AI Video Picks blog."""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import os

OUTPUT_DIR = "/home/tom/ai-video-tools-blog/assets/images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Brand colors
DARK_BLUE = (26, 26, 46)       # #1a1a2e
ACCENT_BLUE = (21, 93, 252)    # #155DFC
WHITE = (255, 255, 255)
LIGHT_BLUE = (100, 149, 237)
MUTED_BLUE = (40, 40, 70)
DARK_BG = (15, 15, 30)

# Fonts
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
UBUNTU_BOLD = "/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf"
UBUNTU_REGULAR = "/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf"


def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()


def draw_gradient(draw, width, height, color1, color2, direction="horizontal"):
    """Draw a smooth gradient."""
    for i in range(width if direction == "horizontal" else height):
        ratio = i / (width if direction == "horizontal" else height)
        r = int(color1[0] + (color2[0] - color1[0]) * ratio)
        g = int(color1[1] + (color2[1] - color1[1]) * ratio)
        b = int(color1[2] + (color2[2] - color1[2]) * ratio)
        if direction == "horizontal":
            draw.line([(i, 0), (i, height)], fill=(r, g, b))
        else:
            draw.line([(0, i), (width, i)], fill=(r, g, b))


def draw_diagonal_gradient(img, color1, color2):
    """Draw a diagonal gradient."""
    w, h = img.size
    draw = ImageDraw.Draw(img)
    for y in range(h):
        for x in range(w):
            ratio = (x / w * 0.6 + y / h * 0.4)
            r = int(color1[0] + (color2[0] - color1[0]) * ratio)
            g = int(color1[1] + (color2[1] - color1[1]) * ratio)
            b = int(color1[2] + (color2[2] - color1[2]) * ratio)
            draw.point((x, y), fill=(r, g, b))


def draw_radial_glow(img, cx, cy, radius, color, intensity=0.8):
    """Draw a radial glow effect."""
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for r in range(radius, 0, -1):
        alpha = int(intensity * 255 * (1 - r / radius) ** 2)
        c = (*color, alpha)
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)
    img.paste(Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB"))


def text_center_x(draw, text, font, width):
    """Get x position to center text."""
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    return (width - tw) // 2


def draw_rounded_rect(draw, xy, radius, fill):
    """Draw a rounded rectangle."""
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill)


def draw_play_button(draw, cx, cy, size, fill_color, outline_color=None):
    """Draw a play button (triangle in circle)."""
    # Circle
    r = size
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=outline_color or fill_color, width=3)
    # Triangle
    tri_size = size * 0.5
    offset = tri_size * 0.15  # slight right offset for visual centering
    points = [
        (cx - tri_size * 0.4 + offset, cy - tri_size * 0.7),
        (cx - tri_size * 0.4 + offset, cy + tri_size * 0.7),
        (cx + tri_size * 0.7 + offset, cy),
    ]
    draw.polygon(points, fill=fill_color)


# ============================================================
# 1. COMPARISON THUMBNAIL (600x340)
# ============================================================
def create_comparison_thumbnail():
    w, h = 600, 340
    img = Image.new("RGB", (w, h), DARK_BLUE)
    draw = ImageDraw.Draw(img)

    # Diagonal gradient background
    for y in range(h):
        for x in range(w):
            ratio = (x / w * 0.5 + y / h * 0.5)
            r = int(DARK_BLUE[0] + (MUTED_BLUE[0] - DARK_BLUE[0]) * ratio)
            g = int(DARK_BLUE[1] + (MUTED_BLUE[1] - DARK_BLUE[1]) * ratio)
            b = int(DARK_BLUE[2] + (MUTED_BLUE[2] - DARK_BLUE[2]) * ratio)
            draw.point((x, y), fill=(r, g, b))

    # Subtle grid lines for tech feel
    for x in range(0, w, 40):
        draw.line([(x, 0), (x, h)], fill=(255, 255, 255, 8), width=1)
    for y in range(0, h, 40):
        draw.line([(0, y), (w, y)], fill=(255, 255, 255, 8), width=1)

    # Glow behind VS
    draw_radial_glow(img, w // 2, h // 2 + 15, 120, ACCENT_BLUE, 0.4)
    draw = ImageDraw.Draw(img)  # refresh draw after glow

    # "2026 COMPARISON" badge at top
    badge_font = load_font(UBUNTU_BOLD, 13)
    badge_text = "2026 COMPARISON"
    bbox = draw.textbbox((0, 0), badge_text, font=badge_font)
    bw = bbox[2] - bbox[0] + 24
    bh = bbox[3] - bbox[1] + 10
    bx = (w - bw) // 2
    by = 18
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=4, fill=ACCENT_BLUE)
    draw.text((bx + 12, by + 4), badge_text, fill=WHITE, font=badge_font)

    # Large "VS" in center
    vs_font = load_font(FONT_BOLD, 72)
    vx = text_center_x(draw, "VS", vs_font, w)
    draw.text((vx + 2, h // 2 - 38 + 2), "VS", fill=(0, 0, 0), font=vs_font)  # shadow
    draw.text((vx, h // 2 - 40), "VS", fill=ACCENT_BLUE, font=vs_font)

    # Tool names
    name_font = load_font(UBUNTU_BOLD, 26)

    # HeyGen on left
    draw.text((45, h // 2 - 15), "HeyGen", fill=WHITE, font=name_font)

    # Synthesia center-right
    bbox_s = draw.textbbox((0, 0), "Synthesia", font=name_font)
    draw.text((w // 2 + 60, h // 2 - 50), "Synthesia", fill=WHITE, font=name_font)

    # Pictory on right
    draw.text((w // 2 + 60, h // 2 + 15), "Pictory", fill=LIGHT_BLUE, font=name_font)

    # Divider lines (vertical)
    draw.line([(w // 2 - 55, h // 2 - 55), (w // 2 - 55, h // 2 + 55)], fill=(255, 255, 255, 60), width=1)
    draw.line([(w // 2 + 50, h // 2 - 55), (w // 2 + 50, h // 2 + 55)], fill=(255, 255, 255, 60), width=1)

    # Bottom tagline
    tag_font = load_font(UBUNTU_REGULAR, 14)
    tag = "Which AI Video Tool Wins?"
    tx = text_center_x(draw, tag, tag_font, w)
    draw.text((tx, h - 40), tag, fill=(180, 180, 220), font=tag_font)

    # Decorative corner accents
    draw.line([(10, 10), (40, 10)], fill=ACCENT_BLUE, width=2)
    draw.line([(10, 10), (10, 40)], fill=ACCENT_BLUE, width=2)
    draw.line([(w - 40, h - 10), (w - 10, h - 10)], fill=ACCENT_BLUE, width=2)
    draw.line([(w - 10, h - 40), (w - 10, h - 10)], fill=ACCENT_BLUE, width=2)

    img.save(os.path.join(OUTPUT_DIR, "comparison-thumbnail.png"), quality=95)
    print("Created comparison-thumbnail.png")


# ============================================================
# 2. TUTORIAL THUMBNAIL (600x340)
# ============================================================
def create_tutorial_thumbnail():
    w, h = 600, 340
    img = Image.new("RGB", (w, h), DARK_BLUE)
    draw = ImageDraw.Draw(img)

    # Blue gradient background (top-left dark to bottom-right accent)
    for y in range(h):
        for x in range(w):
            ratio = (x / w * 0.4 + y / h * 0.6)
            r = int(DARK_BLUE[0] + (35 - DARK_BLUE[0]) * ratio)
            g = int(DARK_BLUE[1] + (70 - DARK_BLUE[1]) * ratio)
            b = int(DARK_BLUE[2] + (130 - DARK_BLUE[2]) * ratio)
            draw.point((x, y), fill=(r, g, b))

    # Play button - large, centered-left area
    play_cx, play_cy = 180, h // 2
    play_r = 55

    # Glow behind play button
    draw_radial_glow(img, play_cx, play_cy, 90, ACCENT_BLUE, 0.35)
    draw = ImageDraw.Draw(img)

    # Circle outline
    draw.ellipse([play_cx - play_r, play_cy - play_r, play_cx + play_r, play_cy + play_r],
                 outline=WHITE, width=3)
    # Inner circle subtle fill
    draw.ellipse([play_cx - play_r + 4, play_cy - play_r + 4, play_cx + play_r - 4, play_cy + play_r - 4],
                 fill=(30, 50, 100))

    # Triangle
    tri_offset = 5
    tri_points = [
        (play_cx - 18 + tri_offset, play_cy - 28),
        (play_cx - 18 + tri_offset, play_cy + 28),
        (play_cx + 28 + tri_offset, play_cy),
    ]
    draw.polygon(tri_points, fill=WHITE)

    # "Step-by-Step Guide" label at top-right area
    step_font = load_font(UBUNTU_REGULAR, 16)
    draw.rounded_rectangle([310, 80, 540, 108], radius=4, fill=ACCENT_BLUE)
    draw.text((322, 84), "Step-by-Step Guide", fill=WHITE, font=step_font)

    # "HeyGen" large text
    title_font = load_font(UBUNTU_BOLD, 42)
    draw.text((310, 120), "HeyGen", fill=WHITE, font=title_font)

    # "Tutorial" below
    sub_font = load_font(UBUNTU_BOLD, 32)
    draw.text((310, 172), "Tutorial", fill=LIGHT_BLUE, font=sub_font)

    # Decorative steps indicator (dots)
    dot_y = 235
    for i in range(4):
        color = WHITE if i == 0 else (100, 100, 150)
        draw.ellipse([310 + i * 25, dot_y, 318 + i * 25, dot_y + 8], fill=color)
    step_label = load_font(UBUNTU_REGULAR, 12)
    draw.text((420, dot_y - 2), "4 Easy Steps", fill=(150, 150, 190), font=step_label)

    # Bottom bar
    draw.rectangle([0, h - 4, w, h], fill=ACCENT_BLUE)

    # Corner accents
    draw.line([(10, 10), (40, 10)], fill=ACCENT_BLUE, width=2)
    draw.line([(10, 10), (10, 40)], fill=ACCENT_BLUE, width=2)

    img.save(os.path.join(OUTPUT_DIR, "tutorial-thumbnail.png"), quality=95)
    print("Created tutorial-thumbnail.png")


# ============================================================
# 3. COMING SOON THUMBNAIL (600x340)
# ============================================================
def create_coming_soon_thumbnail():
    w, h = 600, 340
    img = Image.new("RGB", (w, h), DARK_BG)
    draw = ImageDraw.Draw(img)

    # Dark muted gradient
    for y in range(h):
        ratio = y / h
        r = int(15 + (30 - 15) * ratio)
        g = int(15 + (25 - 15) * ratio)
        b = int(30 + (50 - 30) * ratio)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

    # Subtle radial glow from center
    draw_radial_glow(img, w // 2, h // 2, 200, (30, 40, 80), 0.3)
    draw = ImageDraw.Draw(img)

    # "TOP 10" large text
    top_font = load_font(FONT_BOLD, 80)
    tx = text_center_x(draw, "TOP 10", top_font, w)
    # Shadow
    draw.text((tx + 3, 65 + 3), "TOP 10", fill=(0, 0, 20), font=top_font)
    draw.text((tx, 65), "TOP 10", fill=WHITE, font=top_font)

    # "Best AI Video Tools 2026" subtitle
    sub_font = load_font(UBUNTU_BOLD, 22)
    sub_text = "Best AI Video Tools 2026"
    sx = text_center_x(draw, sub_text, sub_font, w)
    draw.text((sx, 165), sub_text, fill=LIGHT_BLUE, font=sub_font)

    # "COMING SOON" overlay - semi-transparent ribbon
    ribbon_y = 220
    # Ribbon background
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.rectangle([0, ribbon_y, w, ribbon_y + 55], fill=(21, 93, 252, 200))
    img_rgba = img.convert("RGBA")
    img = Image.alpha_composite(img_rgba, overlay).convert("RGB")
    draw = ImageDraw.Draw(img)

    cs_font = load_font(UBUNTU_BOLD, 30)
    cs_text = "COMING SOON"
    cx = text_center_x(draw, cs_text, cs_font, w)
    draw.text((cx, ribbon_y + 10), cs_text, fill=WHITE, font=cs_font)

    # Decorative stars/dots
    star_font = load_font(FONT_REGULAR, 18)
    for i in range(5):
        sx = 180 + i * 60
        draw.text((sx, 295), "\u2605", fill=(80, 80, 130), font=star_font)

    # Corner accents
    draw.line([(10, 10), (50, 10)], fill=(60, 60, 100), width=1)
    draw.line([(10, 10), (10, 50)], fill=(60, 60, 100), width=1)
    draw.line([(w - 50, h - 10), (w - 10, h - 10)], fill=(60, 60, 100), width=1)
    draw.line([(w - 10, h - 50), (w - 10, h - 10)], fill=(60, 60, 100), width=1)

    img.save(os.path.join(OUTPUT_DIR, "coming-soon-thumbnail.png"), quality=95)
    print("Created coming-soon-thumbnail.png")


# ============================================================
# 4. TWITTER PROFILE (400x400)
# ============================================================
def create_twitter_profile():
    w, h = 400, 400
    img = Image.new("RGB", (w, h), DARK_BLUE)
    draw = ImageDraw.Draw(img)

    # Subtle radial gradient from center
    for y in range(h):
        for x in range(w):
            dist = math.sqrt((x - w // 2) ** 2 + (y - h // 2) ** 2)
            max_dist = math.sqrt((w // 2) ** 2 + (h // 2) ** 2)
            ratio = min(dist / max_dist, 1.0)
            r = int(35 + (DARK_BLUE[0] - 35) * ratio)
            g = int(35 + (DARK_BLUE[1] - 35) * ratio)
            b = int(60 + (DARK_BLUE[2] - 60) * ratio)
            draw.point((x, y), fill=(r, g, b))

    cx, cy = w // 2, h // 2 - 15

    # Play button - large triangle in circle
    r = 100
    # Circle with accent blue
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=ACCENT_BLUE, width=5)

    # Filled triangle
    tri_offset = 8
    tri_points = [
        (cx - 35 + tri_offset, cy - 50),
        (cx - 35 + tri_offset, cy + 50),
        (cx + 55 + tri_offset, cy),
    ]
    draw.polygon(tri_points, fill=ACCENT_BLUE)

    # "AVP" text below
    avp_font = load_font(UBUNTU_BOLD, 36)
    avp_x = text_center_x(draw, "AVP", avp_font, w)
    draw.text((avp_x, cy + r + 20), "AVP", fill=WHITE, font=avp_font)

    img.save(os.path.join(OUTPUT_DIR, "twitter-profile.png"), quality=95)
    print("Created twitter-profile.png")


# ============================================================
# 5. TWITTER HEADER (1500x500)
# ============================================================
def create_twitter_header():
    w, h = 1500, 500
    img = Image.new("RGB", (w, h), DARK_BLUE)
    draw = ImageDraw.Draw(img)

    # Horizontal gradient: dark blue to accent blue
    for x in range(w):
        ratio = x / w
        # Ease-in curve for smoother gradient
        ratio = ratio ** 0.7
        r = int(DARK_BLUE[0] + (ACCENT_BLUE[0] - DARK_BLUE[0]) * ratio)
        g = int(DARK_BLUE[1] + (ACCENT_BLUE[1] - DARK_BLUE[1]) * ratio)
        b = int(DARK_BLUE[2] + (ACCENT_BLUE[2] - DARK_BLUE[2]) * ratio)
        draw.line([(x, 0), (x, h)], fill=(r, g, b))

    # Subtle geometric pattern (diagonal lines)
    for i in range(-h, w + h, 80):
        draw.line([(i, 0), (i + h, h)], fill=(255, 255, 255, 15), width=1)

    # Play button icon on the left
    play_cx, play_cy = 200, h // 2
    play_r = 50
    draw.ellipse([play_cx - play_r, play_cy - play_r, play_cx + play_r, play_cy + play_r],
                 outline=WHITE, width=3)
    tri_points = [
        (play_cx - 15 + 5, play_cy - 25),
        (play_cx - 15 + 5, play_cy + 25),
        (play_cx + 28 + 5, play_cy),
    ]
    draw.polygon(tri_points, fill=WHITE)

    # "AI Video Picks" - main title
    title_font = load_font(UBUNTU_BOLD, 72)
    draw.text((320, h // 2 - 70), "AI Video Picks", fill=WHITE, font=title_font)

    # Tagline
    tag_font = load_font(UBUNTU_REGULAR, 26)
    tagline = "Honest Reviews & Comparisons of AI Video Tools"
    draw.text((325, h // 2 + 25), tagline, fill=(200, 210, 240), font=tag_font)

    # Decorative underline
    draw.rectangle([325, h // 2 + 15, 600, h // 2 + 19], fill=ACCENT_BLUE)

    # Small decorative dots on right side
    for i in range(5):
        dx = w - 100 - i * 30
        dy = h // 2 + 10 * math.sin(i * 1.2)
        draw.ellipse([dx - 4, dy - 4, dx + 4, dy + 4], fill=(255, 255, 255, 80))

    img.save(os.path.join(OUTPUT_DIR, "twitter-header.png"), quality=95)
    print("Created twitter-header.png")


# ============================================================
# Generate all images
# ============================================================
if __name__ == "__main__":
    print("Generating AI Video Picks assets...\n")
    create_comparison_thumbnail()
    create_tutorial_thumbnail()
    create_coming_soon_thumbnail()
    create_twitter_profile()
    create_twitter_header()
    print(f"\nAll images saved to {OUTPUT_DIR}/")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        if f.endswith(".png"):
            size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
            img = Image.open(os.path.join(OUTPUT_DIR, f))
            print(f"  {f}: {img.size[0]}x{img.size[1]} ({size:,} bytes)")
