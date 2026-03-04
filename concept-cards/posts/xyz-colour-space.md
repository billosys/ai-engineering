---
concept: XYZ Colour Space
slug: xyz-colour-space
category: colour-theory
subcategory: colorimetry
tier: intermediate
layer: 2-domain
source: "A Perceptual Color Space for Image Processing"
source_slug: posts
authors: "Bj\u00f6rn Ottosson"
chapter: "Converting from XYZ to Oklab"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: medium
aliases:
  - []
prerequisites:
  - colour-space
  - d65-whitepoint
extends:
  - colour-space
related:
  - lms-cone-responses
  - oklab
  - oklab-conversion
  - matrix-transformation-colour
contrasts_with:
  - []
answers_questions:
  - "How do you convert between colour spaces for image processing?"
rosetta_stone:
  - domain: mathematics
    concept: "Linear vector space"
    rating: rigorous
    note: "XYZ is a linear colour space \u2014 all operations on it are linear transformations (matrix multiplications). Non-linear steps are applied after leaving XYZ."
css_implementation: []
---

# Quick Definition

CIE XYZ is a device-independent, linear colour space that serves as the universal reference intermediary for converting between all other colour spaces; Oklab's conversion pipeline passes through XYZ.

# Core Definition

The source treats XYZ as the starting point for the Oklab conversion, describing it as: "Given a color in XYZ coordinates, with a D65 whitepoint and white as Y=1." XYZ is not defined further in the source \u2014 it is assumed background knowledge \u2014 but it is used as the common reference from which cone responses and ultimately Oklab coordinates are derived.

XYZ is a linear colour space: it models colour as a linear combination of three tristimulus values (X, Y, Z) calibrated to human vision by the CIE in 1931. Y corresponds to luminance. The source provides a reference table of XYZ/Oklab pairs with white at (X=0.950, Y=1.000, Z=1.089), confirming D65 normalisation.

# Prerequisites

- **Colour space** \u2014 XYZ is a colour space; the general concept is required.
- **D65 whitepoint** \u2014 The source specifies XYZ with D65 whitepoint; the normalisation matters for the conversion.

# Key Properties

1. Device-independent: XYZ describes colour in terms of human tristimulus response, not device primaries.
2. Linear: all colour operations in XYZ are linear transforms (matrix multiplications); no gamma correction.
3. Y is luminance; X and Z carry chrominance information.
4. D65-normalised white: (X\u22480.950, Y=1.000, Z\u22481.089).
5. The entire visible gamut can be represented; it is not limited to sRGB.

# Construction / Recognition

## To Construct/Create:
1. Convert from linear sRGB using the standard sRGB-to-XYZ matrix (not given explicitly in the source; Oklab's M1 concatenates this with the XYZ-to-LMS step).
2. Ensure Y=1 corresponds to D65 white.

## To Identify/Recognise:
1. Three channels X, Y, Z \u2014 all non-negative for physical colours.
2. White at approximately (0.950, 1.000, 1.089) under D65.
3. A linear space \u2014 no gamma curve applied.

# Context & Application

- **Typical contexts**: Colour science; universal intermediary in colour conversion pipelines; CSS Color Level 4 defines `color(xyz-d65 ...)`.
- **Common applications**: Converting between any two colour spaces (sRGB \u2192 XYZ \u2192 Oklab; sRGB \u2192 XYZ \u2192 Display P3, etc.).

## Cross-Domain Connections

**Mathematics \u2192 RIGOROUS**: XYZ is a linear vector space \u2014 operations on XYZ coordinates are linear transformations (matrix multiplications). This is why the sRGB\u2192XYZ and XYZ\u2192LMS steps in the Oklab pipeline are pure matrix multiplications: linearity is preserved all the way until the cube-root non-linearity is applied to the LMS values.

# Examples

**Example 1** (from source): The conversion pipeline begins with XYZ input: "(l m s)^T = M1 \u00d7 (X Y Z)^T". The reference table confirms four XYZ\u2192Oklab conversions, with pure X (1,0,0) mapping to Oklab (0.450, 1.236, -0.019) \u2014 a highly saturated colour in the red-magenta direction. (Section: "Converting from XYZ to Oklab")

# Relationships

## Builds Upon
- **Colour space** \u2014 XYZ is a specific colour space.
- **CIE 1931 colour matching functions** \u2014 XYZ was defined by the CIE using experimental colour matching data (assumed background; not discussed in source).

## Enables
- **LMS cone responses** \u2014 XYZ is transformed to approximate cone responses via M1.
- **Oklab conversion** \u2014 The full pipeline is XYZ \u2192 LMS (approximate) \u2192 LMS' (cube root) \u2192 Lab.
- **Universal colour conversion** \u2014 Any colour space that can be expressed in XYZ terms can be converted to any other via XYZ as intermediary.

## Related
- **Matrix transformation in colour conversion** \u2014 XYZ \u2194 sRGB and XYZ \u2194 LMS both use matrix multiplication.

## Contrasts With
- **sRGB** \u2014 sRGB is device-specific and non-linear (gamma-encoded); XYZ is device-independent and linear.
- **Oklab** \u2014 Oklab is perceptually uniform and non-linear; XYZ is perceptually non-uniform and linear.

# Common Errors

- **Error**: Using gamma-encoded sRGB values directly as XYZ inputs.
  **Correction**: sRGB must be linearised (gamma-decoded) before conversion to XYZ. The source references this: "To compute linear sRGB values, see my previous post."

# Common Confusions

- **Confusion**: XYZ is the same as xyY or xy chromaticity.
  **Clarification**: xyY is a derived representation of XYZ (normalised chromaticity coordinates); they encode the same information differently.

# Source Reference

"Converting from XYZ to Oklab"; "Table of example XYZ and Oklab pairs" sections.

# Verification Notes

- Definition source: Synthesised from usage; the source assumes prior knowledge of XYZ and does not define it.
- Confidence rationale: Medium \u2014 XYZ is used as background infrastructure in the source, not explained; definition synthesised from colour science convention and source usage.
- Uncertainties: The source does not discuss the CIE 1931 derivation of XYZ or the meaning of individual X, Y, Z axes beyond noting Y=1 for D65 white.
- Cross-reference status: Verified against conversion equations and example table.
- Rosetta Stone check: Mathematics/linear-vector-space mapping added as rigorous.
- OCR issues: None significant.
