# AI Video Picks Case-Study Plan — LynnReal-Omni

**Status:** PLAN — supplier rights, security, hardware and spend gates apply
**Candidate classification:** Monitor only
**Evidence confidence:** C
**Business question:** Can LynnReal-Omni use one exact rights-cleared product reference to produce three repeatable 8-second 9:16 affiliate clips that preserve product identity while matching or beating Google Flow's approved reference workflow at zero unapproved cost?

## 1. Case-study thesis

LynnReal-Omni matters to AIVP only if its unified reference-and-control workflow preserves a specific product through motion. Broad multimodal feature coverage and publisher speed claims do not answer that business question.[1][8]

## 2. Locked real-product brief

- **Audience:** Australian creators and SMB product marketers.
- **Input:** AIVP's Revlon One-Step Plus 2.0 product reference pack, only after supplier reuse permission and source hashes are recorded.
- **Prompt:** “Vertical close product demonstration of the exact referenced black-and-red oval hot-air brush. A woman lifts it beside dry hair and slowly rotates it once. Preserve oval barrel shape, red accent ring, black handle, control collar, bristle layout and supplied accessories. Neutral bathroom, natural movement, no text, no substituted dryer or round brush.”
- **Output:** 8 seconds, 9:16, at least 720×1280, 24 or 30fps, H.264 MP4.
- **Control:** identical rights-cleared reference and prompt through Google Flow Veo 3.1 Fast Ingredients/References.
- **Hard product gate:** the exact brush is distinctive in the first frame and remains recognizable at every sampled QC frame; footage is illustrative, not performance proof.

## 3. Three bounded runs

1. Standard default documented reference-to-video path, seed 41.
2. Best documented reference/pose control path, seed 42.
3. Exact repeat of run 2 and seed 42 to test determinism.

For every run record source and prompt hashes, repository/model commit, complete settings, hardware, start/end/cold-start/render timing, credit/compute display, retries, output hash, decode report and QC decision.

## 4. Pass/fail criteria

**PASS only if all three runs:** preserve the brush's geometry, colourway, controls and bristles; show it within the first second and throughout sampled frames; return valid vertical MP4; complete in ≤180 seconds per warm run; use no paid credits or unapproved compute; and pass supplier-input and monetized-output rights checks.

**FAIL:** a generic/substituted brush, material geometry or colour drift, product absent in any first-10-seconds QC sample, invalid media, any failed run, any warm run over 180 seconds, or unresolved publication rights.

**STOP immediately:** supplier permission is absent; code/security audit fails; package security scans are incomplete; suitable zero-cost hardware is unavailable; download would breach storage margin; payment/paid credits are requested; credentials/2FA/identity/payment/signature are required; or rights terms change.

## 5. Evidence package

- supplier permission and frozen source assets;
- code/security audit, dependency lock and network-egress map;
- repository/model/weight hashes and licence snapshots;
- exact prompts/settings, hardware and timing logs;
- all three outputs including failures and SHA-256 hashes;
- first/middle/final-frame contact sheets plus product-identity QC;
- cost ledger and score delta against the Google Flow control;
- before/after strength scorecard.

## 6. Vendor automation handoff

Before generation, audit the custom build backend, installer, shell launchers, ComfyUI nodes, model loaders, network egress and output paths. Sandbox all downloads and outputs. Do not build an MCP/API wrapper until one controlled local or hosted run passes.

## 7. Publishable outputs if passed

Create an evidence-led case study, a buyer-guide comparison module and a behind-the-scenes Short. Include AI-generated illustrative-demonstration and complimentary-access disclosures where applicable. Add no affiliate CTA unless a programme is accepted and tracking is verified.

## 8. Decision

`RETEST` — first secure supplier rights and a verified no-cost hosted/H100 route, then complete security audit before generation.

## Sources

[1] https://github.com/LynnReal-AI/LynnReal-Omni — LynnReal-Omni official repository and README
[8] https://github.com/LynnReal-AI/LynnReal-Omni/blob/main/docs/LynnReal-Omni-Paper.pdf — LynnReal-Omni technical report
