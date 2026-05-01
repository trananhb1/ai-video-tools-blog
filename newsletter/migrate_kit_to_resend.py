#!/usr/bin/env python3
"""
Migrate all Kit (ConvertKit) forms to Resend-powered forms across the site.
Run once: python3 newsletter/migrate_kit_to_resend.py
"""

import re, glob, os

WORKER_URL = "https://aivideopicks-newsletter.trananhb1.workers.dev"
BLOG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "posts")
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RESEND_FORM_JS = f"""<script>
(function(){{
  var W='{WORKER_URL}';
  document.querySelectorAll('form[data-newsletter]').forEach(function(form){{
    form.addEventListener('submit',function(e){{
      e.preventDefault();
      var btn=form.querySelector('button[type="submit"]');
      var ei=form.querySelector('input[name="email"]');
      var ni=form.querySelector('input[name="first_name"]');
      if(!ei||!ei.value)return;
      var ot=btn.textContent;btn.disabled=true;btn.textContent='...';
      fetch(W+'/subscribe',{{method:'POST',headers:{{'Content-Type':'application/json'}},
        body:JSON.stringify({{email:ei.value,first_name:ni?ni.value:''}})
      }}).then(function(r){{return r.json()}}).then(function(d){{
        if(d.success){{form.innerHTML='<p style="color:#155DFC;font-weight:600;margin:8px 0;">You\\'re in! Check your inbox.</p>';
          if(typeof gtag==='function')gtag('event','newsletter_subscribe',{{method:'resend'}});
        }}else{{btn.disabled=false;btn.textContent=ot;}}
      }}).catch(function(){{btn.disabled=false;btn.textContent=ot;}});
    }});
  }});
}})();
</script>"""

changes = 0

def migrate_file(filepath):
    global changes
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    if 'kit.com/forms/9231849' not in content and 'convertkit.com/ckjs' not in content:
        return False

    original = content

    # 1. Replace inline capture forms (email-only, mid-article)
    content = re.sub(
        r'<form\s+action="https://app\.kit\.com/forms/9231849/subscriptions"[^>]*data-sv-form="9231849"[^>]*>\s*'
        r'<input\s+type="email"\s+name="email_address"([^>]*)>\s*'
        r'<button\s+type="submit"([^>]*)>(.*?)</button>\s*'
        r'</form>',
        lambda m: (
            f'<form data-newsletter style="{_extract_style(m.group(0))}">'
            f'<input type="email" name="email"{m.group(1).replace("email_address", "email")}>'
            f'<button type="submit"{m.group(2)}>{m.group(3)}</button>'
            f'</form>'
        ),
        content,
        flags=re.DOTALL
    )

    # 2. Replace full forms (first_name + email)
    content = re.sub(
        r'<form\s+action="https://app\.kit\.com/forms/9231849/subscriptions"[^>]*data-sv-form="9231849"[^>]*>\s*'
        r'(<input\s+type="text"\s+name="fields\[first_name\]"([^>]*)>\s*)?'
        r'<input\s+type="email"\s+name="email_address"([^>]*)>\s*'
        r'<button\s+type="submit"([^>]*)>(.*?)</button>\s*'
        r'</form>',
        lambda m: _build_resend_form(m),
        content,
        flags=re.DOTALL
    )

    # 3. Catch any remaining Kit form patterns (exit popup variant)
    content = re.sub(
        r'<form\s+action="https://app\.kit\.com/forms/9231849/subscriptions"[^>]*>',
        '<form data-newsletter>',
        content
    )
    content = re.sub(r'name="email_address"', 'name="email"', content)
    content = re.sub(r'name="fields\[first_name\]"', 'name="first_name"', content)

    # 4. Remove Kit script
    content = re.sub(
        r'\s*<script\s+async\s+src="https://f\.convertkit\.com/ckjs/ck\.5\.js"></script>',
        '',
        content
    )

    # 5. Add Resend form JS before </body> if any form was converted
    if 'data-newsletter' in content and WORKER_URL not in content:
        content = content.replace('</body>', RESEND_FORM_JS + '\n</body>')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        changes += 1
        return True
    return False


def _extract_style(form_html):
    m = re.search(r'style="([^"]*)"', form_html)
    return m.group(1) if m else ''


def _build_resend_form(m):
    has_name = m.group(1) is not None
    name_attrs = m.group(2) or '' if has_name else ''
    email_attrs = m.group(3) or ''
    btn_attrs = m.group(4) or ''
    btn_text = m.group(5) or 'Subscribe'

    # Clean up attrs
    email_attrs = email_attrs.replace('email_address', 'email')
    name_attrs = name_attrs.replace('fields[first_name]', 'first_name')

    # Extract form style from the surrounding context
    parts = ['<form data-newsletter style="display:flex;gap:10px;flex-wrap:wrap;">']
    if has_name:
        parts.append(f'<input type="text" name="first_name"{name_attrs}>')
    parts.append(f'<input type="email" name="email"{email_attrs}>')
    parts.append(f'<button type="submit"{btn_attrs}>{btn_text}</button>')
    parts.append('</form>')
    return '\n'.join(parts)


def main():
    # Process all post files
    post_files = sorted(glob.glob(os.path.join(BLOG_DIR, "*.html")))
    for f in post_files:
        if migrate_file(f):
            print(f"  Migrated: {os.path.basename(f)}")

    # Process other pages
    for page in ['index.html', 'about.html', 'contact.html']:
        fp = os.path.join(ROOT_DIR, page)
        if os.path.exists(fp) and migrate_file(fp):
            print(f"  Migrated: {page}")

    # Process landing pages
    for f in glob.glob(os.path.join(ROOT_DIR, "landing", "*.html")):
        if migrate_file(f):
            print(f"  Migrated: landing/{os.path.basename(f)}")

    print(f"\nDone. Migrated {changes} files from Kit to Resend.")


if __name__ == "__main__":
    main()
