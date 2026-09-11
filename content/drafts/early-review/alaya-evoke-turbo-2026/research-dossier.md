# Research Dossier: Alaya-EVOKE-Turbo

**Status:** New official model variant; primary repository evidence only; no AIVP run  
**Release date:** 2026-09-11  
**Discovery date:** 2026-09-11  
**Contract materiality score:** 9 — QUALIFIED  
**Gate 1 score:** 8/10 — QUALIFIED  
**Content type:** First Look only; commercial publication blocked

## Search strategy and deduplication

The Hugging Face monitor surfaced `AlayaLab/Evoke-Turbo`.

The desk checked the official model card/API and EVOKE repository.[1][2][3]

It separately checked the base-model card, required ViGeo dependency and project page.[4][5][6]

Commit history and hosted-demo status were also checked.[7][10]

This is not the August EVOKE foundation-model launch. The official September 11 commit announces a new controllability-optimized Turbo checkpoint, and the new repository identifies EVOKE as its base model.[1][2][7]

No other changed monitor item represents a new event in this tick: the Google News, Product Hunt, OpenAI, Google AI, older Hugging Face entries and GitHub result are unchanged from the prior snapshot.

## Gate 1 — launch materiality

**Contract score 9 — threshold met.** Launch within 72 hours +3; reference-input relevance through the documented shared EVOKE image/video conditioning workflow +2; primary official repository evidence +2; likely specialist-reader impact from a new camera/instruction-control variant +2.[1][2][3]

No points are awarded for a new hosted creator product, immediate AIVP hands-on access, explicit commercial output rights, broad AU-SMB accessibility, transactional search intent or affiliate economics. The required ViGeo checkpoint is CC BY-NC 4.0, so this workflow is not cleared for monetized AIVP output.[1][5]

**Gate 1: 8/10 — QUALIFIED.**

Relevance is 3/3 because the model generates video and shares EVOKE's text/image/video conditioning workflow.[1][3]

Differentiation is 2/3 because it is a control-optimized checkpoint rather than a new architecture, and recency is 2/2.[1][2][7]

Accessibility is 1/2 because weights are ungated but there is no inference provider, the hosted community Space is sleeping, and local requirements are impractical on this host.[2][10]

## Primary findings

Alaya Lab describes Turbo as a controllability-optimized EVOKE variant focused on camera-motion following and scene/subject instruction adherence. It retains the 14B architecture, three-step CFG-free inference and 384 × 640 output at 24 fps.[1]

The repository reports a WBench average of 82.0003 for Turbo versus 80.8210 for base EVOKE, with higher Navigation, Consistency and Physical scores but lower Video Quality and Setting scores. The card explicitly says Turbo's seed-44 results were selected from six prompt variants while EVOKE uses published scores with different prompts and poses, so this is not a controlled apples-to-apples AIVP benchmark.[1]

The Turbo transformer is FP32, 14.31B parameters and 57,249,822,376 bytes.[2]

It additionally requires the EVOKE base components and ViGeo depth backend.[1][2]

The selectively required EVOKE base files total 23,252,745,039 bytes and ViGeo adds 5,021,893,802 bytes, yielding about 79.7 GiB before code, caches and outputs; this host has only 73 GiB free.[8][9]

The current host also has 11 GiB RAM and no `nvidia-smi`.

The official base implementation reports its speed on one H200, not creator hardware.[3]

No download or generation was attempted because storage and compatible accelerator gates fail.

## Commercial-rights finding

Turbo and the base repository declare Apache-2.0, but the Turbo card says external components retain their own licences and requires ViGeo.[1][4]

ViGeo explicitly declares CC BY-NC 4.0 and is a preliminary checkpoint with a known loss-implementation issue that may cause minor camera-pose and distant-region visualization artifacts.[5]

That required noncommercial dependency closes the monetized-output and publication gate.[1][5] A vendor clarification, commercial ViGeo licence, or documented commercially permitted replacement depth backend is required before AIVP may use generated output in affiliate or AdSense content.[5]

## Strength and decision

**Verified floor 19/100; potential ceiling 90; evidence coverage 29%; confidence C; Monitor only.**

Documented reference conditioning, camera/prompt controls, CLI workflow and open weight access earn limited floor points.[1][3]

Output quality, exact-product fidelity, repeatability, render reliability and cost per accepted output remain untested, while the current commercial-rights criterion is a resolved failure.[1][3][5]

No Category Leader or Strong Specialist language is permitted at confidence C.

The first-10-seconds product gate remains closed until the exact LED mask survives three artifact-backed runs, and the commercial-rights gate must be resolved first.[1][5]

## Contact, affiliate and publication status

The official project page publishes two contributor addresses, but neither uses Alaya Lab's official `alayalab.ai` domain.[6]

A direct fetch of the official Alaya Lab website succeeded but exposed no email address; contact coverage is therefore complete for the checked official web surfaces, not an unknown source failure.[11]

The standing policy requires a published official-domain contact, so no address was guessed and no email was sent.[6]

STRENGTH: Monitor only — 19/100 verified floor, 90 ceiling, 29% coverage, confidence C.[1][3][5]  
CASE_STUDY: Planned; blocked by noncommercial required dependency, hardware and storage.[2][5][8]  
OUTREACH_STATUS: HELD_NO_VERIFIED_OFFICIAL_DOMAIN_EMAIL.  
AFFILIATE_STATUS: NONE_FOUND on the checked official surfaces.[1][3][6]  
PUBLICATION_STATUS: STAGED_FIRST_LOOK_ONLY; BLOCKED_BY_COMMERCIAL_RIGHTS_AND_HANDS_ON_GATES.[1][5]  
NEXT_ACTION: Wait for Alaya Lab to publish an official-domain contact or commercially permitted depth-backend route; then request rights clarification and no-cost bounded remote test access before any pilot.[5][6]

## Sources

[1] https://huggingface.co/AlayaLab/Evoke-Turbo — AlayaLab Evoke-Turbo model card
[2] https://huggingface.co/api/models/AlayaLab/Evoke-Turbo — Evoke-Turbo Hugging Face API metadata
[3] https://github.com/AlayaLab/Evoke — Official EVOKE implementation
[4] https://huggingface.co/AlayaLab/Evoke — AlayaLab EVOKE base model card
[5] https://huggingface.co/pkqbajng/ViGeo — ViGeo required depth backend model card
[6] https://evoke-world.github.io/Evoke — Official EVOKE project page and contributor contacts
[7] https://github.com/AlayaLab/Evoke/commits/main — EVOKE commit history
[8] https://huggingface.co/api/models/AlayaLab/Evoke/tree/main/evoke-base — EVOKE base component tree
[9] https://huggingface.co/api/models/pkqbajng/ViGeo/tree/main — ViGeo repository file tree
[10] https://huggingface.co/spaces/hugging-apps/evoke — Community EVOKE Hugging Face Space status
[11] https://alayalab.ai — Alaya Lab official website
