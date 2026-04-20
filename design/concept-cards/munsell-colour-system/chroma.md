---
# === CORE IDENTIFICATION ===
concept: Chroma
slug: chroma

# === CLASSIFICATION ===
category: colour-theory
subcategory: colour-properties
tier: foundational
layer: 2-domain

# === PROVENANCE ===
source: "A Practical Description of The Munsell Color System"
source_slug: munsell-colour-system
authors: "T. M. Cleland"
chapter: "III. Chroma"
chapter_number: 6
pdf_page: 7
section: "III. Chroma"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "colour strength"
  - "saturation"
  - "purity"
  - "Munsell chroma"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - munsell-colour-system
  - hue
  - colour-value
  - neutral-axis
contrasts_with:
  - hue
  - colour-value

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 3: What is the difference between hue, saturation/chroma, and lightness/value?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: mathematics
    concept: "Radial coordinate in cylindrical space"
    rating: rigorous
    note: "Chroma is the radial coordinate (r) in the Munsell cylindrical system. Unlike hue (bounded, cyclic) and value (bounded, linear), chroma is open-ended — r ∈ [0, ∞) theoretically, limited only by available pigments or display gamut."

css_implementation:
  - property: "oklch() chroma channel"
    example: "color: oklch(0.7 0.15 240); /* C = 0.15 */"
    support: baseline
  - property: "hsl() saturation channel"
    example: "color: hsl(240, 50%, 50%); /* S = 50% (not directly comparable) */"
    support: baseline
---

# Quick Definition

Chroma is the third dimension of colour — the quality that measures how strong or weak a colour is, from neutral gray (chroma 0) outward to maximum colour intensity.

# Core Definition

Cleland introduces chroma through comparison: "Both may be green and of the same Value of light, but the emerald is strong in color and the grape is weak in color or grayer. It is this difference which is measured on the dimension of Chroma" (p. 7). Chroma measures the departure from neutral gray at any given value level.

The scale radiates outward from the neutral axis: "if we imagine any one of these hues on the circumference of the band to grow inward toward the gray pole in the center, growing grayer or weaker in color strength until it reaches this center pole and loses its color entirely, we have grasped the idea of the dimension known as Chroma" (p. 7).

Chroma is written in a colour formula as a numeral below a line: "/5, /8, /9, etc." (p. 7).

# Prerequisites

This is a foundational concept with no prerequisites within this source. It is one of the three primitive dimensions of colour.

# Key Properties

1. **Colour strength**: Chroma measures how far a colour departs from neutral gray. Zero chroma = pure gray; high chroma = vivid colour.
2. **Radial measurement**: Measured "at right angles to the vertical pole" — perpendicular to the value axis, radiating outward from the neutral center (p. 7).
3. **Open-ended scale**: Unlike hue (cyclic, 100 steps) and value (bounded, 0-10), chroma is "limited only by the strength of pigments" (p. 9). New pigments can extend the scale.
4. **Unequal maxima by hue**: "Colors differ by nature in their Chroma Strength, some being much more powerful than others. The strongest red pigment... is twice as powerful as the strongest blue-green pigment" — Red reaches /10, Blue-Green only /5 (p. 8).
5. **Unequal maxima by value**: "All colors do not reach their maximum Chroma Strength at the same level of Value" — strongest yellow is high-value, strongest blue is low-value (p. 8).
6. **Independence from hue and value**: A colour's chroma can be assessed independently of its hue or lightness.

# Construction / Recognition

## To Construct/Create:
1. Start at the neutral axis (gray) at a given value level.
2. Move radially outward in the direction of a specific hue.
3. Count the measured steps of increasing colour strength.
4. Each step represents one unit of chroma.

## To Identify/Recognise:
1. Compare the colour to a neutral gray of the same lightness (value).
2. Assess how different the colour is from that gray — how "colourful" it appears.
3. A vivid emerald is high chroma; a grayish sage is low chroma — even if both are the same hue and value.

# Context & Application

- **Typical contexts**: Palette construction, colour balance calculations, accessibility (low-chroma colours are safer for backgrounds), design systems.
- **Common applications**: The C channel in OKLCH; controlling vibrancy in design; creating muted/vivid variations of a base colour; the Munsell balance formula uses chroma as a key variable.

## Cross-Domain Connections

**Mathematics → Rigorous**: Chroma is the radial coordinate in the Munsell cylindrical coordinate system. It is the only unbounded dimension — r ∈ [0, ∞) theoretically — which explains the asymmetric "colour tree" shape of the practical Munsell solid. The open-endedness of chroma contrasts with the closed topology of hue (cyclic) and the bounded interval of value.

# Examples

**Example 1** (p. 7): The emerald vs. grape comparison — "Both may be green and of the same Value of light, but the emerald is strong in color and the grape is weak in color or grayer."

**Example 2** (p. 8): "The strongest red pigment used, for example, is twice as powerful as the strongest blue-green pigment and will require a correspondingly greater number of steps on a longer path to reach gray. The Chroma path of Red is the longest... being ten measured steps from the neutral pole; while Blue-Green is the shortest, being only five steps."

**Example 3** (p. 9): In the colour formula PB 3/2, the "/2" indicates chroma 2 — only two steps from neutral gray, a weak, grayish purple-blue.

# Relationships

## Builds Upon
This is a foundational primitive — it does not build upon other concepts.

## Enables
- **Munsell Colour Notation** — Chroma is the C component in H V/C.
- **Munsell Colour Solid** — Chroma determines the radial extent of the solid.
- **Colour Balance** — Balance requires proportioning area inversely to chroma.
- **Munsell Balance Formula** — Area ∝ 1/(Chroma × Value).

## Related
- **Munsell Colour System** — Chroma is the third of the system's three dimensions.
- **Neutral Axis** — Chroma is measured as departure from the neutral axis.
- **Hue** — The first dimension, independent of chroma.
- **Colour Value** — The second dimension, independent of chroma.

## Contrasts With
- **Hue** — Hue identifies which colour; chroma measures how much colour.
- **Colour Value** — Value measures lightness; chroma measures colour strength. "We may say of an emerald that it is green and that it is light, but... there is a decided difference" (p. 7).

# Common Errors

- **Error**: Using maximum chroma for all colours in a design, assuming "more colourful = better."
  **Correction**: Different hues have different maximum chromas. Using maximum chroma for every hue creates visual imbalance — red at /10 will overwhelm blue-green at /5 unless area is adjusted.

# Common Confusions

- **Confusion**: Chroma and saturation are the same thing.
  **Clarification**: Munsell chroma is an absolute measure — chroma 5 means the same departure from gray regardless of hue. HSL saturation is a relative percentage of maximum for that hue/lightness combination. Red at HSL saturation 100% and blue-green at 100% have very different perceptual colour strengths, but they'd have different Munsell chroma values.

- **Confusion**: Low chroma means the colour is dark.
  **Clarification**: Low chroma means the colour is close to gray — it could be a light gray (high value, low chroma) or a dark gray (low value, low chroma). Chroma and value are independent.

# Source Reference

Chapter 3: By T. M. Cleland, p. 4 (introduction). Chapter 6: III. Chroma, pp. 7-9.

# Verification Notes

- Definition source: Direct quotes from pp. 7-8. Cleland's emerald/grape comparison is the explicit definition.
- Confidence rationale: High — explicit definition with concrete examples; the concept is clearly and extensively described.
- Uncertainties: None significant.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. Mathematics (radial coordinate) included, rated RIGOROUS.
