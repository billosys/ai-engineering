---
# === CORE IDENTIFICATION ===
concept: Hue
slug: hue

# === CLASSIFICATION ===
category: colour-theory
subcategory: colour-properties
tier: foundational
layer: 2-domain

# === PROVENANCE ===
source: "A Practical Description of The Munsell Color System"
source_slug: munsell-colour-system
authors: "T. M. Cleland"
chapter: "I. Hue"
chapter_number: 4
pdf_page: 4
section: "I. Hue"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "colour family"
  - "spectral identity"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - munsell-colour-system
  - colour-value
  - chroma
contrasts_with:
  - colour-value
  - chroma

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 3: What is the difference between hue, saturation/chroma, and lightness/value?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: mathematics
    concept: "Angular coordinate / modular arithmetic"
    rating: structural
    note: "Hue maps to the angular coordinate in cylindrical colour space. The 100-step Munsell hue circle is a cyclic group Z/100Z. Complementary hues relate by h → (h + 50) mod 100. Structurally identical to pitch classes in music theory (Z/12Z) and angles in trigonometry (mod 360)."

css_implementation:
  - property: "oklch() hue channel"
    example: "color: oklch(0.7 0.15 240); /* H = 240deg = blue */"
    support: baseline
  - property: "hsl() hue channel"
    example: "color: hsl(240, 50%, 50%); /* H = 240deg = blue */"
    support: baseline
---

# Quick Definition

Hue is the quality by which we distinguish one colour from another — red from yellow, green from blue — independent of how light, dark, strong, or weak the colour is.

# Core Definition

Munsell defines hue as "The quality by which we distinguish one color from another, as a red from a yellow, a green, a blue or a purple" (p. 4). Cleland immediately clarifies its independence: "but this dimension does not tell us whether the color is dark or light, or strong or weak. It merely refers to some point in the spectrum of all colors, such as we have seen in the reflection of sunlight through a prism" (p. 4).

Hue is the **first dimension** of the Munsell system, corresponding to the spectral identity of a colour — the dominant wavelength or combination of wavelengths perceived. In the Munsell system, hues are arranged in a **closed circle** because the spectrum wraps from red through purple back to red via non-spectral purples.

## Mathematical Formulation

Hue is the angular coordinate (θ) in the Munsell cylindrical space:
- θ ∈ [0, 100) Munsell steps, or equivalently [0°, 360°)
- Mapping: Munsell step n → n × 3.6 degrees
- Complementary hue = (step + 50) mod 100
- The space is **cyclic**: hue 100 = hue 0

# Prerequisites

This is a foundational concept with no prerequisites within this source. It is one of the three primitive dimensions of colour, comprehensible without prior knowledge of the Munsell system.

# Key Properties

1. **Spectral basis**: Hue corresponds to position in the visible spectrum, extended by non-spectral purples to close the circle. "It merely refers to some point in the spectrum of all colors" (p. 4).
2. **Independence from value and chroma**: Hue alone "does not tell us whether the color is dark or light, or strong or weak" (p. 4). A dark red and a light red share the same hue.
3. **Circular arrangement**: The spectrum is bent into a circle so that red meets red-purple, forming a continuous, closed loop (pp. 4-5).
4. **Decimal subdivision**: The circle divides into 10 families, each subdivided into 10 steps, yielding 100 distinguishable hue positions — "about as fine a variation of Hue as even a trained eye can distinguish" (p. 5).
5. **Fixed order**: Hues always appear in the same sequence. "We know it to be a scientific fact that it contains all possible hues, merging by indistinguishable degrees, one into the other, but always in a fixed order" (p. 4).

# Construction / Recognition

## To Construct/Create:
1. Begin with the visible spectrum — "a section taken out of a rainbow" (p. 4).
2. Identify 5 principal hues at perceptually equal intervals: Red, Yellow, Green, Blue, Purple.
3. Identify 5 intermediate hues halfway between each pair: Yellow-Red, Green-Yellow, Blue-Green, Purple-Blue, Red-Purple.
4. Bend the resulting 10-step band into a circle, joining red to red.
5. Subdivide each step into 10 further steps for a 100-step hue circle.

