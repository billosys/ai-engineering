---
concept: RGB Colour Model (CSS)
slug: rgb-colour-model
category: colour-theory
subcategory: colour-models
tier: foundational
layer: 2-domain
source: "Working With Colors Guide"
source_slug: posts
authors: "Sarah Drasner"
chapter: "Color values / RGB Values"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - ["rgb()", "rgba()", "CSS RGB"]
prerequisites:
  - additive-colour-mixing
  - colour-bit-depth
extends:
  - []
related:
  - hex-colour-notation
  - hsl
  - css-rgba
contrasts_with:
  - hsl
answers_questions:
  - "What distinguishes additive from subtractive colour mixing, and which does a monitor use?"
  - "What is the relationship between bit depth and available colour range?"
rosetta_stone: []
css_implementation:
  - property: "color / background-color"
    example: "rgb(150, 150, 150);"
    support: baseline
  - property: "color / background-color"
    example: "rgba(150, 150, 150, 0.5);"
    support: baseline
---

# Quick Definition

The CSS RGB colour model specifies colours by three integer values (0\u2013255) for red, green, and blue channels, directly encoding the additive light intensities of each primary colour on a monitor display.

# Core Definition

Drasner explains: "In terms of web color values in an RGB channel, we specify color on a range from 0-255." The syntax is `rgb(x, x, x)` or `rgba(x, x, x, y)` where x is 0\u2013255 and y (alpha) is 0.0\u20131.0. This directly follows from the 8-bit-per-channel structure of 24-bit True Color displays: "In this 24-bit depth, 8 bits are dedicated to red, green, and blue. The rest are used for transparency or alpha channels." RGB values in CSS are sRGB values \u2014 they describe the intensity of red, green, and blue phosphors (or equivalent sub-pixels) in a monitor's additive light output.

# Prerequisites

- **Additive colour mixing** \u2014 RGB directly encodes additive primaries
- **Colour bit depth** \u2014 The 0\u2013255 range comes from 8 bits per channel

# Key Properties

1. Three channels: Red, Green, Blue, each 0\u2013255
2. (0, 0, 0) = black; (255, 255, 255) = white
3. rgba() adds a fourth parameter for alpha (opacity): 0.0 = fully transparent, 1.0 = fully opaque
4. Values are sRGB, not linear light \u2014 gamma encoding is applied

# Construction / Recognition

## To Construct/Create:
1. Determine desired colour as R, G, B values each in [0, 255]
2. Write as `rgb(R, G, B)` or with alpha as `rgba(R, G, B, A)` where A is 0.0\u20131.0

## To Identify/Recognise:
1. Look for three comma-separated integers 0\u2013255 inside `rgb()` or `rgba()`
2. `rgb(255, 0, 0)` = pure red; `rgb(0, 255, 0)` = pure green; `rgb(0, 0, 255)` = pure blue

# Context & Application

- **Typical contexts**: CSS stylesheets, JavaScript colour manipulation, canvas/SVG rendering
- **Common applications**: Setting element colours programmatically; generating colours with Math.random() as shown by Drasner

# Examples

**Example 1** (from source): `rgba(150, 150, 150, 0.5)` \u2014 Drasner's canonical example showing a medium grey at 50% opacity.

**Example 2** (from source \u2014 JavaScript): Drasner's React component generates colours as `rgb(200, ${addColor1}, ${addColor2})` by iterating over calculated values, demonstrating programmatic RGB colour generation.

# Relationships

## Builds Upon
- **Additive colour mixing** \u2014 RGB encodes additive primaries
- **Colour bit depth** \u2014 8 bits per channel \u2192 0\u2013255 range

## Enables
- **Hex colour notation** \u2014 Hex is an alternative encoding of the same RGB values
- **HSL colour space** \u2014 HSL is a coordinate transformation of RGB values

## Related
- **CSS rgba()** \u2014 The alpha extension of rgb()

## Contrasts With
- **HSL** \u2014 HSL is more human-readable for choosing and adjusting colours; RGB is closer to the hardware representation
- **CMYK** \u2014 Print colour model based on subtractive mixing; RGB must be converted for print output

# Common Errors

- **Error**: Using floating-point values (e.g. rgb(0.5, 0.5, 0.5)) in CSS rgb().
  **Correction**: CSS rgb() expects integers 0\u2013255. rgb(128, 128, 128) is the correct form for 50% grey in legacy syntax. (CSS Color 4 does allow percentages and new syntax, but the classic form requires integers.)

# Source Reference

"RGB Values" section under "Color values," Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Definition source: Direct quotes from Drasner
- Confidence rationale: High \u2014 explicitly defined with syntax examples
- Uncertainties: Source predates CSS Color 4's new syntax; the integer 0\u2013255 description reflects the classic syntax
- Cross-reference status: Not discussed in detail in Ottosson source
- Rosetta Stone check: No mappings added
- OCR issues: None significant
