---
# === CORE IDENTIFICATION ===
concept: Triadic Colour Balance
slug: triadic-colour-balance

# === CLASSIFICATION ===
category: colour-theory
subcategory: colour-harmony
tier: advanced
layer: 2-domain

# === PROVENANCE ===
source: "A Practical Description of The Munsell Color System"
source_slug: munsell-colour-system
authors: "T. M. Cleland"
chapter: "Color Combinations"
chapter_number: 9
pdf_page: 15
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "three-colour balance"
  - "triadic harmony"
  - "split-complement balance"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - complementary-colours
  - colour-balance
  - munsell-balance-formula
extends:
  - colour-balance
  - complementary-harmony
related:
  - colour-harmony-as-order
  - munsell-colour-solid
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 30: A dashboard uses teal header, red error badges, green success indicators, blue links, yellow warning banners, and purple notification badges. It looks like a 'clown car.' What principle was violated, and how do you fix it?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: mathematics
    concept: "Partition of a vector into components"
    rating: structural
    note: "Splitting a complement into two component hues is structurally analogous to decomposing a vector into orthogonal components. The component areas must sum to the original area-weight to maintain balance, just as vector components must sum to the original vector."

css_implementation: []
---

# Quick Definition

Triadic colour balance extends the two-colour complementary balance to three colours by splitting one complement into its two constituent hues, dividing its area-weight between them proportionally.

# Core Definition

Cleland demonstrates the extension from two-colour to three-colour balance: "The principle governing the Balance of opposite colors will also apply to combinations of three colors. Let us assume that Blue is required as one of the colors in a three-color combination. We find that its opposite Hue is Yellow-Red, and as this is merely an admixture of Yellow and Red, it follows logically that the use of these two Hues, with due regard to proportion of areas or strength of Chroma, will yield a perfect color Balance" (p. 15).

The method: "we may proceed exactly as in the case of a two-color combination of Blue and Yellow-Red; but in this case we would divide the amount or strength of a correct Yellow-Red between our Yellow and our Red" (p. 16).

# Prerequisites

- **Complementary Colours** — Understanding which hues are opposite provides the starting point.
- **Colour Balance** — The area-proportioning principle extends directly.
- **Munsell Balance Formula** — The calculation of visual weight (C × V) is used to determine area splits.

# Key Properties

1. **Complement splitting**: The complement is decomposed into its two adjacent constituent hues.
2. **Area division**: The complement's area allocation is divided between the two replacement hues.
3. **Same balance principle**: The total visual weight on each side of the neutral axis remains equal.
4. **Richer palette**: Three hues provide more variety than two while maintaining balance.
5. **Extends to more colours**: Cleland notes "the same rule would apply to three or any other number of colors" (p. 14).

# Construction / Recognition

## To Construct/Create:
1. Select a primary hue (e.g., Blue 4/5).
2. Find its complement (Yellow-Red).
3. Calculate the two-colour balance: Blue weight = 4 × 5 = 20; YR 6/7 weight = 6 × 7 = 42.
4. Determine areas inversely: 42 parts Blue, 20 parts Yellow-Red.
5. Split the complement's area equally between its constituent hues: 10 parts Yellow 6/7 + 10 parts Red 6/7.
6. Final proportions: 42 parts Blue 4/5 : 10 parts Yellow 6/7 : 10 parts Red 6/7.

## To Identify/Recognise:
1. Three hues where two are adjacent and one is roughly opposite to their midpoint.
2. The single hue occupies a larger area; the two adjacent hues share a smaller combined area.
3. The composition feels balanced despite using three distinct hues.

# Context & Application

- **Typical contexts**: Brand palettes with primary + two accents, editorial design, packaging with multiple colour elements, data visualisation with three categories.
- **Common applications**: Extending a two-colour scheme to three colours without losing balance; creating richer palettes for complex layouts; proportioning dashboard colour elements.

## Cross-Domain Connections

**Mathematics → Structural**: Splitting a complement into component hues parallels vector decomposition. The complement Yellow-Red is decomposed into Yellow and Red components, each carrying a portion of the original vector's magnitude (area-weight). Balance is maintained because the sum of components equals the original, just as in vector addition.

# Examples

**Example 1** (pp. 15-16): Blue 4/5 with Yellow 6/7 and Red 6/7:
- Blue weight: 4 × 5 = 20 → 42 parts area.
- Yellow-Red weight: 6 × 7 = 42 → 20 parts area total.
- "If we would use 20 parts of Yellow-Red, 6/7, it naturally follows that we would use 10 parts of Red 6/7 and 10 parts of Yellow 6/7 to effect the same Balance."

# Relationships

## Builds Upon
- **Colour Balance** — The same inverse proportionality principle.
- **Complementary Harmony** — Triadic balance starts from a complementary pair.
- **Munsell Balance Formula** — Provides the calculation method.

## Enables
- **Colour Harmony as Order** — Triadic balance is an orderly multi-colour path through colour space.

## Related
- **Munsell Colour Solid** — Multi-colour combinations trace paths through the solid.

## Contrasts With
No direct contrast within this source.

# Common Errors

- **Error**: Splitting the complement but giving each replacement hue the full complement area, effectively doubling the warm side.
  **Correction**: The two replacement hues share the complement's area allocation — divide, don't duplicate.

- **Error**: Choosing arbitrary third colours rather than splitting the complement systematically.
  **Correction**: The third colour should be derived from the complement to maintain the balance relationship.

# Common Confusions

- **Confusion**: Triadic balance requires exactly equilateral spacing on the hue circle (120° apart).
  **Clarification**: Cleland's triadic method splits a complement into its adjacent constituents, which may not be equilateral. The balance comes from the proportioning, not the geometric spacing.

# Source Reference

Chapter 9: Color Combinations, pp. 15-16.

# Verification Notes

- Definition source: Direct quotes from pp. 15-16, with a detailed worked example.
- Confidence rationale: High — explicitly demonstrated with Blue + Yellow + Red example.
- Uncertainties: Cleland only works one example; generalization to non-adjacent splits is implied but not demonstrated.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Mathematics (vector decomposition) rated STRUCTURAL.
