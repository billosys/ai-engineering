---
concept: "Triadic Colour Balance"
slug: "triadic-colour-balance"
category: "colour-theory"
subcategory: "colour-harmony"
tier: "advanced"
layer: "2-domain"
source: "A Practical Description of The Munsell Color System"
source_slug: "munsell-colour-system"
authors: "T. M. Cleland"
chapter: "Color Combinations"
chapter_number: 9
pdf_page: 15
section: null
extraction_confidence: "high"
aliases:
  - "three-colour balance"
  - "triadic harmony"
  - "split-complement balance"
prerequisites:
  - "complementary-colours"
  - "colour-balance"
  - "munsell-balance-formula"
extends:
  - "colour-balance"
  - "complementary-harmony"
related:
  - "colour-harmony-as-order"
  - "munsell-colour-solid"
contrasts_with: []
answers_questions:
  - "CQ 30: A dashboard uses teal header, red error badges, green success indicators, blue links, yellow warning banners, and purple notification badges. It looks like a 'clown car.' What principle was violated, and how do you fix it?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Historical complement-splitting heuristic"
    rating: "loose"
    note: "The recorded complement-splitting example suggests a loose allocation analogy. Hue names are not orthogonal vectors, and adding scalar areas or C*V weights does not establish physical colour mixing or neutral cancellation; a specific mixture model would be needed."
css_implementation: []
---

# Quick Definition

This recorded three-colour heuristic splits one member of a complementary pair into two named hues and shares its area allocation. The arithmetic can be inspected; hue-name splitting does not establish physical mixing or neutral cancellation.

# Core Definition

The earlier extraction attributes the following wording to Cleland; the book and prepared text are unavailable, so quotations, locators, context and historical attribution remain unverified.

Retained reported wording: "The principle governing the Balance of opposite colors will also apply to combinations of three colors. Let us assume that Blue is required as one of the colors in a three-color combination. We find that its opposite Hue is Yellow-Red, and as this is merely an admixture of Yellow and Red, it follows logically that the use of these two Hues, with due regard to proportion of areas or strength of Chroma, will yield a perfect color Balance" "we may proceed exactly as in the case of a two-color combination of Blue and Yellow-Red; but in this case we would divide the amount or strength of a correct Yellow-Red between our Yellow and our Red"

The reported method shares a complement’s scalar area allocation between two named hues. Its 42:10:10 arithmetic can be retained conditionally. Hue-name decomposition is not an orthogonal vector decomposition or a specified physical mixture, and no universal cancellation follows.

Further recorded extraction wording (unverified attribution/context; these are not adopted universal claims):

- "the same rule would apply to three or any other number of colors" (p. 14)

# Prerequisites

- **Complementary Colours** — Supplies the relevant H/V/C or diagram vocabulary for this card; this is an understanding route, not a claim of physical or historical derivation.
- **Colour Balance** — Supplies the stipulated positive-input historical model for the conditional arithmetic; it does not establish a mixing or harmony law.
- **Munsell Balance Formula** — Supplies the stipulated positive-input historical model for the conditional arithmetic; it does not establish a mixing or harmony law.

# Key Properties

1. This is the reported complement-splitting method, not necessarily an equilateral 120° triad.
2. Dividing an allocated scalar area preserves its sum, not a colour mixture vector.
3. Hue names such as Yellow-Red are not orthogonal vector components or pigment recipes.
4. The recorded 42:10:10 example is conditional bookkeeping; it is not a general multi-colour balance law.
5. No particular third hue, hue count or area split guarantees harmony, contrast or accessible category distinction.

# Construction / Recognition

## To Construct/Create:

1. Adopt the historical positive-C, positive-V two-colour approximation for an explicit exercise only.
2. Blue 4/5 has product 20; Yellow-Red 6/7 has product 42, giving areas 42:20.
3. Share the 20 allocated parts as 10 Yellow 6/7 and 10 Red 6/7 to reproduce the recorded 42:10:10 arithmetic.
4. 42×20=840 and 10×42+10×42=840. This scalar equality does not prove that the substituted colours mix like Yellow-Red or neutralise Blue.
5. For actual palettes return to roles, gamut and pair/state checks; no generic three-colour prescription follows.

