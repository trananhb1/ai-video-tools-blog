# Research Dossier: Video Rebirth BACH 1.0 Pro

**Status:** QUALIFIED — First Look only; no AIVP hands-on run  
**Event date:** 2026-09-16  
**Discovery date:** 2026-09-16  
**Gate 1 materiality score:** 8/10  
**Confidence:** C (leaderboard benchmark + official docs + press release; no AIVP-run artifacts)

---

## Signal source

Monitor diff, 2026-09-16T12:48:02Z: TipRanks article "Video Rebirth Advances AI Video Model to Top-Three Leaderboard Position" triggered the change detection.

Primary source: Video Rebirth LinkedIn post (company official), confirmed via TipRanks article citing that post directly.

---

## Search strategy

1. Searched: "Video Rebirth BACH new model 2026 September top-three AI video leaderboard"
2. Fetched: https://crafiq.ai/models/video/video-rebirth-bach-1-0-preview (leaderboard data)
3. Fetched: https://ponpon.ai/blog/bach-ai-video-engine-multi-shot-films (independent analysis, May 2026)
4. Fetched: https://www.bach.art (product page, live)
5. Fetched: https://www.bach.art/docs (API documentation)
6. Fetched: https://www.videorebirth.com/press (official press hub — press contact confirmed)
7. Fetched: https://www.prnewswire.com/news-releases/video-rebirth-launches-bach--... (official PR)
8. Fetched: https://tipranks.com/news/article/video-rebirth-advances-ai-video-model-to-top-three-leaderboard-position (trigger article)

---

## Event summary

Video Rebirth (Singapore AI startup, $80M AMD-backed, founded by Dr. Wei Liu, ex-Tencent Distinguished Scientist and IEEE/AAAS Fellow) announced via LinkedIn on 2026-09-16 that their **BACH 1.0 Pro** model has advanced to **#3 on the Artificial Analysis Image-to-Video leaderboard**, up from #6 debut position (Preview, April 5 2026) and #5 (Preview, ~May 2026).

The advancement is attributed to post-training via **Recursive Self-Improvement** — the model generates videos, evaluates them against an internal quality standard, and uses successful outputs as additional training data.

BACH 1.0 Pro is expected to **go live end of September 2026** (not yet released as of this dossier). Current product at bach.art is BACH 1.0 Preview/existing build.

---

## Verified capability claims (from official docs and press releases)

- **Multi-shot Montage:** Generates multi-shot films up to 30 seconds from reference images + text prompt. Automatic shot planning and transitions.
- **Character consistency:** "Locked Character" — same character held across every shot with directable micro-expressions. Physics-Native Attention (PNA) architecture.
- **Cinematic camera language:** Whip pans, rack focus, Rembrandt lighting — physically modelled, not filters. Dual Diffusion Transformer (DDiT) architecture.
- **Native 1080p output at 30fps** (not interpolated, not upscaled — claim unverified by AIVP)
- **Audio in workflow:** SFX, voiceover, BGM generated in same workflow (claimed)
- **API available:** REST API documented at bach.art/docs. Endpoints: text2video, image2video, montage2video, element2video, text2image.
- **Free sign-up credits:** Complimentary credits for new users upon sign-up (confirmed from PR and product page)
- **Enterprise pilots:** Major global e-commerce platform, film studios, advertising agencies, game studios (unverified by AIVP)

---

## Leaderboard ranking context

| Rank (AA I2V) | Model | Notes |
|---|---|---|
| #1 | Google Gemini Omni Flash | |
| #2 | MiniMax H3 | |
| #3 | **BACH 1.0 Pro** (Video Rebirth) | Announced 2026-09-16, not yet live |
| Previously #5 | Bach-1.0 Preview | April–Sept 2026 |

Source: Artificial Analysis Video Arena (blind human preference Elo scores). Previous leaderboard from crafiq.ai shows Avenger 0.5 Pro (prior Video Rebirth model) at #32; Bach-1.0 Preview was #5 Image-to-Video.

---

## AU creator accessibility

- Product is at bach.art — no geographic restriction observed on product page
- Singapore-based company; global access expected
- Free sign-up credits confirmed
- Pricing page returned 404; specific per-credit/plan costs not verified
- API documentation is public (api-gen-na.bach.art — "na" suggests North America region endpoint)
- Payment method not confirmed for AU creators

---

## Gate 1: Launch materiality scoring

| Criterion | Score | Rationale |
|---|---|---|
| Relevance to AI-video production | 3/3 | Multi-shot video generation, character consistency, 1080p output directly applicable to AIVP affiliate video workflow |
| Differentiation | 3/3 | Top-3 leaderboard; Montage (multi-shot, 30s) is architecturally differentiated from single-clip generators; character lock across shots is rare |
| Launch recency | 1/2 | Leaderboard announcement today (Sept 16); BACH 1.0 Pro not yet live (end-of-September expected). Current product accessible now. |
| Accessibility | 1/2 | Free sign-up credits at bach.art — accessible. Pricing for sustained use unverified; "na" endpoint may indicate AU routing untested. |

**Total: 8/10 → QUALIFIED**

---

## Strength classification summary

**Verified floor: 57/100 | Potential ceiling: 100/100 | Evidence: 57% | Confidence: C**

Classification: **Promising/conditional** — strong leaderboard positioning and differentiated multi-shot architecture, but no AIVP hands-on runs, commercial rights unverified, pricing unknown.

See strength-scorecard.json for full 100-point breakdown.

---

## Planned case study

A narrow three-run test: Use BACH's reference-guided generation to produce a recognizable 30-second product affiliate clip for an LED face mask (Amazon B0D2XTZN8V) and compare output specificity against current AIVP baseline (Google Flow Veo 3.1 Fast). Pass/fail: product distinctive in first 10 seconds.

See case-study-plan.md for full brief.

---

## Outreach record

- Vendor contact: **Fay Wong, pr@videorebirth.com** (confirmed official — published at https://www.videorebirth.com/press and in PR Newswire press release)
- Affiliate program: Not yet found on public site; inquiry included in outreach
- Status: See vendor-outreach-draft.md and outreach-send-result.json (post-send)

---

## Next action

1. Tom approves or auto-approved by standing policy `aivp-qualified-launch-outreach-v1` → send outreach
2. Monitor bach.art for BACH 1.0 Pro live date (expected end of September 2026)
3. On launch: run Gate 4 case study (free sign-up credits)
4. If pass: produce First Look → Review → cross-link to best-ai-video-tools-2026.html, best-ai-image-to-video-generators-2026.html, sora-alternatives-2026.html
