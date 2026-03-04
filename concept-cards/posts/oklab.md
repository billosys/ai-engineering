---
concept: Oklab Colour Space
slug: oklab
category: colour-theory
subcategory: perceptual colour models
tier: foundational
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
  - perceptual-uniformity
  - colour-space
  - xyz-colour-space
extends:
  - perceptual-uniformity
related:
  - lms-cone-responses
  - d65-whitepoint
  - chroma-perceptual
  - lightness-perceptual
  - colour-interpolation-perceptual
  - oklab-conversion
  - colour-space-comparison
contrasts_with:
  - colour-space-comparison
answers_questions:
  - "What makes a colour space perceptually uniform, and why does it matter for design?"
  - "How do you construct a palette that changes lightness uniformly across hues?"
  - "How do you convert between colour spaces for image processing?"
rosetta_stone: []
css_implementation:
  - property: "color"
    example: "color: oklab(0.7 0.1 -0.08);"
    support: baseline
  - property: "color"
    example: "color: oklch(70% 0.15 200);"
    support: baseline
---

# Quick Definition

Oklab is a perceptual colour space designed by Bj\u00f6rn Ottosson that represents colours with three coordinates (L, a, b) where equal numerical distances correspond to equal perceived differences in lightness, chroma, and hue.

# Core Definition

Ottosson describes Oklab as "a new perceptual color space, designed to be simple to use, while doing a good job at predicting perceived lightness, chroma and hue." The name means "an OK Lab color space." A colour in Oklab is represented with three coordinates:

- **L** \u2014 perceived lightness
- **a** \u2014 how green/red the colour is
- **b** \u2014 how blue/yellow the colour is

Oklab uses a D65 whitepoint, matching sRGB and other common colour spaces. It can also be expressed in polar form as LCh (lightness, chroma, hue), where:

C = sqrt(a\u00b2 + b\u00b2), h\u00b0 = atan2(b, a)

Oklab was derived by optimising the matrices M1 and M2 (3\u00d73) and the exponent \u03b3 = 1/3 to minimise prediction errors across datasets for lightness, chroma, and hue simultaneously \u2014 following the same computational structure as IPT but calibrated to match CAM16-UCS performance.

# Prerequisites

- **Perceptual uniformity** \u2014 Oklab is defined as an attempt to achieve this property; understanding what it means is essential for understanding why Oklab exists.
- **Colour space (general concept)** \u2014 Oklab is a colour space; the general concept of coordinate-based colour representation is assumed.
- **XYZ colour space** \u2014 The conversion pipeline from sRGB to Oklab goes through XYZ; the intermediate representation is XYZ.

# Key Properties

1. Perceptually uniform: equal distances in L, a, b correspond to equal perceived colour differences.
2. Uses D65 whitepoint, matching sRGB, Display P3, and Rec. 2020.
3. Numerically simple: composed of two 3\u00d73 matrix multiplications and a cube-root non-linearity (\u03b3 = 1/3).
4. L and C axes are orthogonal \u2014 changing lightness does not change hue, and vice versa.
5. Blending two colours in Oklab coordinates produces visually even transitions without unexpected hue shifts.

# Construction / Recognition

## To Construct/Create:
1. Start with a linear sRGB colour (gamma-decoded).
2. Multiply by the first matrix M1 to produce approximate cone responses (l, m, s).
3. Apply cube-root non-linearity: l' = l^(1/3), m' = m^(1/3), s' = s^(1/3).
4. Multiply by the second matrix M2 to produce (L, a, b).
5. Optionally convert to LCh polar form: C = sqrt(a\u00b2 + b\u00b2), h = atan2(b, a).

## To Identify/Recognise:
1. Three-channel Lab-like space with L \u2208 [0, 1] for colours within the sRGB gamut.
2. D65 white maps to (L=1, a=0, b=0).
3. Typical sRGB red maps to approximately (L=0.63, a=0.22, b=0.13) \u2014 highly saturated colours have large a or b magnitude.

# Context & Application

- **Typical contexts**: Gradient generation, palette design, image saturation adjustment, greyscale conversion, colour pickers, game engine colour systems.
- **Common applications**: Now the default gradient interpolation method in Photoshop; part of CSS Color Level 4/5 (supported by major browsers as `oklab()` and `oklch()`); used in Unity gradients and Godot's colour picker.