## To Identify/Recognise:

1. Distinguish a split-complement example from equally spaced hue-angle selection.
2. Check the area allocation and model assumptions separately from mixture or aesthetic claims.
3. Do not diagnose a multi-hue dashboard solely by the number of hues.

# Context & Application

For CQ30 the example can explain conditional area accounting, not identify an automatic dashboard error or fix. Assess meaning/role coherence, hierarchy, pair/state contrast and redundant signals; many hues can be justified by the task.

## Cross-Domain Connections

**Mathematics → Loose allocation analogy**: Splitting 20 into 10+10 preserves a scalar total. It is not orthogonal vector decomposition and provides no specified physical mixture coordinates. The reported example remains historical, not experimental verification.

# Examples

Recorded extraction examples below retain their reported locators; they were not checked against the missing book. Any balance or harmony result is historical advice or conditional arithmetic, not an independently observed mixing or aesthetic result.

**Example 1** (pp. 15-16): Blue 4/5 with Yellow 6/7 and Red 6/7:
- Blue weight: 4 × 5 = 20 → 42 parts area.
- Yellow-Red weight: 6 × 7 = 42 → 20 parts area total.
- "If we would use 20 parts of Yellow-Red, 6/7, it naturally follows that we would use 10 parts of Red 6/7 and 10 parts of Yellow 6/7 to effect the same Balance."

# Relationships

## Builds Upon

- **Colour Balance** — The recorded split shares an area allocation, with no general multi-colour balance proof.
- **Complementary Harmony** — The method starts with a reported opposed pair, then substitutes named hues conditionally.
- **Munsell Balance Formula** — The formula supplies the initial positive-input scalar products; hue-name splitting is an additional unverified model step.

## Enables

- **Colour Harmony as Order** — The example can be described as an organized selection, not a demonstrated harmony theorem.

## Related

- **Munsell Colour Solid** — The diagram locates hues/values/chromas; scalar area sums are not physical mixture vectors.

## Contrasts With

No additional card-local bullet is recorded here. This is navigation scope, not a verified absence or a historical-source completeness result.

# Common Errors

- **Error**: Giving each replacement the whole 20-part allocation when reproducing the recorded exercise.
  **Correction**: Sharing it as 10+10 preserves the stipulated total; doubling it changes that arithmetic.
- **Error**: Requiring every third colour to derive from a complement.
  **Correction**: This is one named historical method. Other candidates can be appropriate; check the actual task.

# Common Confusions

- **Confusion**: Every triad has to use 120° spacing or the example proves neutral mixing.
  **Clarification**: This method uses a reported split complement. Neither the name nor equal scalar weights proves physical cancellation or harmony.

# Source Reference

Chapter 9: Color Combinations, pp. 15-16.

# Verification Notes

- This revision reviewed the complete available card body and local relationships/CQ components; it did not inspect the missing original book, prepared Cleland text or diagrams. All historical quotations, dates, page claims, named attributions and source-specific efficacy claims remain unassessed for fidelity.
- Extraction-confidence metadata is preserved from the predecessor. Earlier “exact quote,” “verified planned cards” and “0010 checked” notes described historical extraction/navigation observations, not current independent semantic proof.
- Current technical qualifications use the [RIT renotation overview](https://www.rit.edu/science/munsell-color-science-lab-educational-resources#munsell-renotation-data), [CIE appearance terminology](https://cie.co.at/eilvterm/17-22-067) and [CSS Color4](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/), with elementary conditional algebra where stated. These do not establish historical-source fidelity, exact perceptual equality, physical neutralisation or aesthetic guarantees.
- CSS metadata/body examples are model-specific illustrations, not Munsell conversions, checked contrast pairs or mandatory project palettes. No browser, assistive-technology, disc/material experiment or hosted rendering result was produced.
