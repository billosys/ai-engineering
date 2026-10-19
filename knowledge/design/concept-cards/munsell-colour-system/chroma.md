---
concept: "Chroma"
slug: "chroma"
category: "colour-theory"
subcategory: "colour-properties"
tier: "foundational"
layer: "2-domain"
source: "A Practical Description of The Munsell Color System"
source_slug: "munsell-colour-system"
authors: "T. M. Cleland"
chapter: "III. Chroma"
chapter_number: 6
pdf_page: 7
section: "III. Chroma"
extraction_confidence: "high"
aliases:
  - "colour strength"
  - "saturation"
  - "purity"
  - "Munsell chroma"
prerequisites: []
extends: []
related:
  - "munsell-colour-system"
  - "hue"
  - "colour-value"
  - "neutral-axis"
contrasts_with:
  - "hue"
  - "colour-value"
answers_questions:
  - "CQ 3: What is the difference between hue, saturation/chroma, and lightness/value?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Radial coordinate in cylindrical space"
    rating: "rigorous"
    note: "Chroma is drawn radially from a neutral axis in the Munsell diagram. Abstract nonnegative coordinates do not imply unlimited realizable surface colours: available chroma depends on hue, value, reference conditions and material or destination gamut."
css_implementation:
  -
    property: "oklch() chroma channel"
    example: "color: oklch(0.7 0.15 240); /* C = 0.15 */"
    support: "baseline"
  -
    property: "hsl() saturation channel"
    example: "color: hsl(240, 50%, 50%); /* S = 50% (not directly comparable) */"
    support: "baseline"
---

# Quick Definition

Chroma describes colour departure from an achromatic reference under specified conditions. Munsell chroma is the H/V/C system’s radial coordinate; it differs from saturation and from OKLCH C.

# Core Definition

The earlier extraction attributes the following wording to Cleland; the book and prepared text are unavailable, so quotations, locators, context and historical attribution remain unverified.

Retained reported wording: "Both may be green and of the same Value of light, but the emerald is strong in color and the grape is weak in color or grayer. It is this difference which is measured on the dimension of Chroma" "if we imagine any one of these hues on the circumference of the band to grow inward toward the gray pole in the center, growing grayer or weaker in color strength until it reaches this center pole and loses its color entirely, we have grasped the idea of the dimension known as Chroma" "/5, /8, /9, etc."

Munsell chroma is drawn as departure from neutral at a specified hue/value. Realizable extent is reference/material/gamut dependent. Chroma, saturation and CSS channels require their own definitions; historic pigment examples do not establish universal maxima.

Further recorded extraction wording (unverified attribution/context; these are not adopted universal claims):

- "at right angles to the vertical pole" (p. 7)
- "limited only by the strength of pigments" (p. 9)
- "Colors differ by nature in their Chroma Strength, some being much more powerful than others. The strongest red pigment... is twice as powerful as the strongest blue-green pigment" (p. 8)
- "All colors do not reach their maximum Chroma Strength at the same level of Value" (p. 8)
- "We may say of an emerald that it is green and that it is light, but... there is a decided difference" (p. 7)

# Prerequisites

No card-local prerequisite is recorded in the preserved metadata. This is an editorial starting point, not proof that the concept has no dependencies in the wider domain.

# Key Properties

1. In the diagram C=0 is neutral and hue is undefined there.
2. Chroma is drawn radially at a chosen hue/value; this does not establish Euclidean perceptual distance.
3. There is no single fixed maximum for all hues and values; realizable chroma depends on reference conditions, material and gamut.
4. Red /10 versus BG /5 is a recorded pigment example, not an all-time physical limit.
5. Distinct H/V/C coordinates do not guarantee unrestricted independence in realizable colours or perceived appearance.
6. CIE chroma and saturation use different reference judgments; HSL saturation and OKLCH C have separate model definitions.

# Construction / Recognition

## To Construct/Create:

1. Choose a reference hue/value and viewing context.
2. Compare with the achromatic reference at that level.
3. Use the reference system's calibration to assign chroma; do not measure arbitrary diagram length as physical colourfulness.
4. Check any resulting digital candidate against its destination gamut.

## To Identify/Recognise:

1. Identify which model or appearance definition is meant by chroma.
2. Compare muted/vivid variation without assuming that darkness is chroma.
3. Distinguish the coordinate value from a device/material maximum.

