/**
 * AI Video Picks — Newsletter + Contact + Tracking Worker (Cloudflare Workers)
 *
 * Routes:
 *   POST /subscribe           — adds contact to Resend Audience, stores source interest
 *   POST /contact             — contact form → inbox via Resend
 *   GET  /t/:hash?url=...     — click-tracking proxy: logs click, redirects to destination
 *   GET  /admin/subscribers   — lists all subscribers with interest profiles
 *   GET  /admin/stats         — subscriber count + engagement summary
 *   GET  /admin/profiles      — all subscriber interest profiles from KV
 *   GET  /admin/profile/:hash — single subscriber profile
 *   POST /admin/send          — send newsletter (supports personalized affiliate picks)
 *   POST /admin/send-personalized — send segment-targeted newsletters
 *
 * KV namespace: TRACKING — stores subscriber profiles and click events
 *   profile:{hash}  → { email, interests: {category: score}, clicks: [...], source, created }
 *   clicks:{date}   → [{ hash, url, category, ts }]  (daily aggregate)
 *
 * Environment variables:
 *   RESEND_API_KEY, AUDIENCE_ID, ADMIN_TOKEN
 */

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': 'https://aivideopicks.com',
  'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Authorization',
};

const FROM_EMAIL = 'Tom from AI Video Picks <newsletter@aivideopicks.com>';
const CONTACT_FROM = 'AI Video Picks Contact Form <contact@aivideopicks.com>';
const CONTACT_INBOX = 'trananhb1@gmail.com';
const REPLY_TO = 'trananhb1@gmail.com';
const SITE_URL = 'https://aivideopicks.com';

// ── Interest category mapping ──────────────────────────────────────────────
const INTEREST_RULES = [
  { pattern: /heygen|synthesia|colossyan|deepbrain|d-id|elai|hourone|avatar/i, category: 'avatars' },
  { pattern: /pictory|invideo|descript|veed|kapwing|repurpos/i, category: 'repurposing' },
  { pattern: /arcads|creatify|makeugc|ugc|ad[- ]?(video|generator|creative)/i, category: 'ads' },
  { pattern: /training|onboarding|enterprise|l&d/i, category: 'training' },
  { pattern: /free|cheapest|budget|pricing|cost|deal|coupon|save/i, category: 'budget' },
  { pattern: /pika|runway|kling|veo|sora|text-to-video|creative/i, category: 'creative' },
  { pattern: /submagic|capcut|opus.clip|caption|shorts|tiktok|reels/i, category: 'shorts' },
  { pattern: /gear|amazon|microphone|webcam|light|stream.deck/i, category: 'gear' },
  { pattern: /fliki|zebracat|murf|elevenlabs|voice|audio/i, category: 'voicevideo' },
  { pattern: /beginner|how.to|tutorial|guide|glossary/i, category: 'learning' },
];

function classifyUrl(url) {
  const categories = [];
  for (const rule of INTEREST_RULES) {
    if (rule.pattern.test(url)) {
      categories.push(rule.category);
    }
  }
  return categories.length ? categories : ['general'];
}

