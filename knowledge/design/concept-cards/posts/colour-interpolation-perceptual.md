---
concept: Colour Interpolation (Perceptual)
slug: colour-interpolation-perceptual
category: colour-theory
subcategory: colour operations
tier: intermediate
layer: 2-domain
source: "A Perceptual Color Space for Image Processing"
source_slug: posts
authors: "Bj\u00f6rn Ottosson"
chapter: "Blending colors"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - []
prerequisites:
  - oklab
  - perceptual-uniformity
  - oklab-conversion
extends:
  - perceptual-uniformity
related:
  - chroma-perceptual
  - lightness-perceptual
  - colour-space-comparison
contrasts_with:
  - []
answers_questions:
  - "How do you construct a palette that changes lightness uniformly across hues?"
  - "What makes a colour space perceptually uniform, and why does it matter for design?"
rosetta_stone:
  - domain: music
    concept: "Glissando / pitch slide in equal temperament"
    rating: structural
    note: "A glissando through equal-tempered semitones sounds even; linear interpolation through Oklab coordinates looks even. Non-uniform spaces produce the auditory equivalent of a glissando that jumps pitch unevenly."
css_implementation:
  - property: "color-interpolation"
    example: "@keyframes fade { to { color: oklab(0.9 0 0); } } /* interpolates in Oklab */"
    support: experimental
  - property: "background"
    example: "background: linear-gradient(in oklch, red, blue);"
    support: baseline
---

# Quick Definition

Perceptual colour interpolation is linear blending of colour coordinates in a perceptually uniform space (such as Oklab), producing transitions where each intermediate step appears visually halfway between the endpoints.

# Core Definition

The source identifies even colour transitions as a core requirement of a perceptual colour space: "Blending two colors should result in even transitions. The transition colors should appear to be in between the blended colors (e.g. passing through a warmer color than either original color is not good)."

The source demonstrates this with blending plots: white blended with blue in Oklab coordinates produces a smooth, hue-stable transition. The same blend in CIELAB, CIELUV, and HSV all show a hue shift toward purple. CAM16's chroma compression causes it to desaturate rapidly, producing a different kind of unevenness.

Perceptual interpolation is simply linear interpolation (lerp) of the colour coordinates in the perceptual space:

colour(t) = (1-t) \u00d7 colour_A + t \u00d7 colour_B, for t \u2208 [0, 1]

The perceptual uniformity of the space is what makes linear interpolation visually smooth.

# Prerequisites

- **Oklab** \u2014 The interpolation is performed in Oklab coordinates.
- **Perceptual uniformity** \u2014 Only meaningful in a uniform space; in a non-uniform space, linear interpolation produces uneven visual transitions.
- **Oklab conversion** \u2014 Colours must be converted to Oklab before interpolation and back to sRGB for display.

# Key Properties

1. Interpolation is linear arithmetic in Oklab (L, a, b) or LCh (L, C, h) coordinates.
2. The visual result is smooth and even \u2014 no unexpected hue shifts or lightness jumps.
3. In non-uniform spaces (HSV, sRGB), the same arithmetic interpolation produces visually uneven transitions.
4. For hue interpolation in LCh, the shortest path through hue angle is usually preferred (wrapping at 360\u00b0).
5. This is now the default method for gradients in Photoshop and CSS Level 4/5 (`linear-gradient(in oklab, ...)` or `in oklch`).

# Construction / Recognition

## To Construct/Create:
1. Convert both endpoint colours from sRGB to Oklab: (L1, a1, b1) and (L2, a2, b2).
2. For each step t \u2208 [0, 1]: L(t) = L1 + t\u00b7(L2-L1), a(t) = a1 + t\u00b7(a2-a1), b(t) = b1 + t\u00b7(b2-b1).
3. Convert each interpolated (L(t), a(t), b(t)) back to linear sRGB, then apply gamma encoding.
4. Alternatively, interpolate in LCh: L(t), C(t), h(t) \u2014 useful for "constant chroma" hue rotations.

