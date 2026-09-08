# Case Study Plan: Film Studio Skills on a Real Product Short

## Business Question
Can the seven-skill workflow produce a more complete and repeatable generation-ready shot package for AIVP’s LED-mask product Short than the current manual brief, without changing source facts or exact-product identity?

## Locked Brief
Create planning artifacts for a 30-second 9:16 affiliate video about the rights-cleared red/blue LED face mask used in AIVP’s prior specificity pilot. Freeze the product geometry, colourway, eye and mouth openings, controller, emitter pattern, price statement, source hashes, and approved claims. No image or video generation is authorized in this test.

## Control
The current AIVP locked brief and manual shot list. Compare completeness, contradictions, setup time, revision count, and exact-product fields against the candidate workflow.

## Three Bounded Runs
1. Run the full workflow in an isolated fixture directory using the locked brief.
2. Repeat from a clean fixture with identical inputs and no access to Run 1 outputs.
3. Repeat after one predeclared product-state change, red mode to blue mode, while requiring all invariant product fields to remain unchanged.

## Success Criteria
- Every run preserves all locked product fields and places the exact product in the first 10 seconds.
- All required assets have versioned passports and no unlocked asset reaches a final shot prompt.
- The three outputs use the required file structure and contain no invented product claim or price.
- Two unchanged runs produce materially equivalent shot constraints.
- Total agent time is under 30 minutes per run and no external generation cost is incurred.
- The workflow beats the control on completeness without adding contradictions.

## Failure and Stop Conditions
Fail on product-field drift, invented facts, an unlocked asset reaching generation-ready status, destructive writes outside the fixture, or materially inconsistent repeat output. Stop on credential requests, profile/instruction-file writes outside the fixture, network calls, license acceptance, paid credits, or any executable payload.

## Evidence Package
Save the audited commit, seven source-file SHA-256 values, sandbox tree before/after, immutable brief hash, every generated planning file, timestamps, diff between runs, deterministic QC report, and security notes. Record failures as evidence rather than deleting them.

## Publication Path
If the test passes and license/reuse rights are clarified, publish a methodology-led workflow First Look and comparison module. Review language requires artifact-backed hands-on evidence. No affiliate CTA exists or is authorized.

## Outcome
PLANNED — BLOCKED_LICENSE_AND_SANDBOX_HARDENING