// ── Affiliate picks with interest targeting ────────────────────────────────
const AFFILIATE_PICKS = [
  { name: 'HeyGen', url: 'https://www.heygen.com/?via=aivideopicks', tagline: 'Best for marketing videos & avatars', offer: 'Free plan available', color: '#6C5CE7', icon: 'HG', interests: ['avatars', 'ads'] },
  { name: 'Synthesia', url: 'https://www.synthesia.io/?via=aivideopicks', tagline: 'Enterprise training & L&D', offer: '160+ AI avatars, 130+ languages', color: '#00B894', icon: 'Sy', interests: ['avatars', 'training'] },
  { name: 'Pictory', url: 'https://pictory.ai?ref=aivideopicks', tagline: 'Turn scripts & blogs into videos', offer: 'New 2.0 with AI avatars!', color: '#A29BFE', icon: 'Pc', interests: ['repurposing'] },
  { name: 'InVideo', url: 'https://invideo.sjv.io/aivideopicks', tagline: 'AI video editor for social content', offer: 'Free plan available', color: '#00CEC9', icon: 'IV', interests: ['repurposing', 'budget'] },
  { name: 'Creatify', url: 'https://app.creatify.ai/?via=Aivideopicks', tagline: 'AI ad video generator', offer: '$49 off first month', color: '#FF7675', icon: 'Cr', interests: ['ads'] },
  { name: 'Zebracat', url: 'https://studio.zebracat.ai/?via=aivideopicks', tagline: 'Fast social & ad video creation', offer: 'Code 6YAZM9V5 for 15% off', color: '#FDCB6E', icon: 'Zc', interests: ['ads', 'shorts'] },
  { name: 'Fliki', url: 'https://fliki.ai/?via=aivideopicks', tagline: 'Blog-to-video in minutes', offer: 'Free plan + paid from $28/mo', color: '#0984E3', icon: 'Fk', interests: ['repurposing', 'voicevideo'] },
  { name: 'Pika', url: 'https://pika.style/?via=aivideopicks', tagline: 'Creative text-to-video generation', offer: 'Free tier available', color: '#E17055', icon: 'Pk', interests: ['creative'] },
  { name: 'Submagic', url: 'https://submagic.co/?via=aivideopicks', tagline: 'Viral captions for short-form video', offer: 'Auto-captions in 1 click', color: '#636E72', icon: 'Sm', interests: ['shorts'] },
  { name: 'Arcads', url: 'https://arcads.ai/?via=aivideopicks', tagline: 'AI actors for UGC-style ads', offer: '25% recurring commission', color: '#D63031', icon: 'Ar', interests: ['ads'] },
];

function pickAffiliatesForProfile(profile, count = 4) {
  if (!profile || !profile.interests || Object.keys(profile.interests).length === 0) {
    const shuffled = [...AFFILIATE_PICKS].sort(() => Math.random() - 0.5);
    return shuffled.slice(0, count);
  }

  const sorted = Object.entries(profile.interests).sort((a, b) => b[1] - a[1]);
  const topInterests = sorted.slice(0, 3).map(e => e[0]);

  const scored = AFFILIATE_PICKS.map(pick => {
    let score = Math.random() * 0.3;
    for (const interest of pick.interests) {
      const idx = topInterests.indexOf(interest);
      if (idx !== -1) score += (3 - idx);
    }
    return { ...pick, _score: score };
  });

  scored.sort((a, b) => b._score - a._score);
  return scored.slice(0, count);
}

// ── Hashing ────────────────────────────────────────────────────────────────
async function hashEmail(email) {
  const data = new TextEncoder().encode(email.toLowerCase().trim());
  const buf = await crypto.subtle.digest('SHA-256', data);
  const arr = Array.from(new Uint8Array(buf));
  return arr.map(b => b.toString(16).padStart(2, '0')).join('').slice(0, 16);
}

// ── Subscriber profile helpers ─────────────────────────────────────────────
async function getProfile(env, hash) {
  const raw = await env.TRACKING.get(`profile:${hash}`);
  if (!raw) return null;
  try { return JSON.parse(raw); } catch { return null; }
}

async function upsertProfile(env, hash, updates) {
  const existing = await getProfile(env, hash) || {
    interests: {},
    clicks: [],
    source: null,
    created: new Date().toISOString(),
    email_hash: hash,
  };

  if (updates.source && !existing.source) {
    existing.source = updates.source;
  }
  if (updates.email && !existing.email) {
    existing.email = updates.email;
  }

  if (updates.click) {
    const categories = classifyUrl(updates.click.url);
    for (const cat of categories) {
      existing.interests[cat] = (existing.interests[cat] || 0) + 1;
    }
    existing.clicks.push({
      url: updates.click.url,
      categories,
      ts: new Date().toISOString(),
    });
    if (existing.clicks.length > 100) {
      existing.clicks = existing.clicks.slice(-100);
    }
  }

  if (updates.interests) {
    for (const [cat, score] of Object.entries(updates.interests)) {
      existing.interests[cat] = (existing.interests[cat] || 0) + score;
    }
  }

  await env.TRACKING.put(`profile:${hash}`, JSON.stringify(existing), {
    expirationTtl: 365 * 86400,
  });
  return existing;
}

