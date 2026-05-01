/**
 * AI Video Picks — Newsletter Signup Worker (Cloudflare Workers)
 *
 * Handles POST /subscribe from static site forms.
 * Adds contact to Resend Audience, triggers welcome email.
 *
 * Environment variables (set in wrangler.toml or dashboard):
 *   RESEND_API_KEY  — Resend API key
 *   AUDIENCE_ID     — Resend audience ID
 */

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': 'https://aivideopicks.com',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

const FROM_EMAIL = 'Tom from AI Video Picks <newsletter@aivideopicks.com>';
const REPLY_TO = 'trananhb1@gmail.com';
const SITE_URL = 'https://aivideopicks.com';

export default {
  async fetch(request, env) {
    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: CORS_HEADERS });
    }

    if (request.method !== 'POST') {
      return jsonResponse({ error: 'Method not allowed' }, 405);
    }

    const url = new URL(request.url);

    if (url.pathname === '/subscribe') {
      return handleSubscribe(request, env);
    }

    return jsonResponse({ error: 'Not found' }, 404);
  },
};

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
    <h1 style="color:#ffffff;font-size:22px;font-weight:800;margin:0;">AI Video <span style="color:#60a5fa;">Hub</span></h1>
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

function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json', ...CORS_HEADERS },
  });
}
