---
concept: "Neutral Axis"
slug: "neutral-axis"
category: "colour-theory"
subcategory: "colour-systems"
tier: "foundational"
layer: "2-domain"
source: "A Practical Description of The Munsell Color System"
source_slug: "munsell-colour-system"
authors: "T. M. Cleland"
chapter: "II. Value / III. Chroma"
chapter_number: 5
pdf_page: 6
section: null
extraction_confidence: "high"
aliases:
  - "gray pole"
  - "neutral pole"
  - "neutral center"
  - "achromatic axis"
  - "value axis"
prerequisites: []
extends: []
related:
  - "munsell-colour-system"
  - "colour-value"
  - "chroma"
  - "munsell-colour-solid"
contrasts_with: []
answers_questions:
  - "CQ 3: What is the difference between hue, saturation/chroma, and lightness/value?"
rosetta_stone: []
css_implementation:
  -
    property: "oklch() with zero chroma"
    example: "color: oklch(0.5 0 0); /* neutral gray at L=0.5 */"
    support: "baseline"
---

# Quick Definition

The neutral axis is the achromatic value axis in the Munsell diagram. It supplies a zero-chroma reference at each value; hue is undefined on it.

# Core Definition

The earlier extraction attributes the following wording to Cleland; the book and prepared text are unavailable, so quotations, locators, context and historical attribution remain unverified.

Retained reported wording: "a vertical pole, or axis to our circle of Hues, black at the lower end, representing total absence of light, and white at the top, representing pure light, and between these a number of divisions of gray, regularly graded between black and white" "itself, of no color, but is pure gray" "all of the Hues cross and meet in the neutral pole, which represents the point of their union"

The neutral axis supplies an achromatic value reference at each height. Hue is undefined at zero chroma. Historical black/white rhetoric does not define every physical material or display extreme, and a photometer does not directly establish perceptual equality.

Further recorded extraction wording (unverified attribution/context; these are not adopted universal claims):

- "if we imagine any one of these hues... to grow inward toward the gray pole in the center, growing grayer or weaker in color strength until it reaches this center pole and loses its color entirely" (p. 7)
- "The nearer our colors approach to this common center (the weaker they are in Chroma) the more nearly they are related; and the easier it becomes to harmonize them" (p. 17)

# Prerequisites

No card-local prerequisite is recorded in the preserved metadata. This is an editorial starting point, not proof that the concept has no dependencies in the wider domain.

# Key Properties

1. Neutrals have C=0 and no perceptual hue.
2. The nominal value range is 0–10, with V5 a coordinate midpoint, not 50% luminance or OKLCH L=.5.
3. Radial paths approach neutral at a chosen value; all hues do not meet at one single gray for all values.
4. The recorded black/white “absence/pure light” rhetoric is historical, not a physical description of every surface/display.
5. Lower chroma can be a candidate design choice; it does not guarantee harmony, contrast or accessibility.
6. A fulcrum is a metaphor in the historical balance account, not a proof of neutral mixing.

# Construction / Recognition

## To Construct/Create:

1. Identify a reference scale and viewing conditions.
2. Plot neutral samples on the value axis, retaining decimals as required; the historical integer 1–9 example remains one sampling.
3. Use calibrated reference data rather than photometry alone to claim perceptual steps.

## To Identify/Recognise:

1. Look for an achromatic axis at zero chroma in the named model.
2. Distinguish Munsell value, OKLCH L and photometric luminance.
3. A CSS neutral can store a hue angle, but the angle is powerless at zero chroma.

# Context & Application

A neutral/value study can reveal tonal grouping, but a grayscale preview does not establish rendered-pair contrast or accessibility. Use actual composited pairs, roles and states rather than a neutral-axis diagram as a pass criterion.

## Cross-Domain Connections

The neutral axis is structurally comparable to the vertical axis of a cylindrical diagram. It supplies a radial origin at each height; this schematic connection proves neither perceptual distance nor a mechanical fulcrum law.

# Examples

Recorded extraction examples below retain their reported locators; they were not checked against the missing book. Any balance or harmony result is historical advice or conditional arithmetic, not an independently observed mixing or aesthetic result.

**Example 1** (p. 6): The value scale from 0 to 10 with "the middle one of these will be 5 — what is referred to as Middle Value."

**Example 2** (p. 7): "Around this pole we may place our band representing the scale of Hue and then if we imagine any one of these hues on the circumference of the band to grow inward toward the gray pole in the center, growing grayer or weaker in color strength until it reaches this center pole and loses its color entirely."

**Example 3** (p. 17): "All of the Hues cross and meet in the neutral pole, which represents the point of their union."

# Relationships

## Builds Upon

No additional card-local bullet is recorded here. This is navigation scope, not a verified absence or a historical-source completeness result.

## Enables

- **Colour Value** — The axis diagrams neutral value samples; it is not a physical calibrated instrument.
- **Chroma** — It supplies the radial zero reference; numerical distance is not a universal perceptual metric.
- **Munsell Colour Solid** — The value axis is a structural diagram component, with reference-dependent colour boundaries.
- **Colour Balance** — The fulcrum is a historical metaphor; no neutral cancellation follows from the axis alone.

## Related

- **Hue** — Hue is arranged around the axis and becomes undefined at zero chroma.
- **Munsell Colour System** — It is the system’s achromatic reference at each value, not one gray shared across all values.
- **Complementary Colours** — A diagram diameter passes through the neutral centre; mixture/contrast are separate claims.

## Contrasts With

No additional card-local bullet is recorded here. This is navigation scope, not a verified absence or a historical-source completeness result.

# Common Errors

- **Error**: Treating the historical 1–9 example as every achievable neutral or all allowed samples.
  **Correction**: Values can be decimal; physical extremes depend on material, display and reference conditions.

# Common Confusions

- **Confusion**: Neutral means unimportant or universally harmonious.
  **Clarification**: Neutral references help describe colour; their suitability depends on the composition and task.
- **Confusion**: A photometer directly measures equal perceived value.
  **Clarification**: Photometry measures light quantities; perceptual/reference calibration is an additional matter.

# Source Reference

Chapter 5: II. Value, p. 6. Chapter 6: III. Chroma, pp. 7-9. Chapter 9: Color Combinations, p. 17.

# Verification Notes

- This revision reviewed the complete available card body and local relationships/CQ components; it did not inspect the missing original book, prepared Cleland text or diagrams. All historical quotations, dates, page claims, named attributions and source-specific efficacy claims remain unassessed for fidelity.
- Extraction-confidence metadata is preserved from the predecessor. Earlier “exact quote,” “verified planned cards” and “0010 checked” notes described historical extraction/navigation observations, not current independent semantic proof.
- Current technical qualifications use the [RIT renotation overview](https://www.rit.edu/science/munsell-color-science-lab-educational-resources#munsell-renotation-data), [CIE appearance terminology](https://cie.co.at/eilvterm/17-22-067) and [CSS Color4](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/), with elementary conditional algebra where stated. These do not establish historical-source fidelity, exact perceptual equality, physical neutralisation or aesthetic guarantees.
- CSS metadata/body examples are model-specific illustrations, not Munsell conversions, checked contrast pairs or mandatory project palettes. No browser, assistive-technology, disc/material experiment or hosted rendering result was produced.
