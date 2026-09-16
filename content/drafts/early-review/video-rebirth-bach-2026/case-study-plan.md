# Case Study Plan: Video Rebirth BACH — Product-Specific Affiliate Clip

## Business Question

Can BACH's reference-guided generation (Element2Video / montage2video) turn a product hero shot into a recognizable 30-second vertical affiliate video that passes the AIVP first-10-seconds product identity gate — and at what cost and time compared to the current Google Flow Veo 3.1 Fast baseline?

## Use Case

Convert a product reference image for an LED face mask (Amazon B0D2XTZN8V, AU ~$50) into a 30-second 9:16 vertical clip with red/blue LED glow visible, character in frame, and product identifiable in first 10 seconds.

This maps directly to BACH's "Element to Video" (product subject + scene description) and optionally "Montage" (multi-shot with same product across cuts).

## Locked Brief

```
PRODUCT: LED face mask B0D2XTZN8V, AU $50, red and blue LED light therapy
INPUT: Clean product reference image on plain/dark background (same reference used in Google Flow tests)
PROMPT: "Woman in a minimal bedroom, wearing a red and blue LED face mask, relaxed expression, 
         warm ambient lighting, camera slowly pulls back from close-up to medium shot, 9:16 vertical."
ENDPOINT: element2video (subject = product reference, scene = prompt above)
RESOLUTION: 1080p (default)
DURATION: 6–8 seconds (single shot, test 1); if passing, test 2: montage2video for 30-second multi-shot
FORMAT: MP4 H.264, 9:16

CONTROL (baseline): Google Flow Veo 3.1 Fast, same reference image, same product, same brief
BASELINE_METRICS: ~8 minutes setup → first output; cost ~$0.50 per clip; product distinctive YES

SUCCESS_CRITERIA:
  - Product (red/blue LED glow, mask shape) visually distinctive in first 10 seconds ✓
  - 1080p output usable without re-editing ✓
  - Total time from API call to downloaded MP4 ≤ 10 minutes ✓
  - Cost per 6–8 second clip ≤ $2.00 ✓
  - Commercial use rights confirmed before production run ✓ (prerequisite gate)

FAILURE CRITERIA:
  - Product not visible or not identifiable in first 10 seconds → STOP
  - Render timeout > 15 minutes → STOP
  - Cost per clip > $2.00 after two runs → STOP
  - Commercial rights not confirmed → DO NOT RUN (rights gate)
```

## Prerequisites

- [ ] Commercial use rights confirmed (from vendor outreach response or published TOS)
- [ ] BACH 1.0 Pro live at bach.art (expected end of September 2026)
- [ ] Free sign-up credits available for trial

## Three Runs

| Run | Date | Model | Settings | Prompt variant | Cost | Result |
|-----|------|-------|----------|---------------|------|--------|
| 1 | TBD | bach-1.0 Pro | element2video, 1080p, 6s | Base prompt | TBD | TBD |
| 2 | TBD | bach-1.0 Pro | element2video, 1080p, 8s | + "LED lights illuminating face" | TBD | TBD |
| 3 | TBD | bach-1.0 Pro | montage2video, 1080p, 30s | Multi-shot sequence | TBD | TBD |

## Evidence Package (required before escalating to Review)

- [ ] Source assets: product reference image (same as used in Flow tests), rights confirmed
- [ ] API response JSON for each run (includes model, settings, generation time)
- [ ] 3 output video files (including failures) with SHA-256 hashes
- [ ] Frame QC: first frame, 5s mark, final frame — product visibility noted
- [ ] Timing: API call timestamp → first output timestamp
- [ ] Cost: credits used per run, dollar equivalent (requires pricing confirmation)
- [ ] Commercial rights: Explicit TOS or vendor email confirmation → GATE before run
- [ ] Comparison: BACH vs Google Flow — time, cost, product specificity score

## Publishable Outputs (if case study passes)

1. **First Look → Review upgrade:** video-rebirth-bach-2026 folder
2. **Best AI Image-to-Video article update:** Add BACH to best-ai-image-to-video-generators-2026.html with leaderboard context
3. **Best AI Video Tools 2026:** Add BACH as strong new entrant in multi-shot/character-consistency section
4. **Sora Alternatives 2026:** Add BACH as narrative/cinematic alternative (multi-shot)
5. **Behind-the-scenes YouTube Short:** Brief → element2video → output comparison vs Google Flow
6. **Affiliate CTA:** Only after affiliate programme confirmed and tracking verified

## Stop Conditions

- Commercial rights not confirmed → **DO NOT RUN any credits**
- Product not visible in Run 1 → STOP; reclassify as narrative-only tool
- Cost > $2/clip after Run 2 → STOP; note cost limit in first look
