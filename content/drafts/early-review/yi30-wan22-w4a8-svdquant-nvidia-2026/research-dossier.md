# Research Dossier: Yi30 Wan2.2 W4A8 SVDQuant — NVIDIA Artifacts

**Status:** Newly published community quantization; primary repository evidence only; no AIVP run  
**Release date:** 2026-09-10  
**Discovery date:** 2026-09-11  
**Contract materiality score:** 11 — QUALIFIED  
**Gate 1 score:** 8/10 — QUALIFIED  
**Content type:** First Look only

## Search strategy and deduplication

The Hugging Face monitor surfaced `Yi30/wan2.2-ti2v-w4a8-svd-nvidia`. The desk checked its model card and file description, the upstream Wan2.2 TI2V model and the referenced vLLM-Omni SVDQuant implementation.[1][2][3]

The publisher profile was checked separately for a verified contact route.[4]

This is not a new Wan model. It is a September 10 quantized checkpoint package for the existing Wan2.2 TI2V-5B and T2V-A14B models, so the event is classified as a new deployment artifact rather than a new foundation-model launch.[1][2]

The monitor's GitHub API source initially failed with `HTTPError`. A same-run deterministic retry recovered successfully and returned only the already-recorded `machina-exm/film-studio-skills` repository; GitHub coverage is therefore restored for this tick.

## Materiality

**Contract score 11 — threshold met.** Launch within 72 hours +3; product-reference support through the TI2V 5B artifact +2; explicit Apache-2.0 repository licence +2; primary repository evidence +2; likely specialist-reader impact from a portable precomputed NVIDIA quantization route +2.[1][2]

No points are awarded for a new hosted creator tool, immediate AIVP hands-on access, broad AU-SMB accessibility, transactional search intent or affiliate economics.

**Gate 1: 8/10 — QUALIFIED.** Relevance 3/3 because the 5B artifact supports text/image-to-video; differentiation 2/3 for precomputed W4A8 SVDQuant artifacts rather than a new generation model; recency 2/2; accessibility 1/2 because files are ungated but the documented validation target is an NVIDIA B300 and the smallest measured run peaks at 26.3GB.[1][2]

## Primary findings

The publisher describes calibrated W4A8 SVDQuant checkpoints using MXFP4 weights, dynamic MXFP8 activations and rank-32 correction. The package includes an approximately 9.5GB TI2V-5B transformer and approximately 54GB dual-expert A14B transformers, plus sample MP4s and trajectory-similarity files.[1]

The documented 5B sample uses 480×832, 41 frames and 20 steps, with reported 26.3GB peak memory. The A14B sample uses 720×1280, 81 frames and 40 steps, with reported 56.4GB peak memory. These are publisher measurements, not independent AIVP benchmarks.[1]

The base Wan2.2 TI2V-5B model supports text-to-video and image-to-video at 720p/24fps and identifies the original model release as July 28, 2025.[2]

The referenced vLLM-Omni pull request is merged, but its described purpose centres on an AMD gfx950 path; the Yi30 repository documents a separate pure-PyTorch CUDA export path from that implementation head. Integration therefore needs code audit and environment validation before use.[1][3]

## Access, cost and host feasibility

The repository is public and Apache-2.0 licensed.[1] No per-render vendor fee is documented, but that does not make the workflow costless: compatible GPU compute, storage, setup time and electricity remain unmeasured.

This AIVP host has 73GB free disk, 11GiB RAM and no `nvidia-smi`. It cannot execute the documented 26.3GB-VRAM minimum measured path, and a meaningful local pilot is blocked. No paid cloud compute or hardware purchase is authorized.

## Strength

**Verified floor 32/100; potential ceiling 100; evidence coverage 32%; confidence C; Monitor only.** The floor reflects documented image-conditioned capability, controls, packaged checkpoints, Apache licensing and a command-line integration path.[1][2]

Output quality, exact-product identity, repeatability, creator-hardware speed, failure rate and cost per accepted output remain unresolved. No Category Leader or Strong Specialist language is permitted.

The product-affiliate gate is closed until ASIN B0D2XTZN8V remains visually distinctive from frame one through all three bounded outputs. The checkpoint's existence alone is not evidence that it preserves exact product geometry.

## Contact and decision

The publisher profile identifies Yi Liu but publishes no email address or official vendor-domain contact.[4] No address was guessed and no form or social DM was used.

OUTREACH_STATUS: HELD_NO_VERIFIED_PUBLISHED_EMAIL.  
AFFILIATE_STATUS: NONE_FOUND.  
PUBLICATION_STATUS: STAGED_FIRST_LOOK_ONLY; HANDS_ON, PRODUCT_IDENTITY_AND_HOST_FEASIBILITY GATES OPEN.  
NEXT_ACTION: Obtain no-cost access to an audited NVIDIA environment with at least 32GB VRAM and adequate storage, or wait for lower-memory independently tested artifacts; then execute the locked three-run case study.

## Sources

[1] https://huggingface.co/Yi30/wan2.2-ti2v-w4a8-svd-nvidia — Wan2.2 W4A8 SVDQuant NVIDIA artifacts
[2] https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B-Diffusers — Wan2.2 TI2V 5B Diffusers base model
[3] https://github.com/vllm-project/vllm-omni/pull/6527 — vLLM-Omni PR 6527: Quark W4A8 SVDQuant support
[4] https://huggingface.co/Yi30 — Yi Liu (Yi30) Hugging Face profile
