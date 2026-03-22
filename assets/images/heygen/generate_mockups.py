#!/usr/bin/env python3
"""Generate 9 HeyGen UI mockup illustrations for the blog post."""

from PIL import Image, ImageDraw, ImageFont
import os

# Constants
W, H = 760, 420
OUT_DIR = "/home/tom/ai-video-tools-blog/assets/images/heygen"

# Colors
DARK_HEADER = "#1a1a2e"
ACCENT = "#4F46E5"
ACCENT_LIGHT = "#6366F1"
BG_WHITE = "#FFFFFF"
BG_LIGHT = "#f5f5f5"
BG_PANEL = "#eaeaea"
TEXT_DARK = "#1a1a2e"
TEXT_MED = "#555555"
TEXT_LIGHT = "#999999"
GREEN = "#22c55e"
GREEN_DARK = "#16a34a"
BORDER = "#d1d5db"
SELECTED_BORDER = "#4F46E5"
WHITE = "#FFFFFF"
OVERLAY_BG = "#00000066"

# Fonts
FONT_BOLD_24 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
FONT_BOLD_20 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
FONT_BOLD_18 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
FONT_BOLD_16 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
FONT_BOLD_14 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
FONT_BOLD_12 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 12)
FONT_REG_16 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
FONT_REG_14 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
FONT_REG_13 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
FONT_REG_12 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
FONT_REG_11 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
FONT_BOLD_32 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
FONT_BOLD_28 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)


def new_canvas():
    img = Image.new("RGB", (W, H), BG_WHITE)
    draw = ImageDraw.Draw(img)
    return img, draw


def draw_header(draw, active_tab=None):
    """Draw the dark header bar with HeyGen logo."""
    draw.rectangle([0, 0, W, 48], fill=DARK_HEADER)
    # Logo
    draw.text((20, 12), "HeyGen", fill=WHITE, font=FONT_BOLD_20)
    # Accent dot
    draw.ellipse([95, 16, 105, 26], fill=ACCENT)
    if active_tab:
        tabs = active_tab if isinstance(active_tab, list) else [active_tab]
        x = 140
        for tab in tabs:
            bbox = draw.textbbox((0, 0), tab, font=FONT_REG_13)
            tw = bbox[2] - bbox[0]
            draw.text((x, 16), tab, fill="#aaaaaa", font=FONT_REG_13)
            x += tw + 28


def draw_rounded_rect(draw, xy, radius, fill=None, outline=None, width=1):
    """Draw a rounded rectangle."""
    x0, y0, x1, y1 = xy
    r = radius
    # Use pieslice for corners + rectangles for body
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)


def draw_button(draw, xy, text, fill=ACCENT, text_color=WHITE, font=FONT_BOLD_14):
    """Draw a button with rounded corners."""
    draw_rounded_rect(draw, xy, radius=8, fill=fill)
    x0, y0, x1, y1 = xy
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = x0 + (x1 - x0 - tw) // 2
    ty = y0 + (y1 - y0 - th) // 2 - 1
    draw.text((tx, ty), text, fill=text_color, font=font)


