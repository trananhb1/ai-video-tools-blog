# Research Dossier: FastWan2.2 TI2V 5B MLX Q8

**Candidate ID:** `jboone100-fastwan22-ti2v-5b-mlx-q8-2026-09-21`
**Assessment date:** 2026-09-21
**Evidence scope:** Primary documentation only; no AIVP render was run.
**Decision:** QUALIFIED (Gate 1 8/10) -> First Look staged; hands-on testing held because the documented LocalLab runtime is not publicly linked and the public `mlx-video` loader is incompatible with the quantized encoder.

## Search strategy and primary evidence

The deterministic Hugging Face launch monitor surfaced the repository. Verification used its model card and API metadata, then compared it with the stated upstream MLX conversion.[6][7][8] No independent output benchmark, official vendor domain, public compatible runtime, pricing page or published contact was found in this tick.

## Gate 1 - launch materiality

- **AI-video relevance: 3/3.** It packages a three-step text/image-to-video model for Apple Silicon and documents complete prompt-to-MP4 runs.[6]
- **Differentiation: 2/3.** The changed component is an 8-bit umT5 encoder: 6.0 GB resident versus 22.7 GB for the loader-upcast source in the author's M2 Max measurement; transformer and VAE are unchanged.[6][7]
- **Recency: 2/2.** Hugging Face records creation on 2026-09-21.[7]
- **Accessibility: 1/2.** The 18.87 GB Apache-2.0 repository is public and ungated, but the card says stock `mlx-video` should use the source repository; the measured path uses an unlinked LocalLab engine.[6][7]

**Total: 8/10 - QUALIFIED.** This is a material low-memory Apple-Silicon deployment artifact, not a new foundation model.

## Verified capabilities and limitations

The author reports 832x480 output at 24 fps, 43 seconds end-to-end for a one-second clip and 311 seconds for a five-second clip on an M2 Max with 32 GB unified memory.[6] These are vendor/author measurements, not AIVP runs. The source MLX conversion is a self-contained 24.2 GB, three-step image-to-video package; this candidate retains its transformer/VAE and changes the text encoder.[6][8]

Hard limitations:

- no AIVP output or independent benchmark;
- no public compatible command/runtime demonstrated in the candidate card;
- no evidence that an exact affiliate product remains distinctive in the first 10 seconds;
- no measured failure rate or three-run consistency;
- local compute cost and Australian hardware economics are unmeasured;
- Apache-2.0 repository licensing is explicit, but generated-output and every upstream-input right still require a production rights check.[6][7]

## Strength classification

- **Verified floor:** 36/100
- **Potential ceiling:** 100/100
- **Evidence coverage:** 36%
- **Confidence:** C (primary documents only)
- **Classification:** Weak fit pending a controlled run

See `strength-scorecard.json`. No Category Leader or Strong Specialist language is justified.

## Decision and next action

Stage a clearly labelled First Look only. Do not recommend it for product affiliate production yet. Obtain or implement a public, audited MLX loader without paid spend, then execute the locked three-run reference-product case study. Outreach is HELD because no verified official-domain published email was found.

## Sources

[6] https://huggingface.co/jboone100/FastWan2.2-TI2V-5B-MLX-q8
[7] https://huggingface.co/api/models/jboone100/FastWan2.2-TI2V-5B-MLX-q8
[8] https://huggingface.co/lBroth/FastWan2.2-TI2V-5B-MLX
