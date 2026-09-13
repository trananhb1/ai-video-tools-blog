# Research Dossier: Vercel AI Gateway MiniMax H3 Promotion

**Assessed:** 2026-09-13  
**Evidence:** Official documents only; no AIVP hands-on run  
**Decision:** QUALIFIED / CONDITIONAL FIRST LOOK

## Verification and search strategy

The deterministic delta contained no new underlying launch: it removed a previously excluded Kling promotional reissue and changed an already processed OpenArt publisher label. Because the GitHub source failed, fallback searches covered GitHub, Product Hunt, launch news and official vendor pages. They surfaced this previously unrecorded Vercel event.

Vercel announced on August 30 that MiniMax H3 and H3 Max requests through AI Gateway were 50% off through September 13, 2026.[1] This is a late discovery, not a launch within 72 hours. H3 supports text, start-image, first/last-frame and multi-reference image/video/audio input at 2K; H3 Max accepts text or a starting image at 480p/768p.[1][2][3]

Vercel documents a browser playground and AI SDK access. It says unpaid users receive US$5 of credits every 30 days, while generation is billed at API rates.[2][3] This host had no Vercel CLI session, `AI_GATEWAY_API_KEY`, or `VERCEL_TOKEN`, so no generation was attempted.

## Gate 1

| Criterion | Score | Basis |
|---|---:|---|
| AI-video relevance | 3/3 | Direct reference-conditioned video generation.[1][2] |
| Differentiation | 2/3 | Useful gateway/API route; underlying H3 predates the promotion.[1] |
| Launch recency | 0/2 | Announced August 30; discovered September 13.[1] |
| AU accessibility | 2/2 | Public web/API and no-payment credits documented; AU billing untested.[2][3] |
| **Total** | **7/10** | CONDITIONAL; nominal free-credit access exists but authentication is absent. |

**Contract score: 11** — hands-on access +3, product references +2, AU fit +2, primary source +2, likely reader impact +2. This clears the contract threshold of 8.

## Gate 2

- **Verified floor:** 45/100
- **Potential ceiling:** 100/100
- **Evidence coverage:** 45%
- **Confidence:** C
- **Classification:** Weak fit pending testing

Exact-product preservation, accepted-output cost, repeatability and visual quality are untested. Vercel permits outputs to be deployed, copied, shared, published or downloaded, but third-party provider terms apply and Vercel requires users to determine commercial usability themselves.[4] Monetized-use rights therefore remain unresolved.

## Gate 3

A three-run exact-product test is planned with the real B0D2XTZN8V LED mask. It is limited to the documented no-payment US$5 allowance and stops before any charge.

## Gate 4 and affiliate

No published press, partnership or affiliate email was found on official Vercel contact/press surfaces. Forms are prohibited, so outreach is **HELD_NO_VERIFIED_CONTACT**. Vercel has affiliate terms, but acceptance is discretionary and payout requires an account, payment method and tax documentation.[5] No application was submitted and no affiliate CTA is permitted.

## Coverage gaps

- GitHub monitor returned `HTTPError`; fallback search does not establish complete coverage.
- Product Hunt remained empty; fallback search found no dated candidate.
- MiniMax terms extraction was incomplete; commercial rights remain unresolved.
- Global cutoff stays preserved.

## Editorial decision

Stage a docs-only First Look but do not publish: the promotion expires today and product fidelity and rights are untested. Next action: authenticate only through a Tom-controlled session, then use no-payment credits for the locked test; abort at any payment prompt.

## Sources

[1] https://vercel.com/changelog/minimax-h3-and-h3-max-are-50-off-on-ai-gateway — MiniMax H3 and H3 Max are 50% off on AI Gateway
[2] https://vercel.com/ai-gateway/models/minimax-h3 — MiniMax H3 API, Pricing & Playground
[3] https://vercel.com/ai-gateway/models/minimax-h3-max — MiniMax H3 Max API, Pricing & Playground
[4] https://vercel.com/legal/ai-product-terms — Vercel AI Product Terms
[5] https://vercel.com/legal/affiliate-marketing-terms — Vercel Affiliate Marketing Terms
