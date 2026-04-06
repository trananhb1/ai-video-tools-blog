#!/usr/bin/env python3
"""
AI Video Picks — Pre-Publish Content Reviewer
Validates articles before deployment: content, thumbnails, internal links, SEO.

Usage:
    python3 review_content.py                    # Review all posts
    python3 review_content.py posts/my-post.html # Review specific file(s)
    python3 review_content.py --staged           # Review only git-staged files
"""

import os
import sys
import re
import glob
import json
import subprocess
from html.parser import HTMLParser
from collections import defaultdict

# ─── Config ──────────────────────────────────────────────────────────────────
SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(SITE_ROOT, "posts")
ASSETS_DIR = os.path.join(SITE_ROOT, "assets", "images")
INDEX_HTML = os.path.join(SITE_ROOT, "index.html")
SITEMAP_XML = os.path.join(SITE_ROOT, "sitemap.xml")
GA_ID = "G-M5NLTFV6FL"
DOMAIN = "https://aivideopicks.com"
MAX_TITLE_LEN = 60
MAX_DESC_LEN = 160

# Known affiliate link patterns
AFFILIATE_PATTERNS = [
    "amzn.to", "via=", "a_aid=", "?ref=", "partner", "affiliate",
]

# Required elements in every post
REQUIRED_META = ["title", "description", "canonical", "og:title", "og:description", "og:image"]
REQUIRED_SCHEMA = ["Article"]  # minimum schema type
REQUIRED_SECTIONS = ["ftc", "h1", "h2"]

# ─── HTML Parser ─────────────────────────────────────────────────────────────
class ArticleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.meta = {}
        self.links = []           # all hrefs
        self.internal_links = []  # relative links to other posts
        self.external_links = []  # external links
        self.affiliate_links = [] # links with affiliate patterns
        self.images = []
        self.headings = []        # (level, text)
        self.schemas = []
        self.has_ga = False
        self.has_ftc = False
        self.has_toc = False
        self.has_faq = False
        self.has_canonical = False
        self.canonical_url = ""
        self.og_image = ""
        self.title_tag = ""
        self.meta_desc = ""
        self._in_title = False
        self._in_heading = None
        self._heading_text = ""
        self._in_script = False
        self._script_text = ""
        self._current_tag = ""
        self._current_attrs = {}

        # Link validation
        self.links_missing_rel = []     # affiliate links without nofollow
        self.links_missing_target = []  # external links without target=_blank
        self.lazy_images = 0
        self.total_images = 0

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self._current_tag = tag
        self._current_attrs = attrs_dict

        if tag == "title":
            self._in_title = True

        elif tag == "meta":
            name = attrs_dict.get("name", "")
            prop = attrs_dict.get("property", "")
            content = attrs_dict.get("content", "")
            if name == "description":
                self.meta["description"] = content
                self.meta_desc = content
            elif name == "robots":
                self.meta["robots"] = content
            elif prop == "og:title":
                self.meta["og:title"] = content
            elif prop == "og:description":
                self.meta["og:description"] = content
            elif prop == "og:image":
                self.meta["og:image"] = content
                self.og_image = content
            elif prop == "og:type":
                self.meta["og:type"] = content
            elif name == "twitter:title":
                self.meta["twitter:title"] = content
            elif name == "twitter:description":
                self.meta["twitter:description"] = content

        elif tag == "link":
            rel = attrs_dict.get("rel", "")
            href = attrs_dict.get("href", "")
            if "canonical" in rel:
                self.has_canonical = True
                self.canonical_url = href
                self.meta["canonical"] = href

        elif tag == "script":
            src = attrs_dict.get("src", "")
            if GA_ID in src or "gtag" in src:
                self.has_ga = True
            stype = attrs_dict.get("type", "")
            if stype == "application/ld+json":
                self._in_script = True
                self._script_text = ""

        elif tag == "a":
            href = attrs_dict.get("href", "")
            rel = attrs_dict.get("rel", "")
            target = attrs_dict.get("target", "")

            if href:
                self.links.append(href)

                # Classify link
                is_external = href.startswith("http") or href.startswith("//")
                is_internal_post = (not is_external and href.endswith(".html")
                                    and not href.startswith("#")
                                    and not href.startswith("mailto:"))

                is_affiliate = any(p in href for p in AFFILIATE_PATTERNS)

                if is_internal_post:
                    self.internal_links.append(href)
                elif is_external:
                    self.external_links.append(href)
                    if target != "_blank" and not href.startswith("#"):
                        self.links_missing_target.append(href)

                if is_affiliate:
                    self.affiliate_links.append(href)
                    if "nofollow" not in rel and "sponsored" not in rel:
                        self.links_missing_rel.append(href)

        elif tag == "img":
            src = attrs_dict.get("src", "")
            loading = attrs_dict.get("loading", "")
            self.images.append(src)
            self.total_images += 1
            if loading == "lazy":
                self.lazy_images += 1

        elif tag in ("h1", "h2", "h3", "h4"):
            self._in_heading = tag
            self._heading_text = ""

        elif tag == "div":
            cls = attrs_dict.get("class", "")
            style = attrs_dict.get("style", "")
            if "ftc" in cls.lower() or "disclosure" in cls.lower():
                self.has_ftc = True
            if "toc" in cls.lower() or "table-of-contents" in cls.lower():
                self.has_toc = True

    def handle_data(self, data):
        if self._in_title:
            self.title_tag += data

        if self._in_heading:
            self._heading_text += data

        if self._in_script:
            self._script_text += data

        # Check for FTC text
        text_lower = data.strip().lower()
        if any(phrase in text_lower for phrase in [
            "affiliate", "commission", "ftc", "disclosure",
            "we may earn", "at no extra cost"
        ]):
            self.has_ftc = True

        # Check for GA inline
        if GA_ID in data:
            self.has_ga = True

        # Check for TOC
        if "table of contents" in text_lower:
            self.has_toc = True

        # Check for FAQ
        if "frequently asked" in text_lower or "faq" in text_lower:
            self.has_faq = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
            self.meta["title"] = self.title_tag.strip()

        if tag in ("h1", "h2", "h3", "h4") and self._in_heading == tag:
            level = int(tag[1])
            self.headings.append((level, self._heading_text.strip()))
            self._in_heading = None

        if tag == "script" and self._in_script:
            self._in_script = False
            try:
                schema = json.loads(self._script_text)
                stype = schema.get("@type", "")
                if stype:
                    self.schemas.append(stype)
                # Check mainEntity for FAQ
                if stype == "FAQPage" or "mainEntity" in schema:
                    self.has_faq = True
            except (json.JSONDecodeError, ValueError):
                pass


