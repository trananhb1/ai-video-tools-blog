# Research Dossier: JoaoZaokk LTX-2.3 22B Distilled 1.1 W4A8 ConvRot

**Status:** Newly published community quantization; publisher artifacts and benchmark only; no AIVP run  
**Release date:** 2026-09-14  
**Discovery date:** 2026-09-14  
**Contract materiality score:** 15 — QUALIFIED  
**Gate 1 score:** 8/10 — QUALIFIED  
**Content type:** First Look only

## Search strategy and deduplication

The Hugging Face monitor surfaced `JoaoZaokk/LTX-2.3-22B-distilled-1.1-W4A8-ConvRot`. The desk checked the model card, complete recursive tree metadata, copied licence, official Lightricks base-model card, linked benchmark repository and publisher profile.[1][2][3][4][5][6]

This is not a new foundation model: Lightricks' LTX-2.3 repository predates this upload. It is also not a mirror. The publisher says 1,440 transformer linear layers were re-encoded from BF16 into ComfyUI `asym_w4a8_int8`, while the video VAE, audio VAE, vocoder and text projection were retained byte-for-byte.[1][4]

An earlier third-party INT4 ConvRot transformer exists, so four-bit LTX-2.3 itself is not novel.[8] This release is differentiated by its W4A8 activation path, single-file audio-video checkpoint, matched BF16/W4A8/W4A4/Q6_K evidence, saved-conditioning control and LoRA output tests.[1][5]

The new Google News item is a refreshed seasonal YouCam Video article, not a product launch. Its canonical page still labels itself 2025, describes existing filters/effects and calls Face Swap newly released without a dated release announcement.[7]

## Materiality

**Contract score 15 — threshold met.** Launch within 72 hours +3; no existing AIVP page +3; ungated downloadable artifact +3; underlying LTX-2.3 supports local audio-video generation and the release includes a product-themed LoRA test +2 for product-reference relevance pending verification; explicit commercial-use framework +2; primary repository evidence +2.[1][3][4]

No affiliate, transactional-demand or broad AU-SMB points are awarded. The specialist GPU and storage requirements prevent ordinary creator accessibility.

**Gate 1: 8/10 — QUALIFIED.** Relevance 3/3; differentiation 2/3 because this is a measured deployment derivative rather than a new model; recency 2/2; accessibility 1/2 because the artifact is public and ungated but no inference provider serves it and the demonstrated path requires RTX 3090/3080 Ti hardware plus specialist ComfyUI tooling.[1]

## Primary findings

The repository's single-file checkpoint is 16,651,422,654 bytes (15.51 GiB), with LFS SHA-256 `e1d14f103f094882139ddd9b79284ce649245364df17e4c9c491656c3906c866`.[2] At assessment time, Hugging Face marked its Protect AI and JFrog scans queued and its antivirus, pickle-import and VirusTotal scans unscanned, so independent execution is security-blocked.[2]

The publisher reports one 249-frame, 512×512, 25 fps, eight-step, seed-1234 audio-video comparison on an RTX 3090. W4A8's sampling loop took 18 seconds and its whole run 208 seconds; its picture measured 10.39 MAE, 21.89 dB PSNR and 0.829 SSIM versus BF16. The 6-bit Q6_K arm was closer to BF16 at 3.59 MAE, 29.00 dB PSNR and 0.941 SSIM, but sampled in 40 seconds.[1]

For audio, W4A8 and Q6_K both measured 0.163 log-mel L1 against BF16, with 0 ms reported lag.[1] The publisher explicitly limits the result to one prompt, one seed, one resolution, one frame rate and one card, and says these distances are not human quality judgements or an audio-video synchrony measure.[1]

The same repository includes four LoRA output clips and reports that a commercial-product LoRA affected the rendered headphone scene. That is useful workflow evidence but does not verify exact ASIN preservation, first-frame product identity or repeatability.[1][2]

## Access, rights, cost and host feasibility

The LTX-2 Community License grants a royalty-free limited licence subject to its restrictions, requires entities with at least US$10 million in annual revenue to obtain a paid commercial licence, says Lightricks claims no rights in generated output, and requires machine-generated disclosure.[3] This is not legal advice; archive and re-check the binding terms before monetized use.

No per-render fee is attached to local weights, but hardware, electricity, setup time and accepted-output cost remain unmeasured. This host has no `nvidia-smi`, 11 GiB RAM and 69GB free disk. It cannot reproduce the publisher's two-GPU workflow safely, and no paid compute or hardware purchase is authorized.

## Strength

**Verified floor 49/100; potential ceiling 100; evidence coverage 49%; confidence C; Weak fit.** The floor recognizes unusually detailed publisher artifacts, synchronized audio-video evidence, explicit settings and controls, a public ComfyUI route, and documented rights.[1][3][4][5]

Exact-product identity, vertical output, human-perceived quality, multi-run reliability, real total setup time, current-host operation and cost per accepted output remain unresolved. No Category Leader or Strong Specialist language is permitted.

The product-affiliate gate remains closed until the LED mask ASIN B0D2XTZN8V is distinctive from frame one through the first 10 seconds in all three bounded runs.

## Contact and decision

The publisher's public GitHub profile publishes no name, company, website, social handle or email.[6] A personal address visible only in commit metadata is not an official-domain published vendor contact. No address was guessed, no form was submitted and no outreach was sent.

OUTREACH_STATUS: HELD_NO_VERIFIED_OFFICIAL_DOMAIN_CONTACT.  
AFFILIATE_STATUS: NONE_FOUND.  
PUBLICATION_STATUS: STAGED_FIRST_LOOK_ONLY; HANDS_ON, SECURITY, PRODUCT_IDENTITY_AND_HOST_FEASIBILITY GATES OPEN.  
NEXT_ACTION: Recheck Hugging Face security scans; if they clear and a no-cost approved 24GB+ NVIDIA environment becomes available, audit the loader/tooling and run the locked three-run exact-product case study without buying compute.

## Sources

[1] https://huggingface.co/JoaoZaokk/LTX-2.3-22B-distilled-1.1-W4A8-ConvRot — JoaoZaokk LTX-2.3 22B distilled 1.1 W4A8 ConvRot model card
[2] https://huggingface.co/api/models/JoaoZaokk/LTX-2.3-22B-distilled-1.1-W4A8-ConvRot/tree/main?recursive=true&expand=true — Hugging Face model tree, hashes and security scan state
[3] https://huggingface.co/JoaoZaokk/LTX-2.3-22B-distilled-1.1-W4A8-ConvRot/blob/main/LICENSE_LTX_2_COMMUNITY.txt — LTX-2 Community License Agreement
[4] https://huggingface.co/Lightricks/LTX-2.3 — Official Lightricks LTX-2.3 model card
[5] https://github.com/JoaoZaokk/comfy-quant-bench — JoaoZaokk comfy-quant-bench repository
[6] https://api.github.com/users/JoaoZaokk — Public GitHub profile metadata for JoaoZaokk
[7] https://www.perfectcorp.com/consumer/blog/video-editing/video-filters-for-halloween-tiktok — Perfect Corp YouCam Halloween filter article
[8] https://huggingface.co/Winnougan/INT4-Convrot-Comfy-Models/blob/main/ltx-2.3-22b-distilled-1.1_transformer_only-int4_convrot.safetensors — Earlier LTX-2.3 INT4 ConvRot transformer artifact
