# AI Video Picks Case-Study Plan — Runway current pricing and plan model

**Status:** PLAN — access, rights, spend and publication gates apply  
**Candidate classification:** Monitor only pending a bounded current-plan run  
**Evidence confidence:** C  
**Business question:** Can Runway Standard produce three repeatable five-second 9:16 product-reference hooks in which the exact LED face mask remains recognizable, at an allocated plan cost of no more than US$2 per accepted clip?

## 1. Case-study thesis

Runway's current Standard allowance can be viable for short affiliate hooks if Gen-4.5 preserves the exact reference product across three runs without retries pushing accepted-output cost above US$2.

## 2. Real AIVP scenario

- **Audience:** Australian creators and SMBs.
- **Input:** rights-cleared hero image of Amazon product B0D2XTZN8V, AIVP's $49.99 LED face mask; frozen five-second motion prompt.
- **Output:** three H.264 MP4 hooks, 1080×1920, 9:16, five seconds, no captions or narration.
- **Control:** the same source and motion brief through AIVP's last accepted Dreamina reference-image workflow.
- **Product gate:** exact mask shape, eye/mouth cut-outs and red/blue LED treatment must be distinctive from the first frame through the final frame.

## 3. Locked brief and three bounded runs

**Locked prompt:** `Create a five-second vertical close-up product hook. Preserve the exact face-mask shape, eye and mouth openings, controls and colourway from the supplied reference. Begin with red LEDs illuminated, transition to blue LEDs, slow push-in camera, clean neutral background, no text, no extra products, no redesign.`

Freeze model version, reference image, prompt, duration, aspect ratio, resolution and any seed supported by the UI.

1. **Run 1 — Baseline:** default Gen-4.5 image-to-video settings.
2. **Run 2 — Repeatability:** identical inputs and settings.
3. **Run 3 — Repeatability:** identical inputs and settings.

For each run record start/end time, queue/render duration, displayed and consumed credits, retries, exported file, SHA-256, and acceptance reason.

## 4. Strength criteria tested

- product specificity: exact-product first-frame-to-final-frame preservation;
- output quality: coherence, deformation, flicker and export usability;
- control and consistency: visual drift across three identical runs;
- workflow strength: setup-to-export friction;
- speed and reliability: render time, failures and retries;
- cost efficiency: actual credits and nominal allocated plan cost per accepted output;
- commercial rights: terms snapshot plus input-rights record.

## 5. Acceptance and stop conditions

**Pass:** 3/3 exports complete; exact product recognizable throughout all clips; no material deformation; each accepted clip consumes no more than 60 credits and has nominal allocated cost no more than US$2; median setup-to-export time no more than 10 minutes; monetized use remains permitted.  
**Fail:** fewer than 3 accepted clips, identity drift in any clip, more than one retry total, or any accepted clip exceeds 60 credits/US$2 nominal allocation.  
**Stop immediately:** payment prompt, unapproved paid-credit use, credential/2FA step, missing source rights, commercial-rights change, or displayed credit debit above the locked ceiling.

## 6. Evidence package

- source asset and rights record;
- prompt/settings JSON or exact UI transcription;
- screenshots of account tier, model, settings and pre-generation displayed cost;
- all outputs, including failures;
- first/mid/final-frame contact sheet and product-identity QC;
- timing and credit ledger;
- SHA-256 hashes;
- Runway terms/pricing snapshots;
- pre/post scorecards and Dreamina control comparison.

## 7. Publishable deliverables

If the case study passes: evidence-led pricing update, Runway review correction, buyer-guide cost module and a behind-the-scenes Short. An affiliate CTA remains prohibited until programme acceptance and tracking are verified.

## 8. Vendor collaboration boundary

Runway may provide documents, bounded access, credits, media and factual corrections. It receives no editorial control, pre-publication approval, guaranteed rating, recommendation or affiliate placement.

## 9. Decision

`RETEST` — highest-leverage next action: verify the pricing configuration in a second official observation, then execute the three no-cost five-second runs if sufficient complimentary/free credits are available without a payment or credential escalation.