async function logClick(env, hash, url, categories) {
  const date = new Date().toISOString().slice(0, 10);
  const key = `clicks:${date}`;
  const raw = await env.TRACKING.get(key);
  const log = raw ? JSON.parse(raw) : [];
  log.push({ hash, url, categories, ts: new Date().toISOString() });
  await env.TRACKING.put(key, JSON.stringify(log), {
    expirationTtl: 90 * 86400,
  });
}

// ── Routes ─────────────────────────────────────────────────────────────────
export default {
  async fetch(request, env, ctx) {
    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: CORS_HEADERS });
    }

    const url = new URL(request.url);

    // Click tracking (public, GET)
    if (url.pathname.startsWith('/t/')) {
      return handleClickTrack(url, env, ctx);
    }

    // Admin routes
    if (url.pathname.startsWith('/admin/')) {
      if (!verifyAdmin(request, env)) {
        return jsonResponse({ error: 'Unauthorized' }, 401);
      }
      if (request.method === 'GET' && url.pathname === '/admin/subscribers') {
        return handleAdminSubscribers(env);
      }
      if (request.method === 'GET' && url.pathname === '/admin/stats') {
        return handleAdminStats(env);
      }
      if (request.method === 'GET' && url.pathname === '/admin/profiles') {
        return handleAdminProfiles(env);
      }
      if (request.method === 'GET' && url.pathname.startsWith('/admin/profile/')) {
        const hash = url.pathname.split('/admin/profile/')[1];
        return handleAdminSingleProfile(env, hash);
      }
      if (request.method === 'POST' && url.pathname === '/admin/send') {
        return handleAdminSend(request, env);
      }
      if (request.method === 'POST' && url.pathname === '/admin/send-personalized') {
        return handleAdminSendPersonalized(request, env);
      }
      return jsonResponse({ error: 'Not found' }, 404);
    }

    if (request.method !== 'POST') {
      return jsonResponse({ error: 'Method not allowed' }, 405);
    }
    if (url.pathname === '/subscribe') return handleSubscribe(request, env);
    if (url.pathname === '/contact') return handleContact(request, env);

    return jsonResponse({ error: 'Not found' }, 404);
  },
};

// ── Click tracking ─────────────────────────────────────────────────────────
async function handleClickTrack(url, env, ctx) {
  const hash = url.pathname.split('/t/')[1]?.split('/')[0] || '';
  const dest = url.searchParams.get('url');

  if (!dest) {
    return Response.redirect(SITE_URL, 302);
  }

  let decodedUrl;
  try {
    decodedUrl = decodeURIComponent(dest);
  } catch {
    decodedUrl = dest;
  }

  if (hash && env.TRACKING) {
    const categories = classifyUrl(decodedUrl);
    const updates = { click: { url: decodedUrl } };
    ctx.waitUntil(Promise.all([
      upsertProfile(env, hash, updates),
      logClick(env, hash, decodedUrl, categories),
    ]));
  }

  return Response.redirect(decodedUrl, 302);
}

