---
concept: "Munsell Hue Circle"
slug: "munsell-hue-circle"
category: "colour-theory"
subcategory: "colour-models"
tier: "foundational"
layer: "2-domain"
source: "A Practical Description of The Munsell Color System"
source_slug: "munsell-colour-system"
authors: "T. M. Cleland"
chapter: "I. Hue"
chapter_number: 4
pdf_page: 4
section: "I. Hue"
extraction_confidence: "high"
aliases:
  - "Munsell Color Circle"
  - "Munsell hue wheel"
  - "10-hue circle"
prerequisites:
  - "hue"
extends:
  - "hue"
related:
  - "munsell-colour-system"
  - "munsell-hue-notation"
  - "complementary-colours"
contrasts_with: []
answers_questions:
  - "CQ 3: What is the difference between hue, saturation/chroma, and lightness/value?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Cyclic group Z/10Z"
    rating: "structural"
    note: "Indexing ten hue-family positions by residues 0 through 9 permits cyclic addition modulo 10; adding 5 twice returns to the starting index. This is a chosen indexing model, not the same group as Z/12Z or a law of colour mixing. Z/10Z has no three-element cosets."
css_implementation:
  -
    property: "color"
    example: "/* A Munsell hue alone is insufficient for OKLCH: identify H V/C, reference data, viewing conditions and destination gamut. */"
    support: "baseline"
---

# Quick Definition

The Munsell hue circle orders ten named families, five principal and five intermediate, around a neutral axis. A coarse ten- or hundred-position diagram is a selected representation of that ordering, not an exact perceptual metric.

# Core Definition

The earlier extraction attributes the following wording to Cleland; the book and prepared text are unavailable, so quotations, locators, context and historical attribution remain unverified.

Retained reported wording: "fixed or printed on a band of paper" "bend this band around into a circular hoop, so that the red at one end meets and laps the red at the other end" "a perfect scale of Hue in the circular form in which we shall always consider it" "5 always marking a Principal Hue or an Intermediate Hue and 10 falling always half way between a Principal and an Intermediate Hue"

The named circular order supports a diagram. Ten or one hundred selected positions may be indexed modularly, but exact equal appearance, discrimination limits and neutral mixing do not follow. Decimal hue prefixes exist and hue alone cannot determine an OKLCH conversion.

## Mathematical Formulation

Choose indices 0…9 or 0…99, not family labels themselves, as residues of Z/10Z or Z/100Z. Adding half the chosen even modulus represents diagram opposition. This construction supplies modular arithmetic; it establishes neither perceptual distances nor mixing. Three-element cosets cannot partition a group of order 10.

Further recorded extraction wording (unverified attribution/context; these are not adopted universal claims):

- "So it is that when we state the first dimension of a color we are merely referring to its position on this circle of hues" (p. 5)

# Prerequisites

- **Hue** — Supplies the relevant H/V/C or diagram vocabulary for this card; this is an understanding route, not a claim of physical or historical derivation.

# Key Properties

1. The circular family order is R→YR→Y→GY→G→BG→B→PB→P→RP→R.
2. The recorded principal/intermediate labels are 5R, 5YR, 5Y, 5GY, 5G, 5BG, 5B, 5PB, 5P, 5RP.
3. Ten subdivisions per family give a convenient 100-position diagram; decimal prefixes allow other samples.
4. Calibration seeks approximate perceptual ordering; equal drawn angles do not prove equal appearance.
5. Recorded opposite pairs include R↔BG and B↔YR. Diagram opposition does not guarantee neutral mixture, WCAG contrast or pleasure.
6. Family names are notation conventions, not physical decomposition into constituent pigments.

# Construction / Recognition

## To Construct/Create:

1. Draw the ten families in their circular order.
2. Place their nominal centres and subdivisions, keeping the diagram convention explicit.
3. Use actual reference data and full H/V/C for conversion. Hue alone leaves value/chroma unknown.

## To Identify/Recognise:

