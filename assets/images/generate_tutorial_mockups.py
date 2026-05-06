#!/usr/bin/env python3
"""Generate tutorial step mockup images for Submagic and HeyGen+Submagic posts."""

from PIL import Image, ImageDraw, ImageFont
import os

W, H = 760, 420

# Brand colors
DARK_HEADER = "#1a1a2e"
ACCENT_SUBMAGIC = "#7C3AED"       # Submagic purple
ACCENT_HEYGEN   = "#4F46E5"       # HeyGen indigo
BG_WHITE  = "#FFFFFF"
BG_LIGHT  = "#f5f5f5"
BG_PANEL  = "#eaeaea"
TEXT_DARK = "#1a1a2e"
TEXT_MED  = "#555555"
TEXT_LIGHT= "#999999"
BORDER    = "#d1d5db"
WHITE     = "#FFFFFF"
GREEN     = "#22c55e"

def font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)

def canvas():
    img = Image.new("RGB", (W, H), BG_WHITE)
    return img, ImageDraw.Draw(img)

def rrect(draw, xy, r, fill=None, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)

def button(draw, xy, text, fill, text_color=WHITE, sz=14):
    rrect(draw, xy, 8, fill=fill)
    x0,y0,x1,y1 = xy
    f = font(sz, bold=True)
    bb = draw.textbbox((0,0), text, font=f)
    tx = x0 + (x1-x0-(bb[2]-bb[0]))//2
    ty = y0 + (y1-y0-(bb[3]-bb[1]))//2 - 1
    draw.text((tx,ty), text, fill=text_color, font=f)

def header(draw, brand="Submagic", accent=ACCENT_SUBMAGIC, subtitle=""):
    draw.rectangle([0,0,W,50], fill=DARK_HEADER)
    draw.text((20,14), brand, fill=WHITE, font=font(20, bold=True))
    if subtitle:
        bb = draw.textbbox((0,0), subtitle, font=font(13))
        draw.text((W - bb[2] - bb[0] - 20, 18), subtitle, fill="#aaaacc", font=font(13))

