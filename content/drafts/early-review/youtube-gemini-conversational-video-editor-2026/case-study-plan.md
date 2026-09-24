# AI Video Picks Case-Study Plan — YouTube Gemini Conversational Video Editor

**Status:** PLAN — access, rights, spend, and publication gates apply  
**Candidate classification:** Monitor only (confidence C; primary vendor documentation only)  
**Evidence confidence:** C (primary vendor documentation only)  
**Business question:** Can the YouTube Gemini conversational video editing assistant in YouTube Create assemble, trim pauses, reorder raw footage, and sync music to the beat for a 45-second vertical product review of the Rode PodMic USB microphone while preserving distinctive product geometry and brand markings across three bounded runs without requiring manual timeline repairs?

## 1. Case-study thesis

At Made on YouTube 2026, YouTube introduced a conversational editing assistant powered by Gemini for YouTube Shorts and YouTube Create, claiming it handles tedious editing tasks like trimming pauses, reordering frames, syncing music to the beat, and generating first drafts from conversational prompts. This case study evaluates whether a solo creator or affiliate marketer can rely on this conversational assistant to turn raw smartphone footage of an affiliate gear product into a finished, publication-ready vertical short without manual trimming in CapCut or DaVinci Resolve.

## 2. Real AIVP scenario

- **Audience:** Australian creators, mobile vloggers, and solo affiliate reviewers producing vertical short-form video (YouTube Shorts, TikTok, Instagram Reels).
- **Affiliate portfolio product:** Rode PodMic USB Dynamic Microphone (referenced in existing AIVP creator gear guide: `posts/best-gear-ai-video-creators-2026.html` via link: `https://amzn.to/48fa7tJ`; Australian brand fit; no ASIN invented).
- **Mandatory asset rights precondition:** Testing cannot begin until AIVP-owned video recordings or documented manufacturer-cleared footage of the Rode PodMic USB microphone is secured.
- **Rollout precondition:** Hands-on execution is blocked until the conversational editing assistant feature is verified as active on the test account in the Australian storefront.
- **Input package:** Three raw rights-cleared vertical video clips (1080x1920 @ 30 fps) captured on mobile:
  - Clip 1 (20s): Creator speaking into camera with deliberate 2-second silent pauses and hesitations.
  - Clip 2 (15s): Tabletop macro B-roll of the Rode PodMic USB showing capsule, integrated swing mount, and USB-C/XLR rear ports.
  - Clip 3 (15s): Summary conclusion and rating.
  - Background track: Rights-cleared instrumental music track with distinct 120 BPM drum beats.
- **Output:** A finished 40–45 second vertical MP4 video with pauses cut, B-roll cutaway inserted, and music synced to transitions.
- **Control:** Manual edit completed in CapCut Mobile by a human editor.
- **Product gate:** The Rode PodMic USB microphone capsule, circular mesh grille, gold-dot badge, and side mounting yoke must remain clearly identifiable and uncorrupted in the first 10 seconds of output.

## 3. Test matrix

Three identical bounded test runs executed on a dedicated mobile test device (iOS 18 / Android 14) using the official YouTube Create app (v0.144.420 or newer):

- **Run 1: Baseline Conversational Turn Execution**
  - **Turn 1 (Drafting & Trimming):** Prompt: "Create a draft from these three clips. Trim all awkward pauses, dead air, and vocal stumbles automatically." Record processing latency, number of cuts made, and preservation of speech intent.
  - **Turn 2 (Reordering & Cutaways):** Prompt: "Cut to the B-roll close-up when I talk about the USB connection, then return to the main speaker." Record whether visual continuity is preserved without clipping words.
  - **Turn 3 (Audio & Beat Sync):** Prompt: "Add the background music track at 20% volume and sync the main cut to the musical beat." Record beat alignment accuracy and audio ducking.

- **Run 2: Identical Repeat Run**
  - Execute exact same three turns with identical source files and identical prompt phrasing. Measure conversational drift, variability in cut timestamps, and UI repeatability.

- **Run 3: Stress & Boundary Run**
  - Execute exact same three turns to measure three-run consistency, stability, and verify whether any quota or conversational turn limits trigger.

## 4. Strength criteria tested

- **Product specificity:** Verification that raw B-roll frames showing the microphone are not warped, cropped awkwardly, or obscured by automated text stickers.
- **Output quality:** Smoothness of cuts, absence of audio pops/clicks at edit boundaries, and natural vocal pacing.
- **Control & consistency:** Predictability of conversational prompt execution and ability to adjust edits via bidirectional manual timeline controls.
- **Workflow strength:** Total friction from raw footage import to final 1080x1920 export.
- **Speed & reliability:** Round-trip latency per conversational prompt turn and failure/error frequency.
- **Cost efficiency:** Confirmation that full workflow runs at zero cost under standard Google account entitlements.
- **Commercial rights:** Verification of export licensing for monetized YouTube Partner Program channels and off-platform syndication.

## 5. Acceptance and stop conditions

**Pass:**
- All 3 runs complete successfully without app crash or server error.
- Pauses greater than 0.8 seconds are cleanly removed without clipping consonants.
- The Rode PodMic USB remains prominently visible and undistorted in the opening 10 seconds.
- Background music is smoothly ducked under speech and aligns to within ±3 frames of a transition beat.
- Final export renders at native 1080x1920 resolution at 30 fps in standard H.264 MP4.
- Total editing time through conversational prompts is under 5 minutes per run.

**Fail:**
- Conversational assistant fails to parse trimming instructions or cuts active speech.
- B-roll placement overrides crucial speech segments or fails to sync.
- Audio pops, audio desync, or clipping occurs at edit points.
- Output resolution is restricted or forced to lower quality.
- App crashes or displays network timeout errors during prompt execution.

**Stop immediately:**
- Lack of verified ownership or supplier permission documentation for the test footage.
- Feature is not yet activated on the testing account.
- Any prompt requiring payment, credit purchase, or subscription upgrade.
- Any terms requiring surrender of creator IP ownership to Google or YouTube.
- Any credential, 2FA, or private account verification gate requiring Tom.

## 6. Evidence package

- Source video clips, audio tracks, and input checksums (SHA-256).
- Screen recordings of the YouTube Create app showing exact prompt entries and real-time assistant responses.
- Timeline EDL/cut-point comparison across Runs 1, 2, and 3.
- Exported final MP4 files for all three runs.
- Frame-by-frame inspection sheet of the transition cuts and product close-ups.
- Verified timing and latency logs.

## 7. Publishable deliverables

- Evidence-backed First Look update for YouTube Create / Shorts AI editing tools on AI Video Picks.
- Factual updates to `ai-tools-youtube-creators-2026.html` and `turn-long-videos-into-shorts-ai.html`.
- 30-second split-screen comparison showing raw footage vs. conversational AI edit.

## 8. Vendor collaboration boundary

YouTube provides public apps and creator documentation. No editorial previews, ranking commitments, or commercial sponsorships are provided.

## 9. Decision

`NOT_RUN` — live feature rollout verification on Australian test account, authentication, physical mobile device test harness setup, zero-cost account confirmation, commercial off-platform terms verification, and documented Rode PodMic USB footage rights pending before hands-on testing.
