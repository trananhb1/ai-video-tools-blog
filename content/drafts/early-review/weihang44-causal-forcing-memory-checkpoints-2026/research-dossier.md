# Research Dossier: Causal Forcing Memory Checkpoints

**Status:** MONITOR ONLY — below Gate 1 and contract thresholds  
**Discovery date:** September 20, 2026  
**Candidate:** `weihang44/Causal-Forcing-Memory-Checkpoints`  
**Gate 1 score:** 4/10  
**Contract score:** 2/8 threshold

## Search strategy and primary evidence

The deterministic Hugging Face monitor surfaced a same-day public text-to-video repository with zero downloads and zero likes at assessment.[1][4]

The desk checked the repository page, raw README, component notice, API metadata and commit history.[1][2][3]

The repository is a research archive of 127 saved compressor checkpoints from five existing Causal Forcing training runs, plus an unmodified copy of the upstream chunkwise generator.[1][2][3]

## Gate 1 — launch materiality

**Relevance: 2/3.** The artifacts support video-memory-compression research and require a separate generation stack, so they are adjacent to AI-video generation but do not themselves provide a creator workflow.[2]

**Differentiation: 0/3.** This release archives training checkpoints and mirrors an existing upstream generator; it does not claim a new generation model, evaluated creator capability or product launch.[2][3]

**Recency: 2/2.** Hugging Face records creation at 2026-09-20T02:09:00Z, within the 72-hour window.[4][5]

**Accessibility: 0/2.** The archive is approximately 721.6 GB plus a 5.68 GB generator, uses PyTorch Distributed Checkpoint shards, is not a Transformers or Diffusers export, retains cluster-specific paths, and still requires the generator, text encoder, VAE, cache policy and separate inference repository.[2]

**Decision: 4/10 — MONITOR ONLY.** It is not an immediately accessible Australian creator tool and fails the conditional-access requirement.[2]

## Contract materiality

**Score: 2 — below threshold 8.** Primary artifact +2 and launch recency +3 are offset by -3 for repackaging existing model components without a new creator-facing differentiator.[1][2][3]

No current AIVP article fact, commercial right, pricing, transactional intent, affiliate opportunity or product-reference workflow changed.[1][2][3]

The component notice says the upstream generator declares Apache-2.0, but explicitly does not assert a new licence for the separately trained compressor weights. Commercial reuse therefore remains unresolved.[3]

## Gates 2–4 — not opened

Because the retrieved artifact fails Gate 1 and the contract threshold, no strength scorecard, case-study plan, First Look, outreach draft, affiliate application, account action, test or publication was created.[1][2][3]

- **STRENGTH:** `MONITOR_ONLY_BELOW_THRESHOLD`
- **CASE_STUDY:** `NOT_CREATED_BELOW_THRESHOLD`
- **OUTREACH_STATUS:** `NOT_ELIGIBLE_BELOW_THRESHOLD`
- **AFFILIATE_STATUS:** `NONE`
- **PUBLICATION_STATUS:** `EXCLUDED`
- **NEXT_ACTION:** Revisit only if the project ships a materially smaller supported inference package, creator-accessible hosted workflow, explicit compressor-weight licence, or independently evaluated generation capability.
- **Next review date:** September 27, 2026

## Sources

[1] https://huggingface.co/weihang44/Causal-Forcing-Memory-Checkpoints — Causal Forcing Memory Checkpoints model page
[2] https://huggingface.co/weihang44/Causal-Forcing-Memory-Checkpoints/raw/main/README.md — Causal Forcing Memory Checkpoints README
[3] https://huggingface.co/weihang44/Causal-Forcing-Memory-Checkpoints/raw/main/NOTICE.md — Causal Forcing Memory Checkpoints component notice
[4] https://huggingface.co/api/models/weihang44/Causal-Forcing-Memory-Checkpoints — Hugging Face repository metadata
[5] https://huggingface.co/api/models/weihang44/Causal-Forcing-Memory-Checkpoints/commits/main — Hugging Face commit history
