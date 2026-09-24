# Early Review Desk Todo Ledger

**Job ID:** `aivp-early-review-desk`
**Repository:** `/home/tom/aivideopicks-worktrees/early-review-desk`
**Branch:** `automation/early-review-desk`
**Run:** `tick-20260924T0415+0200`
**Task type:** Continuation
**Harness:** `task-transition-harness`; direct execution by Antigravity worker.

## Completed continuation
- [x] Inspect current branch (`automation/early-review-desk`), git status, authoritative contract (`aivp-ai-video-market.json`), recent commit history (`6eeb0c9`), monitor state/output (`monitor_last_output.txt`), and pending artifacts.
- [x] Identify genuinely new monitor delta since commit `6eeb0c9`: `RunningHubAI/rh-wan-remix-i2v-highnoise-unet` and `RunningHubAI/rh-wan-remix-i2v-lownoise-unet` from Hugging Face text-to-video models.
- [x] Verify primary sources: model cards, raw READMEs, API endpoints, author attribution, and upstream Wan2.2 lineage.
- [x] Evaluate Gate 1 materiality: Gate 1 score 6/10 (relevance 2/3, differentiation 1/3, recency 2/2, accessibility 1/2); contract score 4 (< 8 threshold); MONITOR ONLY / excluded from pipeline due to ComfyUI UNET export format, lack of standalone consumer interface, unspecified upstream commercial grant, and zero turnkey Australian creator access.
- [x] Deduplicate prior work: re-verify `longxiaooo/StreamLTX` (retained as excluded monitor-only signal, 0 bytes stored, weights coming soon), `Adobe / Topaz Labs` transaction completion (Forbes secondary coverage deduplicated into primary Sept 23 announcement, retained as excluded strategic M&A signal), and `memset0/vsqa-preview-14b` (retained as excluded preview checkpoint).
- [x] Retain existing staged candidates (`Google Vids Gemini Omni 1.1 Flash`, `Synthesia Dubbing 2.0`, `Microsoft Clipchamp Video Super Resolution`, `alibaba-pai/MiniMax-H3-Fun-Controlnet-Union-2.0`) without duplicating candidate work.
- [x] Stage standard triage artifact (`tick-20260924T0415-triage.md`) and citation ledger (`tick-20260924T0415-citation-ledger.json`).
- [x] Verify citations with `sources.py --strict` (92% provenance coverage, citations OK).
- [x] Update authoritative contract state atomically (`aivp-ai-video-market.json`) and profile todo ledger (`f7aa2568c535.json`).
- [x] Validate JSON syntax, inspect diff, commit and push to `automation/early-review-desk`.

## Current outcome
Qualified: 0 | Staged: 0 | Tested: 0 | Applied: 0 | Sent: 0 | Delivered: 0 | Queued: 0 | Bounced: 0 | Held: 0 | Excluded: 2 (RunningHubAI/rh-wan-remix-i2v-highnoise-unet, RunningHubAI/rh-wan-remix-i2v-lownoise-unet) | Published: 0 | Cost-blocked: 0 | Deduplicated: 2 (longxiaooo/StreamLTX unreleased weights retained; Forbes Adobe/Topaz secondary coverage deduplicated into primary completion).

`RunningHubAI/rh-wan-remix-i2v-highnoise-unet` and `RunningHubAI/rh-wan-remix-i2v-lownoise-unet` (14B ComfyUI UNET safetensors checkpoint exports fine-tuning Wan2.2 i2v with motion LoRA and fine pose training by community author `@小肥猴` for high and low lighting) provide raw model weights for ComfyUI or paid RunningHub cloud execution, with no standalone consumer product interface, unspecified upstream commercial rights, and zero turnkey Australian creator access. Gate 1: 6/10; contract score 4 (< 8 threshold). MONITOR ONLY pending standalone product or clear commercial grant.

## Next action
Revisit `RunningHubAI/rh-wan-remix-i2v-highnoise-unet` and `RunningHubAI/rh-wan-remix-i2v-lownoise-unet` on 2026-09-30 or sooner if an independent standalone consumer tool, hosted free creator Space/web app, or explicit commercial license appears; retain staged candidates (`Google Vids Gemini Omni 1.1 Flash`, `Synthesia Dubbing 2.0`, `Microsoft Clipchamp Video Super Resolution`, `alibaba-pai/MiniMax-H3-Fun-Controlnet-Union-2.0`).

## Pending / In-Progress Work
- `Google Vids Gemini Omni 1.1 Flash` (`content/drafts/early-review/google-vids-gemini-omni-1-1-flash-2026/`): Staged First Look; outreach held (no dedicated affiliate/creator contact; generic press route rejected); testing pending Australian account rollout verification.
- `Synthesia Dubbing 2.0` (`content/drafts/early-review/synthesia-dubbing-2-external-video-2026/`): Staged First Look; outreach held under 30-day domain cooldown until 2026-10-08.
- `Microsoft Clipchamp Video Super Resolution` (`content/drafts/early-review/microsoft-clipchamp-video-super-resolution-2026/`): Staged First Look; outreach held (no compliant press/partnerships contact).
- `alibaba-pai/MiniMax-H3-Fun-Controlnet-Union-2.0`: Staged First Look; outreach held (validator domain mismatch), compute cost-blocked.
