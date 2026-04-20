---
# === CORE IDENTIFICATION ===
concept: Munsell Colour Notation
slug: munsell-colour-notation

# === CLASSIFICATION ===
category: colour-theory
subcategory: colour-notation
tier: intermediate
layer: 2-domain

# === PROVENANCE ===
source: "A Practical Description of The Munsell Color System"
source_slug: munsell-colour-system
authors: "T. M. Cleland"
chapter: "III. Chroma"
chapter_number: 6
pdf_page: 9
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Munsell notation"
  - "HV/C notation"
  - "Munsell colour formula"
  - "colour formula"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - hue
  - colour-value
  - chroma
  - munsell-hue-notation
extends:
  - munsell-colour-system
related:
  - munsell-colour-solid
  - munsell-hue-circle
  - neutral-axis
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 3: What is the difference between hue, saturation/chroma, and lightness/value?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: software-engineering
    concept: "Structured identifier / addressing system"
    rating: rigorous
    note: "The HV/C notation is a structured addressing system for colour space, analogous to structured identifiers in code (namespaced identifiers, semantic versioning, coordinate addresses). Each component (H, V, C) addresses one axis of the coordinate system."

css_implementation:
  - property: "oklch() function"
    example: "color: oklch(0.5 0.1 240); /* L C H — different order from Munsell H V/C */"
    support: baseline
---

# Quick Definition

Munsell Colour Notation is the complete formula for specifying any colour as H V/C — Hue Value/Chroma — where each component independently addresses one dimension of the Munsell colour space (e.g., PB 3/2 = Purple-Blue at Value 3, Chroma 2).

# Core Definition

Cleland presents the full notation as the synthesis of the three dimensions: "we are given a certain color to measure and define and we find that upon the scale of Hue it is Purple-Blue. Upon comparing it with the scale of Value, we find it is but three steps from the bottom, and that it is only two steps away from the neutral gray pole upon the scale of Chroma. A complete formula for this color would, therefore, be written P-B 3/2" (p. 9).

He contrasts this with imprecise alternatives: "It is scarcely necessary to point out the practical advantages of such a system of definite measurement and notation over the vague and variable terms in general use, borrowed from the vegetable and animal kingdoms, such as plum, olive, fawn, mouse, etc., of which no two persons ever have quite the same idea" (p. 9).

# Prerequisites

- **Hue** — Provides the H component.
- **Colour Value** — Provides the V component.
- **Chroma** — Provides the C component.
- **Munsell Hue Notation** — The specific encoding of hue in the formula.

# Key Properties

1. **Three-component structure**: H V/C — hue designation, value numeral, slash, chroma numeral.
2. **Hue encoding**: Letter(s) with optional numeral prefix: R, YR, 7R, 3YR, etc.
3. **Value above the line**: Written as superscript or before the slash — "B6/" means blue at value 6 (p. 6).
4. **Chroma below the line**: Written after the slash — "/5" means 5 chroma steps from neutral.
5. **Compact and unambiguous**: Replaces vague colour names with measurable coordinates.
6. **Enables computation**: Balance, complementarity, and harmony can be calculated directly from the notation.

# Construction / Recognition

## To Construct/Create:
1. Determine the hue and write its notation (e.g., PB, 7R).
2. Determine the value (1-9) and write it after the hue.
3. Determine the chroma and write it after a slash.
4. Assemble: H V/C — e.g., PB 3/2, R 5/10, Y 7/9.

## To Identify/Recognise:
1. Letter(s) followed by a numeral/slash/numeral pattern.
2. First numeral (before slash) is value (1-9 range).
3. Second numeral (after slash) is chroma (open-ended, typically 1-14).

# Context & Application

- **Typical contexts**: Colour specification, paint matching, printing, soil classification (USDA), colour science.
- **Common applications**: Communicating exact colours; recording measurements; performing balance calculations; mapping to OKLCH or other digital colour spaces.

## Cross-Domain Connections

**Engineering → Rigorous**: The HV/C notation is structurally identical to a coordinate address in a three-dimensional space. Just as a structured identifier in engineering encodes multiple independent dimensions into a single reference, the Munsell notation encodes three orthogonal dimensions of colour into a compact formula. The notation is not merely a label — it is a structured address from which geometric relationships can be computed.

# Examples

**Example 1** (p. 9): "P-B 3/2" — Purple-Blue at Value 3 (dark), Chroma 2 (weak, near gray).

**Example 2** (p. 6): "B6/" — blue at value 6, chroma not yet specified.

**Example 3** (p. 12): "R5/5 will balance B-G 5/5" — demonstrating how the notation supports balance calculations.

## Worked Example

To notate a specific colour:
1. The colour appears to be a moderately dark, fairly vivid blue leaning toward purple.
2. Hue: Purple-Blue, near position 5 → **PB**.
3. Value: matches gray step 3 → **3**.
4. Chroma: 2 steps from neutral → **/2**.
5. Complete notation: **PB 3/2**.

# Relationships

## Builds Upon
- **Hue**, **Colour Value**, **Chroma** — Provide the three components.
- **Munsell Hue Notation** — Provides the specific hue encoding.
- **Munsell Colour System** — The notation is the symbolic expression of the system.

## Enables
- **Colour Balance** — Balance calculations operate on V and C values.
- **Munsell Balance Formula** — Requires extracting V and C from the notation.

## Related
- **Munsell Colour Solid** — The notation addresses points within the 3D solid.
- **Neutral Axis** — Neutral colours would be written as N V/ (e.g., N 5/ for middle gray).

## Contrasts With
No contrasting notation systems are described in this source.

# Common Errors

- **Error**: Writing H C/V instead of H V/C.
  **Correction**: Value always before the slash, chroma after.

- **Error**: Confusing the hue numeral prefix (e.g., "7" in 7R) with value or chroma.
  **Correction**: The hue prefix is part of the hue component only; it locates position on the 100-step hue circle.

# Common Confusions

- **Confusion**: Higher chroma number always means more "colourful" visual experience.
  **Clarification**: Chroma numbers are absolute. Red /10 and Blue-Green /5 are both at their respective maxima, even though the numbers differ. Red is simply a more powerful hue.

# Source Reference

Chapters 4-6: I. Hue, II. Value, III. Chroma, pp. 4-9.

# Verification Notes

- Definition source: Direct quote from p. 9 — the PB 3/2 example. Additional rules from pp. 5-6.
- Confidence rationale: High — explicitly and procedurally described with multiple examples.
- Uncertainties: Neutral colour notation (N V/) is standard Munsell practice but not explicitly stated in this source.
- Cross-reference status: Verified across Chs 4, 5, 6, 8, 9.
- Rosetta Stone check: Engineering mapping (structured identifiers) rated RIGOROUS.
