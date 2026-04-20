---
concept: Colour Gamut
slug: colour-gamut
category: colour-theory
subcategory: colour-spaces
tier: foundational
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
  - ["gamut", "color gamut", "sRGB gamut"]
prerequisites:
  - []
extends:
  - []
related:
  - hsl
  - hsv
  - okhsl
  - okhsv
contrasts_with:
  - []
answers_questions:
  - "What makes a colour picker perceptually well-designed?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition

A colour gamut is the complete set of colours that a colour system, device, or model can reproduce or represent; in the context of colour pickers and CSS, the sRGB gamut is the standard target.

# Core Definition

Ottosson defines the focus of colour picker design as "picking colors in the sRGB gamut." The gamut is the boundary of representable colours within a given colour space. Its shape in perceptual colour spaces is highly irregular \u2014 Ottosson illustrates this with slices of the sRGB gamut in Oklab, showing that for a constant blue hue the gamut cross-section is triangular and asymmetric, and for yellow it differs substantially. This irregular shape is the central difficulty in designing colour pickers: "The sRGB gamut has a quite irregular shape in these color spaces. As a result, changing one parameter, such as hue, can easily create a color outside the target gamut." The design goal of "Simple Geometrical Shape" in colour picker design means fitting the gamut into a cylinder or other shape that lets parameters be altered independently without leaving the gamut.

# Prerequisites

- None \u2014 gamut is a foundational concept

# Key Properties

1. The sRGB gamut is the subset of all colours reproducible by the sRGB standard (covering most monitors as of the source's writing)
2. In perceptual colour spaces (Oklab, CIELab), the sRGB gamut has an irregular, hue-dependent shape
3. In HSL and HSV, the sRGB gamut is mapped to a cylinder \u2014 a simplification that sacrifices perceptual accuracy for usability
4. Wide gamut displays extend beyond sRGB; Ottosson notes wide-gamut and HDR colour picking as an important area for future research

# Construction / Recognition

## To Identify/Recognise:
1. An out-of-gamut colour is one that cannot be displayed on the target device; in CSS it is typically clamped to the nearest in-gamut value
2. The boundary of the sRGB gamut in an HSV picker is the outer edges of the picker widget \u2014 the entire widget surface is in-gamut by construction
3. In a perceptual colour space (CIELab), the gamut boundary is irregular and must be calculated per hue

# Context & Application

- **Typical contexts**: Colour space design, colour picker implementation, gamut mapping in print/digital conversion, CSS Color 4 `color()` function
- **Common applications**: Determining which colours are safe to use on screen; clipping or mapping colours when converting between gamuts

# Examples

**Example 1** (from source): Ottosson shows that the sRGB gamut plotted in Oklab coordinates with L_r on the Y-axis and chroma on the X-axis produces triangular cross-sections that differ substantially by hue (yellow versus blue versus magenta). This is the problem that Okhsv and Okhsl are designed to solve.

**Example 2** (from source): "Several color pickers have been made using either CIELab or more modern lab-like color spaces... it is also common to see CIELab based color pickers showing colors outside the target gamut and often they are mapped back by simply clamping individual RGB components. This creates severe distortions in hue, lightness and chroma."

# Relationships

## Builds Upon
- **RGB colour model** \u2014 sRGB is the reference standard that defines the gamut

## Enables
- **Colour picker design** \u2014 The gamut shape determines the complexity of picker design
- **Okhsl / Okhsv** \u2014 Both spaces are designed to map the sRGB gamut to a cylinder

## Related
- **Colour spaces** \u2014 Each colour space represents the gamut differently

# Common Errors

- **Error**: Assuming that a colour specified in HSL is always displayable.
  **Correction**: It is, by construction \u2014 HSL maps the sRGB gamut to a cylinder, so all HSL values within [0, 360] \u00d7 [0%, 100%] \u00d7 [0%, 100%] are in-gamut. However, when using wider gamut or perceptual colour spaces, out-of-gamut values are common.

# Common Confusions

- **Confusion**: Gamut and colour space are synonymous.
  **Clarification**: A colour space defines a coordinate system; the gamut is the subset of colours representable in a given context (device, standard). The sRGB gamut is a bounded volume within larger colour spaces.

# Source Reference

"What makes a good color picker?" and "Finding a better tradeoff," Okhsv and Okhsl (Bj\u00f6rn Ottosson).

# Verification Notes

- Definition source: Synthesised from Ottosson's discussion
- Confidence rationale: High \u2014 gamut is discussed pervasively and critically throughout the Ottosson source
- Uncertainties: None significant
- Cross-reference status: Primarily from Ottosson source; not discussed substantively in Drasner
- Rosetta Stone check: No mappings added
- OCR issues: None significant
