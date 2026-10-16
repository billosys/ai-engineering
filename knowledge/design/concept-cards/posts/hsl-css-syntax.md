---
concept: "HSL CSS Syntax"
slug: "hsl-css-syntax"
category: "colour-theory"
subcategory: "colour-notation"
tier: "foundational"
layer: "3-implementation"
source: "Working With Colors Guide"
source_slug: "posts"
authors: "Sarah Drasner"
chapter: "Color values / HSL Values"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "high"
aliases:
  -
    - "hsl()"
    - "hsla()"
    - "CSS HSL"
prerequisites:
  - "hsl"
  - "rgb-colour-model"
extends:
  - "hsl"
related:
  - "hex-colour-notation"
  - "rgb-colour-model"
  - "css-rgba"
contrasts_with:
  - "hex-colour-notation"
answers_questions:
  - "How do CSS custom properties enable systematic colour theming?"
rosetta_stone: []
css_implementation:
  -
    property: "color / background-color"
    example: "hsl(150, 50%, 50%);"
    support: "baseline"
  -
    property: "color / background-color"
    example: "hsla(150, 50%, 50%, 0.5);"
    support: "baseline"
---

# Quick Definition

CSS HSL uses `hsl()` with hue, saturation, lightness and optional alpha components. Modern space-separated syntax and legacy comma-separated syntax are accepted; `hsla()` is an alias. Hue accepts an angle and wraps around the hue circle; HSL coordinates are a convenient sRGB transformation, not a perceptually uniform scale.

# Core Definition

Drasner explains that "hsl values work with hue, saturation, lightness values" and compares the system with Munsell. Treat this as Drasner’s attributed comparison, not as proof of direct derivation or mathematical equivalence. Her prepared article gives legacy comma-separated examples and bounded ranges. Current CSS permits modern space-separated syntax, angle units, hue wrapping and number or percentage alpha. Modern HSL saturation and lightness accept either percentages or numbers on a 0–100 reference scale; legacy comma syntax requires percentages for both. The same HSL coordinates remain nonuniform in perceived lightness. Drasner emphasises its human-readability advantage: "It's a relatively easy change (around 11 lines of code, to be precise) for the browsers to exchange between rgb and hsl values, but for us humans, the use of hsl can be a lot easier to interpret." She also notes its practical advantage for generative colour: "hsl is very easy to work with to step through color because you know that looping through the hue from 0 to 360 will give you a full range."

# Prerequisites

- **HSL colour space** — The conceptual model underlying the syntax
- **RGB colour model** — Browsers convert HSL to RGB internally for rendering

# Key Properties

1. Hue wraps around one full turn; numeric hues use degrees (0=red, 120=green, 240=blue), and CSS accepts angle units such as `turn`, `rad` and `grad`
2. Saturation (S): modern syntax accepts percentages or numbers on a 0–100 reference scale (0%/0 = grey; 100%/100 = maximum colourfulness at that lightness); legacy comma syntax requires a percentage
3. Lightness (L): modern syntax accepts percentages or numbers on a 0–100 reference scale (0%/0 = black; 100%/100 = white); legacy comma syntax requires a percentage. 50%/50 at S=100% gives the nominal saturated hue
4. Optional alpha accepts a number or percentage; 0 is transparent and 1/100% is opaque

# Construction / Recognition

## To Construct/Create:
1. Decide hue angle (colour category on the wheel)
2. Decide saturation (0%–100% in either syntax, or 0–100 as a number in modern syntax; 0 = grey, 100 = vivid)
3. Decide lightness (0%–100% in either syntax, or 0–100 as a number in modern syntax; 0 = black, 50 = normal, 100 = white)
4. Optionally add alpha for transparency

## To Identify/Recognise:
1. Recognize modern space/slash syntax or legacy comma syntax; hue may be a number or angle, with optional alpha
2. Modern syntax accepts number or percentage S/L (numbers use the 0–100 reference scale); legacy comma syntax requires percentage S/L. Thus `hsl(180 100 50 / 50%)` and `hsl(180 100% 50% / 50%)` agree, while legacy `hsl(180, 100, 50)` is invalid. Hue may use degrees, turns, radians or gradians.