## To Identify/Recognise:
1. Isolate the chromatic identity of the colour — ignore how light/dark or vivid/dull it is.
2. Ask: "Is this closer to red, yellow, green, blue, or purple?" to find the principal hue.
3. Refine: "Is it between two principal hues?" to find the intermediate hue.

# Context & Application

- **Typical contexts**: Colour specification, colour mixing, palette construction, colour harmony analysis, digital colour picking.
- **Common applications**: Choosing the H value in `hsl()` or `oklch()` CSS functions; identifying complementary and analogous schemes; communicating colour intent independently of lightness and saturation.

## Cross-Domain Connections

**Mathematics → Structural**: Hue maps to angular measurement in a modular arithmetic system. The 100-step Munsell hue circle is a ring Z/100Z. Complementary hues are related by the involution h → (h + 50) mod 100. This is structurally identical to how pitch classes work in music theory (Z/12Z) — the key difference is the modulus (10 for Munsell hue families vs. 12 for pitch classes).

# Examples

**Example 1** (p. 4): Munsell's definition — "The quality by which we distinguish one color from another, as a red from a yellow, a green, a blue or a purple."

**Example 2** (p. 5): "when we state the first dimension of a color we are merely referring to its position on this circle of hues."

**Example 3** (p. 6): A colour "the hue of which is neither Red nor Yellow-Red, but about half way between the two, we would write it 10R."

# Relationships

## Builds Upon
This is a foundational primitive — it does not build upon other concepts.

## Enables
- **Munsell Hue Circle** — The arrangement of hues into a measured system.
- **Munsell Hue Notation** — The notation system for writing hue in a formula.
- **Complementary Colours** — Complements are defined by diametrically opposite hue positions.
- **Munsell Colour Notation** — Hue is the first element (H) in the H V/C formula.

## Related
- **Munsell Colour System** — Hue is the first of the system's three dimensions.
- **Colour Value** — The second dimension, independent of hue.
- **Chroma** — The third dimension, independent of hue.

## Contrasts With
- **Colour Value** — Value measures lightness/darkness; hue measures spectral identity.
- **Chroma** — Chroma measures colour strength; hue measures spectral identity.

# Common Errors

- **Error**: Confusing hue with colour. Saying "that's a different hue" when what changed was value or chroma.
  **Correction**: Hue is only one of three dimensions. A dark red and a light red have the same hue but different values.

- **Error**: Treating the hue scale as linear (with endpoints) rather than circular.
  **Correction**: The hue scale is circular — 10RP wraps to 1R. Arithmetic on hue values must be modular.

# Common Confusions

- **Confusion**: Hue and wavelength are the same thing.
  **Clarification**: Most hues correspond to dominant wavelengths, but purples (P, RP) are non-spectral — they do not correspond to any single wavelength. Hue is a perceptual quality, not a physical measurement.

- **Confusion**: All hue circles are equivalent.
  **Clarification**: Different colour models (HSL, Munsell, NCS, OKLCH) arrange hues differently. Munsell's circle is perceptually uniform (equal-step), while HSL's is based on RGB primaries with perceptual non-uniformities.

# Source Reference

Chapter 3: By T. M. Cleland, p. 4; Chapter 4: I. Hue, pp. 4-6.

# Verification Notes

- Definition source: Direct quote from p. 4 — Munsell's own definition as cited by Cleland.
- Confidence rationale: High — the definition is an exact quote, key properties are directly stated, the concept is unambiguous.
- Uncertainties: The mathematical formulation (modular arithmetic, angular mapping) is a modern formalisation not present in the 1937 text but is mathematically exact.
- Cross-reference status: References to chroma, complementary-colours verified as planned cards.
- Rosetta Stone check: Checked against 0010 tables. Mathematics (angular / modular arithmetic) included, rated STRUCTURAL.
