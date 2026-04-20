---
concept: Orthogonal Colour Properties
slug: orthogonal-colour-properties
category: colour-theory
subcategory: colour-spaces
tier: intermediate
layer: 2-domain
source: "Okhsv and Okhsl"
source_slug: posts
authors: "Bj\u00f6rn Ottosson"
chapter: "What makes a good color picker?"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - ["independent colour axes", "colour axis independence"]
prerequisites:
  - colour-gamut
  - hsl
  - hsv
extends:
  - colour-picker-design-principles
related:
  - okhsl
  - okhsv
  - chroma-vs-saturation
contrasts_with:
  - []
answers_questions:
  - "What makes a colour picker perceptually well-designed?"
  - "What distinguishes chroma from saturation in a colour space?"
rosetta_stone:
  - domain: mathematics
    concept: "Orthogonal basis vectors in a vector space"
    rating: rigorous
    note: "Perceptual orthogonality in colour is directly analogous to mathematical orthogonality: changing one axis component should produce no component change along other axes, in perceptual space rather than Euclidean space."
---

# Quick Definition

Orthogonal colour properties are the design goal that each axis of a colour space (hue, lightness, chroma, saturation) can be adjusted independently without causing perceived changes to the other axes.

# Core Definition

Ottosson articulates four orthogonality properties: "Orthogonal Lightness \u2014 Hue/Chroma/Saturation can be altered, while keeping perceived Lightness constant"; "Orthogonal Chroma \u2014 Lightness/Hue can be altered, while keeping perceived Chroma constant"; "Orthogonal Saturation \u2014 Lightness/Hue can be altered, while keeping perceived Saturation constant"; and "Orthogonal Hue \u2014 Lightness/Chroma/Saturation can be altered, while keeping perceived Hue constant." These are ideal goals; no existing colour space satisfying a simple geometric shape achieves all four simultaneously. The conflict is fundamental: "independent control of hue, lightness and chroma can not be achieved in a color space that also maps sRGB to a simple geometrical shape."

# Prerequisites

- **Colour gamut** \u2014 The shape of the gamut determines which orthogonalities are geometrically achievable
- **Perceptual colour concepts** \u2014 Requires understanding that hue, lightness, chroma, saturation are perceptual quantities, not purely mathematical ones

# Key Properties

1. Four distinct orthogonality properties: lightness, chroma, saturation, hue
2. Orthogonal Hue is the most achievable \u2014 Oklab-derived spaces (Okhsl, Okhsv) achieve it
3. Orthogonal Lightness requires a perceptually uniform lightness scale, which HSL and HSV lack
4. All four cannot be simultaneously achieved with a simple cylindrical gamut shape

# Construction / Recognition

## To Identify/Recognise:
1. Orthogonal Hue: dragging the saturation slider in HSV causes a purple shift in deep blues \u2014 a violation
2. Orthogonal Lightness: a yellow and a blue with the same HSL Lightness value appear at vastly different brightness \u2014 a violation
3. Orthogonal Chroma: in HSLuv, keeping constant "Saturation" while changing hue causes the perceived chroma to "change drastically and abruptly" \u2014 a violation

# Context & Application

- **Typical contexts**: Colour space design, evaluation of colour pickers, perceptual colour science
- **Common applications**: Understanding why certain colour pickers feel more intuitive; designing colour scales for data visualisation

## Cross-Domain Connections

**Mathematics \u2192 RIGOROUS**: Orthogonality in colour spaces is a direct analogue of orthogonality in linear algebra. In both cases, a change in one axis coordinate produces zero change along other axes. In colour, the axes are perceptual quantities (lightness, hue, chroma); in mathematics they are dimensions of a vector space. The mapping is rigorous in concept, though colour perception is non-linear and dependent on context.

# Examples

**Example 1** (from source): The comparison table shows that only Lab-like colour spaces achieve "yes" for Orthogonal Lightness and Orthogonal Chroma, while HSL achieves "no" for both. Okhsl achieves "yes" for Orthogonal Lightness and Orthogonal Hue \u2014 an improvement over HSL.

**Example 2** (from source): HSV achieves "partial" for Orthogonal Hue and Saturation. The partiality comes from the hue distortion visible in deep blue colours when saturation is reduced.

# Relationships

## Builds Upon
- **Perceptual colour science** \u2014 Orthogonality is defined in perceptual, not numeric, terms

## Enables
- **Okhsl / Okhsv design** \u2014 Both spaces prioritise Orthogonal Hue, with Okhsl additionally achieving Orthogonal Lightness

## Related
- **Colour picker design principles** \u2014 Orthogonality is a subset of the full eight-property framework
- **Chroma vs saturation** \u2014 The distinction matters because Orthogonal Chroma and Orthogonal Saturation are different properties

# Common Errors

- **Error**: Assuming that numerical independence (adjusting one slider parameter) implies perceptual independence.
  **Correction**: In HSL, changing Lightness while keeping H and S constant numerically constant changes the perceived hue in deep blue and purple colours \u2014 numerical independence does not guarantee perceptual orthogonality.

# Common Confusions

- **Confusion**: Orthogonal Saturation and Orthogonal Chroma are the same property.
  **Clarification**: They are distinct properties because saturation and chroma are different quantities. Saturation is relative to the maximum colourfulness possible at the same lightness; chroma is an absolute measure of colourfulness.

# Source Reference

"What makes a good color picker?" section, Okhsv and Okhsl (Bj\u00f6rn Ottosson).

# Verification Notes

- Definition source: Direct quotes from Ottosson's property list
- Confidence rationale: High \u2014 explicitly listed and discussed at length
- Uncertainties: None significant
- Cross-reference status: Verified within Ottosson source
- Rosetta Stone check: Mathematics/orthogonal-basis analogy added as rigorous
- OCR issues: None significant