def progress_bar(draw, steps, active, accent=ACCENT_SUBMAGIC):
    n = len(steps)
    gap = W // (n + 1)
    y = H - 42
    # Line
    draw.line([gap, y, W - gap, y], fill=BORDER, width=2)
    for i, s in enumerate(steps):
        x = gap * (i + 1)
        done = i < active
        curr = i == active
        c = accent if (done or curr) else BG_PANEL
        draw.ellipse([x-14, y-14, x+14, y+14], fill=c, outline=accent if curr else BORDER, width=2 if curr else 1)
        label = str(i+1)
        f = font(11, bold=curr)
        bb = draw.textbbox((0,0), label, font=f)
        draw.text((x-(bb[2]-bb[0])//2, y-(bb[3]-bb[1])//2-1), label, fill=WHITE if (done or curr) else TEXT_LIGHT, font=f)
        bb2 = draw.textbbox((0,0), s, font=font(10))
        draw.text((x-(bb2[2]-bb2[0])//2, y+18), s, fill=accent if curr else TEXT_LIGHT, font=font(10))

# ════════════════════════════════════════════════════════
# SUBMAGIC TUTORIAL: how-to-add-viral-captions-tiktok
# ════════════════════════════════════════════════════════

OUT_S = "/home/user/ai-video-tools-blog/assets/images/how-to-add-viral-captions-tiktok-submagic"

def submagic_step0_hero():
    """Hero: Submagic viral captions on a TikTok video."""
    img, draw = canvas()

    # Dark gradient background
    for i in range(H):
        v = int(26 + i*0.12)
        draw.line([0, i, W, i], fill=(v, int(v*0.8), int(v*1.4)))

    # Phone mockup (left)
    px, py, pw, ph = 80, 30, 170, 340
    rrect(draw, [px, py, px+pw, py+ph], 24, fill="#1a1a1a", outline=WHITE, width=2)
    # Phone screen
    sx, sy, sw, sh = px+10, py+30, pw-20, ph-60
    rrect(draw, [sx, sy, sx+sw, sy+sh], 8, fill="#111111")
    # TikTok video frame simulation
    draw.rectangle([sx+2, sy+2, sx+sw-2, sy+sh-2], fill="#1e1e2e")

    # Caption overlay at bottom of phone
    cap_y = sy + sh - 90
    caption_text = "THIS IS HOW YOU"
    caption2 = "GO VIRAL 🔥"
    draw.text((sx+10, cap_y), caption_text, fill="#FFFF00", font=font(14, bold=True))
    draw.text((sx+10, cap_y+26), caption2, fill=WHITE, font=font(16, bold=True))
    # Highlight word
    rrect(draw, [sx+9, cap_y+25, sx+9+88, cap_y+46], 4, fill=ACCENT_SUBMAGIC)
    draw.text((sx+10, cap_y+26), "VIRAL 🔥", fill=WHITE, font=font(16, bold=True))

    # Right side: Submagic UI panel
    rx = 300
    rrect(draw, [rx, 30, W-30, H-30], 16, fill="#ffffff", outline="#e2d9fb", width=2)

    draw.text((rx+20, 50), "Submagic", fill=ACCENT_SUBMAGIC, font=font(22, bold=True))
    draw.text((rx+20, 82), "Viral Caption Generator", fill=TEXT_MED, font=font(13))

    # Template previews
    templates = [("MrBeast Style", "#FFFF00", "#000000"),
                 ("Hormozi Style", "#FF6B35", WHITE),
                 ("Ali Abdaal", "#22c55e", WHITE)]
    ty = 118
    for name, bg, fg in templates:
        rrect(draw, [rx+20, ty, rx+380, ty+44], 8, fill=bg)
        draw.text((rx+34, ty+12), name, fill=fg, font=font(14, bold=True))
        ty += 54

    draw.text((rx+20, ty+10), "AI detects emphasis words", fill=TEXT_MED, font=font(12))
    draw.text((rx+20, ty+30), "& highlights them automatically", fill=TEXT_MED, font=font(12))

    button(draw, [rx+20, H-80, rx+200, H-48], "Add Captions Free", fill=ACCENT_SUBMAGIC, sz=13)

    img.save(os.path.join(OUT_S, "step-0-hero.png"))
    print("  ✓ step-0-hero.png (Submagic)")


def submagic_step1_signup():
    """Step 1: Submagic signup page."""
    img, draw = canvas()
    header(draw, "Submagic", ACCENT_SUBMAGIC, "Create Account")

    # Center card
    cx = W // 2
    cw, ch = 420, 300
    rrect(draw, [cx-cw//2, 70, cx+cw//2, 70+ch], 16, fill=BG_LIGHT, outline="#e2d9fb", width=2)

    draw.text((cx-60, 90), "Get Started Free", fill=TEXT_DARK, font=font(20, bold=True))
    draw.text((cx-110, 122), "No credit card required • Cancel anytime", fill=TEXT_MED, font=font(12))

    # Social signup buttons
    by = 148
    for label, bg, tc in [("Continue with Google", "#ffffff", TEXT_DARK),
                           ("Continue with Email", ACCENT_SUBMAGIC, WHITE)]:
        rrect(draw, [cx-cw//2+20, by, cx+cw//2-20, by+42], 8, fill=bg, outline=BORDER if bg=="#ffffff" else None, width=1 if bg=="#ffffff" else 0)
        bb = draw.textbbox((0,0), label, font=font(14, bold=True))
        tx = cx - (bb[2]-bb[0])//2
        draw.text((tx, by+11), label, fill=tc, font=font(14, bold=True))
        by += 52

    draw.text((cx-130, 284), "Already have an account? ", fill=TEXT_MED, font=font(12))
    draw.text((cx+8, 284), "Log in →", fill=ACCENT_SUBMAGIC, font=font(12, bold=True))

    # Trust badges
    draw.text((cx-160, 340), "✓ 1M+ creators", fill=GREEN, font=font(12, bold=True))
    draw.text((cx-60, 340), "✓ Free plan available", fill=GREEN, font=font(12, bold=True))
    draw.text((cx+100, 340), "✓ No watermark on paid", fill=GREEN, font=font(12, bold=True))

    progress_bar(draw, ["Sign Up","Upload","Captions","Templates","Export"], 0, ACCENT_SUBMAGIC)

    img.save(os.path.join(OUT_S, "step-1-signup.png"))
    print("  ✓ step-1-signup.png (Submagic)")


def submagic_step2_upload():
    """Step 2: Submagic upload screen."""
    img, draw = canvas()
    header(draw, "Submagic", ACCENT_SUBMAGIC, "New Project")

    # Upload zone (large, centered)
    ux, uy, uw, uh = 80, 70, 600, 240
    rrect(draw, [ux, uy, ux+uw, uy+uh], 16, fill="#faf5ff", outline=ACCENT_SUBMAGIC, width=2)

    # Dashed border simulation
    for i in range(0, uw, 20):
        draw.rectangle([ux+i, uy, ux+i+10, uy+2], fill=ACCENT_SUBMAGIC)
        draw.rectangle([ux+i, uy+uh-2, ux+i+10, uy+uh], fill=ACCENT_SUBMAGIC)
    for i in range(0, uh, 20):
        draw.rectangle([ux, uy+i, ux+2, uy+i+10], fill=ACCENT_SUBMAGIC)
        draw.rectangle([ux+uw-2, uy+i, ux+uw, uy+i+10], fill=ACCENT_SUBMAGIC)

    # Upload icon
    cx, cy = ux + uw//2, uy + 80
    draw.ellipse([cx-30, cy-30, cx+30, cy+30], fill="#ede9fe")
    draw.text((cx-10, cy-16), "↑", fill=ACCENT_SUBMAGIC, font=font(28, bold=True))

    draw.text((cx-80, cy+46), "Drag & drop your video here", fill=TEXT_DARK, font=font(16, bold=True))
    draw.text((cx-50, cy+72), "MP4, MOV, AVI up to 4GB", fill=TEXT_MED, font=font(13))

    button(draw, [cx-80, cy+100, cx+80, cy+132], "Browse Files", fill=ACCENT_SUBMAGIC, sz=14)

    # Or separator
    draw.text((cx-18, uy+uh+14), "— or —", fill=TEXT_LIGHT, font=font(12))

    # URL input
    rrect(draw, [ux, uy+uh+36, ux+uw, uy+uh+68], 8, fill=WHITE, outline=BORDER, width=2)
    draw.text((ux+16, uy+uh+48), "Paste YouTube / TikTok URL...", fill=TEXT_LIGHT, font=font(13))

    progress_bar(draw, ["Sign Up","Upload","Captions","Templates","Export"], 1, ACCENT_SUBMAGIC)

    img.save(os.path.join(OUT_S, "step-2-upload.png"))
    print("  ✓ step-2-upload.png (Submagic)")


def submagic_step4_templates():
    """Step 4: Submagic caption template carousel."""
    img, draw = canvas()
    header(draw, "Submagic", ACCENT_SUBMAGIC, "Choose Template")

    draw.text((30, 62), "Viral Caption Styles", fill=TEXT_DARK, font=font(18, bold=True))
    draw.text((30, 90), "Used by 1M+ creators. Pick a style — AI does the rest.", fill=TEXT_MED, font=font(12))

    templates = [
        ("MrBeast Style", "#000000", "#FFFF00", "Word-by-word, yellow highlight,\nfast pacing — max retention"),
        ("Hormozi Style", "#FF6B35", WHITE,      "Bold orange punch, emphasis\nwords explode on screen"),
        ("Ali Abdaal", "#22c55e", WHITE,          "Clean green, calm pacing —\nperfect for edu content"),
        ("Iman Gadzhi", "#C0A060", "#000000",    "Gold on black, premium feel\nfor business/finance content"),
    ]
    tx = 20
    for i, (name, bg, fg, desc) in enumerate(templates):
        selected = i == 0
        bw = 168
        rrect(draw, [tx, 116, tx+bw, 310], 12, fill=bg,
              outline=ACCENT_SUBMAGIC if selected else BORDER,
              width=3 if selected else 1)

        # Caption preview box inside
        rrect(draw, [tx+10, 126, tx+bw-10, 182], 6, fill=WHITE if bg=="#000000" else "#00000033")
        draw.text((tx+16, 134), name.split()[0], fill=fg if bg!="#000000" else bg, font=font(13, bold=True))

        # Template name
        draw.text((tx+10, 192), name, fill=WHITE if bg not in ("#FFFF00","#C0A060") else "#1a1a2e", font=font(12, bold=True))
        for j, dline in enumerate(desc.split("\n")):
            draw.text((tx+10, 212+j*18), dline, fill=WHITE if bg not in ("#FFFF00","#C0A060") else TEXT_MED, font=font(10))

        if selected:
            rrect(draw, [tx+10, 280, tx+bw-10, 300], 6, fill=ACCENT_SUBMAGIC)
            draw.text((tx+30, 283), "✓ Selected", fill=WHITE, font=font(11, bold=True))

        tx += bw + 10

    button(draw, [W//2-100, H-70, W//2+100, H-42], "Apply Template →", fill=ACCENT_SUBMAGIC, sz=14)

    progress_bar(draw, ["Sign Up","Upload","Captions","Templates","Export"], 3, ACCENT_SUBMAGIC)

    img.save(os.path.join(OUT_S, "step-4-templates.png"))
    print("  ✓ step-4-templates.png (Submagic)")


def submagic_step6_proofread():
    """Step 6: Submagic transcript editor proofreading."""
    img, draw = canvas()
    header(draw, "Submagic", ACCENT_SUBMAGIC, "Proofread & Edit")

    # Split layout
    # Left: video preview
    rrect(draw, [20, 60, 310, 330], 10, fill="#1a1a1a", outline=BORDER)
    # Simulated video frame
    for i in range(60, 330):
        v = int(28 + (i-60)*0.15)
        draw.line([21, i, 309, i], fill=(v, int(v*0.7), int(v*1.3)))
    draw.text((100, 180), "▶  0:12 / 0:47", fill="#ffffffaa", font=font(14))
    # Caption on video
    rrect(draw, [30, 280, 300, 315], 4, fill="#000000bb")
    draw.text((40, 285), "and then you just", fill=WHITE, font=font(13, bold=True))
    rrect(draw, [40+110, 284, 40+110+52, 308], 3, fill=ACCENT_SUBMAGIC)
    draw.text((40+112, 285), "click", fill=WHITE, font=font(13, bold=True))

    # Right: transcript editor
    rx = 330
    draw.text((rx, 62), "Transcript", fill=TEXT_DARK, font=font(16, bold=True))
    draw.text((rx, 84), "Click a word to correct it", fill=TEXT_MED, font=font(12))

    # Word tokens
    words = [
        ("and",   False, False),
        ("then",  False, False),
        ("you",   False, False),
        ("just",  False, False),
        ("klick", True,  False),   # WRONG word — highlighted red
        ("the",   False, False),
        ("button", False, False),
        ("to",    False, False),
        ("export", False, True),   # emphasized
        ("your",  False, False),
        ("video", False, False),
    ]
    wx, wy = rx, 112
    for word, wrong, emph in words:
        bb = draw.textbbox((0,0), word, font=font(13, bold=emph))
        ww = bb[2]-bb[0]+16
        if wx + ww > W - 20:
            wx = rx
            wy += 36
        bg = "#FEE2E2" if wrong else ("#ede9fe" if emph else BG_LIGHT)
        outline = "#EF4444" if wrong else (ACCENT_SUBMAGIC if emph else BORDER)
        rrect(draw, [wx, wy, wx+ww, wy+28], 6, fill=bg, outline=outline, width=2 if wrong else 1)
        draw.text((wx+8, wy+5), word, fill="#EF4444" if wrong else (ACCENT_SUBMAGIC if emph else TEXT_DARK), font=font(13, bold=emph or wrong))
        wx += ww + 8

    # Correction popup for "klick"
    rrect(draw, [rx+30, 200, rx+200, 270], 10, fill=WHITE, outline="#EF4444", width=2)
    draw.text((rx+42, 210), "⚠ Did you mean:", fill="#EF4444", font=font(12, bold=True))
    rrect(draw, [rx+42, 230, rx+120, 256], 6, fill=GREEN)
    draw.text((rx+50, 234), '"click"', fill=WHITE, font=font(13, bold=True))
    rrect(draw, [rx+130, 230, rx+188, 256], 6, fill=BG_PANEL, outline=BORDER)
    draw.text((rx+140, 234), "Ignore", fill=TEXT_MED, font=font(12))

    progress_bar(draw, ["Sign Up","Upload","Captions","Templates","Export"], 5, ACCENT_SUBMAGIC)

    img.save(os.path.join(OUT_S, "step-6-proofread.png"))
    print("  ✓ step-6-proofread.png (Submagic)")


# ════════════════════════════════════════════════════════
# HEYGEN + SUBMAGIC TUTORIAL: how-to-make-faceless-youtube
# ════════════════════════════════════════════════════════

OUT_H = "/home/user/ai-video-tools-blog/assets/images/how-to-make-faceless-youtube-heygen-submagic"

def faceless_step0_hero():
    """Hero: Faceless YouTube workflow overview."""
    img, draw = canvas()

    # Dark background
    for i in range(H):
        v = int(20 + i*0.1)
        draw.line([0, i, W, i], fill=(v, v, int(v*1.5)))

    # Title
    draw.text((40, 30), "Faceless YouTube Channel", fill=WHITE, font=font(22, bold=True))
    draw.text((40, 62), "Powered by AI — No Camera Required", fill="#aaaacc", font=font(14))

    # Workflow steps
    steps = [
        ("1", "Write Script", ACCENT_HEYGEN, "GPT or Claude"),
        ("2", "AI Avatar",    "#6366f1",     "HeyGen"),
        ("3", "Add Captions", ACCENT_SUBMAGIC, "Submagic"),
        ("4", "Upload",       "#22c55e",     "YouTube Studio"),
    ]

    sx = 40
    for num, title, color, tool in steps:
        rrect(draw, [sx, 110, sx+150, 300], 12, fill=color)
        draw.text((sx+56, 128), num, fill=WHITE, font=font(32, bold=True))
        draw.text((sx+10, 200), title, fill=WHITE, font=font(14, bold=True))
        draw.text((sx+10, 224), tool, fill="#ffffffcc", font=font(12))

        if sx + 150 < W - 40:
            ax = sx + 162
            draw.text((ax, 196), "→", fill="#6666aa", font=font(20, bold=True))
        sx += 175

    # Bottom stats
    stats = [("$0/mo", "Camera cost"), ("15min", "Per video"), ("Avatar V", "Tech used"), ("100%", "AI-generated")]
    bx = 40
    for val, lab in stats:
        rrect(draw, [bx, 318, bx+150, 390], 10, fill="#ffffff11", outline="#ffffff22")
        bb = draw.textbbox((0,0), val, font=font(18, bold=True))
        draw.text((bx + (150-(bb[2]-bb[0]))//2, 328), val, fill=WHITE, font=font(18, bold=True))
        bb2 = draw.textbbox((0,0), lab, font=font(11))
        draw.text((bx + (150-(bb2[2]-bb2[0]))//2, 358), lab, fill="#aaaacc", font=font(11))
        bx += 175

    img.save(os.path.join(OUT_H, "step-0-hero.png"))
    print("  ✓ step-0-hero.png (Faceless YT)")


def faceless_step3_heygen_signup():
    """Step 3: HeyGen signup / dashboard first view."""
    img, draw = canvas()
    header(draw, "HeyGen", ACCENT_HEYGEN, "Welcome")

    # Welcome card
    cx = W // 2
    rrect(draw, [cx-250, 65, cx+250, 310], 16, fill=BG_LIGHT, outline="#c7d2fe", width=2)

    draw.text((cx-80, 82), "Welcome to HeyGen!", fill=TEXT_DARK, font=font(18, bold=True))
    draw.text((cx-130, 110), "Start creating AI avatar videos in minutes", fill=TEXT_MED, font=font(13))

    # Plan selector
    for i, (plan, price, active) in enumerate([("Free", "$0/mo", False),
                                                ("Creator", "$29/mo", True),
                                                ("Business", "$89/mo", False)]):
        px = cx - 210 + i*148
        bg = ACCENT_HEYGEN if active else WHITE
        rrect(draw, [px, 140, px+136, 220], 10, fill=bg, outline=ACCENT_HEYGEN if active else BORDER, width=2)
        tc = WHITE if active else TEXT_DARK
        draw.text((px+10, 150), plan, fill=tc, font=font(14, bold=True))
        draw.text((px+10, 174), price, fill=tc, font=font(13))
        if active:
            draw.text((px+10, 198), "Most Popular", fill="#c7d2fe", font=font(11, bold=True))

    button(draw, [cx-120, 240, cx+120, 278], "Start Free Trial", fill=ACCENT_HEYGEN, sz=15)

    draw.text((cx-120, 290), "✓ Avatar V included  ✓ 175 languages  ✓ No camera", fill=TEXT_MED, font=font(11))

    # Trust indicators
    draw.text((50, 340), "Used by 50,000+ creators and businesses worldwide", fill=TEXT_LIGHT, font=font(12))

    img.save(os.path.join(OUT_H, "step-3-heygen-signup.png"))
    print("  ✓ step-3-heygen-signup.png (Faceless YT)")


def faceless_step5_scene_editor():
    """Step 5: HeyGen scene editor with avatar."""
    img, draw = canvas()
    header(draw, "HeyGen", ACCENT_HEYGEN, "Scene Editor")

    # Main video preview (center-left)
    pvx, pvy, pvw, pvh = 20, 58, 440, 270
    rrect(draw, [pvx, pvy, pvx+pvw, pvy+pvh], 10, fill="#2d2d44")
    for i in range(pvh):
        v = int(28 + i*0.12)
        draw.line([pvx+1, pvy+i, pvx+pvw-1, pvy+i], fill=(v, int(v*0.9), int(v*1.6)))
    rrect(draw, [pvx, pvy, pvx+pvw, pvy+pvh], 10, outline="#6366f1", width=2)

    # Avatar silhouette
    acx, acy = pvx + pvw//2 - 40, pvy + pvh//2 + 10
    draw.ellipse([acx-28, acy-70, acx+28, acy-14], fill="#6b7280")
    draw.rounded_rectangle([acx-42, acy-10, acx+42, acy+70], radius=20, fill="#6b7280")

    # Script overlay on video
    rrect(draw, [pvx+10, pvy+pvh-45, pvx+pvw-10, pvy+pvh-12], 6, fill="#00000099")
    draw.text((pvx+20, pvy+pvh-41), '"Welcome to our channel — no camera needed!"', fill=WHITE, font=font(12))

    # "Avatar V" badge
    rrect(draw, [pvx+pvw-90, pvy+8, pvx+pvw-8, pvy+30], 6, fill=ACCENT_HEYGEN)
    draw.text((pvx+pvw-84, pvy+11), "Avatar V", fill=WHITE, font=font(11, bold=True))

    # Right panel
    rpx = 476
    rrect(draw, [rpx, 58, W-16, H-16], 10, fill=BG_LIGHT, outline=BORDER)
    draw.text((rpx+12, 68), "Scene Controls", fill=TEXT_DARK, font=font(15, bold=True))

    draw.text((rpx+12, 100), "Avatar", fill=TEXT_MED, font=font(13, bold=True))
    rrect(draw, [rpx+12, 120, rpx+258, 148], 6, fill=WHITE, outline=BORDER)
    draw.text((rpx+22, 127), "Avatar V — Emma  ▼", fill=TEXT_DARK, font=font(12))

    draw.text((rpx+12, 160), "Script", fill=TEXT_MED, font=font(13, bold=True))
    rrect(draw, [rpx+12, 180, rpx+258, 240], 6, fill=WHITE, outline=BORDER)
    draw.text((rpx+18, 188), "Welcome to our channel —", fill=TEXT_DARK, font=font(11))
    draw.text((rpx+18, 206), "no camera needed!", fill=TEXT_DARK, font=font(11))

    draw.text((rpx+12, 252), "Background", fill=TEXT_MED, font=font(13, bold=True))
    colors_bg = ["#1a1a2e","#0f3460","#FFFFFF","#f5f5f5"]
    cx2 = rpx + 12
    for c in colors_bg:
        rrect(draw, [cx2, 272, cx2+32, 300], 6, fill=c, outline=BORDER)
        cx2 += 38

    button(draw, [rpx+12, H-52, rpx+258, H-24], "Generate Video →", fill=ACCENT_HEYGEN, sz=13)

    img.save(os.path.join(OUT_H, "step-5-scene-editor.png"))
    print("  ✓ step-5-scene-editor.png (Faceless YT)")


def faceless_step8_submagic():
    """Step 8: Submagic applied to HeyGen video — final captions."""
    img, draw = canvas()
    header(draw, "Submagic", ACCENT_SUBMAGIC, "Final Export")

    # Left: video with captions
    vx, vy, vw, vh = 20, 58, 400, 290
    rrect(draw, [vx, vy, vx+vw, vy+vh], 10, fill="#1a1a2e")
    for i in range(vh):
        v = int(26 + i*0.1)
        draw.line([vx+1, vy+i, vx+vw-1, vy+i], fill=(v, int(v*0.8), int(v*1.4)))

    # Avatar in video
    acx, acy = vx+vw//2-30, vy+vh//2+10
    draw.ellipse([acx-24, acy-58, acx+24, acy-10], fill="#6b7280")
    draw.rounded_rectangle([acx-36, acy-6, acx+36, acy+60], radius=16, fill="#6b7280")

    # Viral caption overlay
    rrect(draw, [vx+10, vy+vh-65, vx+vw-10, vy+vh-12], 4, fill="#000000cc")
    draw.text((vx+20, vy+vh-61), "NO CAMERA", fill="#FFFF00", font=font(16, bold=True))
    draw.text((vx+20, vy+vh-38), "REQUIRED", fill=WHITE, font=font(16, bold=True))

    # Caption style badge
    rrect(draw, [vx+vw-110, vy+8, vx+vw-8, vy+30], 6, fill=ACCENT_SUBMAGIC)
    draw.text((vx+vw-104, vy+11), "MrBeast Style", fill=WHITE, font=font(11, bold=True))

    # Right panel: export options
    rpx = 440
    rrect(draw, [rpx, 58, W-20, H-16], 12, fill=BG_LIGHT, outline="#e2d9fb", width=2)

    draw.text((rpx+16, 70), "Ready to Export!", fill=GREEN, font=font(16, bold=True))
    draw.text((rpx+16, 96), "Your faceless YouTube video is", fill=TEXT_MED, font=font(12))
    draw.text((rpx+16, 114), "captioned and ready to upload.", fill=TEXT_MED, font=font(12))

    # Stats
    stats = [("Duration", "3:24"), ("Captions", "142 words"), ("Style", "MrBeast")]
    sy = 140
    for label, val in stats:
        draw.text((rpx+16, sy), f"{label}:", fill=TEXT_LIGHT, font=font(11))
        draw.text((rpx+100, sy), val, fill=TEXT_DARK, font=font(11, bold=True))
        sy += 22

    # Export buttons
    button(draw, [rpx+16, 220, rpx+268, 254], "Download MP4  ↓", fill=ACCENT_SUBMAGIC, sz=13)

    rrect(draw, [rpx+16, 264, rpx+268, 298], 8, fill=WHITE, outline="#FF0000", width=2)
    draw.text((rpx+66, 273), "▶ Upload to YouTube", fill="#FF0000", font=font(13, bold=True))

    draw.text((rpx+16, 316), "✓ 1080p HD", fill=GREEN, font=font(11, bold=True))
    draw.text((rpx+100, 316), "✓ No watermark", fill=GREEN, font=font(11, bold=True))
    draw.text((rpx+220, 316), "✓ FTC safe", fill=GREEN, font=font(11, bold=True))

    draw.text((rpx+16, 354), "Workflow: HeyGen → Submagic → YouTube", fill=TEXT_LIGHT, font=font(11))
    draw.text((rpx+16, 372), "Total time: ~15 minutes per video", fill=TEXT_LIGHT, font=font(11))

    img.save(os.path.join(OUT_H, "step-8-submagic.png"))
    print("  ✓ step-8-submagic.png (Faceless YT)")


if __name__ == "__main__":
    print("=== Generating Submagic tutorial images ===")
    submagic_step0_hero()
    submagic_step1_signup()
    submagic_step2_upload()
    submagic_step4_templates()
    submagic_step6_proofread()

    print("\n=== Generating HeyGen+Submagic faceless YT images ===")
    faceless_step0_hero()
    faceless_step3_heygen_signup()
    faceless_step5_scene_editor()
    faceless_step8_submagic()

    print("\nAll 9 tutorial images generated.")
