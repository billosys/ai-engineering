---
concept: Chroma (Perceptual)
slug: chroma-perceptual
category: colour-theory
subcategory: perceptual colour attributes
tier: intermediate
layer: 2-domain
source: "A Perceptual Color Space for Image Processing"
source_slug: posts
authors: "Bj\u00f6rn Ottosson"
chapter: "The Oklab color space"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - []
prerequisites:
  - oklab
  - perceptual-uniformity
extends:
  - []
related:
  - lightness-perceptual
  - colour-space-comparison
  - colour-interpolation-perceptual
contrasts_with:
  - []
answers_questions:
  - "What distinguishes chroma from saturation in perceptual colour models?"
  - "How do you construct a palette that changes lightness uniformly across hues?"
rosetta_stone: []
css_implementation:
  - property: "color"
    example: "color: oklch(70% 0.15 200);"
    support: baseline
---

# Quick Definition

Chroma is the perceptual magnitude of a colour's colourfulness, measured as the distance from the neutral (grey) axis in a perceptual colour space \u2014 distinct from saturation, which is relative colourfulness scaled to lightness.

# Core Definition

The source introduces chroma as the C coordinate in Oklab's polar (LCh) form. Chroma is defined geometrically as:

C = sqrt(a\u00b2 + b\u00b2)

where a and b are the Oklab Cartesian coordinates (red-green and blue-yellow axes respectively). The source links to the Wikipedia definition of chroma (colorfulness) and distinguishes it from saturation implicitly by framing it as an absolute distance in colour space rather than a ratio relative to lightness.

The source's requirements state that a perceptual colour space should "predict lightness, chroma and hue well. L, C and h should be perceived as orthogonal, so one can be altered without affecting the other two."

# Prerequisites

- **Oklab** \u2014 Chroma in this source is defined specifically within Oklab (and LCh polar form).
- **Perceptual uniformity** \u2014 Chroma's value as a concept depends on the space being perceptually uniform; otherwise equal C steps do not equal equal perceived colourfulness steps.

# Key Properties

1. Chroma is the Euclidean distance from the achromatic axis in the ab plane of Oklab.
2. Achromatic colours (greys, black, white) have C = 0.
3. Increasing C while holding L and h constant makes a colour appear more colourful without shifting its perceived lightness or hue.
4. Chroma is an absolute measure of colourfulness; saturation is relative (chroma divided by lightness).
5. In Oklab, C for typical sRGB colours ranges from 0 to approximately 0.4, with fully saturated colours near the edges of the sRGB gamut having the highest values.

# Construction / Recognition

## To Construct/Create:
1. Convert a colour to Oklab (L, a, b).
2. Compute C = sqrt(a\u00b2 + b\u00b2).
3. Optionally compute hue: h = atan2(b, a).
4. To construct a colour at a specific chroma: set a = C\u00b7cos(h), b = C\u00b7sin(h).

## To Identify/Recognise:
1. Chroma = 0: pure grey (a=0, b=0 at any L).
2. Chroma increases as a colour becomes more saturated.
3. In a Munsell-like plot in Oklab, equal-chroma colours form approximate circles in the ab plane.

# Context & Application

- **Typical contexts**: Palette design (holding C constant across hues produces uniformly colourful palettes); increasing colourfulness in image processing.
- **Common applications**: CSS `oklch()` where the second parameter is chroma; colour picker interfaces that separate colourfulness from lightness.

# Examples

**Example 1** (from source): The hue gradient comparison shows Oklab with constant C and L across all hues appearing visually even, while HSV at constant value and saturation appears highly uneven in perceived lightness and colourfulness. (Section: "Comparing Oklab to HSV")

**Example 2** (from source): Munsell data plotted in Oklab forms approximate circles in the ab plane (chroma as radius), while other spaces (CIELAB, CIELUV, IPT) show squashed or distorted circles, demonstrating better chroma prediction by Oklab. (Section: "Munsell data")

# Relationships

## Builds Upon
- **Oklab** \u2014 Chroma is derived from Oklab's a and b coordinates.
- **Perceptual uniformity** \u2014 Chroma is only meaningful as a perceptual quantity if the underlying space is uniform.

## Enables
- **Colour interpolation (perceptual)** \u2014 Holding C constant during hue interpolation produces transitions without desaturation artefacts.
- **Palette design** \u2014 Constant-C, varying-h, varying-L palettes can be systematically designed.

## Related
- **Lightness (perceptual)** \u2014 Chroma and lightness are orthogonal axes in Oklab; changing one should not appear to change the other.
- **Hue** \u2014 Chroma and hue together define the chromaticity in LCh polar form.

## Contrasts With
- **Saturation (HSV/HSL)** \u2014 Saturation is relative (chroma/lightness ratio); HSV saturation is not perceptually uniform. The source notes that HSV "does not meet any of the requirements" for perceptual uniformity.

# Common Errors

- **Error**: Using HSV saturation as a proxy for perceptual chroma.
  **Correction**: HSV saturation is not perceptually uniform \u2014 equal saturation steps in HSV produce very different perceived colourfulness changes. Use Oklab C instead.

# Common Confusions

- **Confusion**: Chroma and saturation are synonyms.
  **Clarification**: In perceptual colour science, chroma is absolute colourfulness from the neutral axis; saturation is chroma relative to lightness. The source links specifically to the Wikipedia "colorfulness" article when introducing chroma, signalling this distinction.

# Source Reference

"The Oklab color space" (C formula); "Munsell data" (chroma prediction comparison); comparison table in "Comparison with other color spaces".

# Verification Notes

- Definition source: Formula C = sqrt(a\u00b2+b\u00b2) is explicit in the source. The distinction from saturation is inferred from the Wikipedia link and the source's consistent use of "chroma" alongside "lightness" and "hue" as orthogonal perceptual attributes.
- Confidence rationale: High \u2014 formula and context are explicit; the saturation distinction is strongly implied.
- Uncertainties: The source does not give an explicit numerical range for C in sRGB colours; the approximate range stated in Key Properties was inferred from the example table values and colour science convention.
- Cross-reference status: Verified against LCh formula, Munsell discussion, and comparison table.
- Rosetta Stone check: No rosetta stone mappings.
- OCR issues: None significant.