// ── Admin: profiles ────────────────────────────────────────────────────────
async function handleAdminProfiles(env) {
  try {
    const list = await env.TRACKING.list({ prefix: 'profile:' });
    const profiles = [];
    for (const key of list.keys) {
      const raw = await env.TRACKING.get(key.name);
      if (raw) {
        const profile = JSON.parse(raw);
        const topInterests = Object.entries(profile.interests || {})
          .sort((a, b) => b[1] - a[1])
          .slice(0, 5);
        profiles.push({
          hash: key.name.replace('profile:', ''),
          email: profile.email || null,
          source: profile.source || null,
          interests: Object.fromEntries(topInterests),
          total_clicks: (profile.clicks || []).length,
          last_click: profile.clicks?.length ? profile.clicks[profile.clicks.length - 1].ts : null,
          segment: getSegment(profile),
          created: profile.created,
        });
      }
    }
    return jsonResponse({ total: profiles.length, profiles });
  } catch (err) {
    return jsonResponse({ error: 'Failed to fetch profiles', message: err.message }, 500);
  }
}

async function handleAdminSingleProfile(env, hash) {
  const profile = await getProfile(env, hash);
  if (!profile) {
    return jsonResponse({ error: 'Profile not found' }, 404);
  }
  return jsonResponse({
    ...profile,
    segment: getSegment(profile),
    recommended_picks: pickAffiliatesForProfile(profile).map(p => p.name),
  });
}

function getSegment(profile) {
  if (!profile.interests || Object.keys(profile.interests).length === 0) return 'new';
  const sorted = Object.entries(profile.interests).sort((a, b) => b[1] - a[1]);
  const top = sorted[0];
  if (top[1] >= 5) return top[0];
  if (sorted.length >= 3) return 'explorer';
  return 'warming';
}

// ── Admin: personalized send ───────────────────────────────────────────────
async function handleAdminSendPersonalized(request, env) {
  let body;
  try {
    body = await request.json();
  } catch {
    return jsonResponse({ error: 'Invalid JSON body' }, 400);
  }

  const { subject, html_template, test_email } = body;
  if (!subject || !html_template) {
    return jsonResponse({ error: 'subject and html_template required. Use {{AFFILIATE_SECTION}} placeholder.' }, 400);
  }

  try {
    let contacts;
    if (test_email) {
      contacts = [{ email: test_email }];
    } else {
      const contactRes = await fetch(
        `https://api.resend.com/audiences/${env.AUDIENCE_ID}/contacts`,
        { headers: { Authorization: `Bearer ${env.RESEND_API_KEY}` } }
      );
      const contactData = await contactRes.json();
      if (!contactRes.ok) return jsonResponse({ error: 'Resend error', details: contactData }, 502);
      contacts = (contactData.data || []).filter(c => !c.unsubscribed);
      if (!contacts.length) return jsonResponse({ error: 'No subscribers' }, 400);
    }

    const emails = [];
    for (const contact of contacts) {
      const hash = await hashEmail(contact.email);
      const profile = await getProfile(env, hash);
      const picks = pickAffiliatesForProfile(profile);

      let personalizedHtml = html_template;

      // Replace tracked links: rewrite all aivideopicks.com and affiliate URLs
      personalizedHtml = personalizedHtml.replace(
        /href="(https?:\/\/[^"]+)"/g,
        (match, url) => {
          const tracked = `${new URL(request.url).origin}/t/${hash}?url=${encodeURIComponent(url)}`;
          return `href="${tracked}"`;
        }
      );

      // Replace affiliate section placeholder
      if (personalizedHtml.includes('{{AFFILIATE_SECTION}}')) {
        personalizedHtml = personalizedHtml.replace('{{AFFILIATE_SECTION}}', buildAffiliateHtml(picks, hash, new URL(request.url).origin));
      }

      // Replace name placeholder
      const name = contact.first_name || 'there';
      personalizedHtml = personalizedHtml.replace(/\{\{NAME\}\}/g, name);

      emails.push({
        from: FROM_EMAIL,
        to: [contact.email],
        reply_to: REPLY_TO,
        subject,
        html: personalizedHtml,
      });
    }

    const results = [];
    for (let i = 0; i < emails.length; i += 100) {
      const batch = emails.slice(i, i + 100);
      const sendRes = await fetch('https://api.resend.com/emails/batch', {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${env.RESEND_API_KEY}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(batch),
      });
      const sendData = await sendRes.json();
      results.push({ batch: Math.floor(i / 100) + 1, count: batch.length, response: sendData });
    }

    return jsonResponse({ sent: contacts.length, personalized: true, batches: results });
  } catch (err) {
    return jsonResponse({ error: 'Send failed', message: err.message }, 500);
  }
}

