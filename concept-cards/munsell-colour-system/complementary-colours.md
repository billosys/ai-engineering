---
# === CORE IDENTIFICATION ===
concept: Complementary Colours
slug: complementary-colours

# === CLASSIFICATION ===
category: colour-theory
subcategory: colour-relationships
tier: foundational
layer: 2-domain

# === PROVENANCE ===
source: "A Practical Description of The Munsell Color System"
source_slug: munsell-colour-system
authors: "T. M. Cleland"
chapter: "Opposite or Complementary Colors"
chapter_number: 7
pdf_page: 10
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "opposite colours"
  - "complementary colors"
  - "opposite hues"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - hue
  - munsell-hue-circle
extends: []
related:
  - munsell-colour-system
  - neutral-axis
  - colour-balance
  - complementary-harmony
contrasts_with:
  - analogous-harmony

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 3: What is the difference between hue, saturation/chroma, and lightness/value?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: music
    concept: "Tritone / consonance-dissonance"
    rating: loose
    note: "Complementary colours provide maximum contrast and mutual enhancement, loosely analogous to the tritone's maximum intervallic tension. However, trichromatic colour perception and frequency-based pitch perception are fundamentally different mechanisms, so the parallel is suggestive, not formally grounded."

css_implementation:
  - property: "oklch() relative colour syntax"
    example: "color: oklch(from var(--base) l c calc(h + 180)); /* complementary hue */"
    support: partial
---

# Quick Definition

Complementary colours are hue pairs that sit directly opposite each other on the Munsell hue circle and, when mixed in correct proportions, produce a perfectly neutral gray.

# Core Definition

Cleland explains: "each Hue on the circle will be found directly opposite to another Hue. Thus a straight line drawn from Red on the circle of Hues through the neutral pole will pass through Blue-Green, its opposite or complementary color" (p. 10).

The term "opposite" is preferred in the Munsell system "because it is simple and is self-explanatory" (p. 10). The relationship has an empirical basis: "When any two colors are truly opposite or at the point of strongest contrast, their admixture will produce a perfectly neutral gray" (p. 10). This can be verified by "arranging two opposite colors on a disc in proportions relative to the Chroma strength of each and revolving them with such rapidity that we cannot see them separately and they are mixed, when if they are truly opposite, they will unite in a perfect gray" (p. 10).

A key structural property: "each of the Principal Hues, Red, Purple, Blue, Green and Yellow falls opposite an Intermediate Hue, Blue-Green, Green-Yellow, Yellow-Red, etc." (p. 10).

# Prerequisites

- **Hue** — Understanding what hue is (the spectral dimension) is required.
- **Munsell Hue Circle** — Complementary pairs are defined by their diametric positions on this circle.

# Key Properties

1. **Diametric opposition**: Complements are exactly opposite on the hue circle — a straight line through the neutral pole connects them.
2. **Maximum contrast**: "Two colors which are thus opposite to one another are... in actual use the most strongly contrasting" (p. 10).
3. **Gray-producing mixture**: Mixed in correct proportions (by chroma strength), they produce perfectly neutral gray.
4. **Principal ↔ Intermediate**: Each principal hue's complement is an intermediate hue: R↔BG, Y↔PB, G↔RP, B↔YR, P↔GY.
5. **Any point works**: "It does not matter at what point we draw the line, whether it is from one of the regular Hues or from a point between two Hues, if it passes through the center it will fall upon the Hue... which is its strongest contrast" (p. 10).
6. **Non-opposite mixing**: Lines between non-opposite hues cross non-neutral points — their mixture produces a colour intermediate between them, not gray (pp. 10-11).

# Construction / Recognition

## To Construct/Create:
1. Locate the hue on the Munsell hue circle.
2. Draw a straight line through the neutral centre to the opposite side.
3. The hue at the far end is the complement.
4. Mathematically: complement = (hue step + 50) mod 100.

## To Identify/Recognise:
1. Two colours that, when mixed (e.g., on Maxwell discs), produce neutral gray.
2. Two hues on exactly opposite sides of the hue circle.
3. Maximum visual contrast when placed side-by-side.

# Context & Application

- **Typical contexts**: Colour scheme design, palette construction, achieving maximum contrast, creating visual vibrance.
- **Common applications**: Complementary colour schemes in design; accent colour selection (complement of primary colour); colour correction in photography and film.

## Cross-Domain Connections

**Music Theory → Loose**: Complementary colours provide maximum chromatic contrast and mutual enhancement, loosely analogous to the tritone (augmented fourth / diminished fifth), which provides maximum intervallic tension in music. Both occupy the midpoint of their respective circular systems (hue circle / pitch-class circle). However, the analogy is suggestive rather than rigorous: colour perception is trichromatic (three cone types) while pitch perception is frequency-based, and the perceptual mechanisms diverge fundamentally.

# Examples

**Example 1** (p. 10): "A straight line drawn from Red on the circle of Hues through the neutral pole will pass through Blue-Green, its opposite or complementary color."

**Example 2** (p. 10): "A line from Blue through the neutral pole will pass through Yellow-Red."

**Example 3** (pp. 10-11): Non-opposite mixing — "three different lines have been drawn, no one of them through the neutral center. These lines... cross points which are not neutral, but nearer to one or another of the Hues lying between."

# Relationships

## Builds Upon
- **Hue** — Complementary relationships exist between hues.
- **Munsell Hue Circle** — The circle defines which hues are opposite.

## Enables
- **Colour Balance** — Complementary colours are the basis for balance calculations.
- **Complementary Harmony** — Using complements together in design.
- **Triadic Colour Balance** — Extending complementary principles to three colours.

## Related
- **Neutral Axis** — Lines connecting complements pass through it.
- **Munsell Colour System** — Complementary relationships are a fundamental system property.

## Contrasts With
- **Analogous Harmony** — Analogous uses neighbouring hues (proximity); complementary uses opposite hues (maximum contrast).

# Common Errors

- **Error**: Assuming that equal areas of complementary colours will balance.
  **Correction**: Balance requires accounting for chroma strength. Red /10 needs twice the area of Blue-Green /5 for balance (see colour-balance).

# Common Confusions

- **Confusion**: Any two contrasting colours are complementary.
  **Clarification**: Complementary has a precise definition: the two colours must mix to neutral gray. Red and green are complementary in the Munsell system; red and blue are not (they produce a purple-red, not gray).

- **Confusion**: Complementary colours clash and should be avoided.
  **Clarification**: Opposite colours "tend to stimulate and enhance each other" (p. 15) — they are the basis of some of the most effective colour combinations when properly balanced.

# Source Reference

Chapter 7: Opposite or Complementary Colors, pp. 10-11.

# Verification Notes

- Definition source: Direct quotes from pp. 10-11.
- Confidence rationale: High — explicitly defined with empirical verification method (Maxwell discs).
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. Music theory mapping rated LOOSE per 0010 specifications.
