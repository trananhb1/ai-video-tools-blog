# AI Video Picks Case-Study Plan — JoaoZaokk LTX-2.5 22B Distilled W4A8 ConvRot

**Status:** PLAN — HARDWARE/SECURITY/COST BLOCKED on current host  
**Candidate classification:** Weak fit  
**Evidence confidence:** C  
**Business question:** On an approved no-cost 24GB NVIDIA environment, can this W4A8 transformer animate the exact LED face mask ASIN B0D2XTZN8V in a 9:16 ten-second product shot three times without identity drift, while using no more than 12 GiB transformer storage and materially less render time than BF16?[1][4]

## 1. Locked brief

Use one rights-cleared 512×896 front/three-quarter reference image and one fixed prompt: “Static white LED face mask worn front-facing; red LEDs transition to blue; preserve exact shell outline, eye and mouth cut-outs, controller and cable; subtle slow camera push; plain dark background; no generated text; no medical claim.”

Freeze 249 frames, 25 fps, three steps, CFG 1.0, Euler, manual sigmas `0.909375, 0.725, 0.421875, 0.0`, seed 1234, ComfyUI workflow, model/component hashes and environment. Control: the same source, prompt and settings with Lightricks' official INT8 transformer; run BF16 only if it fits the no-cost approved environment without offload changing the comparison.[1][4]

## 2. Three bounded runs

1. W4A8 baseline with the publisher-documented settings and the locked product reference.
2. Identical W4A8 repeat with the same seed and settings after cache clearing.
3. Identical W4A8 repeat with the same seed and settings after cache clearing.

Record input/settings hashes, all model/component hashes, security-scan state, GPU/driver/CUDA/ComfyUI/comfy-kitchen versions, start/end/render time, peak VRAM, errors/retries, electricity or compute charge if exposed, and output SHA-256.

## 3. Pass/fail criteria

**PASS all three:** valid 512×896 MP4 with synchronized audio or an explicitly documented silent-output limitation; 249 frames at 25 fps; mask visible in frame one and distinctive through the full clip; shell, cut-outs, controller/cable and LED layout remain specific; no generic substitution; no retry; each W4A8 render ≤481.5 seconds; transformer resident within 12 GiB; no material product-identity loss against official INT8; external charge US$0.

**FAIL:** any identity drift, geometry mutation, generic replacement, invalid output, crash/retry, render over 481.5 seconds, transformer footprint over 12 GiB, or material fidelity loss against INT8.

**STOP immediately:** any paid compute/credit prompt, required purchase or subscription, GPU under 24GB, insufficient storage, unresolved model security scan, dependency audit failure, password/2FA/payment/signature step, unclear source-image rights, or changed licence terms.

## 4. Evidence package

Save source and licence snapshots, model and workflow hashes, dependency/security audit, rights-cleared input, all three W4A8 outputs including failures, official-INT8 control, BF16 control if feasible, per-second contact sheets, first-10-seconds identity QC, audio QC, timing/VRAM/error/cost logs and updated scorecard.

## 5. Publishable outputs and boundary

If it passes: evidence-led case study, local-video-model comparison module and a behind-the-scenes Short. No affiliate CTA unless a programme is accepted and tracking is verified. Access does not grant editorial control or guarantee positive coverage.

`RETEST` — execute only after no-cost compatible NVIDIA access and security review are documented; do not buy compute or download the 12.5GB checkpoint on this host.

## Sources

[1] https://huggingface.co/JoaoZaokk/LTX-2.5-22B-distilled-W4A8-ConvRot — JoaoZaokk LTX-2.5 22B distilled W4A8 ConvRot model card
[4] https://huggingface.co/Lightricks/LTX-2.5 — Official Lightricks LTX-2.5 model card
