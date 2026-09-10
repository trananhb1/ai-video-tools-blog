# Research Dossier: Marvis AI Studio

**Status:** Same-day launch; vendor-docs-only; no AIVP run  
**Launch date:** 2026-09-10 (Hugging Face repository creation timestamp)  
**Discovery date:** 2026-09-10  
**Contract materiality score:** 15  
**Gate 1 score:** 8/10 — QUALIFIED  
**Content type:** First Look only

## Search strategy and deduplication

The desk inspected the newly created Hugging Face repository/API metadata, the public Marvis service and the builder's dated technical account.[1][2][3]

MiniMax's official H3 announcement and model card were used to check upstream capability and licensing.[4][5][6]

The repository contains only a README and metadata rather than model weights. Marvis is therefore one hosted wrapper/service event around an existing MiniMax H3 derivative, not a new foundation model.[1][4]

The same tick's TaurusDuan upload is already deduplicated to the previously assessed T8star VDN-MiniMax-H3 bundle. Rolling Google News removals are feed-window churn, not new events.

## Materiality

**Contract score: 15 — threshold met.** Launch within 72 hours +3; new tool without an AIVP page +3; immediate no-signup access +3; AU/SMB accessibility +2; transactional intent +3; primary creator source +2; likely reader impact +2; generic-wrapper penalty −3.[1][2][6]

No product-reference, explicit complete-output commercial-rights, or affiliate points were awarded.

**Gate 1: 8/10 — QUALIFIED.** Relevance 3/3; differentiation 1/3 because the service's single-consumer-GPU/no-account delivery is operationally unusual but the generation model is an existing H3 derivative; recency 2/2; accessibility 2/2.[1][2][4]

## Primary findings

Marvis exposes text-to-video only, with selectable 864×480, 1344×768 and 1664×928 resolutions, two-to-ten-second duration, native audio and 24fps output. Its public UI advertises daily free credits and no account or card.[2]

The model card says the service runs an int8 MiniMax H3 derivative plus a Qwen3-VL 32B text encoder through ComfyUI on one RTX 5060 Ti 16GB and allows three generations per IP per day.[1]

The builder reports approximately six minutes for a three-second 864×480 clip, 21 minutes for a five-second 1344×768 clip and 40 minutes for a five-second 1664×928 clip. Those timings are vendor-authored evidence, not AIVP measurements.[3]

The live page exposes JSON generation, task, queue and gallery endpoints in client-side code, but there is no published developer API contract, webhook, uptime commitment or pricing table.[2]

## Product-specificity and rights limits

The public interface accepts text only. It does not expose image, video or product-URL references, so it fails AIVP's exact-product input gate and must not be recommended for ASIN-specific affiliate videos.[2]

The live service says every generated video is the user's, while the repository's CC0 metadata is immediately qualified by a note that MiniMax H3 weights retain their own licence.[1][2]

MiniMax publishes H3 under its Community License Agreement and lists a separate licence application route limited to the USA, EU, UK and South Korea. Australia-specific commercial use of this derivative is therefore unresolved.[5]

## Strength and decision

**Verified floor 22/100; potential ceiling 80; evidence coverage 42%; confidence C; Monitor only.** Verified points cover a low-friction public workflow, limited resolution/duration controls, published self-reported timings, free quota, visible JSON endpoints and broad browser accessibility.[1][2][3]

Output quality, repeatability, actual failure rate and monetized Australian rights remain unresolved. Product-specificity has a structural zero in the current text-only UI, which caps the product-affiliate ceiling below 100.

No official Marvis-domain email was published on the service, model card or builder article. Outreach is HELD rather than guessed or submitted through a form.

OUTREACH_STATUS: HELD_NO_VERIFIED_OFFICIAL_DOMAIN_CONTACT.  
AFFILIATE_STATUS: NO_PROGRAMME_FOUND.  
PUBLICATION_STATUS: STAGED_FIRST_LOOK_ONLY_NOT_PUBLISHABLE_RIGHTS_UNRESOLVED.  
NEXT_ACTION: Obtain a published Marvis contact and Australia-specific H3 commercial-rights confirmation; then run the three no-cost narrative tests. Do not use for product affiliate.

## Sources

[1] https://huggingface.co/erniou86/Marvis-AI-Studio — Marvis AI Studio model card
[2] https://ai.jxzhihi.com/intl — Marvis AI Studio live service
[3] https://dev.to/ernioiu8/i-put-a-paid-ai-video-generator-on-my-own-gaming-gpu-no-cloud-bill-24hk — Builder account of Marvis AI Studio
[4] https://www.minimax.io/news/minimax-h3-open-source — MiniMax H3 open-source announcement
[5] https://huggingface.co/MiniMaxAI/MiniMax-H3 — MiniMax H3 model card and license route
[6] https://huggingface.co/api/models/erniou86/Marvis-AI-Studio — Hugging Face API metadata for Marvis AI Studio
