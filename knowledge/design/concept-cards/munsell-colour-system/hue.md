---
concept: "Hue"
slug: "hue"
category: "colour-theory"
subcategory: "colour-properties"
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
  - "colour family"
  - "spectral identity"
prerequisites: []
extends: []
related:
  - "munsell-colour-system"
  - "colour-value"
  - "chroma"
contrasts_with:
  - "colour-value"
  - "chroma"
answers_questions:
  - "CQ 3: What is the difference between hue, saturation/chroma, and lightness/value?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Angular coordinate / modular arithmetic"
    rating: "structural"
    note: "A chosen discrete circular hue index can use addition modulo 100. This indexing construction is not a perceptual metric, pigment-mixing law, CSS hue conversion, or an isomorphism with the 12-element pitch-class group."
css_implementation:
  -
    property: "oklch() hue channel"
    example: "color: oklch(0.7 0.15 240); /* CSS candidate; not a Munsell conversion */"
    support: "baseline"
  -
    property: "hsl() hue channel"
    example: "color: hsl(240, 50%, 50%); /* H = 240deg = blue */"
    support: "baseline"
---

# Quick Definition

Hue is a perceptual colour attribute: the red/yellow/green/blue character or combinations in a closed ring. It is distinct from lightness and chroma; it does not specify a unique wavelength or a complete colour.

# Core Definition

The earlier extraction attributes the following wording to Cleland; the book and prepared text are unavailable, so quotations, locators, context and historical attribution remain unverified.

Retained reported wording: "The quality by which we distinguish one color from another, as a red from a yellow, a green, a blue or a purple" "but this dimension does not tell us whether the color is dark or light, or strong or weak. It merely refers to some point in the spectrum of all colors, such as we have seen in the reflection of sunlight through a prism"

Hue is perceptual, not a unique wavelength. Munsell hue ordering and the abstract modular index are distinct. A family designation gives neither V/C nor a CSS hue angle; the circular diagram is not a physical spectral-red-to-red theorem.

## Mathematical Formulation

Choose an abstract index h ∈ {0,…,99}, with addition modulo 100. Its plotted angle may be θ=3.6h degrees; h→h+50 is then an involution. This statement is exact about the chosen index. It is not a law of wavelength, physical mixture, perceptual distance or Munsell-to-CSS conversion.

Further recorded extraction wording (unverified attribution/context; these are not adopted universal claims):

- "about as fine a variation of Hue as even a trained eye can distinguish" (p. 5)
- "We know it to be a scientific fact that it contains all possible hues, merging by indistinguishable degrees, one into the other, but always in a fixed order" (p. 4)

# Prerequisites

No card-local prerequisite is recorded in the preserved metadata. This is an editorial starting point, not proof that the concept has no dependencies in the wider domain.

# Key Properties

1. Hue identifies a perceptual quality, not a unique spectral composition. Non-spectral purples already defeat a one-wavelength account.
2. Hue, value and chroma have distinct meanings; a fixed hue label does not imply unrestricted realizability at every value/chroma.
3. Munsell orders named hue families circularly; this is not a physical bending of a spectrum.
4. A 100-position index is a useful selected discretization, not a limit on discrimination or exact equal-appearance claim. Decimal prefixes such as 2.5R exist.
5. Hue is undefined at zero chroma. A CSS stored angle at C=0 does not create a perceived hue.

# Construction / Recognition

## To Construct/Create:

1. Use the ordered families R, YR, Y, GY, G, BG, B, PB, P, RP as a reference diagram.
2. Distinguish a diagram/index from measured colour samples. For actual matching, specify reference conditions and full H V/C.
3. If discrete arithmetic helps, choose indices 0…99 explicitly; do not treat a family label such as 5R as a raw residue.

## To Identify/Recognise:

1. Separate hue character from light/dark and muted/vivid comparisons.
2. Use a reference sample under stated viewing conditions; names alone do not provide a measurement.
3. At neutral chroma do not assign a perceptual hue from an arbitrary angle.

# Context & Application