function buildAffiliateHtml(picks, hash, origin) {
  return picks.map(p => {
    const trackedUrl = `${origin}/t/${hash}?url=${encodeURIComponent(p.url)}`;
    return `<tr><td style="padding:6px 0;">
      <table width="100%" cellpadding="0" cellspacing="0" style="background:#ffffff;border:1px solid #e2e4eb;border-radius:10px;">
        <tr>
          <td width="56" style="padding:14px 0 14px 14px;vertical-align:middle;">
            <div style="width:44px;height:44px;border-radius:10px;background:${p.color};text-align:center;line-height:44px;color:#ffffff;font-size:16px;font-weight:800;">${p.icon}</div>
          </td>
          <td style="padding:14px 16px;vertical-align:middle;">
            <a href="${trackedUrl}" style="color:#155DFC;font-size:15px;font-weight:700;text-decoration:none;">${p.name}</a>
            <span style="color:#4a4a68;font-size:13px;"> — ${p.tagline}</span>
            <p style="color:#7a7a96;font-size:12px;margin:4px 0 0;">${p.offer}</p>
          </td>
          <td width="80" style="padding:14px 14px 14px 0;vertical-align:middle;text-align:right;">
            <a href="${trackedUrl}" style="display:inline-block;background:#f0f2f5;color:#155DFC;font-size:12px;font-weight:700;padding:6px 12px;border-radius:6px;text-decoration:none;">Try Free →</a>
          </td>
        </tr>
      </table>
    </td></tr>`;
  }).join('\n');
}

// ── Admin: subscribers + stats (existing) ──────────────────────────────────
function verifyAdmin(request, env) {
  const auth = request.headers.get('Authorization') || '';
  const token = auth.replace(/^Bearer\s+/i, '');
  return token && token === env.ADMIN_TOKEN;
}

async function handleAdminSubscribers(env) {
  try {
    const res = await fetch(
      `https://api.resend.com/audiences/${env.AUDIENCE_ID}/contacts`,
      { headers: { Authorization: `Bearer ${env.RESEND_API_KEY}` } }
    );
    const data = await res.json();
    if (!res.ok) return jsonResponse({ error: 'Resend API error', details: data }, 502);

    const contacts = [];
    for (const c of (data.data || [])) {
      const hash = await hashEmail(c.email);
      const profile = await getProfile(env, hash);
      contacts.push({
        email: c.email,
        first_name: c.first_name || '',
        subscribed: !c.unsubscribed,
        created_at: c.created_at,
        hash,
        segment: profile ? getSegment(profile) : 'new',
        interests: profile?.interests || {},
        total_clicks: profile?.clicks?.length || 0,
      });
    }
    return jsonResponse({
      total: contacts.length,
      subscribed: contacts.filter(c => c.subscribed).length,
      contacts,
    });
  } catch (err) {
    return jsonResponse({ error: 'Failed to fetch subscribers' }, 500);
  }
}

