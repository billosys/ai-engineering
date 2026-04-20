---
concept: HSV Colour Space
slug: hsv
category: colour-theory
subcategory: colour-models
tier: foundational
layer: 2-domain
source: "Okhsv and Okhsl"
source_slug: posts
authors: "Bj\u00f6rn Ottosson"
chapter: "HSV"
chapter_number: null
pdf_page: null
section: "Color spaces for color picking"
extraction_confidence: high
aliases:
  - ["Hue Saturation Value", "HSB", "Hue Saturation Brightness"]
prerequisites:
  - []
extends:
  - []
related:
  - hsl
  - okhsv
  - colour-gamut
contrasts_with:
  - hsl
  - okhsv
answers_questions:
  - "What distinguishes Okhsl from Okhsv, and when would you use each?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition

HSV (also called HSB) is a cylindrical colour model introduced in 1978 that describes colours by Hue (angular position), Saturation (colourfulness relative to maximum for a given hue), and Value (a measure of brightness, ranging from black to the maximum coloured light).

# Core Definition

HSV describes colours with three parameters, as Ottosson defines them: Hue, which "roughly corresponds to perceived hue, but it has quite severe distortions"; Saturation, which "roughly corresponds to saturation relative to maximum possible saturation in sRGB of the same hue"; and Value, which is "a bit hard to define" and "can be seen as how much to mix the color with black, with 100% being no black and 0% completely black." Value is "sometimes also referred to as Brightness." Like HSL, HSV is "not quite a color space on its own" but is a "transformation from a source RGB color space," most commonly sRGB. HSV maps the sRGB gamut to a cylinder with a cone-like internal structure (a pointed bottom at V=0 and a circular top face at V=1).

# Prerequisites

- **RGB colour model** \u2014 HSV is a cylindrical re-parameterisation of RGB

# Key Properties

1. V=0 always yields black regardless of H or S; V=1 and S=1 yields the purest colour for a given hue
2. The maximum chroma colour for any hue sits on the edge of the colour solid (V=1, S=1), satisfying the "Max Chroma at Edge" design goal
3. Maps sRGB to a simple cylindrical shape, preventing out-of-gamut values when parameters are adjusted independently
4. Hue angle has severe perceptual non-uniformity \u2014 equal angular steps do not correspond to equally-perceived hue differences

# Construction / Recognition

## To Construct/Create:
1. Identify the hue angle (0\u2013360 or 0\u20131 normalised)
2. Set Saturation: 0 = grey axis, 1 = maximum colourfulness for the hue
3. Set Value: 0 = black, 1 = maximum brightness; the resulting colour is a mixture of the fully-saturated hue and black

## To Identify/Recognise:
1. Look for a square two-dimensional picker widget where the horizontal axis is Saturation and the vertical axis is Value, with a separate hue slider
2. The bottom-left corner of such a picker is always pure black

# Context & Application

- **Typical contexts**: Digital painting applications (Photoshop, Procreate, GIMP), colour pickers in design tools, image processing
- **Common applications**: Adjusting colour brightness while keeping hue consistent; selecting the most vivid version of a hue at V=1, S=1

# Examples

**Example 1** (from source): Ottosson illustrates HSV's hue distortion: deep blue colours in HSV show "a purple shift as saturation decreases," demonstrating that S=0 achromatic axis produces different perceived hues than expected.

**Example 2** (from source): The comparison table shows that HSV achieves "yes" for Simple Geometrical Shape and Max Chroma at Edge, but "no" for Orthogonal Lightness and Orthogonal Chroma, and only "partial" for Orthogonal Hue and Saturation.

# Relationships

## Builds Upon
- **sRGB colour model** \u2014 HSV is a coordinate transformation of sRGB

## Enables
- **Okhsv** \u2014 Okhsv was designed as a perceptually-improved replacement for HSV while preserving its cylindrical structure
- **HWB colour model** \u2014 HSV can be transformed to HWB (hue, whiteness, blackness) form, which is structurally similar to NCS

## Related
- **HSL** \u2014 Sibling model from the same 1978 paper; shares the hue calculation
- **Natural Colour System (NCS)** \u2014 Ottosson notes "HSV is quite similar to the Natural Color System in its structure"

## Contrasts With
- **Okhsv** \u2014 Okhsv corrects HSV's perceptual distortions using Oklab while maintaining cylindrical geometry
- **HSL** \u2014 Different lightness axis: HSL places grey at L=50%, S=0; HSV has grey at V=any, S=0

# Common Errors

- **Error**: Assuming that decreasing Saturation in HSV while keeping H and V constant preserves the perceived hue.
  **Correction**: Ottosson documents that blue colours shift toward purple as saturation decreases in HSV.

- **Error**: Treating Value as equivalent to perceived lightness.
  **Correction**: Value is not perceptual lightness; a yellow at V=0.5 will appear far brighter than a blue at V=0.5 due to the differing luminance contributions of the RGB primaries.

# Common Confusions

- **Confusion**: HSV Saturation and HSL Saturation mean the same thing.
  **Clarification**: Ottosson explicitly states they are not the same. HSV Saturation is relative to the maximum saturation of the same hue at V=1; HSL Saturation is relative to the most colourful colour at the same lightness.

# Source Reference

"HSV" section under "Color spaces for color picking," Okhsv and Okhsl (Bj\u00f6rn Ottosson).

# Verification Notes

- Definition source: Direct quotes from Ottosson
- Confidence rationale: High \u2014 source dedicates a full named section to HSV with properties table
- Uncertainties: None significant
- Cross-reference status: Verified within source; no substantial HSV content in Drasner source
- Rosetta Stone check: No rigorous cross-domain mappings added
- OCR issues: HTML artifacts present; prose content clean