# ─── Validators ──────────────────────────────────────────────────────────────

def load_index_thumbs():
    """Parse index.html to get thumb-class -> image-file mapping and post -> thumb-class mapping."""
    thumb_map = {}   # class -> image file
    post_thumbs = {} # post filename -> thumb class

    if not os.path.exists(INDEX_HTML):
        return thumb_map, post_thumbs

    with open(INDEX_HTML, "r") as f:
        content = f.read()

    # Extract CSS: .card-thumb.thumb-XXX { background-image: url('...'); }
    for m in re.finditer(r'\.card-thumb\.thumb-([\w-]+)\s*\{[^}]*url\([\'"]?([^\'")]+)[\'"]?\)', content):
        cls = m.group(1)
        img = m.group(2)
        thumb_map[cls] = img

    # Extract card -> post mapping
    # Pattern: <div class="card-thumb thumb-XXX"> ... <a href="posts/YYY.html">
    card_pattern = re.compile(
        r'card-thumb\s+thumb-([\w-]+).*?href=["\']posts/([\w-]+\.html)["\']',
        re.DOTALL
    )
    for m in card_pattern.finditer(content):
        cls = m.group(1)
        post = m.group(2)
        post_thumbs[post] = cls

    return thumb_map, post_thumbs


def load_sitemap_urls():
    """Get all URLs from sitemap.xml."""
    urls = set()
    if os.path.exists(SITEMAP_XML):
        with open(SITEMAP_XML, "r") as f:
            for m in re.finditer(r"<loc>(.*?)</loc>", f.read()):
                urls.add(m.group(1))
    return urls


def get_all_posts():
    """List all HTML files in posts/."""
    return sorted(glob.glob(os.path.join(POSTS_DIR, "*.html")))


