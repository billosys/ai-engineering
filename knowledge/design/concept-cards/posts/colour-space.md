---
concept: "Colour Space (General)"
slug: "colour-space"
category: "colour-theory"
subcategory: "colour models"
tier: "foundational"
layer: "2-domain"
source: "A Perceptual Color Space for Image Processing"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "A perceptual color space for image processing"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "medium"
aliases: []
prerequisites: []
extends: []
related:
  - "oklab"
  - "xyz-colour-space"
  - "lms-cone-responses"
  - "d65-whitepoint"
  - "gamut-srgb"
contrasts_with: []
answers_questions:
  - "What makes a colour space perceptually uniform, and why does it matter for design?"
---

# Quick Definition
A colour space assigns coordinates to colours under stated model, observer, reference conditions and representable domain.

# Core Definition
A colour space is a coordinate representation whose meaning depends on its model and reference conditions. Coordinates may be constrained by a device gamut or defined over a wider mathematical domain. A representation does not promise a unique polar hue when chroma is zero, nor that every visible colour is representable by every device space. XYZ is a useful tristimulus representation and conversion route, but not a mandatory intermediary for all colour-space conversions.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Coordinate values are meaningful only with their model, observer/reference and encoding conventions.
2. Device spaces such as sRGB have bounded representable gamuts; a mathematical coordinate may convert outside that gamut.
3. Polar hue is undefined at zero chroma.
4. Different representations can describe overlapping colours without identical coordinates or encoding.

# Construction / Recognition

## To Construct/Create:
1. Choose axes representing perceptual or physical dimensions of colour.
2. Define a whitepoint.
3. Derive a transform from a reference space (e.g., XYZ) to the new coordinates.
4. Verify the transform is invertible and numerically stable.

## To Identify/Recognise:
1. Look for a coordinate tuple (2D or 3D) assigned to each colour.
2. Identify the whitepoint and the reference space it relates to.
3. Determine whether the space is linear or non-linear (e.g., sRGB uses gamma encoding; Oklab uses a cube root).

# Context & Application

- **Typical contexts**: Image processing, colour correction, display engineering, UI/CSS colour specification, colour science research.
- **Common applications**: Converting colours between display devices; specifying colours in CSS; comparing perceived colour differences; designing palettes.

# Examples
**Example 1** (source): Ottosson describes sRGB using D65 and presents a linear-sRGB → XYZ → LMS-like → Oklab route. This is one stated conversion route, not a requirement for every conversion. (Section: “Implementation”)

# Relationships
## Builds Upon
- **Coordinate system** — A model assigns meaning to coordinates.

## Enables
- **Colour conversion** — Requires compatible definitions and a specified route.

## Related
- **XYZ colour space** — One useful tristimulus representation.
- **D65 whitepoint** — A reference condition used by some spaces.

## Contrasts With
- **Device gamut** — A bounded representable subset is distinct from a general coordinate model.

# Common Errors
- **Error**: Assuming every colour space uniquely represents every visible colour.
  **Correction**: State the represented domain and distinguish device gamut from a model's mathematical coordinates.
- **Error**: Assuming all conversions must pass through XYZ.
  **Correction**: XYZ is useful, but direct conversions may use another valid route.

# Common Confusions
- **Confusion**: All colour spaces cover every visible colour and provide a unique hue coordinate.
  **Clarification**: Device gamuts are bounded, and polar hue is undefined at zero chroma.

# Source Reference

"A perceptual color space for image processing" (introduction); colour space comparisons throughout "Comparison with other color spaces" and "What about existing models?".

# Verification Notes
The prepared article and CSS Color 4 distinguish model coordinates, reference white and destination gamut. These notes correct scope; they do not establish full-corpus conformance or original-capture fidelity.
