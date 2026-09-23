# Case Study Plan: Synthesia Dubbing 2.0 External Video

## Business Question
Can Synthesia turn a rights-cleared 30-second AI Video Picks English talking-head tool explainer into a publishable Spanish localization while preserving voice, lip alignment, product terminology, and timing for zero incremental cost?

## Rights-Cleared Input
Use AIVP-owned footage recorded or generated under documented commercial rights. Freeze the source MP4, transcript, glossary, and SHA-256 before Run 1.

## Locked Brief
- Source: one 30-second, 1080x1920, H.264 English talking-head explainer owned by AIVP
- Target: Spanish (Spain)
- Lip sync: on
- Duration: Adaptive
- Glossary: freeze `AI Video Picks`, the named tool, and one product term
- Output: downloadable H.264 MP4, 1080x1920 where available
- No transcript or settings changes between runs
- Three identical runs using the same account tier and tool version

## Success Criteria
- All three runs complete without error.
- Brand/tool terms are correct in all outputs.
- Speaker identity remains recognizably consistent by blinded A/B voice check.
- Lip sync has no material drift in sampled first, middle, and final speaking frames.
- Total duration differs from source by no more than 15%.
- Each output is usable without timeline re-editing.
- UI estimate confirms zero charge and no paid-credit consumption before every run.
- Commercial use for monetized AIVP publishing is confirmed in current terms or writing.

## Failure and Stop Conditions
- Stop before generation if the UI shows a charge, paid-credit use, upgrade, or financial commitment.
- Stop if source rights or commercial-output rights are unresolved.
- Stop at any password, 2FA, identity, payment, or signature gate requiring Tom.
- Stop after two failed runs or unexpected settings drift.
- Product/brand terminology failure in two runs is a case-study failure.

## Three Runs and Evidence Package
For Runs 1-3 save source and output MP4s; tool/version/date; all settings; before/after screenshots; transcript/glossary; estimated and actual credits; upload, queue, render, and total seconds; errors; SHA-256 for source, settings, and output; first/mid/final frame QC; voice and terminology notes; watermark state; and rights evidence.

## Control
Use the same source and target language in the current no-cost baseline localization workflow. Record time, cost, terminology errors, lip-sync verdict, and edit minutes. Compute deltas only from measured values.

## Outcome
`NOT_RUN` — authentication, zero-cost estimate, and rights gates remain unresolved. Handoff to vendor-tool-automation only after those gates pass.
