---
concept: Natural Colour System (NCS)
slug: natural-colour-system
category: colour-theory
subcategory: colour-ordering-systems
tier: intermediate
layer: 2-domain
source: "Okhsv and Okhsl"
source_slug: posts
authors: "Bj\u00f6rn Ottosson"
chapter: "Color picking before computers"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: medium
aliases:
  - ["NCS", "NCS color system"]
prerequisites:
  - []
extends:
  - []
related:
  - munsell-colour-system
  - colour-picker-design-principles
  - hsv
contrasts_with:
  - munsell-colour-system
  - hsl
  - hsv
answers_questions:
  - "What makes a colour picker perceptually well-designed?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition

The Natural Colour System (NCS) is a Swedish perceptual colour ordering system based on describing colours by their visual similarity to six elementary colours (white, black, yellow, red, green, blue), using a triangular model of whiteness, blackness, and chromaticness.

# Core Definition

Ottosson describes NCS as taking "a different approach" to Munsell: "it is designed to make it easy to describe colors, rather than to match perceptual qualities." NCS "does this by describing colors by their similarity to six primary colors: white, black, yellow, red, green and blue. The yellow, red, green and blue colors are used to determine the hue. The final color is described by a color triangle with the corners white, black and the most saturated color of the given hue. A position in the triangle is described with the parameters whiteness, blackness, chromaticness. Any two of those parameters are sufficient, since they sum to one." Ottosson also notes the structural similarities and differences between NCS and HSV/HWB: "HSV is quite similar to the Natural Color System in its structure and it's possible to transform it to have parameters more similar to NCS, then referred to as hue, whiteness and blackness (HWB)." The key differences are that "NCS is derived based on research into the appearance of colors and does a good job at matching human perception" while "HWB/HSV has a simple construction, not taking research into color appearance into account"; additionally, "NCS has a gamut designed to contain pigments realizable in paint/print" while HWB/HSV is based on an RGB gamut.

# Prerequisites

- None \u2014 NCS is a foundational colour description system

# Key Properties

1. Six elementary colours: white, black, yellow, red, green, blue (not the same as RGB primaries)
2. Any colour is described by its resemblance to these six, expressed as whiteness (w), blackness (s), and chromaticness (c) \u2014 any two of which are sufficient since w + s + c = 1
3. Hue is a circular scale based on similarity to the four chromatic elementaries (Y, R, G, B)
4. Shape is a swept triangle per hue; this is geometrically simple but does not match the sRGB gamut

# Construction / Recognition

## To Identify/Recognise:
1. NCS notation specifies resemblance to elementaries, e.g. NCS S 1050-Y90R means 10% blackness, 50% chromaticness, hue 90% toward Red from Yellow
2. An NCS colour picker shows a triangle with white, black, and chromatic corners and a separate hue circle

# Context & Application

- **Typical contexts**: Architectural colour specification, paint and coatings industry (Scandinavian markets especially), interior design
- **Common applications**: Specifying wall paint colours, surface material specifications, design standards in Scandinavian countries

# Examples

**Example 1** (from source): Ottosson's comparison table shows NCS achieves "partial" for Orthogonal Chroma and "yes" for Orthogonal Hue \u2014 better than HSL/HSV on hue, but its gamut does not match sRGB which limits digital applicability.

**Example 2** (from source): Ottosson shows an NCS colour picker screenshot from the "Colourpin" app as an example of a real-world non-HSL picker.

# Relationships

## Builds Upon
- **Perceptual colour research** \u2014 NCS was derived from experiments on human colour appearance

## Related
- **Munsell colour system** \u2014 Both are perceptual colour ordering systems; NCS uses similarity to elementaries while Munsell uses independent dimensions (Hue, Chroma, Value)
- **HWB colour model** \u2014 HWB (hue, whiteness, blackness) is structurally similar to NCS but based on RGB rather than perception

## Contrasts With
- **Munsell colour system** \u2014 "The Munsell Color System... colors are described with three parameters, designed to match the perceived appearance of colors: Hue, Chroma and Value. The parameters are designed to be independent and each have a uniform scale." NCS uses similarity/resemblance framing rather than independent orthogonal parameters.
- **HSV / HWB** \u2014 NCS is derived from perceptual research; HSV/HWB from a simple RGB transformation

# Common Errors

- **Error**: Treating NCS as equivalent to sRGB/HSV for digital design.
  **Correction**: NCS gamut is based on pigment colours achievable in paint/print, not sRGB. NCS codes cannot be directly converted to sRGB without a mapping table.

# Common Confusions

- **Confusion**: NCS and Munsell use the same underlying model.
  **Clarification**: They are different in principle. Munsell uses independent perceptual dimensions (Hue, Chroma, Value); NCS uses resemblance to six elementary colours (whiteness, blackness, chromaticness, hue). Munsell's parameters are designed to be independent; NCS parameters (w + s + c = 1) are not independent.

# Source Reference

"Color picking before computers" and comparison table, Okhsv and Okhsl (Bj\u00f6rn Ottosson).

# Verification Notes

- Definition source: Direct quotes from Ottosson
- Confidence rationale: Medium \u2014 NCS is described accurately but briefly; no deep technical detail in source
- Uncertainties: Source provides overview only; detailed NCS specifications require primary NCS sources
- Cross-reference status: Not present in Drasner source
- Rosetta Stone check: No mappings added
- OCR issues: None significant
