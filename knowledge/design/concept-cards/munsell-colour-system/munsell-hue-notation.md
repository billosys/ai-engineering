---
# === CORE IDENTIFICATION ===
concept: Munsell Hue Notation
slug: munsell-hue-notation

# === CLASSIFICATION ===
category: colour-theory
subcategory: colour-notation
tier: intermediate
layer: 2-domain

# === PROVENANCE ===
source: "A Practical Description of The Munsell Color System"
source_slug: munsell-colour-system
authors: "T. M. Cleland"
chapter: "I. Hue"
chapter_number: 4
pdf_page: 5
section: "I. Hue"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Munsell hue designation"
  - "H component of Munsell notation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - hue
  - munsell-hue-circle
extends:
  - munsell-hue-circle
related:
  - munsell-colour-system
  - munsell-colour-notation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 3: What is the difference between hue, saturation/chroma, and lightness/value?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []
css_implementation: []
---

# Quick Definition

Munsell hue notation is a numeral-letter code (e.g., `5R`, `7YR`, `10RP`) specifying a colour's exact position on the 100-step hue circle, where the numeral indicates the substep and the letter(s) indicate the hue family.

# Core Definition

Cleland describes the procedure: "in writing a color formula, of which one of these intermediate hues is a part, we place the numeral, denoting the position of the hue on this scale before the letter which stands for the nearest Principal or Intermediate Hue, thus 7R, 3YR, 2Y" (p. 5).

The system uses 10 hue-family abbreviations:
- **Principal**: R (Red), Y (Yellow), G (Green), B (Blue), P (Purple)
- **Intermediate**: YR (Yellow-Red), GY (Green-Yellow), BG (Blue-Green), PB (Purple-Blue), RP (Red-Purple)

Each family spans 10 substeps (1-10), with **5 always marking the principal or intermediate hue itself**, and **10 falling halfway between** two families (p. 5).

# Prerequisites

- **Hue** — Understanding spectral identity is necessary before learning to notate it.
- **Munsell Hue Circle** — The notation references positions on the 100-step circle.

# Key Properties

1. **Numeral-before-letter format**: `5R`, not `R5`.
2. **5 = family centre**: `5R` is the purest red; `5YR` is the most balanced yellow-red.
3. **10 = family boundary**: `10R` is halfway between Red and Yellow-Red.
4. **100-step precision**: "about as fine a variation of Hue as even a trained eye can distinguish" (p. 5).
5. **Systematic naming**: Munsell avoided colloquial names — "What is called orange, for example, he calls yellow-red" (footnote, p. 5).
6. **Component of full notation**: First element in H V/C (e.g., `5R 6/10`).

# Construction / Recognition

## To Construct/Create:
1. Determine which of the 10 hue families the colour falls in.
2. Determine the substep (1-10), where 5 = family centre.
3. Write numeral before abbreviation: `7R`.
4. For a principal hue: `5R`. For a boundary: `10R`.

## To Identify/Recognise:
1. A 1-2 digit numeral followed by 1-2 uppercase letters.
2. Numeral in range 1-10.
3. Letters are one of the 10 valid abbreviations.

# Context & Application

- **Typical contexts**: Colour specification sheets, paint chip identification, Munsell colour atlases, soil classification (USDA).
- **Common applications**: Writing the hue component of a Munsell formula; converting between Munsell hue and OKLCH hue angle.

# Examples

**Example 1** (p. 5): "The 10 principal hues, then, are expressed: 5R, 5YR, 5Y, 5GY, 5G, 5BG, 5B, 5PB, 5P, 5RP."

**Example 2** (p. 5): The full sequence: "6RP, 7RP, 8RP, 9RP, 10RP, 1R, 2R, 3R, 4R, 5R, 6R, 7R, 8R, 9R, 10R, 1YR, 2YR, 3YR, 4YR."

**Example 3** (p. 6): "If, for example, we wish to write the formula of a color, the hue of which is neither Red nor Yellow-Red, but about half way between the two, we would write it 10R."

# Relationships

## Builds Upon
- **Hue** — Hue notation is the symbolic encoding of the hue concept.
- **Munsell Hue Circle** — The notation maps to positions on the 100-step circle.

## Enables
- **Munsell Colour Notation** — Hue notation is the first component of H V/C.

## Related
- **Munsell Colour System** — Part of the system's notation apparatus.

## Contrasts With
No contrasting notation systems are described in this source.

# Common Errors

- **Error**: Writing the letter before the number (`R5` instead of `5R`).
  **Correction**: Numeral always first: `5R`, `7YR`, `10PB`.

- **Error**: Using `0` as a substep (e.g., `0YR`).
  **Correction**: Range is 1-10. What would be `0YR` is written as `10R`.

# Common Confusions

- **Confusion**: `10R` means "very red" (highest number).
  **Clarification**: `10R` is the *least* red position in the R family — it's the boundary with YR. The "most red" red is `5R`.

- **Confusion**: The numeral indicates chroma or saturation strength.
  **Clarification**: The numeral indicates only hue position within a family. Chroma is separate, written after the slash.

# Source Reference

Chapter 4: I. Hue, pp. 5-6.

# Verification Notes

- Definition source: Direct quotes from Cleland, pp. 5-6.
- Confidence rationale: High — procedurally described with multiple examples.
- Uncertainties: None significant.
- Cross-reference status: Verified against planned cards.
- Rosetta Stone check: No specific mapping for hue notation as a procedural concept.
