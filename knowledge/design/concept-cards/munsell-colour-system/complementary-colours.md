---
concept: "Complementary Colours"
slug: "complementary-colours"
category: "colour-theory"
subcategory: "colour-relationships"
tier: "foundational"
layer: "2-domain"
source: "A Practical Description of The Munsell Color System"
source_slug: "munsell-colour-system"
authors: "T. M. Cleland"
chapter: "Opposite or Complementary Colors"
chapter_number: 7
pdf_page: 10
section: null
extraction_confidence: "high"
aliases:
  - "opposite colours"
  - "complementary colors"
  - "opposite hues"
prerequisites:
  - "hue"
  - "munsell-hue-circle"
extends: []
related:
  - "munsell-colour-system"
  - "neutral-axis"
  - "colour-balance"
  - "complementary-harmony"
contrasts_with:
  - "analogous-harmony"
answers_questions:
  - "CQ 3: What is the difference between hue, saturation/chroma, and lightness/value?"
rosetta_stone:
  -
    domain: "music"
    concept: "Tritone / consonance-dissonance"
    rating: "loose"
    note: "Opposition in a chosen colour diagram can be loosely compared with musical tension. Neither maximum visual contrast, a universal tritone tension ranking, neutral mixing, nor aesthetic success follows from that analogy; the media and perceptual tasks differ."
css_implementation:
  -
    property: "oklch() relative colour syntax"
    example: "color: oklch(from var(--base) l c calc(h + 180)); /* CSS hue-offset candidate; not Munsell conversion or a contrast guarantee */"
    support: "partial"
---

# Quick Definition

Here complementary colours means opposed hue positions in the chosen Munsell diagram. Recorded neutral-disc and strongest-contrast claims need their own conditions and evidence; opposition alone establishes neither.

# Core Definition

The earlier extraction attributes the following wording to Cleland; the book and prepared text are unavailable, so quotations, locators, context and historical attribution remain unverified.

Retained reported wording: "each Hue on the circle will be found directly opposite to another Hue. Thus a straight line drawn from Red on the circle of Hues through the neutral pole will pass through Blue-Green, its opposite or complementary color" "opposite" "because it is simple and is self-explanatory" "When any two colors are truly opposite or at the point of strongest contrast, their admixture will produce a perfectly neutral gray" "arranging two opposite colors on a disc in proportions relative to the Chroma strength of each and revolving them with such rapidity that we cannot see them separately and they are mixed, when if they are truly opposite, they will unite in a perfect gray" "each of the Principal Hues, Red, Purple, Blue, Green and Yellow falls opposite an Intermediate Hue, Blue-Green, Green-Yellow, Yellow-Red, etc."

Diagram opposition identifies reported hue pairs, including R↔BG. Recorded disc averaging is a distinct operation from material mixing, linear-light averaging and encoded/OKLCH CSS interpolation. None follows simply from a diagram diameter.

Further recorded extraction wording (unverified attribution/context; these are not adopted universal claims):

- "Two colors which are thus opposite to one another are... in actual use the most strongly contrasting" (p. 10)
- "It does not matter at what point we draw the line, whether it is from one of the regular Hues or from a point between two Hues, if it passes through the center it will fall upon the Hue... which is its strongest contrast" (p. 10)
- "tend to stimulate and enhance each other" (p. 15)

# Prerequisites

- **Hue** — Supplies the relevant H/V/C or diagram vocabulary for this card; this is an understanding route, not a claim of physical or historical derivation.
- **Munsell Hue Circle** — Supplies the relevant H/V/C or diagram vocabulary for this card; this is an understanding route, not a claim of physical or historical derivation.

# Key Properties

1. A line through the diagram's neutral centre identifies opposite hue positions.
2. Recorded family pairs are R↔BG, Y↔PB, G↔RP, B↔YR and P↔GY; R↔G is not this diagram's pair.
3. An abstract half-turn can represent opposition, but hue labels are not raw residues or CSS angles.
4. Temporal Maxwell-disc averaging differs from material mixing and from CSS interpolation in encoded, linear-light or OKLCH coordinates.
5. Diagram opposition guarantees no maximum usable contrast, WCAG ratio, neutral mixture or aesthetic enhancement.
6. Non-opposite diagram lines are geometric illustrations, not universal mixture predictions.

# Construction / Recognition

## To Construct/Create:

