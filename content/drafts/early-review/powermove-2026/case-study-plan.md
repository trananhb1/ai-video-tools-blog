# AI Video Picks Case-Study Plan — Powermove

**Status:** PLAN — held for external Apple Silicon test harness  
**Candidate classification:** Promising/conditional  
**Evidence confidence:** C  
**Business question:** Can Powermove v1.0.0 running on an Apple Silicon Mac (M-series) with an authenticated Claude Code / Codex CLI session successfully execute three consecutive natural-language timeline modification passes (adjusting keyframe pacing, adding a title layer, and forking an inspector panel) without corrupting project state, failing frame validation, or exceeding 5 minutes per pass?

## 1. Case-study thesis

Powermove's agent-in-the-loop paradigm provides real utility over traditional NLEs only if its typed tool layer prevents agent hallucinations from breaking the timeline or producing invalid video frames.

## 2. Locked test brief

- **Hardware Target:** Apple Silicon Mac (M1/M2/M3/M4) running macOS 14+.
- **Dependencies:** Bun >= 1.3, Xcode CLI tools, Claude Code / Codex CLI logged in.
- **Input:** Standardized 10-second 1080p MP4 test video clip with 2 keyframed overlay layers.
- **Prompt Sequence:**
  1. "Adjust the opacity curve of Layer 2 to fade out smoothly between 00:03 and 00:05."
  2. "Generate a minimalist timer overlay in the top-right corner."
  3. "Fork the transform panel to add an instant 9:16 vertical crop toggle."

## 3. Pass/Fail criteria

- All three passes complete with clean undo checkpoints.
- Rendered output video plays back smoothly without dropped frames or visual artifacts.
- No unhandled exceptions in the Electron main or renderer processes.
