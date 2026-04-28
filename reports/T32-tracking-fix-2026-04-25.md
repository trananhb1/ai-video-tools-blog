# T32 — Tracking Instrumentation Fix

**Owner**: content-writer (dev) | **Date**: 2026-04-25 | **Status**: complete (working tree dirty)

## Why

T20 found two bugs poisoning every CTA decision: (1) `affiliate_click` fired on every outbound link (YouTube, CapCut, citations) — ~2x inflation; (2) 123 direct vendor URLs bypassed `/go/*`, untracked. T22 was blocked until both were fixed.

## Part A — Click handler rewrite

`assets/js/analytics.js` (v2). `affiliate_click` now fires **only** on `/go/...` or `https://aivideopicks.com/go/...` clicks. Other off-site clicks fire a separate `outbound_click` event so we keep visibility without polluting affiliate metrics. Both events carry `link_url` (full destination href). `affiliate_click` retains `affiliate_partner` (slug) + `affiliate_url`; `outbound_click` carries `link_domain` (hostname). Both carry `link_text` and `page_path`.

## Part B — 123 direct vendor URLs replaced with `/go/*`

All four target redirects already exist and return 200 on production (smoke-tested via `curl -I`). Counts:

| Vendor | URLs | Files |
|---|---|---|
| HeyGen | 48 | 13 |
| Synthesia | 41 | 9 |
| Zebracat | 25 | 9 |
| Submagic | 9 | 7 |

24 unique post files touched (de-duped — many had multiple vendors): `what-is-text-to-video-ai`, `invideo-review-2026`, `d-id-vs-elai-vs-hourone`, `heygen-review-2026`, `ai-video-deals-coupons-2026`, `ai-video-for-ecommerce`, `heygen-vs-synthesia-vs-pictory`, `murf-ai-review-2026`, `best-ai-video-tools-beginners-2026`, `ai-training-onboarding-videos`, `heygen-vs-synthesia-2026`, `best-ai-talking-head-tools-2026`, `ai-video-pricing-compared-2026`, `ai-video-social-media-marketing-2026`, `synthesia-review-2026`, `zebracat-review-2026`, `kling-vs-veo-vs-runway`, `best-ai-video-tools-2026`, `veed-vs-kapwing-vs-descript`, `turn-long-videos-into-shorts-ai`, `submagic-review-2026`, `opus-clip-review-2026`, `ai-tools-youtube-creators-2026`, plus `best-free-ai-video-generators-2026` (Part C below).

Per-vendor `replace_all` per-file via Edit (not a sweeping sed). `rel="nofollow sponsored"` and `target="_blank"` preserved on every anchor — only `href` changed. Citation links to vendor docs/research/blog (e.g. `heygen.com/research/...`, `heygen.com/blog/...`) left as-is — they are non-affiliate and now correctly fire as `outbound_click`.

## Part C — Spike landing page upgrade callout

`posts/best-free-ai-video-generators-2026.html`:

- One-line above-fold callout immediately under Quick Answer: *"Need more than the free tier? HeyGen's $24/mo Creator plan removes the watermark, lifts the 5-minute limit, and unlocks all 175+ avatars — the cheapest paid upgrade path if your free clip isn't ready for clients yet. Try HeyGen ->"* routed through `/go/heygen/`. Voice matches house style: second-person, specific numbers, no hype verbs.
- Quick Answer **untouched** per T20 guidance (preserves the citation integrity that earned the traffic).
- Body marker added: "Updated April 25, 2026" in hero meta.
- JSON-LD `dateModified`: `2026-04-11` -> `2026-04-25`.
- No structural rewrite — that's T23's scope.

## Part D — Smoke test

- `analytics.js` syntax validated via `new Function(code)`.
- Click-handler exercised against 6 simulated clicks in a Node harness:
  - `/go/heygen/` -> `affiliate_click`, partner=heygen, link_url=/go/heygen/ ✓
  - `https://aivideopicks.com/go/synthesia/` -> `affiliate_click`, partner=synthesia ✓
  - YouTube embed -> `outbound_click`, link_domain=youtube.com (NOT affiliate_click) ✓
  - `heygen.com/research/...` citation -> `outbound_click`, NOT affiliate_click (the bug fix) ✓
  - Internal `/posts/...` link -> no event ✓
  - `mailto:` -> no event ✓
- HTML well-formedness check on all 24 edited post files: zero unbalanced tags, zero unclosed elements.
- `/go/{heygen,synthesia,zebracat,submagic}/` all return 200 on production.

## Anomalies

- **T20 said "13 posts"** — that figure was HeyGen-only. Adding Synthesia/Zebracat/Submagic the unique-file count is 24. All 123 URLs across all 24 files replaced.
- **`heygen-alternatives-2026.html` line 233** has a non-affiliate citation to HeyGen's Avatar V benchmark page (no `?via=`). Left as-is — it's a research citation, not an affiliate CTA. Now fires `outbound_click` under v2.
- **`heygen-avatar-v-guide-2026.html`** has three `heygen.com/{blog,research}/...` URLs — also citations, left untouched.
- **Hero page `best-ai-video-tools-2026.html`** had two direct Zebracat affiliate URLs replaced. Hero URL, JSON-LD `@id`, and structure unchanged.
- **Legacy slug audit** (`via=tuan-tran|tom26|d98eb9|fbca94`): zero matches sitewide. Already cleaned in the 2026-04-19 standardization.

## Open questions for the human

1. **Register `link_url` as a GA4 custom dimension** on property 530029168. Until registered, the value sits in raw event data unindexed and won't appear in standard reports. Analytics-analyst flagged at T20 they need owner/editor access. Either grant access, or register manually (`link_url`, `link_domain` event-scoped; `affiliate_partner` already exists).
2. **Re-pull baseline on 2026-05-02** so T22 has 7+ days of clean post-fix data to compare against the broken baseline.

## Working tree

26 modified files (1 JS + 24 posts + this report). Not committed — left for human review/commit per task brief. After deploy (~1-2 min on GitHub Pages), the new tracker is live and the next 7 days will reflect corrected event firing.
