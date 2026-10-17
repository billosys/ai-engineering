---
concept: "D65 Whitepoint"
slug: "d65-whitepoint"
category: "colour-theory"
subcategory: "illuminants"
tier: "foundational"
layer: "2-domain"
source: "A Perceptual Color Space for Image Processing"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "The Oklab color space"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "medium"
aliases: []
prerequisites:
  - "colour-space"
extends: []
related:
  - "oklab"
  - "xyz-colour-space"
  - "gamut-srgb"
contrasts_with: []
answers_questions:
  - "What makes a colour space perceptually uniform, and why does it matter for design?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition
D65 is a standard illuminant/reference white used by several colour models; it is not an absolute display maximum.

# Core Definition
Ottosson's Oklab model uses a D65 reference. With the article's normalized D65 XYZ white, the stated coefficients map white approximately to L=1, a=b=0; the rounded table vector is not an exact universal constant. Shared D65 can avoid a whitepoint adaptation step between compatible representations, but does not remove encoding, transfer-function or gamut differences. CSS Lab/LCH and ProPhoto RGB use D50 reference conditions, while CSS Oklab/OkLCh use D65.

# Prerequisites

- **Colour space** — Whitepoints are a property of colour spaces; the general concept is required.

# Key Properties
1. D65 identifies a reference illuminant/white, not a display peak or absolute white.
2. Oklab's published coefficients assume its D65 reference; use the matching input conventions.
3. Shared reference white avoids that adaptation step only; it does not imply identical gamut or encoding.
4. CSS Color 4 distinguishes D50 Lab/LCH from D65 Oklab/OkLCh.

# Construction / Recognition

## To Construct/Create:
1. For the article’s XYZ example, use the stated D65 reference and rounded normalized white (X=0.950, Y=1.000, Z=1.089). Those printed values are an example, not an exact universal constant.
2. Convert differing input reference whites to the coefficient family’s expected D65 conditions with an appropriate chromatic-adaptation step; do not re-derive the Oklab matrices merely because an input uses another white.

## To Identify/Recognise:
1. Identify D65 by its standard illuminant/reference chromaticity and the model’s stated convention, not by treating any source near 6500 K as D65.
2. The example table confirms: XYZ (0.950, 1.000, 1.089) → Oklab (1.000, 0.000, 0.000).

# Context & Application
- **Common applications**: CSS colour functions use different reference whites; CSS Color 4 distinguishes D50 Lab/LCH from D65 Oklab/OkLCh.

# Examples

**Example 1** (from source): The XYZ/Oklab example table lists (X=0.950, Y=1.000, Z=1.089) → (L=1.000, a=0.000, b=0.000), which is D65 white mapping to Oklab white. (Section: "Table of example XYZ and Oklab pairs")

# Relationships
## Builds Upon
- **Colour space** — Whitepoints are model/reference conditions.

## Enables
- **Oklab conversion** — Use coefficients with their stated D65 conditions.

## Related
- **sRGB gamut** — sRGB uses D65; encoding and gamut still differ from Oklab.

- **D50-referenced models** — Adapt differing whites as needed.

# Common Errors
- **Error**: Treating D65 as a maximum display white or assuming all CSS spaces use it.
  **Correction**: It is a reference condition; CSS Lab/LCH use D50 while Oklab/OkLCh use D65.
- **Error**: Re-deriving Oklab coefficients whenever another input has a different white.
  **Correction**: Adapt differing reference whites into the expected D65 conditions using an appropriate chromatic adaptation step.

# Common Confusions
- **Confusion**: D65 is a display maximum or all CSS spaces use it.
  **Clarification**: It is a reference condition. CSS Lab/LCH use D50; CSS Oklab/OkLCh use D65.

# Source Reference

"The Oklab color space" section; requirements list in "Motivation and derivation of Oklab"; example table in "Converting from XYZ to Oklab".

# Verification Notes
Reference distinctions were checked against CSS Color 4 CRD 2026-10-09 §§9–10. This WIP Candidate Recommendation Draft is current technical support, not an immutable historical capture.
