---
concept: D65 Whitepoint
slug: d65-whitepoint
category: colour-theory
subcategory: illuminants
tier: foundational
layer: 2-domain
source: "A Perceptual Color Space for Image Processing"
source_slug: posts
authors: "Bj\u00f6rn Ottosson"
chapter: "The Oklab color space"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: medium
aliases:
  - []
prerequisites:
  - colour-space
extends:
  - []
related:
  - oklab
  - xyz-colour-space
  - gamut-srgb
contrasts_with:
  - []
answers_questions:
  - "What makes a colour space perceptually uniform, and why does it matter for design?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition

D65 is a standard reference whitepoint representing average daylight (correlated colour temperature of approximately 6500 K), used as the white reference in sRGB, Display P3, Rec. 2020, and Oklab.

# Core Definition

The source states: "Oklab uses a D65 whitepoint, since this is what sRGB and other common color spaces use." In Oklab, D65 normalised with Y=1 maps to (L=1, a=0, b=0) \u2014 the absolute white of the colour space.

The requirements for Oklab explicitly include: "Should assume a D65 whitepoint. This is what common color spaces like sRGB, rec2020 and Display P3 uses."

In the XYZ example table, the entry (X=0.950, Y=1.000, Z=1.089) corresponds to D65 and maps to Oklab (L=1.000, a=0.000, b=0.000), confirming D65 as the normalising white.

# Prerequisites

- **Colour space** \u2014 Whitepoints are a property of colour spaces; the general concept is required.

# Key Properties

1. D65 represents average daylight, widely adopted as the standard for display-oriented colour spaces.
2. In Oklab (and XYZ with Y=1), D65 maps to the white point of the perceptual coordinate system.
3. Using a shared whitepoint (D65) is what makes Oklab directly compatible with sRGB, Display P3, and Rec. 2020 without a chromatic adaptation step.
4. White in D65-normalised XYZ: (X\u22480.950, Y=1.000, Z\u22481.089).

# Construction / Recognition

## To Construct/Create:
1. When converting to Oklab, use XYZ values normalised so that D65 white = (X=0.950, Y=1.000, Z=1.089).
2. The conversion matrices M1 and M2 in Oklab are derived with this specific normalisation \u2014 using a different whitepoint would require different matrices.

## To Identify/Recognise:
1. A colour space uses D65 if its white reference corresponds to approximately 6500 K daylight.
2. The example table confirms: XYZ (0.950, 1.000, 1.089) \u2192 Oklab (1.000, 0.000, 0.000).

# Context & Application

- **Typical contexts**: Any display-referred colour workflow on standard monitors (sRGB, Display P3, Rec. 2020).
- **Common applications**: CSS colour functions (all CSS Level 4 colour spaces use D65); Photoshop; game engine colour systems using Oklab.

# Examples

**Example 1** (from source): The XYZ/Oklab example table lists (X=0.950, Y=1.000, Z=1.089) \u2192 (L=1.000, a=0.000, b=0.000), which is D65 white mapping to Oklab white. (Section: "Table of example XYZ and Oklab pairs")

# Relationships

## Builds Upon
- **Colour space** \u2014 Whitepoint is a property of a colour space.

## Enables
- **Oklab conversion** \u2014 The specific matrix values in Oklab's conversion are calibrated to D65.
- **Cross-space compatibility** \u2014 Shared D65 whitepoint allows direct conversion between sRGB and Oklab without chromatic adaptation.

## Related
- **sRGB gamut** \u2014 sRGB is a D65-based colour space; Oklab is designed to work natively with it.

# Common Errors

- **Error**: Using Oklab conversion matrices designed for D65 with colour data normalised to a different whitepoint (e.g., D50 used in some print workflows).
  **Correction**: The matrices must be re-derived, or a chromatic adaptation transform must be applied first.

# Common Confusions

- **Confusion**: D65 is a specific colour, not a reference point.
  **Clarification**: D65 is a standard illuminant (spectral power distribution approximating daylight); in practice for display work it is a reference white that allows all other colours to be described relative to it.

# Source Reference

"The Oklab color space" section; requirements list in "Motivation and derivation of Oklab"; example table in "Converting from XYZ to Oklab".

# Verification Notes

- Definition source: Direct quotes from "The Oklab color space" and requirements list; D65 XYZ values from example table.
- Confidence rationale: Medium \u2014 the source uses D65 as a requirement and verification point but does not explain what D65 is; the background definition was inferred from colour science convention.
- Uncertainties: The source does not state the correlated colour temperature (6500 K) explicitly; this was inferred from standard knowledge of D65.
- Cross-reference status: Verified against example table and requirements list.
- Rosetta Stone check: No rosetta stone mappings.
- OCR issues: None significant.