async function handleAdminStats(env) {
  try {
    const res = await fetch(
      `https://api.resend.com/audiences/${env.AUDIENCE_ID}/contacts`,
      { headers: { Authorization: `Bearer ${env.RESEND_API_KEY}` } }
    );
    const data = await res.json();
    if (!res.ok) return jsonResponse({ error: 'Resend API error', details: data }, 502);

    const contacts = data.data || [];
    const subscribed = contacts.filter(c => !c.unsubscribed);
    const lastWeek = new Date(Date.now() - 7 * 86400000).toISOString();
    const recent = subscribed.filter(c => c.created_at >= lastWeek);

    // Segment distribution
    const segments = {};
    for (const c of subscribed) {
      const hash = await hashEmail(c.email);
      const profile = await getProfile(env, hash);
      const seg = profile ? getSegment(profile) : 'new';
      segments[seg] = (segments[seg] || 0) + 1;
    }

    // Today's clicks
    const today = new Date().toISOString().slice(0, 10);
    const todayClicks = await env.TRACKING.get(`clicks:${today}`);
    const clickCount = todayClicks ? JSON.parse(todayClicks).length : 0;

    return jsonResponse({
      total: contacts.length,
      subscribed: subscribed.length,
      unsubscribed: contacts.length - subscribed.length,
      new_last_7_days: recent.length,
      segments,
      clicks_today: clickCount,
      recent_signups: recent.map(c => ({
        email: c.email,
        first_name: c.first_name || '',
        created_at: c.created_at,
      })),
    });
  } catch (err) {
    return jsonResponse({ error: 'Failed to fetch stats' }, 500);
  }
}

// ── Admin: basic send (non-personalized, existing) ─────────────────────────
async function handleAdminSend(request, env) {
  let body;
  try {
    body = await request.json();
  } catch {
    return jsonResponse({ error: 'Invalid JSON body' }, 400);
  }

  const { subject, html, test_email } = body;
  if (!subject || !html) {
    return jsonResponse({ error: 'subject and html are required' }, 400);
  }

  try {
    let active;
    if (test_email) {
      active = [{ email: test_email }];
    } else {
      const contactRes = await fetch(
        `https://api.resend.com/audiences/${env.AUDIENCE_ID}/contacts`,
        { headers: { Authorization: `Bearer ${env.RESEND_API_KEY}` } }
      );
      const contactData = await contactRes.json();
      if (!contactRes.ok) return jsonResponse({ error: 'Failed to fetch contacts', details: contactData }, 502);
      active = (contactData.data || []).filter(c => !c.unsubscribed);
      if (!active.length) return jsonResponse({ error: 'No active subscribers' }, 400);
    }

    const emails = active.map(c => ({
      from: FROM_EMAIL,
      to: [c.email],
      reply_to: REPLY_TO,
      subject,
      html,
    }));

    const results = [];
    for (let i = 0; i < emails.length; i += 100) {
      const batch = emails.slice(i, i + 100);
      const sendRes = await fetch('https://api.resend.com/emails/batch', {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${env.RESEND_API_KEY}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(batch),
      });
      const sendData = await sendRes.json();
      results.push({ batch: Math.floor(i / 100) + 1, count: batch.length, response: sendData });
    }

    return jsonResponse({ sent: active.length, batches: results });
  } catch (err) {
    return jsonResponse({ error: 'Send failed', message: err.message }, 500);
  }
}

// ── Subscribe (with source tracking) ───────────────────────────────────────
async function handleSubscribe(request, env) {
  let body;
  const contentType = request.headers.get('content-type') || '';

  if (contentType.includes('application/json')) {
    body = await request.json();
  } else if (contentType.includes('form')) {
    const formData = await request.formData();
    body = Object.fromEntries(formData);
  } else {
    return jsonResponse({ error: 'Invalid content type' }, 400);
  }

  const email = (body.email || '').trim().toLowerCase();
  const firstName = (body.first_name || body.firstName || '').trim();
  const source = (body.source || '').trim();

  if (!email || !email.includes('@')) {
    return jsonResponse({ error: 'Valid email required' }, 400);
  }

  try {
    const contactRes = await fetch(
      `https://api.resend.com/audiences/${env.AUDIENCE_ID}/contacts`,
      {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${env.RESEND_API_KEY}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email,
          first_name: firstName || undefined,
          unsubscribed: false,
        }),
      }
    );

    const contactData = await contactRes.json();
    if (!contactRes.ok) {
      console.error('Resend contact error:', contactData);
      return jsonResponse({ error: 'Signup failed, please try again' }, 500);
    }

    // Track source interest in KV
    const hash = await hashEmail(email);
    const sourceInterests = {};
    if (source) {
      const cats = classifyUrl(source);
      for (const cat of cats) sourceInterests[cat] = 2;
    }
    await upsertProfile(env, hash, {
      email,
      source: source || 'direct',
      interests: sourceInterests,
    });

    sendWelcomeEmail(email, firstName, env).catch(console.error);

    return jsonResponse({ success: true, message: 'Subscribed!' });
  } catch (err) {
    console.error('Subscribe error:', err);
    return jsonResponse({ error: 'Something went wrong' }, 500);
  }
}

