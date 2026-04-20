---
# === CORE IDENTIFICATION ===
concept: Monochromatic Harmony
slug: monochromatic-harmony

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
  - "single-hue harmony"
  - "monochromatic colour scheme"
  - "monochromatic palette"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - hue
  - colour-value
  - chroma
extends: []
related:
  - analogous-harmony
  - complementary-harmony
  - colour-harmony-as-order
contrasts_with:
  - complementary-harmony

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 23: How do you construct a colour palette starting from a single brand colour using OKLCH?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: music
    concept: "Variation within a single key/mode"
    rating: structural
    note: "Monochromatic harmony is structurally analogous to musical variation within a single key — varying dynamics (value) and articulation (chroma) while maintaining the same tonal centre (hue). The parallel captures the essential idea of unity through constraint."

css_implementation:
  - property: "oklch() value/chroma variation"
    example: "/* Monochromatic palette from a single hue */\n--base: oklch(0.5 0.15 240);\n--light: oklch(0.8 0.08 240);\n--dark: oklch(0.3 0.12 240);"
    support: baseline
---

# Quick Definition

Monochromatic harmony is a colour combination strategy using a single hue with variations in value and/or chroma — described by Cleland as "practically infallible" for producing harmonious results.

# Core Definition

Cleland describes monochromatic harmony as "another very simple and practically infallible series of color harmonies... made within a single Hue" (p. 15). He identifies three variations:

1. **Value contrast**: "a low Value of any Hue with a high Value of the same"
2. **Chroma contrast**: "a weak Chroma of any Hue with a stronger Chroma of the same"
3. **Combined**: "a low Value and weak Chroma with a high Value and stronger Chroma or vice versa"

He notes that "Experiments with the possibilities of single Hues will yield very interesting results in the great variety of colors thus obtainable" (p. 15).

# Prerequisites

- **Hue** — Understanding that a single hue anchors the palette.
- **Colour Value** — Value variation is a primary tool in monochromatic schemes.
- **Chroma** — Chroma variation provides additional range within the single hue.

# Key Properties

1. **Single hue constraint**: All colours share the same position on the hue circle.
2. **Value variation**: Dark to light within the same hue.
3. **Chroma variation**: Weak (grayish) to strong (vivid) within the same hue.
4. **Combined variation**: Both value and chroma can vary simultaneously.
5. **"Practically infallible"**: Harmony is almost guaranteed because the unity of hue provides inherent coherence.
6. **Great variety**: Despite the single-hue constraint, "a great variety of colors" is obtainable (p. 15).

# Construction / Recognition

## To Construct/Create:
1. Select a hue (e.g., 5B — Blue).
2. Choose two or more value levels (e.g., V3 and V7).
3. Choose two or more chroma levels (e.g., /2 and /6).
4. Combine: 5B 3/2 (dark, muted blue) with 5B 7/6 (light, vivid blue).
5. Apply balance principles: stronger chroma/higher value = smaller area.

## To Identify/Recognise:
1. All colours in the composition share the same hue family.
2. Variation occurs only in lightness and/or saturation.
3. The effect feels unified and cohesive.

# Context & Application

- **Typical contexts**: Brand palettes, card/component backgrounds, data visualisation (sequential colour scales), minimalist design.
- **Common applications**: Creating depth with a single brand colour; generating light/dark mode variants; building tint/shade scales for design tokens.

## Cross-Domain Connections

**Music Theory → Structural**: Monochromatic harmony parallels musical variation within a single key or mode — varying dynamics (loud/soft ↔ high/low value) and articulation (sharp/legato ↔ high/low chroma) while maintaining the same tonal centre (key ↔ hue). The unity principle is the same: coherence from constraint.

# Examples

**Example 1** (p. 15): Value contrast — "a low Value of any Hue with a high Value of the same" — e.g., dark blue with light blue.

**Example 2** (p. 15): Chroma contrast — "a weak Chroma of any Hue with a stronger Chroma of the same" — e.g., grayish blue with vivid blue.

**Example 3** (p. 15): Combined — "a low Value and weak Chroma with a high Value and stronger Chroma" — e.g., dark muted blue with light vivid blue.

# Relationships

## Builds Upon
- **Hue**, **Colour Value**, **Chroma** — The three dimensions constrained and varied.

## Enables
- **Colour Harmony as Order** — Monochromatic harmony exemplifies orderly paths through colour space (vertical movement along one hue's column in the colour solid).

## Related
- **Analogous Harmony** — Extends the principle by allowing neighbouring hues.
- **Colour Balance** — Balance principles apply to monochromatic schemes when chroma/value differ.

## Contrasts With
- **Complementary Harmony** — Complementary uses maximum hue contrast; monochromatic uses zero hue contrast.

# Common Errors

- **Error**: Using only value variation without chroma variation, producing a dull palette.
  **Correction**: Combine value AND chroma variation for richer monochromatic schemes.

# Common Confusions

- **Confusion**: Monochromatic means only using one exact colour.
  **Clarification**: Monochromatic means one hue with multiple values and chromas — potentially many distinct colours.

# Source Reference

Chapter 9: Color Combinations, p. 15.

# Verification Notes

- Definition source: Direct quotes from p. 15.
- Confidence rationale: High — explicitly described with clear examples.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Music theory mapping (variation within a key) rated STRUCTURAL.
