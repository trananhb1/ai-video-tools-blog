# AI Video Picks Case-Study Plan — changwangss Wan2.2 SVDQuant

**Status:** PLAN — HARDWARE/COST BLOCKED  
**Business question:** Can this quantized Wan2.2 T2V-A14B package create three usable five-second 720p b-roll shots for an AIVP AI-video pricing explainer with lower peak memory than upstream BF16 and no material quality loss?[3][4]

## Locked brief

Prompt: “Cinematic close-up of a solo creator comparing AI video subscription plans on a clean studio monitor, slow lateral camera move, realistic hands, neutral office lighting, no readable brand names, no logos, no generated text.” Freeze seed 42, 1280×720, 81 frames, scheduler, guidance, software/model revisions and hardware. Control: upstream BF16 on the same approved environment.

## Three bounded runs

Run the identical brief three times. Save all outputs including failures, hashes, settings, timing, peak VRAM, retries and cost.

## Pass/fail and stop conditions

PASS only if all three decode, contain coherent hands/screens/camera motion, require no corrective edit, complete without retry and show a material memory reduction without visible quality loss versus BF16. FAIL for malformed anatomy, unreadable distracting pseudo-text, temporal breakage, crash/retry or no meaningful memory benefit. STOP for any charge, paid compute prompt, credential/2FA/payment/signature requirement, unclear rights or failed code audit.

This is a narrative test only. The artifact must not be recommended for exact-product affiliate clips because it has no reference-image path.

## Evidence package

Licence snapshot; model/environment/settings/input hashes; three outputs and BF16 control; frame QC; timing/VRAM/error/cost logs; post-test scorecard.

## Sources

[3] https://huggingface.co/changwangss/wan22-svdquant-signround-nosmooth — Wan2.2 SVDQuant artifact
[4] https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B-Diffusers — Wan2.2 T2V A14B base model
