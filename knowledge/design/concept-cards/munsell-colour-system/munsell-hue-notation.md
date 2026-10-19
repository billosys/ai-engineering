---
concept: "Munsell Hue Notation"
slug: "munsell-hue-notation"
category: "colour-theory"
subcategory: "colour-notation"
tier: "intermediate"
layer: "2-domain"
source: "A Practical Description of The Munsell Color System"
source_slug: "munsell-colour-system"
authors: "T. M. Cleland"
chapter: "I. Hue"
chapter_number: 4
pdf_page: 5
section: "I. Hue"
extraction_confidence: "high"
aliases:
  - "Munsell hue designation"
  - "H component of Munsell notation"
prerequisites:
  - "hue"
  - "munsell-hue-circle"
extends:
  - "munsell-hue-circle"
related:
  - "munsell-colour-system"
  - "munsell-colour-notation"
contrasts_with: []
answers_questions:
  - "CQ 3: What is the difference between hue, saturation/chroma, and lightness/value?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition

Munsell hue notation combines a numeric prefix with a family abbreviation, for example 5R, 7YR or 2.5R. It locates a hue within this colour-order convention, not a complete colour or CSS angle.

# Core Definition

The earlier extraction attributes the following wording to Cleland; the book and prepared text are unavailable, so quotations, locators, context and historical attribution remain unverified.

Retained reported wording: "in writing a color formula, of which one of these intermediate hues is a part, we place the numeral, denoting the position of the hue on this scale before the letter which stands for the nearest Principal or Intermediate Hue, thus 7R, 3YR, 2Y"

Numeric prefix plus family identifies a hue under the notation convention. The recorded 5-centre/10-boundary examples remain useful, while decimal prefixes and full H/V/C prevent treating the hundred-position diagram as an exhaustive scale.

Further recorded extraction wording (unverified attribution/context; these are not adopted universal claims):

- "about as fine a variation of Hue as even a trained eye can distinguish" (p. 5)

# Prerequisites

- **Hue** — Supplies the relevant H/V/C or diagram vocabulary for this card; this is an understanding route, not a claim of physical or historical derivation.
- **Munsell Hue Circle** — Supplies the relevant H/V/C or diagram vocabulary for this card; this is an understanding route, not a claim of physical or historical derivation.

# Key Properties

1. Write the numeral before the family: 5R, not R5.
2. In the recorded convention, 5 marks a family centre, not a physically pure or maximally saturated colour.
3. 10R names the boundary toward YR; it does not mean “more red.”
4. Decimal hue prefixes occur; the integer 1…10 example is not an exhaustive parser or precision limit.
5. The hue prefix is distinct from V and C in H V/C.
6. A hue designation alone does not determine gamut, lightness or chroma.

# Construction / Recognition

## To Construct/Create:

1. Identify the reference hue family and position under stated conditions.
2. Write the numeric prefix, including decimals where appropriate, then its abbreviation.
3. Add measured/reference V and C for a full designation. Keep historical short forms distinguishable from fully qualified modern notation.

## To Identify/Recognise:

1. Recognize a numeric prefix followed by a valid family abbreviation.
2. Check decimal as well as integer values and the notation source's boundary convention.
3. Do not confuse the prefix with the number before the slash in full H V/C.

# Context & Application

Use notation for recording or comparing reference colours. Mapping to OKLCH requires full H V/C, reference data, viewing/white-point assumptions and destination-gamut handling, rather than substitution of the hue label.

# Examples

Recorded extraction examples below retain their reported locators; they were not checked against the missing book. Any balance or harmony result is historical advice or conditional arithmetic, not an independently observed mixing or aesthetic result.

**Example 1** (p. 5): "The 10 principal hues, then, are expressed: 5R, 5YR, 5Y, 5GY, 5G, 5BG, 5B, 5PB, 5P, 5RP."

**Example 2** (p. 5): The full sequence: "6RP, 7RP, 8RP, 9RP, 10RP, 1R, 2R, 3R, 4R, 5R, 6R, 7R, 8R, 9R, 10R, 1YR, 2YR, 3YR, 4YR."

**Example 3** (p. 6): "If, for example, we wish to write the formula of a color, the hue of which is neither Red nor Yellow-Red, but about half way between the two, we would write it 10R."

# Relationships

## Builds Upon

- **Hue** — The notation encodes the hue attribute, not its spectrum.
- **Munsell Hue Circle** — Labels reference the ordered families, without restricting precision to integer positions.

## Enables

- **Munsell Colour Notation** — Hue notation supplies H; V/C and conditions remain necessary.

## Related

- **Munsell Colour System** — Notation is one descriptive apparatus of the system, not proof of exact perceptual spacing.

## Contrasts With

No additional card-local bullet is recorded here. This is navigation scope, not a verified absence or a historical-source completeness result.

# Common Errors

- **Error**: Reversing prefix and family or using the prefix as saturation.
  **Correction**: 7R locates hue only; value and chroma are separate.
- **Error**: Treating a chosen residue 0 as a literal family prefix.
  **Correction**: Keep the abstract index separate from notation conventions such as writing the boundary as 10R rather than 0YR.

# Common Confusions

- **Confusion**: 10R is the “reddest” red.
  **Clarification**: 5R is the nominal family centre and 10R the boundary; neither defines spectral purity or maximum chroma.
- **Confusion**: Only integer hue labels are valid.
  **Clarification**: Decimal labels such as 2.5R and 7.5R are present in renotation data.

# Source Reference

Chapter 4: I. Hue, pp. 5-6.

# Verification Notes

- This revision reviewed the complete available card body and local relationships/CQ components; it did not inspect the missing original book, prepared Cleland text or diagrams. All historical quotations, dates, page claims, named attributions and source-specific efficacy claims remain unassessed for fidelity.
- Extraction-confidence metadata is preserved from the predecessor. Earlier “exact quote,” “verified planned cards” and “0010 checked” notes described historical extraction/navigation observations, not current independent semantic proof.
- Current technical qualifications use the [RIT renotation overview](https://www.rit.edu/science/munsell-color-science-lab-educational-resources#munsell-renotation-data), [CIE appearance terminology](https://cie.co.at/eilvterm/17-22-067) and [CSS Color4](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/), with elementary conditional algebra where stated. These do not establish historical-source fidelity, exact perceptual equality, physical neutralisation or aesthetic guarantees.
- CSS metadata/body examples are model-specific illustrations, not Munsell conversions, checked contrast pairs or mandatory project palettes. No browser, assistive-technology, disc/material experiment or hosted rendering result was produced.
