---
# === CORE IDENTIFICATION ===
concept: Neutral Axis
slug: neutral-axis

# === CLASSIFICATION ===
category: colour-theory
subcategory: colour-systems
tier: foundational
layer: 2-domain

# === PROVENANCE ===
source: "A Practical Description of The Munsell Color System"
source_slug: munsell-colour-system
authors: "T. M. Cleland"
chapter: "II. Value / III. Chroma"
chapter_number: 5
pdf_page: 6
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "gray pole"
  - "neutral pole"
  - "neutral center"
  - "achromatic axis"
  - "value axis"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - munsell-colour-system
  - colour-value
  - chroma
  - munsell-colour-solid
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 3: What is the difference between hue, saturation/chroma, and lightness/value?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "oklch() with zero chroma"
    example: "color: oklch(0.5 0 0); /* neutral gray at L=0.5 */"
    support: baseline
---

# Quick Definition

The neutral axis is the achromatic vertical centre of the Munsell colour system — a scale of pure grays from black to white, around which all chromatic colours are arranged, and from which chroma is measured as radial departure.

# Core Definition

Cleland describes the neutral axis as "a vertical pole, or axis to our circle of Hues, black at the lower end, representing total absence of light, and white at the top, representing pure light, and between these a number of divisions of gray, regularly graded between black and white" (p. 6). The axis is "itself, of no color, but is pure gray" (p. 7).

The neutral axis serves three structural roles simultaneously: it is the **value scale** (measuring lightness along its length), the **chroma origin** (the zero-chroma reference from which all colour strength is measured), and the **convergence point of all hues** — "all of the Hues cross and meet in the neutral pole, which represents the point of their union" (p. 17).

# Prerequisites

This is a foundational structural concept with no prerequisites within this source.

# Key Properties

1. **Achromatic**: The axis has no hue — it consists entirely of neutral grays.
2. **Vertical orientation**: Black at the bottom (0), white at the top (10), with grays between.
3. **Chroma zero-point**: All chroma measurements begin at this axis — chroma is distance from the neutral pole.
4. **Convergence point**: All hues approach the same gray as chroma decreases — "if we imagine any one of these hues... to grow inward toward the gray pole in the center, growing grayer or weaker in color strength until it reaches this center pole and loses its color entirely" (p. 7).
5. **Harmonising function**: "The nearer our colors approach to this common center (the weaker they are in Chroma) the more nearly they are related; and the easier it becomes to harmonize them" (p. 17).
6. **Balance fulcrum**: In colour balance, the neutral axis is the fulcrum — balanced opposite colours produce the gray at this centre.

# Construction / Recognition

## To Construct/Create:
1. Establish pure black (0) and pure white (10) as theoretical endpoints.
2. Grade 9 perceptually equal steps of gray between them (1-9).
3. Calibrate with a photometer for perceptual equality.
4. This axis becomes the vertical spine of the colour solid.

## To Identify/Recognise:
1. Any achromatic scale from dark to light in a colour model is a neutral axis.
2. In the Munsell system, it is the vertical centre around which all hues orbit.
3. In OKLCH, it is any colour with C = 0.

# Context & Application

- **Typical contexts**: Colour system architecture, grayscale design, value studies, accessibility checking.
- **Common applications**: Testing designs in grayscale (stripping all colour to the neutral axis); establishing the value structure before adding colour; measuring chroma departure; anchoring balance calculations.

## Cross-Domain Connections

The neutral axis is structurally analogous to the z-axis in a cylindrical coordinate system. All radial (chroma) and angular (hue) measurements reference this central axis.

# Examples

**Example 1** (p. 6): The value scale from 0 to 10 with "the middle one of these will be 5 — what is referred to as Middle Value."

**Example 2** (p. 7): "Around this pole we may place our band representing the scale of Hue and then if we imagine any one of these hues on the circumference of the band to grow inward toward the gray pole in the center, growing grayer or weaker in color strength until it reaches this center pole and loses its color entirely."

**Example 3** (p. 17): "All of the Hues cross and meet in the neutral pole, which represents the point of their union."

# Relationships

## Builds Upon
This is a foundational structural element — it does not build upon other concepts.

## Enables
- **Colour Value** — The neutral axis is the physical embodiment of the value scale.
- **Chroma** — Chroma is measured as radial distance from the neutral axis.
- **Munsell Colour Solid** — The neutral axis is the structural spine.
- **Colour Balance** — The neutral fulcrum is where opposite chromas cancel to gray.

## Related
- **Hue** — All hues orbit the neutral axis.
- **Munsell Colour System** — The neutral axis is the backbone of the system.
- **Complementary Colours** — Lines connecting complements pass through the neutral axis.

## Contrasts With
No direct contrast — the neutral axis is a structural element.

# Common Errors

- **Error**: Placing pure black (0) and pure white (10) on the practical scale as achievable values.
  **Correction**: Cleland notes these are unattainable ideals. The practical scale runs from 1 (darkest gray) to 9 (lightest gray).

# Common Confusions

- **Confusion**: Thinking "neutral" means the axis has no role in chromatic design.
  **Clarification**: The neutral axis is the reference against which all chromatic colours are measured. It is the fulcrum of colour balance and the convergence point of all hues.

- **Confusion**: Equating the neutral axis with "brightness" without nuance.
  **Clarification**: The value steps are perceptually calibrated (photometric), not linearly related to physical luminance. They represent perceived lightness, not raw light intensity.

# Source Reference

Chapter 5: II. Value, p. 6. Chapter 6: III. Chroma, pp. 7-9. Chapter 9: Color Combinations, p. 17.

# Verification Notes

- Definition source: Direct quotes from Ch 5 p. 6 and Ch 6 p. 7. Additional properties from Ch 9 p. 17.
- Confidence rationale: High — explicitly described across multiple chapters with consistent terminology.
- Uncertainties: None.
- Cross-reference status: Verified across Chs 5, 6, 7, 8, and 9.
- Rosetta Stone check: No formal mapping assigned — structural parallel to cylindrical z-axis is noted but captured in munsell-colour-solid card.
