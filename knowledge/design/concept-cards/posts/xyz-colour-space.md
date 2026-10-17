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
1. X, Y and Z are tristimulus coordinates under stated observer/reference conditions.
2. They are not independent perceptual channels; X and Z are not standalone chrominance channels.
3. The representation is linear, but complete conversion routes can include nonlinear stages.
4. Pure-axis test values are arithmetic fixtures unless a display conversion and gamut check establish otherwise.
5. XYZ is useful, not mandatory, as a conversion intermediate.

# Construction / Recognition

## To Construct/Create:
1. Convert from linear sRGB using the standard sRGB-to-XYZ matrix (not given explicitly in the source; Oklab's M1 concatenates this with the XYZ-to-LMS step).
2. Ensure Y=1 corresponds to D65 white.

## To Identify/Recognise:
1. Three channels X, Y, Z — all non-negative for physical colours.
2. White at approximately (0.950, 1.000, 1.089) under D65.
3. A linear space — no gamma curve applied.

# Context & Application

- **Typical contexts**: Colour science; universal intermediary in colour conversion pipelines; CSS Color Level 4 defines `color(xyz-d65 ...)`.
- **Common applications**: Converting between any two colour spaces (sRGB → XYZ → Oklab; sRGB → XYZ → Display P3, etc.).

## Cross-Domain Connections

**Mathematics → RIGOROUS**: XYZ is a linear vector space — operations on XYZ coordinates are linear transformations (matrix multiplications). This is why the sRGB→XYZ and XYZ→LMS steps in the Oklab pipeline are pure matrix multiplications: linearity is preserved all the way until the cube-root non-linearity is applied to the LMS values.

# Examples
The article's pure-axis XYZ vectors are arithmetic examples. Without a specified display conversion and gamut check they are not verified visible colours.

# Relationships

## Builds Upon
- **Colour space** — XYZ is a specific colour space.
- **CIE 1931 colour matching functions** — XYZ was defined by the CIE using experimental colour matching data (assumed background; not discussed in source).

## Enables
- **LMS cone responses** — XYZ is transformed to approximate cone responses via M1.
- **Oklab conversion** — The full pipeline is XYZ → LMS (approximate) → LMS' (cube root) → Lab.
- **Universal colour conversion** — Any colour space that can be expressed in XYZ terms can be converted to any other via XYZ as intermediary.

## Related
- **Matrix transformation in colour conversion** — XYZ ↔ sRGB and XYZ ↔ LMS both use matrix multiplication.

## Contrasts With
- **sRGB** — sRGB is device-specific and non-linear (gamma-encoded); XYZ is device-independent and linear.
- **Oklab** — Oklab is perceptually uniform and non-linear; XYZ is perceptually non-uniform and linear.

# Common Errors
- **Error**: Claiming every operation involving XYZ is linear, or that all space conversions must pass through it.
  **Correction**: Scope linearity to the representation and actual linear stages; name nonlinear steps and the selected route.
- **Error**: Calling pure X/Y/Z fixtures visible saturated colours.
  **Correction**: Label them as arithmetic test coordinates unless display conversion and gamut have been verified.

# Common Confusions
- **Confusion**: X/Z directly encode chrominance while Y is brightness.
  **Clarification**: These are tristimulus coordinates under a defined observer; they are not independent perceptual channels.

# Source Reference

"Converting from XYZ to Oklab"; "Table of example XYZ and Oklab pairs" sections.

# Verification Notes
XYZ's role and Oklab's nonlinear route were checked against the prepared article and CSS Color 4 CRD 2026-10-09. The rosetta note scopes linearity to the representation/stages. Pure-axis examples are arithmetic only.
