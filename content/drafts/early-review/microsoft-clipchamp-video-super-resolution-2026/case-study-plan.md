# AI Video Picks Case-Study Plan — Clipchamp Video Super Resolution

**Status:** PLAN — rights, hardware and zero-cost gates apply
**Candidate classification:** Monitor only pending controlled testing
**Evidence confidence:** C

## Business question

Can Clipchamp Video Super Resolution convert the same rights-cleared 720p vertical affiliate-product clip to usable 1080p three times in five minutes median or less, with zero incremental spend and without altering exact product identity?

## Locked brief

- Input: one AIVP-owned, rights-cleared 720×1280, 8-second H.264 product clip from the current affiliate/demo portfolio. Do not run until the source/input rights record is attached.
- Product gate: exact silhouette, colourway, logo/label placement and visible controls remain distinctive from frame one through eight seconds.
- App/device: record Clipchamp version, Windows build, CPU/NPU/GPU and account tier; freeze these across all runs.
- Operation: import source, select **Upscale → 1080p**, export H.264 MP4 at 1080×1920 with no other edits.
- Control: the original 720p source enlarged to 1080p by the existing deterministic editor workflow.
- Runs: three identical Clipchamp runs; retain failures.

## Success criteria

- 3/3 valid 1080×1920 exports.
- Product remains recognizable throughout; no invented or shifted labels, controls or geometry.
- No new flicker, haloing or temporal instability at first/mid/final-frame QC.
- Median processing time ≤5 minutes and failure rate 0/3.
- Incremental charge/paid-credit use = $0.
- Output may be used in monetized AIVP content under applicable Microsoft/Clipchamp terms.

## Failure and stop conditions

Fail on any product-identity defect, fewer than three valid exports, median over five minutes, or material quality regression versus control. Stop before a purchase/subscription prompt, paid feature, password/2FA/identity/payment/signature step, unsupported hardware workaround, unclear input rights, or unclear monetized-output rights.

## Evidence package

Source-rights record; source and control hashes; device/app/account screenshots; settings; start/end timestamps; three exports including failures; SHA-256 hashes; first/mid/final frames; blind QC notes; cost evidence; terms snapshot; updated scorecard.

## Publishable outputs

If passed: tested section in a relevant Clipchamp/creator-editing article and a short side-by-side demonstration. No affiliate CTA without programme acceptance and tracking verification. If failed: retain evidence and publish only a limitations-led First Look if editorially useful.

## Outcome

`NOT_RUN` — requires compatible Windows 11 hardware and rights-cleared fixture; no paid test is authorized.