# Context & Application

Chroma helps describe and vary candidates. Low chroma alone does not make a background safe or legible; complete rendered foreground/background pairs and states need checks. A Munsell chroma number cannot be placed directly into CSS OKLCH C.

## Cross-Domain Connections

**Mathematics → Diagram geometry**: Chroma is radial in the stipulated cylindrical diagram. Nonnegative abstract radii do not imply infinite realizable surface colours. Available chroma varies with hue/value and conditions.

# Examples

Recorded extraction examples below retain their reported locators; they were not checked against the missing book. Any balance or harmony result is historical advice or conditional arithmetic, not an independently observed mixing or aesthetic result.

**Example 1** (p. 7): The emerald vs. grape comparison — "Both may be green and of the same Value of light, but the emerald is strong in color and the grape is weak in color or grayer."

**Example 2** (p. 8): "The strongest red pigment used, for example, is twice as powerful as the strongest blue-green pigment and will require a correspondingly greater number of steps on a longer path to reach gray. The Chroma path of Red is the longest... being ten measured steps from the neutral pole; while Blue-Green is the shortest, being only five steps."

**Example 3** (p. 9): In the colour formula PB 3/2, the "/2" indicates chroma 2 — only two steps from neutral gray, a weak, grayish purple-blue.

# Relationships

## Builds Upon

No additional card-local bullet is recorded here. This is navigation scope, not a verified absence or a historical-source completeness result.

## Enables

- **Munsell Colour Notation** — Chroma supplies C in H V/C, with reference-specific calibration.
- **Munsell Colour Solid** — Chroma supplies the radial diagram coordinate and contributes to the gamut boundary.
- **Colour Balance** — The historical model uses positive C,V to compute inverse areas; no general visual-weight law follows.
- **Munsell Balance Formula** — A∝1/(C×V) is a conditional positive-input approximation, not neutral-background division.

## Related

- **Munsell Colour System** — Chroma is one of the named coordinates, not a universal absolute colourfulness amount.
- **Neutral Axis** — Neutral supplies the radial origin at each value, where hue is undefined.
- **Hue** — Hue and chroma describe distinct attributes, without unrestricted independent realizability.
- **Colour Value** — Value and chroma describe distinct attributes, both subject to model/reference/gamut conditions.

## Contrasts With

- **Hue** — Hue identifies colour character; chroma concerns departure from a neutral reference.
- **Colour Value** — Value concerns light/dark character; chroma concerns departure from neutral.

# Common Errors

- **Error**: Assuming maximum chroma is always best or inevitably creates imbalance.
  **Correction**: Evaluate the actual task, roles, gamut and pairs. The historical inverse-product model is a conditional heuristic, not a general visual-weight law.

# Common Confusions

- **Confusion**: Chroma and saturation are synonyms or universal C/L ratios.
  **Clarification**: CIE chroma relates colourfulness to an achromatic reference; saturation to the area's own brightness. Munsell C, OKLCH C and HSL/HSV saturation are model-specific.
- **Confusion**: Low chroma means dark.
  **Clarification**: Near-neutral colours can be light or dark; admissible chroma at each value still depends on the reference/gamut.

# Source Reference

Chapter 3: By T. M. Cleland, p. 4 (introduction). Chapter 6: III. Chroma, pp. 7-9.

# Verification Notes

- This revision reviewed the complete available card body and local relationships/CQ components; it did not inspect the missing original book, prepared Cleland text or diagrams. All historical quotations, dates, page claims, named attributions and source-specific efficacy claims remain unassessed for fidelity.
- Extraction-confidence metadata is preserved from the predecessor. Earlier “exact quote,” “verified planned cards” and “0010 checked” notes described historical extraction/navigation observations, not current independent semantic proof.
- Current technical qualifications use the [RIT renotation overview](https://www.rit.edu/science/munsell-color-science-lab-educational-resources#munsell-renotation-data), [CIE appearance terminology](https://cie.co.at/eilvterm/17-22-067) and [CSS Color4](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/), with elementary conditional algebra where stated. These do not establish historical-source fidelity, exact perceptual equality, physical neutralisation or aesthetic guarantees.
- CSS metadata/body examples are model-specific illustrations, not Munsell conversions, checked contrast pairs or mandatory project palettes. No browser, assistive-technology, disc/material experiment or hosted rendering result was produced.
