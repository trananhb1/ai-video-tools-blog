#!/usr/bin/env python3
"""Generate 600x340 thumbnails with app logos for the 3 new GSC-gap articles."""

import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os

OUT_DIR = "assets/images"
W, H = 600, 340
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

_logo_cache = {}

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def make_gradient(w, h, top_color, bottom_color):
    img = Image.new('RGB', (w, h))
    r1, g1, b1 = hex_to_rgb(top_color)
    r2, g2, b2 = hex_to_rgb(bottom_color)
    for y in range(h):
        ratio = y / h
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        for x in range(w):
            img.putpixel((x, y), (r, g, b))
    return img

def fetch_logo(domain, target_size=80):
    if domain in _logo_cache:
        logo = _logo_cache[domain]
        return logo.copy() if logo else None

    sources = [
        f"https://icon.horse/icon/{domain}?size=large",
        f"https://favicone.com/{domain}?s=128",
        f"https://www.google.com/s2/favicons?domain={domain}&sz=128",
    ]
    best_logo, best_size = None, 0
    for url in sources:
        try:
            r = requests.get(url, timeout=10, allow_redirects=True)
            if r.status_code == 200 and len(r.content) > 200:
                logo = Image.open(BytesIO(r.content)).convert("RGBA")
                w, h = logo.size
                if w > best_size:
                    best_size = w
                    best_logo = logo
                if w >= 128:
                    break
        except Exception:
            continue

    _logo_cache[domain] = best_logo
    return best_logo.copy() if best_logo else None

