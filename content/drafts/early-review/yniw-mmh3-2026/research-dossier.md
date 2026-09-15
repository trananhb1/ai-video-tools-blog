# Research Dossier: yniw/mmh3 + MiniMax-H3-mmh3

**Status:** QUALIFIED — First Look only; repository evidence, no AIVP hands-on run  
**Release date:** 2026-09-13  
**Discovery date:** 2026-09-15  
**Contract materiality score:** 8  
**Gate 1 score:** 8/10 — QUALIFIED

## Search strategy and deduplication

The desk inspected the new Hugging Face package, its linked `niw/mmh3` repository and repository metadata.[1][2][3]

The desk separately checked the model and software licences plus the publisher’s public profile.[4][5][6]

The Hugging Face files are support weights for the same new `mmh3` inference engine, so they are treated as one underlying release rather than two candidates.[1][2] The newly indexed Visko/Dealroom headline was separately deduplicated against the September 1 Orbis event already staged.

## Gate 1 — launch materiality

`mmh3` is a new Rust/CUDA inference engine dedicated to MiniMax H3 that implements text-to-video with synchronized stereo audio without PyTorch or ComfyUI and writes MP4 or WebM directly.[2] The repository was created September 13, inside the 72-hour window when assessed.[3]

**Gate 1: 8/10 — QUALIFIED.** Relevance 3/3; differentiation 3/3 for the dedicated framework-free runtime and native encoded output; recency 2/2; accessibility 0/2 because the verified path requires Linux, CUDA 13 and an NVIDIA Blackwell GPU, has no inference provider, and this host has no NVIDIA runtime.[1][2]

**Contract score: 8 — threshold met.** Launch within 72 hours +3; new tool without an AIVP page +3; primary repository evidence +2. No points were awarded for current hands-on access, product references, explicit universal rights, AU SMB practicality, affiliate economics or measured reader impact.

## Documented capability

The publisher reports one complete 5.2-second, 1344×768 MP4 generation with stereo audio on a DGX Spark in 86.29 seconds and one WebM run in 90.88 seconds; these are individual publisher runs, not averages or AIVP tests.[2]

The engine exposes prompt, seed, sampler, attention, patch and LoRA controls, validates output before model loading, and includes stage-level comparison tools against ComfyUI.[2] Its companion package adds a 2.70GB FastH3 patch and 2.80GB INT8 ConvRot video VAE, with publisher-reported held-out decode fidelity of about 60.9 dB PSNR against FP16.[1]

Important limitations are explicit: only one-at-a-time T2VA is complete; first/last-frame conditioning, reference conditioning, HTTP serving and Apple Silicon are not implemented.[2] The full model set needs about 55GB of disk, while this workspace currently has about 68GB free, leaving too little safe margin for an unapproved integration download.

## Strength classification

**Verified floor: 28/100; potential ceiling: 100/100; evidence coverage: 28%; confidence C; classification: Monitor only.** The floor credits documented CLI/export workflow, controls, publisher timing/accuracy evidence, open-source software terms and an Australia-compatible model territory.[2][4][5]

No output-quality, exact-product, multi-run reliability or accepted-output-cost claim is treated as hands-on evidence. Reference conditioning is not implemented, so `mmh3` currently fails AIVP’s product-affiliate specificity gate.[2]

## Commercial rights and safety boundary

The engine code is MIT licensed.[5] The support weights use the MiniMax H3 Community License, which excludes the EU, UK, Republic of Korea and United States but not Australia, says MiniMax claims no rights over generated outputs, imposes attribution/disclosure and acceptable-use duties, and requires separate authorization above its stated commercial-revenue threshold.[4]

Those terms do not establish rights to any third-party input, likeness, trademark or generated content. AIVP must use rights-cleared references and disclose machine-generated publication; no product-performance claim may be inferred from generated footage.

## Access, security and cost gate

No model weights were downloaded and no generation was attempted. This host has no `nvidia-smi`; the documented runtime targets Blackwell GPUs and the companion package has no inference provider.[1][2] Stage 2 vendor-integration security audit and three-run testing therefore remain blocked by hardware/access and storage risk, with no spend authorized.

## Outreach and affiliate decision

The publisher’s official GitHub profile exposes no public email, company or website, and the project publishes no press, partnership or affiliate address.[6] The standing policy prohibits guessing an address or using forms, so outreach is held and no message was sent.

OUTREACH_STATUS: HELD_NO_VERIFIED_PUBLISHED_CONTACT.  
AFFILIATE_STATUS: NOT_FOUND.  
PUBLICATION_STATUS: STAGED_FIRST_LOOK_ONLY_NOT_PUBLISHABLE.  
NEXT_ACTION: Monitor for reference-conditioning support or a zero-cost Blackwell inference route; then complete a code/security audit before three exact-product runs.

## Sources

[1] https://huggingface.co/yniw/MiniMax-H3-mmh3 — MiniMax H3 files for mmh3
[2] https://github.com/niw/mmh3 — niw/mmh3 repository
[3] https://api.github.com/repos/niw/mmh3 — GitHub repository metadata for niw/mmh3
[4] https://huggingface.co/yniw/MiniMax-H3-mmh3/raw/main/LICENSE — MiniMax H3 Community License
[5] https://github.com/niw/mmh3/blob/master/LICENSE — mmh3 MIT License
[6] https://api.github.com/users/niw — GitHub public profile for niw
