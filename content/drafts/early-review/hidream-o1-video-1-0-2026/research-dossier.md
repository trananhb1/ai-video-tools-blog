# Research Dossier: HiDream-O1-Video-1.0 (HD-V1) Launch

**Observed:** September 17, 2026, 10:16 CEST  
**Status:** QUALIFIED — First Look only; no AIVP hands-on run  
**Underlying event:** HiDream-O1-Video-1.0 (HD-V1) native omnimodal foundation model launch, September 15, 2026

## Search strategy and deduplication

The radar monitor surfaced Google News syndication from The Manila Times covering the HiDream-O1-Video-1.0 launch.[5]

The desk retrieved and validated primary launch reporting from Phoenix Tech dated September 15, 2026.[1]

It separately inspected official developer documentation on HiHarness, the HiDream developer portal, and the primary platform site.[2][3][4]

Multiple news and syndication items reference the same underlying release; they are deduplicated as a single foundational model launch event.[1][5]

## Gate 1 — Launch materiality

**Gate 1 score: 9/10 — QUALIFIED.** Relevance 3/3 because HD-V1 provides multimodal video generation from text, image, and video inputs.[1][2]

Differentiation 3/3 because it introduces a native omnimodal architecture with physical law modeling, 5–20s duration, integrated native audio, and top-tier benchmark placements.[1]

Recency 2/2 for discovery within 48 hours of the September 15 launch.[1]

Accessibility 1/2 because HiHarness documents a callable async single-image-to-video API with published request/response schema, though Australian self-serve accessibility cannot be assumed beyond public documentation and no hands-on execution has taken place.[2]

**Contract score: 17 — threshold met.** Launch within 72 hours +3, primary source confirmed +2, and product reference inputs supported +2.[1][2]

New tool status +3, transactional search intent +3, likely reader impact +2, and Australian creator/SMB fit +2 round out the scoring.[3][5]

## What is verified—and what is not

Phoenix Tech reports that HiDream.ai officially released HiDream-O1-Video-1.0 (HD-V1) on September 15, 2026, featuring text, image, and video inputs, direct 1080p generation between 5 and 20 seconds, and native audio-visual synchronization.[1]

The launch reporting claims the model ranks fourth on the Artificial Analysis Image to Video Leaderboard (With Audio) and eighth on the Arena.ai Image-to-Video blind test.[1]

The reporting also describes structured multimodal intent planning, physics-guided simulation, and a simultaneous C+ funding round from Sinoview Capital, Jiaozi Capital, and ICBC Capital.[1] These assertions must be treated as vendor and press claims rather than independently audited facts.[1]

HiHarness official documentation confirms that `HiDream-O1-Video-1.0` is exposed as an asynchronous single-image-to-video API endpoint.[2]

The API accepts one reference image supplied via public URL or Base64 encoding alongside a text prompt, preserves the input aspect ratio, and supports dynamic duration or a fixed 10-second duration.[2]

The workflow requires submitting a task, retrieving a `task_id`, and polling the result endpoint until completion.[2]

What is not verified is hands-on generation: actual queue latency, render duration, error rates, billed credit debit on HiHarness, end-user commercial ownership terms, and exact product identity retention remain untested.[2][3]

The HiDream developer portal highlights enterprise MaaS solutions, over 200 APIs, and commercial creative tools, but does not publish a granular public pricing table for HD-V1.[3]

The platform site showcases creative tooling but provides no public self-serve affiliate application or explicit end-user licensing agreement for HD-V1 outputs.[4]

## Gate 2 — Strength

**Verified floor:** 35/100  
**Potential ceiling:** 100/100  
**Evidence coverage:** 35%  
**Confidence:** C — primary documentation and launch reporting only; no hands-on run  
**Classification:** Monitor only

The September 15 release establishes high technical interest and verifiable API endpoint documentation, but no hands-on test exists.[1][2]

Under hard standing rules, no tool may be classified as Category Leader or Strong Specialist below confidence B.[1]

