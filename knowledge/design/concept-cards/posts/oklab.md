---
concept: "Oklab Colour Space"
slug: "oklab"
category: "colour-theory"
subcategory: "perceptual colour models"
tier: "foundational"
layer: "2-domain"
source: "A Perceptual Color Space for Image Processing"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "The Oklab color space"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "high"
aliases: []
prerequisites:
  - "perceptual-uniformity"
  - "colour-space"
  - "xyz-colour-space"
extends:
  - "perceptual-uniformity"
related:
  - "lms-cone-responses"
  - "d65-whitepoint"
  - "chroma-perceptual"
  - "lightness-perceptual"
  - "colour-interpolation-perceptual"
  - "oklab-conversion"
  - "colour-space-comparison"
contrasts_with:
  - "colour-space-comparison"
answers_questions:
  - "What makes a colour space perceptually uniform, and why does it matter for design?"
  - "How do you construct a palette that changes lightness uniformly across hues?"
  - "How do you convert between colour spaces for image processing?"
rosetta_stone: []
css_implementation:
  -
    property: "color"
    example: "color: oklab(0.7 0.1 -0.08);"
    support: "baseline"
  -
    property: "color"
    example: "color: oklch(70% 0.15 200);"
    support: "baseline"
---

# Quick Definition
Oklab is a D65-referenced colour model designed to approximate lightness, chroma and hue judgements with a simple transform; uniformity is an approximate fit, not a guarantee.

# Core Definition
Oklab represents a colour with L, a and b coordinates and may be expressed in polar form as L, C and h. Ottosson describes the model as intended to do a good job predicting perceived lightness, chroma and hue. The transform is fitted and approximate; coordinate independence is a modelling goal, not a promise of perceptual independence at every hue, context, display or gamut. Oklab uses D65 reference conditions. CSS Lab/LCH use D50, while CSS Oklab/OkLCh use D65. The article's coefficient family and CSS Color's standardized values should not be silently mixed.

# Prerequisites

- **Perceptual uniformity** — Oklab is defined as an attempt to achieve this property; understanding what it means is essential for understanding why Oklab exists.
- **Colour space (general concept)** — Oklab is a colour space; the general concept of coordinate-based colour representation is assumed.
- **XYZ colour space** — The conversion pipeline from sRGB to Oklab goes through XYZ; the intermediate representation is XYZ.

# Key Properties
1. Oklab uses a D65 reference; diffuse reference white does not set a display's absolute maximum.
2. The route for linear sRGB uses two linear transforms around real cube roots; encoded sRGB must first be decoded.
3. Approximate uniformity and model-coordinate independence do not guarantee equal appearance across all conditions.
4. Oklab coordinates can convert outside a destination gamut; conversion and gamut mapping are distinct.
5. The article's examples and comparisons remain attributed to its stated conditions and datasets.

# Construction / Recognition

## To Construct/Create:
1. Start with a linear sRGB colour (gamma-decoded).
2. Multiply by the first matrix M1 to produce approximate cone responses (l, m, s).
3. Apply cube-root non-linearity: l' = l^(1/3), m' = m^(1/3), s' = s^(1/3).
4. Multiply by the second matrix M2 to produce (L, a, b).
5. Optionally convert to LCh polar form: C = sqrt(a² + b²), h = atan2(b, a).

## To Identify/Recognise:
1. Three-channel Lab-like space with L ∈ [0, 1] for colours within the sRGB gamut.
2. D65 white maps to (L=1, a=0, b=0).
3. Typical sRGB red maps to approximately (L=0.63, a=0.22, b=0.13) — highly saturated colours have large a or b magnitude.

# Context & Application
- **Typical contexts**: Colour transformations and candidate palette construction, followed by destination gamut/render checks.
- **Common applications**: CSS Color 4 defines `oklab()` and `oklch()` syntax and explicit interpolation-space choices; actual host support was not tested here.

# Examples

**Example 1** (from source): An Oklab gradient with varying hue, constant lightness (L) and chroma (C) appears even and uniform. By contrast, an HSV gradient with constant value and saturation shows yellow, magenta, and cyan dramatically lighter than red and blue. (Section: "Comparing Oklab to HSV")

**Example 2** (from source): The quantitative error table shows Oklab achieving the lowest L RMS (0.20) and C RMS (0.81) of all tested colour spaces except CAM16-UCS (the source of training data). (Section: "Comparison with other color spaces")

**Example 3** (from source): Blending white with blue in Oklab produces no hue shift toward purple — unlike CIELAB, CIELUV, and HSV, which all show a purple shift when blending blue. (Section: "Blending colors")

# Relationships
## Builds Upon
- **Perceptual uniformity** — A fitted approximation, not an exact law.
- **Colour space** — Oklab is a model-specific coordinate system.
- **XYZ colour space** — One useful route in the article's conversion.

## Enables
- **Colour interpolation** — A host may select Oklab coordinates for a particular path.
- **Palette construction** — Use coordinates for candidates, then check gamut and appearance.

## Related
- **CIELAB** — Similar Lab-like form, but different reference conditions and behaviour.
- **Chroma / Lightness** — Oklab coordinates with approximate perceptual interpretation.

## Contrasts With
- **HSL/HSV** — Different model coordinates and parameter meanings.

# Common Errors
- **Error**: Treating equal Oklab distances or fixed L/C hue sweeps as universally equal-looking and displayable.
  **Correction**: Treat uniformity as approximate, then check output gamut, rendering and context.
- **Error**: Treating Oklab L as WCAG luminance or using article coefficients as identical to CSS standardized coefficients.
  **Correction**: Keep measures and coefficient families distinct.

# Common Confusions

- **Confusion**: "OK" in Oklab is an informal quality rating — it's just acceptable.
  **Clarification**: Per the source, "it is called the Oklab color space, because it is an OK Lab color space" — the "OK" is a deliberate understatement, since the space performs substantially better than CIELAB on lightness and chroma metrics.

- **Confusion**: Oklab and OKLch are different colour spaces.
  **Clarification**: OKLch (or Oklch) is merely Oklab expressed in polar form — same space, cylindrical coordinates.

# Source Reference

"The Oklab color space", "Implementation", "How Oklab was derived", "Comparison with other color spaces" sections.

# Verification Notes
Definitions and stage order were checked against Ottosson and CSS Color 4 CRD 2026-10-09 §§9–10. CSS Color is a work-in-progress Candidate Recommendation Draft. The article's hue-sweep image was not visually inspected, and reported data are not new experiments.
