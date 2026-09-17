# Research Dossier: changwangss Wan2.2 SVDQuant

**Status:** New community quantization artifact; repository evidence only; no AIVP run  
**Release/discovery date:** 2026-09-16  
**Contract materiality score:** 10 — QUALIFIED  
**Gate 1 score:** 8/10 — QUALIFIED  
**Content type:** First Look only

## Search strategy and deduplication

The monitor surfaced `changwangss/wan22-svdquant-signround-nosmooth`. The desk inspected the repository model card, quantization audit/run manifests and upstream Wan2.2 T2V-A14B model. This is a new deployment artifact for an existing July 2025 model, not a new foundation-model release.[3][4]

## Materiality

**Contract score 10 — threshold met.** Launch within 72 hours +3; primary artifact evidence +2; new deployment artifact +3; specialist-reader impact +2.[3]

**Gate 1: 8/10 — QUALIFIED.** Relevance 3/3; differentiation 2/3 for a documented dual-expert W4A8/SVDQuant export; recency 2/2; accessibility 1/2 because files are ungated but no creator-hardware inference envelope is documented.[3]

## Primary findings

The run manifest records rank-32 SVDQuant, MXFP4 weights, dynamic MXFP8 activations, 16 calibration steps and eight calibration prompts. Export auditing reports 400 quantized linears in each of Wan2.2's two experts.[3]

Calibration ran on two NVIDIA B300 GPUs and peaked at about 202.34GiB CUDA allocation per worker; this describes model preparation, not necessarily inference. The repository provides no independent perceptual benchmark, creator-GPU inference memory, end-to-end render timing or controlled output-quality evidence.[3]

The artifact is text-to-video only, so it structurally fails AIVP's exact-product affiliate hard gate. Its appropriate test is a narrative/explainer b-roll workflow, not an ASIN-specific recommendation.[3][4]

## Access, cost and host feasibility

The repository is public and labels the artifact Apache-2.0.[3][4] The current host has no NVIDIA GPU and cannot run it. No paid cloud compute or hardware purchase is authorized.

## Strength

**Verified floor 26/100; potential ceiling 80; evidence coverage 33%; confidence C; Monitor only.** Packaging, quantization controls, CLI-compatible Diffusers structure and licensing are documented, but product specificity is a known zero and output quality, speed, reliability and real cost remain unverified.[3][4]

## Contact and decision

No official vendor-domain published email was found. No address was guessed and no form or social DM was used.

OUTREACH_STATUS: HELD_NO_VERIFIED_PUBLISHED_EMAIL.  
AFFILIATE_STATUS: NONE_FOUND.  
PUBLICATION_STATUS: STAGED_FIRST_LOOK_ONLY.  
NEXT_ACTION: Wait for no-cost audited NVIDIA access and creator-hardware inference documentation; if available, run the locked three-run narrative b-roll test. Do not use for exact-product affiliate video.

## Sources

[3] https://huggingface.co/changwangss/wan22-svdquant-signround-nosmooth — Wan2.2 SVDQuant artifact
[4] https://huggingface.co/Wan-AI/Wan2.2-T2V-A14B-Diffusers — Wan2.2 T2V A14B base model
