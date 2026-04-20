---
concept: Colour Space Comparison (Oklab vs CIELAB vs HSL)
slug: colour-space-comparison
category: colour-theory
subcategory: perceptual colour models
tier: advanced
layer: 2-domain
source: "A Perceptual Color Space for Image Processing"
source_slug: posts
authors: "Bj\u00f6rn Ottosson"
chapter: "What about existing models?"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - []
prerequisites:
  - perceptual-uniformity
  - oklab
  - colour-space
  - chroma-perceptual
  - lightness-perceptual
extends:
  - perceptual-uniformity
related:
  - colour-interpolation-perceptual
  - gamut-srgb
contrasts_with:
  - []
answers_questions:
  - "What makes a colour space perceptually uniform, and why does it matter for design?"
  - "How do you construct a palette that changes lightness uniformly across hues?"
rosetta_stone: []
css_implementation:
  - property: "color"
    example: "color: oklab(0.7 0.1 -0.08);"
    support: baseline
  - property: "color"
    example: "color: hsl(200deg 50% 60%);"
    support: baseline
---

# Quick Definition

Compared across perceptual error metrics, Oklab outperforms CIELAB on lightness and chroma prediction while matching or exceeding most spaces on hue uniformity; HSL/HSV provides no perceptual uniformity at all.

# Core Definition

The source provides a systematic comparison of eight colour spaces \u2014 Oklab, CIELAB, CIELUV, OSA-UCS, IPT, JzAzBz, HSV, and CAM16-UCS \u2014 across three error metrics (L RMS, C RMS, H RMS) and three supplementary metrics (L 95, C 95, H 95).

Key verdicts from the source on the main competitors:

- **CIELAB**: "Largest issue is their inability to predict hue. In particular blue hues are predicted badly."
- **CAM16-UCS**: "Does a good job at being perceptually uniform overall, but doesn't meet other requirements: Bad numerical behavior, it is not scale invariant and blending does not behave well because of its compression of chroma."
- **HSV**: "Only on this list because it is widely used. Does not meet any of the requirements except having a D65 whitepoint."
- **IPT**: "Does a great job modelling hue uniformity. Doesn't predict lightness and chroma well unfortunately."

Error table (RMS errors; best non-CAM16 in bold):

| Metric | Oklab | CIELAB | CIELUV | OSA-UCS | IPT | JzAzBz | HSV |
|--------|-------|--------|--------|---------|-----|--------|-----|
| L RMS  | **0.20** | 1.70 | 1.72 | 2.05 | 4.92 | 2.38 | 11.59 |
| C RMS  | **0.81** | 1.84 | 2.32 | 1.28 | 2.18 | 1.79 | 3.38 |
| H RMS  | 0.49 | 0.69 | 0.68 | 0.49 | 0.48 | **0.43** | 1.10 |

# Prerequisites

- **Perceptual uniformity** \u2014 The comparison is structured around which spaces achieve it.
- **Oklab** \u2014 The primary space being advocated.
- **Colour space** \u2014 Background on what each space is.
- **Chroma (perceptual)** and **Lightness (perceptual)** \u2014 The metrics being compared.

# Key Properties

1. Oklab achieves the lowest L RMS and C RMS of all compared spaces except CAM16-UCS.
2. Oklab achieves H RMS comparable to IPT and OSA-UCS; JzAzBz is slightly better on hue.
3. HSV/HSL provides no perceptual uniformity for lightness or chroma (L RMS = 11.59; C RMS = 3.38).
4. CIELAB's primary weakness is hue prediction, especially for blues.
5. CAM16-UCS's chroma compression makes it poor for colour blending despite its perceptual accuracy.
6. Blending: CIELAB, CIELUV, and HSV all show hue shifts toward purple when blending blue with white; Oklab does not.

# Construction / Recognition

## To Construct/Create:
1. To compare colour spaces, convert a test set of experimentally judged equal-L, equal-C, and equal-H pairs to each space.
2. Swap the relevant coordinate between pairs (e.g., swap L values for the lightness test) and measure CIEDE2000 colour difference.
3. RMSE across all pairs gives the error metric per space.

## To Identify/Recognise:
1. A space with low L RMS produces hue-sweep gradients at constant L that appear visually even in brightness.
2. A space with good chroma prediction shows Munsell rings as circles in the ab plane.
3. A space with poor blending behaviour shows hue shifts in gradient transitions.

# Context & Application

- **Typical contexts**: Selecting a colour space for image processing, UI design, gradient generation, or palette construction.
- **Common applications**: Choosing Oklab over HSL for CSS gradients; preferring Oklab over CIELAB when blue hue accuracy matters.

# Examples

**Example 1** (from source): Blending white with blue: Oklab produces no hue shift; CIELAB, CIELUV, and HSV all shift toward purple. CAM16 desaturates rapidly. (Section: "Blending colors")

**Example 2** (from source): Munsell chroma data plotted in each space: Oklab and CAM16 produce near-circular rings; CIELAB, CIELUV, IPT, and OSA-UCS all show distorted rings. (Section: "Munsell data")

**Example 3** (from source): Luo-Rigg ellipses: "The shape of the full gamut is quite odd in CIELAB and OSA-UCS, which likely means that their predictions are quite bad for highly saturated colors." (Section: "Luo-Rigg dataset and full gamut")

# Relationships

## Builds Upon
- **Perceptual uniformity** \u2014 This is what is being measured and compared.
- **All individual colour spaces listed** \u2014 Understanding each space's design is required to interpret the comparison.

## Enables
- **Colour space selection** \u2014 The comparison provides the basis for choosing Oklab for image processing tasks.
- **Understanding tradeoffs** \u2014 The comparison makes explicit that no single space is optimal on all metrics; Oklab is chosen for the best overall balance.

## Related
- **Colour interpolation (perceptual)** \u2014 The blending comparison is a practical consequence.
- **Chroma (perceptual)** \u2014 Chroma prediction is one of the three metrics.

## Contrasts With
- **HSV/HSL** \u2014 The comparison makes quantitative the intuitive failure of HSV/HSL for perceptual tasks.
- **CIELAB** \u2014 Closely related structure but inferior lightness, chroma, and blue-hue prediction.

# Common Errors

- **Error**: Assuming CIELAB is "good enough" because it has been the standard for decades.
  **Correction**: The quantitative comparison shows Oklab's L RMS is 8.5x lower than CIELAB's and C RMS is 2.3x lower; the blue hue failure in CIELAB is particularly problematic for design use.

# Common Confusions

- **Confusion**: A lower hue error (H RMS) is always better.
  **Clarification**: JzAzBz achieves the lowest H RMS (0.43) but at the cost of introducing a dependence on scale/exposure that makes it impractical for general image processing. The best H RMS does not determine the best overall choice.

# Source Reference

"What about existing models?"; "Comparison with other color spaces"; "Blending colors"; "Munsell data"; "Luo-Rigg dataset and full gamut" sections.

# Verification Notes

- Definition source: Error table reproduced from source; verdict quotes are direct from "What about existing models?" bullet list.
- Confidence rationale: High \u2014 quantitative data and qualitative verdicts are all explicit in the source.
- Uncertainties: The error data was generated against CAM16-derived test data, which the source acknowledges may not perfectly represent human perception.
- Cross-reference status: Verified against table, Munsell plots description, and blending description.
- Rosetta Stone check: No rosetta stone mappings.
- OCR issues: Markdown table extracted successfully; HTML div columns with images ignored.
