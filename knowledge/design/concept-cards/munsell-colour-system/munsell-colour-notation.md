---
concept: "Munsell Colour Notation"
slug: "munsell-colour-notation"
category: "colour-theory"
subcategory: "colour-notation"
tier: "intermediate"
layer: "2-domain"
source: "A Practical Description of The Munsell Color System"
source_slug: "munsell-colour-system"
authors: "T. M. Cleland"
chapter: "III. Chroma"
chapter_number: 6
pdf_page: 9
section: null
extraction_confidence: "high"
aliases:
  - "Munsell notation"
  - "HV/C notation"
  - "Munsell colour formula"
  - "colour formula"
prerequisites:
  - "hue"
  - "colour-value"
  - "chroma"
  - "munsell-hue-notation"
extends:
  - "munsell-colour-system"
related:
  - "munsell-colour-solid"
  - "munsell-hue-circle"
  - "neutral-axis"
contrasts_with: []
answers_questions:
  - "CQ 3: What is the difference between hue, saturation/chroma, and lightness/value?"
rosetta_stone:
  -
    domain: "software-engineering"
    concept: "Structured identifier / addressing system"
    rating: "structural"
    note: "H V/C is a structured colour designation, loosely comparable to a coordinate address. This does not identify its semantics with software namespacing or versioning, or make colour conversion and perceptual effects derivable from syntax alone."
css_implementation:
  -
    property: "oklch() function"
    example: "color: oklch(0.5 0.1 240); /* L C H — different order from Munsell H V/C */"
    support: "baseline"
---

# Quick Definition

Munsell H V/C is a structured designation of hue, value and chroma. A complete designation and reference context support colour communication; notation alone does not calculate appearance or conversion.

# Core Definition

The earlier extraction attributes the following wording to Cleland; the book and prepared text are unavailable, so quotations, locators, context and historical attribution remain unverified.

Retained reported wording: "we are given a certain color to measure and define and we find that upon the scale of Hue it is Purple-Blue. Upon comparing it with the scale of Value, we find it is but three steps from the bottom, and that it is only two steps away from the neutral gray pole upon the scale of Chroma. A complete formula for this color would, therefore, be written P-B 3/2" "It is scarcely necessary to point out the practical advantages of such a system of definite measurement and notation over the vague and variable terms in general use, borrowed from the vegetable and animal kingdoms, such as plum, olive, fawn, mouse, etc., of which no two persons ever have quite the same idea"

The recorded PB 3/2 example communicates hue, value and chroma in the source’s abbreviated convention. A more fully qualified designation and reference context are needed for matching/conversion. Syntax alone does not determine appearance, gamut or harmony.

# Prerequisites

- **Hue** — Supplies the relevant H/V/C or diagram vocabulary for this card; this is an understanding route, not a claim of physical or historical derivation.
- **Colour Value** — Supplies the relevant H/V/C or diagram vocabulary for this card; this is an understanding route, not a claim of physical or historical derivation.
- **Chroma** — Supplies the relevant H/V/C or diagram vocabulary for this card; this is an understanding route, not a claim of physical or historical derivation.
- **Munsell Hue Notation** — Supplies the relevant H/V/C or diagram vocabulary for this card; this is an understanding route, not a claim of physical or historical derivation.

# Key Properties

1. Write hue, then value before the slash, chroma after: H V/C.
2. A hue prefix belongs to H, not V or C; qualified notation may include decimal positions.
3. Historical short forms such as PB 3/2 retain the source's reported convention; do not silently infer missing precision.
4. Value is nominally 0–10 and can be sampled at decimals; 1–9 is the recorded practical example.
5. Chroma's realizable range depends on H/V and reference conditions; it is not an unlimited material range.
6. Neutral designations such as N 5/ have no perceptual hue. Syntax alone establishes no harmony or neutralisation.

# Construction / Recognition

## To Construct/Create:

1. Identify the hue against a reference under stated conditions.
2. Determine value and chroma from that reference, retaining any needed decimals.
3. Assemble H V/C and retain the sample/data/condition identity.
4. For CSS use a complete, defined conversion; do not assign OKLCH L=V/10 or a hue-family angle.

## To Identify/Recognise:

1. Separate the hue prefix from the value/chroma pair.
2. Recognize incomplete historical fragments such as B6/ without pretending they specify chroma.
3. Distinguish a neutral N designation from a chromatic hue label.

# Context & Application

Use structured designations for reference matching and communication. Conversion to a digital space needs full data and conditions. The CSS metadata illustrates parameter order only; it supplies no Munsell conversion, accessibility result or prescribed palette.

## Cross-Domain Connections

**Engineering → Structural analogy**: H V/C resembles a coordinate address because it has named fields. Namespacing and semantic versioning have different semantics. A structured string cannot by itself derive colour distances, physical mixture or perceptual results.

# Examples

Recorded extraction examples below retain their reported locators; they were not checked against the missing book. Any balance or harmony result is historical advice or conditional arithmetic, not an independently observed mixing or aesthetic result.

**Example 1** (p. 9): "P-B 3/2" — Purple-Blue at Value 3 (dark), Chroma 2 (weak, near gray).

**Example 2** (p. 6): "B6/" — blue at value 6, chroma not yet specified.

**Example 3** (p. 12): "R5/5 will balance B-G 5/5" — demonstrating how the notation supports balance calculations.

## Worked Example

Read the recorded **PB 3/2** example as Purple-Blue, value 3 and chroma 2.
The prefix-free PB is the reported historical shorthand. If an actual reference
match is at position 5PB, specify **5PB 3/2** rather than silently assuming the
missing prefix. Retain the reference and viewing conditions; this notation
exercise is not a measurement or CSS conversion.

# Relationships

## Builds Upon

- **Hue**, **Colour Value**, **Chroma** — These supply H,V,C semantics; coordinate distinction does not ensure unrestricted realizability.
- **Munsell Hue Notation** — The prefix/family convention supplies H, separate from the value number.
- **Munsell Colour System** — H V/C is a notation for system coordinates, not a theorem of colour geometry.

## Enables

- **Colour Balance** — The recorded balance exercise consumes positive C,V values; notation alone warrants no harmony.
- **Munsell Balance Formula** — The equation extracts C,V; its inverse-product domain excludes zero inputs.

## Related

- **Munsell Colour Solid** — The designation refers to system positions under a specified reference, not every abstract point.
- **Neutral Axis** — Neutral notation N V/ records no hue; its historical source attribution is still unavailable.

## Contrasts With

No additional card-local bullet is recorded here. This is navigation scope, not a verified absence or a historical-source completeness result.

# Common Errors

- **Error**: Writing H C/V or confusing a hue prefix with V.
  **Correction**: Keep H and its prefix separate; value precedes the slash and chroma follows it.
- **Error**: Treating a valid formula as proof of realizability or exact digital colour.
  **Correction**: Inspect reference data, conditions and destination gamut.

# Common Confusions

- **Confusion**: A higher chroma guarantees a stronger or better experience regardless of context.
  **Clarification**: Chroma is model/reference-dependent. Historical pigment maxima do not rank all hues or guarantee displayability, contrast or suitability.

# Source Reference

Chapters 4-6: I. Hue, II. Value, III. Chroma, pp. 4-9.

# Verification Notes

- This revision reviewed the complete available card body and local relationships/CQ components; it did not inspect the missing original book, prepared Cleland text or diagrams. All historical quotations, dates, page claims, named attributions and source-specific efficacy claims remain unassessed for fidelity.
- Extraction-confidence metadata is preserved from the predecessor. Earlier “exact quote,” “verified planned cards” and “0010 checked” notes described historical extraction/navigation observations, not current independent semantic proof.
- Current technical qualifications use the [RIT renotation overview](https://www.rit.edu/science/munsell-color-science-lab-educational-resources#munsell-renotation-data), [CIE appearance terminology](https://cie.co.at/eilvterm/17-22-067) and [CSS Color4](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/), with elementary conditional algebra where stated. These do not establish historical-source fidelity, exact perceptual equality, physical neutralisation or aesthetic guarantees.
- CSS metadata/body examples are model-specific illustrations, not Munsell conversions, checked contrast pairs or mandatory project palettes. No browser, assistive-technology, disc/material experiment or hosted rendering result was produced.
