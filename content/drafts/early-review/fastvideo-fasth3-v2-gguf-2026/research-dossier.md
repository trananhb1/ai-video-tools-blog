# Research Dossier: RealRebelAI FastH3 V2 GGUF

**Observed:** September 16, 2026  
**Status:** QUALIFIED — First Look only; no AIVP hands-on run  
**Underlying event:** Public Q4_K_M GGUF conversion of FastVideo FastH3 8-Step V2

## Search strategy and deduplication

The monitor surfaced `realrebelai/FastH3-V2_GGUFs`; the desk checked its model card, Hugging Face metadata and commit history.[1][2][7]

The desk then traced the conversion to FastVideo’s primary V2 checkpoint and checked its release history.[3][4]

The implementation repository and inherited MiniMax licence were checked separately.[5][6]

The GGUF is treated as one new conversion event rather than a new foundation model. The upstream checkpoint was created privately on September 4 and its commit history says public release and GPU validation were still pending on September 8; public quick-start documentation appeared September 15.[4] The GGUF repository and its 19.84GB model file were published September 16.[2][7]

## Gate 1 — launch materiality

**Gate 1 score: 8/10 — QUALIFIED.** Relevance 3/3 because it generates synchronized video and audio; differentiation 2/3 because it packages the complete V2 transformer as a lower-storage GGUF rather than merely copying the upstream file; recency 2/2; accessibility 1/2 because the file is public and ungated, but it still needs ComfyUI-GGUF, a text encoder, video/audio VAEs and suitable GPU hardware.[1][2][3]

**Contract score: 8 — threshold met.** Launch within 72 hours +3; new conversion without an AIVP page +3; primary public artifact +2.[1][2][7]

No hands-on-access, exact-product-reference, affiliate, transactional-intent or measured-reader-impact points were awarded.[1][3]

## Verified capability and constraints

The repository contains one Q4_K_M GGUF whose metadata size is 19,840,127,552 bytes. Its card says it was reconstructed from the full official BF16 V2 transformer rather than the pruned ComfyUI checkpoint and preserves higher-precision projection/conditioning tensors where appropriate.[1][2]

The upstream model is a 35B-parameter BF16 checkpoint trained with data-free DMD2 and VSA-H3 at 80% sparsity. It generates text-conditioned synchronized audio/video with eight transformer forwards, requires the VSA-H3 attention backend and uses scheduler shift 10.[3]

This conversion is not a complete standalone pipeline. Its card requires a separate Qwen3-VL text encoder, MiniMax H3 video VAE and audio VAE, and warns that exact workflow compatibility depends on current ComfyUI MiniMax-H3 and attention/VSA support.[1]

Most importantly for AIVP, FastVideo says FL2VA and Ref2VA were not distilled for this V2 checkpoint. It therefore has no documented exact-product reference input and fails the product-affiliate specificity hard gate before generation.[1][3]

## Strength classification

**Verified floor: 21/100; potential ceiling: 100/100; evidence coverage: 21%; confidence C; classification: Monitor only.** The floor credits the documented local workflow, generation settings, lower storage, Australia-compatible licence and ComfyUI route.[1][2][5]

No output-quality, three-run consistency, end-to-end timing, reliability or accepted-output-cost points are inferred because the primary pages provide no controlled GGUF evidence for those criteria.[1][2][3] No AIVP output was generated.

## Rights and safety boundary

The conversion inherits the MiniMax H3 Community License.[1][3] The licence includes Australia in its applicable territory, says MiniMax claims no rights over outputs, and imposes territorial, attribution, disclosure, acceptable-use and commercial-revenue conditions.[5]

The licence does not clear third-party product images, trademarks or performance claims.[5] Generated product footage would require a clear machine-generation disclosure and could not be presented as physical testing.[5]

## Access, integration and cost gate

No 19.84GB model file or supporting model was downloaded; this host has 63GB free storage and no `nvidia-smi` command. The upstream tested default uses four B200 GPUs, while the conversion card provides no complete GGUF hardware benchmark.[1][3] Integration therefore remains blocked by hardware, storage margin and a mandatory code/dependency/security audit; no paid compute or credits were used.

## Outreach and affiliate decision

FastVideo’s official repository and Hao AI Lab site expose GitHub discussions, Slack/WeChat and documentation, but the retrieved official pages do not publish a press, partnership or affiliate email.[6] Rebel AI’s public Hugging Face and GitHub profiles likewise expose no verified business email.[8][9]

The standing policy prohibits guessed addresses and contact forms. No manifest was created and no message was sent.

**OUTREACH_STATUS:** HELD_NO_VERIFIED_PUBLISHED_CONTACT  
**AFFILIATE_STATUS:** NOT_FOUND  
**PUBLICATION_STATUS:** STAGED_FIRST_LOOK_ONLY_NOT_PUBLISHED  
**NEXT_ACTION:** Monitor for a reference-conditioned FastH3 release or a documented no-cost compatible GPU route; do not allocate production effort to this T2VA-only conversion.[1][3]

## Sources

[1] https://huggingface.co/realrebelai/FastH3-V2_GGUFs — RealRebelAI FastH3 V2 GGUFs
[2] https://huggingface.co/api/models/realrebelai/FastH3-V2_GGUFs — Hugging Face metadata: FastH3 V2 GGUFs
[3] https://huggingface.co/FastVideo/FastVideo-FastH3-8-Step-V2 — FastVideo FastH3 8-Step V2
[4] https://huggingface.co/api/models/FastVideo/FastVideo-FastH3-8-Step-V2/commits/main — FastH3 8-Step V2 commit history
[5] https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE — MiniMax H3 Community License
[6] https://github.com/hao-ai-lab/FastVideo — FastVideo repository
[7] https://huggingface.co/realrebelai/FastH3-V2_GGUFs/commits/main — FastH3 V2 GGUF commit history
[8] https://huggingface.co/realrebelai — Rebel AI Hugging Face profile
[9] https://api.github.com/users/RealRebelAI — RealRebelAI GitHub public profile metadata
