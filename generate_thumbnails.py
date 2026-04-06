#!/usr/bin/env python3
"""Generate professional 600x340 thumbnails with service logos for AI Video Picks blog."""

import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os

OUT_DIR = "assets/images"
W, H = 600, 340
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

PALETTES = {
    "heygen":     ("#1a1a2e", "#0d47a1", "#4fc3f7"),
    "synthesia":  ("#1a1a2e", "#1565c0", "#42a5f5"),
    "zebracat":   ("#0d3b2e", "#1b5e20", "#66bb6a"),
    "pictory":    ("#1a1a2e", "#4a148c", "#ce93d8"),
    "descript":   ("#1a1a2e", "#263238", "#80cbc4"),
    "invideo":    ("#1a1a2e", "#e65100", "#ffb74d"),
    "colossyan":  ("#1a1a2e", "#1565c0", "#90caf9"),
    "runway":     ("#1a1a2e", "#212121", "#e0e0e0"),
    "fliki":      ("#3e2723", "#5d4037", "#ffab91"),
    "opus-clip":  ("#1a1a2e", "#6a1b9a", "#ea80fc"),
    "murf-ai":    ("#1a1a2e", "#0277bd", "#4fc3f7"),
    "leonardo":   ("#1a1a2e", "#1b5e20", "#a5d6a7"),
    "deepbrain":  ("#0d47a1", "#1565c0", "#64b5f6"),
    "vidnoz":     ("#1a1a2e", "#00695c", "#4db6ac"),
    "submagic":   ("#1a1a2e", "#ad1457", "#f48fb1"),
    "kapwing":    ("#1a1a2e", "#1565c0", "#64b5f6"),
}

LOGO_DOMAINS = {
    "heygen": "heygen.com",
    "synthesia": "synthesia.io",
    "zebracat": "zebracat.ai",
    "pictory": "pictory.ai",
    "descript": "descript.com",
    "invideo": "invideo.io",
    "colossyan": "colossyan.com",
    "runway": "runwayml.com",
    "fliki": "fliki.ai",
    "opus-clip": "opus.pro",
    "murf-ai": "murf.ai",
    "leonardo": "leonardo.ai",
    "deepbrain": "deepbrain.io",
    "vidnoz": "vidnoz.com",
    "submagic": "submagic.co",
    "kapwing": "kapwing.com",
}

REVIEWS = [
    ("heygen", "HeyGen", "9.2 / 10", "AI Avatar Video Platform"),
    ("synthesia", "Synthesia", "8.0 / 10", "AI Avatar Platform Review"),
    ("zebracat", "Zebracat", "4.2 / 5.0", "AI Video Generation Platform"),
    ("pictory", "Pictory", "4.6 / 5", "Content Repurposing Tool"),
    ("descript", "Descript", "4.5 / 5", "AI Video Editor"),
    ("invideo", "InVideo", "4.4 / 5", "AI Video Maker"),
    ("colossyan", "Colossyan", "4.3 / 5", "Multilingual AI Video"),
    ("runway", "Runway", "4.2 / 5", "AI Video Generation"),
    ("fliki", "Fliki", "7.8 / 10", "AI Text-to-Video Platform"),
    ("opus-clip", "Opus Clip", "4.1 / 5", "AI Video Repurposing"),
    ("murf-ai", "Murf AI", "4.1 / 5", "AI Voiceover Platform"),
    ("deepbrain", "DeepBrain AI", "8.5 / 10", "AI Avatar Video Platform"),
    ("vidnoz", "Vidnoz", "7.5 / 10", "Free AI Avatar Platform"),
    ("submagic", "Submagic", "8.0 / 10", "AI Caption Generator"),
]

# Cache for fetched logos
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
    """Fetch highest quality logo available, with caching."""
    if domain in _logo_cache:
        logo = _logo_cache[domain]
        if logo:
            return logo.copy()
        return None

    # Try sources in order of quality
    sources = [
        f"https://icon.horse/icon/{domain}?size=large",
        f"https://favicone.com/{domain}?s=128",
        f"https://www.google.com/s2/favicons?domain={domain}&sz=128",
    ]

    best_logo = None
    best_size = 0

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
                    break  # Good enough
        except Exception as e:
            continue

    _logo_cache[domain] = best_logo
    if best_logo:
        return best_logo.copy()
    return None


