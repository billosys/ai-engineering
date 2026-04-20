---
concept: Lightness (Perceptual, L Axis)
slug: lightness-perceptual
category: visual-perception
subcategory: perceptual colour attributes
tier: intermediate
layer: 0-perception
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
  - chroma-perceptual
  - colour-space-comparison
  - colour-interpolation-perceptual
contrasts_with:
  - []
answers_questions:
  - "What makes a colour space perceptually uniform, and why does it matter for design?"
  - "How do you construct a palette that changes lightness uniformly across hues?"
rosetta_stone: []
css_implementation:
  - property: "color"
    example: "color: oklch(70% 0.15 200);"
    support: baseline
---

# Quick Definition

Perceived lightness (L) is the first coordinate in Oklab, representing a colour's apparent brightness relative to white, where L=0 is black and L=1 is the D65 whitepoint.

# Core Definition

The source defines the L coordinate simply: "L \u2013 perceived lightness." In Oklab, L=0 corresponds to black and L=1 corresponds to D65 white (confirmed by the example table: D65 XYZ maps to L=1.000).

The source's requirements state that lightness should be predictable: "L, C and h should be perceived as orthogonal, so one can be altered without affecting the other two. This is useful for things like turning an image black and white and increasing colorfulness without introducing hue shifts."

The source provides quantitative evidence: Oklab achieves L RMS = 0.20 against CAM16-generated equal-lightness test data, compared to CIELAB at 1.70 and HSV at 11.59.

# Prerequisites

- **Oklab** \u2014 L is the first coordinate of Oklab; the space must be understood.
- **Perceptual uniformity** \u2014 L is only a reliable lightness measure if the space is perceptually uniform.

# Key Properties

1. L=0 is black; L=1 is D65 white.
2. L is perceptually orthogonal to chroma (C) and hue (h): changing L should not appear to change hue or colourfulness.
3. Equal steps in L correspond to equal perceived lightness differences (perceptual uniformity).
4. Oklab's L has the lowest RMS error against CAM16 lightness predictions of all tested spaces except CAM16 itself.
5. A cube-root non-linearity (\u03b3 = 1/3) in the conversion pipeline produces the approximately linear perceptual response of L.

# Construction / Recognition

## To Construct/Create:
1. Convert a colour to Oklab using the M1 \u2192 cube root \u2192 M2 pipeline.
2. The first component of the result is L.
3. To create a greyscale version of an image: keep L for each pixel, set a=0, b=0, convert back.

## To Identify/Recognise:
1. L \u2208 [0, 1] for colours within the sRGB gamut.
2. Achromatic greys lie on the L axis with a=0, b=0.
3. When varying hue or chroma, L should remain visually constant if the space is perceptually uniform.

# Context & Application

- **Typical contexts**: Greyscale conversion; contrast checking; accessibility (WCAG contrast ratios require lightness comparison); palette construction with predictable lightness steps.
- **Common applications**: Turning an image grayscale while preserving perceived lightness (set a=0, b=0 in Oklab); CSS `oklch()` first parameter; generating tonal scales for design systems.

# Examples

**Example 1** (from source): The hue gradient example demonstrates that Oklab at constant L produces a visually even-brightness strip across all hues, while HSV at constant value shows yellow, magenta, and cyan appearing much lighter than red and blue. A lightness plot of the HSV gradient confirms the dramatic L variation. (Section: "Comparing Oklab to HSV")

**Example 2** (from source): From the error table, Oklab achieves L 95th percentile error = 0.44 vs. CIELAB = 3.16 and HSV = 23.17, confirming L is far better calibrated to perception in Oklab. (Section: "Comparison with other color spaces")

# Relationships

## Builds Upon
- **Oklab** \u2014 L is derived from Oklab's conversion pipeline.
- **Perceptual uniformity** \u2014 L is the lightness axis of a perceptually uniform space.
- **LMS cone responses + cube-root non-linearity** \u2014 The cube root applied to cone responses is what produces the approximately linear perceptual response.

## Enables
- **Greyscale conversion** \u2014 Setting a=0, b=0 in Oklab produces a greyscale colour at the original perceived lightness.
- **Palette construction** \u2014 Tonal scales (varying L, fixed h and C) produce palettes with uniform perceived brightness steps.
- **Colour interpolation** \u2014 Linear interpolation of L produces smooth lightness transitions.

## Related
- **Chroma (perceptual)** \u2014 The complementary axis; L and C are orthogonal in Oklab.
- **D65 whitepoint** \u2014 L=1 is defined as D65 white.

## Contrasts With
- **HSV Value** \u2014 HSV Value is not a perceptual lightness measure; it is simply the maximum of the R, G, B channels and has no perceptual uniformity.
- **Luminance (Y in XYZ)** \u2014 Y is a physical luminance measure, not perceptually uniform; L is a cube-root-compressed, perceptually linearised version.

# Common Errors

- **Error**: Using HSV Value or sRGB channel average as a proxy for perceived lightness.
  **Correction**: These measures are not perceptually uniform. Use L from Oklab (or CIELAB as a second choice) for tasks requiring consistent perceived lightness.

# Common Confusions

- **Confusion**: L in Oklab and L* in CIELAB are the same.
  **Clarification**: Both represent perceived lightness and both range from 0 to 100 (CIELAB) or 0 to 1 (Oklab), but they are computed differently. Oklab's L achieves substantially lower prediction error against CAM16 than CIELAB's L*.

# Source Reference

"The Oklab color space" (definition); "Comparing Oklab to HSV" (visual demonstration); "Comparison with other color spaces" (error table).

# Verification Notes

- Definition source: "L \u2014 perceived lightness" is a direct quote. L=0 to L=1 range inferred from example table (D65 \u2192 L=1.000).
- Confidence rationale: High \u2014 the concept is central, defined explicitly, and extensively demonstrated with quantitative data.
- Uncertainties: The source does not give an explicit formula for L in isolation from the full pipeline.
- Cross-reference status: Verified against example table, error table, and gradient comparison.
- Rosetta Stone check: No rosetta stone mappings.
- OCR issues: None significant.