def validate_post(filepath, thumb_map, post_thumbs, sitemap_urls, all_post_files):
    """Run all checks on a single post file. Returns (errors, warnings, info)."""
    errors = []
    warnings = []
    info = []

    filename = os.path.basename(filepath)
    rel_path = os.path.relpath(filepath, SITE_ROOT)

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    parser = ArticleParser()
    parser.feed(content)

    # ── 1. META TAGS ─────────────────────────────────────────────────────
    title = parser.meta.get("title", "")
    desc = parser.meta.get("description", "")

    if not title:
        errors.append("Missing <title> tag")
    elif len(title) > MAX_TITLE_LEN:
        warnings.append(f"Title too long: {len(title)} chars (max {MAX_TITLE_LEN}): \"{title}\"")

    if not desc:
        errors.append("Missing meta description")
    elif len(desc) > MAX_DESC_LEN:
        warnings.append(f"Description too long: {len(desc)} chars (max {MAX_DESC_LEN})")

    for meta_key in REQUIRED_META:
        if meta_key not in parser.meta:
            errors.append(f"Missing required meta: {meta_key}")

    if not parser.has_canonical:
        errors.append("Missing canonical URL")
    elif parser.canonical_url:
        expected = f"{DOMAIN}/{rel_path}"
        if parser.canonical_url != expected and parser.canonical_url != f"{DOMAIN}/posts/{filename}":
            warnings.append(f"Canonical URL mismatch: {parser.canonical_url}")

    # ── 2. GOOGLE ANALYTICS ──────────────────────────────────────────────
    if not parser.has_ga:
        errors.append(f"Missing Google Analytics ({GA_ID})")

    # ── 3. SCHEMA MARKUP ─────────────────────────────────────────────────
    if not parser.schemas:
        errors.append("No JSON-LD schema found")
    else:
        if "Article" not in parser.schemas:
            warnings.append("Missing Article schema (found: " + ", ".join(parser.schemas) + ")")
        info.append(f"Schemas: {', '.join(parser.schemas)}")

    # ── 4. FTC DISCLOSURE ────────────────────────────────────────────────
    if parser.affiliate_links and not parser.has_ftc:
        errors.append("Has affiliate links but no FTC disclosure")

    # ── 5. CONTENT STRUCTURE ─────────────────────────────────────────────
    h1_count = sum(1 for h in parser.headings if h[0] == 1)
    h2_count = sum(1 for h in parser.headings if h[0] == 2)

    if h1_count == 0:
        errors.append("No H1 heading found")
    elif h1_count > 1:
        warnings.append(f"Multiple H1 headings ({h1_count})")

    if h2_count == 0:
        warnings.append("No H2 headings found — thin content?")

    if not parser.has_toc and h2_count >= 3:
        warnings.append(f"No Table of Contents found (article has {h2_count}+ sections)")

    # ── 6. THUMBNAIL CHECK ───────────────────────────────────────────────
    og_image = parser.og_image

    if not og_image:
        errors.append("No og:image set — no thumbnail for social sharing")
    else:
        # Check if thumbnail file exists
        if og_image.startswith(DOMAIN):
            img_path = og_image.replace(DOMAIN + "/", "")
            full_path = os.path.join(SITE_ROOT, img_path)
            if not os.path.exists(full_path):
                errors.append(f"Thumbnail file not found: {img_path}")
            else:
                # Check image dimensions
                try:
                    from PIL import Image
                    img = Image.open(full_path)
                    w, h = img.size
                    if w != 600 or h != 340:
                        warnings.append(f"Thumbnail size {w}x{h}, expected 600x340")
                    info.append(f"Thumbnail: {img_path} ({w}x{h})")
                except ImportError:
                    info.append(f"Thumbnail: {img_path} (install Pillow to check dimensions)")
                except Exception:
                    warnings.append(f"Could not read thumbnail: {img_path}")

    # Check homepage card has thumbnail
    if filename in post_thumbs:
        thumb_cls = post_thumbs[filename]
        if thumb_cls in thumb_map:
            thumb_file = thumb_map[thumb_cls]
            thumb_path = os.path.join(SITE_ROOT, thumb_file)
            if not os.path.exists(thumb_path):
                errors.append(f"Homepage thumbnail missing: {thumb_file} (class: thumb-{thumb_cls})")
        info.append(f"Homepage card: thumb-{thumb_cls}")
    else:
        warnings.append("Post not listed on homepage (no card found in index.html)")

    # ── 7. INTERNAL LINKS ────────────────────────────────────────────────
    all_post_names = {os.path.basename(p) for p in all_post_files}

    broken_internal = []
    for link in parser.internal_links:
        # Resolve relative path from the post's directory
        if link.startswith("/"):
            resolved = os.path.join(SITE_ROOT, link.lstrip("/"))
        else:
            resolved = os.path.normpath(os.path.join(os.path.dirname(filepath), link))
        if not os.path.exists(resolved):
            broken_internal.append(link)

    if broken_internal:
        for bl in broken_internal:
            errors.append(f"Broken internal link: {bl}")

    # Check for back-link to roundup (important for SEO)
    has_roundup_link = any("best-ai-video-tools" in l for l in parser.internal_links)
    if filename != "best-ai-video-tools-2026.html" and not has_roundup_link:
        warnings.append("No back-link to the roundup (best-ai-video-tools-2026.html)")

    # Count internal links
    if len(parser.internal_links) == 0:
        warnings.append("No internal links to other posts")
    elif len(parser.internal_links) < 3:
        warnings.append(f"Only {len(parser.internal_links)} internal links (aim for 3+)")

    info.append(f"Internal links: {len(parser.internal_links)}, External: {len(parser.external_links)}")

    # ── 8. AFFILIATE LINK COMPLIANCE ─────────────────────────────────────
    if parser.links_missing_rel:
        for link in parser.links_missing_rel[:3]:
            short = link[:80] + "..." if len(link) > 80 else link
            errors.append(f"Affiliate link missing rel=\"nofollow sponsored\": {short}")

    if parser.links_missing_target:
        for link in parser.links_missing_target[:3]:
            short = link[:80] + "..." if len(link) > 80 else link
            warnings.append(f"External link missing target=\"_blank\": {short}")

    # ── 9. IMAGE LAZY LOADING ────────────────────────────────────────────
    if parser.total_images > 0:
        non_lazy = parser.total_images - parser.lazy_images
        if non_lazy > 1:  # first image can be eager
            warnings.append(f"{non_lazy}/{parser.total_images} images missing loading=\"lazy\"")

    # ── 10. SITEMAP CHECK ────────────────────────────────────────────────
    expected_url = f"{DOMAIN}/posts/{filename}"
    if expected_url not in sitemap_urls:
        warnings.append(f"Post not in sitemap.xml")

    # ── 11. FAQ CHECK ────────────────────────────────────────────────────
    has_faq_schema = "FAQPage" in parser.schemas
    if parser.has_faq and not has_faq_schema:
        warnings.append("Has FAQ section but no FAQPage schema")
    if has_faq_schema and not parser.has_faq:
        warnings.append("Has FAQPage schema but no visible FAQ section")

    return errors, warnings, info


