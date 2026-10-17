---
concept: "Colour Gamut"
slug: "colour-gamut"
category: "colour-theory"
subcategory: "colour-spaces"
tier: "foundational"
layer: "2-domain"
source: "Okhsv and Okhsl"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "What makes a good color picker?"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "high"
aliases:
  -
    - "gamut"
    - "color gamut"
    - "sRGB gamut"
prerequisites: []
extends: []
related:
  - "hsl"
  - "hsv"
  - "okhsl"
  - "okhsv"
contrasts_with: []
answers_questions:
  - "What makes a colour picker perceptually well-designed?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition


A colour gamut is the set of colours representable under a specified colour space, encoding and output or model constraint. A gamut is the set or volume, not merely its boundary; sRGB is one defined target, not a universal screen or CSS gamut.

# Core Definition


Ottosson frames this article around selecting colours in sRGB and shows how that gamut occupies irregular, hue-dependent regions in Oklab-derived coordinates. A gamut is the representable set; its boundary marks the limit. In a chosen RGB coordinate representation, HSL and HSV re-parameterize the encoded sRGB cube into bounded cylindrical coordinates, but this geometry does not make their axes perceptually uniform. The article’s sRGB picker comparison is scoped to that target and to its proposed criteria. Wider-gamut displays and HDR are distinct conditions, not synonyms for gamut.

# Prerequisites

- None — gamut is a foundational concept

# Key Properties


1. sRGB defines a bounded RGB gamut; it is not all colours visible to humans and not the gamut of every display.
2. The same target gamut has different coordinate-space shapes; its boundary can vary with hue and lightness in perceptual coordinates.
3. HSL/HSV parameter ranges describe the encoded sRGB cube through a coordinate transform; bounded parameters do not establish perceptual accuracy.
4. Conversion between spaces, mapping to a destination gamut, and clipping components are distinct operations. CSS Color 4 specifies particular display mapping conditions; there is no generic nearest-colour or component-clamp rule for every context.

# Construction / Recognition

## To Identify/Recognise:

1. Name the source and destination spaces, encoding, and output constraints before deciding whether a colour is representable.
2. An out-of-gamut value is outside the destination set; how it is mapped depends on the applicable method and destination.
3. In an HSL/HSV coordinate box for encoded sRGB, in-range coordinates map into that RGB gamut. This is a coordinate fact, not a claim about a widget’s visible boundary or perceptual uniformity.
4. The article’s Oklab slices illustrate hue-dependent sRGB boundaries; they are attributed examples, not newly inspected figures.

# Context & Application

- **Typical contexts**: Colour space design, colour picker implementation, gamut mapping in print/digital conversion, CSS Color 4 `color()` function
- **Common applications**: Determining which colours are safe to use on screen; clipping or mapping colours when converting between gamuts

# Examples

**Example 1** (source description): In the Okhsv construction, the source uses L_r vertically and C·L_r/L horizontally for hue-specific sRGB cross-sections, then describes a triangular approximation, cusp remapping and a curved-top compensation through v. The axes and geometry are attributed to the prepared text; the figures were not independently inspected. The horizontal coordinate is scaled chroma, not raw Oklab C.

**Example 2** (source-reported observation, not independently tested): "Several color pickers have been made using either CIELab or more modern lab-like color spaces... it is also common to see CIELab based color pickers showing colors outside the target gamut and often they are mapped back by simply clamping individual RGB components. This creates severe distortions in hue, lightness and chroma."

# Relationships

## Builds Upon

- **RGB colour model** — sRGB’s RGB definition specifies one reference gamut; other RGB standards and devices can define different sets.

## Enables

- **Colour picker design** — A named target gamut informs which candidates and output checks apply.
- **Okhsl / Okhsv** — The prepared article compares their constructions for an sRGB picker; this is not a universal gamut claim.

## Related

- **Colour spaces** — Coordinate systems and their representable sets are related but distinct.

# Common Errors


**Error**: Assuming every CSS colour is in gamut or that out-of-gamut values are always clamped to the nearest sRGB colour.
  **Correction**: Identify the specified colour space and actual display destination. CSS Color 4 distinguishes valid out-of-gamut values from the display-time gamut-mapping process; other pipelines can use other methods.

**Error**: Saying HSL values are invalid because they fall outside a perceptual boundary.
  **Correction**: HSL coordinates resolve to sRGB under CSS syntax. Interpret the bounded HSL ranges as a re-parameterization, not a perceptual gamut model.

# Common Confusions


**Confusion**: Gamut means the boundary of a colour space.
  **Clarification**: A colour space supplies coordinates; a gamut is the subset representable under stated conditions, and the boundary is only its limit. A device, standard, encoding or model may constrain a different set.

**Confusion**: The article’s sRGB target is the default gamut for every CSS or screen task.
  **Clarification**: It is the scope of this picker comparison. CSS and displays can involve other spaces and destinations.

# Source Reference

"What makes a good color picker?" and "Finding a better tradeoff," Okhsv and Okhsl (Björn Ottosson).

# Verification Notes


This full available-evidence review checked the definition and source-specific examples against the complete prepared picker article and CSS Color Module Level 4, a W3C Candidate Recommendation Draft published 2026-10-09 (https://www.w3.org/TR/2026/CRD-css-color-4-20261009/), especially §§7–7.2 and 14. The sRGB and picker comparisons remain source-scoped; conversion, mapping and clipping are distinguished. Figures were described from prepared text and not independently inspected. No device, browser, HDR, print or accessibility behavior was tested; original capture fidelity and full-corpus review remain open. Extraction-confidence metadata is unchanged.
