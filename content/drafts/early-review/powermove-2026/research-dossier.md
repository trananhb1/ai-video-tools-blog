# Research Dossier: Powermove

**Status:** QUALIFIED — First Look only; public repository and release artifacts, local execution held on Linux host  
**Release date:** 2026-09-18  
**Discovery date:** 2026-09-18  
**Contract materiality score:** 15  
**Gate 1 score:** 9/10 — QUALIFIED  

## Search strategy and deduplication

The desk inspected the new Product Hunt listing and official website for Powermove.[4][10]
It examined the GitHub repository, release notes for v1.0.0, and package manifests.[5][9][11]

The Product Hunt post ("Powermove", published 2026-09-14) was unified with the official GitHub release v1.0.0 published September 18, 2026.[4][9]
They represent a single underlying product launch: the v1.0.0 public milestone of an open-source, AI-native desktop motion editor.[5][9]

## Gate 1 — launch materiality

Powermove is an iterative video and motion editor for macOS where an AI agent sits inside the editing loop.[5][10]
It features an intentionally tiny kernel; timeline editing, effects, inspector panels, and UI controls are implemented as extensions.[5][10]
An AI coding agent, specifically OpenAI Codex CLI or Anthropic Claude Code, can add or fork panels, inspect the project, render test frames, and execute transactional, undoable edits directly on the live project.[5][10]

**Gate 1: 9/10 — QUALIFIED.**
- **Relevance to AI-video production: 3/3.** Motion/video editor with timeline layers, keyframe animation, frame rendering, video playback, and integrated agent workflows.[5][10]
- **Differentiation: 3/3.** Self-rewriting architecture where the editor's UI and tool panels are live-reloaded extensions authored in-editor by local coding agents.[5][10]
- **Launch recency: 2/2.** Version 1.0.0 released September 18, 2026, which is within 12 hours of the current assessment tick.[9]
- **Accessibility: 1/2.** Free GPL-3.0 software available publicly; however, execution is strictly constrained to macOS on Apple Silicon (arm64) and requires active signed-in CLI credentials for Claude Code or Codex.[5][11]

**Contract score: 15 — threshold met.** Launch within 72 hours (+3); new tool without an AIVP page (+3); primary source confirmed (+2); explicit commercial rights under GPL-3.0-or-later (+2); likely reader impact (+2); hands-on code available now (+3).[5][9][11] No points awarded for affiliate economics or established transactional volume.

## Architecture and runtime constraints

- **Repository Layout:** Bun workspace monorepo containing @powermove/desktop (Electron, Svelte 5, electron-vite), @powermove/www (SvelteKit static), shared design tokens, native macOS haptics addon, and embedded player bundles.[5][11]
- **Licensing:** Free software under GPL-3.0-or-later.[11]
- **Hardware/OS Requirements:** macOS on Apple Silicon (arm64), Bun >= 1.3, Xcode Command Line Tools.[5]
- **Agent Dependency:** Requires local installation and active authentication of OpenAI Codex CLI or Anthropic Claude Code.[5]
- **Execution Hold:** The current evaluation host is Linux (x86_64), preventing direct execution of macOS Apple Silicon Electron builds. Following the precedent of lynnreal-omni-2026 and vanch007, hands-on testing is held (HOLD_LOCAL_APPLE_SILICON_REQUIRED).

## Gate 2 — Strength

**Verified floor:** 35/100
**Potential ceiling:** 100/100
**Evidence coverage:** 35%
**Confidence:** C — public repository and release documentation only; no hands-on execution
**Classification:** Promising/conditional

Powermove introduces a novel extensible architecture for desktop motion editing.[5][10]
However, key operational properties—including frame rendering consistency, timeline corruption resistance under autonomous agent edits, and export reliability—remain untested.
Under standing rules, no candidate may advance beyond confidence C without controlled artifact-backed evaluation.

## Gate 3 — Case study

**CASE_STUDY: PLANNED_HELD_LOCAL_APPLE_SILICON_REQUIRED.**
The current evaluation environment is Linux (x86_64), which cannot execute macOS Apple Silicon Electron builds.[5]
A structured case-study protocol is defined for execution when Apple Silicon test hardware is allocated, evaluating three consecutive natural-language timeline modification passes (keyframe pacing, timer overlay, and transform panel fork) with Claude Code or Codex CLI.

## Gate 4 — Outreach and affiliate

Inspection of the GitHub repository, package metadata, and official website found no published official-domain email address.[5][10][11]
Standing policy mandates that outreach may only be directed to an email address published on the vendor's official domain.
Git commit author addresses and guessed aliases are prohibited under standing policy.
Therefore, outreach is held under `HELD_NO_VERIFIED_OFFICIAL_DOMAIN_PUBLISHED_CONTACT`.
No manifest entry was created and no email was sent.

**OUTREACH_STATUS:** HELD_NO_VERIFIED_OFFICIAL_DOMAIN_PUBLISHED_CONTACT
**AFFILIATE_STATUS:** NONE_FOUND
**PUBLICATION_STATUS:** STAGED_FIRST_LOOK_ONLY_NOT_PUBLISHED
**NEXT_ACTION:** Hold hands-on testing pending Apple Silicon hardware allocation; hold outreach pending published official-domain contact.

## Update — 2026-09-20 tick

Powermove v1.0.1 was released September 19, 2026, and verified from the GitHub releases page on September 20.[6]

The release adds editor and UX fixes including save-progress feedback, GIF/video preview scrubbing, font hot-reload, agent attachment improvements, and panel compatibility warnings.[6]

It also adds a new `npx powermove serve` remote-host mode for accessing the editor from a browser over LAN or a tailnet.[6]

The macOS Apple Silicon constraint, GPL-3.0-or-later licensing, and absence of a published official-domain contact are unchanged. The Product Hunt listing resurfacing and v1.0.1 activity are a version bump to the same candidate, not a separate launch. All existing testing and outreach holds remain in force.

## Update — 2026-09-20 04:15 CEST tick

Monitor signal: "Product Hunt Powermove disappearance." Resolved as FALSE SIGNAL.
Direct inspection of the Product Hunt listing confirmed the page remains live at #35 day rank, 66 upvotes, "launched this week" on the same URL.[4]
No deletion, delisting, or takedown was detected.
All existing gates, holds, and classifications unchanged.

## Sources

[4] https://www.producthunt.com/products/powermove-2 — Powermove on Product Hunt (confirmed live 2026-09-20)
[5] https://github.com/iterative-computer/powermove — Powermove GitHub repository
[6] https://github.com/iterative-computer/powermove/releases — Powermove releases list
[9] https://github.com/iterative-computer/powermove/releases/tag/v1.0.0 — Powermove 1.0.0 release
[10] https://trypowermove.com — Powermove official site
[11] https://raw.githubusercontent.com/iterative-computer/powermove/main/package.json — Powermove package metadata
