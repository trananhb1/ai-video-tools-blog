# Case Study Plan: Alibaba PAI MiniMax-H3-Fun-Controlnet-Union-2.0

**Status:** PLANNED - no hands-on run; held for rights-cleared footage and no-cost compatible compute
**Confidence before test:** C

## Business question

Can Layout control plus post-normalization inpainting change a product-video background and one masked region while keeping the exact Revlon One-Step Volumiser Plus 2.0 distinctive throughout the first 10 seconds in three repeatable 15-second vertical runs?

## Locked brief

- Product: Revlon One-Step Volumiser Plus 2.0.
- Source: AIVP-captured footage or supplier-approved footage only; written rights record required before generation.
- Input: one fixed 15-second 9:16 control video, fixed layout track, fixed binary mask and fixed prompt.
- Prompt goal: replace the room background with a bright creator studio while preserving the black/red brush, barrel shape, bristles, controls, hand placement and motion.
- Settings: publisher v2 config; 704x1280 pixel budget; 24 fps; 40 steps; guidance scale 1.0; control scale 1.0; seed 43; identical software and weights for all runs.[1]
- Output: H.264 MP4, no added text or performance claim.

## Three bounded runs

Run the locked brief three times in fresh processes with identical assets/settings. Save every output and failure. Record setup time, render time, peak hardware allocation, retries and no-cost credit consumption.

## Success criteria

- Exact product remains visually distinctive at 0s, 3s and 10s in all 3 runs.
- Product geometry, black/red colourway, barrel/bristles and controls do not materially mutate.
- Background and only the masked region change as instructed; kept regions remain stable.
- 3/3 runs finish without timeout and no more than one retry total.
- Output can be used in monetized AIVP content under written terms, with required AI disclosure.
- Total AIVP cash cost is US$0 for this pilot; any paid-credit request triggers STOP and Tom approval.

## Failure and stop conditions

Stop on product-identity failure in run 1, unavailable supplier rights, licence ambiguity for the execution territory, password/2FA/payment/identity request, paid-credit consumption, or no no-cost compatible compute. Do not treat generated visuals as physical performance proof.

## Evidence package

Rights record; source video/layout/mask hashes; exact prompt/config; model and code commit IDs; dated input/output screenshots; all MP4s including failures; SHA-256 hashes; timing and cost ledger; 0s/3s/10s/final-frame QC; licence snapshot; disclosure text; delta against the unedited control.

## Outcome

PENDING. No render, quality score or cost measurement exists yet.

## Sources

[1] https://huggingface.co/alibaba-pai/MiniMax-H3-Fun-Controlnet-Union-2.0 - publisher settings and workflow
[4] https://huggingface.co/alibaba-pai/MiniMax-H3-Fun-Controlnet-Union-2.0/raw/main/LICENSE - execution and output conditions
