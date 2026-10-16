---
concept: "RGB Colour Model (CSS)"
slug: "rgb-colour-model"
category: "colour-theory"
subcategory: "colour-models"
tier: "foundational"
layer: "2-domain"
source: "Working With Colors Guide"
source_slug: "posts"
authors: "Sarah Drasner"
chapter: "Color values / RGB Values"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "high"
aliases:
  -
    - "rgb()"
    - "rgba()"
    - "CSS RGB"
prerequisites:
  - "additive-colour-mixing"
  - "colour-bit-depth"
extends: []
related:
  - "hex-colour-notation"
  - "hsl"
  - "css-rgba"
contrasts_with:
  - "hsl"
answers_questions:
  - "What distinguishes additive from subtractive colour mixing, and which does a monitor use?"
  - "What is the relationship between bit depth and available colour range?"
rosetta_stone: []
css_implementation:
  -
    property: "color / background-color"
    example: "rgb(150, 150, 150);"
    support: "baseline"
  -
    property: "color / background-color"
    example: "rgba(150, 150, 150, 0.5);"
    support: "baseline"
---

# Quick Definition

CSS `rgb()` specifies an sRGB colour using red, green and blue components. Components may be numbers or percentages; fractional numeric values are allowed. These sRGB components are encoded values, not linear light intensities, and CSS does not require an 8-bit framebuffer.

# Core Definition

Drasner explains: "In terms of web color values in an RGB channel, we specify color on a range from 0-255." The prepared article describes the legacy 0–255 form. Current CSS also accepts percentage components and modern space-separated syntax with optional slash alpha; legacy comma syntax remains. Number components are interpreted on the 0–255 scale, so `0.5` is a small channel value, not 50 percent. CSS colour syntax does not prescribe the display framebuffer bit depth. sRGB channel values are gamma-encoded; linearize them before treating them as light contributions.

# Prerequisites

- **Additive colour mixing** — RGB directly encodes additive primaries
- **Colour bit depth** — The 0–255 range comes from 8 bits per channel

# Key Properties

1. Three channels: Red, Green, Blue; CSS accepts numbers or percentages
2. (0, 0, 0) = black; (255, 255, 255) = white
3. rgba() adds a fourth parameter for alpha (opacity): 0.0 = fully transparent, 1.0 = fully opaque
4. Values are sRGB, not linear light — gamma encoding is applied

# Construction / Recognition

## To Construct/Create:
1. Choose numeric components on the 0–255 scale or percentage components on the 0%–100% scale
2. Write as `rgb(R, G, B)` or with alpha as `rgba(R, G, B, A)` where A is 0.0–1.0

## To Identify/Recognise:
1. Recognize both legacy comma-separated and modern space-separated forms; component values need not be integers
2. `rgb(255, 0, 0)` = pure red; `rgb(0, 255, 0)` = pure green; `rgb(0, 0, 255)` = pure blue

# Context & Application

- **Typical contexts**: CSS stylesheets, JavaScript colour manipulation, canvas/SVG rendering
- **Common applications**: Setting element colours programmatically; generating colours with Math.random() as shown by Drasner

# Examples

**Example 1** (from source): `rgba(150, 150, 150, 0.5)` — Drasner's canonical example showing a medium grey at 50% opacity.

**Example 2** (from source — JavaScript): Drasner's React component generates colours as `rgb(200, ${addColor1}, ${addColor2})` by iterating over calculated values, demonstrating programmatic RGB colour generation.

# Relationships

## Builds Upon
- **Additive colour mixing** — RGB encodes additive primaries
- **Colour bit depth** — 8 bits per channel → 0–255 range

## Enables
- **Hex colour notation** — Hex is an alternative encoding of the same RGB values
- **HSL colour space** — HSL is a coordinate transformation of RGB values

## Related
- **CSS rgba()** — The alpha extension of rgb()

## Contrasts With
- **HSL** — HSL is a cylindrical transformation of RGB coordinates that some authors find easier to adjust; neither representation guarantees perceptual uniformity
- **CMYK** — A subtractive print model; conversion between RGB and a print profile depends on the destination conditions

# Common Errors

- **Error**: Treating `rgb(0.5, 0.5, 0.5)` as invalid or as 50% grey.
  **Correction**: Numeric components may be fractional on the 0–255 scale; `0.5` is not 50%. Use `rgb(50% 50% 50%)` for 50% components. Modern syntax permits mixed number/percentage components; legacy comma syntax does not permit mixed component units.

# Source Reference

"RGB Values" section under "Color values," Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Current syntax: [CSS Color 4 §§4.1–4.3 and 5.1](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/#rgb-functions) defines modern/legacy forms, alpha and RGB components. The 2026-10-09 CRD is work in progress.

- Definition source: Direct quotes from Drasner
- Confidence rationale: High — explicitly defined with syntax examples
- Uncertainties: Source predates CSS Color 4's new syntax; the integer 0–255 description reflects the classic syntax
- Cross-reference status: Not discussed in detail in Ottosson source
- Rosetta Stone check: No mappings added
- OCR issues: None significant
