# AI Video Picks Case-Study Plan — Yoroll Superfast Video hosted preview

**Status:** PLAN — no completed generation; public preview is non-commercial evaluation only
**Confidence:** C
**Business question:** Can the hosted Superfast preview produce three repeatable, editorially usable five-second audio-video clips for an AI Video Picks narrative first-look workflow without queue failure or material seed drift?

## Use case and hard gate

This is a narrative B-roll test, not a product-affiliate test. The live surface accepts text, duration and seed but no image/product reference, so it cannot qualify for exact-ASIN recommendation or the first-10-seconds product-identity gate.

## Locked brief

Create a five-second 16:9 establishing shot for an AIVP explainer: “A clean creator desk at sunrise, laptop showing an abstract video timeline with no readable brands or text, camera slowly pushes in, soft room tone, realistic cinematic lighting.” Use duration 5 seconds and seed 260921 for every run. Do not upload third-party media, names, logos, faces, prices or factual product claims.

## Three bounded runs

1. Submit the locked prompt, duration and seed; record queue and render timing.
2. Repeat without changing any input; preserve every output including failure.
3. Repeat once more; stop after the third submission.

## Success criteria

- All three jobs return downloadable playable video with audio.
- At least two outputs are editorially usable without repair.
- No brands, readable fabricated text, faces or unsafe content appear.
- Same-seed composition remains recognisably consistent across all completed runs.
- Median submit-to-download time is at most five minutes.
- No payment, account, paid credit or terms-acceptance step appears.

## Failure and stop criteria

Stop on any payment prompt, paid-credit debit, login/2FA, identity/payment request, private-endpoint bypass, unclear consent, or third-party-rights issue. Fail the test if fewer than two runs complete, audio is absent from two or more outputs, median elapsed time exceeds five minutes, or outputs are not downloadable.

## Evidence package

Save the normalized prompt and SHA-256, interface/config screenshot, exact settings, submit/queue/render timestamps, all three videos including failures, video SHA-256 values, codec/resolution/fps/audio metadata, first/middle/final frame QC, and a run table. Label outputs vendor-hosted free-evaluation evidence and do not publish or monetize them without written permission.

## Outcome

`NOT_RUN`. Browser-capable execution was unavailable after the mandated Antigravity worker returned quota exhaustion. Retry through the public UI only; do not call the private Gradio generation function directly.
