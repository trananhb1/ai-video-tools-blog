# Research Dossier: Microsoft Clipchamp Video Super Resolution

**Observed:** September 22, 2026, 22:15 CEST
**Event date:** September 21, 2026
**Status:** QUALIFIED — First Look only; no AIVP hands-on run
**Source strategy:** Resolved the Google News report to Clipchamp’s official launch tutorial, checked Microsoft Support for availability/workflow limitations, Microsoft Learn for the underlying Windows VSR surface, and the official company page for product ownership and AU provenance.

## Gate 1 — Launch Materiality

**Gate 1 score: 9/10 — QUALIFIED**

- Relevance: **3/3** — directly enhances and edits video inside Clipchamp.[1][2]
- Differentiation: **2/3** — local, in-editor upscaling with reversible originals and queued multi-clip processing is useful, but AI upscaling is not a new category.[1][2]
- Recency: **2/2** — Clipchamp published the feature on September 21, within 72 hours of this run.[1]
- Accessibility: **2/2** — available now in the Windows desktop app for personal, work and school accounts on supported Windows 11 hardware; not available in the browser.[1][2]

**Contract score: 15 (threshold 8).** Recency +3, primary source +2, hands-on access available now +3, AU creator/SMB fit +2, likely reader impact +2, transactional search intent +3. No press-release-only penalty applies because official instructions and live availability are documented.[1][2]

## Verified current state

Clipchamp says Video Super Resolution creates a higher-resolution copy locally, offers 480p, 720p, 1080p and 4K targets where higher than the source, and cannot recover detail absent from the original.[1] Microsoft Support documents reversible originals, multi-clip queues, device-dependent availability and variable results based on source resolution, compression and content.[2]

The feature is Windows-desktop-only and hardware-dependent. The Clipchamp launch post says compatible Windows 11 CPUs or Copilot+ NPUs may be used, while the Microsoft Learn API page describes its current developer VSR surface as requiring a Copilot+ PC; exact device coverage must be tested rather than inferred.[1][3]

The new Hugging Face upload `pepsibox2740/optima-tools-ai-medium` is not a new model: its card states it redistributes unchanged Wan2.2-TI2V-5B files for an Optima-Tools hardware profile, requiring Windows x64, 16 GB VRAM minimum, 48 GB RAM and 45 GB disk.[5] Gate 1: relevance 3, differentiation 0, recency 2, accessibility 1 = **6/10 CONDITIONAL**, excluded because immediate compatible hands-on access is not established. The MiniMax-H3 ControlNet like increase 14→16 is metadata-only engagement churn, not a product event.[6]

## Gate 2 — Strength classification

**Verified floor:** 28/100
**Potential ceiling:** 100/100
**Evidence coverage:** 28%
**Confidence:** C — primary documents only
**Classification:** Monitor only pending controlled upscaling tests

No output-quality, timing, repeatability, accepted-output cost or product-detail preservation points are awarded without saved runs.

## Gate 3 — Case study

**CASE_STUDY:** PLANNED_NOT_RUN. Test whether Clipchamp can upscale the same rights-cleared 720p vertical affiliate-product clip to 1080p three times, with product identity intact in the first 10 seconds, no invented label/control details, median processing at most five minutes, and zero incremental spend.

## Gate 4 — outreach and publication

**OUTREACH_STATUS:** HELD_NO_VERIFIED_PUBLISHED_EMAIL. Official surfaces exposed support/contact UI, but this run found no published Microsoft/Clipchamp press, partnerships or affiliate email suitable for the standing policy.[4] No address was guessed, no form submitted, no manifest created and no email sent.

**AFFILIATE_STATUS:** NONE_VERIFIED_NOT_APPLIED. No Clipchamp-specific affiliate programme or tracking route was verified; no affiliate CTA is permitted.

**PUBLICATION_STATUS:** STAGED_FIRST_LOOK_ONLY. Review language is blocked until an artifact-backed run exists; publication is not approved from docs alone.

**NEXT_ACTION:** On a compatible Windows 11 device, run the locked no-cost three-run fixture and record inputs, outputs, timings, screenshots, hashes and frame QC. Stop before any subscription, paid feature, credential/2FA or terms escalation.

## Sources

[1] https://clipchamp.com/en/blog/how-to-upscale-video-windows/ — Clipchamp launch tutorial
[2] https://support.microsoft.com/en-us/clipchamp/how-to-upscale-videos-with-video-super-resolution — Microsoft Support
[3] https://learn.microsoft.com/en-us/windows/ai/apis/video-super-resolution — Microsoft Learn VSR API
[4] https://clipchamp.com/en/company/ — Microsoft Clipchamp company page
[5] https://huggingface.co/pepsibox2740/optima-tools-ai-medium — Optima-Tools model card
[6] https://huggingface.co/alibaba-pai/MiniMax-H3-Fun-Controlnet-Union-2.0 — existing MiniMax model card
