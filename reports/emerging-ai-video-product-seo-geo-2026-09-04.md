# Emerging AI-video product SEO/GEO decision

**Research date:** 2026-09-04  
**Scope:** Public primary sources, current SERPs, and the AI Video Picks publication repository. No authenticated analytics or invented keyword volumes.

## Decision

Update the existing Runway review immediately, then create a focused Gemini Omni 1.1 Flash explainer. Do not publish a standalone Solaris review yet.

## Best emerging-product opportunity

### Gemini Omni 1.1 Flash

Google announced Gemini Omni 1.1 Flash on 2026-08-27. Its material production features are:

- scene extension in 10-second increments up to 40 seconds cumulative;
- up to 10 seconds of prior context for extensions;
- first/last-frame interpolation;
- video-reference inputs;
- 360p drafts for cheaper/faster iteration;
- 1080p and 4K finishing;
- availability through Google AI Studio/API, Google Flow for AI Plus/Pro/Ultra users, and integrations including Runway.

Runway separately documents Gemini Omni Flash on Standard plans and above. In Runway, the current documented surface generates or edits 3–10 second 720p clips, accepts prompt/reference inputs, and costs 10 Runway credits per output second, with additional input/reference costs for video editing.

This creates two intents on one topic:

1. informational/developer intent: what it is, API pricing, scene extension, keyframes and 4K;
2. commercial creator intent: whether to access it through Google or a multi-model Runway subscription.

### Why this beats Solaris as the first page

Runway announced Solaris on 2026-08-31, creating a fresh explanatory query. Solaris is an early-access Interface World Model that renders interactive interfaces frame by frame. Runway is still seeking launch partners and lists unresolved limits around text, trust, long sessions, accessibility and integration.

Solaris is strong for news links and AI-answer citations but weak for immediate buyer conversion. It should be a dated section in the Runway review, not a scored product review. A standalone page becomes justified when public access, pricing, terms and a reproducible test exist.

### Runner-up: Seedance 2.5

ByteDance launched Seedance 2.5 on 2026-07-31 with 30-second generation, multimodal references, timestamp-level editing and multi-round extension. Runway also exposes Seedance 2.5. It deserves a later comparison against Gemini Omni and Gen-4.5, but the launch is older and the current Gemini query surface is fresher.

## Urgent existing-page refresh

**Target:** `posts/runway-review-2026.html`  
**Current title:** `Runway Gen-4.5 Review 2026: Pricing & Features`  
**Article dateModified:** 2026-05-31  
**Sitemap lastmod:** 2026-06-01

### Blocking factual drift

The current article says:

- Gen-4.5 costs 25 credits per second;
- a 10-second clip costs 250 credits;
- the top plan is Unlimited with 2,250 credits;
- Runway is mainly Gen-4.5, Act One and older generation tools;
- unsupported superlatives such as “nothing else comes close.”

Runway's public pricing page retrieved on 2026-09-04 says:

- Gen-4.5 costs 60 credits per five seconds, or 12 credits per second;
- Standard: US$15 monthly or US$12/month billed annually, 625 credits;
- Pro: US$35 monthly or US$28/month billed annually, 2,250 credits;
- Max: US$95 monthly or US$76/month billed annually, 9,500 credits;
- the platform includes third-party models such as Kling 3.0, Seedance 2.5, Veo 3.1 and Gemini Omni.

The article and sitemap dates also disagree, which blocks the AI Video Picks revenue publish gate.

### Affiliate state

Runway's public affiliate page currently advertises:

- US$15 per new paid subscriber;
- a 25% reader discount through the partner code;
- complimentary Runway Max for active partners;
- a three-month initial pilot.

However, `go/runway/index.html` currently forwards to the plain Runway homepage with no affiliate code. Its visible link is `nofollow` rather than `nofollow sponsored`. AI Video Picks must not describe this route as commission-tracked until Runway approves the application and supplies the code.

## Recommended publication sequence

### 1. Safety/freshness refresh: existing Runway review

Keep the existing URL and canonical. Do not throw away accumulated authority.

Suggested title:

`Runway Review 2026: Gen-4.5, Gemini Omni, Pricing & Solaris`

Required edits:

