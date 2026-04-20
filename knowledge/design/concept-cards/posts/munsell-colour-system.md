---
concept: Munsell Colour System
slug: munsell-colour-system
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
  - ["Munsell", "Munsell color model"]
prerequisites:
  - []
extends:
  - []
related:
  - natural-colour-system
  - hsl
  - okhsl
contrasts_with:
  - natural-colour-system
answers_questions:
  - "What makes a colour picker perceptually well-designed?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition

The Munsell Colour System is a perceptual colour ordering system developed in the early 20th century that describes colours by three independent dimensions \u2014 Hue, Chroma, and Value \u2014 each with a uniform perceptual scale, resulting in an irregular colour solid.

# Core Definition

Ottosson describes the Munsell system as one of "two important color systems" that "emerged" during the 20th century, both "based on human perception and derived using experiments." "In the Munsell color system, colors are described with three parameters, designed to match the perceived appearance of colors: Hue, Chroma and Value. The parameters are designed to be independent and each have a uniform scale. This results in a color solid with an irregular shape." Drasner notes in Working With Colors Guide that the HSL system "is based on a Munsell color system (he was the first to separate out color into these three channels, or create a three dimensional system based on mathematical principles tied to actual human vision)." Ottosson further notes that "Modern color spaces and models, such as CIELab, Cam16 and my own Oklab, are very similar in their construction" to Munsell.

# Prerequisites

- None \u2014 Munsell is a foundational historical system

# Key Properties

1. Three independent dimensions: Hue (10 principal hues in a circle), Value (0=black to 10=white), Chroma (0=neutral to ~20 for strongest colours)
2. Perceptually uniform scales \u2014 equal numerical steps correspond to equal perceived colour differences
3. Irregular shape \u2014 the gamut boundary is non-cylindrical because maximum chroma varies across hues and values
4. Predecessor to modern perceptual colour spaces (CIELab, Oklab)

# Construction / Recognition

## To Identify/Recognise:
1. Munsell notation: H V/C \u2014 e.g. 5R 5/10 means Hue=5R (red), Value=5, Chroma=10
2. The Munsell colour tree image shows the irregular, uneven solid that results from perceptually uniform spacing

# Context & Application

- **Typical contexts**: Colour science education, paint industry colour specification (especially US), historical reference for modern perceptual colour spaces
- **Common applications**: Soil colour classification (Munsell soil colour charts), artistic colour education, foundational reference in colour science

# Examples

**Example 1** (from source): Ottosson includes the Munsell colour tree photo and notes the irregular shape \u2014 "a color solid with an irregular shape" \u2014 as a consequence of perceptual uniformity. This irregular shape is the same problem that makes Lab-like colour spaces difficult to use in colour pickers.

**Example 2** (from source \u2014 Drasner): "hsl values work with hue, saturation, lightness values. This system is based on a Munsell color system (he was the first to separate out color into these three channels, or create a three dimensional system based on mathematical principles tied to actual human vision)."

# Relationships

## Builds Upon
- **Perceptual colour research** \u2014 Munsell derived dimensions from perceptual experiments

## Enables
- **CIELab, Oklab** \u2014 Modern perceptual spaces directly continue Munsell's approach with more rigorous mathematical grounding
- **HSL** \u2014 Drasner notes HSL's three-channel structure traces to Munsell's conceptual framework

## Related
- **Natural Colour System (NCS)** \u2014 A contemporary perceptual system using different principles
- **Oklab** \u2014 Ottosson's own colour space, which follows "very similar construction" to Munsell

## Contrasts With
- **NCS** \u2014 Munsell uses independent dimensions; NCS uses resemblance to elementary colours
- **HSL/HSV** \u2014 These are simple RGB transformations, not perceptually uniform in the way Munsell is

# Common Confusions

- **Confusion**: Munsell Chroma and HSL Saturation are equivalent.
  **Clarification**: They are not. Munsell Chroma is an independent, absolute perceptual quantity. HSL "Saturation" is a relative quantity (relative chroma at fixed lightness), and is not perceptually uniform.

# Source Reference

"Color picking before computers" section, Okhsv and Okhsl (Bj\u00f6rn Ottosson); "HSL Values" section, Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Definition source: Direct quotes from both sources
- Confidence rationale: Medium \u2014 both sources reference Munsell briefly; detailed technical content requires separate Munsell-specific sources
- Uncertainties: This card is a cross-reference; deeper content is expected to exist in a dedicated munsell-colour-system source
- Cross-reference status: Verified in both sources; abbreviated by instruction
- Rosetta Stone check: No mappings added
- OCR issues: None significant
