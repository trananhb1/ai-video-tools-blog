# Case Study Plan: Can Premiere Build a Product-Specific Short Without Losing the Product?

**Status:** PLAN — blocked on rights-cleared product assets and authorized Premiere beta access  
**Tool:** Adobe Premiere Generative Media Tool (beta)  
**Current classification:** verified floor 34/100; potential ceiling 100/100; confidence C  
**Decision this test will answer:** Should AI Video Picks use Premiere’s in-timeline generator for product-affiliate Shorts, or keep generation and editing as separate workflows?

## 1. Falsifiable thesis

Premiere’s Generative Media Tool can turn one rights-cleared 9:16 hero-product clip and reference image into a usable 30-second product Short faster and at no higher than US$2 per accepted output, while preserving the exact product’s defining appearance throughout the first 10 seconds.

Failure on product identity or commercial rights overrides speed, convenience and numerical score.

## 2. Real AI Video Picks scenario

- **Audience:** Australian skincare/wellness buyers and creators.
- **Product:** the same distinctive red/blue LED face-mask category used in the prior AIVP specificity pilot, but only with AIVP-owned footage or vendor-supplied assets carrying written reuse permission.
- **Output:** 30-second, 9:16, caption-ready product explainer with a clear hero product in the opening 10 seconds.
- **Premiere task:** use the real hero clip as timeline context; generate only supporting inserts, sound effects and optional music.
- **Control workflow:** current reference-led generation followed by manual Premiere import/edit, using the same locked script and rights-cleared inputs.
- **Do not use:** Amazon listing imagery without permission, generic stock as the hero product, or text-only footage that invents a different mask.

## 3. Locked brief

“Create a clean Australian creator-style 30-second vertical explainer around this exact red-and-blue LED face mask. Preserve its shape, colourway, eye/mouth openings, controller and light pattern. The real product must remain clearly identifiable during the first 10 seconds. Generated inserts may show contextual use but must not change the product model or imply unverified medical outcomes.”

No prompt changes between compared models except model-required syntax.

## 4. Three bounded runs

1. **Adobe Firefly baseline:** reference-guided gap fill plus generated sound effects; record estimated and consumed credits.
2. **Partner-model comparison:** lowest-credit suitable available model using the same timeline range, prompt and references.
3. **Consistency repeat:** repeat the better of Runs 1–2 unchanged to measure product drift and reproducibility.

Stop before generation if credits require purchase or the interface does not show sufficient cost/rights information.

## 5. Measurements

For every run capture:

- Premiere beta and model version;
- Australian availability and plan;
- setup time to first generation;
- displayed credit estimate and actual credits consumed;
- queue/render time;
- failures and retries;
- first frame, midpoint and final frame;
- exact-product geometry, colour, light placement, controls, accessories and visible branding;
- 9:16 handling and export friction;
- Content Credentials result;
- accepted/rejected decision with reason;
- effective cost per accepted clip.

## 6. Acceptance criteria

**Pass only if all are true:**

- Rights for inputs and monetized outputs are documented.
- Exact product is distinctive during the first 10 seconds.
- No material drift in mask shape, colourway, openings, controller or light pattern.
- 9:16 output integrates without corrective reframing that obscures the product.
- At least two of three runs produce usable material.
- Setup is under 30 minutes after access is available.
- Winning run renders within five minutes, excluding a documented vendor outage.
- Effective generation cost is no more than US$2 per accepted output.

**Fail if any are true:** product identity drifts, rights remain unclear, fewer than two runs are usable, mandatory paid add-on appears, or cost cannot be measured.

## 7. Evidence package

Save under `evidence/adobe-premiere-generative-media-tool-2026/`:

- locked brief and source-asset rights record;
- input hashes and copies or immutable references;
- settings/model/credit screenshots;
- every generated output, including failures;
- three-frame contact sheet per output;
- timing/credit/cost CSV;
- export and Content Credentials screenshots;
- completed scorecard with before/after delta.

## 8. Deliverables if the test passes

1. **Flagship case study:** “We Tested Premiere’s New AI Video Tool on a Real Product Short.”
2. **Evidence-led full review:** replace First Look language only after artifacts exist.
3. **Buyer-guide module:** Premiere versus a separate generator-plus-editor workflow.
4. **30–60 second behind-the-scenes Short:** exact input → timeline generation → output → score.
5. **Affiliate CTA:** only after Adobe/Partnerize acceptance and live tracking verification.

If it fails, publish the failure honestly as a limitations case study when legally and editorially appropriate.

## 9. Vendor boundary

Adobe may provide documentation, access, credits, approved media and factual corrections. Adobe receives no editorial control, pre-publication approval, guaranteed rating, positive coverage or affiliate placement.

## Decision

`RETEST` — obtain bounded review access and rights-cleared input assets, then run the three-test protocol.