def generate_review_thumbnail(key, name, rating, subtitle):
    palette = PALETTES.get(key, PALETTES["heygen"])
    bg_top, bg_bottom, accent = palette
    img = make_gradient(W, H, bg_top, bg_bottom)
    draw = ImageDraw.Draw(img)
    accent_rgb = hex_to_rgb(accent)

    # Decorative circles
    draw.ellipse([W-90, -30, W+30, 90], outline=accent_rgb, width=2)
    draw.ellipse([-30, H-90, 90, H+30], outline=accent_rgb, width=2)
    draw.ellipse([W-50, H-50, W-20, H-20], outline=accent_rgb, width=2)

    # Fetch and place logo
    domain = LOGO_DOMAINS.get(key)
    logo = fetch_logo(domain) if domain else None

    if logo:
        logo_display = 80
        logo = logo.resize((logo_display, logo_display), Image.LANCZOS)
        circle_size = logo_display + 20
        circle_bg = Image.new('RGBA', (circle_size, circle_size), (0, 0, 0, 0))
        circle_draw = ImageDraw.Draw(circle_bg)
        circle_draw.ellipse([0, 0, circle_size - 1, circle_size - 1], fill=(255, 255, 255, 255))
        circle_bg.paste(logo, (10, 10), logo)
        logo_x = (W - circle_size) // 2
        logo_y = 25
        img.paste(circle_bg, (logo_x, logo_y), circle_bg)
        text_start_y = logo_y + circle_size + 10
    else:
        text_start_y = 50

    # Badge
    badge_font = ImageFont.truetype(FONT_BOLD, 11)
    badge_text = "IN-DEPTH REVIEW"
    bbox = draw.textbbox((0, 0), badge_text, font=badge_font)
    bw = bbox[2] - bbox[0] + 24
    bh = bbox[3] - bbox[1] + 12
    bx = (W - bw) // 2
    by = text_start_y
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=4, fill=accent_rgb)
    draw.text((W // 2, by + bh // 2), badge_text, fill=(255, 255, 255), font=badge_font, anchor="mm")

    # Tool name
    name_font = ImageFont.truetype(FONT_BOLD, 34)
    name_y = by + bh + 12
    draw.text((W // 2, name_y), name.upper(), fill=(255, 255, 255), font=name_font, anchor="mt")

    # Stars
    star_font = ImageFont.truetype(FONT_REG, 20)
    star_y = name_y + 42
    draw.text((W // 2, star_y), "\u2605\u2605\u2605\u2605\u2605", fill=hex_to_rgb("#f59e0b"), font=star_font, anchor="mt")

    # Rating
    rating_font = ImageFont.truetype(FONT_BOLD, 17)
    rating_y = star_y + 26
    draw.text((W // 2, rating_y), rating, fill=hex_to_rgb("#f59e0b"), font=rating_font, anchor="mt")

    # Subtitle
    sub_font = ImageFont.truetype(FONT_REG, 13)
    sub_y = rating_y + 24
    draw.text((W // 2, sub_y), subtitle, fill=(200, 200, 220), font=sub_font, anchor="mt")

    return img


def generate_comparison_thumbnail(keys, title):
    img = make_gradient(W, H, "#1a1a2e", "#0d47a1")
    draw = ImageDraw.Draw(img)
    draw.ellipse([W-90, -30, W+30, 90], outline=(100, 181, 246), width=2)
    draw.ellipse([-30, H-90, 90, H+30], outline=(100, 181, 246), width=2)

    logos = []
    for key in keys:
        domain = LOGO_DOMAINS.get(key)
        logo = fetch_logo(domain) if domain else None
        logos.append(logo)

    logo_size = 70
    circle_size = logo_size + 20
    valid_logos = [l for l in logos if l is not None]
    n = len(valid_logos)

    if n >= 2:
        if n == 2:
            total = circle_size * 2 + 60
            start_x = (W - total) // 2
            for idx, logo in enumerate(valid_logos):
                logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
                cb = Image.new('RGBA', (circle_size, circle_size), (0, 0, 0, 0))
                cd = ImageDraw.Draw(cb)
                cd.ellipse([0, 0, circle_size - 1, circle_size - 1], fill=(255, 255, 255, 255))
                cb.paste(logo, (10, 10), logo)
                x = start_x + idx * (circle_size + 60)
                img.paste(cb, (x, 25), cb)
            vs_font = ImageFont.truetype(FONT_BOLD, 24)
            draw.text((W // 2, 25 + circle_size // 2), "VS", fill=(255, 200, 50), font=vs_font, anchor="mm")
        else:
            total = circle_size * min(n, 3) + 25 * (min(n, 3) - 1)
            start_x = (W - total) // 2
            for idx in range(min(3, n)):
                logo = valid_logos[idx].resize((logo_size, logo_size), Image.LANCZOS)
                cb = Image.new('RGBA', (circle_size, circle_size), (0, 0, 0, 0))
                cd = ImageDraw.Draw(cb)
                cd.ellipse([0, 0, circle_size - 1, circle_size - 1], fill=(255, 255, 255, 255))
                cb.paste(logo, (10, 10), logo)
                x = start_x + idx * (circle_size + 25)
                img.paste(cb, (x, 20), cb)
        text_y = 130
    else:
        text_y = 60

    title_font = ImageFont.truetype(FONT_BOLD, 24)
    words = title.split()
    lines, current = [], ""
    for w in words:
        test = f"{current} {w}".strip()
        bbox = draw.textbbox((0, 0), test, font=title_font)
        if bbox[2] - bbox[0] > W - 60:
            lines.append(current)
            current = w
        else:
            current = test
    if current:
        lines.append(current)

    for i, line in enumerate(lines):
        draw.text((W // 2, text_y + i * 35), line, fill=(255, 255, 255), font=title_font, anchor="mt")

    sub_y = text_y + len(lines) * 35 + 10
    sub_font = ImageFont.truetype(FONT_REG, 13)
    draw.text((W // 2, sub_y), "Head-to-Head Comparison 2026", fill=(180, 180, 200), font=sub_font, anchor="mt")

    brand_font = ImageFont.truetype(FONT_REG, 11)
    draw.text((W // 2, H - 15), "AI Video Picks", fill=(150, 150, 170), font=brand_font, anchor="mb")
    return img


def generate_top10_thumbnail():
    img = make_gradient(W, H, "#1a1a2e", "#0d47a1")
    draw = ImageDraw.Draw(img)
    draw.ellipse([W-80, -30, W+30, 80], outline=(100, 181, 246), width=2)
    draw.ellipse([-30, H-80, 80, H+30], outline=(100, 181, 246), width=2)

    top_keys = ["heygen", "synthesia", "zebracat", "pictory", "descript"]
    logo_size = 45
    circle_size = logo_size + 14
    total = circle_size * len(top_keys) + 12 * (len(top_keys) - 1)
    start_x = (W - total) // 2

    for i, key in enumerate(top_keys):
        logo = fetch_logo(LOGO_DOMAINS[key])
        if logo:
            logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
            cb = Image.new('RGBA', (circle_size, circle_size), (0, 0, 0, 0))
            cd = ImageDraw.Draw(cb)
            cd.ellipse([0, 0, circle_size - 1, circle_size - 1], fill=(255, 255, 255, 255))
            cb.paste(logo, (7, 7), logo)
            x = start_x + i * (circle_size + 12)
            img.paste(cb, (x, 18), cb)

    badge_font = ImageFont.truetype(FONT_BOLD, 12)
    badge_text = "2026 RANKING"
    bbox = draw.textbbox((0, 0), badge_text, font=badge_font)
    bw = bbox[2] - bbox[0] + 24
    bh = bbox[3] - bbox[1] + 12
    bx = (W - bw) // 2
    by = 88
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=4, fill=hex_to_rgb("#f59e0b"))
    draw.text((W // 2, by + bh // 2), badge_text, fill=(255, 255, 255), font=badge_font, anchor="mm")

    big_font = ImageFont.truetype(FONT_BOLD, 58)
    draw.text((W // 2, 150), "TOP 10", fill=(255, 255, 255), font=big_font, anchor="mt")

    sub_font = ImageFont.truetype(FONT_BOLD, 21)
    draw.text((W // 2, 220), "Best AI Video Tools", fill=(255, 255, 255), font=sub_font, anchor="mt")

    draw.line([(W // 2 - 40, 253), (W // 2 + 40, 253)], fill=hex_to_rgb("#f59e0b"), width=3)

    bottom_font = ImageFont.truetype(FONT_REG, 13)
    draw.text((W // 2, 268), "Complete Guide & Reviews", fill=(180, 180, 200), font=bottom_font, anchor="mt")

    brand_font = ImageFont.truetype(FONT_REG, 11)
    draw.text((W // 2, H - 12), "AI Video Picks", fill=(150, 150, 170), font=brand_font, anchor="mb")
    return img


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)

    print("=== Review Thumbnails ===")
    for key, name, rating, subtitle in REVIEWS:
        print(f"  {name}...", end=" ", flush=True)
        img = generate_review_thumbnail(key, name, rating, subtitle)
        fn = f"deepbrain-ai-review-thumbnail.png" if key == "deepbrain" else f"{key}-review-thumbnail.png"
        img.save(os.path.join(OUT_DIR, fn), "PNG", optimize=True)
        print(f"-> {fn}")

    print("\n=== Comparison Thumbnails ===")
    comparisons = [
        (["heygen", "synthesia"], "HeyGen vs Synthesia 2026", "heygen-vs-synthesia-thumbnail.png"),
        (["heygen", "synthesia", "pictory"], "HeyGen vs Synthesia vs Pictory", "comparison-thumbnail.png"),
        (["runway"], "Kling vs Veo vs Runway 2026", "kling-veo-runway-thumbnail.png"),
        (["descript", "kapwing"], "VEED vs Kapwing vs Descript", "veed-kapwing-descript-thumbnail.png"),
    ]
    for keys, title, fn in comparisons:
        print(f"  {title}...", end=" ", flush=True)
        img = generate_comparison_thumbnail(keys, title)
        img.save(os.path.join(OUT_DIR, fn), "PNG", optimize=True)
        print(f"-> {fn}")

    print("\n=== Top 10 Thumbnail ===")
    img = generate_top10_thumbnail()
    img.save(os.path.join(OUT_DIR, "top10-thumbnail.png"), "PNG", optimize=True)
    print("-> top10-thumbnail.png")

    print("\nDone!")
