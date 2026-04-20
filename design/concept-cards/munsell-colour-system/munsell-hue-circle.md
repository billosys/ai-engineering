---
# === CORE IDENTIFICATION ===
concept: Munsell Hue Circle
slug: munsell-hue-circle

# === CLASSIFICATION ===
category: colour-theory
subcategory: colour-models
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
  - "Munsell Color Circle"
  - "Munsell hue wheel"
  - "10-hue circle"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - hue
extends:
  - hue
related:
  - munsell-colour-system
  - munsell-hue-notation
  - complementary-colours
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 3: What is the difference between hue, saturation/chroma, and lightness/value?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: mathematics
    concept: "Cyclic group Z/10Z"
    rating: structural
    note: "The 10 principal hue steps form a cyclic group Z/10Z. Complementary hues are related by the order-2 element (+5 mod 10). The structure is the same as pitch-class set theory (Z/12Z) in music, differing only in the modulus."

css_implementation:
  - property: "oklch() hue angle mapping"
    example: "/* Approximate: 5R~29deg, 5Y~100deg, 5G~155deg, 5B~245deg, 5P~310deg */"
    support: baseline
---

# Quick Definition

The Munsell Hue Circle is the circular arrangement of 10 principal hue steps — 5 principal hues (R, Y, G, B, P) and 5 intermediate hues (YR, GY, BG, PB, RP) — subdivided decimally into 100 perceptually equal steps.

# Core Definition

Cleland constructs the hue circle through a thought experiment: take the full spectrum "fixed or printed on a band of paper" beginning and ending with red, then "bend this band around into a circular hoop, so that the red at one end meets and laps the red at the other end" — the result is "a perfect scale of Hue in the circular form in which we shall always consider it" (pp. 4-5).

The circle divides into **10 primary steps** at perceptually equal intervals:

**5 Principal Hues**: Red (R), Yellow (Y), Green (G), Blue (B), Purple (P)

**5 Intermediate Hues**: Yellow-Red (YR), Green-Yellow (GY), Blue-Green (BG), Purple-Blue (PB), Red-Purple (RP)

Each step subdivides into 10 decimal steps, yielding **100 distinguishable hue positions**. The numbering places 5 at each principal/intermediate hue and 10 at the boundary between families: "5 always marking a Principal Hue or an Intermediate Hue and 10 falling always half way between a Principal and an Intermediate Hue" (p. 5).

## Mathematical Formulation

The hue circle is a **cyclic group**:
- Coarse level: H ∈ {R, YR, Y, GY, G, BG, B, PB, P, RP} — Z/10Z
- Fine level: h ∈ {1, 2, ..., 100} — Z/100Z
- Complementary hue = (h + 50) mod 100
- No preferred origin; R is conventional, not privileged

# Prerequisites

- **Hue** — Understanding what hue is (spectral identity, independence from value/chroma) is required before arranging hues into a measured circle.

# Key Properties

1. **Circular topology**: No beginning or end. "So it is that when we state the first dimension of a color we are merely referring to its position on this circle of hues" (p. 5).
2. **5 + 5 structure**: Five principal and five intermediate hues at equal perceptual intervals. Munsell "wisely adopted a terminology which is commonly understood as referring only to color, and has avoided the use of such terms as orange, pink, violet, etc." (footnote, p. 5).
3. **Decimal subdivision**: 10 families × 10 substeps = 100 total steps — the perceptual resolution limit.
4. **Perceptual uniformity**: Spacing is calibrated so each step appears equally different from its neighbours.
5. **Diametric complements**: Hues directly across the circle mix to neutral gray.
6. **Systematic naming**: Intermediate hues are named by combining their flanking principals: Yellow-Red (not orange), Green-Yellow (not chartreuse).

# Construction / Recognition

## To Construct/Create:
1. Lay out the visible spectrum linearly, red to red.
2. Select 5 perceptually equidistant principal hues: R, Y, G, B, P.
3. Select 5 intermediate hues halfway between each pair: YR, GY, BG, PB, RP.
4. Bend into a circle, joining the two red ends.
5. Subdivide each step into 10 substeps, numbered 1-10, with 5 at the family centre.

## To Identify/Recognise:
1. A circular arrangement of colour with 10 named divisions.
2. Sequence: R → YR → Y → GY → G → BG → B → PB → P → RP → R.
3. Decimal subdivision numbering (1-10 within each family).

# Context & Application

- **Typical contexts**: Colour selection, palette construction, pigment mixing, colour education.
- **Common applications**: Identifying complementary colours (diametrically opposite); constructing analogous schemes (adjacent hues); mapping between Munsell notation and CSS hue angles.

## Cross-Domain Connections

**Mathematics → Structural**: The 10-hue circle is a cyclic group Z/10Z. Its symmetry properties — complementary pairs as involutions, triads as coset decompositions — are the same algebraic structures found in pitch-class set theory (Z/12Z) in music. The difference is the modulus: 10 for Munsell hues vs. 12 for pitch classes.

# Examples

**Example 1** (p. 4): "Let us imagine that we have such a spectrum fixed or printed on a band of paper, and that it begins at one end with red and going through all possible hues, it arrives back at red again."

**Example 2** (p. 5): "The 10 principal hues, then, are expressed: 5R, 5YR, 5Y, 5GY, 5G, 5BG, 5B, 5PB, 5P, 5RP."

**Example 3** (p. 5): The full sequence between two hues: "6RP, 7RP, 8RP, 9RP, 10RP, 1R, 2R, 3R, 4R, 5R, 6R, 7R, 8R, 9R, 10R, 1YR, 2YR, 3YR, 4YR."

# Relationships

## Builds Upon
- **Hue** — The hue circle is the structural arrangement of hue into a navigable, measured system.

## Enables
- **Munsell Hue Notation** — The numbering system is defined on this circle.
- **Complementary Colours** — Defined as diametrically opposite positions.
- **Analogous Harmony** — Adjacent hues on this circle.

## Related
- **Munsell Colour System** — The hue circle forms the equatorial plane of the colour solid.

## Contrasts With
The Munsell circle differs from the traditional artist's colour wheel (primaries at 120° based on pigment mixing) and from the HSL hue wheel (RGB primaries at 0°, 120°, 240°).

# Common Errors

- **Error**: Placing "orange," "violet," or other colloquial names on the Munsell hue circle.
  **Correction**: Munsell deliberately used systematic names: "What is called orange, for example, he calls yellow-red because it is a mixture of these two hues" (footnote, p. 5).

# Common Confusions

- **Confusion**: The 10 hue steps are spaced by dominant wavelength.
  **Clarification**: They are spaced by **perceptual equality**, not wavelength. The wavelength intervals between adjacent hues are unequal.

- **Confusion**: The Munsell hue circle is the same as the HSL/HSV hue wheel.
  **Clarification**: HSL's wheel is based on RGB primaries at 0°, 120°, 240°. Munsell has 5 principal hues at 72° intervals. The perceptual spacing differs significantly.

# Source Reference

Chapter 4: I. Hue, pp. 4-6.

# Verification Notes

- Definition source: Direct construction from Cleland's prose, pp. 4-5.
- Confidence rationale: High — step-by-step construction is explicit in the source.
- Uncertainties: OKLCH hue angle mapping in css_implementation is modern, not in the 1937 text.
- Cross-reference status: Verified against planned cards.
- Rosetta Stone check: Checked against 0010 tables. Mathematics (cyclic group) rated STRUCTURAL.
