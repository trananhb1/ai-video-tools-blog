// Google Analytics GA4 — G-M5NLTFV6FL
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-M5NLTFV6FL', { 'send_page_view': true });

/* AVP_OUTBOUND_TRACKER_v1 */
(function(){
  if (typeof gtag !== 'function') return;
  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var isGo = href.indexOf('/go/') === 0 || href.indexOf('https://aivideopicks.com/go/') === 0;
    var isExt = /^https?:\/\//.test(href) && href.indexOf('aivideopicks.com') === -1;
    if (!isGo && !isExt) return;
    var slug = '';
    var m = href.match(/\/go\/([^\/?#]+)/);
    if (m) slug = m[1];
    else try { slug = (new URL(href)).hostname.replace(/^www\./,''); } catch(_) { slug = href.slice(0,80); }
    gtag('event','affiliate_click', {
      event_category: 'affiliate',
      event_label: slug,
      affiliate_partner: slug,
      affiliate_url: href,
      link_text: (a.innerText||'').trim().slice(0,80),
      page_path: location.pathname,
      transport_type: 'beacon'
    });
  }, true);
})();
