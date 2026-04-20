---
# === CORE IDENTIFICATION ===
concept: Munsell Value Scale
slug: munsell-value-scale

# === CLASSIFICATION ===
category: colour-theory
subcategory: colour-systems
tier: foundational
layer: 2-domain

# === PROVENANCE ===
source: "A Practical Description of The Munsell Color System"
source_slug: munsell-colour-system
authors: "T. M. Cleland"
chapter: "II. Value"
chapter_number: 5
pdf_page: 6
section: "II. Value"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Munsell gray scale"
  - "value scale"
  - "lightness scale"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - colour-value
extends:
  - colour-value
related:
  - munsell-colour-system
  - neutral-axis
  - munsell-colour-notation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 3: What is the difference between hue, saturation/chroma, and lightness/value?"
  - "CQ 14: How does the visual-elements concept of 'value' (light-dark range) connect to colour theory's 'lightness' and to contrast as a design principle?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: mathematics
    concept: "Discrete psychophysical scale on [0, 10]"
    rating: rigorous
    note: "The Munsell value scale is a photometrically calibrated discrete scale where equal step differences correspond to equal perceived lightness differences. The underlying physical-to-perceptual mapping follows an approximate power law (Stevens), not a linear function."

css_implementation:
  - property: "oklch() lightness channel"
    example: "/* Munsell V5 ≈ oklch(0.53 ...) — not a simple linear mapping */"
    support: baseline
---

# Quick Definition

The Munsell Value Scale is a 0-10 photometrically calibrated grayscale that forms the vertical axis of the Munsell colour system, with black (0) and white (10) as unattainable ideals and 9 practical steps of perceptually equal gray between them.

# Core Definition

Cleland describes the scale as "a vertical pole, or axis to our circle of Hues, black at the lower end, representing total absence of light, and white at the top, representing pure light, and between these a number of divisions of gray, regularly graded between black and white" (p. 6).

The scale is bounded but its extremes are theoretical: "Since pure black is unattainable, we will call that 0 and begin our scale with the darkest gray as 1, numbering the steps up to 9, which is the lightest gray. Pure white, which is also unattainable, we will call 10" (p. 6).

The middle step has special significance: "the middle one of these will be 5 — what is referred to as Middle Value" (p. 6). The steps are scientifically calibrated: "These steps of Value, have been scientifically measured and registered by means of an instrument known as a Photometer" (p. 6).

# Prerequisites

- **Colour Value** — Understanding the concept of lightness as a colour dimension is needed before engaging with the specific 0-10 scale.

# Key Properties

1. **0-10 range**: Black = 0 (theoretical), White = 10 (theoretical), practical range 1-9.
2. **Middle Value = 5**: The central reference point, used extensively in balance calculations.
3. **Photometric calibration**: Steps are empirically measured for perceptual equality.
4. **9 practical steps**: The "gradation could also be infinite" but 9 steps suffice for practical use (p. 6).
5. **Forms the neutral axis**: The value scale is simultaneously the achromatic spine of the colour solid.
6. **Written as superscript/above-line numeral**: "B6/ for example" means blue at value 6 (p. 6).

# Construction / Recognition

## To Construct/Create:
1. Obtain the darkest achievable surface (value 1) and lightest achievable surface (value 9).
2. Interpolate 7 intermediate grays using photometric measurement.
3. Verify that each step appears perceptually equidistant from its neighbours.
4. Label 0 (theoretical black) and 10 (theoretical white) as endpoints.

## To Identify/Recognise:
1. A linear sequence of achromatic patches from very dark to very light.
2. Exactly 9 practical steps (1-9), with middle gray at 5.
3. Each step appears equally different from its neighbours.

# Context & Application

- **Typical contexts**: Colour specification, value studies in painting and design, checking contrast ratios, establishing visual hierarchy through lightness differences.
- **Common applications**: Setting the L channel in OKLCH; establishing foreground/background contrast for accessibility; the V component in Munsell H V/C notation; value-based composition (squint test).

## Cross-Domain Connections

**Mathematics → Rigorous**: The Munsell value scale is a psychophysical scale — a discrete sampling of a continuous perceptual function. The mapping from physical luminance (Y) to perceived value (V) follows approximately V = f(Y) where f is a non-linear function close to a cube root (the CIE later formalised this as L* = 116 × (Y/Yn)^(1/3) - 16 in CIELAB). Equal value steps require geometrically, not arithmetically, increasing luminance.

# Examples

**Example 1** (p. 6): "B6/" — a blue at value 6, "is as light or as dark as the 6th step upon the scale of Value."

**Example 2** (p. 6): "A color such as is commonly called 'maroon' is an example of a red which is low in Value, because it is dark, and what is called 'pink' is a red which is high in Value because it is light."

# Relationships

## Builds Upon
- **Colour Value** — The Munsell value scale is the specific implementation of the value concept.

## Enables
- **Munsell Colour Notation** — Value is the V in H V/C.
- **Colour Balance** — Balance calculations multiply chroma by value.
- **Munsell Colour Solid** — The value scale forms the vertical axis.

## Related
- **Neutral Axis** — The value scale IS the neutral axis.
- **Munsell Colour System** — Fundamental structural component.

## Contrasts With
No contrasting value scales are described in this source.

# Common Errors

- **Error**: Treating value steps as linearly proportional to physical luminance.
  **Correction**: The relationship is approximately a power function. Doubling the physical luminance does not double the perceived value.

# Common Confusions

- **Confusion**: Munsell value 5 means 50% physical reflectance.
  **Clarification**: Munsell value 5 (middle gray) corresponds to approximately 20% reflectance, not 50%. The perceptual midpoint is much darker than the physical midpoint.

# Source Reference

Chapter 5: II. Value, pp. 6-7.

# Verification Notes

- Definition source: Direct quotes from p. 6.
- Confidence rationale: High — the scale is explicitly described with clear boundaries and calibration method.
- Uncertainties: The cube-root mapping (CIE L*) is a modern formalisation not in the 1937 text but is mathematically well-established.
- Cross-reference status: Verified against planned cards.
- Rosetta Stone check: Mathematics (psychophysical scale) included, rated RIGOROUS.
