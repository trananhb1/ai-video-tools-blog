# Research Dossier: Alibaba PAI MiniMax-H3-Fun-Controlnet-Union-2.0

**Status:** QUALIFIED - First Look only; publisher artifacts and documentation, no controlled AIVP run
**Release date:** 2026-09-22
**Discovery date:** 2026-09-22
**Contract materiality score:** 12
**Gate 1 score:** 9/10 - QUALIFIED

## Search strategy and deduplication

The desk inspected the official Alibaba PAI Hugging Face model card and API metadata, compared the release with the v1 model card, reviewed the linked VideoX-Fun repository, and read the shipped MiniMax H3 community licence.[1][2][3][4][5] This is a material v2 checkpoint rather than a duplicate: the publisher documents eight control conditions instead of five, ten control blocks instead of five, and a changed post-normalization inpainting recipe.[1][3]

## Gate 1 - launch materiality

- **Relevance: 3/3.** It directly controls, transforms and inpaints video.[1]
- **Differentiation: 3/3.** V2 adds Scribble, Layout and Gray control, doubles structural injection points, and changes the masked-pixel recipe for cleaner blending.[1][3]
- **Recency: 2/2.** Hugging Face records creation on September 22, 2026.[2]
- **Accessibility: 1/2.** The 13.59 GB checkpoint is public and ungated, but no inference provider is attached and the documented stack needs the separate roughly 62 GB transformer and roughly 62 GB text encoder, with offload on one 80 GB GPU.[1][2]
- **Total: 9/10 - QUALIFIED.**

**Contract score: 12.** Launch within 72 hours +3, primary source +2, new material tool/update without an AIVP page +3, likely reader impact +2, and reference/control inputs +2.[1][2]

## Documented capabilities and limits

One checkpoint supports Canny, Depth, HED, MLSD, Pose, Scribble, Layout and Gray control plus video inpainting. The publisher specifies 40 inference steps, guidance scale 1.0, control scale 1.0, 704x1280 sample budget, 24 fps and a maximum 15-second duration.[1] The checkpoint is only the control branch and requires the base MiniMax-H3 stack plus a specific v2 configuration; loading the v1 configuration silently drops half the control weights.[1]

The model card contains publisher-produced control/output samples, but AIVP has not rendered or independently inspected an output. Output quality, product-identity preservation, three-run consistency, render time, failure rate and accepted-output cost remain unresolved.[1]

The licence permits use only in the applicable territory, which excludes the EU, UK, Republic of Korea and United States; Australia is not excluded. It says MiniMax claims no rights over outputs, permits commercial use subject to conditions, requires separate authorization above US$20 million yearly commercial revenue, requires prominent MiniMax H3 display in commercial products, and mandates disclosure for public AI-generated information/content.[4]

## Gate 2 - strength

**Verified floor:** 34/100
**Potential ceiling:** 100/100
**Evidence coverage:** 34%
**Confidence:** C - primary publisher documentation and artifacts only
**Classification:** Weak fit pending controlled testing

The low floor reflects severe local hardware friction and the absence of independent output, timing, reliability and cost evidence. It is not a Strong Specialist or Category Leader claim.

## Gate 3 - case study

**CASE_STUDY:** `case-study-plan.md` - planned, held for rights-cleared product footage and no-cost compatible compute. Three identical runs will test whether Layout plus inpainting can preserve a Revlon One-Step Volumiser Plus 2.0 while changing only a background and selected masked region in a 15-second vertical affiliate clip.

## Gate 4 - outreach

Alibaba Cloud publishes press contacts on its official press-room page.[6] A policy-ready draft requests bounded PAI/DSW access, evaluation credits, prompt/workflow documentation, pricing, rights, media permission, partner terms and a technical contact. No form is used.

**OUTREACH_STATUS:** HELD_VALIDATOR_REJECTED_CONTACT_DOMAIN_SOURCE_MISMATCH
**AFFILIATE_STATUS:** NONE_VERIFIED
**PUBLICATION_STATUS:** STAGED_FIRST_LOOK_ONLY_NOT_PUBLISHED
**NEXT_ACTION:** Find a validator-compatible official published contact whose source proves the recipient domain; then revalidate. Await no-cost compute/access and rights before any three-run test.

## Sources

[1] https://huggingface.co/alibaba-pai/MiniMax-H3-Fun-Controlnet-Union-2.0 - Alibaba PAI model card
[2] https://huggingface.co/api/models/alibaba-pai/MiniMax-H3-Fun-Controlnet-Union-2.0 - Hugging Face API metadata
[3] https://huggingface.co/alibaba-pai/MiniMax-H3-Fun-Controlnet-Union - v1 model card
[4] https://huggingface.co/alibaba-pai/MiniMax-H3-Fun-Controlnet-Union-2.0/raw/main/LICENSE - MiniMax H3 community licence
[5] https://github.com/aigc-apps/VideoX-Fun - VideoX-Fun repository
[6] https://www.alibabacloud.com/en/press-room/press-release?_p_lc=1 - Alibaba Cloud official press contacts
