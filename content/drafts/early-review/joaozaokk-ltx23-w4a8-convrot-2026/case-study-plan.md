# AI Video Picks Case-Study Plan — JoaoZaokk LTX-2.3 22B Distilled 1.1 W4A8 ConvRot

**Status:** PLAN — HARDWARE/SECURITY/COST BLOCKED on current host  
**Candidate classification:** Weak fit  
**Evidence confidence:** C  
**Business question:** On an approved no-cost 24GB+ NVIDIA environment, can this W4A8 checkpoint animate the exact LED face mask ASIN B0D2XTZN8V as a 9:16 ten-second audio-video product shot three times without identity drift, with sampling at or below 40 seconds and no external charge?[1][4]

## 1. Locked brief

Use one rights-cleared 512×896 front/three-quarter reference image and one fixed prompt: “Static white LED face mask worn front-facing; red LEDs transition to blue; preserve exact shell outline, eye and mouth cut-outs, controller and cable; subtle slow camera push; plain dark background; synchronized neutral room tone only; no generated text; no medical or performance claim.”

Freeze 249 frames, 25 fps, eight steps, CFG 1.0, Euler, manual sigmas `1.0, 0.99375, 0.9875, 0.98125, 0.975, 0.909375, 0.725, 0.421875, 0.0`, seed 1234, conditioning method, ComfyUI workflow, checkpoint/component hashes and environment. Use the same fixed prompt conditioning in every arm. Control: the publisher-cited 6-bit Q6_K transformer with identical non-transformer components and settings.[1]

The 40-second sampler ceiling allows for the 1.75× pixel-count increase from the publisher's 512×512 W4A8 run while remaining bounded; it is not a vendor claim.

## 2. Three bounded runs

1. W4A8 baseline with the locked product reference and settings.
2. Identical W4A8 repeat after clearing model/output caches.
3. Identical W4A8 repeat after clearing model/output caches.

Record input/settings hashes, model/component hashes, security-scan state, GPU/driver/CUDA/ComfyUI/comfy-kitchen versions, conditioning identity-control result, start/end/sampler/whole-run times, peak VRAM, errors/retries, electricity or compute charge if exposed, and output SHA-256.

## 3. Pass/fail criteria

**PASS all three:** valid 512×896 MP4; 249 frames at 25 fps; non-silent synchronized audio; mask visible in frame one and distinctive throughout the first 10 seconds; shell, cut-outs, controller/cable and LED layout remain specific; no generic substitution; no retry; each sampling loop ≤40 seconds; checkpoint remains within its documented 15.51 GiB file size; no material product-identity loss against Q6_K; external charge US$0.

**FAIL:** any identity drift, geometry mutation, generic replacement, missing/desynchronized audio, invalid output, crash/retry, sampler over 40 seconds, or material identity loss against Q6_K.

**STOP immediately:** any paid compute/credit prompt, purchase or subscription; insufficient GPU/RAM/storage; unresolved checkpoint security scan; dependency audit failure; password/2FA/payment/signature step; unclear source-image rights; or changed licence terms.

## 4. Evidence package

Save source and licence snapshots, file and workflow hashes, dependency/security audit, rights-cleared input, live-versus-saved conditioning identity control, all three W4A8 outputs including failures, Q6_K control, per-second contact sheets, first-10-seconds identity QC, audio/synchrony QC, timing/VRAM/error/cost logs and updated scorecard.

## 5. Publishable outputs and boundary

If it passes: evidence-led case study, local audio-video model comparison module and behind-the-scenes Short. Label generated footage as an AI-generated illustrative demonstration; do not present it as physical product testing. No affiliate CTA unless a programme is accepted and tracking is verified. Access does not grant editorial control or guarantee positive coverage.

`RETEST` — recheck security scans first; execute only after a no-cost compatible NVIDIA environment and rights-cleared source asset are documented.

## Sources

[1] https://huggingface.co/JoaoZaokk/LTX-2.3-22B-distilled-1.1-W4A8-ConvRot — JoaoZaokk LTX-2.3 22B distilled 1.1 W4A8 ConvRot model card
[4] https://huggingface.co/Lightricks/LTX-2.3 — Official Lightricks LTX-2.3 model card
