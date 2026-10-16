---
concept: "CSS rgba() (Alpha Channel)"
slug: "css-rgba"
category: "colour-theory"
subcategory: "colour-notation"
tier: "intermediate"
layer: "3-implementation"
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
    - "rgba()"
    - "CSS alpha"
    - "opacity in color"
prerequisites:
  - "rgb-colour-model"
  - "colour-bit-depth"
extends:
  - "rgb-colour-model"
related:
  - "hsl-css-syntax"
  - "hex-colour-notation"
contrasts_with: []
answers_questions: []
rosetta_stone: []
css_implementation:
  -
    property: "color / background-color"
    example: "rgba(150, 150, 150, 0.5);"
    support: "baseline"
  -
    property: "color / background-color"
    example: "rgba(0, 0, 0, 0);"
    support: "baseline"
---

# Quick Definition

In current CSS, `rgba()` is an alias of `rgb()`. The optional alpha component may be a number or percentage; values outside the accepted range are clamped. Colour alpha affects that colour during compositing, while the `opacity` property applies to the rendered element group, including descendants.

# Core Definition

Drasner describes the rgba syntax: "x is a number from 0-255 [for colour channels], y is a number from 0.0 to 1.0 [for alpha]" in the form `rgba(x, x, x, y)`. Alpha is a colour component; CSS syntax does not require a particular in-memory bit allocation. "In this 24-bit depth, 8 bits are dedicated to red, green, and blue. The rest are used for transparency or alpha channels." Alpha contributes to compositing the colour over the backdrop; 0 is transparent and 1 is opaque. It is distinct from the `opacity` property, which applies to the element’s rendered group including descendants, while colour alpha affects the selected colour value.

# Prerequisites

- **RGB colour model** — rgba() is an extension of rgb()
- **Colour bit depth** — The alpha channel is the extra 8 bits in 32-bit colour

# Key Properties

1. Optional alpha component: number or percentage, clamped to the 0–1 range
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

**Example 1** (from source): `rgba(150, 150, 150, 0.5)` — Drasner's canonical example; a 50% transparent medium grey.

# Relationships

## Builds Upon
- **RGB colour model** — rgba() adds transparency to RGB

## Enables
- **Semi-transparent colour** — Enables layering visual elements without full opacity

## Related
- **CSS hsla()** — The HSL equivalent with the same alpha parameter
- **CSS opacity property** — A related but distinct transparency mechanism affecting the whole element

# Common Errors

- **Error**: Using an integer (e.g. rgba(255, 0, 0, 1)) expecting 100% opacity.
  **Correction**: This is correct — 1 (or 1.0) does mean fully opaque. However, using a value like `255` for alpha is wrong; it will be treated as `1` or may be invalid depending on browser strictness.

- **Error**: Confusing rgba() alpha with CSS `opacity`.
  **Correction**: `opacity: 0.5` makes the entire element (including text and children) 50% transparent. `background-color: rgba(0,0,0,0.5)` makes only the background colour 50% transparent; children remain fully opaque.

# Source Reference

"RGB Values" section under "Color values," Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Current syntax and alpha: [CSS Color 4 §§3.3, 4.1–4.2 and 5.1](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/#alpha-syntax) distinguishes colour alpha and element opacity; `rgb()` and `rgba()` are aliases.

- Definition source: Direct quote from Drasner
- Confidence rationale: High — clearly defined with example
- Uncertainties: CSS Color 4 syntax allows `rgb(R G B / A)` form; source describes only legacy comma syntax
- Cross-reference status: Not in Ottosson source
- Rosetta Stone check: No mappings added
- OCR issues: None significant