# ─── Output Formatting ───────────────────────────────────────────────────────

RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"


def print_report(filename, errors, warnings, info):
    """Print a formatted report for one file."""
    status = f"{GREEN}PASS{RESET}" if not errors else f"{RED}FAIL{RESET}"
    if not errors and warnings:
        status = f"{YELLOW}WARN{RESET}"

    print(f"\n{BOLD}[{status}] {filename}{RESET}")

    for e in errors:
        print(f"  {RED}ERROR{RESET}  {e}")
    for w in warnings:
        print(f"  {YELLOW}WARN {RESET}  {w}")
    for i in info:
        print(f"  {DIM}INFO   {i}{RESET}")

    return len(errors) == 0


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    os.chdir(SITE_ROOT)

    # Determine which files to check
    files_to_check = []

    if "--staged" in sys.argv:
        # Only check git-staged post files
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            capture_output=True, text=True
        )
        for f in result.stdout.strip().split("\n"):
            if f.startswith("posts/") and f.endswith(".html"):
                files_to_check.append(os.path.join(SITE_ROOT, f))
        if not files_to_check:
            print(f"{GREEN}No staged post files to review.{RESET}")
            return 0
    elif len(sys.argv) > 1 and sys.argv[1] != "--staged":
        # Specific files
        for arg in sys.argv[1:]:
            if os.path.exists(arg):
                files_to_check.append(os.path.abspath(arg))
            elif os.path.exists(os.path.join(POSTS_DIR, arg)):
                files_to_check.append(os.path.join(POSTS_DIR, arg))
            else:
                print(f"{RED}File not found: {arg}{RESET}")
    else:
        # All posts
        files_to_check = get_all_posts()

    if not files_to_check:
        print("No files to check.")
        return 0

    # Load shared data
    thumb_map, post_thumbs = load_index_thumbs()
    sitemap_urls = load_sitemap_urls()
    all_post_files = get_all_posts()

    print(f"{BOLD}{'='*60}")
    print(f"  AI Video Picks — Content Review")
    print(f"  Checking {len(files_to_check)} file(s)")
    print(f"{'='*60}{RESET}")

    total_errors = 0
    total_warnings = 0
    passed = 0
    failed = 0

    for filepath in files_to_check:
        filename = os.path.basename(filepath)
        errors, warnings, info = validate_post(
            filepath, thumb_map, post_thumbs, sitemap_urls, all_post_files
        )
        ok = print_report(filename, errors, warnings, info)
        total_errors += len(errors)
        total_warnings += len(warnings)
        if ok:
            passed += 1
        else:
            failed += 1

    # Summary
    print(f"\n{BOLD}{'─'*60}")
    print(f"  Summary: {passed} passed, {failed} failed, {total_warnings} warnings")
    print(f"  Total:   {total_errors} errors across {len(files_to_check)} files")
    print(f"{'─'*60}{RESET}")

    if total_errors > 0:
        print(f"\n{RED}{BOLD}  Fix {total_errors} error(s) before publishing.{RESET}\n")
        return 1
    elif total_warnings > 0:
        print(f"\n{YELLOW}{BOLD}  All clear, but {total_warnings} warning(s) to consider.{RESET}\n")
        return 0
    else:
        print(f"\n{GREEN}{BOLD}  All checks passed!{RESET}\n")
        return 0


if __name__ == "__main__":
    sys.exit(main())
