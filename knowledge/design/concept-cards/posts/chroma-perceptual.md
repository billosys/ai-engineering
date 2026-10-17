---
concept: "Chroma (Perceptual)"
slug: "chroma-perceptual"
category: "colour-theory"
subcategory: "perceptual colour attributes"
tier: "intermediate"
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
  - "oklab"
  - "perceptual-uniformity"
extends: []
related:
  - "lightness-perceptual"
  - "colour-space-comparison"
  - "colour-interpolation-perceptual"
contrasts_with: []
answers_questions:
  - "What distinguishes chroma from saturation in perceptual colour models?"
  - "How do you construct a palette that changes lightness uniformly across hues?"
rosetta_stone: []
css_implementation:
  -
    property: "color"
    example: "color: oklch(70% 0.15 200);"
    support: "baseline"
---

# Quick Definition
Chroma in Oklab is C = hypot(a, b), the radial coordinate in its a–b plane. This model-specific coordinate is not a universal appearance step or a saturation ratio.

# Core Definition
The source defines Oklab polar chroma from Cartesian coordinates as C = sqrt(a²+b²), with hue obtained from atan2(b,a). This is an exact coordinate relation within Oklab. Its perceptual interpretation is an approximate correlate, conditioned by the model and viewing context. The source's stated goal that L, C and h be perceived as orthogonal describes a design aim, not a guarantee for every hue, display or gamut.

CIE terminology distinguishes chroma from saturation: chroma relates colourfulness to a similarly illuminated achromatic reference; saturation relates colourfulness to the stimulus's own brightness. These appearance terms do not license a general C/L formula. HSL and HSV parameters called “saturation” are model-specific quantities.

# Prerequisites

- **Oklab** — Chroma in this source is defined specifically within Oklab (and LCh polar form).
- **Perceptual uniformity** — Chroma's value as a concept depends on the space being perceptually uniform; otherwise equal C steps do not equal equal perceived colourfulness steps.

# Key Properties
1. C = hypot(a,b); C=0 when a=b=0, where polar hue is undefined.
2. C is measured in the chosen Oklab coordinates; it is not a universal absolute colourfulness scale.
3. Varying C while fixing L and hue changes the model coordinates as intended, but does not guarantee unchanged perceived lightness/hue or equal-looking steps.
4. CSS OkLCh's percentage reference of 0.4 is a syntax scale, not a maximum chroma. Reachable chroma depends on lightness, hue and destination gamut.

# Construction / Recognition

## To Construct/Create:
1. Convert the colour to Oklab (L,a,b) using the intended reference and conversion.
2. Compute C = hypot(a,b); when C>0, h = atan2(b,a), converted to the desired angle unit.
3. Recover a=C cos(h), b=C sin(h), converting degrees to radians where required.
4. Check the resulting colour against the intended output gamut and rendering.

## To Identify/Recognise:
1. C=0 identifies the neutral axis in these coordinates; hue is undefined there.
2. A constant-C locus is a circle in the Oklab a–b plane by definition. This geometry alone does not establish equal perceived colourfulness in every condition.

# Context & Application
- **Typical contexts**: Comparing or constructing Oklab coordinates in palette tools and colour models.
- **Common applications**: CSS `oklch()` uses a chroma coordinate; select candidates, check destination gamut/rendering, then assess actual foreground/background pairs when contrast matters.

# Examples
**Example 1** (source description, not an independent visual inspection): Ottosson describes an Oklab hue sweep with fixed L and C and varying hue, and compares it with an HSV sweep. This is an attributed example, not a guarantee for arbitrary output devices or a claim that the embedded image was inspected. (Section: “Comparing Oklab to HSV”)

**Example 2** (source description): The article describes Oklab Munsell data plotted as approximately circular in the a–b plane. This is evidence from the stated dataset and plot, not a universal result. (Section: “Munsell data”)

# Relationships

## Builds Upon
- **Oklab** — The coordinate model that defines a and b.

## Enables
- **Colour interpolation (perceptual)** — C can be one chosen coordinate to hold or vary; the path still requires gamut and appearance checks.
- **Palette design** — Supports candidate construction in explicit model coordinates, not a universal palette recipe.

## Related
- **Lightness (perceptual)** — L and C are distinct coordinates in Oklab; coordinate independence does not guarantee perceptual independence.
- **Hue** — Along with L and C, hue describes the polar form when C is nonzero.

## Contrasts With
- **Saturation (HSV/HSL)** — CIE appearance saturation and model parameters labelled HSL/HSV saturation are distinct; neither is generally C/L.

# Common Errors
- **Error**: Treating a constant-C hue sweep as equally colourful and displayable everywhere.
  **Correction**: Treat it as a coordinate construction; check target gamut, rendering, and the intended viewing context.
- **Error**: Using `C/L` as a universal saturation definition.
  **Correction**: Distinguish the CIE appearance term from model-specific HSL/HSV parameters and from Oklab C.

# Common Confusions
- **Confusion**: Chroma is an absolute, context-free amount of colourfulness.
  **Clarification**: The formula is exact for the coordinate system; its perceptual interpretation is model- and condition-dependent. The source's Wikipedia link does not establish a C/L saturation law.

# Source Reference

"The Oklab color space" (C formula); "Munsell data" (chroma prediction comparison); comparison table in "Comparison with other color spaces".

# Verification Notes
- The formula and Oklab coordinate reading are explicit in the prepared article. The CIE distinction follows CIE S 017:2020 entries 17-22-073 and 17-22-074.
- Predecessor extraction confidence is preserved as historical metadata; it is not a new evidence grade.
- Current technical support is limited to the stated formula, terminology distinction, and attributed article examples. No original capture, browser behaviour, or embedded plots were independently verified.
