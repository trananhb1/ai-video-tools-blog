# AI Video Picks Case-Study Plan — Yi30 Wan2.2 W4A8 SVDQuant NVIDIA Artifacts

**Status:** PLAN — HARDWARE/COST BLOCKED on current host  
**Candidate classification:** Monitor only  
**Evidence confidence:** C  
**Business question:** On an approved no-cost NVIDIA environment, can the quantized Wan2.2 TI2V-5B artifact animate the exact LED face mask ASIN B0D2XTZN8V in a 41-frame vertical shot three times without product-identity drift, while reducing memory versus the BF16 control?[1][2]

## 1. Locked brief

Use one rights-cleared 480×832 front/three-quarter product reference image and one fixed prompt: “Static white LED face mask worn front-facing; red LEDs transition to blue; preserve the exact shell outline, eye and mouth cut-outs, controller and cable; subtle camera push; plain dark background; no text and no medical claim.”

Freeze seed 42, 41 frames, 20 inference steps, scheduler, guidance, software revisions and hardware. Control: the same source, prompt, seed and settings through upstream BF16 Wan2.2 TI2V-5B where the approved environment can run both.[1][2]

## 2. Three bounded runs

1. Quantized baseline with the repository's documented 5B settings.
2. Identical quantized repeat with the same seed/settings.
3. Identical quantized repeat with the same seed/settings.

Record exact repository/model hashes, input hash and rights record, environment/container hash, GPU/driver/CUDA versions, settings JSON, start/end/render time, peak VRAM, energy/compute cost if exposed, errors/retries and output SHA-256.

## 3. Pass/fail criteria

**PASS all three:** valid MP4; mask is visible in frame one and recognizable throughout; shell, cut-outs, controller/cable and LED layout remain specific; no generic substitution; all outputs decode; no retries; peak VRAM ≤27GB; quantized-vs-BF16 visual QC has no material product-identity loss; total external charge US$0.

**FAIL:** any identity drift or generic substitute, geometry mutation, invalid output, crash/retry, peak VRAM >27GB, or material quality loss against BF16.

**STOP immediately:** any paid compute or credit prompt, required purchase/subscription, insufficient storage, GPU below the documented memory envelope, password/2FA/payment/signature step, unclear input rights, or an environment/code audit failure.

## 4. Evidence package

Save source and licence snapshots, commits/model hashes, audit notes, source assets and rights record, settings/environment exports, all three outputs including failures, BF16 control output, per-second frame contact sheets, timing/VRAM/error/cost logs, output hashes and the post-test scorecard.

## 5. Publishable outputs and boundary

If it passes: evidence-led case study, an open-model workflow comparison module and a behind-the-scenes Short. No affiliate CTA unless a programme is accepted and tracking is verified. Access does not grant the publisher editorial control or guarantee positive coverage.

`RETEST` — run only after no-cost compatible NVIDIA access and security review are documented; do not purchase compute or download the full artifact set on this host.

## Sources

[1] https://huggingface.co/Yi30/wan2.2-ti2v-w4a8-svd-nvidia — Wan2.2 W4A8 SVDQuant NVIDIA artifacts
[2] https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers — Wan2.2 TI2V 5B Diffusers base model
