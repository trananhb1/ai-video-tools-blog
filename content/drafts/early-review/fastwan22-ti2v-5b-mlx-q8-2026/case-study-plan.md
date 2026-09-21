# Case Study Plan: FastWan2.2 TI2V 5B MLX Q8

## Business Question

Can this 8-bit-encoder MLX package generate three consistent, exact-product 5-second vertical affiliate clips on accessible Apple Silicon while keeping peak unified memory at or below 20 GB and total render time at or below 6 minutes per clip?

## Use Case

Create a short illustrative clip for the Revlon One-Step hair-styling brush using only rights-cleared AIVP reference assets. This tests local Apple-Silicon feasibility and product identity; it does not claim physical product performance.

## Prerequisites / Stop Before Spend

- Publicly auditable compatible runtime or a minimal locally audited loader.
- Rights-cleared source image and written asset provenance.
- Apple Silicon host with at least 32 GB unified memory.
- Apache/upstream/output-rights review complete.
- No paid cloud compute or paid credits without Tom's approval.

## Locked Brief

Create a 5-second 9:16 illustrative product clip at the highest supported vertical resolution near the documented 832x480 pixel budget. The same Revlon One-Step reference image, prompt, negative prompt, seed, three-step schedule and decoder settings must be used for all runs. Keep the black-and-red brush recognizable from frame 1 through the final frame. Add no generated text, price or performance claim.

Continuity prompt: "Vertical studio product shot of the same black and red oval hair-styling brush from the supplied reference, held naturally in one hand, slow controlled half-turn, clean warm bathroom background, realistic lighting, product shape and colour unchanged, no logo mutation, no extra controls, no text."

## Success Criteria

- Three of three runs export playable MP4 files.
- Exact black/red oval-brush identity is visually distinctive in the first frame and remains recognizable throughout.
- No material extra controls, duplicated parts, hand fusion or identity drift.
- Each render completes in <= 360 seconds on the same 32 GB Apple-Silicon host.
- Peak unified memory <= 20 GB.
- Output is usable after deterministic crop/overlay only, with no generative re-edit.
- Rights check permits monetized YouTube/affiliate use with "AI-generated illustrative demonstration" disclosure.

## Failure / Stop Conditions

- Product identity fails in any run: stop recommendation and classify product-affiliate hard-gate FAIL.
- First two runs both exceed six minutes or 20 GB: stop the third run.
- Loader requires paid compute or an unaudited binary: stop and seek approval/audit.
- Rights remain ambiguous: no publication or monetized use.

## Three Identical Runs

- Run 1: pending - identical locked inputs/settings.
- Run 2: pending - identical locked inputs/settings.
- Run 3: pending - identical locked inputs/settings.

## Evidence Package

Save source-rights record, input image and SHA-256, exact prompt/settings JSON and SHA-256, runtime commit/version, host specification, command log, wall time, peak memory, all three MP4s including failures, MP4 SHA-256 values, and first/mid/final frame QC contact sheets. Compare with the unquantized upstream MLX package only if it can be run at no cost on the same host.

## Outcome

**NOT RUN.** Blocked on a public compatible runtime and suitable Apple-Silicon test host. No credits or money were spent.
