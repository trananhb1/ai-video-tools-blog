#!/usr/bin/env python3
"""Generate 600x340 VS thumbnail for HeyGen vs Vidnoz comparison."""

import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

W, H = 600, 340
OUT = "/home/tom/ai-video-tools-blog/assets/images/heygen-vs-vidnoz-2026-thumbnail.png"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

LOGO_SOURCES = {
    "heygen": [
        "https://icon.horse/icon/heygen.com?size=large",
        "https://favicone.com/heygen.com?s=128",
        "https://www.google.com/s2/favicons?domain=heygen.com&sz=128",
    ],
    "vidnoz": [
        "https://icon.horse/icon/vidnoz.com?size=large",
        "https://favicone.com/vidnoz.com?s=128",
        "https://www.google.com/s2/favicons?domain=vidnoz.com&sz=128",
    ],
}


def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def fetch_logo(sources, target_size=80):
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
                    break
        except Exception:
            continue
    return best_logo


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


def main():
    # Gradient: deep navy to HeyGen blue
    img = make_gradient(W, H, "#1a1a2e", "#0d47a1")
    draw = ImageDraw.Draw(img)

    # Decorative circles
    draw.ellipse([W-90, -30, W+30, 90], outline=(100, 181, 246), width=2)
    draw.ellipse([-30, H-90, 90, H+30], outline=(100, 181, 246), width=2)

    # Fetch logos
    heygen_logo = fetch_logo(LOGO_SOURCES["heygen"])
    vidnoz_logo = fetch_logo(LOGO_SOURCES["vidnoz"])

    logo_size = 70
    circle_size = logo_size + 20

    # Place logos in circles with VS between
    total = circle_size * 2 + 60
    start_x = (W - total) // 2

    for idx, logo in enumerate([heygen_logo, vidnoz_logo]):
        if logo:
            logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
            cb = Image.new('RGBA', (circle_size, circle_size), (0, 0, 0, 0))
            cd = ImageDraw.Draw(cb)
            cd.ellipse([0, 0, circle_size - 1, circle_size - 1], fill=(255, 255, 255, 255))
            cb.paste(logo, (10, 10), logo)
            x = start_x + idx * (circle_size + 60)
            img.paste(cb, (x, 25), cb)

    # VS text between logos
    vs_font = ImageFont.truetype(FONT_BOLD, 24)
    draw.text((W // 2, 25 + circle_size // 2), "VS", fill=(255, 200, 50), font=vs_font, anchor="mm")

    # Title
    title_font = ImageFont.truetype(FONT_BOLD, 24)
    title = "HeyGen vs Vidnoz 2026"
    draw.text((W // 2, 140), title, fill=(255, 255, 255), font=title_font, anchor="mt")

    # Subtitle
    sub_font = ImageFont.truetype(FONT_REG, 16)
    draw.text((W // 2, 175), "Premium vs Budget AI Video", fill=(200, 200, 220), font=sub_font, anchor="mt")

    # Subtitle 2
    sub2_font = ImageFont.truetype(FONT_REG, 13)
    draw.text((W // 2, 205), "Which One Wins?", fill=(180, 180, 200), font=sub2_font, anchor="mt")

    # Feature pills
    pill_font = ImageFont.truetype(FONT_BOLD, 11)
    pills = [
        ("HeyGen: $24/mo Premium Avatars", hex_to_rgb("#155DFC")),
        ("Vidnoz: $14.99/mo Budget Pick", hex_to_rgb("#e65100")),
    ]
    pill_y = 240
    for text, color in pills:
        bbox = draw.textbbox((0, 0), text, font=pill_font)
        pw = bbox[2] - bbox[0] + 24
        ph = bbox[3] - bbox[1] + 12
        px = (W - pw) // 2
        draw.rounded_rectangle([px, pill_y, px + pw, pill_y + ph], radius=6, fill=(*color, 200))
        draw.text((W // 2, pill_y + ph // 2), text, fill=(255, 255, 255), font=pill_font, anchor="mm")
        pill_y += ph + 8

    # Brand
    brand_font = ImageFont.truetype(FONT_REG, 11)
    draw.text((W // 2, H - 15), "AI Video Picks", fill=(150, 150, 170), font=brand_font, anchor="mb")

    img.save(OUT)
    print(f"Saved: {OUT}")


if __name__ == "__main__":
    main()
