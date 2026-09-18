# Research Dossier: Powermove

**Status:** QUALIFIED — First Look only; public repository and release artifacts, local execution held on Linux host  
**Release date:** 2026-09-18  
**Discovery date:** 2026-09-18  
**Contract materiality score:** 15  
**Gate 1 score:** 9/10 — QUALIFIED  

## Search strategy and deduplication

The desk inspected the new Product Hunt listing, official website (trypowermove.com), GitHub repository (iterative-computer/powermove), release notes for v1.0.0, package manifests, and repository license.[4][5][9][10][11]

The Product Hunt post ("Powermove", published 2026-09-14) was unified with the official GitHub release v1.0.0 published September 18, 2026.[4][9] They represent a single underlying product launch: the v1.0.0 public milestone of an open-source, AI-native desktop motion editor.

## Gate 1 — launch materiality

Powermove is an iterative video and motion editor for macOS where an AI agent sits inside the editing loop.[5][10] It features an intentionally tiny kernel; timeline editing, effects, inspector panels, and UI controls are implemented as extensions. An AI coding agent (specifically OpenAI Codex CLI or Anthropic Claude Code) can add or fork panels, inspect the project, render test frames, and execute transactional, undoable edits directly on the live project.[5][10]

**Gate 1: 9/10 — QUALIFIED.**
- **Relevance to AI-video production: 3/3.** Motion/video editor with timeline layers, keyframe animation, frame rendering, video playback, and integrated agent workflows.
- **Differentiation: 3/3.** Self-rewriting architecture where the editor's UI and tool panels are live-reloaded extensions authored in-editor by local coding agents.
- **Launch recency: 2/2.** Version 1.0.0 released September 18, 2026 (<12 hours prior to current assessment tick).
- **Accessibility: 1/2.** Free GPL-3.0 software available publicly; however, execution is strictly constrained to macOS on Apple Silicon (arm64) and requires active signed-in CLI credentials for Claude Code or Codex.

**Contract score: 15 — threshold met.** Launch within 72 hours (+3); new tool without an AIVP page (+3); primary source confirmed (+2); explicit commercial rights under GPL-3.0-or-later (+2); likely reader impact (+2); hands-on code available now (+3). No points awarded for affiliate economics or established transactional volume.

## Architecture and runtime constraints

- **Repository Layout:** Bun workspace monorepo containing @powermove/desktop (Electron, Svelte 5, electron-vite), @powermove/www (SvelteKit static), shared design tokens, native macOS haptics addon, and embedded player bundles.[5][11]
- **Licensing:** Free software under GPL-3.0-or-later.[11]
- **Hardware/OS Requirements:** macOS on Apple Silicon (arm64), Bun >= 1.3, Xcode Command Line Tools.[5]
- **Agent Dependency:** Requires local installation and active authentication of OpenAI Codex CLI or Anthropic Claude Code.[5]
- **Execution Hold:** The current evaluation host is Linux (x86_64), preventing direct execution of macOS Apple Silicon Electron builds. Following the precedent of lynnreal-omni-2026 and vanch007, hands-on testing is held (HOLD_LOCAL_APPLE_SILICON_REQUIRED).
