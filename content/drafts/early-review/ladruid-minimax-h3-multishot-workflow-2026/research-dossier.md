# Research Dossier: LaDruid/MiniMax-H3-Multishot-Workflow

**Status:** EXCLUDED — duplicate community workflow mirror; not a standalone product
**Discovery date:** 2026-09-20
**Contract materiality score:** 0 (excluded)
**Gate 1 score:** 2/10 — MONITOR ONLY (duplicate exclusion applied before full scoring)

## Search strategy and deduplication

Monitor output on 2026-09-20 surfaced `LaDruid/MiniMax-H3-Multishot-Workflow` on HuggingFace.[1]

The desk retrieved the HuggingFace model card and compared it against previously recorded MiniMax H3 community workflow candidates.[1][2][3]

## Gate 1 — launch materiality

`LaDruid/MiniMax-H3-Multishot-Workflow` is a HuggingFace mirror repository hosting the ComfyUI-H3-Multishot node pack and workflows authored by `jlucasmcrell` (GitHub: https://github.com/jlucasmcrell/ComfyUI-H3-Multishot) and distributed via `joeygambino/MiniMax-H3-Multishot-Workflow` on HuggingFace.[1][2][3]

The repository contents are identical: the ComfyUI-H3-Multishot custom node pack (samplers, loaders, GGUF arch patch), three ready-to-load workflow JSONs (H3_Seamless_Chain_v2.json, H3_Seamless_Chain_CORE.json, H3_Keyframes.json), INSTALL.md, SETTINGS.md, and PROMPTING.md.[1]

**Deduplication verdict:** SAME_CANDIDATE as `joeygambino/MiniMax-H3-Multishot-Workflow` — these are the same workflow pack under a different HuggingFace username hosting the same zip release (v2.7.0 per README).[1][2]

**Gate 1: 2/10 — MONITOR ONLY (excluded before full scoring).**
- **Relevance to AI-video production: 2/3.** ComfyUI workflow chaining MiniMax-H3 for multi-shot video generation is relevant to video production, but it is a community workflow wrapper, not a standalone product.[1]
- **Differentiation: 0/3.** Not differentiated — identical content to existing joeygambino/jlucasmcrell candidate already in desk records.[1][2][3]
- **Launch recency: 0/2.** No new launch event; mirror repository hosting existing content.
- **Accessibility: 0/2.** Requires local ComfyUI installation, GPU hardware (24–32 GB VRAM minimum), and ComfyUI-GGUF + architecture patch. No self-serve SaaS access. Not accessible to an average AU creator without significant hardware and technical setup.[1]

**Exclusion decision: DUPLICATE — no new underlying event. Superseded by existing H3 multishot records (joaozaokk-ltx23-w4a8-convrot-2026, t8star-vdn-minimax-h3-comfy-2026, bunny-h3-conditioning-bridge-2026, yniw-mmh3-2026, yoroll-h3-superfast-yolive-2026, fastvideo-fasth3-v2-gguf-2026).**

## Note on the underlying workflow

The jlucasmcrell/joeygambino ComfyUI-H3-Multishot workflow itself was previously assessed as part of the broader MiniMax H3 community ecosystem. The current version (v2.7.0) adds per-subject voice references across chained shots and ComfyUI 0.34 compatibility. This is a maintenance release of an existing community tool, not a new launch event.

## Gate 2–4 — skipped

Duplicate exclusion applied at Gate 1. No scorecard, case study, or outreach artifacts were created.

**OUTREACH_STATUS:** N/A — EXCLUDED_DUPLICATE
**AFFILIATE_STATUS:** NONE_FOUND
**PUBLICATION_STATUS:** EXCLUDED
**NEXT_ACTION:** No action required. If the underlying jlucasmcrell workflow reaches a major commercial milestone (SaaS product launch, affiliate program), re-evaluate as a new candidate.

## Sources

[1] https://huggingface.co/LaDruid/MiniMax-H3-Multishot-Workflow — LaDruid Hugging Face duplicate
[2] https://huggingface.co/joeygambino/MiniMax-H3-Multishot-Workflow — Canonical Hugging Face distribution
[3] https://github.com/jlucasmcrell/ComfyUI-H3-Multishot — Canonical GitHub repository