1. Choose and name the colour-order diagram.
2. Locate a hue and the opposed position, retaining full V/C and conditions for actual colours.
3. If using an explicit 0…99 index, compute h+50 modulo 100 as diagram arithmetic only.
4. Test any claimed mixture or rendered contrast using the actual model/task.

## To Identify/Recognise:

1. Identify opposed positions in a named diagram, rather than any visually contrasting pair.
2. Keep a measured disc or material-mixture result distinct from drawing a diameter.
3. In CSS, +180° creates an angle-offset candidate in that CSS space, not a Munsell conversion or contrast pass.

# Context & Application

Opposed selections are candidates for exploration. Preserve the supplied brand/role context and check gamut and complete rendered state pairs. Hue opposition alone cannot establish call-to-action visibility, category distinction or colour-accessible use.

## Cross-Domain Connections

**Music → Loose**: Diagram opposition can evoke musical tension. A universal tritone tension maximum and a common colour/music mechanism are not established. Circular indexing similarities do not transfer neutral mixing, harmony or perceptual laws.

# Examples

Recorded extraction examples below retain their reported locators; they were not checked against the missing book. Any balance or harmony result is historical advice or conditional arithmetic, not an independently observed mixing or aesthetic result.

**Example 1** (p. 10): "A straight line drawn from Red on the circle of Hues through the neutral pole will pass through Blue-Green, its opposite or complementary color."

**Example 2** (p. 10): "A line from Blue through the neutral pole will pass through Yellow-Red."

**Example 3** (pp. 10-11): Non-opposite mixing — "three different lines have been drawn, no one of them through the neutral center. These lines... cross points which are not neutral, but nearer to one or another of the Hues lying between."

# Relationships

## Builds Upon

- **Hue** — Hue supplies the perceptual attribute whose diagram positions are opposed.
- **Munsell Hue Circle** — The chosen circle defines opposed positions; family labels are not CSS angles.

## Enables

- **Colour Balance** — The balance exercise uses selected opposed pairs and positive C,V as a historical approximation.
- **Complementary Harmony** — The named method explores opposed hues without guaranteed harmony or maximum usable contrast.
- **Triadic Colour Balance** — The reported split example starts from opposition, but hue-name splitting is not physical decomposition.

## Related

- **Neutral Axis** — A diagram diameter crosses the neutral centre; it does not prove mixture neutrality.
- **Munsell Colour System** — Opposition is one relation in the system’s hue ordering.

## Contrasts With

- **Analogous Harmony** — Adjacent versus opposed hue choices distinguish strategies, not a universal contrast ranking.

# Common Errors

- **Error**: Giving Red C10 twice the BG C5 area in the equal-V inverse-chroma exercise.
  **Correction**: Red:BG is 1:2 within that model, with positive inputs. This is arithmetic, not verified mixing.

# Common Confusions

- **Confusion**: Any contrast pair is complementary or red↔green is Munsell opposition.
  **Clarification**: Name the diagram: its reported Red partner is Blue-Green. Contrast and physical mixture require separate criteria.
- **Confusion**: Complements inevitably clash or enhance one another.
  **Clarification**: Both are contextual judgments. The recorded enhancement claim is unverified here and is no guarantee of suitability.

# Source Reference

Chapter 7: Opposite or Complementary Colors, pp. 10-11.

# Verification Notes

- This revision reviewed the complete available card body and local relationships/CQ components; it did not inspect the missing original book, prepared Cleland text or diagrams. All historical quotations, dates, page claims, named attributions and source-specific efficacy claims remain unassessed for fidelity.
- Extraction-confidence metadata is preserved from the predecessor. Earlier “exact quote,” “verified planned cards” and “0010 checked” notes described historical extraction/navigation observations, not current independent semantic proof.
- Current technical qualifications use the [RIT renotation overview](https://www.rit.edu/science/munsell-color-science-lab-educational-resources#munsell-renotation-data), [CIE appearance terminology](https://cie.co.at/eilvterm/17-22-067) and [CSS Color4](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/), with elementary conditional algebra where stated. These do not establish historical-source fidelity, exact perceptual equality, physical neutralisation or aesthetic guarantees.
- CSS metadata/body examples are model-specific illustrations, not Munsell conversions, checked contrast pairs or mandatory project palettes. No browser, assistive-technology, disc/material experiment or hosted rendering result was produced.