def draw_play_icon(draw, cx, cy, size=16, fill=WHITE):
    """Draw a play triangle."""
    s = size
    points = [(cx - s//3, cy - s//2), (cx - s//3, cy + s//2), (cx + s//2, cy)]
    draw.polygon(points, fill=fill)


def draw_sidebar(draw, items, active_idx=0, top=48, width=170):
    """Draw a left sidebar with menu items."""
    draw.rectangle([0, top, width, H], fill=BG_LIGHT)
    draw.line([width, top, width, H], fill=BORDER, width=1)
    y = top + 16
    for i, item in enumerate(items):
        if i == active_idx:
            draw_rounded_rect(draw, [8, y - 4, width - 8, y + 26], radius=6, fill=ACCENT)
            draw.text((24, y), item, fill=WHITE, font=FONT_BOLD_14)
        else:
            draw.text((24, y), item, fill=TEXT_MED, font=FONT_REG_14)
        y += 38
    return width


def draw_avatar_circle(draw, cx, cy, r, label=None, selected=False):
    """Draw an avatar placeholder circle."""
    outline_c = SELECTED_BORDER if selected else BORDER
    outline_w = 3 if selected else 1
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BG_PANEL, outline=outline_c, width=outline_w)
    # Simple person icon
    head_r = r // 3
    draw.ellipse([cx - head_r, cy - r//2 - head_r, cx + head_r, cy - r//2 + head_r], fill=TEXT_LIGHT)
    draw.arc([cx - r//2, cy - r//6, cx + r//2, cy + r//2 + 4], start=200, end=340, fill=TEXT_LIGHT, width=2)
    if label:
        bbox = draw.textbbox((0, 0), label, font=FONT_REG_11)
        tw = bbox[2] - bbox[0]
        draw.text((cx - tw // 2, cy + r + 6), label, fill=TEXT_MED, font=FONT_REG_11)
    if selected:
        # Checkmark badge
        bx, by = cx + r - 6, cy - r + 6
        draw.ellipse([bx - 8, by - 8, bx + 8, by + 8], fill=ACCENT)
        draw.text((bx - 5, by - 7), "✓", fill=WHITE, font=FONT_BOLD_12)


# ─── Image 1: Homepage ───
def gen_homepage():
    img, draw = new_canvas()
    draw_header(draw, ["Features", "Pricing", "Enterprise"])

    # Hero section
    draw.text((130, 90), "Create AI Videos", fill=TEXT_DARK, font=FONT_BOLD_32)
    draw.text((195, 132), "in Minutes", fill=ACCENT, font=FONT_BOLD_32)

    draw.text((165, 180), "Turn text into professional videos with", fill=TEXT_MED, font=FONT_REG_14)
    draw.text((175, 200), "AI avatars, voices, and templates.", fill=TEXT_MED, font=FONT_REG_14)

    # CTA button
    draw_button(draw, [280, 240, 480, 282], "Get Started Free", fill=ACCENT, font=FONT_BOLD_18)

    # Feature icons row
    features = [
        ("100+ Avatars", "👤"),
        ("40+ Languages", "🌐"),
        ("300+ Voices", "🎙"),
        ("Templates", "📋"),
    ]
    fx = 100
    for label, icon in features:
        # Icon circle
        draw_rounded_rect(draw, [fx, 320, fx + 54, 374], radius=12, fill=BG_LIGHT, outline=BORDER)
        draw.text((fx + 14, 334), icon, fill=ACCENT, font=FONT_REG_16)
        bbox = draw.textbbox((0, 0), label, font=FONT_REG_11)
        tw = bbox[2] - bbox[0]
        draw.text((fx + 27 - tw // 2, 380), label, fill=TEXT_MED, font=FONT_REG_11)
        fx += 155

    img.save(os.path.join(OUT_DIR, "heygen-homepage.png"))
    print("  ✓ heygen-homepage.png")


# ─── Image 2: Dashboard ───
def gen_dashboard():
    img, draw = new_canvas()
    draw_header(draw)

    sidebar_items = ["My Videos", "Templates", "Avatars", "Brand Kit", "Settings"]
    sw = draw_sidebar(draw, sidebar_items, active_idx=0)

    # Main area
    mx = sw + 20
    draw_button(draw, [mx, 64, mx + 160, 100], "+ Create Video", fill=ACCENT, font=FONT_BOLD_14)
    draw.text((mx + 180, 72), "Recent Projects", fill=TEXT_MED, font=FONT_REG_14)

    # Video thumbnail grid (2 rows x 3 cols)
    gx_start = mx
    gy = 120
    for row in range(2):
        gx = gx_start
        for col in range(3):
            tw, th = 170, 100
            draw_rounded_rect(draw, [gx, gy, gx + tw, gy + th], radius=8, fill=BG_PANEL, outline=BORDER)
            # Play icon
            draw_play_icon(draw, gx + tw // 2, gy + th // 2, size=20, fill=TEXT_LIGHT)
            # Label
            draw.text((gx + 4, gy + th + 4), f"Video {row * 3 + col + 1}", fill=TEXT_MED, font=FONT_REG_11)
            draw.text((gx + 4, gy + th + 18), "2 days ago", fill=TEXT_LIGHT, font=FONT_REG_11)
            gx += tw + 14
        gy += th + 40

    img.save(os.path.join(OUT_DIR, "heygen-dashboard.png"))
    print("  ✓ heygen-dashboard.png")


# ─── Image 3: Avatar Library ───
def gen_avatar_library():
    img, draw = new_canvas()
    draw_header(draw, ["Avatars"])

    # Filter bar
    draw_rounded_rect(draw, [20, 58, W - 20, 94], radius=8, fill=BG_LIGHT, outline=BORDER)
    filters = ["All", "Female", "Male", "Professional", "Casual"]
    fx = 32
    for i, f in enumerate(filters):
        if i == 0:
            draw_rounded_rect(draw, [fx - 4, 64, fx + 36, 88], radius=6, fill=ACCENT)
            draw.text((fx, 68), f, fill=WHITE, font=FONT_BOLD_12)
        else:
            draw.text((fx, 68), f, fill=TEXT_MED, font=FONT_REG_12)
        bbox = draw.textbbox((0, 0), f, font=FONT_REG_12)
        fx += bbox[2] - bbox[0] + 30

    # Search box
    draw_rounded_rect(draw, [W - 220, 64, W - 32, 88], radius=6, fill=WHITE, outline=BORDER)
    draw.text((W - 212, 68), "🔍 Search avatars...", fill=TEXT_LIGHT, font=FONT_REG_12)

    # Avatar grid: 2 rows x 3 cols
    names = ["Sarah", "James", "Emma", "Michael", "Aria", "David"]
    selected_idx = 2  # Emma
    ax_start = 80
    ay = 130
    for row in range(2):
        ax = ax_start
        for col in range(3):
            idx = row * 3 + col
            is_sel = idx == selected_idx
            draw_avatar_circle(draw, ax, ay, 42, label=names[idx], selected=is_sel)
            if is_sel:
                bbox = draw.textbbox((0, 0), "Selected", font=FONT_BOLD_12)
                tw = bbox[2] - bbox[0]
                draw.text((ax - tw // 2, ay + 60), "Selected", fill=ACCENT, font=FONT_BOLD_12)
            ax += 125
        ay += 140

    # Right info panel
    px = 490
    draw_rounded_rect(draw, [px, 110, W - 20, H - 20], radius=10, fill=BG_LIGHT, outline=BORDER)
    draw.text((px + 14, 120), "Avatar Details", fill=TEXT_DARK, font=FONT_BOLD_16)
    draw.text((px + 14, 148), "Name: Emma", fill=TEXT_MED, font=FONT_REG_13)
    draw.text((px + 14, 170), "Style: Professional", fill=TEXT_MED, font=FONT_REG_13)
    draw.text((px + 14, 192), "Gender: Female", fill=TEXT_MED, font=FONT_REG_13)
    draw.text((px + 14, 214), "Gestures: 12 available", fill=TEXT_MED, font=FONT_REG_13)
    draw_button(draw, [px + 14, 250, px + 220, 284], "Use This Avatar", fill=ACCENT, font=FONT_BOLD_14)

    img.save(os.path.join(OUT_DIR, "heygen-avatar-library.png"))
    print("  ✓ heygen-avatar-library.png")


# ─── Image 4: Script Editor ───
def gen_script_editor():
    img, draw = new_canvas()
    draw_header(draw, ["Script Editor"])

    # Left: avatar preview
    lx, ly = 40, 80
    draw_rounded_rect(draw, [lx, ly, lx + 200, ly + 260], radius=12, fill=BG_LIGHT, outline=BORDER)
    # Avatar circle
    cx, cy = lx + 100, ly + 100
    draw.ellipse([cx - 50, cy - 50, cx + 50, cy + 50], fill=BG_PANEL, outline=BORDER, width=2)
    head_r = 16
    draw.ellipse([cx - head_r, cy - 25, cx + head_r, cy - 25 + 2 * head_r], fill=TEXT_LIGHT)
    draw.arc([cx - 30, cy + 2, cx + 30, cy + 40], start=200, end=340, fill=TEXT_LIGHT, width=3)
    draw.text((cx - 22, cy + 58), "Emma", fill=TEXT_DARK, font=FONT_BOLD_14)
    draw.text((cx - 36, cy + 76), "Professional", fill=TEXT_MED, font=FONT_REG_12)

    # Voice info
    draw.text((lx + 14, ly + 200), "Voice: Sarah", fill=TEXT_MED, font=FONT_REG_12)
    draw.text((lx + 14, ly + 218), "Language: English (US)", fill=TEXT_MED, font=FONT_REG_12)
    draw.text((lx + 14, ly + 236), "Speed: 1.0x", fill=TEXT_MED, font=FONT_REG_12)

    # Right: script input area
    rx = 260
    draw.text((rx, 68), "Enter Your Script", fill=TEXT_DARK, font=FONT_BOLD_16)
    draw_rounded_rect(draw, [rx, 92, W - 30, 330], radius=10, fill=WHITE, outline=BORDER, width=2)

    script_lines = [
        "Welcome to our product demo. Today I'll",
        "walk you through the key features of our",
        "new platform. We've designed it with",
        "simplicity in mind, so you can get started",
        "in just a few minutes.",
        "",
        "Let me show you how easy it is to create",
        "professional AI videos with HeyGen...",
    ]
    ty = 104
    for line in script_lines:
        draw.text((rx + 14, ty), line, fill=TEXT_DARK, font=FONT_REG_13)
        ty += 22

    # Text cursor blink simulation
    draw.line([rx + 14 + 310, ty - 22, rx + 14 + 310, ty - 6], fill=ACCENT, width=2)

    # Bottom stats bar
    draw_rounded_rect(draw, [rx, 345, W - 30, 378], radius=8, fill=BG_LIGHT, outline=BORDER)
    draw.text((rx + 14, 352), "Word Count: 145", fill=TEXT_MED, font=FONT_REG_13)
    draw.text((rx + 180, 352), "|", fill=BORDER, font=FONT_REG_13)
    draw.text((rx + 200, 352), "Est. Duration: 1:12", fill=TEXT_MED, font=FONT_REG_13)
    draw.text((rx + 380, 352), "|", fill=BORDER, font=FONT_REG_13)
    draw.text((rx + 400, 352), "Characters: 892", fill=TEXT_MED, font=FONT_REG_13)

    # Bottom action buttons
    draw_button(draw, [W - 200, 390, W - 30, 415], "Continue →", fill=ACCENT, font=FONT_BOLD_14)

    img.save(os.path.join(OUT_DIR, "heygen-script-editor.png"))
    print("  ✓ heygen-script-editor.png")


# ─── Image 5: Scene Editor ───
def gen_scene_editor():
    img, draw = new_canvas()
    draw_header(draw, ["Scene Editor"])

    # Center video preview
    px, py = 30, 60
    pw, ph = 460, 280
    draw_rounded_rect(draw, [px, py, px + pw, py + ph], radius=10, fill="#2d2d44", outline=BORDER)

    # Background gradient simulation
    for i in range(ph):
        r = int(45 + (i / ph) * 30)
        g = int(45 + (i / ph) * 20)
        b = int(68 + (i / ph) * 30)
        draw.line([px + 1, py + i, px + pw - 1, py + i], fill=(r, g, b))
    draw_rounded_rect(draw, [px, py, px + pw, py + ph], radius=10, outline=BORDER)

    # Avatar in center of preview
    acx, acy = px + pw // 2, py + ph // 2 + 20
    draw.ellipse([acx - 40, acy - 60, acx + 40, acy + 20], fill="#555577")
    draw.ellipse([acx - 16, acy - 52, acx + 16, acy - 20], fill="#8888aa")
    draw.rectangle([acx - 30, acy - 10, acx + 30, acy + 50], fill="#555577")

    # "Preview" label
    draw.text((px + 10, py + 8), "Scene Preview", fill="#aaaacc", font=FONT_REG_12)

    # Text overlay on preview
    draw_rounded_rect(draw, [px + 80, py + ph - 50, px + pw - 80, py + ph - 20], radius=6, fill="#00000088")
    draw.text((px + 120, py + ph - 46), "Welcome to our demo", fill=WHITE, font=FONT_BOLD_14)

    # Right panel
    rpx = px + pw + 16
    rpw = W - rpx - 16
    draw_rounded_rect(draw, [rpx, 60, W - 16, H - 16], radius=10, fill=BG_LIGHT, outline=BORDER)

    draw.text((rpx + 12, 70), "Customize Scene", fill=TEXT_DARK, font=FONT_BOLD_16)

    # Background section
    draw.text((rpx + 12, 100), "Background", fill=TEXT_DARK, font=FONT_BOLD_14)
    colors = ["#1a1a2e", "#0f3460", "#533483", "#e94560", "#f5f5f5", "#22c55e"]
    cx = rpx + 12
    for c in colors:
        draw_rounded_rect(draw, [cx, 122, cx + 28, 150], radius=4, fill=c, outline=BORDER)
        cx += 34
    draw_rounded_rect(draw, [rpx + 12, 158, rpx + rpw - 24, 180], radius=6, fill=WHITE, outline=BORDER)
    draw.text((rpx + 22, 162), "📁 Upload Image", fill=TEXT_MED, font=FONT_REG_12)

    # Text overlay section
    draw.text((rpx + 12, 196), "Text Overlay", fill=TEXT_DARK, font=FONT_BOLD_14)
    draw_rounded_rect(draw, [rpx + 12, 218, rpx + rpw - 24, 244], radius=6, fill=WHITE, outline=BORDER)
    draw.text((rpx + 22, 223), "Welcome to our demo", fill=TEXT_MED, font=FONT_REG_12)

    # Font size / color
    draw.text((rpx + 12, 252), "Size:", fill=TEXT_MED, font=FONT_REG_12)
    draw_rounded_rect(draw, [rpx + 50, 249, rpx + 100, 269], radius=4, fill=WHITE, outline=BORDER)
    draw.text((rpx + 62, 252), "24px", fill=TEXT_DARK, font=FONT_REG_12)

    # Logo upload section
    draw.text((rpx + 12, 286), "Logo", fill=TEXT_DARK, font=FONT_BOLD_14)
    draw_rounded_rect(draw, [rpx + 12, 308, rpx + rpw - 24, 350], radius=6, fill=WHITE, outline=BORDER)
    draw.text((rpx + 50, 320), "+ Upload Logo", fill=TEXT_LIGHT, font=FONT_REG_12)

    # Apply button
    draw_button(draw, [rpx + 12, 362, rpx + rpw - 24, 392], "Apply Changes", fill=ACCENT, font=FONT_BOLD_14)

    img.save(os.path.join(OUT_DIR, "heygen-scene-editor.png"))
    print("  ✓ heygen-scene-editor.png")


# ─── Image 6: Timeline ───
def gen_timeline():
    img, draw = new_canvas()
    draw_header(draw, ["Timeline"])

    # Video preview area
    pvx, pvy = 120, 58
    pvw, pvh = W - 240, 200
    draw_rounded_rect(draw, [pvx, pvy, pvx + pvw, pvy + pvh], radius=10, fill="#2d2d44")
    draw_play_icon(draw, pvx + pvw // 2, pvy + pvh // 2, size=30, fill="#ffffffaa")
    draw.text((pvx + 10, pvy + 8), "00:00 / 02:48", fill="#aaaacc", font=FONT_REG_12)

    # Progress bar
    bar_y = pvy + pvh - 20
    draw.line([pvx + 10, bar_y, pvx + pvw - 10, bar_y], fill="#555577", width=3)
    draw.line([pvx + 10, bar_y, pvx + 180, bar_y], fill=ACCENT, width=3)
    draw.ellipse([pvx + 176, bar_y - 5, pvx + 186, bar_y + 5], fill=ACCENT)

    # Timeline area
    ty = 275
    draw_rounded_rect(draw, [16, ty - 10, W - 16, H - 10], radius=10, fill=BG_LIGHT, outline=BORDER)
    draw.text((28, ty), "Scenes Timeline", fill=TEXT_DARK, font=FONT_BOLD_14)

    # Scene blocks
    scenes = [
        ("Scene 1", "0:00 - 0:42", "#4F46E5"),
        ("Scene 2", "0:42 - 1:15", "#6366F1"),
        ("Scene 3", "1:15 - 2:10", "#818CF8"),
        ("Scene 4", "2:10 - 2:48", "#A5B4FC"),
    ]
    sx = 28
    sy = ty + 30
    total_w = W - 100
    widths = [140, 155, 175, 140]
    for i, (name, dur, color) in enumerate(scenes):
        sw = widths[i]
        draw_rounded_rect(draw, [sx, sy, sx + sw, sy + 65], radius=8, fill=color)
        draw.text((sx + 10, sy + 8), name, fill=WHITE, font=FONT_BOLD_14)
        draw.text((sx + 10, sy + 30), dur, fill="#ffffffcc", font=FONT_REG_11)
        # Drag handle dots
        draw.text((sx + sw - 18, sy + 24), "⋮", fill="#ffffffaa", font=FONT_BOLD_16)
        sx += sw + 8

    # Add scene button
    draw_rounded_rect(draw, [sx, sy, sx + 50, sy + 65], radius=8, fill=WHITE, outline=BORDER, width=2)
    draw.text((sx + 16, sy + 18), "+", fill=ACCENT, font=FONT_BOLD_24)

    # Playback controls
    ctrl_y = ty + 105
    draw.text((300, ctrl_y), "⏮", fill=TEXT_MED, font=FONT_BOLD_18)
    draw.text((340, ctrl_y), "▶", fill=ACCENT, font=FONT_BOLD_18)
    draw.text((380, ctrl_y), "⏭", fill=TEXT_MED, font=FONT_BOLD_18)
    draw.text((430, ctrl_y), "🔊", fill=TEXT_MED, font=FONT_BOLD_18)

    img.save(os.path.join(OUT_DIR, "heygen-timeline.png"))
    print("  ✓ heygen-timeline.png")


# ─── Image 7: Voice Selection ───
def gen_voice_selection():
    img, draw = new_canvas()
    draw_header(draw, ["Voice Settings"])

    # Language dropdown
    draw.text((30, 64), "Language", fill=TEXT_DARK, font=FONT_BOLD_16)
    draw_rounded_rect(draw, [30, 88, 260, 118], radius=8, fill=WHITE, outline=BORDER, width=2)
    draw.text((44, 94), "English (US)", fill=TEXT_DARK, font=FONT_REG_14)
    draw.text((228, 94), "▼", fill=TEXT_MED, font=FONT_REG_14)

    # Voice list
    draw.text((30, 138), "Select Voice", fill=TEXT_DARK, font=FONT_BOLD_16)
    voices = [
        ("Sarah", "Professional", True),
        ("James", "Casual", False),
        ("Emily", "Warm", False),
        ("Michael", "Authoritative", False),
        ("Aria", "Friendly", False),
    ]

    vy = 164
    for name, style, selected in voices:
        bg = "#E8E7FD" if selected else WHITE
        outline = ACCENT if selected else BORDER
        w_out = 2 if selected else 1
        draw_rounded_rect(draw, [30, vy, 360, vy + 40], radius=8, fill=bg, outline=outline, width=w_out)

        # Play button circle
        draw.ellipse([42, vy + 8, 66, vy + 32], fill=ACCENT if selected else BG_PANEL)
        draw_play_icon(draw, 54, vy + 20, size=10, fill=WHITE if selected else TEXT_MED)

        draw.text((76, vy + 5), name, fill=TEXT_DARK, font=FONT_BOLD_14)
        draw.text((76, vy + 22), style, fill=TEXT_MED, font=FONT_REG_11)

        # Duration
        draw.text((300, vy + 12), "Preview", fill=ACCENT if selected else TEXT_LIGHT, font=FONT_REG_11)

        if selected:
            draw.text((340, vy + 12), "✓", fill=ACCENT, font=FONT_BOLD_14)

        vy += 48

    # Right panel - Speed + pitch controls
    rpx = 400
    draw_rounded_rect(draw, [rpx, 64, W - 20, H - 20], radius=10, fill=BG_LIGHT, outline=BORDER)

    draw.text((rpx + 16, 78), "Voice Settings", fill=TEXT_DARK, font=FONT_BOLD_16)

    # Speed slider
    draw.text((rpx + 16, 116), "Speed", fill=TEXT_MED, font=FONT_BOLD_14)
    slider_y = 145
    draw.line([rpx + 16, slider_y, rpx + 310, slider_y], fill=BORDER, width=4)
    draw.line([rpx + 16, slider_y, rpx + 163, slider_y], fill=ACCENT, width=4)
    draw.ellipse([rpx + 155, slider_y - 8, rpx + 171, slider_y + 8], fill=ACCENT)
    draw.text((rpx + 16, slider_y + 14), "0.5x", fill=TEXT_LIGHT, font=FONT_REG_11)
    draw.text((rpx + 148, slider_y + 14), "1.0x", fill=ACCENT, font=FONT_BOLD_12)
    draw.text((rpx + 290, slider_y + 14), "2.0x", fill=TEXT_LIGHT, font=FONT_REG_11)

    # Pitch slider
    draw.text((rpx + 16, 196), "Pitch", fill=TEXT_MED, font=FONT_BOLD_14)
    slider_y2 = 225
    draw.line([rpx + 16, slider_y2, rpx + 310, slider_y2], fill=BORDER, width=4)
    draw.line([rpx + 16, slider_y2, rpx + 163, slider_y2], fill=ACCENT, width=4)
    draw.ellipse([rpx + 155, slider_y2 - 8, rpx + 171, slider_y2 + 8], fill=ACCENT)
    draw.text((rpx + 16, slider_y2 + 14), "Low", fill=TEXT_LIGHT, font=FONT_REG_11)
    draw.text((rpx + 145, slider_y2 + 14), "Default", fill=ACCENT, font=FONT_BOLD_12)
    draw.text((rpx + 290, slider_y2 + 14), "High", fill=TEXT_LIGHT, font=FONT_REG_11)

    # Pause control
    draw.text((rpx + 16, 272), "Pause After Sentences", fill=TEXT_MED, font=FONT_BOLD_14)
    draw_rounded_rect(draw, [rpx + 16, 296, rpx + 100, 320], radius=6, fill=WHITE, outline=BORDER)
    draw.text((rpx + 30, 300), "0.5s", fill=TEXT_DARK, font=FONT_REG_13)
    draw.text((rpx + 86, 300), "▼", fill=TEXT_MED, font=FONT_REG_12)

    # Preview audio button
    draw_button(draw, [rpx + 16, 345, rpx + 200, 378], "🔊 Preview Voice", fill=ACCENT, font=FONT_BOLD_14)

    img.save(os.path.join(OUT_DIR, "heygen-voice-selection.png"))
    print("  ✓ heygen-voice-selection.png")


# ─── Image 8: Preview Screen ───
def gen_preview():
    img, draw = new_canvas()
    draw_header(draw, ["Preview & Generate"])

    # Large video preview
    pvx, pvy = 40, 62
    pvw, pvh = W - 80, 260
    draw_rounded_rect(draw, [pvx, pvy, pvx + pvw, pvy + pvh], radius=12, fill="#1a1a2e")

    # Gradient background
    for i in range(pvh):
        intensity = int(26 + (i / pvh) * 20)
        draw.line([pvx + 1, pvy + i, pvx + pvw - 1, pvy + i], fill=(intensity, intensity, intensity + 20))
    draw_rounded_rect(draw, [pvx, pvy, pvx + pvw, pvy + pvh], radius=12, outline="#333355", width=2)

    # Play button overlay (circle + triangle)
    pcx, pcy = pvx + pvw // 2, pvy + pvh // 2
    draw.ellipse([pcx - 30, pcy - 30, pcx + 30, pcy + 30], fill="#00000088", outline="#ffffffaa", width=2)
    draw_play_icon(draw, pcx + 3, pcy, size=24, fill="#ffffffdd")

    # Time display
    draw.text((pvx + 14, pvy + pvh - 28), "00:00 / 01:12", fill="#aaaacc", font=FONT_REG_12)

    # Progress bar
    bar_y2 = pvy + pvh - 10
    draw.line([pvx + 14, bar_y2, pvx + pvw - 14, bar_y2], fill="#555577", width=3)

    # Controls below preview
    cy2 = pvy + pvh + 16

    # Quality dropdown
    draw.text((pvx, cy2 + 4), "Quality:", fill=TEXT_MED, font=FONT_BOLD_14)
    draw_rounded_rect(draw, [pvx + 80, cy2, pvx + 200, cy2 + 32], radius=6, fill=WHITE, outline=BORDER)
    draw.text((pvx + 94, cy2 + 7), "1080p (HD)", fill=TEXT_DARK, font=FONT_REG_13)
    draw.text((pvx + 180, cy2 + 7), "▼", fill=TEXT_MED, font=FONT_REG_12)

    # Captions toggle
    draw.text((pvx + 230, cy2 + 4), "Captions:", fill=TEXT_MED, font=FONT_BOLD_14)
    # Toggle switch
    draw_rounded_rect(draw, [pvx + 320, cy2 + 4, pvx + 360, cy2 + 26], radius=11, fill=ACCENT)
    draw.ellipse([pvx + 340, cy2 + 6, pvx + 358, cy2 + 24], fill=WHITE)

    # Generate button (large, prominent)
    draw_button(draw, [W - 260, cy2 - 4, W - 40, cy2 + 38], "Generate Video", fill=ACCENT, font=FONT_BOLD_18)

    # Estimated time
    draw.text((W - 240, cy2 + 42), "Est. processing: ~3 minutes", fill=TEXT_LIGHT, font=FONT_REG_11)

    img.save(os.path.join(OUT_DIR, "heygen-preview.png"))
    print("  ✓ heygen-preview.png")


# ─── Image 9: Download Page ───
def gen_download():
    img, draw = new_canvas()
    draw_header(draw, ["My Videos"])

    # Success area (centered card)
    cx = W // 2
    card_w, card_h = 500, 300
    card_x = cx - card_w // 2
    card_y = 70
    draw_rounded_rect(draw, [card_x, card_y, card_x + card_w, card_y + card_h], radius=16, fill=BG_LIGHT, outline=BORDER)

    # Checkmark circle
    check_y = card_y + 40
    draw.ellipse([cx - 28, check_y - 28, cx + 28, check_y + 28], fill=GREEN)
    draw.text((cx - 12, check_y - 14), "✓", fill=WHITE, font=FONT_BOLD_24)

    # Title
    draw.text((cx - 70, check_y + 40), "Video Ready!", fill=TEXT_DARK, font=FONT_BOLD_24)

    # Video info
    draw.text((cx - 120, check_y + 80), "Duration: 1:12", fill=TEXT_MED, font=FONT_REG_14)
    draw.text((cx + 20, check_y + 80), "|", fill=BORDER, font=FONT_REG_14)
    draw.text((cx + 40, check_y + 80), "Size: 24 MB", fill=TEXT_MED, font=FONT_REG_14)
    draw.text((cx - 60, check_y + 102), "Quality: 1080p", fill=TEXT_MED, font=FONT_REG_14)

    # Three buttons in a row
    btn_y = check_y + 136
    btn_h = 40
    btn_gap = 12

    # Download MP4
    b1x = card_x + 24
    b1w = 148
    draw_button(draw, [b1x, btn_y, b1x + b1w, btn_y + btn_h], "Download MP4", fill=ACCENT, font=FONT_BOLD_14)

    # Copy Share Link
    b2x = b1x + b1w + btn_gap
    b2w = 160
    draw_button(draw, [b2x, btn_y, b2x + b2w, btn_y + btn_h], "Copy Share Link", fill=WHITE, text_color=ACCENT, font=FONT_BOLD_14)
    draw_rounded_rect(draw, [b2x, btn_y, b2x + b2w, btn_y + btn_h], radius=8, outline=ACCENT, width=2)

    # Get Embed Code
    b3x = b2x + b2w + btn_gap
    b3w = 156
    draw_button(draw, [b3x, btn_y, b3x + b3w, btn_y + btn_h], "Get Embed Code", fill=WHITE, text_color=ACCENT, font=FONT_BOLD_14)
    draw_rounded_rect(draw, [b3x, btn_y, b3x + b3w, btn_y + btn_h], radius=8, outline=ACCENT, width=2)

    # Bottom footer bar
    footer_y = card_y + card_h + 16
    draw.text((cx - 140, footer_y), "Want to make changes?", fill=TEXT_MED, font=FONT_REG_13)
    draw.text((cx + 22, footer_y), "Edit Video", fill=ACCENT, font=FONT_BOLD_14)
    draw.text((cx + 110, footer_y), "|", fill=BORDER, font=FONT_REG_13)
    draw.text((cx + 126, footer_y), "Create New", fill=ACCENT, font=FONT_BOLD_14)

    img.save(os.path.join(OUT_DIR, "heygen-download.png"))
    print("  ✓ heygen-download.png")


# ─── Generate all ───
if __name__ == "__main__":
    print("Generating HeyGen UI mockups...")
    gen_homepage()
    gen_dashboard()
    gen_avatar_library()
    gen_script_editor()
    gen_scene_editor()
    gen_timeline()
    gen_voice_selection()
    gen_preview()
    gen_download()
    print("\nAll 9 images generated successfully!")
