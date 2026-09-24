# Early Review Desk Todo Ledger

**Job ID:** `aivp-early-review-desk`
**Repository:** `/home/tom/aivideopicks-worktrees/early-review-desk`
**Branch:** `automation/early-review-desk`
**Run:** `tick-20260924T1415+0200`
**Task type:** Continuation
**Harness:** `task-transition-harness`; direct execution by Antigravity worker.

## Completed continuation
- [x] Inspect current branch (`automation/early-review-desk`), git status, authoritative contract (`aivp-ai-video-market.json`), recent commit history (`22971c9`), monitor state/output (`cdbc27f`), and pending artifacts.
- [x] Identify genuinely new monitor delta since commit `22971c9` (tick `tick-20260924T1220+0200`):
  - Hugging Face:
    - `RunningHubAI/rh-ramthrusts-nsfw-pink-alchemy-anima-v2.9-unet` (2026-09-24T11:41:18.000Z)
  - Re-verify retained monitor items:
    - Google News: `Social Media Examiner`, `Google Vids`, `Synthesia Dubbing 2.0`, `Microsoft Clipchamp`, `Jake Paul`, `David Warner`, `TBC/AWS`, `Jang Young-ran`
    - Hugging Face: `Alibaba SparkWan2.2` & `SparkWan2.1` batch, `RunningHub rh-wan2.2` & `rh-anima-aesthetic` UNETs, `memset0/vsqa-preview-14b-200steps`, `stimi/ltx-video-api`, `KyleNeverGivesUp FastH3`, `anonymousopsd-v/OPSD-V`
    - GitHub: `LynnReal-AI/LynnReal-Omni`
- [x] Verify primary sources: resolve redirect/canonical URLs, model cards, raw READMEs, codebases, licensing, API endpoints, author attribution, upstream lineages, and dates.
- [x] Evaluate Gate 1 materiality (0–10 scale, threshold >=8 for full Gate 2–4 artifacts, docs-only labels, no invented tests):
  - RunningHubAI rh-ramthrusts-nsfw-pink-alchemy-anima-v2.9 UNET (Gate 1: 6/10, contract: 4/8 -> MONITOR ONLY / EXCLUDED)
- [x] Deduplicate prior work against existing dossiers and exclusions:
  - Deduplicate RunningHubAI rh-ramthrusts into ComfyUI / RunningHub derivative patterns and Anima family
  - Retain deduplications for SparkWan2.2 into SparkDiffusion family, vsqa-preview-14b-200steps into earlier vsqa-preview, stimi ltx-video-api into third-party gateway wrappers, and Social Media Examiner into prior coverage
- [x] Retain existing staged candidates without duplication (`Google Vids Gemini Omni 1.1 Flash`, `Synthesia Dubbing 2.0`, `Microsoft Clipchamp Video Super Resolution`, `alibaba-pai/MiniMax-H3-Fun-Controlnet-Union-2.0`, `LynnReal-Omni`, etc.).
- [x] Stage standard triage artifact (`tick-20260924T1415-triage.md`) and citation ledger (`tick-20260924T1415-citation-ledger.json`).
- [x] Verify citations with `sources.py --strict` (98% provenance coverage, zero warnings/errors, citations OK).
- [x] Update authoritative contract state atomically (`aivp-ai-video-market.json`) and profile todo ledger (`f7aa2568c535.json`).
- [x] Validate JSON syntax, inspect diff, commit and push completed tick to `automation/early-review-desk`.

## Current outcome
Qualified: 0 | Staged: 0 | Tested: 0 | Applied: 0 | Sent: 0 | Delivered: 0 | Queued: 0 | Bounced: 0 | Held: 0 | Excluded: 7 (RunningHub rh-ramthrusts UNET, Social Media Examiner newsletter, RunningHub rh-wan2.2 UNET, RunningHub rh-anima-aesthetic UNET, memset0 vsqa-preview-14b-200steps, stimi ltx-video-api gateway wrapper, Alibaba SparkWan2.2-T2V-14B-480P sparse attention checkpoint) | Published: 0 | Cost-blocked: 0 | Deduplicated: 4 (RunningHub rh-ramthrusts into ComfyUI / RunningHub derivative patterns; SparkWan2.2 into SparkDiffusion family; vsqa-preview-14b-200steps into earlier vsqa-preview; prior RunningHub UNET checkpoints into ComfyUI patterns).

RunningHub rh-ramthrusts is a 3,988 MiB quantized UNET safetensors checkpoint for ComfyUI / RunningHub cloud execution fine-tuned from circlestone-labs/Anima under CircleStone Labs Non-Commercial License, offering zero turnkey Australian creator access and no standalone consumer UI (Gate 1: 6/10, contract score: 4/8, MONITOR ONLY). Social Media Examiner article is an educational marketing newsletter and industry roundup (Gate 1: 0/10, contract score: 0/8, EXCLUDED). RunningHub rh-wan2.2 and rh-anima-aesthetic are quantized UNET checkpoints for ComfyUI / RunningHub cloud execution with unspecified upstream licensing (Gate 1: 6/10, contract score: 4/8, MONITOR ONLY). memset0 vsqa-preview-14b-200steps is an intermediate unevaluated step-200 training preview deduplicating into earlier VSQA preview (Gate 1: 6/10, contract score: 4/8, MONITOR ONLY). stimi ltx-video-api is an undifferentiated third-party API gateway wrapper on apimodels.app with zero weights (Gate 1: 4/10, contract score: 2/8, MONITOR ONLY). alibabagroup SparkWan2.2-T2V-14B-480P is a raw PyTorch research checkpoint batch deduplicating into the SparkDiffusion family without a consumer web UI (Gate 1: 7/10, contract score: 6/8, MONITOR ONLY).

## Next action
Revisit `RunningHubAI` UNET checkpoints and `SparkWan2.2` / `memset0` research checkpoints on 2026-09-30 or sooner if hosted creator spaces, ComfyUI wrapper nodes, or independent standalone consumer tools appear; retain staged candidates (`Google Vids Gemini Omni 1.1 Flash`, `Synthesia Dubbing 2.0`, `Microsoft Clipchamp Video Super Resolution`, `alibaba-pai/MiniMax-H3-Fun-Controlnet-Union-2.0`, `LynnReal-Omni`).

## Pending / In-Progress Work
- `Google Vids Gemini Omni 1.1 Flash` (`content/drafts/early-review/google-vids-gemini-omni-1-1-flash-2026/`): Staged First Look; outreach held (no dedicated affiliate/creator contact; generic press route rejected); testing pending Australian account rollout verification.
- `Synthesia Dubbing 2.0` (`content/drafts/early-review/synthesia-dubbing-2-external-video-2026/`): Staged First Look; outreach held under 30-day domain cooldown until 2026-10-08; testing pending zero-cost account estimate and rights clearance.
- `Microsoft Clipchamp Video Super Resolution` (`content/drafts/early-review/microsoft-clipchamp-video-super-resolution-2026/`): Staged First Look; outreach held (no compliant press/partnerships contact).
- `alibaba-pai/MiniMax-H3-Fun-Controlnet-Union-2.0`: Staged First Look; outreach held (validator domain mismatch), compute cost-blocked.
- `LynnReal-AI/LynnReal-Omni`: Staged First Look; outreach held (hardware/storage cost blocked).
