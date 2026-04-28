// Google Analytics GA4 — G-M5NLTFV6FL
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-M5NLTFV6FL', { 'send_page_view': true });

/* AVP_OUTBOUND_TRACKER_v2 (2026-04-25)
 * - affiliate_click ONLY fires for /go/<slug>/ links (or absolute https://aivideopicks.com/go/...).
 *   This stops YouTube/CapCut/Canva/etc. from inflating the affiliate metric.
 * - All other off-site clicks fire as outbound_click so we keep visibility without
 *   polluting affiliate numbers.
 * - link_url is captured on both events so destinations can be split per merchant in GA4
 *   (note: link_url custom dimension may need to be registered in GA4 admin before it
 *   appears in standard reports — until then the value sits in raw event data).
 */
(function(){
  if (typeof gtag !== 'function') return;
  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var isGo = href.indexOf('/go/') === 0 || href.indexOf('https://aivideopicks.com/go/') === 0;
    var isExt = /^https?:\/\//.test(href) && href.indexOf('aivideopicks.com') === -1;
    if (!isGo && !isExt) return;

    var linkText = (a.innerText || '').trim().slice(0, 80);

    if (isGo) {
      var slug = '';
      var m = href.match(/\/go\/([^\/?#]+)/);
      if (m) slug = m[1];
      gtag('event', 'affiliate_click', {
        event_category: 'affiliate',
        event_label: slug,
        affiliate_partner: slug,
        affiliate_url: href,
        link_url: href,
        link_text: linkText,
        page_path: location.pathname,
        transport_type: 'beacon'
      });
      return;
    }

    // Non-affiliate external link — track separately so we keep visibility
    // but don't pollute affiliate metrics.
    var host = '';
    try { host = (new URL(href, location.origin)).hostname.replace(/^www\./, ''); }
    catch (_) { host = href.slice(0, 80); }
    gtag('event', 'outbound_click', {
      event_category: 'outbound',
      event_label: host,
      link_domain: host,
      link_url: href,
      link_text: linkText,
      page_path: location.pathname,
      transport_type: 'beacon'
    });
  }, true);
})();

/* AVP_FORM_TRACKER_v1 (T21 — 2026-04-25)
 * Site-wide newsletter + contact form instrumentation. Reason: GA4 reported 53
 * form_start vs 1 form_submit over 30 days (98% abandonment). Causes identified:
 *   1. Kit forms used target="_blank" — submission opened a new tab where Kit's
 *      reCAPTCHA challenge lives, users never saw confirmation in the tab they
 *      were reading, abandoned the funnel.
 *   2. contact.html had action="https://formspree.io/f/your-form-id" placeholder
 *      — every contact submit went to a 404, no error UI.
 *   3. No custom form_submit gtag — relied on GA4 enhanced-measurement which
 *      under-counts cross-tab submits.
 *
 * Fix:
 *   - Strip target="_blank" from any Kit form on load so reCAPTCHA appears in
 *     the same tab and users see confirmation.
 *   - Fire gtag('event', 'form_submit', ...) on every newsletter / contact
 *     submit with form_destination + page_path so funnel is recoverable in GA4
 *     even before custom dimensions are registered.
 *   - Fire gtag('event', 'form_start', ...) on first focus per form so we own
 *     the start metric (independent of GA4 enhanced measurement).
 */
(function(){
  if (typeof gtag !== 'function') return;
  if (typeof document === 'undefined') return;

  function classify(form){
    var action = (form.getAttribute('action') || '').toLowerCase();
    if (action.indexOf('app.kit.com') !== -1 || action.indexOf('convertkit.com') !== -1) return 'newsletter_kit';
    if (form.classList && form.classList.contains('contact-form')) return 'contact';
    if (action.indexOf('formspree.io') !== -1) return 'contact_formspree';
    if (action.indexOf('mailto:') === 0) return 'contact_mailto';
    return null;
  }

  function instrument(form){
    if (form.__avpFormBound) return;
    form.__avpFormBound = true;

    var dest = classify(form);
    if (!dest) return;

    // Defensive: Kit forms ship with target="_blank" which sends the user to
    // Kit's CAPTCHA in a new tab. Remove it so they stay in flow.
    if (dest === 'newsletter_kit' && form.getAttribute('target') === '_blank') {
      form.removeAttribute('target');
    }

    var startedFired = false;
    form.addEventListener('focusin', function(){
      if (startedFired) return;
      startedFired = true;
      gtag('event', 'form_start', {
        event_category: 'form',
        event_label: dest,
        form_destination: dest,
        page_path: location.pathname
      });
    }, true);

    form.addEventListener('submit', function(){
      gtag('event', 'form_submit', {
        event_category: 'form',
        event_label: dest,
        form_destination: dest,
        page_path: location.pathname,
        transport_type: 'beacon'
      });
    }, true);
  }

  function scan(){
    var forms = document.getElementsByTagName('form');
    for (var i = 0; i < forms.length; i++) instrument(forms[i]);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', scan);
  } else {
    scan();
  }
  // Catch forms injected late (e.g. Kit's ckjs widget).
  setTimeout(scan, 1500);
})();
