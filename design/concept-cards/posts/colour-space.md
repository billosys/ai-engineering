---
concept: Colour Space (General)
slug: colour-space
category: colour-theory
subcategory: colour models
tier: foundational
layer: 2-domain
source: "A Perceptual Color Space for Image Processing"
source_slug: posts
authors: "Bj\u00f6rn Ottosson"
chapter: "A perceptual color space for image processing"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: medium
aliases:
  - []
prerequisites:
  - []
extends:
  - []
related:
  - oklab
  - xyz-colour-space
  - lms-cone-responses
  - d65-whitepoint
  - gamut-srgb
contrasts_with:
  - []
answers_questions:
  - "What makes a colour space perceptually uniform, and why does it matter for design?"
---

# Quick Definition

A colour space is a mathematical coordinate system in which every colour is represented as a point, allowing colours to be specified, compared, and manipulated numerically.

# Core Definition

The source uses the term "color space" throughout to refer to systems that assign numerical coordinates to colours. Multiple colour spaces are compared: CIELAB, CIELUV, HSV, sRGB, XYZ, IPT, JzAzBz, CAM16-UCS, OSA-UCS, and Oklab. Each represents the same physical colours with different coordinate systems, chosen for different purposes \u2014 device representation (sRGB), perceptual uniformity (CIELAB, Oklab), or computational simplicity (HSV).

A colour space involves at minimum: a set of axes (dimensions), a whitepoint reference, and a conversion relationship to other colour spaces. Many colour spaces are derived by applying a mathematical transform to another space.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Each colour space assigns a unique coordinate tuple to every representable colour.
2. Colour spaces are related by mathematical transforms (often matrix multiplication plus non-linear functions).
3. A colour space's usefulness depends on its purpose: device encoding, perceptual uniformity, or gamut coverage.
4. All colour spaces discussed in the source share a common whitepoint (D65) for meaningful comparison.

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

**Example 1** (from source): The source compares eight colour spaces (Oklab, CIELAB, CIELUV, OSA-UCS, IPT, JzAzBz, HSV, CAM16-UCS) on the same three perceptual error metrics, demonstrating that different colour spaces make very different trade-offs. (Section: "Comparison with other color spaces")

**Example 2** (from source): sRGB is described as a colour space using a D65 whitepoint, whose colours can be converted to Oklab via linear sRGB \u2192 XYZ \u2192 LMS \u2192 Oklab. (Section: "Implementation")

# Relationships

## Builds Upon
- **Human visual perception** \u2014 Colour spaces ultimately reference the three-channel nature of human cone responses.

## Enables
- **Oklab colour space** \u2014 Oklab is a specific colour space.
- **XYZ colour space** \u2014 XYZ is the reference intermediary between most other colour spaces.
- **Colour interpolation** \u2014 Requires a colour space to define the coordinates to interpolate.

## Related
- **Gamut** \u2014 Each colour space has an associated gamut (the set of colours it can represent).
- **Whitepoint** \u2014 Every colour space requires a reference white for normalisation.

## Contrasts With
- (No specific contrasts defined at this foundational level \u2014 the concept encompasses all colour spaces equally.)

# Common Errors

- **Error**: Assuming all colour spaces represent the same range of colours.
  **Correction**: Different colour spaces have different gamuts; sRGB cannot represent all colours in the visible gamut, while XYZ can.

# Common Confusions

- **Confusion**: A colour space and a colour model are the same thing.
  **Clarification**: A colour model defines the type of axes (e.g., RGB, Lab, LCh); a colour space is a specific instantiation with defined primaries, whitepoint, and transform.

# Source Reference

"A perceptual color space for image processing" (introduction); colour space comparisons throughout "Comparison with other color spaces" and "What about existing models?".

# Verification Notes

- Definition source: Synthesised from usage across the entire article; the source assumes prior knowledge of colour spaces rather than defining the concept explicitly.
- Confidence rationale: Medium \u2014 the concept is implicit rather than explicitly defined in the source; definition was constructed from the article's consistent usage.
- Uncertainties: The source does not offer a single-sentence definition of "colour space" \u2014 it is background knowledge assumed of the reader.
- Cross-reference status: Verified as consistent with all colour space references throughout the source.
- Rosetta Stone check: No rosetta stone mappings for this foundational concept.
- OCR issues: None significant.
