# Research Dossier: TechnoBaptist ASMR Trigger Audio H3 LoRA

**Status:** EXCLUDED — explicit duplicate of an already assessed conditional candidate
**Discovery date:** 2026-09-20
**Contract materiality score:** 1 (below threshold 8)
**Gate 1 score:** 3/10 — MONITOR ONLY

## Search strategy and deduplication

The deterministic Hugging Face monitor surfaced `TechnoBaptist/asmr-trigger-audio-h3-lora`, created on 2026-09-19.[1]

The desk checked the model page, API metadata and commit history against the previously assessed `vpakarinen/asmr-trigger-audio-h3-lora` candidate.[1][2][3]

## Gate 1 — launch materiality

The TechnoBaptist repository has one commit titled `Duplicate from vpakarinen/asmr-trigger-audio-h3-lora`, co-authored by the upstream creator.[3]
Its model card, six listed files, MiniMax-H3 adapter relationship, settings, prompt example and creator support links match the upstream repository.[1][2][4]

**Deduplication verdict:** SAME_CANDIDATE as the existing `vpakarinen-asmr-trigger-audio-h3-lora-2026-09-17` assessment.
The duplicate adds no model, workflow, benchmark, licence, hosted creator access or capability event.[1][2][3]

**Gate 1: 3/10 — MONITOR ONLY.**
- **Relevance: 3/3.** It is a MiniMax-H3 text-to-video/image-to-video audio LoRA.[1]
- **Differentiation: 0/3.** The repository explicitly declares itself a duplicate.[3]
- **Launch recency: 0/2.** The new repository is only a copy; the underlying upstream artifact was already assessed from its 2026-09-17 launch.[2][3]
- **Accessibility: 0/2.** The duplicate does not add a self-serve application or documented no-setup inference route; it remains a narrow model adapter rather than an accessible creator product.[1][2]

**Contract score: 1.** Public primary artifact +2 and immediate file access +2, minus 3 for a duplicate/generic repackaging with no differentiator.[1][3]
Below the contract threshold of 8.[3]

## Existing candidate continuity

The upstream vpakarinen candidate remains `conditional_excluded_no_immediate_inference_narrow_audio_adapter` with Gate 1 6/10 and contract score 7. The monitor like-count movement from 11 to 13 is engagement metadata, not a material product event.[2]

The Google News removal of a secondary Krea Agent story is index churn. The existing Krea Agent launch assessment and primary changelog evidence are unchanged.[5]

## Gates 2–4 — skipped

The duplicate failed Gate 1 based on the explicit duplication evidence.[3] No strength scorecard, case study, First Look, outreach draft, affiliate application, test or publication was created.

- **STRENGTH:** EXCLUDED_DUPLICATE
- **CASE_STUDY:** NOT_CREATED_BELOW_THRESHOLD
- **OUTREACH_STATUS:** NOT_ELIGIBLE_BELOW_THRESHOLD
- **AFFILIATE_STATUS:** NONE
- **PUBLICATION_STATUS:** EXCLUDED
- **NEXT_ACTION:** Monitor the canonical vpakarinen repository only; reconsider only for a material capability or accessible inference launch.

## Sources

[1] https://huggingface.co/TechnoBaptist/asmr-trigger-audio-h3-lora — TechnoBaptist duplicate model page
[2] https://huggingface.co/vpakarinen/asmr-trigger-audio-h3-lora — Canonical upstream model page
[3] https://huggingface.co/api/models/TechnoBaptist/asmr-trigger-audio-h3-lora/commits/main — Hugging Face duplicate commit record
[4] https://huggingface.co/api/models/TechnoBaptist/asmr-trigger-audio-h3-lora — Hugging Face duplicate repository metadata
[5] https://www.krea.ai/docs/changelog — Krea official changelog
