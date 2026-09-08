# Research Dossier: Film Studio Skills

**Status:** Repository evidence only; static security audit completed; no generation run  
**Event date:** 2026-08-14 (late discovery)  
**Contract materiality score:** 12  
**Content type:** First Look only

## Launch materiality

The repository packages seven installable agent skills covering setup, studio initialization, script breakdown, reference boards, asset passports, static stress tests, and locked shot prompts.[1][2] It is directly relevant to AI-video preproduction and available without a waitlist, but it is not a renderer, does not generate media itself, and was discovered more than three weeks after its two initial commits on August 14.[3]

**Score: 12 — QUALIFIED (late discovery).** Breakdown: new workflow tool without an AIVP page +3; hands-on access available now +3; Australian creator accessibility +2; primary source confirmed +2; likely reader/workflow impact +2. No launch-recency, transactional-intent, commercial-rights, or affiliate points were awarded.

## Strength classification

**Verified floor: 38/100; potential ceiling: 88/100; evidence coverage: 38%; confidence C; classification: Weak fit on verified evidence, promising workflow candidate.** The floor reflects the documented file-based workflow, explicit consistency gates, model-agnostic design, and local inspectability. Output quality, time savings, cross-agent repeatability, and commercial reuse remain unverified. A Category Leader or Strong Specialist label is prohibited at confidence C.

## Static security and integration audit

The audited commit was 314517381b1be72c1404c068a9e37a064ec4215c. It contains seven Markdown skill files and image assets, with no package manifest, executable script, binary, network client, or embedded credential. The setup skill tells agents to store only environment-variable names rather than secret values.[2]

The main operational risk is instruction-file mutation: the setup skill writes an AI film studio section into both CLAUDE.md and AGENTS.md. That behavior is inappropriate for direct installation into the AIVP profile without a sandbox and targeted hardening. The repository also has no tracked LICENSE file at the audited commit, so reuse, modification, redistribution, and monetized publication rights are unresolved. **Do not install into the active Hermes profile.**

## Product-specificity fit

The package is structurally aligned with AIVP’s exact-product requirement because it uses asset passports, immutable references, stress tests, and generation logs.[2] That is workflow design, not proof. The planned test fails if the exact LED-mask geometry, controller, colourway, or emitter pattern is omitted from the locked passport or changed in the final shot prompt.

## Outreach status

No company-domain email was published in the repository or GitHub organization profile. No address was guessed and no GitHub issue, form, or social DM was submitted. **OUTREACH_STATUS: HELD_NO_VERIFIED_CONTACT.**

## Decision

Stage a sandbox-only three-run planning test after license clarification. Do not install, generate paid media, publish Review language, or add an affiliate CTA.

## Sources

[1] https://github.com/machina-exm/film-studio-skills — Film Studio Skills repository
[2] https://raw.githubusercontent.com/machina-exm/film-studio-skills/main/README.md — Film Studio Skills README
[3] https://github.com/machina-exm/film-studio-skills/commits/main — Film Studio Skills commit history