def draw_logo_row(img, draw, domains, names, logo_size, y_pos):
    circle_size = logo_size + 14
    n = len(domains)
    spacing = 10
    total = circle_size * n + spacing * (n - 1)
    start_x = (W - total) // 2
    label_font = ImageFont.truetype(FONT_REG, 10)

    for i, (domain, name) in enumerate(zip(domains, names)):
        x = start_x + i * (circle_size + spacing)
        logo = fetch_logo(domain) if domain else None
        cb = Image.new('RGBA', (circle_size, circle_size), (0, 0, 0, 0))
        cd = ImageDraw.Draw(cb)
        cd.ellipse([0, 0, circle_size - 1, circle_size - 1], fill=(255, 255, 255, 255))
        if logo:
            logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
            cb.paste(logo, (7, 7), logo)
        else:
            # Fallback: first letter in circle
            letter_font = ImageFont.truetype(FONT_BOLD, logo_size // 2)
            cd.text((circle_size // 2, circle_size // 2), name[0], fill=(80, 80, 80), font=letter_font, anchor="mm")
        img.paste(cb, (x, y_pos), cb)
        draw.text((x + circle_size // 2, y_pos + circle_size + 4), name, fill=(200, 210, 230), font=label_font, anchor="mt")


# ── 1. HeyGen Streaming Avatar API ──
def gen_heygen_api():
    img = make_gradient(W, H, "#0d47a1", "#1a237e")
    draw = ImageDraw.Draw(img)
    draw.ellipse([W-90, -30, W+30, 90], outline=(100, 181, 246, 80), width=2)
    draw.ellipse([-30, H-90, 90, H+30], outline=(100, 181, 246, 80), width=2)

    # HeyGen logo centered
    logo = fetch_logo("heygen.com")
    if logo:
        logo = logo.resize((70, 70), Image.LANCZOS)
        cb = Image.new('RGBA', (90, 90), (0, 0, 0, 0))
        cd = ImageDraw.Draw(cb)
        cd.ellipse([0, 0, 89, 89], fill=(255, 255, 255, 255))
        cb.paste(logo, (10, 10), logo)
        img.paste(cb, (W // 2 - 45, 15), cb)

    # Badge
    badge_font = ImageFont.truetype(FONT_BOLD, 11)
    badge_text = "DEVELOPER GUIDE"
    bbox = draw.textbbox((0, 0), badge_text, font=badge_font)
    bw = bbox[2] - bbox[0] + 20
    bh = bbox[3] - bbox[1] + 10
    bx = (W - bw) // 2
    by = 115
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=4, fill=(76, 175, 80))
    draw.text((W // 2, by + bh // 2), badge_text, fill=(255, 255, 255), font=badge_font, anchor="mm")

    # Title
    title_font = ImageFont.truetype(FONT_BOLD, 28)
    draw.text((W // 2, 150), "HeyGen API", fill=(255, 255, 255), font=title_font, anchor="mt")
    draw.text((W // 2, 185), "Background Colors", fill=(255, 255, 255), font=title_font, anchor="mt")

    # Code snippet
    code_font = ImageFont.truetype(FONT_REG, 14)
    code = '{ type: "color", value: "#hex" }'
    bbox = draw.textbbox((0, 0), code, font=code_font)
    cw = bbox[2] - bbox[0] + 20
    ch = bbox[3] - bbox[1] + 12
    cx = (W - cw) // 2
    cy = 228
    draw.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=6, fill=(30, 30, 60))
    draw.text((W // 2, cy + ch // 2), code, fill=(130, 230, 130), font=code_font, anchor="mm")

    # Color swatches
    colors = ["#FAFAFA", "#1a1a2e", "#0d47a1", "#008000", "#000000"]
    swatch_size = 22
    total_sw = len(colors) * (swatch_size + 6)
    sx = (W - total_sw) // 2
    sy = 265
    for i, c in enumerate(colors):
        x = sx + i * (swatch_size + 6)
        draw.rounded_rectangle([x, sy, x + swatch_size, sy + swatch_size], radius=4, fill=hex_to_rgb(c), outline=(200, 200, 200), width=1)

    # Subtitle
    sub_font = ImageFont.truetype(FONT_REG, 12)
    draw.text((W // 2, 300), "Studio API + LiveAvatar Workaround", fill=(180, 190, 210), font=sub_font, anchor="mt")

    # Brand
    brand_font = ImageFont.truetype(FONT_REG, 10)
    draw.text((W // 2, H - 10), "aivideopicks.com", fill=(120, 130, 150), font=brand_font, anchor="mb")

    img.convert("RGB").save(os.path.join(OUT_DIR, "heygen-streaming-avatar-api-background-guide-thumbnail.png"), "PNG", optimize=True)
    print("  -> heygen-streaming-avatar-api-background-guide-thumbnail.png")


# ── 2. Best AI Image-to-Video Generators ──
def gen_image_to_video():
    img = make_gradient(W, H, "#1a1a2e", "#4a148c")
    draw = ImageDraw.Draw(img)
    draw.ellipse([W-90, -30, W+30, 90], outline=(206, 147, 216, 80), width=2)
    draw.ellipse([-30, H-90, 90, H+30], outline=(206, 147, 216, 80), width=2)

    # Badge
    badge_font = ImageFont.truetype(FONT_BOLD, 11)
    badge_text = "7 TOOLS TESTED  |  2026"
    bbox = draw.textbbox((0, 0), badge_text, font=badge_font)
    bw = bbox[2] - bbox[0] + 20
    bh = bbox[3] - bbox[1] + 10
    bx = (W - bw) // 2
    by = 15
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=4, fill=(255, 140, 0))
    draw.text((W // 2, by + bh // 2), badge_text, fill=(255, 255, 255), font=badge_font, anchor="mm")

    # Title
    title_font = ImageFont.truetype(FONT_BOLD, 30)
    draw.text((W // 2, 48), "Best AI Image-to-Video", fill=(255, 255, 255), font=title_font, anchor="mt")
    sub_title = ImageFont.truetype(FONT_BOLD, 26)
    draw.text((W // 2, 85), "Generators", fill=(206, 147, 216), font=sub_title, anchor="mt")

    # Divider
    draw.line([(W // 2 - 50, 122), (W // 2 + 50, 122)], fill=(206, 147, 216), width=2)

    # Logo row
    domains = ["runwayml.com", "klingai.com", "google.com", "pixverse.ai", "lumalabs.ai", "seedance.ai", "hailuoai.com"]
    names = ["Runway", "Kling", "Veo", "PixVerse", "Luma", "Seedance", "Hailuo"]
    draw_logo_row(img, draw, domains, names, 42, 135)

    # Bottom info
    info_font = ImageFont.truetype(FONT_BOLD, 14)
    draw.text((W // 2, 275), "Free & Paid  |  Quality Compared", fill=(230, 220, 255), font=info_font, anchor="mt")

    brand_font = ImageFont.truetype(FONT_REG, 10)
    draw.text((W // 2, H - 10), "aivideopicks.com", fill=(150, 150, 170), font=brand_font, anchor="mb")

    img.convert("RGB").save(os.path.join(OUT_DIR, "best-ai-image-to-video-generators-2026-thumbnail.png"), "PNG", optimize=True)
    print("  -> best-ai-image-to-video-generators-2026-thumbnail.png")


# ── 3. Free AI Video Generators for YouTube ──
def gen_youtube_free():
    img = make_gradient(W, H, "#b71c1c", "#880e4f")
    draw = ImageDraw.Draw(img)
    draw.ellipse([W-90, -30, W+30, 90], outline=(255, 200, 200, 80), width=2)
    draw.ellipse([-30, H-90, 90, H+30], outline=(255, 200, 200, 80), width=2)

    # Badge
    badge_font = ImageFont.truetype(FONT_BOLD, 11)
    badge_text = "FREE TOOLS FOR YOUTUBE"
    bbox = draw.textbbox((0, 0), badge_text, font=badge_font)
    bw = bbox[2] - bbox[0] + 20
    bh = bbox[3] - bbox[1] + 10
    bx = (W - bw) // 2
    by = 15
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=4, fill=(229, 57, 53))
    draw.text((W // 2, by + bh // 2), badge_text, fill=(255, 255, 255), font=badge_font, anchor="mm")

    # Title
    title_font = ImageFont.truetype(FONT_BOLD, 28)
    draw.text((W // 2, 48), "Free AI Video Generators", fill=(255, 255, 255), font=title_font, anchor="mt")
    sub_title = ImageFont.truetype(FONT_BOLD, 24)
    draw.text((W // 2, 83), "for YouTube", fill=(255, 200, 200), font=sub_title, anchor="mt")

    # Divider
    draw.line([(W // 2 - 50, 118), (W // 2 + 50, 118)], fill=(255, 200, 200), width=2)

    # Logo row — top 7 tools
    domains = ["capcut.com", "google.com", "klingai.com", "invideo.io", "fliki.ai", "vidnoz.com", "descript.com"]
    names = ["CapCut", "Veo", "Kling", "InVideo", "Fliki", "Vidnoz", "Descript"]
    draw_logo_row(img, draw, domains, names, 42, 130)

    # Bottom pills
    pill_font = ImageFont.truetype(FONT_BOLD, 11)
    pills = ["No Watermark", "1080p", "YPP-Safe"]
    total_pw = sum(draw.textbbox((0, 0), t, font=pill_font)[2] - draw.textbbox((0, 0), t, font=pill_font)[0] + 20 for t in pills) + 10 * (len(pills) - 1)
    px = (W - total_pw) // 2
    py = 270
    for t in pills:
        bbox = draw.textbbox((0, 0), t, font=pill_font)
        pw = bbox[2] - bbox[0] + 20
        ph = bbox[3] - bbox[1] + 10
        draw.rounded_rectangle([px, py, px + pw, py + ph], radius=6, fill=(255, 255, 255, 50))
        draw.text((px + pw // 2, py + ph // 2), t, fill=(255, 255, 255), font=pill_font, anchor="mm")
        px += pw + 10

    brand_font = ImageFont.truetype(FONT_REG, 10)
    draw.text((W // 2, H - 10), "aivideopicks.com", fill=(200, 180, 180), font=brand_font, anchor="mb")

    img.convert("RGB").save(os.path.join(OUT_DIR, "free-ai-video-generators-youtube-2026-thumbnail.png"), "PNG", optimize=True)
    print("  -> free-ai-video-generators-youtube-2026-thumbnail.png")


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    print("Generating thumbnails with app logos...")
    gen_heygen_api()
    gen_image_to_video()
    gen_youtube_free()
    print("Done!")