AIVP will not recommend HD-V1 for product-affiliate workflows until controlled testing confirms exact-product identity retention throughout the first 10 seconds.

## Gate 3 — Case study

**CASE_STUDY: PLANNED_NOT_RUN_COST_RIGHTS_ACCESS_BLOCKED.** The locked test evaluates whether HD-V1 can take a single reference image of the rights-cleared white LED face mask (Amazon ASIN B0D2XTZN8V) and generate three consistent 10-second vertical promotional clips that keep the exact product visually distinctive throughout the first 10 seconds, with synchronized ambient audio, at a cost under US$2.00 per accepted output. No API calls were made because credit debits, commercial rights, and billing limits remain unverified.[2][3]

## Gate 4 — Outreach and affiliate

A search was conducted across official reporting and HiHarness documentation.[1][2]
Additional checks evaluated dev.hidreamai.com and hidreamai.com.[3][4]

The address `info@hidream.ai` is published on `dev.hidreamai.com` but absent from the root domain `https://hidream.ai`.[3][4]

Under standing policy `aivp-qualified-launch-outreach-v1`, cross-domain publication is unverified without root-domain confirmation.

Furthermore, no dedicated affiliate contact or programme exists on the platform.[4]

In accordance with desk instructions, outreach is held under `HOLD_NO_VERIFIED_CONTACT`. No email was sent, no trial credits were consumed, and no financial details were entered.

**OUTREACH_STATUS:** HOLD_NO_VERIFIED_CONTACT  
**AFFILIATE_STATUS:** NONE_FOUND  
**PUBLICATION_STATUS:** STAGED_FIRST_LOOK_ONLY_NOT_PUBLISHED  
**NEXT_ACTION:** Hold outreach until an official root-domain contact or dedicated partnership route is verified; do not apply or consume paid credits.

## Sources

[1] https://i.ifeng.com/c/8wRbgGbpwie — Phoenix Tech HD-V1 launch reporting
[2] https://hiharness.ai/docs/hidream_o/video/introduction.html — HiHarness HiDream-O1-Video-1.0 documentation
[3] https://dev.hidreamai.com — HiDream developer portal
[4] https://hidreamai.com — HiDream official platform
[5] https://news.google.com/rss/articles/CBMijgJBVV95cUxPVVl0MHNrU1AxOHMxNDIzNzduR0lJZXRjZEZFRGVVMml0cjlGTUk4c0E5ZE1oNXpRTTAtODM2TEFvX3U2ZGFsN0dDWXRpb2ZwajVxU0RPd0hhWUlfejBlQmxYLWNzSlRYTThWaWE1cGdQcHhmYzRhY2twbm9QQkhjOWFOVVItRjl2dG5pbnJZaVFGZ1RUd2pVR25QLTBQdGw3N0lBLUVTYmpZOE1faGhNRzJFUlhNemd3SFpBdXRjV24wTEkwY3FsSWYwcFc0T19idmZPeXYzTldOc1p2Y01OLWZQcEdmNE1SY05GMS11a1VOcmFpbWk0SHM4d2lVVHpVczl0ZEpHOE5LUFFBcXfSAZMCQVVfeXFMUGFKUko2ZnVhYWQwcWNGQk5SM3ozQ2E5MzhPWlpsSWJXb0tGQTlpb1BqR2JJQVVEWTFjWTdoR1NGa25pR2dZSTUtR1lmRDMyM2FKS3B6emdGb3hyZzFqLWZfV2hPQ3hZTFJJeTBLQjlGLVVvTkdDaFoyZUtBWVNRLW9HWkVLdVRBbG5WYmZFbVliZHJ1MGRfbWFIcTF6TFFMWkI2aURkMk4yc1c5SGt6cEEtUnZrY0llcm1fMlhqcEFXR0NkbjVQUTZGam9xR2ZCeXZvSlJDUWR1WndWLXJ6WFVKVlkwckEzR3BJRVZBVnJKdGlQOGwxd2UyZ0JDVzA3Q2xiTEZVdkhfbjFNZjV2Q283bnM?oc=5 — Google News Manila Times launch radar
