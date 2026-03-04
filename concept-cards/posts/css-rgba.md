---
concept: CSS rgba() (Alpha Channel)
slug: css-rgba
category: colour-theory
subcategory: colour-notation
tier: intermediate
layer: 3-implementation
source: "Working With Colors Guide"
source_slug: posts
authors: "Sarah Drasner"
chapter: "Color values / RGB Values"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - ["rgba()", "CSS alpha", "opacity in color"]
prerequisites:
  - rgb-colour-model
  - colour-bit-depth
extends:
  - rgb-colour-model
related:
  - hsl-css-syntax
  - hex-colour-notation
contrasts_with:
  - []
answers_questions: []
rosetta_stone: []
css_implementation:
  - property: "color / background-color"
    example: "rgba(150, 150, 150, 0.5);"
    support: baseline
  - property: "color / background-color"
    example: "rgba(0, 0, 0, 0);"
    support: baseline
---

# Quick Definition

CSS rgba() extends rgb() with a fourth alpha channel parameter specifying opacity, where 0.0 is fully transparent and 1.0 is fully opaque.

# Core Definition

Drasner describes the rgba syntax: "x is a number from 0-255 [for colour channels], y is a number from 0.0 to 1.0 [for alpha]" in the form `rgba(x, x, x, y)`. The alpha channel corresponds to the 8-bit transparency component in 32-bit colour: "In this 24-bit depth, 8 bits are dedicated to red, green, and blue. The rest are used for transparency or alpha channels." Alpha controls the compositing of the element's colour over its background \u2014 0.0 means the element's colour is entirely transparent (background shows through), 1.0 means fully opaque. Alpha is distinct from CSS `opacity`, which affects the entire element including its children; rgba() affects only the colour value of the specific property it is applied to.

# Prerequisites

- **RGB colour model** \u2014 rgba() is an extension of rgb()
- **Colour bit depth** \u2014 The alpha channel is the extra 8 bits in 32-bit colour

# Key Properties

1. Fourth parameter: 0.0 (fully transparent) to 1.0 (fully opaque)
2. Applies only to the colour value, not to child elements (unlike `opacity` property)
3. The alpha value is a floating-point decimal, not an integer or percentage (in the classic syntax)
4. Equivalent alpha support exists in hsla()

# Construction / Recognition

## To Construct/Create:
1. Start with an rgb() value
2. Add a fourth comma-separated value between 0.0 and 1.0
3. Example: `rgba(255, 0, 0, 0.5)` = 50% transparent red

## To Identify/Recognise:
1. `rgba(R, G, B, A)` with four parameters
2. The fourth value is always a decimal between 0 and 1

# Context & Application

- **Typical contexts**: CSS colour properties, overlays, shadows, semi-transparent UI elements
- **Common applications**: Creating glassmorphism effects; hover state overlays; semi-transparent backgrounds; colour tokens with built-in transparency

# Examples

**Example 1** (from source): `rgba(150, 150, 150, 0.5)` \u2014 Drasner's canonical example; a 50% transparent medium grey.

# Relationships

## Builds Upon
- **RGB colour model** \u2014 rgba() adds transparency to RGB

## Enables
- **Semi-transparent colour** \u2014 Enables layering visual elements without full opacity

## Related
- **CSS hsla()** \u2014 The HSL equivalent with the same alpha parameter
- **CSS opacity property** \u2014 A related but distinct transparency mechanism affecting the whole element

# Common Errors

- **Error**: Using an integer (e.g. rgba(255, 0, 0, 1)) expecting 100% opacity.
  **Correction**: This is correct \u2014 1 (or 1.0) does mean fully opaque. However, using a value like `255` for alpha is wrong; it will be treated as `1` or may be invalid depending on browser strictness.

- **Error**: Confusing rgba() alpha with CSS `opacity`.
  **Correction**: `opacity: 0.5` makes the entire element (including text and children) 50% transparent. `background-color: rgba(0,0,0,0.5)` makes only the background colour 50% transparent; children remain fully opaque.

# Source Reference

"RGB Values" section under "Color values," Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Definition source: Direct quote from Drasner
- Confidence rationale: High \u2014 clearly defined with example
- Uncertainties: CSS Color 4 syntax allows `rgb(R G B / A)` form; source describes only legacy comma syntax
- Cross-reference status: Not in Ottosson source
- Rosetta Stone check: No mappings added
- OCR issues: None significant