# Context & Application

- **Typical contexts**: CSS authoring, Sass/preprocessor colour functions, generative colour in JavaScript
- **Common applications**: Creating colour palettes by stepping hue; adjusting lightness for hover states; programmatic colour sequences in loops

# Examples

**Example 1** (from source): `hsla(150, 50%, 50%, 0.5)` — Drasner's canonical example showing a semi-transparent greenish colour. **Example 1a** (current CSS syntax): `hsl(0.5turn 100% 50% / 50%)` uses an angle hue and percentage alpha. **Example 1b**: modern `hsl(180 100 50 / 50%)` is equivalent to `hsl(180 100% 50% / 50%)`; the comma-separated legacy form `hsl(180, 100, 50)` is invalid because legacy S/L require percentages.

**Example 2** (historical source example — Sass mixin, not standalone CSS): `hsl(($i - 10)*($color*1.25), ($i - 1)*($color / $color-frequency), 40%)` — Drasner's Sass loop steps through HSL values to generate sequences of colours.

**Example 3** (historical source example — GreenSock interpolation syntax, not standalone CSS): `fill:"hsl(+=0, +=50%, +=0%)"` — animating HSL saturation relative to current value, demonstrating HSL's utility for parametric animation.

# Relationships

## Builds Upon
- **HSL colour space** — CSS hsl() directly expresses the HSL colour model

## Enables
- **Generative colour** — The hue angle can be varied to generate a sequence; resulting perceptual spacing is not uniform
- **CSS custom properties for colour** — HSL values can be stored in custom properties when that representation suits the project

## Related
- **CSS rgba()** — RGB alpha syntax; `rgb()` and `rgba()` are aliases, as are `hsl()` and `hsla()`
- **Hex colour notation** — Alternative encoding of the same sRGB values, less human-readable

## Contrasts With
- **Hex notation** — Hex is computer-friendly; HSL is human-readable and better for systematic adjustment

# Common Errors

- **Error**: Using `hsl()` values greater than 360 for hue expecting an error.
  **Correction**: Drasner notes "because it's a full circle, you don't need to stick to ranges of 0–360, even -480 or 600 is still a value a browser can interpret."

- **Error**: Using bare-number saturation or lightness in legacy comma syntax, or treating modern S/L numbers as 0–1 fractions.
  **Correction**: Modern HSL numbers use a 0–100 reference scale, so modern `hsl(180 100 50 / 50%)` agrees with `hsl(180 100% 50% / 50%)`. Legacy comma syntax requires percentage S/L, so `hsl(180, 100, 50)` is invalid.

# Source Reference

"HSL Values" section under "Color values," Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Iteration02 scope: The current technical support below uses the prepared text and linked rules; this correction does not assess fidelity to the unavailable original capture or browser behavior. Extraction-confidence metadata is unchanged. Retained extraction/provenance remarks below are predecessor assertions present at source 19c7a08a; their authorship is not inferred here, and they are not new current results. Where this iteration clarifies a note, that clarification scopes a prior assertion rather than recording a new extraction or verification result.

- Current syntax: [CSS Color 4 §§4.1–4.3 and 7](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/#the-hsl-notation) defines modern number-or-percentage S/L on a 0–100 reference scale, legacy percentage-only S/L, hue, alpha, and `hsl()`/`hsla()` aliases. The Munsell statement above is only an attribution to Drasner’s comparison; the draft is not browser-support evidence.

- Definition source: Direct quotes from Drasner
- Confidence rationale: High — complete syntax definition with multiple examples
- Historical source note: Drasner’s examples use legacy comma syntax; current CSS also accepts modern space-separated components, angle units and slash alpha.
- Cross-reference status: The prepared Drasner article describes HSL; current syntax claims are separately supported by CSS Color 4. This does not verify the unavailable original capture.
- Rosetta Stone check: No mappings added
- OCR issues: None significant