Use hue to describe and compare candidates. CSS HSL and OKLCH have their own hue coordinates; the examples are CSS-model candidates, not Munsell conversions. For a supplied brand colour, preserve its value, choose task roles, explore candidates and check destination gamut and complete rendered pairs/states.

## Cross-Domain Connections

A chosen finite index with addition modulo 100 forms Z/100Z. Adding 50 twice returns to the same index. Mapping n to 3.6n degrees draws that index, not a measured CSS or perceptual conversion. Z/100Z and the 12-element pitch-class group have different orders and are not isomorphic.

# Examples

Recorded extraction examples below retain their reported locators; they were not checked against the missing book. Any balance or harmony result is historical advice or conditional arithmetic, not an independently observed mixing or aesthetic result.

**Example 1** (p. 4): Munsell's definition — "The quality by which we distinguish one color from another, as a red from a yellow, a green, a blue or a purple."

**Example 2** (p. 5): "when we state the first dimension of a color we are merely referring to its position on this circle of hues."

**Example 3** (p. 6): A colour "the hue of which is neither Red nor Yellow-Red, but about half way between the two, we would write it 10R."

# Relationships

## Builds Upon

No additional card-local bullet is recorded here. This is navigation scope, not a verified absence or a historical-source completeness result.

## Enables

- **Munsell Hue Circle** — Hue-circle ordering uses the hue attribute; the diagram is not a wavelength or perceptual metric.
- **Munsell Hue Notation** — Hue notation encodes position in the named convention, not a CSS conversion.
- **Complementary Colours** — Opposition is defined within a selected hue diagram; mixing/contrast need separate support.
- **Munsell Colour Notation** — Hue is H in H V/C; full reference conditions are still needed.

## Related

- **Munsell Colour System** — Hue is one of its three named coordinates.
- **Colour Value** — Value concerns light/dark character, distinct from hue; realizability/perception need conditions.
- **Chroma** — Chroma concerns departure from neutral, distinct from hue; hue is undefined at zero chroma.

## Contrasts With

- **Colour Value** — Value and hue describe different attributes, not lightness versus unique wavelength.
- **Chroma** — Chroma and hue describe different attributes; numeric independence is not unrestricted perceptual independence.

# Common Errors

- **Error**: Calling a value or chroma change a hue change.
  **Correction**: Describe the changed coordinate and conditions; multiple changes can occur together.
- **Error**: Treating 10RP→1R as a numerical discontinuity in colour or a discrimination threshold.
  **Correction**: It is the recorded integer-label wrap; decimal notation permits finer positions and the circular index is a separate construction.

# Common Confusions

- **Confusion**: Hue equals wavelength.
  **Clarification**: Hue is perceptual; different spectra can have similar appearances and purples need no single spectral wavelength.
- **Confusion**: Every hue circle has the same angles or exact equal-looking steps.
  **Clarification**: Munsell, HSL and OKLCH have different constructions. No fixed family-to-OKLCH-angle table or exact uniformity follows.

# Source Reference

Chapter 3: By T. M. Cleland, p. 4; Chapter 4: I. Hue, pp. 4-6.

# Verification Notes

- This revision reviewed the complete available card body and local relationships/CQ components; it did not inspect the missing original book, prepared Cleland text or diagrams. All historical quotations, dates, page claims, named attributions and source-specific efficacy claims remain unassessed for fidelity.
- Extraction-confidence metadata is preserved from the predecessor. Earlier “exact quote,” “verified planned cards” and “0010 checked” notes described historical extraction/navigation observations, not current independent semantic proof.
- Current technical qualifications use the [RIT renotation overview](https://www.rit.edu/science/munsell-color-science-lab-educational-resources#munsell-renotation-data), [CIE appearance terminology](https://cie.co.at/eilvterm/17-22-067) and [CSS Color4](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/), with elementary conditional algebra where stated. These do not establish historical-source fidelity, exact perceptual equality, physical neutralisation or aesthetic guarantees.
- CSS metadata/body examples are model-specific illustrations, not Munsell conversions, checked contrast pairs or mandatory project palettes. No browser, assistive-technology, disc/material experiment or hosted rendering result was produced.
