---
# === CORE IDENTIFICATION ===
concept: Analogous Harmony
slug: analogous-harmony

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
  - "neighbouring hue harmony"
  - "analogous colour scheme"
  - "adjacent hue harmony"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - hue
  - munsell-hue-circle
extends: []
related:
  - monochromatic-harmony
  - complementary-harmony
  - colour-harmony-as-order
contrasts_with:
  - complementary-harmony

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 23: How do you construct a colour palette starting from a single brand colour using OKLCH?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "oklch() hue offset"
    example: "/* Analogous palette: base hue ± 30-36 degrees */\n--base: oklch(0.6 0.15 240);\n--warm: oklch(0.6 0.12 210);\n--cool: oklch(0.6 0.12 270);"
    support: baseline
---

# Quick Definition

Analogous harmony uses neighbouring hues on the colour circle — colours that are adjacent rather than opposite — producing harmony through proximity rather than contrast.

# Core Definition

Cleland describes analogous combinations as using "neighboring Hues, that is of any Hue with the Hue which immediately precedes or follows it on the scale — Green with Green-Yellow, Red with Yellow-Red, Yellow with Yellow-Red, etc." (p. 15).

The key distinction from complementary harmony: "In all of these cases the harmony depends upon proximity rather than contrast, as in the case of opposites" (p. 15).

He notes two extensions: "These may in turn be varied by taking them at different steps of Value and different strengths of Chroma" and "In the same way, Hues may be combined with neighboring intermediate Hues" (p. 15).

# Prerequisites

- **Hue** — Understanding hue identity and position on the circle.
- **Munsell Hue Circle** — Adjacency is defined by position on the circle.

# Key Properties

1. **Proximity-based**: Harmony comes from closeness on the hue circle, not opposition.
2. **Adjacent hues**: Typically spanning 1-3 steps on the 10-hue circle (e.g., R, YR, Y).
3. **Value/chroma variation**: Can be enriched by varying value and chroma within the adjacent hue range.
4. **Extends to intermediate hues**: Not limited to principal hues — any adjacent positions work.
5. **Contrast with complementary**: "proximity rather than contrast" (p. 15).

# Construction / Recognition

## To Construct/Create:
1. Select a primary hue (e.g., Blue, 5B).
2. Include one or both immediately neighbouring hues (e.g., Blue-Green 5BG, Purple-Blue 5PB).
3. Vary value and chroma within each hue for additional richness.
4. Optionally extend to 2 neighbours on each side for a wider analogous range.

## To Identify/Recognise:
1. All hues in the composition occupy a contiguous arc of the hue circle.
2. The arc spans no more than about 3-5 hue families.
3. The effect feels cohesive and unified, with subtle hue variation.

# Context & Application

- **Typical contexts**: Nature-inspired palettes, gradient backgrounds, editorial design, brand palette extensions.
- **Common applications**: Creating warm or cool palettes (selecting from the warm or cool arc of the circle); enriching a monochromatic scheme with subtle hue variation; designing harmonious multi-colour layouts.

# Examples

**Example 1** (p. 15): "Neighboring Hues — Green with Green-Yellow, Red with Yellow-Red, Yellow with Yellow-Red."

**Example 2** (p. 15): "These may in turn be varied by taking them at different steps of Value and different strengths of Chroma."

# Relationships

## Builds Upon
- **Hue** — Analogous harmony varies the hue dimension within a narrow range.
- **Munsell Hue Circle** — Adjacency is defined on this circle.

## Enables
- **Colour Harmony as Order** — Analogous harmony exemplifies orderly paths (short arcs) through colour space.

## Related
- **Monochromatic Harmony** — Monochromatic is the limit case of analogous (zero hue variation).

## Contrasts With
- **Complementary Harmony** — Complementary uses maximum hue contrast; analogous uses minimal hue contrast.

# Common Errors

- **Error**: Spanning too many hue families (e.g., from R through G) and calling it "analogous."
  **Correction**: Analogous harmony works with neighbouring hues — typically 2-3 adjacent families. Wider spans need balance adjustments.

# Common Confusions

- **Confusion**: Analogous colours are always harmonious regardless of value and chroma choices.
  **Clarification**: Hue proximity provides inherent harmony, but extreme value or chroma contrasts within an analogous scheme can still feel discordant. Cleland recommends varying value and chroma in orderly steps.

# Source Reference

Chapter 9: Color Combinations, p. 15.

# Verification Notes

- Definition source: Direct quotes from p. 15.
- Confidence rationale: High — explicitly described with examples.
- Uncertainties: The specific number of hue families that constitute "analogous" is not quantified in the source — Cleland says "immediately precedes or follows."
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: No formal mapping assigned for analogous harmony specifically.
