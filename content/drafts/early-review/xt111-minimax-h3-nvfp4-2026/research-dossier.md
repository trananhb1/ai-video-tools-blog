# Research Dossier: xt111 MiniMax H3 NVFP4

**Status:** New community deployment artifact; repository evidence only; no AIVP run  
**Release/discovery date:** 2026-09-16  
**Contract materiality score:** 14 — QUALIFIED  
**Gate 1 score:** 9/10 — QUALIFIED  
**Content type:** First Look only

## Search strategy and deduplication

The Hugging Face monitor surfaced `xt111/MiniMax-H3-NVFP4`. The desk inspected the model card, repository metadata and upstream MiniMax H3 model. The repository is a new packaging of existing MiniMax H3 weights rather than a new foundation model.[1][2]

The publisher discloses that two mixed-precision files are mirrors from `rockerBOO`; those files are not treated as a new event. The candidate event is the publisher's own single-pass 12.5GB ref2va/fl2va NVFP4 builds and associated ComfyUI documentation.[1]

## Materiality

**Contract score 14 — threshold met.** Launch within 72 hours +3; primary repository +2; new deployment artifact +3; reference-image support +2; likely specialist-reader impact +2; transactional hardware/workflow intent +2.[1]

**Gate 1: 9/10 — QUALIFIED.** Relevance 3/3; differentiation 2/3 for new small-footprint NVFP4 ref2va/fl2va packages; recency 2/2; accessibility 2/2 because files are ungated and available globally, although practical use requires Blackwell hardware.[1]

## Primary findings

The repository packages 12.5GB pruned NVFP4 variants for reference-image-to-video and first/last-frame-to-video. Its publisher reports 11.9GB DiT VRAM and 1.90 seconds per iteration for ref2va on an RTX PRO 6000 Blackwell, but also says current single-pass builds have not been re-benchmarked and the fl2va build has not been run end to end.[1]

The card explicitly warns that 4-bit weights may reduce motion quality versus the upstream 8-bit route, retracts an earlier no-visible-degradation statement, and says the current quality comparison remains untested. It also records an out-of-memory failure for 1344×768 at 362 frames even on a 96GB card.[1]

The inherited MiniMax H3 community licence is not an unrestricted open-source grant. Output and territorial/commercial conditions require direct legal review before monetized use.[1][2]

## Access, cost and host feasibility

The files are ungated with no model fee, but native NVFP4 requires NVIDIA Blackwell hardware. The current AIVP host has no NVIDIA GPU and cannot execute this case study. Downloading the full components would also consume substantial storage without a runnable environment. No paid cloud compute or hardware purchase is authorized.

## Strength

**Verified floor 34/100; potential ceiling 100; evidence coverage 34%; confidence C; Monitor only.** Reference inputs, deterministic files, detailed limitations and a ComfyUI path are documented. Exact-product fidelity, current-build quality, three-run consistency, accepted-output cost and licence suitability remain unresolved.[1][2]

No Category Leader or Strong Specialist language is permitted. Product-affiliate use remains blocked until the exact ASIN is visually distinctive in the first frame and through all three bounded runs.

## Contact and decision

No official vendor-domain published email was found on the repository or model card. No address was guessed and no form or social DM was used.

OUTREACH_STATUS: HELD_NO_VERIFIED_PUBLISHED_EMAIL.  
AFFILIATE_STATUS: NONE_FOUND.  
PUBLICATION_STATUS: STAGED_FIRST_LOOK_ONLY.  
NEXT_ACTION: Wait for no-cost audited Blackwell access or independently verified current-build tests; then run the locked three-run exact-product case study and review the inherited licence.

## Sources

[1] https://huggingface.co/xt111/MiniMax-H3-NVFP4 — MiniMax H3 NVFP4 model card
[2] https://huggingface.co/MiniMaxAI/MiniMax-H3 — MiniMax H3 base model