## To Identify/Recognise:
1. A perceptually smooth gradient appears even in lightness and colourfulness across all steps.
2. A non-perceptual gradient (e.g., sRGB interpolation) shows a dip toward grey or an unexpected hue in the middle.

# Context & Application

- **Typical contexts**: CSS gradients (`linear-gradient(in oklch, ...)`); colour palette generation; image blending; gradient maps in image editing.
- **Common applications**: Photoshop gradient interpolation (now defaults to Oklab); CSS Level 4/5 gradient colour interpolation; design token gradient scales.

## Cross-Domain Connections

**Music \u2192 STRUCTURAL**: A glissando through equal-tempered pitches sounds even because equal temperament guarantees uniform perceptual steps between semitones. Linear interpolation through Oklab coordinates is visually even for the same reason \u2014 the space is calibrated so that equal steps equal equal perceptual differences. Interpolating in sRGB is like playing a glissando on an instrument tuned to just intonation: some intervals sound larger than others.

# Examples

**Example 1** (from source): Blending white with blue: Oklab \u2192 smooth blue gradient with no hue shift; CIELAB \u2192 visible purple shift; CIELUV \u2192 purple shift; HSV \u2192 purple shift; CAM16 \u2192 rapid desaturation, uneven. (Section: "Blending colors")

**Example 2** (from source): The hue gradient comparison shows that an Oklab hue sweep (constant L and C, varying h) produces a visually even strip, while an HSV hue sweep (constant V and S) shows large lightness variation across hues \u2014 demonstrating that HSV hue sweeps are not perceptual interpolations. (Section: "Comparing Oklab to HSV")

# Relationships

## Builds Upon
- **Perceptual uniformity** \u2014 The reason linear interpolation in Oklab is visually smooth.
- **Oklab** \u2014 The space in which the interpolation is performed.
- **Oklab conversion** \u2014 Required to enter and exit the Oklab space.

## Enables
- **Gradient design tools** \u2014 CSS `linear-gradient(in oklab, ...)` is the direct implementation.
- **Uniform palette generation** \u2014 Hue sweeps at constant L and C.

## Related
- **Chroma (perceptual)** \u2014 Can be held constant during hue interpolation.
- **Lightness (perceptual)** \u2014 Can be independently ramped or held constant.

## Contrasts With
- **sRGB interpolation** \u2014 Produces visually uneven transitions; midpoint appears lighter or darker than expected.
- **HSV hue interpolation** \u2014 Passes through visually non-intermediate lightness values.

# Common Errors

- **Error**: Interpolating in gamma-encoded sRGB space.
  **Correction**: Interpolation must occur in a linear or perceptual space. sRGB interpolation produces a light grey midpoint when blending dark colours.

- **Error**: Interpolating hue angle linearly without considering the wrap-around at 0\u00b0/360\u00b0.
  **Correction**: Use the shortest angular path (e.g., if hue difference > 180\u00b0, take the complementary route).

# Common Confusions

- **Confusion**: Interpolating in CIELAB instead of Oklab is equally good.
  **Clarification**: CIELAB interpolation introduces hue shifts for blue colours specifically. Oklab was designed to fix this, and the blending plots in the source confirm a visible difference.

# Source Reference

"Blending colors"; requirements list in "Motivation and derivation of Oklab" (blending requirement); "Comparing Oklab to HSV".

# Verification Notes

- Definition source: Blending requirement directly quoted from "Motivation and derivation of Oklab"; demonstration from blending plots described in "Blending colors".
- Confidence rationale: High \u2014 blending is one of the primary motivating use cases of the article; the comparison is explicit and visual.
- Uncertainties: The article discusses blending qualitatively (with reference to images) rather than giving the interpolation formula explicitly; the lerp formula was inferred from standard colour science practice consistent with the source.
- Cross-reference status: Verified against blending section and requirements list.
- Rosetta Stone check: Music/equal-temperament-glissando mapping added as structural.
- OCR issues: None significant.