// ── Welcome email ──────────────────────────────────────────────────────────
async function sendWelcomeEmail(email, firstName, env) {
  const name = firstName || 'there';

  const html = `<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
<body style="margin:0;padding:0;background:#f0f2f5;font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#f0f2f5;padding:20px 0;">
<tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;">
  <tr><td style="background:linear-gradient(135deg,#155DFC 0%,#1a1a2e 100%);padding:32px 24px;border-radius:12px 12px 0 0;text-align:center;">
    <h1 style="color:#ffffff;font-size:22px;font-weight:800;margin:0;">AI Video <span style="color:#60a5fa;">Picks</span></h1>
    <p style="color:#94a3b8;font-size:13px;margin:8px 0 0;">Welcome to AI Video Picks!</p>
  </td></tr>
  <tr><td style="background:#ffffff;padding:28px 24px;">
    <p style="color:#1a1a2e;font-size:16px;line-height:1.6;margin:0;">Hey ${name}!</p>
    <p style="color:#4a4a68;font-size:14px;line-height:1.7;margin:16px 0;">Welcome to <strong>AI Video Picks</strong> — your weekly shortcut to the best AI video tools, tips, and honest reviews.</p>
    <p style="color:#4a4a68;font-size:14px;line-height:1.7;">Every weekend I'll send you a digest of new reviews, trending tools, and exclusive deals. Here's your quick start:</p>
    <table cellpadding="0" cellspacing="0" style="margin:20px 0;"><tr><td>
      <a href="${SITE_URL}/posts/best-ai-video-tools-2026.html?utm_source=welcome&utm_medium=email" style="display:inline-block;background:#155DFC;color:#ffffff;font-size:14px;font-weight:700;padding:12px 28px;border-radius:8px;text-decoration:none;">Read the Top 10 AI Video Tools →</a>
    </td></tr></table>
    <p style="color:#4a4a68;font-size:14px;line-height:1.7;">Hit reply and tell me what you want to create — I read every one.</p>
    <p style="color:#1a1a2e;font-size:14px;margin:24px 0 0;">Talk soon,<br><strong>Tom</strong><br><span style="color:#7a7a96;">AI Video Picks</span></p>
  </td></tr>
  <tr><td style="background:#1a1a2e;padding:20px 24px;border-radius:0 0 12px 12px;text-align:center;">
    <p style="color:#94a3b8;font-size:12px;margin:0;"><a href="${SITE_URL}" style="color:#60a5fa;">aivideopicks.com</a></p>
  </td></tr>
</table>
</td></tr>
</table>
</body>
</html>`;

  await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${env.RESEND_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      from: FROM_EMAIL,
      to: [email],
      reply_to: REPLY_TO,
      subject: 'Welcome to AI Video Picks — here\'s your first win',
      html,
    }),
  });
}