# Examples

**Example 1** (from source): An Oklab gradient with varying hue, constant lightness (L) and chroma (C) appears even and uniform. By contrast, an HSV gradient with constant value and saturation shows yellow, magenta, and cyan dramatically lighter than red and blue. (Section: "Comparing Oklab to HSV")

**Example 2** (from source): The quantitative error table shows Oklab achieving the lowest L RMS (0.20) and C RMS (0.81) of all tested colour spaces except CAM16-UCS (the source of training data). (Section: "Comparison with other color spaces")

**Example 3** (from source): Blending white with blue in Oklab produces no hue shift toward purple \u2014 unlike CIELAB, CIELUV, and HSV, which all show a purple shift when blending blue. (Section: "Blending colors")

# Relationships

## Builds Upon
- **Perceptual uniformity** \u2014 Oklab is built to achieve this.
- **XYZ colour space** \u2014 The conversion route passes through XYZ.
- **LMS cone responses** \u2014 M1 converts XYZ to approximate cone responses as an intermediate step.
- **IPT colour space** \u2014 Oklab adopts IPT's computational structure (matrix \u00d7 cube-root \u00d7 matrix).
- **CAM16-UCS** \u2014 Oklab's training data was generated from CAM16, and Oklab is calibrated to match CAM16's lightness and chroma predictions.

## Enables
- **Colour interpolation (perceptual)** \u2014 Oklab coordinates can be linearly interpolated to produce perceptually smooth gradients.
- **Uniform palette construction** \u2014 Holding L and C constant while varying h produces a hue palette with equal perceived lightness.
- **CSS colour functions** \u2014 `oklab()` and `oklch()` in CSS Color Level 4/5.

## Related
- **CIELAB** \u2014 Same coordinate structure (L, a, b with a D65 whitepoint), but CIELAB has inferior hue uniformity, especially for blues.
- **Chroma (perceptual)** \u2014 C in the LCh polar form.
- **Lightness (perceptual)** \u2014 L is the first coordinate.

## Contrasts With
- **HSL / HSV** \u2014 These do not predict perceptual uniformity at all; the source rates HSV as meeting none of the requirements.
- **CIELAB** \u2014 Shares the coordinate structure but Oklab has substantially lower lightness and chroma prediction error.
- **CAM16-UCS** \u2014 Higher overall perceptual accuracy but poor numerical behaviour and bad blending due to chroma compression.

# Common Errors

- **Error**: Using Oklab coordinates on gamma-encoded (standard) sRGB values rather than linear sRGB.
  **Correction**: The conversion formula requires linear sRGB input. Gamma must be decoded first (see Ottosson's prior post on the topic).

- **Error**: Assuming Oklab and CIELAB are interchangeable because they share the L, a, b coordinate names.
  **Correction**: The matrix coefficients and the intermediate LMS step differ significantly; values are not compatible between the two spaces.

# Common Confusions

- **Confusion**: "OK" in Oklab is an informal quality rating \u2014 it's just acceptable.
  **Clarification**: Per the source, "it is called the Oklab color space, because it is an OK Lab color space" \u2014 the "OK" is a deliberate understatement, since the space performs substantially better than CIELAB on lightness and chroma metrics.

- **Confusion**: Oklab and OKLch are different colour spaces.
  **Clarification**: OKLch (or Oklch) is merely Oklab expressed in polar form \u2014 same space, cylindrical coordinates.

# Source Reference

"The Oklab color space", "Implementation", "How Oklab was derived", "Comparison with other color spaces" sections.

# Verification Notes

- Definition source: Direct quotes from "The Oklab color space" section; coordinate descriptions and formulae from Implementation section.
- Confidence rationale: High \u2014 Oklab is the primary subject of the entire article; definition, equations, and context are all explicit.
- Uncertainties: Numerical ranges of typical L, a, b values were inferred from the example table (XYZ/Oklab pairs), not stated as ranges in prose.
- Cross-reference status: Verified against example table, comparison table, and C++ code listing.
- Rosetta Stone check: No rosetta stone mapping for Oklab itself (it is the subject, not an analogy); mappings are on perceptual-uniformity card.
- OCR issues: HTML anchor-link fragments and base64 SVG strings present throughout; ignored.
