---
concept: "Lightness (Perceptual, L Axis)"
slug: "lightness-perceptual"
category: "visual-perception"
subcategory: "perceptual colour attributes"
tier: "intermediate"
layer: "0-perception"
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
  - "oklab"
  - "perceptual-uniformity"
extends: []
related:
  - "chroma-perceptual"
  - "colour-space-comparison"
  - "colour-interpolation-perceptual"
contrasts_with: []
answers_questions:
  - "What makes a colour space perceptually uniform, and why does it matter for design?"
  - "How do you construct a palette that changes lightness uniformly across hues?"
rosetta_stone: []
css_implementation:
  -
    property: "color"
    example: "color: oklch(70% 0.15 200);"
    support: "baseline"
---

# Quick Definition
Oklab L is the lightness coordinate of that model; it is not XYZ Y, WCAG relative luminance, CIELAB L*, or HSV V.

# Core Definition
Oklab L is produced by the model's complete conversion, including its nonlinear stage. For neutral inputs it supports useful approximate tonal construction, but for arbitrary chromatic colours it is not simply cbrt(Y), nor a direct measure of display brightness or WCAG relative luminance. Approximate uniformity does not guarantee equal-looking L steps. Choose palette candidates, check target gamut/rendering, and calculate WCAG contrast from the actual rendered sRGB foreground/background pair.

# Prerequisites

- **Oklab** — L is the first coordinate of Oklab; the space must be understood.
- **Perceptual uniformity** — L is only a reliable lightness measure if the space is perceptually uniform.

# Key Properties
1. L is an Oklab model coordinate and depends on its defined conversion/reference.
2. It differs from XYZ Y, CIELAB L*, HSV V and WCAG relative luminance.
3. Neutral/grey ramps can be constructed approximately from L, followed by gamut and render checks.
4. L alone cannot certify contrast; use the rendered sRGB pair procedure in the accepted colour guide.

# Construction / Recognition
## To Construct/Create:
1. Choose contextual L/C/h candidates for the intended task.
2. Check each converted colour against target gamut and inspect its rendering.
3. Calculate contrast for each actual foreground/background sRGB pair using the accepted colour-guide procedure; adjust as needed. L cannot certify contrast.

## To Identify/Recognise:
1. Oklab L is a model lightness coordinate, not XYZ Y, CIELAB L*, HSV V or WCAG relative luminance.
2. A constant-L hue sweep is a coordinate construction; its rendered appearance may vary with hue, gamut and context.

# Context & Application

- **Typical contexts**: Greyscale conversion; contrast checking; accessibility (WCAG contrast ratios require lightness comparison); palette construction with predictable lightness steps.
- **Common applications**: Turning an image grayscale while preserving perceived lightness (set a=0, b=0 in Oklab); CSS `oklch()` first parameter; generating tonal scales for design systems.

# Examples
**Example 1** (source description): Ottosson describes a constant-L Oklab hue sweep and compares it with HSV. This is an attributed example; its image was not independently inspected and it is not a universal appearance claim. (Section: “Comparing Oklab to HSV”)

# Relationships

## Builds Upon
- **Oklab** — L is derived from Oklab's conversion pipeline.
- **Perceptual uniformity** — L is the lightness axis of a perceptually uniform space.
- **LMS cone responses + cube-root non-linearity** — The cube root applied to cone responses is what produces the approximately linear perceptual response.

## Enables
- **Greyscale conversion** — Setting a=0, b=0 in Oklab produces a greyscale colour at the original perceived lightness.
- **Palette construction** — Tonal scales (varying L, fixed h and C) produce palettes with uniform perceived brightness steps.
- **Colour interpolation** — Linear interpolation of L produces smooth lightness transitions.

## Related
- **Chroma (perceptual)** — C is a distinct coordinate; coordinate distinction does not guarantee perceptual independence.
- **D65 whitepoint** — L=1 is defined as D65 white.

## Contrasts With
- **HSV Value** — HSV Value is not a perceptual lightness measure; it is simply the maximum of the R, G, B channels and has no perceptual uniformity.
- **Luminance (Y in XYZ)** — Y is a physical luminance measure, not perceptually uniform; L is a cube-root-compressed, perceptually linearised version.

# Common Errors
- **Error**: Using an L value or L difference as a WCAG contrast test.
  **Correction**: Compute the criterion from the actual rendered sRGB pair.
- **Error**: Treating Oklab L as cbrt(Y) for chromatic colours.
  **Correction**: Apply the complete model conversion; the opponent channels and nonlinear stage matter.

# Common Confusions

- **Confusion**: L in Oklab and L* in CIELAB are the same.
  **Clarification**: Both represent perceived lightness and both range from 0 to 100 (CIELAB) or 0 to 1 (Oklab), but they are computed differently. Oklab's L achieves substantially lower prediction error against CAM16 than CIELAB's L*.

# Source Reference

"The Oklab color space" (definition); "Comparing Oklab to HSV" (visual demonstration); "Comparison with other color spaces" (error table).

# Verification Notes
The model distinction follows Ottosson's conversion and CSS Color 4 §§9–10. Pair evaluation follows the retained Slice16 colour-guide method; it is not a fresh browser or accessibility test.
