# AI Video Picks Case-Study Plan — Alaya-EVOKE-Turbo

**Status:** PLAN — RIGHTS/HARDWARE/STORAGE BLOCKED  
**Candidate classification:** Monitor only  
**Evidence confidence:** C  
**Business question:** If commercial rights and no-cost suitable compute are documented, can EVOKE-Turbo preserve the exact LED face mask identity under a controlled camera move more consistently than base EVOKE across three identical runs?[1][3][5]

## 1. Locked brief

Use one rights-cleared 384 × 640 front/three-quarter product image for LED face mask ASIN B0D2XTZN8V and one fixed camera-pose track. Fixed prompt: “The exact white LED face mask remains centred and unchanged; red LEDs transition to blue; preserve shell outline, eye and mouth cut-outs, controller and cable; slow camera arc; dark neutral room; no text; no medical claims.”

Freeze source image, pose track, prompt, seed 44, model/repository commits, three-step settings, chunk count, depth backend, environment and hardware. Control: base EVOKE with identical inputs/settings where technically compatible.[1][3]

## 2. Three bounded Turbo runs

1. Turbo baseline using the documented i2v/camera-control workflow.
2. Identical Turbo repeat with the same seed and settings.
3. Identical Turbo repeat with the same seed and settings.

Also produce one base-EVOKE control only if it adds no financial cost and uses the same approved environment. Record exact hashes, settings, GPU/driver stack, start/end/render duration, peak VRAM, errors/retries, displayed cost and every output hash.

## 3. Pass/fail criteria

**PASS all three:** valid decodable MP4; exact mask visible from frame one and distinctive throughout the first 10 seconds or entire clip if shorter; shell, openings, controller/cable and LED layout remain recognizable; requested camera path followed; no subject substitution; no retries; Turbo beats or matches the base control on a blinded identity/control checklist; total external charge US$0; monetized-output rights explicitly cleared.

**FAIL:** any generic replacement, identity/geometry drift, uncontrolled camera motion, invalid output, retry, material control regression versus base, or rights ambiguity.

**STOP immediately:** CC BY-NC remains in the required runtime chain; payment or paid-compute prompt; insufficient storage/accelerator capacity; password, 2FA, identity, payment or signature request; failed code/security audit; unclear source-asset rights.

## 4. Evidence package

Save claim/source ledger, licence snapshots for every runtime component, vendor rights clarification, repository/model/dependency hashes, security audit, source asset and rights record, pose track, full settings/environment export, all outputs including failures, per-second contact sheets, identity/control QC, timing/VRAM/error/cost logs and pre/post-test scorecards.

## 5. Publishable outputs and decision

If and only if all rights and quality gates pass: an evidence-led case study, a world-model control comparison module and a behind-the-scenes Short. No affiliate CTA unless a programme is accepted and tracking is verified. Access does not guarantee positive coverage or editorial control.

`RETEST` — do not run until a commercially permitted dependency chain and no-cost compatible accelerator/storage environment are documented.

## Sources

[1] https://huggingface.co/AlayaLab/Evoke-Turbo — AlayaLab Evoke-Turbo model card
[3] https://github.com/AlayaLab/Evoke — Official EVOKE implementation
[5] https://huggingface.co/pkqbajng/ViGeo — ViGeo required depth backend model card
