---
# === CORE IDENTIFICATION ===
concept: Colour Value
slug: colour-value

# === CLASSIFICATION ===
category: colour-theory
subcategory: colour-properties
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
  - "value"
  - "lightness"
  - "Munsell value"
  - "tone"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - munsell-colour-system
  - hue
  - chroma
  - neutral-axis
  - munsell-value-scale
contrasts_with:
  - hue
  - chroma

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 3: What is the difference between hue, saturation/chroma, and lightness/value?"
  - "CQ 14: How does the visual-elements concept of 'value' (light-dark range) connect to colour theory's 'lightness' and to contrast as a design principle?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: mathematics
    concept: "Scalar on a bounded interval [0, 10]"
    rating: rigorous
    note: "Value is a scalar quantity on the interval [0, 10] with photometric measurement. The steps are perceptually calibrated, meaning equal differences in value number correspond to equal perceived lightness differences — a psychophysical scale, not a linear physical one."

css_implementation:
  - property: "oklch() lightness channel"
    example: "color: oklch(0.5 0.1 240); /* L = 0.5 = Munsell ~V5 */"
    support: baseline
  - property: "hsl() lightness channel"
    example: "color: hsl(240, 50%, 50%); /* L = 50% */"
    support: baseline
---

# Quick Definition

Colour value is the quality by which we distinguish a light colour from a dark one — the second dimension of the Munsell system, measured on a scale from black (0) through grays to white (10).

# Core Definition

Munsell defines value as "The quality by which we distinguish a light color from a dark one" (p. 6). Cleland explains: "We noted that the first dimension did not tell us whether a color was light or dark. It told us, for example, that it was red and not green, but we know that there may be light red and dark red, and it is the function of this dimension of Value to tell us how light or how dark a given color may be" (p. 6).

Value is measured on a vertical scale from black (0) to white (10), with middle value at step 5. The steps have been "scientifically measured and registered by means of an instrument known as a Photometer" (p. 6), ensuring perceptual equality between steps.

In a colour formula, value is written as a numeral above a line: "B6/ for example, by which we mean that this particular blue, regardless of its other qualities, is as light or as dark as the 6th step upon the scale of Value" (p. 6).

# Prerequisites

This is a foundational concept with no prerequisites within this source. It is one of the three primitive dimensions of colour.

# Key Properties

1. **Light-dark quality**: Value measures only lightness — independent of hue and chroma.
2. **Vertical scale**: Conceived as "a vertical pole, or axis to our circle of Hues, black at the lower end... and white at the top" (p. 6).
3. **0-10 range**: Black = 0, white = 10, with 9 practical steps (1-9). "Since pure black is unattainable, we will call that 0... Pure white, which is also unattainable, we will call 10" (p. 6).
4. **Middle Value = 5**: The midpoint of the scale, referenced repeatedly in balance calculations.
5. **Photometric measurement**: "These steps of Value have been scientifically measured and registered by means of an instrument known as a Photometer" (p. 6).
6. **Perceptual uniformity**: Each step appears equally different from adjacent steps — a psychophysical scale.

# Construction / Recognition

## To Construct/Create:
1. Establish black (0) and white (10) as the endpoints.
2. Divide the range into 9 perceptually equal steps of gray (1-9).
3. Calibrate using photometric measurement to ensure each step appears equally spaced.
4. Step 5 = middle value (the midpoint gray).

## To Identify/Recognise:
1. Squint at the colour or desaturate it mentally — how light or dark is it?
2. Compare to a neutral gray scale: which gray step matches the colour's lightness?
3. A "maroon" is a red low in value (dark); a "pink" is a red high in value (light) (p. 6).

# Context & Application

- **Typical contexts**: Establishing visual hierarchy, checking readability, designing for grayscale compatibility, value-based composition.
- **Common applications**: The L channel in OKLCH; the L channel in HSL; grayscale previews of designs; establishing contrast ratios for accessibility.
- **Historical note**: Cleland uses everyday examples: "A color such as is commonly called 'maroon' is an example of a red which is low in Value, because it is dark, and what is called 'pink' is a red which is high in Value because it is light" (p. 6).

## Cross-Domain Connections

**Mathematics → Rigorous**: Value is a scalar on the bounded interval [0, 10] with perceptual (psychophysical) calibration. The relationship between physical luminance and perceived value follows Stevens's Power Law: ψ = k × Iⁿ with n ≈ 0.33 for brightness. This means equal perceptual value steps correspond to geometrically (not arithmetically) increasing physical luminance.

# Examples

**Example 1** (p. 6): "B6/" — a blue at value 6, "regardless of its other qualities, is as light or as dark as the 6th step upon the scale of Value."

**Example 2** (p. 6): "A color such as is commonly called 'maroon' is an example of a red which is low in Value, because it is dark, and what is called 'pink' is a red which is high in Value because it is light."

# Relationships

## Builds Upon
This is a foundational primitive — it does not build upon other concepts.

## Enables
- **Munsell Value Scale** — The specific 0-10 scale implementing this dimension.
- **Munsell Colour Notation** — Value is the V component in H V/C.
- **Colour Balance** — Balance calculations use value as a multiplier.
- **Munsell Balance Formula** — Area ∝ 1/(Chroma × Value).

## Related
- **Munsell Colour System** — Value is the second of the system's three dimensions.
- **Neutral Axis** — The value scale IS the neutral axis.
- **Hue** — The first dimension, independent of value.
- **Chroma** — The third dimension, independent of value.

## Contrasts With
- **Hue** — Hue measures spectral identity; value measures lightness. "The first dimension did not tell us whether a color was light or dark" (p. 6).
- **Chroma** — Chroma measures colour strength; value measures lightness.

# Common Errors

- **Error**: Assuming dark colours are "more saturated" and light colours are "less saturated."
  **Correction**: Value and chroma are independent. A colour can be dark and weak (low V, low C — dark gray-brown) or dark and strong (low V, high C — deep vivid blue).

# Common Confusions

- **Confusion**: Value and brightness are the same thing.
  **Clarification**: Value is a perceptually calibrated scale. Physical brightness (luminance) does not map linearly to perceived value — it follows a power law. Equal value steps require geometrically increasing luminance.

- **Confusion**: HSL lightness and Munsell value are interchangeable.
  **Clarification**: HSL lightness is computed from RGB components and is not perceptually uniform. Munsell value is photometrically calibrated. Two colours at HSL L=50% can appear very different in lightness; two colours at Munsell V5 appear equally light.

# Source Reference

Chapter 3: By T. M. Cleland, p. 4 (introduction). Chapter 5: II. Value, pp. 6-7.

# Verification Notes

- Definition source: Direct quote from p. 6 — Munsell's definition as cited by Cleland.
- Confidence rationale: High — explicit definition, clear examples, unambiguous concept.
- Uncertainties: The Stevens's Power Law reference in the Rosetta Stone mapping is modern colour science, not in the 1937 text.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. Mathematics (bounded scalar with psychophysical calibration) included.
