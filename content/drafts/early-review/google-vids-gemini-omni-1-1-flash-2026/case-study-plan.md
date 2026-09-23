# AI Video Picks Case-Study Plan — Google Vids Gemini Omni 1.1 Flash

**Status:** PLAN — access, rights, spend, and publication gates apply  
**Candidate classification:** Monitor only (confidence C; primary vendor documentation only)  
**Evidence confidence:** C (primary vendor documentation only)  
**Business question:** Can Google Vids Gemini Omni 1.1 Flash generate and extend a 1080p commercial product B-roll clip of the Blue Yeti USB microphone using Ingredients reference images while preserving product identity, lighting, and audio consistency at zero incremental cost?

## 1. Case-study thesis

Google Vids Gemini Omni 1.1 Flash claims native 1080p full HD generation, super-specific duration controls, and improved scene extension with character and audio consistency. This case study tests whether a creator can produce a clean 1080p commercial product clip and extend it seamlessly by 4 seconds using reference image inputs of an affiliate portfolio product without paying for Vertex AI or Workspace add-ons.

## 2. Real AIVP scenario

- **Audience:** Australian creators, solopreneurs, and SMBs producing marketing and tutorial videos.
- **Affiliate portfolio product:** Blue Yeti USB Microphone (referenced in existing AIVP gear guides via link: `https://amzn.to/4tKJEgb`; no ASIN invented).
- **Mandatory asset rights precondition:** Testing cannot begin until AIVP-owned imagery or explicit supplier asset reuse permission for the Blue Yeti USB microphone is documented.
- **Input:** Two rights-cleared reference photographs of the Blue Yeti USB microphone on its desktop stand, a frozen prompt, locked 1080p resolution, and locked 16:9 aspect ratio.
- **Output:** A commercially usable 1080p MP4 deliverable (8-second initial generation extended to 12 seconds within the timeline).
- **Control:** Current baseline using Google Flow Veo 3.1 Fast and standard clip concatenation in DaVinci Resolve.
- **Product gate:** The Blue Yeti USB microphone grille, volume/mute knob, desk stand geometry, and distinctive capsule shape must remain visually distinctive, recognizable, and artifact-free in the first 10 seconds of output.

## 3. Test matrix

Three identical bounded runs executed under the exact same locked brief, model version, settings, and reference assets. Scene extension is a measured step within each run:

- **Locked Brief & Settings (Runs 1, 2, and 3):**
  - Prompt: "Commercial tabletop product video of a Blue Yeti USB microphone on its desktop stand with subtle warm rim lighting against a minimalist studio background. Camera slowly tracks from left to right."
  - Reference assets: Two rights-cleared still photographs of the Blue Yeti uploaded under Ingredients.
  - Resolution: 1080p Full HD (1920x1080).
  - Aspect ratio: 16:9 landscape.
  - Frame rate: 24 fps.
  - Audio: Native ambient room tone/synchronous audio enabled.

- **Execution within each run:**
  - **Step A (Initial Generation):** Generate an 8-second 1080p clip from the locked brief and Ingredients reference photos. Record queue latency, render time, credit debit (displayed vs consumed), video bitrate, and product fidelity.
  - **Step B (Measured In-Run Scene Extension):** Select the accepted 8-second clip on the Google Vids timeline; set duration control to extend by exactly 4 seconds (total 12 seconds); prompt: "Camera continues smooth tracking shot as soft studio lighting illuminates the microphone capsule". Record extension generation time, credit debit, transition smoothness at the 8.0-second boundary, lighting continuity, and audio consistency.

- **Run 1:** Baseline execution of Step A + Step B.
- **Run 2:** Identical repeat of Step A + Step B to evaluate drift, failure rate, and transition consistency.
- **Run 3:** Identical repeat of Step A + Step B to measure three-run repeatability and credit stability.

## 4. Strength criteria tested

- **Product specificity:** Preservation of physical Blue Yeti microphone geometry, side-address capsule shape, control knobs, and stand.
- **Output quality:** Visual coherence, absence of warping, and true 1080p detail.
- **Control & consistency:** Precision of the 4-second extension duration and seamlessness across the seam across all three identical runs.
- **Workflow strength:** Timeline editing friction, clip arrangement, and direct MP4 export.
- **Speed & reliability:** Generation latency and failure rate.
- **Cost efficiency:** Free allowance debit verification (must remain within the 50 monthly credits personal allowance).
- **Commercial rights:** Verification of export terms for monetized creator use.

## 5. Acceptance and stop conditions

**Pass:**
- All 3 identical runs complete successfully without server timeout or timeline failure.
- Exported video measures 1920x1080 at 24 fps in valid H.264 MP4 container across all runs.
- Blue Yeti microphone remains geometrically consistent with no severe morphing or loss of distinctive shape in the first 10 seconds.
- In each run, the 4-second scene extension joins without visual jump cuts, lighting pops, or audio glitches.
- Consumed credits match displayed estimates and stay strictly within the free personal tier.

**Fail:**
- Generation fails or times out in more than 1 attempt.
- Output resolution falls back to 720p.
- Blue Yeti microphone morphs into an unrecognizable generic cylinder.
- Scene extension introduces discontinuous lighting shift or jarring visual discontinuity.
- Free tier runs out prematurely or requires paid credit purchase.

**Stop immediately:**
- AIVP-owned imagery or explicit supplier reuse permission for the Blue Yeti is not documented.
- Any prompt for credit card details, paid Workspace tier upgrade, or paid credit purchase.
- Any credential, 2FA, or identity verification gate requiring Tom.
- Any terms requiring transfer of ownership of uploaded reference assets to Google.

## 6. Evidence package

- Source images, supplier permission / ownership record, frozen prompts, and SHA-256 hashes for all inputs.
- Timestamped screenshots of Google Vids UI, generation parameters, and credit balances.
- Downloaded MP4 files for all three runs (initial clips and extensions), including any failed attempts.
- Frame-by-frame contact sheet comparing boundary frames at 7.9s, 8.0s, and 8.1s across all three runs.
- Detailed timing and credit consumption log.
- Scorecard update before and after testing.

## 7. Publishable deliverables

- Evidence-backed First Look update for Google Vids on AI Video Picks.
- Factual updates to the Best Free AI Video Generators 2026 guide reflecting 1080p and Omni 1.1 Flash capabilities.
- 45-second split-screen demonstration video showing generation and extension quality.

## 8. Vendor collaboration boundary

Google provides product documentation and help center resources. No editorial control, pre-publication review, or guaranteed placement is extended.

## 9. Decision

`NOT_RUN` — authentication, live account rollout status, zero-cost confirmation, and documented Blue Yeti imagery rights/permissions pending before hands-on testing.
