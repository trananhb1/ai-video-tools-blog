# AI Video Picks Case-Study Plan — T8star VDN-MiniMax-H3 ComfyUI

**Status:** PLAN — HARDWARE/STORAGE/RIGHTS BLOCKED on current host
**Candidate classification:** Weak fit
**Evidence confidence:** C
**Business question:** On compliant Australian-hosted hardware, can the T8star Ref2VA workflow preserve LED face mask ASIN B0D2XTZN8V through a five-second product shot with synchronized audio, under 10 minutes and zero per-render vendor cost, in three identical runs?[1][2][3]

## Locked brief

Use rights-cleared front/three-quarter/product-controller images. Generate 832×480 or the highest documented 16GB-safe setting, 24fps, five seconds, with the mask visible from frame one, red-to-blue LED transition, static shell geometry and no medical claim. Use the same seed/settings for all runs where supported. Control: saved Dreamina reference-image shot.

## Three bounded runs

1. Default pruned Ref2VA workflow.
2. Best documented multi-reference workflow.
3. Exact repeat of run 2 for drift/reliability.

Record pinned commits/model hashes, input hashes, settings/workflow JSON, hardware/driver, start/end/render time, VRAM, energy estimate if available, all outputs/hashes, retries and QC.

## Pass/fail/stop

**PASS all three:** exact shell, cut-outs, controller and LED layout remain recognizable from frame one through five seconds; valid H.264/AAC; no geometry substitution; ≤10 minutes/render; zero per-render vendor charge; license/distribution plan approved.

**FAIL:** identity drift, generic substitute, invalid media, >10 minutes, any crash, or territory requirement incompatible with intended distribution.

**STOP:** any paid compute/credit requirement, less than 100GB free storage, no suitable NVIDIA GPU, password/2FA/payment/signature step, unclear source rights, or legal review says global publication would violate territorial output restrictions.[1][3][4]

## Evidence package and decision

Save source/license snapshots, exact model/workflow revisions, hardware evidence, pre/post storage, inputs, all outputs/failures, frame QC at every second, timing/VRAM/error logs, hashes and post-test scorecard.

`RETEST` — move only to compliant no-cost Australian GPU infrastructure; do not attempt the 82–83GB download on this 74GB/no-NVIDIA host.

## Sources

[1] https://huggingface.co/t8star/Vdn-Minimax-H3-Comfy — T8star OpenVDN MiniMax H3 ComfyUI bundle
[2] https://github.com/T8mars/comfyui-minimax-h3-audio-T8 — MiniMax H3 Audio T8 ComfyUI node
[3] https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE — MiniMax H3 Community License
[4] https://huggingface.co/OpenVDN/vdn-minimax-h3 — OpenVDN VDN-MiniMax-H3
