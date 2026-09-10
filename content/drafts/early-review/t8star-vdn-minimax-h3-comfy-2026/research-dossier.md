# Research Dossier: T8star VDN-MiniMax-H3 ComfyUI Bundle

**Status:** Late discovery through a duplicate Hugging Face mirror; primary bundle/docs only; no AIVP run
**Primary release date:** 2026-09-03
**Discovery date:** 2026-09-10
**Contract materiality score:** 16
**Gate 1 score:** 7/10 — CONDITIONAL, proceeds because files/workflows are accessible now
**Content type:** First Look only

## Search strategy and deduplication

The monitor surfaced `taurusduan/Vdn-Minimax-H3-Comfy`, created September 10 with zero downloads. Its README points users to `t8star/Vdn-Minimax-H3-Comfy`; the desk treated the Taurus upload as a duplicate mirror and evaluated the September 3 T8star primary bundle once.[1]

The primary-source pass covered the T8star model bundle, required ComfyUI node and MiniMax license.[1][2][3]

Upstream OpenVDN and the author profiles completed the provenance check.[4][5][6]

## Materiality

**Contract score 16 — threshold met.** New AIVP-uncovered workflow +3; immediately downloadable implementation +3; single/multiple reference images and reference-video inputs +2; commercial-use path in Australia +2; AU creator relevance +2; primary repository evidence +2; likely specialist-reader impact +2.[1][2][3]

No recency points: the primary bundle was seven days old at discovery. No affiliate or broad transactional-intent points are awarded.

**Gate 1: 7/10 — CONDITIONAL.** Relevance 3/3; differentiation 2/3 for a ready-to-place 83GB bundle plus tested ComfyUI extensions beyond upstream T2VA; recency 0/2; accessibility 2/2 because the repository is ungated and documents installation.[1][2][4]

## Primary findings

The bundle packages MiniMax H3/OpenVDN components into ComfyUI folders and documents text-to-video, first/last-frame, single/multiple-image, reference-video and audio workflows.[1]

It reports a 9/9 pruned compatibility matrix on an RTX 4060 Ti 16GB, while explicitly warning that this proves compatibility rather than universal quality or 16GB safety.[1]

Upstream OpenVDN says its September 6 release is about 82GB and reports a 14.4-second clip in 11.23 seconds on eight B200 GPUs; that is not a creator-hardware benchmark.[4]

This host has only 74GB free storage, no `nvidia-smi`, and no detected NVIDIA GPU. A full download would not fit and a meaningful local pilot cannot run here.

## Rights

The MiniMax H3 license permits use in Australia but excludes the EU, UK, South Korea and United States; requires attribution on commercial products/services, restricts use/output outside the applicable territory, and says MiniMax claims no rights over generated outputs.[3]

AIVP can plan Australian testing, but publication must disclose AI generation and cannot distribute or use the model/output into excluded territories under this license without separate authorization. This geographic output restriction materially limits a global web/YouTube workflow.[3]

## Strength

**Verified floor 43/100; potential ceiling 100; evidence coverage 43%; confidence C; Weak fit.** Reference controls, workflow packaging and Australian license access earn a floor.[1][2][3]

Upstream compatibility evidence is documented, but AIVP has no output, timing, failure or accepted-output-cost artifacts.[4]

No Category Leader or Strong Specialist language is permitted. Product-affiliate recommendation remains blocked until the exact product is visible and distinctive in the first 10 seconds across three saved runs.

## Contact and decision

The official GitHub and Hugging Face profiles link social/video channels but publish no email address.[5][6]

No address was guessed and no contact form was used. Outreach is held. There is no verified affiliate programme.

OUTREACH_STATUS: HELD_NO_VERIFIED_PUBLISHED_EMAIL.
AFFILIATE_STATUS: NONE_FOUND.
PUBLICATION_STATUS: STAGED_FIRST_LOOK_ONLY; RIGHTS_GEOGRAPHY_AND_HANDS_ON_GATES BLOCK PUBLICATION.
NEXT_ACTION: Re-test only on an Australian-hosted NVIDIA machine with at least 100GB free storage and an approved zero-cost compute allowance, or obtain bounded vendor-hosted access; do not download on this host.

## Sources

[1] https://huggingface.co/t8star/Vdn-Minimax-H3-Comfy — T8star OpenVDN MiniMax H3 ComfyUI bundle
[2] https://github.com/T8mars/comfyui-minimax-h3-audio-T8 — MiniMax H3 Audio T8 ComfyUI node
[3] https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE — MiniMax H3 Community License
[4] https://huggingface.co/OpenVDN/vdn-minimax-h3 — OpenVDN VDN-MiniMax-H3
[5] https://github.com/T8mars — T8mars GitHub profile
[6] https://huggingface.co/t8star — T8star Hugging Face profile
