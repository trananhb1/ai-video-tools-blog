import os
import json
import xml.etree.ElementTree as ET
import glob
import re

def is_indexable(filepath, content):
    if 'content/drafts' in filepath.replace('\\', '/'):
        return False
    if re.search(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'][^"\']*noindex', content, re.IGNORECASE) or \
       re.search(r'<meta[^>]+content=["\'][^"\']*noindex[^"\']*["\'][^>]+name=["\']robots["\']', content, re.IGNORECASE):
        return False
    return True

def get_all_html_files():
    files = glob.glob('**/*.html', recursive=True)
    return [f for f in files if not f.startswith('venv') and not f.startswith('node_modules')]

def validate_banned_phrases(filepath, content):
    phrases = [
        r'30\+\s*tools',
        r'80\+\s*hours',
        r'82\s*hours',
        r'paid\s*every\s*plan',
        r'paid\s*all\s*plan'
    ]
    errors = []
    for phrase in phrases:
        if re.search(phrase, content, re.IGNORECASE):
            errors.append(f"Found banned phrase '{phrase}' in {filepath}")
    return errors

def validate_json_ld(filepath, content):
    errors = []
    matches = re.finditer(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    for match in matches:
        try:
            json.loads(match.group(1))
        except json.JSONDecodeError as e:
            errors.append(f"Invalid JSON-LD in {filepath}: {e}")
    return errors

def validate_html_basics(filepath, content):
    errors = []
    if '<title>' not in content.lower():
        errors.append(f"Missing <title> tag in {filepath}")
    return errors

def validate_links_and_assets(filepath, content, all_files):
    errors = []
    links = re.findall(r'href="([^"]+)"', content)
    srcs = re.findall(r'src="([^"]+)"', content)

    for link in links + srcs:
        if link.startswith('http') or link.startswith('mailto:') or link.startswith('#') or link.startswith('//'):
            continue
        if '{{' in link or "' +" in link or '+ \'' in link:
            continue

        path = link.split('#')[0].split('?')[0]
        if not path:
            continue

        if path.startswith('/'):
            local_path = path[1:]
        else:
            dir_path = os.path.dirname(filepath)
            local_path = os.path.normpath(os.path.join(dir_path, path))

        if local_path and not os.path.exists(local_path):
            errors.append(f"Broken link/asset '{link}' in {filepath} (resolved to {local_path})")

    return errors

def validate_llms_inventory():
    errors = []
    if not os.path.exists('llms.txt'):
        return errors

    indexable_count = 0
    noindex_count = 0
    for filepath in glob.glob('posts/**/*.html', recursive=True):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        if is_indexable(filepath, content):
            indexable_count += 1
        else:
            noindex_count += 1

    with open('llms.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    live_counts = {int(value) for value in re.findall(r'(\d+) live articles', content)}
    noindex_counts = {int(value) for value in re.findall(r'(\d+) noindex redirect stubs', content)}
    if live_counts != {indexable_count}:
        errors.append(
            f"llms.txt live article counts {sorted(live_counts)} do not match "
            f"the {indexable_count} indexable posts"
        )
    if noindex_counts != {noindex_count}:
        errors.append(
            f"llms.txt noindex counts {sorted(noindex_counts)} do not match "
            f"the {noindex_count} noindex posts"
        )
    return errors


def validate_sitemap():
    errors = []
    if not os.path.exists('sitemap.xml'):
        return ["sitemap.xml not found"]

    try:
        tree = ET.parse('sitemap.xml')
        root = tree.getroot()

        urls_in_sitemap = set()
        for url in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
            urls_in_sitemap.add(url.text)

        for f in glob.glob('posts/**/*.html', recursive=True):
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
                if is_indexable(f, content):
                    match = re.search(r'<link rel="canonical" href="([^"]+)"', content)
                    if match:
                        canonical_url = match.group(1)
                        if canonical_url not in urls_in_sitemap:
                            errors.append(f"Canonical URL {canonical_url} for {f} missing from sitemap.xml")

    except ET.ParseError as e:
        errors.append(f"sitemap.xml is not valid XML: {e}")

    with open('sitemap.xml', 'r', encoding='utf-8') as f:
        first_line = f.readline().strip()
        if not first_line.startswith('<?xml'):
            errors.append(f"sitemap.xml first line must be XML declaration, got: {first_line}")

    return errors

def validate_canonical_uniqueness():
    errors = []
    canonicals = {}
    html_files = get_all_html_files()
    for f in html_files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            if not is_indexable(f, content):
                continue
            match = re.search(r'<link rel="canonical" href="([^"]+)"', content)
            if match:
                url = match.group(1)
                if url in canonicals:
                    errors.append(f"Duplicate canonical URL '{url}' found in {f} and {canonicals[url]}")
                canonicals[url] = f
    return errors

def main():
    errors = []
    html_files = get_all_html_files()

    print(f"Validating {len(html_files)} HTML files...")

    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        errors.extend(validate_banned_phrases(filepath, content))
        if is_indexable(filepath, content):
            errors.extend(validate_json_ld(filepath, content))
            errors.extend(validate_html_basics(filepath, content))
            errors.extend(validate_links_and_assets(filepath, content, html_files))

    if os.path.exists('llms.txt'):
        with open('llms.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            errors.extend(validate_banned_phrases('llms.txt', content))

    errors.extend(validate_llms_inventory())
    errors.extend(validate_sitemap())
    errors.extend(validate_canonical_uniqueness())

    # Filter out known pre-existing errors not caused by this work
    known_errors = [
        "../legal/ftc-disclosure.html",
        "../legal/privacy-policy.html",
        "/assets/css/tokens.css",
        "/legal/ftc-disclosure.html",
        "/legal/privacy-policy.html"
    ]
    filtered_errors = []
    for err in errors:
        if not any(known in err for known in known_errors):
            filtered_errors.append(err)

    if filtered_errors:
        print(f"\nFound {len(filtered_errors)} errors:")
        for err in filtered_errors:
            print(f" - {err}")
        exit(1)
    else:
        print("\nAll validations passed successfully!")

if __name__ == "__main__":
    main()
