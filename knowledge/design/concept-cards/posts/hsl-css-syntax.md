---
concept: HSL CSS Syntax
slug: hsl-css-syntax
category: colour-theory
subcategory: colour-notation
tier: foundational
layer: 3-implementation
source: "Working With Colors Guide"
source_slug: posts
authors: "Sarah Drasner"
chapter: "Color values / HSL Values"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - ["hsl()", "hsla()", "CSS HSL"]
prerequisites:
  - hsl
  - rgb-colour-model
extends:
  - hsl
related:
  - hex-colour-notation
  - rgb-colour-model
  - css-rgba
contrasts_with:
  - hex-colour-notation
answers_questions:
  - "How do CSS custom properties enable systematic colour theming?"
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

CSS HSL syntax specifies colours using hsl(H, S%, L%) or hsla(H, S%, L%, A), where H is a hue angle in degrees (0\u2013360), S and L are saturation and lightness percentages (0\u2013100%), and A is optional opacity (0.0\u20131.0).

# Core Definition

Drasner explains that "hsl values work with hue, saturation, lightness values" and that "this system is based on a Munsell color system." The syntax ranges: "x is a number from 0\u2013360 [for hue], y is a percentage from 0% to 100% [for saturation and lightness], z is a number from 0.0 to 1.0 [for alpha]" with forms `hsl(x, y, y)` or `hsla(x, y, y, z)`. Drasner emphasises its human-readability advantage: "It's a relatively easy change (around 11 lines of code, to be precise) for the browsers to exchange between rgb and hsl values, but for us humans, the use of hsl can be a lot easier to interpret." She also notes its practical advantage for generative colour: "hsl is very easy to work with to step through color because you know that looping through the hue from 0 to 360 will give you a full range."

# Prerequisites

- **HSL colour space** \u2014 The conceptual model underlying the syntax
- **RGB colour model** \u2014 Browsers convert HSL to RGB internally for rendering

# Key Properties

1. Hue: 0\u2013360 degrees (0=red, 120=green, 240=blue, 360=red again; circular, values outside 0\u2013360 wrap)
2. Saturation: 0% (grey) to 100% (maximum colourfulness at that lightness)
3. Lightness: 0% (black) to 100% (white); 50% at S=100% gives the nominal saturated hue
4. Alpha (in hsla): 0.0 (fully transparent) to 1.0 (fully opaque)

# Construction / Recognition

## To Construct/Create:
1. Decide hue angle (colour category on the wheel)
2. Decide saturation (how colourful: 0% = grey, 100% = vivid)
3. Decide lightness (how dark/light: 0% = black, 50% = normal, 100% = white)
4. Optionally add alpha for transparency

## To Identify/Recognise:
1. `hsl(H, S%, L%)` or `hsla(H, S%, L%, A)` pattern
2. First value is always a bare number (degrees), second and third always have `%`

# Context & Application

- **Typical contexts**: CSS authoring, Sass/preprocessor colour functions, generative colour in JavaScript
- **Common applications**: Creating colour palettes by stepping hue; adjusting lightness for hover states; programmatic colour sequences in loops

# Examples

**Example 1** (from source): `hsla(150, 50%, 50%, 0.5)` \u2014 Drasner's canonical example showing a semi-transparent greenish colour.

**Example 2** (from source \u2014 Sass mixin): `hsl(($i - 10)*($color*1.25), ($i - 1)*($color / $color-frequency), 40%)` \u2014 Drasner's Sass loop steps through HSL values to generate sequences of colours.

**Example 3** (from source \u2014 GreenSock): `fill:"hsl(+=0, +=50%, +=0%)"` \u2014 animating HSL saturation relative to current value, demonstrating HSL's utility for parametric animation.

# Relationships

## Builds Upon
- **HSL colour space** \u2014 CSS hsl() directly expresses the HSL colour model

## Enables
- **Generative colour** \u2014 The circular, predictable hue angle makes HSL ideal for colour loops
- **CSS custom properties for colour** \u2014 HSL values are commonly stored as custom properties for theming

## Related
- **CSS rgba()** \u2014 The equivalent alpha extension for RGB syntax
- **Hex colour notation** \u2014 Alternative encoding of the same sRGB values, less human-readable

## Contrasts With
- **Hex notation** \u2014 Hex is computer-friendly; HSL is human-readable and better for systematic adjustment

# Common Errors

- **Error**: Using `hsl()` values greater than 360 for hue expecting an error.
  **Correction**: Drasner notes "because it's a full circle, you don't need to stick to ranges of 0\u2013360, even -480 or 600 is still a value a browser can interpret."

# Source Reference

"HSL Values" section under "Color values," Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Definition source: Direct quotes from Drasner
- Confidence rationale: High \u2014 complete syntax definition with multiple examples
- Uncertainties: CSS Color 4 introduces updated `hsl()` syntax (without commas); source uses legacy comma syntax
- Cross-reference status: HSL model verified across both sources; syntax specifics from Drasner only
- Rosetta Stone check: No mappings added
- OCR issues: None significant
