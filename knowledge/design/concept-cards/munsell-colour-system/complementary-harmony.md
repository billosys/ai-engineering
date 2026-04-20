---
# === CORE IDENTIFICATION ===
concept: Complementary Harmony
slug: complementary-harmony

# === CLASSIFICATION ===
category: colour-theory
subcategory: colour-harmony
tier: intermediate
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
  - "opposite-hue harmony"
  - "complementary colour scheme"
  - "contrast harmony"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - complementary-colours
  - colour-balance
extends:
  - complementary-colours
related:
  - monochromatic-harmony
  - analogous-harmony
  - colour-harmony-as-order
  - munsell-balance-formula
contrasts_with:
  - analogous-harmony
  - monochromatic-harmony

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 23: How do you construct a colour palette starting from a single brand colour using OKLCH?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: music
    concept: "Resolution of dissonance"
    rating: loose
    note: "Complementary harmony uses maximum chromatic contrast resolved through proportional balance, loosely analogous to how musical dissonance (e.g., a tritone) resolves to consonance. Both involve tension that is managed, not avoided. The parallel is suggestive rather than formally grounded."

css_implementation:
  - property: "oklch() hue offset"
    example: "/* Complementary palette: base hue + 180 degrees */\n--base: oklch(0.5 0.15 240);\n--complement: oklch(0.6 0.10 60);\n/* Balance: complement occupies smaller area at higher chroma */"
    support: baseline
---

# Quick Definition

Complementary harmony is the use of opposite hues together in a design — described by Cleland as "one of the simplest and surest of color harmonies" — where maximum chromatic contrast is managed through proportional area balance.

# Core Definition

Cleland identifies complementary harmony as a fundamental colour combination: "This combination of opposites is one of the simplest and surest of color harmonies. We have seen how, if properly proportioned as to amount or area, these opposite colors will balance in perfect neutrality" (p. 15).

Beyond mere balance, he notes a perceptual enhancement effect: "another interesting fact with regard to them is that when placed together these contrasting colors tend to stimulate and enhance each other" (p. 15).

The key requirements are: (1) the two hues must be diametrically opposite on the hue circle, and (2) their areas must be proportioned inversely to their visual weight (Chroma × Value) to achieve balance.

# Prerequisites

- **Complementary Colours** — Understanding which hue pairs are opposite on the circle.
- **Colour Balance** — The area-proportioning principle that makes complementary combinations harmonious rather than jarring.

# Key Properties

1. **Maximum contrast**: Opposite hues provide the strongest possible hue contrast.
2. **Mutual enhancement**: Complements "stimulate and enhance each other" when juxtaposed (p. 15).
3. **Area-dependent**: Harmony requires correct area proportions — not equal areas, but inversely proportional to Chroma × Value.
4. **Neutralisation test**: If mixed in their given area proportions, the colours would produce neutral gray.
5. **"Simplest and surest"**: Cleland ranks this among the most reliable harmony types (p. 15).

# Construction / Recognition

## To Construct/Create:
1. Select a hue (e.g., Blue 5B).
2. Find its complement on the hue circle (Yellow-Red 5YR).
3. Choose value and chroma levels for each.
4. Calculate area proportions using the balance formula: Area_A/Area_B = (C_B × V_B)/(C_A × V_A).
5. Assign the smaller area to the colour with higher visual weight.

## To Identify/Recognise:
1. Two dominant hues in the composition are diametrically opposite on the hue circle.
2. The stronger/lighter colour occupies a smaller area.
3. The colours feel simultaneously contrasting and unified.

# Context & Application

- **Typical contexts**: Brand identity (primary + accent), call-to-action design, data visualisation (binary categories), sports team colours.
- **Common applications**: Accent colour selection (complement of primary brand colour); creating visual vibrance and energy; drawing attention through contrast while maintaining balance.

## Cross-Domain Connections

**Music Theory → Loose**: Complementary harmony manages maximum chromatic tension through proportional balance, loosely analogous to how musical dissonance resolves to consonance. A tritone (maximum intervallic tension) can resolve satisfyingly when voice-led correctly; likewise, complementary colours produce satisfying results when area-balanced correctly. Both involve controlled tension rather than avoidance of contrast.

# Examples

**Example 1** (p. 15): "This combination of opposites is one of the simplest and surest of color harmonies... these contrasting colors tend to stimulate and enhance each other."

**Example 2** (pp. 12-13): Red 5/10 with Blue-Green 5/5 — balanced using 5 parts Red to 10 parts Blue-Green (inverse ratio of chromas at same value).

**Example 3** (p. 14): Yellow 7/9 with Purple-Blue 3/4 — 12 parts Yellow to 63 parts Purple-Blue (inverse ratio of Chroma × Value products).

# Relationships

## Builds Upon
- **Complementary Colours** — The hue relationship that makes this harmony possible.
- **Colour Balance** — The proportioning principle that makes it work.

## Enables
- **Triadic Colour Balance** — Extends the complementary principle to three colours by splitting one complement into its constituent hues.
- **Colour Harmony as Order** — Complementary harmony exemplifies orderly paths (diameters) through colour space.

## Related
- **Munsell Balance Formula** — Provides the mathematical tool for calculating correct proportions.

## Contrasts With
- **Analogous Harmony** — Uses proximity (minimal contrast); complementary uses opposition (maximum contrast).
- **Monochromatic Harmony** — Uses zero hue contrast; complementary uses maximum hue contrast.

# Common Errors

- **Error**: Using equal areas of complementary colours regardless of their chroma and value differences.
  **Correction**: Areas must be inversely proportional to visual weight (C × V). Equal areas only balance when both colours have the same chroma and value.

- **Error**: Avoiding complementary combinations because they seem "too bold."
  **Correction**: Complements "stimulate and enhance each other" — the boldness is a feature. Control intensity through area balance and chroma moderation.

# Common Confusions

- **Confusion**: Complementary harmony and complementary colours are the same concept.
  **Clarification**: Complementary colours is the structural relationship (opposite on the circle); complementary harmony is the design strategy of using that relationship with proper balance for aesthetic effect.

# Source Reference

Chapter 9: Color Combinations, p. 15. Chapter 8: Balance, pp. 11-14.

# Verification Notes

- Definition source: Direct quotes from p. 15, supplemented by balance examples from Ch. 8.
- Confidence rationale: High — explicitly described as "one of the simplest and surest of color harmonies."
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Music theory mapping (dissonance resolution) rated LOOSE per 0010 specifications.
