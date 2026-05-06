/**
 * AI Video Picks — Newsletter + Contact Worker (Cloudflare Workers)
 *
 * Routes:
 *   POST /subscribe        — adds contact to Resend Audience, triggers welcome email
 *   POST /contact          — accepts contact form submissions, forwards to inbox via Resend
 *   GET  /admin/subscribers — lists all subscribers (requires Authorization: Bearer <ADMIN_TOKEN>)
 *   GET  /admin/stats       — subscriber count + recent signups summary
 *
 * Environment variables (set in wrangler.toml or `wrangler secret put`):
 *   RESEND_API_KEY  — Resend API key
 *   AUDIENCE_ID     — Resend audience ID
 *   ADMIN_TOKEN     — Bearer token for admin endpoints
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

export default {
  async fetch(request, env) {
    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: CORS_HEADERS });
    }

    const url = new URL(request.url);

    // Admin routes (bearer-token auth)
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
      if (request.method === 'POST' && url.pathname === '/admin/send') {
        return handleAdminSend(request, env);
      }
      return jsonResponse({ error: 'Not found' }, 404);
    }

    // Public routes (POST only)
    if (request.method !== 'POST') {
      return jsonResponse({ error: 'Method not allowed' }, 405);
    }

    if (url.pathname === '/subscribe') {
      return handleSubscribe(request, env);
    }

    if (url.pathname === '/contact') {
      return handleContact(request, env);
    }

    return jsonResponse({ error: 'Not found' }, 404);
  },
};

function verifyAdmin(request, env) {
  const auth = request.headers.get('Authorization') || '';
  const token = auth.replace(/^Bearer\s+/i, '');
  return token && token === env.ADMIN_TOKEN;
}

async function handleAdminSubscribers(env) {
  try {
    const res = await fetch(
      `https://api.resend.com/audiences/${env.AUDIENCE_ID}/contacts`,
      {
        headers: { Authorization: `Bearer ${env.RESEND_API_KEY}` },
      }
    );
    const data = await res.json();
    if (!res.ok) {
      return jsonResponse({ error: 'Resend API error', details: data }, 502);
    }
    const contacts = (data.data || []).map(c => ({
      email: c.email,
      first_name: c.first_name || '',
      subscribed: !c.unsubscribed,
      created_at: c.created_at,
    }));
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
      {
        headers: { Authorization: `Bearer ${env.RESEND_API_KEY}` },
      }
    );
    const data = await res.json();
    if (!res.ok) {
      return jsonResponse({ error: 'Resend API error', details: data }, 502);
    }
    const contacts = data.data || [];
    const subscribed = contacts.filter(c => !c.unsubscribed);
    const lastWeek = new Date(Date.now() - 7 * 86400000).toISOString();
    const recent = subscribed.filter(c => c.created_at >= lastWeek);
    return jsonResponse({
      total: contacts.length,
      subscribed: subscribed.length,
      unsubscribed: contacts.length - subscribed.length,
      new_last_7_days: recent.length,
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
      if (!contactRes.ok) {
        return jsonResponse({ error: 'Failed to fetch contacts', details: contactData }, 502);
      }
      active = (contactData.data || []).filter(c => !c.unsubscribed);
      if (!active.length) {
        return jsonResponse({ error: 'No active subscribers' }, 400);
      }
    }

    const emails = active.map(c => ({
      from: 'Tom from AI Video Picks <newsletter@aivideopicks.com>',
      to: [c.email],
      reply_to: 'trananhb1@gmail.com',
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

  if (!email || !email.includes('@')) {
    return jsonResponse({ error: 'Valid email required' }, 400);
  }

  try {
    // Add contact to Resend Audience
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

    // Send welcome email (fire-and-forget)
    sendWelcomeEmail(email, firstName, env).catch(console.error);

    return jsonResponse({ success: true, message: 'Subscribed!' });
  } catch (err) {
    console.error('Subscribe error:', err);
    return jsonResponse({ error: 'Something went wrong' }, 500);
  }
}

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

  // Honeypot — bots fill this hidden field, humans don't.
  // Silently accept (200 OK) so bots don't retry, but discard.
  const honeypot = (body.website || '').trim();
  if (honeypot) {
    return jsonResponse({ success: true, message: 'Thanks!' });
  }

  const name = (body.name || '').trim();
  const email = (body.email || '').trim().toLowerCase();
  const subject = (body.subject || 'general').trim().slice(0, 100);
  const message = (body.message || '').trim();

  // Validation
  if (!name || name.length < 1 || name.length > 100) {
    return jsonResponse({ error: 'Name is required (1-100 chars)' }, 400);
  }
  if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) || email.length > 254) {
    return jsonResponse({ error: 'A valid email is required' }, 400);
  }
  if (!message || message.length < 10 || message.length > 5000) {
    return jsonResponse({ error: 'Message must be 10-5000 characters' }, 400);
  }

  // Basic spam guards beyond the honeypot
  const lowerMsg = message.toLowerCase();
  const spamHits = ['<a href=', 'http://', 'https://'].filter(s => lowerMsg.includes(s)).length;
  if (spamHits >= 3) {
    // Looks link-spammy — accept silently to avoid signalling the filter.
    return jsonResponse({ success: true, message: 'Thanks!' });
  }

  // Escape for safe HTML rendering in the email body.
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

  const textBody = `New contact form submission

Name: ${name}
Email: ${email}
Subject: ${subject}
IP/Country: ${userIp} / ${country}

Message:
${message}

User-Agent: ${userAgent}
`;

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
