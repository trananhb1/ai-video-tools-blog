# AI Video Picks Case-Study Plan — HiDream-O1-Video-1.0 (HD-V1)

**Status:** PLAN — access, rights, spend and publication gates apply  
**Candidate classification:** Monitor only (Docs-only First Look)  
**Evidence confidence:** C  
**Business question:** Can HiDream-O1-Video-1.0 (HD-V1) take a single product reference image of the rights-cleared white LED face mask (Amazon ASIN B0D2XTZN8V) and generate three consistent 10-second vertical promotional clips that keep the exact product visually distinctive and recognizable throughout the first 10 seconds, with synchronized ambient audio, at a cost under US$2.00 per accepted output?

## 1. Case-study thesis

HiDream claims HD-V1 is a native omnimodal foundation model incorporating physical laws (gravity, collision, inertia) and synchronized audio-video generation, accessible via HiHarness single-image-to-video API with reference image input. The falsifiable test evaluates whether HD-V1 can reliably preserve exact e-commerce product geometry, openings, and illumination without physical hallucinations across three repeated runs.

## 2. Real AIVP scenario

- **Audience:** Australian creators and SMB e-commerce video producers.
- **Input:** One real, rights-cleared AI Video Picks product reference hero image: white LED light therapy face mask (Amazon ASIN B0D2XTZN8V, ~AU$50, white silicone shell, eye and mouth cutouts, handheld controller, white USB cable, red and blue LED emitters). Pre-hashed with SHA-256 before upload.
- **Output:** Commercially usable 10-second vertical (9:16) 1080p promotional video clip with native integrated audio.
- **Control:** The same locked brief and source reference image through the current production baseline (Google Flow Veo 3.1 Fast reference-to-video).
- **Product gate:** The exact mask shell shape, eye and mouth cutouts, controller, cable, colourway, and distinctive red/blue LED pattern must remain visually distinctive and recognizable from frame 1 (0.0s) through frame 10.0s. Generic skincare video, human face substitutions obscuring the mask, or altered shell geometry fails immediately.

## 3. Test matrix

Three identical bounded runs on the HiHarness HiDream-O1-Video-1.0 endpoint:

1. **Run 1 (Baseline):** Default single-image-to-video settings, 10s fixed duration, aspect ratio matching input reference image (9:16), locked prompt.
2. **Run 2 (Best documented workflow):** Recommended prompt structure incorporating physical camera cues and lighting specification, 10s duration, preserving physical consistency.
3. **Run 3 (Stress / consistency / drift):** Exact identical repeat of Run 2 settings and seed to measure prompt drift, visual stability, audio sync consistency, and retry count.

### Locked Brief

```text
PRODUCT: White LED Light Therapy Face Mask (Amazon ASIN B0D2XTZN8V, AU ~$50)
INPUT: Clean rights-cleared product reference image on neutral background (SHA-256 pre-hashed)
PROMPT: "E-commerce product showcase: A clean, neutral studio vanity. The white LED light therapy face mask is featured with gentle camera push-in, illuminated with its distinct red and blue LED glow. Handheld controller and cable resting neatly beside the shell. Soft ambient room tone and gentle activation hum. 9:16 vertical orientation, 1080p, 10 seconds duration. Preserve exact shell silhouette, eye and mouth openings, and LED pattern. No text overlays, no human face substitutions, no medical claims."
ENDPOINT: HiHarness HiDream-O1-Video-1.0 (single-image-to-video async task API)
DURATION: 10 seconds
ASPECT RATIO: 9:16 (vertical, preserved from reference image)
AUDIO: Native integrated audio enabled
```

Record for every run: exact request JSON, reference image URL/hash, task submission timestamp, returned `task_id`, polling intervals, completion timestamp, displayed credits, actual account balance change, output video SHA-256, HTTP status codes, and frame QC observations.

## 4. Strength criteria tested

- **Product specificity (weight 20):** Exact mask geometry, cutouts, controller, and red/blue LED pattern distinctive in the first 10 seconds.
- **Output quality (weight 15):** 1080p visual coherence, absence of edge tearing or temporal jitter, natural lighting decay.
- **Control and consistency (weight 10):** Variation between Run 2 and Run 3 under identical parameters.
- **Workflow strength (weight 15):** Practicality of HiHarness async polling task workflow and video retrieval.
- **Speed and reliability (weight 10):** Queue wait time, total generation latency from task creation to status `1`, and retry rate.
- **Cost efficiency (weight 10):** Verified credit debit per generation converted to USD; ceiling US$2.00 per accepted output.
- **Commercial rights (weight 10):** Verification of explicit commercial-use grant for generated video and audio tracks in monetized content.

## 5. Acceptance and stop conditions

**Pass:**
- 3/3 exports completed without API timeout or unhandled exceptions.
- Exact product recognizable from 0s to 10s without shape substitution or severe warping.
- Native 9:16 vertical resolution preserved.
- Coherent, non-distorted audio track synchronized with visual illumination.
- Median generation latency <= 5 minutes per run.
- Billed cost <= US$2.00 per usable output.
- Written or published commercial-use rights confirmed for monetized editorial and affiliate publication.

**Fail:**
- Product identity lost, distorted, or replaced with a generic model within the first 10 seconds.
- Fewer than 3 usable outputs produced.
- Render timeout > 15 minutes.
- Cost per clip exceeds US$2.00.
- Audio missing, corrupted, or severely desynchronized.
- Output requires destructive cropping or editing to hide severe artifacts.

**Stop immediately:**
- Any payment prompt, required credit card entry, or unapproved subscription charge.
- Debit exceeding approved complimentary allowance.
- Password, 2FA, identity verification, or personal signature prompt.
- Unclear input or output intellectual property terms.

## 6. Evidence package

- Source image SHA-256 hash and provenance log.
- API request payloads and full response JSON logs (with authorization tokens redacted).
- All three generated MP4 video files with SHA-256 checksums.
- Contact sheets and keyframe extracts at 0.0s, 5.0s, and 10.0s noting product recognition.
- Audio waveform analysis verifying integrated soundtrack.
- End-to-end timing logs (task submission -> polling -> completed).
- Pre-test and post-test credit balance snapshots.
- HiHarness Terms of Service and commercial rights snapshot.
- Updated strength scorecard with verified scores post-testing.

## 7. Publishable deliverables

- First Look remains strictly labeled as "Untested Docs-Only" until all three runs complete.
- Upgrade to full Review only if all pass conditions are met.
- Inclusion in comparative table against Google Flow Veo 3.1 Fast.
- Behind-the-scenes Short demonstrating the reference image input and output clip.
- Transparent methodology and AI illustration disclosure.
- Affiliate CTA only after official programme approval and link tracking verification.

## 8. Vendor collaboration boundary

The vendor may provide official documentation, API access, complimentary review credits, and factual corrections. The vendor receives no editorial control, pre-publication copy review, guaranteed rating, guaranteed recommendation, or guaranteed ranking.

## 9. Decision

`RETEST` — Awaiting verified vendor contact, confirmation of commercial rights for generated media, and bounded complimentary review credits. Do not spend paid credits.
