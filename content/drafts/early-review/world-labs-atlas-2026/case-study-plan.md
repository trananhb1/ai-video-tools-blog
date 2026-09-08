# AI Video Picks Case-Study Plan — World Labs Atlas

**Status:** PLAN ONLY — blocked on Atlas access, written publication rights, and no-cost allowance  
**Candidate classification:** Monitor only (23/100 verified floor)  
**Evidence confidence:** C  
**Business question:** Can Atlas turn rights-cleared photographs of one exact LED face mask into a controlled 15-second vertical product orbit while preserving that product’s identity in every frame of the first 10 seconds?

## 1. Case-study thesis

Atlas’s strongest relevant claim is native camera-geometry control over reference-led video.[1] The test falsifies the proposition that this control produces a more repeatable, product-specific affiliate shot than AIVP’s current reference-image workflow.

## 2. Locked real AIVP scenario

- **Audience:** Australian skincare creators and small e-commerce teams.
- **Product:** $49.99 LED face mask, ASIN B0D2XTZN8V.
- **Inputs:** three AIVP-owned photographs of the physical product (front, three-quarter, controller close-up). If AIVP-owned photographs are unavailable, STOP; Amazon listing images are not assumed reusable.
- **Brief:** “Create a 15-second 9:16 product hero video. Keep the exact white mask shell, eye/mouth openings, controller, strap geometry, emitter layout, and red/blue LED modes unchanged. Use a slow 120-degree clockwise camera orbit in a clean vanity setting. Show red mode from 0–7.5 seconds and blue mode from 7.5–15 seconds. No invented logo, accessory, text, hand, or altered product shape.”
- **Output target:** H.264 MP4, 1080×1920 minimum, 24–30 fps, no music or narration.
- **Control:** the same images, brief, duration, and QC rubric through the current approved reference-image workflow.

## 3. Three bounded runs

1. **Baseline:** default Atlas settings with the locked references and camera path.
2. **Documented best workflow:** vendor-recommended reference weighting and camera-path settings, with no paid extras.
3. **Consistency repeat:** identical to run 2, including all settings; only the system seed may vary if Atlas does not allow a fixed seed.

For every run record model/build, account tier, all parameters, seed, start/end timestamps, queue/render duration, displayed and consumed credits, retries, output path, SHA-256, and frame-QC notes at 0s, 5s, 10s, and 15s.

## 4. Acceptance criteria

**Pass only if all three runs:**

- show the exact product by second 1 and keep it distinctive throughout the first 10 seconds;
- preserve shell shape, openings, strap, controller, and emitter pattern with no material drift;
- follow the requested orbit without cuts that hide the product;
- export at least 1080×1920 with no material flicker, geometry break, or invented branding;
- finish in 5 minutes or less per run after setup;
- cost no more than US$2 per accepted output under a vendor-confirmed bounded allowance;
- are covered by explicit written permission for monetized AIVP articles, YouTube, and social media.

**Fail:** any run loses exact-product identity in the first 10 seconds, alters a hard identity feature, or requires repair beyond caption/audio assembly.

**Stop immediately:** payment prompt, paid-credit use, password/2FA/identity/signature requirement, confidentiality that prevents evidence-led publication, unclear input rights, unclear monetized-output rights, or cumulative displayed value above US$6.

## 5. Evidence package

- source photos and signed/dated rights record;
- Atlas access grant and written publication/commercial-rights confirmation;
- screenshots of model, settings, camera path, and displayed cost;
- settings export and environment/version record;
- all three outputs including failures;
- SHA-256 hashes of inputs, settings, and outputs;
- frame contact sheets and product-identity checklist;
- time, retry, and credit ledger;
- control output and score delta;
- pre/post strength scorecards.

## 6. Publishable outputs after a pass

- evidence-led Atlas case study or full review;
- product-reference/camera-control comparison module;
- 30–60 second behind-the-scenes Short using rights-cleared output;
- transparent access, methodology, and limitation disclosure;
- affiliate CTA only after programme acceptance and live tracking verification.

## 7. Decision

`RETEST` — wait for Atlas general access or a bounded non-confidential review grant with explicit monetized-publication rights.

## Sources

[1] https://www.worldlabs.ai/blog/atlas — Atlas: A World Model for Spatial Intelligence
