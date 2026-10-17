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
- **Perceptual uniformity** — Oklab is fitted to approximate perceptual behaviour; that approximation informs interpretation of L but is not a precondition for calculating or using this model coordinate.

# Key Properties
1. L is an Oklab model coordinate and depends on its defined conversion/reference.
2. It differs from XYZ Y, CIELAB L*, HSV V and WCAG relative luminance.
3. Neutral/grey ramps can be constructed approximately from L, followed by gamut and render checks.
4. L alone cannot certify contrast; use the rendered sRGB pair procedure in the accepted colour guide.

# Construction / Recognition
## To Construct/Create:
1. Choose contextual L_start, L_end and an integer n>0. For i=0…n, compute L_i=L_start+i(L_end−L_start)/n; this gives n+1 targets with equal numeric Oklab L steps.
2. Apply the chosen L targets across the intended hues, selecting contextual C values for each candidate; equal numeric L steps do not promise equal perceived appearance.
3. Convert candidates, check destination gamut/mapping and inspect rendering. Calculate contrast for each actual foreground/background sRGB pair using the accepted colour-guide procedure. Adjust as needed and report adjustments rather than presenting them as uniform L steps.

## To Identify/Recognise:
1. Oklab L is a model lightness coordinate, not XYZ Y, CIELAB L*, HSV V or WCAG relative luminance.
2. A constant-L hue sweep is a coordinate construction; its rendered appearance may vary with hue, gamut and context.

# Context & Application

- **Typical contexts**: Approximate neutral-ramp construction, palette candidates and contrast review. WCAG contrast is calculated from the relative luminance of the actual rendered foreground/background pair, not by comparing Oklab L values.
- **Common applications**: Constructing a neutral Oklab coordinate at the chosen model L by setting a=b=0; the resulting appearance is approximate and requires output, gamut and viewing-context checks. CSS `oklch()` first parameter; generating tonal-scale candidates for design systems.

# Examples
**Example 1** (source description): Ottosson describes a constant-L Oklab hue sweep and compares it with HSV. This is an attributed example; its image was not independently inspected and it is not a universal appearance claim. (Section: “Comparing Oklab to HSV”)

# Relationships
## Builds Upon
- **Oklab** — L is its model lightness coordinate.
- **Perceptual uniformity** — The model aims for approximate agreement with perception.
- **LMS-like intermediate and cube-root stage** — Part of the article's conversion, not a universal physiological explanation.

## Enables
- **Greyscale construction** — Setting a=b=0 constructs a neutral model coordinate; check target encoding/rendering.
- **Palette construction** — L/C/h values provide candidates; check gamut, rendering and actual contrast pairs.
- **Colour interpolation** — L may be interpolated as a coordinate; appearance remains context-dependent.

## Related
- **Chroma (perceptual)** — C is a distinct coordinate, not guaranteed perceptually independent.
- **D65 whitepoint** — The normalized reference white maps approximately to L=1.

## Contrasts With
- **HSV Value** — A different model parameter, not an equivalent perceptual lightness measure.
- **XYZ Y / WCAG relative luminance** — Different quantities; compute contrast from rendered sRGB pairs.

# Common Errors
- **Error**: Using an L value or L difference as a WCAG contrast test.
  **Correction**: Compute the criterion from the actual rendered sRGB pair.
- **Error**: Treating Oklab L as cbrt(Y) for chromatic colours.
  **Correction**: Apply the complete model conversion; the opponent channels and nonlinear stage matter.

# Common Confusions

- **Confusion**: A lower reported Oklab L error establishes universal superiority to CIELAB.
  **Clarification**: The article reports generated CAM16 lightness data and a separate perceived-hue dataset used to derive IPT. Its lightness comparison is scoped to that generated dataset and error method; it is not a general ranking or independent human-ground-truth result.

# Source Reference

"The Oklab color space" (definition); "Comparing Oklab to HSV" (visual demonstration); "Comparison with other color spaces" (error table).

# Verification Notes
The model distinction follows Ottosson's conversion and CSS Color 4 §§9–10. Pair evaluation follows the retained Slice16 colour-guide method; it is not a fresh browser or accessibility test.
