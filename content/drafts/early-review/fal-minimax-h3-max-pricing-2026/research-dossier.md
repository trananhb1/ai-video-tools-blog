# Research Dossier: fal MiniMax H3 Max Pricing Expiry

**Status:** QUALIFIED — First Look only; no AIVP hands-on run  
**Event date:** 2026-09-15  
**Discovery date:** 2026-09-15  
**Contract materiality score:** 15  
**Gate 1 materiality:** 9/10

## Decision

fal published launch discounts of 75% for MiniMax H3 Max and H3 Max Turbo, with the H3 Max and Turbo pages stating that the discount ends September 14.[1][2]

The stated post-promotion rates are four times the launch rates.[1][2]

This is a material cost change for creators evaluating these endpoints, but direct page retrieval still displays the promotional amount beside the expired deadline.[1][2]

The effective billed rate is therefore not treated as verified until an account quote or invoice confirms it.[unverified]

A secondary report says the price quadrupled, but AIVP does not use that headline as billing proof because the official fal page is internally stale or transitional.[6]

## Search strategy and source assessment

The monitor delta was checked against the official fal model pages, fal reference-input pricing, MiniMax direct API pricing, and the reporting page that triggered the alert.[1][3][4]

Primary pages outrank the secondary report.[unverified]

The official fal pages document the deadline and scheduled prices; MiniMax separately lists H3 and H3 Max direct API prices, which prevents conflating fal infrastructure pricing with MiniMax direct pricing.[1][2][4]

## Gate 1 — Launch materiality

- Relevance to AI-video production: **3/3** — this directly changes generation cost.[1][2]
- Differentiation/material change: **2/3** — a fourfold scheduled price reset materially changes workflow economics, though it is not a new model.[1][2]
- Recency: **2/2** — the stated discount ended September 14 and was detected September 15.[1][2]
- Accessibility: **2/2** — public API/playground endpoints are accessible, but generation is paid and was not run.[1][2]
- **Total: 9/10 — QUALIFIED.**

Contract score is **15**: launch recency 3, immediate endpoint access 3, product-reference support 2, transactional intent 3, primary confirmation 2, and likely reader impact 2.

## Verified pricing facts

The H3 Max page lists promotional output rates of US$0.0125/s at 480p, US$0.02/s at 768p and US$0.04/s at 1080p, followed by scheduled standard rates of US$0.05/s, US$0.08/s and US$0.16/s after September 14.[1]

The Turbo image-to-video page lists US$0.00625/s, US$0.01/s and US$0.02/s promotional rates, followed by US$0.025/s, US$0.04/s and US$0.08/s after September 14.[2]

fal reference-to-video currently lists US$0.08/s at 768p plus token-priced reference inputs beyond an allowance.[3]

MiniMax direct pricing separately lists H3 Max at US$0.05/s for 480p and US$0.08/s for 768p.[4]

## Strength classification

**Verified floor: 47/100. Potential ceiling: 100/100. Evidence coverage: 47%. Confidence: C. Classification: Weak fit pending a controlled run.**

The docs verify API availability, image/reference input routes, explicit model-page commercial-use labelling, output dimensions and pricing mechanics.[1][2][3]

They do not verify exact-product preservation, multi-run consistency, the actual post-deadline charge, failure rate, output quality, or full monetised-output rights.[unverified]

## Product-specificity and commercial gates

H3 Max Turbo image-to-video accepts a starting image, while the separate H3 Max reference endpoint accepts multiple image, video and audio references.[2][3]

That capability does not establish ASIN fidelity.[unverified]

Product-affiliate recommendation remains blocked until three identical runs keep the exact Revlon One-Step product visually distinctive in the first 10 seconds.[unverified]

The model pages carry a Commercial use label, but AIVP still needs written confirmation covering monetised YouTube and affiliate advertising, input ownership, output reuse and any model-specific restrictions.[1][2]

## Outreach

fal publishes `press@fal.ai` in an official company blog post.[5]

Outreach is directed there as a documented press contact, with a request to route affiliate questions to the proper official programme owner.[unverified]

No address was guessed and no web form was submitted.[unverified]

## Candidate delta disposition

- **fal MiniMax H3 Max scheduled pricing reset:** QUALIFIED and staged.
- **Social Media Examiner Seedance filmmaking article:** excluded; educational coverage of an existing model, not a launch or material vendor change.[7]
- **aztro LTX-2.5 Iara v2 LoRA:** conditional 6/10 but excluded by the immediate-access gate; private-person identity/audio adapter, no inference provider or explicit licence.[8]
- **Yi30 Wan2.2 T2V 2layer:** conditional 6/10 but excluded by the immediate-access and evidence gates; copied upstream card, unexplained two-layer extract, no sample or inference provider.[9]

## Outreach result

The validated standing-policy message was delivered to `press@fal.ai`. Resend message ID: `e0ed176a-dee0-42ad-9c4a-0dd22eba6091`; sender, recipient and subject passed provider read-back verification.[unverified]

## Next action

Request a billing-effective timestamp, bounded review credits, commercial-rights clarification and affiliate-program routing. Do not spend credits. If access is granted at no cost, execute the locked three-run case study.

## Sources

[1] https://fal.ai/models/minimax/h3-max/text-to-video — MiniMax H3 Max Text to Video API on fal
[2] https://fal.ai/models/minimax/h3-max-turbo/image-to-video — H3 Max Turbo Image to Video API on fal
[3] https://fal.ai/models/minimax/h3-max/reference-to-video — H3 Max Reference to Video API on fal
[4] https://platform.minimax.io/docs/guides/pricing-paygo — MiniMax Pay as You Go Pricing
[5] https://blog.fal.ai/fal-and-aws-building-for-the-next-phase-of-generative-media — fal and AWS — official press contact
[6] https://startupfortune.com/minimaxs-h3-max-video-model-topped-sora-and-veo-then-its-price-quadrupled — Startup Fortune report on H3 Max pricing
[7] https://www.socialmediaexaminer.com/how-to-think-like-a-filmmaker-ai-video-with-seedance — How to Think Like a Filmmaker: AI Video With Seedance
[8] https://huggingface.co/aztro/ltx-2.5-iara-v2-lora — LTX-2.5 Iara v2 LoRA
[9] https://huggingface.co/Yi30/Wan2.2-T2V-2layer — Wan2.2 T2V 2layer
