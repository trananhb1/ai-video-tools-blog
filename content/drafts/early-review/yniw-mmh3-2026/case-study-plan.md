# AI Video Picks Case-Study Plan — yniw/mmh3

**Status:** PLAN — reference support, security, rights, hardware and spend gates apply  
**Candidate classification:** Monitor only  
**Evidence confidence:** C  
**Business question:** Once `mmh3` implements reference conditioning, can it produce three repeatable 5.2-second 9:16 synchronized product clips that preserve one exact rights-cleared LED mask, in under 120 seconds per clip on an approved zero-cost Blackwell route?

## 1. Case-study thesis

The dedicated runtime matters to AIVP only if its simpler native-output workflow preserves a specific product as reliably as the current Google Flow reference route. Fast generic T2VA output is insufficient.

## 2. Locked real-product brief

- **Audience:** Australian creators and SMB product marketers.
- **Input:** AIVP’s LED face-mask reference set, only after the asset-rights record is re-confirmed; freeze image hashes across runs.
- **Prompt:** “Vertical close product demonstration of the referenced LED face mask on one person in a neutral bathroom; preserve shell shape, eye and mouth cut-outs, straps, controller and colourway; LEDs glow red; natural room sound; no text or added accessories.”
- **Output:** 5.2 seconds, closest supported 9:16 resolution at 24fps, H.264/AAC MP4.
- **Control:** identical source and prompt through Google Flow Veo 3.1 Fast References/Ingredients, with deterministic labels added only in post.
- **Hard product gate:** exact mask is distinctive in the first frame and throughout; generated footage is illustrative, not physical performance proof.

## 3. Three bounded runs

1. Default documented reference-conditioned settings and seed 41.
2. Best documented production settings and seed 42.
3. Repeat run 2 with seed 42 to test deterministic reproducibility.

For each run save the source/settings hashes, git commit, model and weight hashes, hardware/driver, commands, start/end/render time, energy or provider cost, complete MP4, decode report, errors and QC decision.

## 4. Pass/fail criteria

**PASS only if all three runs:** preserve the exact mask geometry/colour/controller; show it in the first second and every sampled frame; deliver valid synchronized MP4 at a vertical resolution of at least 768×1344; complete in ≤120 seconds each; incur US$0/no paid credits; and satisfy the model’s attribution, AI-disclosure and monetized-publication terms.

**FAIL:** generic or altered mask, missing product in the first 10 seconds, audio/video desynchronization, invalid media, any run over 120 seconds, any failed run, non-zero unapproved cost or rights ambiguity.

**STOP immediately:** reference conditioning still absent; repository security audit fails; model scan is incomplete; hardware/provider requests payment; disk headroom would fall below the approved safety margin; password/2FA/identity/payment/signature is required; or input/output rights are unclear.

## 5. Evidence package

- frozen source assets and rights record;
- source commit, dependency lock and security-audit report;
- model/license snapshots and all weight hashes;
- exact commands/settings and hardware telemetry;
- three full outputs including failures and SHA-256 hashes;
- first/middle/final-frame contact sheets plus product-geometry QC;
- decode, synchronization, timing, retry and cost logs;
- before/after strength scorecard and control delta.

## 6. Vendor automation handoff

Before any run, audit the Rust/CUDA repository, dependency lock, download script, network egress, file paths and native encoders. Keep downloads and outputs sandboxed; there is no browser profile or credit auto-confirm path. Do not deploy an HTTP/MCP wrapper until one controlled run passes.

## 7. Publishable outputs if passed

Create an evidence-led case study, an open-source local-video runtime comparison module and a behind-the-scenes Short. Include AI-generated illustrative-demonstration disclosure. Add no affiliate CTA unless a programme is accepted and tracking is live.

## 8. Decision

`RETEST` — wait for reference conditioning and a no-cost compatible Blackwell route, then audit before generation.
