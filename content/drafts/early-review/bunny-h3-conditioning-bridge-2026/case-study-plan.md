# AI Video Picks Case-Study Plan — BUNNY H3 Conditioning Bridge V1

**Status:** PLAN — HARDWARE/SECURITY/RIGHTS/COST BLOCKED on current host  
**Candidate classification:** Monitor only  
**Evidence confidence:** C  
**Business question:** Can BUNNY H3 reduce hand-to-controller and action-state errors in an exact LED-mask product shot across three paired runs without degrading product identity or adding more than 10% render time?[1][3][5]

## 1. Locked brief

Use one rights-cleared 9:16 front/three-quarter reference image of LED face mask ASIN B0D2XTZN8V and one fixed prompt: “Eight-second vertical close-up. A creator wears the exact white LED mask and holds its wired controller in the right hand. The right thumb presses the single mode button once; LEDs transition from red to blue while the controller remains in the same hand and the cable stays attached. Preserve shell outline, eye and mouth cut-outs, LED layout, controller, cable and colourway. Slow camera push, dark neutral background, no generated text, no medical or performance claim.”

Freeze H3 checkpoint/component hashes, ComfyUI and node versions, 9:16 dimensions, eight-second duration, sampler, steps, guidance, reference image, prompt and paired seeds `4101`, `4102`, `4103`. For each seed, render native H3 with Bridge OFF and then Bridge ON at `alpha=0.10`, `magnitude_match=per_token`; clear caches between outputs.[1][3][4]

## 2. Three bounded paired runs

1. Seed 4101: Bridge OFF control, then Bridge ON.
2. Seed 4102: Bridge OFF control, then Bridge ON.
3. Seed 4103: Bridge OFF control, then Bridge ON.

Record source/settings/model/workflow hashes, full dependency and source audit, GPU/driver/CUDA/ComfyUI versions, start/end and render durations, peak VRAM, displayed/consumed credits or electricity estimate, errors/retries and output SHA-256 for all six outputs.

## 3. Pass/fail criteria

**PASS all three pairs:** valid 9:16 eight-second MP4s; exact mask visible in frame one and distinctive throughout; shell, cut-outs, LEDs, controller and cable remain specific; controller stays in the right hand; one button press causes one red-to-blue state change; Bridge ON has fewer observable ownership/state errors than OFF in at least two of three pairs; no Bridge-ON pair is worse; median Bridge overhead ≤10%; no retries; external charge US$0.

**FAIL:** generic product substitution; mask absent in frame one; identity drift; hand/controller swap; detached or reassigned cable; unexplained LED-state change; new regression in any Bridge-ON output; invalid output; crash/retry; or median overhead above 10%.

**STOP immediately:** any paid compute/credit prompt, purchase/subscription, unsupported reference workflow, GPU or RAM shortfall, unresolved model/package scan, dependency audit failure, password/2FA/payment/signature step, unclear source-image rights, or unresolved commercial/territorial terms.

## 4. Evidence package

Save source and licence snapshots, candidate adapter and node hashes, dependency/security audit, rights-cleared input, all six outputs including failures, per-second contact sheets, frame-one and first-10-seconds product QC, action-role/state-transition QC, timing/VRAM/error/cost logs and updated scorecard.

## 5. Publishable outputs and boundary

If it passes: evidence-led case study, local H3 workflow module and a behind-the-scenes Short with an “AI-generated illustrative demonstration” disclosure. Do not imply physical product testing or performance proof. No affiliate CTA unless a programme is accepted and tracking is verified. Access does not grant editorial control or guarantee positive coverage.

`RETEST` — execute only after audited no-cost compatible NVIDIA access, documented reference-mode compatibility and rights/package compliance; do not buy compute or consume unapproved credits.

## Sources

[1] https://huggingface.co/JOKER141/BUNNY_H3_Conditioning_Bridge — BUNNY H3 Conditioning Bridge model card
[3] https://github.com/aa335615543-ux/BUNNY_H3_Conditioning_Bridge — BUNNY H3 Conditioning Bridge repository
[4] https://raw.githubusercontent.com/aa335615543-ux/BUNNY_H3_Conditioning_Bridge/main/nodes.py — BUNNY H3 Conditioning Bridge node source
[5] https://huggingface.co/MiniMaxAI/MiniMax-H3 — Official MiniMax H3 model card
