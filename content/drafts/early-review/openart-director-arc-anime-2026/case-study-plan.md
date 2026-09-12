# AI Video Picks Case-Study Plan — OpenArt Director

**Status:** PLAN — cost, access, rights and authentication gates apply
**Candidate classification:** Promising/conditional (55/100 verified, confidence C)
**Business question:** Can OpenArt Director turn one rights-cleared LED-mask hero image into three usable 30-second vertical affiliate-video drafts that preserve exact product identity in the first 10 seconds, at no more than US$2 per usable output?

## 1. Case-study thesis

Anime benchmark leadership is relevant to narrative coherence but does not prove affiliate-product specificity. Director is useful to AIVP only if it preserves the exact linked product, produces a usable vertical draft consistently, and stays within the revenue model's hard cost ceiling.

## 2. Locked AIVP brief

- **Product:** Amazon B0D2XTZN8V LED face mask; use only AIVP/manufacturer rights-cleared source assets.
- **Format:** 30 seconds, 9:16, H.264 MP4, 1080×1920 if available, English narration.
- **Audience:** Australian skincare buyers and creators.
- **Message:** “A $49.99 at-home LED mask with red and blue light modes”; do not make medical efficacy claims.
- **Visual gate:** exact mask shape, openings, controller, colourway and LED pattern visible and recognizable throughout the first 10 seconds.
- **Control:** existing Dreamina/reference-image workflow using the same source, script and output specification.
- **Prompt:** `Create a 30-second vertical product demonstration using the supplied LED-mask image as the locked product reference. Show the exact mask in the opening frame and continuously through the first 10 seconds. Begin with red LEDs, transition to blue LEDs, show the controller once, use a friendly Australian-creator tone, no medical claims, no redesign, no substitute product, no invented branding, and end with a neutral learn-more frame.`

## 3. Three bounded runs

Freeze Director version/date, account tier, source hashes, prompt, aspect ratio, duration, language, model choices, storyboard and all settings.

1. Run 1 — baseline.
2. Run 2 — identical repeatability run.
3. Run 3 — identical repeatability run.

Record setup time, generation/render time, retries, displayed predicted debit, actual debit, total cost, output path and SHA-256 for every result including failures.

## 4. Success criteria

- 3/3 completed exports.
- Exact product recognizable in frame one and continuously through second 10.
- 9:16 export; narration intelligible; no unsafe or unsupported claim.
- No material product deformation, logo invention, extra controller or substitute mask.
- Median brief-to-export at most 8 minutes.
- Cost at most US$2 per usable output and at most US$6 total.
- Usable without external re-editing.
- Written confirmation that the exact account tier/output may be monetized on YouTube and affiliate pages.

## 5. Failure and stop conditions

**Fail:** fewer than 3 usable exports, any first-10-seconds identity failure, median over 8 minutes, cost above US$2 per usable output, or required external reconstruction.

**Stop immediately:** any predicted or actual debit would exceed free vendor-granted credits or US$6 total; subscription/purchase prompt; paid-credit use; password, 2FA, identity, payment or signature requirement; unclear source rights; unsupported medical claim; or unapproved terms prompt.

Physion's US$21.30 benchmark cost is directional and already exceeds the AIVP threshold. Do not begin without enough complimentary bounded credits and a confirmed rate card.[2]

## 6. Evidence package

Rights record and source hashes; account/tier and terms snapshots; tool/model/build; complete settings; storyboard; before/after credit balances; all three MP4s; screenshots; first/mid/final and 0–10-second QC frames; timings; costs; failure logs; SHA-256 hashes; control outputs; score delta; commercial-rights confirmation; disclosure record.

## 7. Integration gate

If the test is funded entirely by complimentary credits and passes, audit the official OAuth MCP/CLI, isolate credentials, require account match, disable automatic spend, and cap every generation before considering production integration.[6]

## 8. Outcome

`HELD_COST_ACCESS_AUTH` — plan complete; no run executed and no performance claim approved.
