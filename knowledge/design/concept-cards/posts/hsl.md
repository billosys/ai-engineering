---
concept: HSL Colour Space
slug: hsl
category: colour-theory
subcategory: colour-models
tier: foundational
layer: 2-domain
source: "Okhsv and Okhsl"
source_slug: posts
authors: "Bj\u00f6rn Ottosson"
chapter: "HSL"
chapter_number: null
pdf_page: null
section: "Color spaces for color picking"
extraction_confidence: high
aliases:
  - ["Hue Saturation Lightness", "HSLA"]
prerequisites:
  - []
extends:
  - []
related:
  - hsv
  - hsl-css-syntax
  - okhsl
contrasts_with:
  - hsv
  - okhsl
answers_questions:
  - "What distinguishes Okhsl from Okhsv, and when would you use each?"
rosetta_stone: []
css_implementation:
  - property: "color / background-color"
    example: "hsl(150, 50%, 50%);"
    support: baseline
  - property: "color / background-color"
    example: "hsla(150, 50%, 50%, 0.5);"
    support: baseline
---

# Quick Definition

HSL is a cylindrical colour model that describes colours by three parameters \u2014 Hue (0\u2013360 degrees), Saturation (0\u2013100%), and Lightness (0\u2013100%) \u2014 designed as a more human-readable alternative to RGB.

# Core Definition

HSL, introduced in the 1978 paper "Color Spaces for Computer Graphics," describes colours with three parameters: Hue, which is identical to Hue in HSV (and shares the same perceptual distortions); Saturation, described by Ottosson as "roughly the chroma of the color relative to the most colorful color with the same 'lightness' and 'hue'" (referred to as "relative chroma" in the original paper, not true perceptual saturation); and Lightness, which has "some correlation with the perception of lightness, with 0% corresponding to black and 100% to white" but "does not match the perception of lightness well at all for saturated colors" (referred to as "Intensity" in the original paper). As Drasner notes, "hsl values work with hue, saturation, lightness values" and the "system is based on a Munsell color system."

# Prerequisites

- **RGB colour model** \u2014 HSL is a transformation of RGB values to alternative coordinates

# Key Properties

1. Hue rotates through 360 degrees as a full circle
2. Saturation and Lightness are percentages from 0% to 100%
3. Maps sRGB gamut to a cylinder, allowing independent parameter changes without out-of-gamut colours
4. Lightness of 50% at full saturation does not correspond to perceptual midpoint for most hues

# Construction / Recognition

## To Construct/Create:
1. Choose a Hue angle (0\u2013360): 0/360 = red, 120 = green, 240 = blue
2. Choose Saturation (0% = achromatic grey, 100% = most vivid at this hue/lightness)
3. Choose Lightness (0% = black, 50% = nominal colour, 100% = white)

## To Identify/Recognise:
1. Look for `hsl(H, S%, L%)` or `hsla(H, S%, L%, A)` syntax
2. Yellow at 50% lightness appears far brighter than blue at 50% lightness \u2014 a sign of HSL's perceptual non-uniformity

# Context & Application

- **Typical contexts**: CSS colour authoring, design tool colour pickers, generative colour loops in JavaScript/Sass
- **Common applications**: Drasner notes that "looping through the hue from 0 to 360 will give you a full range," making HSL well-suited for generative colour sequences; adjusting lightness/saturation for hover states; theming

# Examples

**Example 1** (from source \u2014 Working With Colors Guide): Drasner shows `hsla(150, 50%, 50%, 0.5)` as a canonical usage and a Sass mixin that steps through `hsl(($i - 10)*($color*1.25), ($i - 1)*($color / $color-frequency), 40%)` to generate fruit-loop colour sequences.

**Example 2** (from source \u2014 Okhsv and Okhsl): Ottosson illustrates HSL's failure: "colors HSL considers to have the same lightness" includes a bright yellow and a dim blue at equal L values \u2014 a perceptual inconsistency.

# Relationships

## Builds Upon
- **sRGB colour model** \u2014 HSL is a transformation of sRGB coordinates

## Enables
- **Okhsl** \u2014 Okhsl was built to improve upon HSL's perceptual shortcomings while retaining its cylindrical structure
- **Generative colour** \u2014 Predictable 0\u2013360 hue cycle enables looping colour sequences

## Related
- **HSV** \u2014 Sibling model from the same 1978 paper; shares the same hue calculation
- **Munsell colour system** \u2014 HSL's three-channel structure traces conceptually to Munsell

## Contrasts With
- **Okhsl** \u2014 Okhsl corrects HSL's lightness and hue distortions using Oklab
- **HSV** \u2014 Different arrangement of axes; HSL places white/black at L extremes whereas HSV places white at V=1, S=0

# Common Errors

- **Error**: Assuming equal Lightness values mean equal perceived brightness.
  **Correction**: Yellow at hsl(60, 100%, 50%) is far brighter perceptually than blue at hsl(240, 100%, 50%); Lightness in HSL does not match perceived luminance for saturated colours.

- **Error**: Treating HSL Saturation as equivalent to HSV Saturation.
  **Correction**: Ottosson explicitly notes these are "not the same as 'saturation' in HSV"; HSL Saturation is relative chroma normalised to the same lightness and hue, not the same quantity.

# Common Confusions

- **Confusion**: HSL Saturation represents true perceptual saturation.
  **Clarification**: Ottosson notes it "is not comparable to" true saturation; the original paper called it "relative chroma," which is more accurate.

- **Confusion**: HSL is a colour space in its own right.
  **Clarification**: Ottosson notes "HSL and HSV are not quite color spaces on their own, they are transformations from a source RGB color space." The precise values depend on which RGB primaries are used.

# Source Reference

"HSL" section under "Color spaces for color picking," Okhsv and Okhsl; "HSL Values" section, Working With Colors Guide.

# Verification Notes

- Definition source: Direct quotes from both Ottosson (perceptual critique) and Drasner (CSS usage)
- Confidence rationale: High \u2014 both sources discuss HSL explicitly with code examples and comparative analysis
- Uncertainties: Drasner's article predates CSS Color 4; some syntax notes may be dated
- Cross-reference status: Verified across both sources
- Rosetta Stone check: No mappings added \u2014 no strong cross-domain analogies with rigorous correspondence found for HSL alone (distinct from Okhsl)
- OCR issues: HTML artifacts present in source; prose content clean
