# Early Review Desk Todo Ledger

**Job ID:** `aivp-early-review-desk`
**Repository:** `/home/tom/aivideopicks-worktrees/early-review-desk`
**Branch:** `automation/early-review-desk`
**Run:** `tick-20260924T1815+0200`
**Task type:** Continuation
**Harness:** `task-transition-harness`; direct execution by Antigravity worker.

## Completed continuation
- [x] Inspect current branch (`automation/early-review-desk`), git status, authoritative contract (`aivp-ai-video-market.json`), recent commit history (`0191409`), monitor state/output (`monitor_last_output.txt`), and pending artifacts.
- [x] Classify as continuation and initialize todo ledger before substantial work.
- [x] Identify genuinely new monitor delta since tick 1615 (commit `0191409`):
  - Hugging Face:
    - `iknownuting/Sulphur-2-base` (2026-09-24T14:40:10.000Z)
  - Re-verify retained monitor items across Google News, Hugging Face, OpenAI, GitHub:
    - Google News: YouTube Gemini editor, Social Media Examiner, Jang Young-ran, Google Vids, Jake Paul, TBC/AWS, David Warner (x2), Synthesia Dubbing 2.0, Intellectia Google AI tools, Pulse 2.0 Biological Computing, Microsoft Clipchamp.
    - Hugging Face: RunningHub rh-ltx2.3 LoRA, RunningHub rh-ramthrusts UNET, RunningHub rh-wan2.2 UNET, RunningHub rh-anima-aesthetic UNET, memset0 vsqa-preview-14b-200steps, stimi ltx-video-api, Alibaba SparkWan batch, KyleNeverGivesUp FastH3, RunningHub motion LoRA, RunningHub rh-10eros.
    - GitHub: LynnReal-AI/LynnReal-Omni.
- [x] Verify primary sources for new candidate `iknownuting/Sulphur-2-base`: model card, repository weights (187 GB), raw README, license terms (LTX-2.3 Attachment A), prompt enhancer GGUF, ComfyUI workflows, upstream lineage, author attributions, and inference availability.
- [x] Evaluate Gate 1 materiality (0–10 scale, threshold >=8 for full Gate 2–4 artifacts, docs-only labels, no invented tests) and contract scoring:
  - iknownuting/Sulphur-2-base (Gate 1: 6/10, contract score: 4/8 -> MONITOR ONLY / EXCLUDED).
- [x] Deduplicate against existing exclusions and prior models (PocketAiHub Sulphur-2 MLX Q8 from 2026-09-08, TenStrip merges, ComfyUI raw weight derivatives).
- [x] Retain existing staged candidates without duplication (`YouTube Gemini Conversational Video Editor`, `Google Vids Gemini Omni 1.1 Flash`, `Synthesia Dubbing 2.0`, `Microsoft Clipchamp Video Super Resolution`, `alibaba-pai/MiniMax-H3-Fun-Controlnet-Union-2.0`, `LynnReal-Omni`).
- [x] Stage standard triage artifact (`tick-20260924T1815-triage.md`) and citation ledger (`tick-20260924T1815-citation-ledger.json`).
- [x] Verify citations with `sources.py --strict` (96% provenance coverage, zero warnings/errors, citations OK).
- [x] Update authoritative contract state atomically (`aivp-ai-video-market.json`) and profile todo ledger (`f7aa2568c535.json`).
- [x] Validate JSON syntax, inspect diff, commit and push completed tick to `automation/early-review-desk`.

## Current outcome
Qualified: 0 | Staged: 0 | Tested: 0 | Applied: 0 | Sent: 0 | Delivered: 0 | Queued: 0 | Bounced: 0 | Held: 0 | Excluded: 8 (iknownuting/Sulphur-2-base, RunningHub rh-ltx2.3 LoRA, RunningHub rh-ramthrusts UNET, Social Media Examiner newsletter, RunningHub rh-wan2.2 UNET, RunningHub rh-anima-aesthetic UNET, memset0 vsqa-preview-14b-200steps, stimi ltx-video-api gateway wrapper) | Published: 0 | Cost-blocked: 0 | Deduplicated: 5 (iknownuting/Sulphur-2-base into LTX-2.3 fine-tunes / PocketAiHub Sulphur-2 MLX / TenStrip 10Eros family; RunningHub rh-ltx2.3 into LTX LoRA family; RunningHub rh-ramthrusts into ComfyUI / Anima patterns; SparkWan2.2 into SparkDiffusion family; vsqa-preview-14b-200steps into earlier vsqa-preview).

iknownuting/Sulphur-2-base is a 187 GB multi-file repository delivering an uncensored community fine-tune of Lightricks LTX-2.3 for text-to-video and image-to-video with companion GGUF prompt enhancers and ComfyUI workflow files. Readme explicitly notes official inference is coming soon (zero hosted inference or consumer web UI exists). Requires local multi-GPU hardware to run 27-43 GB weights. Repository packages Lightricks LTX-2.3 license whose Attachment A Clause 19 strictly forbids circumvention of technical limitations or content filters, creating a legal contradiction against uncensored branding while upstream commercial rights are restricted (Gate 1: 6/10, contract score: 4/8, MONITOR ONLY).

## Next action
Revisit `iknownuting/Sulphur-2-base` on 2026-09-30 or sooner if official inference or hosted creator spaces appear; retain staged candidates (`YouTube Gemini Conversational Video Editor`, `Google Vids Gemini Omni 1.1 Flash`, `Synthesia Dubbing 2.0`, `Microsoft Clipchamp Video Super Resolution`, `alibaba-pai/MiniMax-H3-Fun-Controlnet-Union-2.0`, `LynnReal-Omni`).

## Pending / In-Progress Work
- `YouTube Gemini Conversational Video Editor` (`content/drafts/early-review/youtube-gemini-conversational-video-editor-2026/`): Staged First Look; outreach held (no compliant dedicated creator contact; generic press route held); testing pending Australian account rollout verification.
- `Google Vids Gemini Omni 1.1 Flash` (`content/drafts/early-review/google-vids-gemini-omni-1-1-flash-2026/`): Staged First Look; outreach held (no dedicated affiliate/creator contact; generic press route rejected); testing pending Australian account rollout verification.
- `Synthesia Dubbing 2.0` (`content/drafts/early-review/synthesia-dubbing-2-external-video-2026/`): Staged First Look; outreach held under 30-day domain cooldown until 2026-10-08; testing pending zero-cost account estimate and rights clearance.
- `Microsoft Clipchamp Video Super Resolution` (`content/drafts/early-review/microsoft-clipchamp-video-super-resolution-2026/`): Staged First Look; outreach held (no compliant press/partnerships contact).
- `alibaba-pai/MiniMax-H3-Fun-Controlnet-Union-2.0`: Staged First Look; outreach held (validator domain mismatch), compute cost-blocked.
- `LynnReal-AI/LynnReal-Omni`: Staged First Look; outreach held (hardware/storage cost blocked).
