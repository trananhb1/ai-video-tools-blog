# Research Dossier: JoaoZaokk LTX-2.5 22B Distilled W4A8 ConvRot

**Status:** Newly published community quantization; publisher benchmark only; no AIVP run  
**Release date:** 2026-09-13  
**Discovery date:** 2026-09-13  
**Contract materiality score:** 15 — QUALIFIED  
**Gate 1 score:** 8/10 — QUALIFIED  
**Content type:** First Look only

## Search strategy and deduplication

The Hugging Face monitor surfaced `JoaoZaokk/LTX-2.5-22B-distilled-W4A8-ConvRot`. The desk checked the model card, recursive file metadata and copied LTX-2.x licence.[1][2][3]

The official Lightricks base-model card, linked benchmark repository and publisher public profile were checked separately.[4][5][6]

This is not a new foundation model and not a mirror. It is a newly quantized derivative of Lightricks LTX-2.5: the publisher says 1,440 linear layers were re-encoded from BF16 to ComfyUI `asym_w4a8_int8`, with no fine-tuning or architecture change.[1] The underlying LTX-2.5 model already supports synchronized video/audio from text, image and video inputs.[4]

The current Google News Kling URL is another route for the already-recorded February 2026 Kling 3.0 promotional reissue, not a new event. All deterministic monitor sources returned `ok`; inherited invalid contract routes remain coverage gaps, so the global cutoff is not advanced.

## Materiality

**Contract score 15 — threshold met.** Launch within 72 hours +3; no existing AIVP page +3; public ungated artifact available now +3; product-reference relevance inherited from LTX-2.5 image/video conditioning +2; explicit commercial-use framework +2; primary repository evidence +2.[1][3][4]

No points are awarded for affiliate economics, broad AU-SMB fit, transactional demand or AIVP hands-on evidence. The 24GB-class GPU requirement keeps this specialist workflow outside ordinary creator accessibility.

**Gate 1: 8/10 — QUALIFIED.** Relevance 3/3 because it deploys an image/video-conditioned video model; differentiation 2/3 because the 4-bit artifact includes a matched three-arm benchmark rather than only repackaging weights; recency 2/2; accessibility 1/2 because the repository is ungated but the demonstrated path needs an RTX 3090-class 24GB card and additional LTX components.[1][4]

## Primary findings

The repository contains a 12,520,267,816-byte transformer with LFS SHA-256 `df0c2f1350aa9c34d2c7417d82d29522f7cd35ab7758986b65f8bc08291e08ae`, a sidecar, a comparison image, a licence and a model card. The large model file's Hugging Face supply-chain scans were still queued or unscanned when assessed; that blocks execution before an independent file and code audit.[2]

The publisher reports one matched 249-frame, 512×512, three-step, seed-1234 run on an RTX 3090. In that run, W4A8 used 11.66 GiB and rendered in 400.9 seconds versus BF16 at 39.13 GiB and 780.7 seconds; however, W4A8 was less faithful than Lightricks INT8, with 25.39 dB versus 29.71 dB PSNR against BF16.[1] These are publisher measurements from one prompt, one seed, one resolution and one GPU—not independent AIVP results.[1]

The publisher explicitly says the audio branch was not decoded and provides no perceptual preference study or multi-seed sweep.[1] The linked benchmark code is MIT licensed, but the checkpoint remains governed by the LTX-2.x Community License.[3][5]

## Access, rights, cost and host feasibility

The LTX licence grants royalty-free production/commercial use below the stated US$10 million entity-wide annual-revenue threshold and says Lightricks claims no rights in generated outputs, subject to its restrictions and disclosure obligations.[3][4] AIVP has not made a legal determination; the binding licence and current acceptable-use policy must be archived again before any monetized publication.

There is no per-render vendor fee for local use documented here, but compatible hardware, electricity, setup and accepted-output cost are unmeasured. The current host has no `nvidia-smi`, 11 GiB RAM and 72GB free disk. It cannot reproduce the demonstrated RTX 3090 path, and no paid GPU compute or hardware purchase is authorized.

## Strength

**Verified floor 44/100; potential ceiling 100; evidence coverage 44%; confidence C; Weak fit.** The floor recognizes reference-input capability, one documented benchmark, explicit controls, a public ComfyUI artifact, clear rights terms and a reproducible integration route.[1][3][4]

Exact-product identity, 9:16 output, audio, repeatability, failure rate, current-host operation and real cost per accepted output remain unresolved. No Category Leader or Strong Specialist language is permitted.

The product-affiliate gate remains closed until the LED mask ASIN B0D2XTZN8V is distinctive from frame one through the first 10 seconds in all three bounded runs.

## Contact and decision

The public GitHub profile publishes no name, company, website or email.[6] A personal address visible only in commit metadata is not an official-domain published vendor contact and is not eligible under the standing policy. No address was guessed, no form was submitted and no outreach was sent.

OUTREACH_STATUS: HELD_NO_VERIFIED_OFFICIAL_DOMAIN_CONTACT.  
AFFILIATE_STATUS: NONE_FOUND.  
PUBLICATION_STATUS: STAGED_FIRST_LOOK_ONLY; HANDS_ON, SECURITY, PRODUCT_IDENTITY_AND_HOST_FEASIBILITY GATES OPEN.  
NEXT_ACTION: Wait for a no-cost audited 24GB NVIDIA environment or independently repeated multi-seed evidence; then run the locked three-run exact-product case study without purchasing compute.

## Sources

[1] https://huggingface.co/JoaoZaokk/LTX-2.5-22B-distilled-W4A8-ConvRot — JoaoZaokk LTX-2.5 22B distilled W4A8 ConvRot model card
[2] https://huggingface.co/api/models/JoaoZaokk/LTX-2.5-22B-distilled-W4A8-ConvRot/tree/main?recursive=true&expand=true — Hugging Face model tree and file metadata
[3] https://huggingface.co/JoaoZaokk/LTX-2.5-22B-distilled-W4A8-ConvRot/blob/main/LICENSE_LTX_2x_COMMUNITY.txt — LTX-2.x Community License Agreement
[4] https://huggingface.co/Lightricks/LTX-2.5 — Official Lightricks LTX-2.5 model card
[5] https://github.com/JoaoZaokk/comfy-quant-bench — JoaoZaokk comfy-quant-bench repository
[6] https://api.github.com/users/JoaoZaokk — Public GitHub profile metadata for JoaoZaokk
