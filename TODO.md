# Early Review Desk Todo Ledger

**Job ID:** `aivp-early-review-desk`
**Repository:** `/home/tom/aivideopicks-worktrees/early-review-desk`
**Branch:** `automation/early-review-desk`
**Run:** `tick-20260924T0615+0200`
**Task type:** Continuation
**Harness:** `task-transition-harness`; direct execution by Antigravity worker.

## Completed continuation
- [x] Inspect current branch (`automation/early-review-desk`), git status, authoritative contract (`aivp-ai-video-market.json`), recent commit history (`c0affa8`), monitor state/output (`monitor_last_output.txt`), and pending artifacts.
- [x] Identify genuinely new monitor delta since commit `c0affa8`: `RunningHubAI/rh-10eros-max-h3-fl2va-pruned-int8-convrot-unet`, `AmateurGuy23/Wan2.1-T2V-14B`, and `RunningHubAI/rh-anima-snowstyle-remix-unet` from Hugging Face text-to-video models.
- [x] Verify primary sources: model cards, raw READMEs, API endpoints, commit histories, author attribution, and upstream model lineages.
- [x] Evaluate Gate 1 materiality:
  - `RunningHubAI/rh-10eros-max-h3-fl2va-pruned-int8-convrot-unet`: Gate 1 score 6/10; contract score 4 (< 8 threshold); MONITOR ONLY / excluded due to pruned INT8 UNET safetensors export format, lack of standalone consumer interface, unspecified upstream commercial grant, and zero turnkey Australian creator access.
  - `AmateurGuy23/Wan2.1-T2V-14B`: Gate 1 score 3/10; contract score 0 (< 8 threshold); MONITOR ONLY / excluded as an exact duplicate mirror of the February 25, 2025 upstream `Wan-AI/Wan2.1-T2V-14B` foundation model.
  - `RunningHubAI/rh-anima-snowstyle-remix-unet`: Gate 1 score 6/10; contract score 4 (< 8 threshold); MONITOR ONLY / excluded due to anime illustration UNET export format, lack of standalone consumer interface, unspecified upstream commercial grant, and zero turnkey Australian creator access.
- [x] Deduplicate prior work: deduplicate `AmateurGuy23/Wan2.1-T2V-14B` into upstream Wan2.1; re-verify `longxiaooo/StreamLTX` (retained as excluded monitor-only signal, 0 bytes stored, weights coming soon), and `Adobe / Topaz Labs` transaction completion (Forbes secondary coverage deduplicated into primary Sept 23 announcement, retained as excluded strategic M&A signal).
- [x] Retain existing staged candidates (`Google Vids Gemini Omni 1.1 Flash`, `Synthesia Dubbing 2.0`, `Microsoft Clipchamp Video Super Resolution`, `alibaba-pai/MiniMax-H3-Fun-Controlnet-Union-2.0`) without duplicating candidate work.
- [x] Stage standard triage artifact (`tick-20260924T0615-triage.md`) and citation ledger (`tick-20260924T0615-citation-ledger.json`).
- [x] Verify citations with `sources.py --strict` (94% provenance coverage, citations OK).
- [x] Update authoritative contract state atomically (`aivp-ai-video-market.json`) and profile todo ledger (`f7aa2568c535.json`).
- [x] Validate JSON syntax, inspect diff, commit and push to `automation/early-review-desk`.

## Current outcome
Qualified: 0 | Staged: 0 | Tested: 0 | Applied: 0 | Sent: 0 | Delivered: 0 | Queued: 0 | Bounced: 0 | Held: 0 | Excluded: 3 (RunningHubAI/rh-10eros-max-h3-fl2va-pruned-int8-convrot-unet, AmateurGuy23/Wan2.1-T2V-14B, RunningHubAI/rh-anima-snowstyle-remix-unet) | Published: 0 | Cost-blocked: 0 | Deduplicated: 3 (AmateurGuy23 duplicate mirror into Wan2.1; longxiaooo/StreamLTX unreleased weights retained; Forbes Adobe/Topaz secondary coverage deduplicated into primary completion).

`RunningHubAI/rh-10eros-max-h3-fl2va-pruned-int8-convrot-unet` (19,996 MiB MiniMax-H3 FL2VA pruned INT8 convrot UNET safetensors checkpoint exported by @T8star-Aix) and `RunningHubAI/rh-anima-snowstyle-remix-unet` (5,367 MiB anima anime illustration UNET safetensors checkpoint exported by @十二雪) provide raw model weights for ComfyUI or paid RunningHub cloud execution, with no standalone consumer product interface, unspecified upstream commercial rights, and zero turnkey Australian creator access. Gate 1: 6/10; contract score: 4/8 (< 8 threshold). MONITOR ONLY.
`AmateurGuy23/Wan2.1-T2V-14B` is an exact community duplicate mirror of the official February 25, 2025 Wan2.1 foundation model. Gate 1: 3/10; contract score: 0/8. EXCLUDED.

## Next action
Revisit `RunningHubAI/rh-10eros-max-h3-fl2va-pruned-int8-convrot-unet` and `RunningHubAI/rh-anima-snowstyle-remix-unet` on 2026-09-30 or sooner if an independent standalone consumer tool, hosted free creator Space/web app, or explicit commercial license appears; retain staged candidates (`Google Vids Gemini Omni 1.1 Flash`, `Synthesia Dubbing 2.0`, `Microsoft Clipchamp Video Super Resolution`, `alibaba-pai/MiniMax-H3-Fun-Controlnet-Union-2.0`).

## Pending / In-Progress Work
- `Google Vids Gemini Omni 1.1 Flash` (`content/drafts/early-review/google-vids-gemini-omni-1-1-flash-2026/`): Staged First Look; outreach held (no dedicated affiliate/creator contact; generic press route rejected); testing pending Australian account rollout verification.
- `Synthesia Dubbing 2.0` (`content/drafts/early-review/synthesia-dubbing-2-external-video-2026/`): Staged First Look; outreach held under 30-day domain cooldown until 2026-10-08; testing pending zero-cost account estimate and rights clearance.
- `Microsoft Clipchamp Video Super Resolution` (`content/drafts/early-review/microsoft-clipchamp-video-super-resolution-2026/`): Staged First Look; outreach held (no compliant press/partnerships contact).
- `alibaba-pai/MiniMax-H3-Fun-Controlnet-Union-2.0`: Staged First Look; outreach held (validator domain mismatch), compute cost-blocked.