- replace all old pricing and credit calculations;
- replace Unlimited with Max where the current public plan applies;
- add a dated “What changed since May” section;
- explain Runway's shift into a multi-model workspace;
- add Gemini Omni, Seedance 2.5, Aleph 2.0 and current model-router context;
- add a short Solaris section labelled early access/research;
- remove unsupported “best,” “industry-leading” and “nothing else comes close” claims unless backed by a dated reproducible test;
- remove claims of hands-on testing that do not point to a test artifact;
- synchronize visible update date, Article/Review schema, sitemap and `llms.txt`;
- keep the Runway CTA editorial until an approved partner code exists.

### 2. New focused page: Gemini Omni 1.1 Flash

Suggested URL:

`posts/gemini-omni-1-1-flash-explained-2026.html`

Suggested title:

`Gemini Omni 1.1 Flash Explained: Pricing, 4K, Scene Extension & Runway Access`

Use “explained,” not “review,” until AI Video Picks runs a reproducible test.

Primary query cluster:

- Gemini Omni 1.1 Flash
- Gemini Omni 1.1 Flash pricing
- Gemini Omni scene extension
- Gemini Omni 4K
- Gemini Omni first and last frame
- Gemini Omni vs Veo 3.1
- Gemini Omni on Runway
- how to access Gemini Omni 1.1 Flash

Page architecture:

1. 50–70 word direct answer naming release date, access routes and strongest limitation.
2. “What changed in 1.1?” fact table with primary-source links.
3. Access-route table: Google AI Studio/API, Flow subscriptions and Runway Standard+.
4. Pricing units kept separate: Google API dollars/tokens versus Runway credits.
5. Worked cost examples with formulas and an explicit retry-cost caveat.
6. Workflow: draft at low resolution, approve composition, then finish at higher resolution.
7. Gemini Omni vs Veo 3.1 vs Seedance 2.5 vs Gen-4.5, limited to sourced dimensions.
8. Limitations: nondeterminism, extension continuity, 720p limitation on the current Runway integration, access differences and commercial-rights checks.
9. FAQ answers for “free?”, “40 seconds at once?”, “native 4K or upscale?”, “available on Runway?”, and “commercial use?”
10. Dated source ledger and update history.

Structured data:

- `TechArticle` while the page is evidence-led rather than hands-on;
- `FAQPage` for questions actually answered in visible copy;
- `BreadcrumbList`;
- `HowTo` only after the exact steps have been exercised and recorded.

GEO/AEO requirements:

- one claim per sentence where possible;
- primary source directly after the claim;
- dates on prices, access and model capabilities;
- answer blocks that stand alone when quoted;
- explicit distinction between vendor claims, AI Video Picks tests and interpretation;
- no fake experience language;
- no unsupported rankings;
- include a short “What we do not know yet” block;
- add the exact headline and quick answer to `llms.txt` after publication approval.

### 3. Later updates

- Update `posts/best-ai-image-to-video-generators-2026.html` for Seedance 2.5, Gemini Omni and current Runway model economics. Its article dateModified is still 2026-05-21.
- Update `posts/google-flow-review-2026.html`; its article dateModified is 2026-07-08 while sitemap lastmod is 2026-08-03, and several free-credit/access claims require fresh verification.
- Update `posts/best-ai-video-tools-2026.html` only after the product pages are corrected, so the roundup does not become another conflicting source of truth.

## SEO/GEO decision

**Yes, update now.** The first action is an existing-page refresh because the Runway review already has internal links and index history but contains material commercial drift. The new Gemini Omni page should follow immediately because the current SERP already contains dedicated pricing/explainer competitors and AI Video Picks has no indexed answer.

Do not build a standalone Solaris review now. Add a concise, sourced early-access section to the Runway page and monitor for public availability.

## Sources retrieved 2026-09-04

1. Google, Gemini Omni 1.1 Flash launch: https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/
2. Runway, Gemini Omni model page: https://runwayml.com/product/models/gemini-omni
3. Runway, Gemini Omni help/specs: https://help.runwayml.com/hc/en-us/articles/53031657806611-Creating-with-Gemini-Omni-Flash
4. Runway pricing: https://runwayml.com/pricing
5. Runway affiliate program: https://runwayml.com/affiliate-program
6. Runway Solaris announcement: https://runwayml.com/news/research/introducing-solaris
7. ByteDance Seedance 2.5 announcement: https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5

## Approval boundary

This report does not update or publish an article, modify affiliate routing, submit a Runway application, or deploy the site. Those actions require a scoped implementation and the AI Video Picks revenue publish gate before human publication approval.
