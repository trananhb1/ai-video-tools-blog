# AI Video Picks Case-Study Plan — Narrative AI Video Editor

**Status:** PLAN — access, source rights, output rights, credentials and spend gates apply  
**Candidate classification:** Weak fit pending testing  
**Evidence confidence:** C  
**Business question:** Can Narrative turn one rights-cleared 24-second AIVP Revlon Plus 2.0 product-video master and its source clips into a conversion-ready 21-second 9:16 cut in under 10 minutes, at zero incremental cost, while keeping the exact product distinctive throughout the first 10 seconds in all three runs?

## 1. Case-study thesis

Narrative is useful to AIVP only if conversational editing reduces revision time without weakening exact-product identity or replacing source footage with generic/generated visuals.

## 2. Locked real-product brief

- **Audience:** Australian creators and SMB affiliate publishers.
- **Input:** the existing unpublished Revlon Plus 2.0 24-second master and original A1/A2/A3 source clips, only after the current asset-rights record is re-confirmed; freeze all SHA-256 hashes.
- **Prompt:** “Make a 21-second vertical conversion cut. Keep the pain-point hook first, show the exact black/red Revlon styling brush in every shot through second 10, preserve the verified narration wording, remove dead air, retain the product-intro and feature order, use source footage only, add no new B-roll or performance claims, and leave the final CTA card editable.”
- **Output:** H.264/AAC MP4, 1080×1920, source frame rate, no watermark.
- **Control:** current deterministic FFmpeg/NLE 21-second edit from the same frozen source assets and narration.
- **Hard product gate:** exact black/red brush, barrel/handle silhouette and controls remain distinctive in the first frame and every sampled frame through second 10; AI-edited illustrative footage is not physical performance proof.

## 3. Three bounded runs

1. Baseline with default/Balanced mode and the locked brief.
2. Best documented mode for long/hard briefs, with the same assets and words.
3. Repeat the accepted mode and identical brief to measure edit-decision drift.

For each run record account/tier, model mode, source hashes, exact prompt, operation log, version IDs, start/end and queue/render time, displayed/consumed credits, export settings, errors/retries, output SHA-256 and QC decision. Save all failures.

## 4. Pass/fail criteria

**PASS only if all three runs:** export valid 1080×1920 H.264/AAC without watermark; finish from upload-ready project to export in ≤10 minutes; incur US$0 and no paid-credit consumption; preserve exact narration claims/order; use only supplied footage; keep the exact product visible and distinctive throughout seconds 0–10; contain no malformed captions or unsupported claims; and remain commercially publishable under written vendor terms.

**FAIL:** any substituted/generated generic product footage, wrong colourway/shape/controls, product absent in any sampled frame during seconds 0–10, narration or claim corruption, duration outside 20–22 seconds, invalid/watermarked export, any failed run, >10 minutes, non-zero unapproved cost, or unresolved monetized-output rights.

**STOP immediately:** trial requires a card; any payment or subscription acceptance appears; free credits are insufficient for all three bounded runs; password/2FA/identity/signature is required; source rights are not current; terms or processors changed materially; or the vendor cannot explicitly confirm monetized editorial/affiliate output rights.

## 5. Evidence package

- frozen source assets, script and supplier-rights record;
- account/tier, terms/privacy snapshots and vendor rights confirmation;
- exact prompts, model modes, operation/version logs and export settings;
- screenshots before every credit-consuming action;
- three outputs including failures and SHA-256 hashes;
- seconds 0/2/5/8/10 plus midpoint/final contact sheets with product-identity QC;
- narration ASR comparison, mediainfo/ffprobe validation, timing/retry/credit log;
- deterministic-control output and measured delta;
- before/after strength scorecard.

## 6. Vendor automation handoff

Treat Narrative as browser-only until a documented API exists. Use an isolated browser profile and CDP port, disable/avoid auto-confirm spending, verify the expected account fail-closed, inspect network egress and upload retention, and verify displayed credits before each run. Do not build MCP automation until one controlled zero-cost run passes security, rights and export checks.

## 7. Publishable outputs if passed

Create an evidence-led case-study review, a conversational-editor comparison module and a behind-the-scenes Short. Disclose complimentary access and AI-assisted editing. Add no affiliate CTA unless a programme is accepted and tracking is live.

## 8. Decision

`RETEST` — obtain bounded review access and explicit commercial-output terms, then run the three locked source-footage edits.
