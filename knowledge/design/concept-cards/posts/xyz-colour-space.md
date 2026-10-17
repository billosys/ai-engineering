---
concept: "XYZ Colour Space"
slug: "xyz-colour-space"
category: "colour-theory"
subcategory: "colorimetry"
tier: "intermediate"
layer: "2-domain"
source: "A Perceptual Color Space for Image Processing"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "Converting from XYZ to Oklab"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "medium"
aliases: []
prerequisites:
  - "colour-space"
  - "d65-whitepoint"
extends:
  - "colour-space"
related:
  - "lms-cone-responses"
  - "oklab"
  - "oklab-conversion"
  - "matrix-transformation-colour"
contrasts_with: []
answers_questions:
  - "How do you convert between colour spaces for image processing?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Linear vector space"
    rating: "rigorous"
    note: "XYZ is a linear tristimulus representation and linear stages can be expressed as matrix operations; a complete conversion or other operation involving XYZ may include nonlinear steps."
css_implementation: []
---

# Quick Definition
CIE XYZ is a linear tristimulus representation defined for a specified standard observer; its coordinates are not standalone chrominance channels or a mandatory route for every conversion.

# Core Definition
XYZ represents tristimulus values under defined observer/reference conventions. Linear operations on XYZ coordinates are possible within the model, but conversions may include nonlinear encoding, chromatic adaptation, gamut mapping or other operations. X and Z are not isolated chrominance channels. XYZ is a useful connection between some colour representations, not a required intermediary in every conversion. Pure-axis test vectors are arithmetic fixtures and should not be presented as verified visible display colours.

# Prerequisites

- **Colour space** — XYZ is a colour space; the general concept is required.
- **D65 whitepoint** — The source specifies XYZ with D65 whitepoint; the normalisation matters for the conversion.

# Key Properties
1. X, Y and Z are tristimulus coordinates under stated observer/reference conditions. In CSS Color 4 §10.9, relative Y is normalized to 1 at diffuse white; XYZ Y has a luminance role under those conventions but is not Oklab L.
2. They are not independent perceptual channels; X and Z are not standalone chrominance channels.
3. The representation is linear, but complete conversion routes can include nonlinear stages.
4. Pure-axis test values are arithmetic fixtures unless a display conversion and gamut check establish otherwise.
5. XYZ is useful, not mandatory, as a conversion intermediate.

# Construction / Recognition
## To Construct/Create:
1. State the standard observer, reference white and normalization.
2. Apply a specified XYZ conversion stage; include any decoding, adaptation or nonlinear steps in the complete route.
3. Treat pure-axis values as arithmetic fixtures unless converted and gamut-checked for display.

## To Identify/Recognise:
1. XYZ values are tristimulus coordinates, not standalone chrominance/brightness channels.
2. The D65 white example is rounded.
3. Distinguish a linear XYZ stage from a complete nonlinear conversion route.

# Context & Application
- **Typical contexts**: Colorimetry and some colour-conversion routes under stated observer/reference conditions.
- **Common applications**: CSS Color defines XYZ-related syntax; under §10.9 relative Y=1 corresponds to diffuse white. XYZ Y and Oklab L are different quantities, and XYZ’s use in some routes does not make it mandatory for all conversions.

## Cross-Domain Connections
**Mathematics → RIGOROUS**: XYZ is a linear tristimulus representation under stated conventions. The article's sRGB→XYZ and XYZ→LMS-like stages are linear matrix operations; its complete Oklab route adds a pointwise cube-root stage.

# Examples
The article's pure-axis XYZ vectors are arithmetic examples. Without a specified display conversion and gamut check they are not verified visible colours.

# Relationships
## Builds Upon
- **Colour space** — XYZ is a model-specific coordinate representation.

## Enables
- **Selected conversions** — XYZ is a useful intermediate for some routes.

## Related
- **LMS-like intermediates** — The article applies an XYZ-form matrix.
- **D65 whitepoint** — The example uses a D65 normalization.

## Contrasts With
- **Nonlinear conversion stages** — A complete route can add operations beyond linear XYZ matrices.

# Common Errors
- **Error**: Claiming every operation involving XYZ is linear, or that all space conversions must pass through it.
  **Correction**: Scope linearity to the representation and actual linear stages; name nonlinear steps and the selected route.
- **Error**: Calling pure X/Y/Z fixtures visible saturated colours.
  **Correction**: Label them as arithmetic test coordinates unless display conversion and gamut have been verified.

# Common Confusions
- **Confusion**: XYZ is a “linear vector space,” so every operation involving it is linear.
  **Clarification**: The representation and stated matrix stages are linear; a complete conversion can include nonlinear operations.

# Source Reference

"Converting from XYZ to Oklab"; "Table of example XYZ and Oklab pairs" sections.

# Verification Notes
XYZ's role and Oklab's nonlinear route were checked against the prepared article and CSS Color 4 CRD 2026-10-09. The rosetta note scopes linearity to the representation/stages. Pure-axis examples are arithmetic only.
