# Case Study Plan: Vercel AI Gateway MiniMax H3

## Business question

Can MiniMax H3 preserve exact Amazon product B0D2XTZN8V identity in three repeatable 9:16 clips while total spend stays within the no-payment US$5 Vercel allowance?

## Locked brief

- **Product:** LED face mask, ASIN B0D2XTZN8V.
- **Source:** One rights-cleared clean AIVP product image; copy rights provenance into evidence before upload.
- **Model/mode:** `minimax/minimax-h3`, reference-to-video, same image every run.
- **Prompt:** `Vertical product hero shot. Preserve the exact mask shape, eye openings, straps, surface details, and red/blue LED pattern from Image 1. A creator lifts the same mask toward camera, then wears it as the LEDs alternate red and blue. Clean skincare studio, realistic hands, no added logos, no text, no redesign.`
- **Output:** MP4, 9:16, 8 seconds, 2K; no generated typography.

## Control

Google Flow: Video → Ingredients/References to Video → Veo 3.1 Fast → 9:16 → 8 seconds, same product ingredient and continuity block. Do not consume new paid Google credits for this intake test.

## Three bounded runs

Freeze model, prompt, reference, duration, ratio and resolution. Record seeds if available.

| Run | Status | Elapsed | Cost | SHA-256 | QC |
|---|---|---:|---:|---|---|
| 1 | Pending authentication | - | - | - | - |
| 2 | Pending | - | - | - | - |
| 3 | Pending | - | - | - | - |

## Success criteria

- Exact product visible and distinctive within 2 seconds and for at least 6/8 seconds in all runs.
- Shape, eye openings, straps and red/blue LED identity survive in first/mid/final frames.
- No substituted product, malformed face/hand, extra logo, generated text or medical claim.
- Native 9:16 MP4 at documented resolution.
- Three of three runs complete without retry and each within 10 minutes.
- Total debit at most US$5 with no payment method.
- Usable with deterministic captions/CTA only; no visual repair.
- Terms or vendor confirmation permit monetized YouTube and affiliate use.

## Stop conditions

- Two product-identity failures → stop.
- Any payment prompt, card requirement, subscription or debit beyond free credits → stop before generation.
- Projected total above US$5, two provider errors or one unexplained debit → stop.
- Password, 2FA, identity, payment or signature required → pause for Tom.
- Unclear monetized rights → outputs stay internal.

## Evidence package

Source-rights record and hash; account check without credentials; full request/response JSON; credit screenshots; task IDs and timing; all MP4s and hashes; first/mid/final frames; QC notes; rights excerpts; Google Flow comparison.

## Outcome

**NOT TESTED / AUTH BLOCKED.** No Vercel session or API token is present. Proceed only with authenticated no-payment access and fail closed at any charge.
