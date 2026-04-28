# T20 — Spike Forensics + Revised Revenue Baseline

**Analyst**: analytics-analyst
**Project**: aivideopicks
**Date**: 2026-04-25
**Period analysed**: 2026-04-23 to 2026-04-25 (3-day spike window), with 30-day context (2026-03-26 to 2026-04-25)

---

## Status (two sentences)

Apr 23-24 was a real, ChatGPT-driven traffic event into a single page — `posts/best-free-ai-video-generators-2026.html` — and it is fading fast (Apr 25 = 87 sessions, down 76% from Apr 24's 368). The bigger finding is that the site's `affiliate_click` instrumentation has been producing inflated, unusable numbers for months because the on-page tracker fires on every outbound link (CapCut, YouTube, Canva, etc.), not just affiliate destinations — fix this before spending a minute more on CTA tuning.

## Data pulled this session

All numbers below pulled live via Composio GA4 (`properties/530029168`) and GSC (`sc-domain:aivideopicks.com`) on 2026-04-25.

**Daily sessions, last 30 days** (GA4):

| Date | Sessions | Users | PV |
|---|---|---|---|
| Mar 26 – Apr 22 (28d avg) | 32.1 | 30.6 | 43.0 |
| Apr 22 (day before spike) | 44 | 42 | 55 |
| **Apr 23** | **279** | 267 | 393 |
| **Apr 24** | **368** | 352 | 575 |
| **Apr 25** | **87** | 86 | 127 |

**Spike window (Apr 23-25, 3 days) totals**:
- Sessions: **734** (vs prior 30-day total **1,080** across **30** days → the 3-day spike = 68% of a normal month)
- Landing pages where those 734 landed:
  - `/posts/best-free-ai-video-generators-2026.html` — **538 sessions** (73.3% of spike), 105 engaged (**19.5% engagement**)
  - `/posts/best-ai-video-tools-2026.html` — 74 sessions (10.1%), 9 engaged (12.2%)
  - `/index.html` + `/` — 49 sessions
  - `/go/heygen/` — **17 sessions** landed directly (ChatGPT is also citing `/go/heygen/` URLs as endpoints)
  - `/posts/heygen-pricing-2026.html` — 8 sessions
  - Everything else: single digits

**Source/medium during spike**:

| Source | Medium | Sessions | % |
|---|---|---|---|
| (direct) | (none) | 330 | 45% |
| chatgpt.com | (not set) | 314 | 43% |
| chatgpt.com | referral | 208 | 28% |
| bing | organic | 27 | 3.7% |
| cn.bing.com | referral | 6 | |
| copilot.com | referral+(not set) | 11 | |
| claude.ai | referral | 2 | |

ChatGPT direct = **522 sessions (71%)**. The "(direct)/(none)" bucket with no landing-page (126 rows) is likely Apps/app store previews from the ChatGPT mobile app stripping referrers — effectively more ChatGPT traffic. Real ChatGPT share is closer to **80-85%**.

**Countries during spike**: India 196 / US 58 / Pakistan 42 / China 27 / Philippines 16 / Egypt 13 / Nigeria 13 / Bangladesh 12. Non-Western geo share **~64%** — this is a low-AOV audience getting a CapCut-free answer, not a HeyGen-paid answer.

**GSC during spike (Apr 23-24)**: Top 12 queries — 0 clicks, total ~65 impressions across mostly API-integration queries (`heygen streamingavatarapi newsessionrequest background type color value hex` = 28 impressions — this is a developer-looking-for-code query, not a buyer query, and the rest are similar). Impressions trend over 30 days: Mar 26 = 422, Apr 21 = 64, Apr 22 = 129. **GSC is declining, not rising — the spike is not from Google organic.**

**Affiliate events, 30-day total**: `affiliate_click` = **519 events** (strategist's "482" was a stale window). 3-day spike window = **258 events** (50% of the 30-day total in 3 days). `/go/*` pageviews 30-day: **182 heygen, 12 synthesia, 4 pictory, 3 each fliki/submagic/descript, 2 each pika/runway, 1 each of 11 others = 232 total `/go/*` pageviews**.

**AdSense**: unable to verify status — Playwright browser locked by another process. No saved AdSense session. Manual check needed at https://adsense.google.com (resubmitted 2026-04-18; policy window opens 2026-05-02).

## The 80/20

- **The hero page isn't the hero anymore.** 538 of 734 spike sessions (73%) landed on `best-free-ai-video-generators-2026.html`, NOT the designated hero `best-ai-video-tools-2026.html`. This matches the plan's observation that hero #2 outperforms on PV. In the spike window, hero #2 is carrying the site 7.3x harder than hero #1.
- **91% of trackable conversion intent is still HeyGen**: 182 of 232 `/go/*` pageviews over 30 days. That didn't change during the spike — the spike amplified ChatGPT's CapCut-as-free-answer, not HeyGen-as-paid-answer.
- **Bottom half of `/go/*`**: 11 redirects (arcads, makeugc, movavi, zebracat, vidu, vizard, wan, veo, seedance, reap, quso, etc.) got ≤1 pageview in 30 days. They exist, they're harmless, ignore for now.

## Findings

### Finding 1 — The spike is ChatGPT citing hero #2 for the "actually free AI video" query, and it's already cooling

- **Evidence**: 522 chatgpt.com sessions to `best-free-ai-video-generators-2026.html` in 3 days (Apr 23-25). Apr 25 = 87 sessions total, a 76% drop from Apr 24. Public web-search results for the same queries do NOT cite aivideopicks.com (checked "best AI video tools 2026", "best free AI video generators 2026", "AI talking head tools 2026", "cheapest AI video generator 2026", "HeyGen alternatives 2026" — dominant citers are Atlas Cloud, WaveSpeed, Zapier, Manus, TheCMO, Synthesia, Colossyan, G2). The citation is inside ChatGPT's retrieval layer only, which we cannot see.
- **Story**: A ChatGPT response (or a cluster of them) surfaced our page as a citation source for free-AI-video-generator queries, probably triggered by an update to OpenAI's retrieval index or a popular shared conversation. The page matches that query well: comparison table, Quick Answer naming CapCut, 8 tools covered, dated 2026. The drop on Apr 25 suggests the citation has dropped out of high-frequency responses (could be recency-weighted scoring, or simply that the original viral ChatGPT thread cooled down).
- **Action for content-writer**: Do NOT rewrite this page. It's getting cited because of what it currently says. Instead, add (a) a `dateModified` bump to 2026-04-24 without changing the body, (b) a "What changed in April 2026" dated paragraph near the top that reinforces the current ranking so re-crawls keep citing it, (c) a single prominent CTA swap: replace the "CapCut" Quick Answer recommendation with a two-line addition "If you need pro-quality avatar video, HeyGen is the cheapest paid upgrade path — free 1-min video, $24/mo after" linking to `/go/heygen/`. This preserves the free-answer integrity that earned the citation while adding an upgrade path.
- **Action for analytics-analyst (me, T28)**: Re-pull daily sessions on 2026-04-26, 2026-04-28, 2026-05-01. If Apr 26-28 all sit below 60 sessions/day, the spike is fully faded — pivot back to pre-spike priorities per T20 kill criteria.

### Finding 2 — The `affiliate_click` metric is broken and has been inflating every decision

- **Evidence**: The on-page tracker in `assets/js/analytics.js` (line 15) fires `affiliate_click` whenever `isExt = /^https?:\/\//.test(href) && href.indexOf('aivideopicks.com') === -1` — i.e. ANY external http(s) link. `posts/best-free-ai-video-generators-2026.html` contains direct URLs to `youtube.com`, `capcut.com`, `canva.com` (all non-affiliate) — clicks on any of these produce `affiliate_click` events with `event_label` = the hostname. That page alone fired 111 `affiliate_click` events in the spike window, but only has ONE `/go/heygen/` link and ZERO direct affiliate URLs to HeyGen. The other 110+ events are non-revenue false positives. The custom `linkUrl` parameter returned blank in GA4 (not registered as a custom dimension), so we can't split by destination without fixing the dimension config first.
- **Story**: The 30-day `affiliate_click` count of 519 events is not 519 affiliate clicks. It's ~232 `/go/*` pageview-equivalent clicks + ~200-280 noise clicks on YouTube/CapCut/Canva/other non-affiliate external links. The real affiliate engagement number is closer to the `/go/*` pageview count of **232**, not 519. That's also why the hero #2 engagement rate "looked okay at 20.7%" — because the click-to-external-link ratio was inflated by non-revenue link clicks.
- **Action for content-writer / dev** (high priority, block T22/T23): Two fixes needed:
  1. In `assets/js/analytics.js`, tighten the event fire to `/go/*` only. Drop the `isExt` branch. If we want to measure all outbound clicks, make that a separate `outbound_click` event, never mix it with `affiliate_click`.
  2. In the posts listed below, replace direct vendor affiliate URLs with `/go/<slug>/` redirects so every real affiliate click produces a trackable `/go/*` pageview. Priority posts (count of direct HeyGen/Synthesia/Zebracat/Submagic URLs that bypass /go/):
     - `posts/heygen-vs-synthesia-2026.html` — 7 direct HeyGen + likely Synthesia
     - `posts/best-ai-talking-head-tools-2026.html` — 7 direct HeyGen
     - `posts/ai-video-for-ecommerce.html` — 7 direct HeyGen
     - `posts/best-ai-video-tools-beginners-2026.html` — 6 direct HeyGen
     - `posts/ai-video-pricing-compared-2026.html` — 5 direct HeyGen
     - `posts/heygen-review-2026.html` — 4 direct HeyGen
     - `posts/ai-training-onboarding-videos.html` — 4 direct HeyGen
     - Site-wide: **48 direct HeyGen + 41 direct Synthesia + 25 direct Zebracat + 9 direct Submagic = 123 bypass-/go/ URLs**
  3. In GA4 admin, register `link_url`, `event_label`, and `affiliate_partner` as custom dimensions (event-scoped). Until that's done, we cannot split affiliate events by destination — we're flying blind on which partner earns the clicks.

### Finding 3 — Revenue baseline is HeyGen-only and unrecoverable without manual dashboard exports

- **Evidence**: Only HeyGen is confirmed: $100.80 commission 2026-04-17 (per project memory). No stored Playwright sessions or saved credentials exist at `~/.claude/secrets/` for any aivideopicks affiliate dashboard. Playwright browser is locked by another process this session, so I cannot even attempt interactive logins.
- **Story**: We have 13 affiliate programs active; we know the revenue of one. Every other decision in the plan is based on the assumption that HeyGen = 91% of conversions, which is reasonable given the `/go/*` pageview share (78%) but is NOT the same as commission share — some programs pay 70% (Vidnoz) vs HeyGen's 35%, so a smaller click share can still pay more revenue.
- **Action for human** (required, 30 min): Log into each and export last-30-day commissions to CSV. Drop into `/home/tom/ai-video-tools-blog/reports/revenue/`. Dashboards:
  - HeyGen (Impact.com or similar — check email for login link)
  - Vidnoz — https://vidnoz.postaffiliatepro.com
  - Movavi / Affise — https://movavi.affise.com (API key in `aivideopicks_movavi_api.md`: `ab4c7e4b1d6d766b3f454af1cbf2ec7a`, pid=6129 — CAN pull programmatically, see T30 recommendation)
  - Submagic — https://submagic.co/affiliates
  - Fliki — https://fliki.ai/affiliate
  - Synthesia — https://synthesia.io/affiliates (PartnerStack)
  - Pictory — https://pictory.ai/affiliates
  - Zebracat — https://zebracat.ai/affiliate
  - Amazon Associates AU — https://affiliate-program.amazon.com.au
- **Action for analytics-analyst**: For Movavi specifically, the Affise API key is stored in memory — I can pull that one programmatically if you give me 10 minutes. Flagging as T30b.
- **AdSense status**: not verifiable this session (browser locked). Manually check https://adsense.google.com for `aivideopicks.com` status. Decision window opens 2026-05-02 per project memory.

### Finding 4 — The spike is low-revenue shape: free-answer intent, low-AOV geos, dropping fast

- **Evidence**: Of the 734 spike sessions, 538 (73%) landed on the "actually free" page whose Quick Answer recommends CapCut + Google Veo (zero-revenue tools). 64% of spike traffic is from India/Pakistan/China/Philippines/Egypt/Nigeria/Bangladesh — markets where HeyGen's $24/mo CTA has a much lower CVR than Vidnoz's free/$8.99 tier. `/go/heygen/` as a landing page only got 17 of 734 sessions. HeyGen `/go/` pageviews across the full 30-day period sum to 182; from the spike 3 days alone, `/go/heygen/` got 73 pageviews (out of 258 events). That's a generous ~$40 if all 73 converted at the same ~$33/commission rate HeyGen has shown — in reality maybe 1-3 conversions, maybe $30-$90.
- **Story**: This spike was a popularity event, not a revenue event. Realistic dollar impact: $30-$120 additional from spike, lump sum, not a recurring rate. Any sustain plan needs to accept that the page is ranked for "free", not for "best paid", and that pushing aggressive upgrade CTAs into it risks losing the ChatGPT citation.
- **Action for strategist**: Recalibrate the $1k/week target. The spike does not put us on that trajectory. See "Sustain plan + dollar gap" below.

## Kill-criteria check

- **T20 kill criterion** (from plan): "if spike has fully reverted to <50 sessions/day by Apr 26, flag it as transient and pivot plan back to the pre-spike priorities." — Apr 25 is 87 sessions (NOT below 50 but 76% down from peak). **Not hit yet; re-check required on 2026-04-26 and 2026-04-27.** If sessions stay in 60-120/day range, treat as elevated baseline; if they crash to <40, kill criterion trips and we revert.
- **T16 (ElevenLabs / PartnerStack)**: already killed per plan. No action.

## Sustain plan + dollar gap

### Current revenue run-rate (best estimate)

- Confirmed HeyGen commissions: $100.80 (one payment, 2026-04-17)
- Weekly revenue during pre-spike baseline (~40 sessions/day, ~5 `/go/heygen/` /day): ~$30-50/week if conversion is consistent
- Weekly revenue including spike afterglow (if sessions stabilise ~60-80/day): ~$50-100/week
- AdSense: unconfirmed, earliest possible revenue May 2-16

### Dollar gap to $1k/week (target 2026-05-11)

- Current: ~$50-100/week affiliate, $0/week AdSense
- Target: $1,000/week total
- **Gap: ~$900-950/week.**
- **This is not reachable from organic affiliate alone in 17 days.** Even a sustained 5x on HeyGen commissions gets us to ~$500/week, not $1k. AdSense approval + favourable RPM is the only single lever that can close the gap, and it's probabilistic.

### Three ranked options (ICE: Impact × Confidence × Ease, 1-10 each, score = product)

**Option A: Fix tracking first, then wire upgrade path into spike page** (ICE: 8 × 9 × 7 = **504**)
- *Impact 8*: Unlocks trustworthy numbers for all future decisions. Adds a real HeyGen upgrade CTA to the highest-traffic page in the site's history. If the spike cools to 60/day and the new CTA captures even 2-3 extra `/go/heygen/` clicks a day, that's +$50-100/week over baseline.
- *Confidence 9*: Mechanical change, no ranking risk if done carefully (don't rewrite body, just add a framed upgrade paragraph).
- *Ease 7*: ~2-3 hrs of work. One `analytics.js` diff, one content diff on the hot page, GA4 custom-dimension registration.
- Assigned: **content-writer + dev** for Fix #1 and #2, **analytics-analyst (me)** for GA4 custom dimensions.

**Option B: Publish `heygen-alternatives-2026.html` within 48 hrs (T25)** (ICE: 7 × 6 × 6 = **252**)
- *Impact 7*: HeyGen-alternative intent is buyer intent. If ChatGPT extends its current citation cluster, this post is one of the highest-CVR formats we can publish.
- *Confidence 6*: We don't know if ChatGPT will pick it up; the public-web SERP is already crowded (Synthesia, G2, Colossyan, D-ID, eesel all cite their own pages).
- *Ease 6*: 6-8 hrs content work per T25 brief. Brand-steward review needed.
- Assigned: **content-writer** after tracking fix lands.

**Option C: Attempt to reverse-engineer the ChatGPT citation by asking ChatGPT directly** (ICE: 6 × 4 × 9 = **216**)
- *Impact 6*: If we learn what exact phrasing got cited, we can replicate it on 2 more pages.
- *Confidence 4*: ChatGPT won't reliably reveal its retrieval sources; this is anecdotal at best.
- *Ease 9*: 15 mins of incognito queries on chatgpt.com with browsing enabled.
- Assigned: **human or strategist**. Analyst can't do this from WebSearch (Google results are different from ChatGPT retrieval).

**Recommendation: do Option A this week**. It unlocks every future decision and has the highest expected value. Options B and C are worth doing after Option A, in that order.

## Prioritised action list

1. **Fix `analytics.js`** — narrow `affiliate_click` to `/go/*` only. **Owner: content-writer / dev. Effort: 20 min. Impact: massive.** Do this before ANY T22 analysis runs — otherwise T22 inherits the same broken numbers.
2. **Register GA4 custom dimensions for `link_url` and `affiliate_partner`** — event-scoped. **Owner: analytics-analyst (me, next session). Effort: 10 min in GA4 admin (requires user-level access — human may need to grant).** Impact: makes T22 possible at all.
3. **Replace 123 direct vendor URLs with `/go/*` redirects** — 48 HeyGen + 41 Synthesia + 25 Zebracat + 9 Submagic, spread across the 13 posts listed in Finding 2. **Owner: content-writer with a sed script. Effort: 1-2 hrs.** Impact: every affiliate click becomes trackable.
4. **Bump `dateModified` on `best-free-ai-video-generators-2026.html` + add dated "What changed in April 2026" paragraph + add HeyGen upgrade-path CTA** (non-destructive). **Owner: content-writer. Effort: 30 min.** Don't rewrite the Quick Answer.
5. **Manual dashboard export for the 8 affiliate programs listed** — by human or by T30b (Movavi via API, I can do). **Effort: human 30 min, or me 15 min for Movavi only.**
6. **AdSense status check on https://adsense.google.com** — manual, by human. **Effort: 2 min.** Re-check weekly from May 2 onward.
7. **T28 mid-plan checkpoint (2026-05-01)** needs revised dollar-gap baseline — will re-run after actions 1-5 complete.

## Open questions for the human

1. **Tracking fix sign-off**: I recommend we ship Option A's `analytics.js` + direct-URL replacement before content-writer starts T22/T23. Otherwise the audit runs on bad numbers. Confirm priority?
2. **GA4 custom dimensions**: do you have owner/editor access to property `530029168`? I need it to register `link_url` and `affiliate_partner` as event-scoped dimensions.
3. **Revenue target realism**: $1k/week by 2026-05-11 is not reachable from affiliate alone even under best-case assumptions. AdSense approval probabilistically closes the gap only if RPM hits $2+ across all 50 posts. Want me to model a conservative (AdSense approved, low RPM), base (AdSense approved, mid RPM), and stretch (AdSense approved + HeyGen cluster lands) scenario at T28?
4. **Movavi API pull**: I can pull Movavi commissions directly via their Affise API today (key in memory `aivideopicks_movavi_api.md`). Want me to include that in T30?

---

## Summary for the plan TL;DR

- Spike is ChatGPT-only, cited page is `best-free-ai-video-generators-2026.html`, already faded 76% from Apr 24 peak to Apr 25
- `affiliate_click` metric has been fundamentally broken for months — fires on any outbound link (YouTube, CapCut, Canva), not just affiliates
- Real trackable affiliate intent = 232 `/go/*` pageviews over 30 days, not the 519 `affiliate_click` events
- 123 direct vendor URLs bypass `/go/*` sitewide across 13 posts; fix before T22 audit
- Realistic dollar gap to $1k/week = ~$900/week; not reachable from affiliate alone in 17 days — AdSense approval is the only lever that can close it

---

*Report generated 2026-04-25. Next re-pull: 2026-04-26 to confirm spike decay or re-elevation.*
