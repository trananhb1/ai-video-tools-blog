# AI Video Picks Case-Study Plan — CreatOK

**Status:** PLAN — access, rights, security, spend and publication gates apply
**Candidate classification:** Weak fit
**Evidence confidence:** C
**Business question:** Can CreatOK turn rights-cleared reference images for LED face mask ASIN B0D2XTZN8V into a 30-second vertical TikTok commerce video that preserves exact product identity in the first 10 seconds, exports through the documented agent workflow, and costs US$0 across three runs?

## 1. Thesis and locked brief

Freeze the product reference set, current source price `$49.99`, and script points: red and blue LED modes, at-home skincare use, price callout, and neutral “check current listing details” CTA. Do not make treatment or efficacy claims.

Output: 30-second 1080×1920, 30fps H.264 MP4, clear English narration, licensed audio, no watermark. The exact mask must appear by 0:03 and remain distinctive through 0:10 by shell shape, eye/mouth cut-outs, colourway, LED pattern, controller and included accessories. Control: Dreamina/reference-image workflow using identical assets and script.

## 2. Three bounded runs

1. Browser baseline with default product-image workflow.
2. Best documented CreatOK workflow with frozen model, prompt, first/end frames and agent settings.
3. Exact repeat of run 2 to measure identity drift, API reliability and recovery.

Before any run, audit the first-party CLI for credentials, shell/file safety, egress, account verification, idempotency and credit-spend controls. Record tool/package version, hashes, exact inputs, settings, start/end and render time, displayed/consumed credits, output path/SHA-256, retries and acceptance reason.

## 3. Acceptance and stop conditions

**PASS only if all three:** exact product visible by 0:03 and distinctive through 0:10; no substitute product or fabricated claim; correct price time-qualified; 1080×1920 MP4; no watermark; complete output/audio commercial rights; ≤10 minutes per run; US$0; deterministic task recovery without duplicate spend.

**FAIL:** identity drift, generic product, invented medical/spec claim, manual rebuild, watermark, export failure, >10 minutes, unsafe CLI behavior or any cost.

**STOP:** payment/subscription prompt, paid credits, unclear displayed credit cost, credential/2FA/identity/payment/signature step, failed security audit, unclear source rights or unclear monetized-output rights.

## 4. Evidence package

Source ledger; rights-cleared inputs and hashes; CLI source/version/audit; API request metadata with secrets redacted; cost screenshots; all outputs including failures; QC frames at 0:00/0:03/0:10/mid/final; timing/retry ledger; rights confirmation; pre/post scorecard.

## 5. Publishable outputs and decision

Evidence-led case study/review only after passing; product-video buyer-guide module; workflow Short; transparent access/methodology disclosure; no affiliate CTA until acceptance and tracking verification. Vendor receives no editorial control or guaranteed coverage. Access does not guarantee positive coverage.

`RETEST` — obtain explicit bounded free credits and complete rights, audit the CLI, then execute the three locked runs.
