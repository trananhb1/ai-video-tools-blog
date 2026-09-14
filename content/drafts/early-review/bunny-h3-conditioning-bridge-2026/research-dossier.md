# Research Dossier: BUNNY H3 Conditioning Bridge V1

**Status:** New community conditioning adapter; publisher evidence only; no AIVP run  
**Release date:** 2026-09-13  
**Discovery date:** 2026-09-14  
**Contract materiality score:** 13 — QUALIFIED  
**Gate 1 score:** 9/10 — QUALIFIED  
**Content type:** First Look only

## Search strategy and deduplication

The Hugging Face monitor first surfaced the item under `JOKER141/BUNNY-H3-Semantic-Bridge`; the live repository was then renamed to `JOKER141/BUNNY_H3_Conditioning_Bridge`. Hugging Face preserves the same creation timestamp, `2026-09-13T23:03:26Z`, while the linked GitHub repository records an initial release followed by the rename and a v1.0.2 metadata update.[1][2][3]

The desk checked the live model card and metadata plus the linked source repository and node implementation.[1][2][3]

MiniMax's official H3 model card and licence, the author's public profile, and the earlier Semantic Bridge project credited by the publisher were checked separately.[5][6][8]

This is a distinct action-logic conditioning adapter, not a new foundation model. It is derived from MiniMax H3 and inspired by the earlier Semantic Bridge; the claimed differentiator is a narrower focus on character/action ownership, attacker/target relationships, object ownership, occlusion and state continuity in complex multi-character scenes.[1][3][9]

A second newly surfaced item, `ToyBoyboos/Wan2.2-Lightning`, states at the top of its own card that it is duplicated from `lightx2v/Wan2.2-Lightning`. The underlying Lightning release dates to August 2025, so the September 2026 copy is excluded as a duplicate rather than treated as a launch.[10]

## Materiality

**Contract score 13 — threshold met.** Launch within 72 hours +3; no existing AIVP page +3; public ungated artifact available now +3; primary model/repository evidence +2; likely reader impact +2.[1][2][3]

No points are awarded for exact-product reference support, explicit derivative-package compliance, broad AU-SMB accessibility, transactional demand or affiliate economics. The adapter has no hosted inference provider and still requires a local MiniMax H3/ComfyUI workflow.[1][5]

**Gate 1: 9/10 — QUALIFIED.** Relevance 3/3 because it modifies video-model conditioning; differentiation 3/3 because it targets action-role and scene-state logic rather than motion smoothness; recency 2/2; accessibility 1/2 because the files and node are public but no hosted inference route exists and the current AIVP host has no NVIDIA GPU.[1][3][4]

## Primary findings

The 130,109,150-byte Hugging Face repository contains one safetensors adapter, an example workflow and three comparison videos. It is ungated, has zero recorded downloads, two likes and no inference-provider deployment at assessment time.[1][2]

The publisher documents a ComfyUI node placed after H3 text conditioning, with `alpha` from 0 to 1, `per_token`, `global` or `none` magnitude matching, and a true bypass. Source inspection confirms safetensors-only loading, tensor-shape validation, path-containment logic for bundled models and no network or shell execution in `nodes.py`.[3][4] This is a limited source inspection, not the mandatory full dependency/security audit required before installation.

The publisher reports approximate internal observations: about 60% of cases improved to some degree, about 20% showed no obvious difference and about 10% regressed. The card explicitly says these are not a formal benchmark and need not sum to 100%; AIVP therefore treats them as vendor/publisher claims, not verified output-quality evidence.[1][3]

The adapter's card does not document Ref2VA compatibility. The credited original Semantic Bridge explicitly says its v1 does not support reference-conditioned Ref2VA and that such tests degraded singing/lip-sync.[9] BUNNY's exact-product and reference-input behavior must therefore remain unresolved rather than inherited from the MiniMax H3 base model.

## Rights, cost and host feasibility

The candidate metadata uses `license: other` and links to the MiniMax H3 Community License, but the linked GitHub file tree includes no `LICENSE` or `NOTICE` file.[2][3]

MiniMax defines adapters/derived works as Model Derivatives, limits the open-weight licence to an applicable territory that excludes the EU, UK, South Korea and US, requires compliance conditions for distribution, and says MiniMax claims no rights over generated outputs.[6][7]

Australia is not listed as excluded, but AIVP has not made a legal determination about this candidate's derivative-package compliance.[6]

No per-render vendor fee is documented for the downloadable adapter. Real accepted-output cost remains unknown because the 33B MiniMax H3 base workflow, hardware, electricity and setup are still required.[1][5] The current host has no `nvidia-smi`, about 12 GB system RAM and no approved paid GPU allowance, so no generation was attempted.

## Strength

**Verified floor 17/100; potential ceiling 100; evidence coverage 17%; confidence C; Monitor only.** Verified points cover explicit conditioning controls, a documented ComfyUI insertion path, public downloadable files, limited source-level integration evidence, and partial upstream-rights clarity.[1][3][4]

Output quality, exact-product identity, Ref2VA behavior, repeated consistency, speed, failure rate, accepted-output economics and derivative-package compliance remain unresolved. No Category Leader or Strong Specialist language is permitted.

The product-affiliate gate remains closed until three controlled bridge-OFF/bridge-ON pairs preserve the exact LED mask identity from frame one through the first 10 seconds while reducing hand/controller relationship errors.

## Contact and decision

The public GitHub profile identifies the author as FourBunny but publishes no company, website, email or social account.[8] No official-domain published candidate contact was found. MiniMax's published model contact is not an authorized contact for this independent adapter, so it is not used for outreach.

OUTREACH_STATUS: HELD_NO_VERIFIED_OFFICIAL_DOMAIN_CONTACT.  
AFFILIATE_STATUS: NONE_FOUND.  
PUBLICATION_STATUS: STAGED_FIRST_LOOK_ONLY; HANDS_ON, SECURITY, RIGHTS, PRODUCT_IDENTITY_AND_HARDWARE GATES OPEN.  
NEXT_ACTION: Recheck for an official contact and Ref2VA statement; run the locked no-cost paired case study only after audited compatible NVIDIA access exists and rights/package compliance are resolved.

## Sources

[1] https://huggingface.co/JOKER141/BUNNY_H3_Conditioning_Bridge — BUNNY H3 Conditioning Bridge model card
[2] https://huggingface.co/api/models/JOKER141/BUNNY_H3_Conditioning_Bridge — Hugging Face model metadata
[3] https://github.com/aa335615543-ux/BUNNY_H3_Conditioning_Bridge — BUNNY H3 Conditioning Bridge repository
[4] https://raw.githubusercontent.com/aa335615543-ux/BUNNY_H3_Conditioning_Bridge/main/nodes.py — BUNNY H3 Conditioning Bridge node source
[5] https://huggingface.co/MiniMaxAI/MiniMax-H3 — Official MiniMax H3 model card
[6] https://huggingface.co/MiniMaxAI/MiniMax-H3/raw/main/LICENSE — MiniMax H3 Community License Agreement
[7] https://huggingface.co/MiniMaxAI/MiniMax-H3/raw/main/docs/QA-about-License.md — MiniMax H3 license Q&A
[8] https://api.github.com/users/aa335615543-ux — FourBunny public GitHub profile
[9] https://huggingface.co/speach1sdef178/MiniMax-H3-Semantic-Bridge — Original MiniMax H3 Semantic Bridge model card
[10] https://huggingface.co/ToyBoyboos/Wan2.2-Lightning — ToyBoyboos Wan2.2-Lightning duplicate model card