1. Look for ten systematic family abbreviations, including five intermediate families.
2. Separate the label sequence from an optional integer index.
3. Check whether a displayed circle is a schematic or a measured sample set.

# Context & Application

Use the circle for colour-order teaching and candidate scheme navigation. Adjacent and opposed selections are named strategies; they do not establish accessibility, physical pigment mixing or a direct CSS-angle mapping.

## Cross-Domain Connections

Index ten selected positions by 0…9 with addition modulo 10; +5 twice is the identity. For 0…99, +50 twice is the identity. Z/10Z and Z/12Z have unequal cardinalities. Coset sizes divide 10, so there are no three-element cosets in Z/10Z; ordinary three-colour selections are not such cosets.

# Examples

Recorded extraction examples below retain their reported locators; they were not checked against the missing book. Any balance or harmony result is historical advice or conditional arithmetic, not an independently observed mixing or aesthetic result.

**Example 1** (p. 4): "Let us imagine that we have such a spectrum fixed or printed on a band of paper, and that it begins at one end with red and going through all possible hues, it arrives back at red again."

**Example 2** (p. 5): "The 10 principal hues, then, are expressed: 5R, 5YR, 5Y, 5GY, 5G, 5BG, 5B, 5PB, 5P, 5RP."

**Example 3** (p. 5): The full sequence between two hues: "6RP, 7RP, 8RP, 9RP, 10RP, 1R, 2R, 3R, 4R, 5R, 6R, 7R, 8R, 9R, 10R, 1YR, 2YR, 3YR, 4YR."

# Relationships

## Builds Upon

- **Hue** — The hue attribute is organized into the reported circular family order.

## Enables

- **Munsell Hue Notation** — Numeric prefixes/family labels locate hue positions, including decimals.
- **Complementary Colours** — Opposition is a diagram relationship, not a neutral-mixing or contrast theorem.
- **Analogous Harmony** — Neighbouring positions motivate a candidate strategy, without a harmony guarantee.

## Related

- **Munsell Colour System** — The circle diagrams hue around the neutral axis at a chosen value, not an automatic empirical equator.

## Contrasts With

No additional card-local bullet is recorded here. This is navigation scope, not a verified absence or a historical-source completeness result.

# Common Errors

- **Error**: Treating colloquial colour names or a spectral line as a unique Munsell designation.
  **Correction**: Use the systematic family and numeric prefix; names and hue alone are insufficient to specify a colour.

# Common Confusions

- **Confusion**: Drawn equal angles mean wavelength or exact perceptual equality.
  **Clarification**: They are diagram positions; calibration, appearance and viewing conditions are separate.
- **Confusion**: Munsell and HSL/OKLCH circles share numeric hue values.
  **Clarification**: Their coordinates differ; conversion needs full H/V/C, identified data/reference conditions and a destination gamut.

# Source Reference

Chapter 4: I. Hue, pp. 4-6.

# Verification Notes

- This revision reviewed the complete available card body and local relationships/CQ components; it did not inspect the missing original book, prepared Cleland text or diagrams. All historical quotations, dates, page claims, named attributions and source-specific efficacy claims remain unassessed for fidelity.
- Extraction-confidence metadata is preserved from the predecessor. Earlier “exact quote,” “verified planned cards” and “0010 checked” notes described historical extraction/navigation observations, not current independent semantic proof.
- Current technical qualifications use the [RIT renotation overview](https://www.rit.edu/science/munsell-color-science-lab-educational-resources#munsell-renotation-data), [CIE appearance terminology](https://cie.co.at/eilvterm/17-22-067) and [CSS Color4](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/), with elementary conditional algebra where stated. These do not establish historical-source fidelity, exact perceptual equality, physical neutralisation or aesthetic guarantees.
- CSS metadata/body examples are model-specific illustrations, not Munsell conversions, checked contrast pairs or mandatory project palettes. No browser, assistive-technology, disc/material experiment or hosted rendering result was produced.
