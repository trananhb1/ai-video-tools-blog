# AI Video Picks Case-Study Plan — xt111 MiniMax H3 NVFP4

**Status:** PLAN — HARDWARE/RIGHTS BLOCKED  
**Business question:** Can the 12.5GB ref2va NVFP4 build preserve the exact LED face mask ASIN B0D2XTZN8V across three 9:16 clips on a 32GB-or-better Blackwell GPU without materially worse identity or motion than the upstream int8 control?[1][2]

## Locked brief

Use one rights-cleared front/three-quarter product reference and a fixed structured H3 prompt: “White LED face mask, exact shell outline, eye and mouth cut-outs, controller and cable preserved; red LEDs transition to blue; subtle push-in; dark background; no text; no medical claim.” Freeze source hash, seed, 864×480 vertical-equivalent settings, 39 frames, 20 steps, scheduler, software/model revisions and hardware. Control: upstream pruned int8_convrot with identical inputs where feasible.

## Three bounded runs

Run the same ref2va input three times with identical settings. Save all outputs including failures, exact settings, model/input hashes, timing, peak VRAM, retries and cost.

## Pass/fail and stop conditions

PASS only if all three files decode, the product is distinctive in frame one and throughout, shell/cut-outs/controller/cable remain specific, no generic substitution occurs, no retries occur, and no material product-identity or motion loss appears against control. STOP for any charge, paid compute prompt, password/2FA/payment/signature step, unclear rights, failed security audit, or first product-identity failure.

## Evidence package

Rights record; licence snapshot; environment and dependency lock; settings JSON; input/output SHA-256; three MP4s; control; frame-one/mid/final QC; timing/VRAM/error/cost logs; post-test scorecard.

No affiliate CTA unless acceptance and tracking are verified. Access does not guarantee coverage, a positive verdict or ranking.

## Sources

[1] https://huggingface.co/xt111/MiniMax-H3-NVFP4 — MiniMax H3 NVFP4 model card
[2] https://huggingface.co/MiniMaxAI/MiniMax-H3 — MiniMax H3 base model