// ── Contact form (unchanged) ───────────────────────────────────────────────
async function handleContact(request, env) {
  let body;
  const contentType = request.headers.get('content-type') || '';

  try {
    if (contentType.includes('application/json')) {
      body = await request.json();
    } else if (contentType.includes('form')) {
      const formData = await request.formData();
      body = Object.fromEntries(formData);
    } else {
      return jsonResponse({ error: 'Invalid content type' }, 400);
    }
  } catch (err) {
    return jsonResponse({ error: 'Could not parse request body' }, 400);
  }

  const honeypot = (body.website || '').trim();
  if (honeypot) {
    return jsonResponse({ success: true, message: 'Thanks!' });
  }

  const name = (body.name || '').trim();
  const email = (body.email || '').trim().toLowerCase();
  const subject = (body.subject || 'general').trim().slice(0, 100);
  const message = (body.message || '').trim();

  if (!name || name.length < 1 || name.length > 100) {
    return jsonResponse({ error: 'Name is required (1-100 chars)' }, 400);
  }
  if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) || email.length > 254) {
    return jsonResponse({ error: 'A valid email is required' }, 400);
  }
  if (!message || message.length < 10 || message.length > 5000) {
    return jsonResponse({ error: 'Message must be 10-5000 characters' }, 400);
  }

  const lowerMsg = message.toLowerCase();
  const spamHits = ['<a href=', 'http://', 'https://'].filter(s => lowerMsg.includes(s)).length;
  if (spamHits >= 3) {
    return jsonResponse({ success: true, message: 'Thanks!' });
  }

  const esc = (s) => s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');

  const userIp = request.headers.get('cf-connecting-ip') || 'unknown';
  const userAgent = request.headers.get('user-agent') || 'unknown';
  const country = request.headers.get('cf-ipcountry') || 'unknown';

  const html = `<!DOCTYPE html><html><body style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;line-height:1.6;color:#1a1a2e;max-width:640px;margin:0 auto;padding:24px;">
<h2 style="color:#155DFC;margin:0 0 16px;">New contact form submission</h2>
<table cellpadding="6" cellspacing="0" style="border-collapse:collapse;width:100%;font-size:14px;">
  <tr><td style="background:#f8f9fa;width:120px;font-weight:600;">Name</td><td>${esc(name)}</td></tr>
  <tr><td style="background:#f8f9fa;font-weight:600;">Email</td><td><a href="mailto:${esc(email)}">${esc(email)}</a></td></tr>
  <tr><td style="background:#f8f9fa;font-weight:600;">Subject</td><td>${esc(subject)}</td></tr>
  <tr><td style="background:#f8f9fa;font-weight:600;">IP / country</td><td>${esc(userIp)} / ${esc(country)}</td></tr>
</table>
<h3 style="margin:24px 0 8px;">Message</h3>
<div style="background:#f8f9fa;padding:16px;border-left:3px solid #155DFC;white-space:pre-wrap;">${esc(message)}</div>
<p style="font-size:11px;color:#999;margin-top:24px;">User-Agent: ${esc(userAgent)}</p>
</body></html>`;

  const textBody = `New contact form submission\n\nName: ${name}\nEmail: ${email}\nSubject: ${subject}\nIP/Country: ${userIp} / ${country}\n\nMessage:\n${message}\n\nUser-Agent: ${userAgent}`;

  try {
    const res = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${env.RESEND_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: CONTACT_FROM,
        to: [CONTACT_INBOX],
        reply_to: email,
        subject: `[contact] ${subject} — ${name}`,
        html,
        text: textBody,
      }),
    });

    if (!res.ok) {
      const errData = await res.json().catch(() => ({}));
      console.error('Resend contact email error:', errData);
      return jsonResponse({ error: 'Could not send message, please email contact@aivideopicks.com directly' }, 500);
    }

    return jsonResponse({ success: true, message: 'Thanks — we got your message and will reply within a few business days.' });
  } catch (err) {
    console.error('Contact handler error:', err);
    return jsonResponse({ error: 'Something went wrong, please try again' }, 500);
  }
}

function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json', ...CORS_HEADERS },
  });
}
