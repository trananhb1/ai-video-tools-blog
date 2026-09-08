# Research Dossier: Minimax-h3_Singularity

**Status:** Repository/model-card evidence; no AIVP run  
**Event date:** 2026-09-05  
**Contract materiality score:** 15  
**Content type:** First Look only

## Decision

Minimax-h3_Singularity is a community fine-tuned fusion of MiniMax H3 for ComfyUI, supporting text-, image-, reference-, and video-to-video workflows and recommending a separate four-step acceleration LoRA.[9] It is not an official new MiniMax model. The official H3 release is a 33B multimodal model with 768p local generation and API-assisted context/2K stages.[11]

**Strength:** verified floor 19/100; potential ceiling 100/100; evidence coverage 19%; confidence C; Monitor only.

## Critical product-specificity finding

An artifact-backed community report shows a custom truck reference being overwritten before animation. The author says the aggressive early diffusion likely caused the distortion and recommends the four-step LoRA at 0.75–1.0, while acknowledging that exact setup was not specifically stress-tested.[22] This is a hard warning for product affiliate: the candidate fails the current evidence gate and cannot be recommended for exact-product video unless three controlled AIVP runs reverse that result.

## Rights and provenance

The model card labels the derivative Apache-2.0, but the underlying official H3 release points to the MiniMax H3 Community License.[9][11] Until compatibility, attribution, output rights, dataset rights and LoRA terms are resolved in writing, the commercial-rights gate is unresolved and publication as a monetised recommendation is blocked.

## Access and operations

The model is available through Hugging Face and an external RunningHub demo, with ComfyUI support.[9] Local hardware requirements and actual render cost were not verified. A second discussion says the author considered it stable enough to release further quantised versions, but that is an author statement rather than an AIVP reliability test.[23]

## Outreach status

The model author’s Hugging Face profile links social and GitHub accounts but publishes no official-domain email.[10] MiniMax publishes official addresses, but MiniMax did not release this derivative; contacting MiniMax as though it did would misattribute the candidate. No email was guessed and no form or platform discussion was submitted. Status: HELD — no verified vendor-domain email.
