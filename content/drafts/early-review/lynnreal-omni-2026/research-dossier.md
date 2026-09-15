# Research Dossier: LynnReal-Omni

**Status:** QUALIFIED — First Look only; publisher artifacts, no AIVP hands-on run
**Release date:** 2026-09-13
**Discovery date:** 2026-09-15
**Contract materiality score:** 12
**Gate 1 score:** 9/10 — QUALIFIED

## Search strategy and deduplication

The desk inspected the official repository and metadata, Standard and Flash model packages, lightweight VAE package, technical report, licence, and organization profile.[1][2][3]

The GitHub repository, three Hugging Face packages, ComfyUI workflows and paper are one underlying LynnReal-Omni beta launch, not separate candidates.[1][3][4]

The changed Google News entries were also deduplicated. The Social Media Examiner title changed capitalization only; its Seedance tutorial was already excluded as educational coverage rather than a launch.[9] The Dealroom Visko timestamp moved by three minutes, but it remains the already-staged September 1 Orbis event; direct Dealroom extraction failed again, so that secondary-body coverage remains UNKNOWN.[10]

## Gate 1 — launch materiality

LynnReal-Omni is a new early-beta framework built around a shared multimodal video model.[1][2] Its documented routes include text-to-video, image-to-video, single- and multi-subject references, body/hand pose control, video continuation, editing, repair and streaming long-video generation.[1]

**Gate 1: 9/10 — QUALIFIED.** Relevance 3/3; differentiation 3/3 for combining reference, pose, structural, editing, repair and streaming routes in one model family; recency 2/2.[1][2]

Accessibility is 1/2 because public code and ungated weights exist, but practical use requires a large local GPU stack and no hosted inference provider is attached.[1][3][4]

**Contract score: 12 — threshold met.** Launch within 72 hours +3; new tool without an AIVP page +3; product-reference input support +2; primary source confirmed +2; Australian applicability under the territorial licence +2.[1][2][6] No points were awarded for hands-on access, transactional demand, affiliate economics or measured reader impact.

## Documented capability and limits

The repository documents a 32B Standard model at four denoiser steps and a 27B Flash model at three steps, with default 1344×768 output and reference-image launchers.[1] The paper reports warm single-H100 timing for 22-frame 540p runs, but those are publisher benchmarks rather than AIVP tests.[8]

The model packages are publicly visible and ungated.

Hugging Face reports approximately 279.6 GB used storage for Standard and 117.5 GB for Flash; the lightweight VAE is a separate package.[3][4][5]

The repository itself warns that this is an early beta with unfinished features, possible compatibility issues and inconsistent generation quality.[1]

The README's model table still says uploads are planned even though Hugging Face metadata shows the Standard and Flash packages are populated. This documentation mismatch is material operational uncertainty, not evidence that either package runs correctly end to end.[1][3][4]

## Strength classification

**Verified floor: 34/100; potential ceiling: 100/100; evidence coverage: 34%; confidence C; classification: Monitor only.**

The floor credits documented reference and control routes plus CLI/ComfyUI workflows.[1]

It also credits publisher benchmark artifacts, public ungated packages and an Australia-compatible model licence.[3][6][8]

No exact-product fidelity, accepted-output quality, three-run consistency, vertical-output quality, cold-start time, failure rate or cost-per-accepted-output claim is treated as verified.[1][8] A documented reference-input route is not proof that a specific affiliate product survives generation.[1]

## Commercial rights and safety boundary

The repository uses the MiniMax H3 Community License.[6] It applies worldwide except the EU, UK, Republic of Korea and United States, so Australia is within the stated territory; MiniMax claims no rights over outputs, while attribution, disclosure, acceptable-use and territorial restrictions still apply.[6] These terms do not grant rights to third-party product imagery, trademarks or likenesses.[6]

Any public AIVP output must be labelled as an AI-generated illustrative demonstration and must not be represented as physical product-performance proof. Supplier asset permission remains a production prerequisite.

## Access, security and cost gate

No weights were downloaded and no generation was attempted. The current host exposes no NVIDIA GPU and has 67 GB free disk, below even the reported Flash package storage footprint. A clone-only source inspection used no paid credits, but a full Stage 2 integration audit and model run remain blocked by hardware, storage and potential compute cost.

## Outreach and affiliate decision

The official GitHub organization profile publishes no website or contact address.[7] The technical report contains an author contact on a `lynnreal.com` domain, but no accessible official-domain contact page was found to satisfy the standing outreach validator.[7][8] Git commit addresses and guessed aliases are not compliant substitutes.

**OUTREACH_STATUS:** HELD_NO_VERIFIED_OFFICIAL_DOMAIN_PUBLISHED_CONTACT.
**AFFILIATE_STATUS:** NOT_FOUND.
**PUBLICATION_STATUS:** STAGED_FIRST_LOOK_ONLY_NOT_PUBLISHABLE.
**NEXT_ACTION:** Monitor for a hosted no-cost inference route or substantially smaller verified package and an official-domain contact page; then complete the code/security audit before three exact-product runs.

## Sources

[1] https://github.com/LynnReal-AI/LynnReal-Omni — LynnReal-Omni official repository and README
[2] https://api.github.com/repos/LynnReal-AI/LynnReal-Omni — GitHub repository metadata
[3] https://huggingface.co/api/models/stdstu123/LynnReal-Onmi-beta-0.1 — LynnReal Standard model metadata
[4] https://huggingface.co/api/models/stdstu123/LynnReal-Onmi-flash-beta-0.1 — LynnReal Flash model metadata
[5] https://huggingface.co/stdstu123/LynnReal-Onmi-light-vae — LynnReal Lightweight Video VAE model card
[6] https://raw.githubusercontent.com/LynnReal-AI/LynnReal-Omni/main/LICENSE — MiniMax H3 Community License used by LynnReal-Omni
[7] https://api.github.com/orgs/LynnReal-AI — LynnReal-AI GitHub organization metadata
[8] https://github.com/LynnReal-AI/LynnReal-Omni/blob/main/docs/LynnReal-Omni-Paper.pdf — LynnReal-Omni technical report
[9] https://www.socialmediaexaminer.com/how-to-think-like-a-filmmaker-ai-video-with-seedance — Social Media Examiner Seedance filmmaking tutorial
[10] https://dealroom.co/news/150573-visko-raises-10m-pre-seed-for-hour-long-4k-ai-video-model — Dealroom Visko Orbis launch/funding item
