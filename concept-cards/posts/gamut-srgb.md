---
concept: Gamut (sRGB)
slug: gamut-srgb
category: colour-theory
subcategory: colour gamuts
tier: foundational
layer: 2-domain
source: "A Perceptual Color Space for Image Processing"
source_slug: posts
authors: "Bj\u00f6rn Ottosson"
chapter: "How Oklab was derived"
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
  - oklab
  - xyz-colour-space
  - colour-space-comparison
contrasts_with:
  - []
answers_questions:
  - "What makes a colour space perceptually uniform, and why does it matter for design?"
rosetta_stone: []
css_implementation:
  - property: "color"
    example: "color(display-p3 1 0 0); /* wider than sRGB */"
    support: partial
---

# Quick Definition

The sRGB gamut is the set of colours representable in the sRGB colour space \u2014 a triangular subset of the full visible colour range defined by three primary colours (red, green, blue) at a D65 whitepoint.

# Core Definition

The source references the sRGB gamut in two key ways. First, as a practical scope constraint on Oklab's design: "when looking at the sRGB gamut, the blue colors folded in on themselves slightly, resulting in a non-convex sRGB gamut." This led to adding a constraint during Oklab's derivation to prevent this: "By forcing the value of \u03b3 to 1/3 and adding a constraint the blue colors to not fold inwards, the final Oklab model was derived."

Second, the Luo-Rigg plots show "a slice of the sRGB gamut" alongside the full visible gamut, making the sRGB gamut a visual reference for comparing colour spaces.

The source also notes HSV "does not handle colors outside sRGB gamut" \u2014 confirming sRGB as a bounded subset of the full colour space.

# Prerequisites

- **Colour space** \u2014 Gamut is a property of a colour space.
- **D65 whitepoint** \u2014 sRGB uses D65; the gamut is defined relative to this white.

# Key Properties

1. sRGB gamut is a bounded triangular region in chromaticity: the set of colours achievable by mixing three specific red, green, and blue primaries.
2. sRGB is a subset of the full visible gamut; many natural colours (especially highly saturated ones) fall outside it.
3. In Oklab, the sRGB gamut forms a convex body in (L, a, b) space \u2014 Oklab's derivation explicitly enforced this convexity for blue colours.
4. The sRGB gamut shares D65 as its whitepoint with Oklab, Display P3, and Rec. 2020.
5. Colours outside the sRGB gamut cannot be directly displayed on standard sRGB monitors; they require gamut mapping.

# Construction / Recognition

## To Construct/Create:
1. The sRGB gamut in Oklab is the image of the unit cube [0,1]\u00b3 in (R,G,B) space under the linear_srgb_to_oklab transform.
2. To check if an Oklab colour is within sRGB: convert to linear sRGB and verify all three channels are in [0, 1].

## To Identify/Recognise:
1. In the Luo-Rigg plots: the sRGB gamut appears as a bounded region inside the larger visible gamut boundary.
2. Colours outside sRGB: conversion to linear sRGB produces values < 0 or > 1 on at least one channel.

# Context & Application

- **Typical contexts**: Web design (sRGB is the default gamut for standard monitors); CSS (sRGB colours specified with `rgb()`, `hsl()`, `hex`); display pipeline engineering.
- **Common applications**: Determining whether a colour in Oklab is displayable on an sRGB monitor; gamut mapping; understanding which colours are "in range" for web design.

# Examples

**Example 1** (from source): During Oklab's derivation, early versions of the model caused blue sRGB gamut colours to "fold in on themselves slightly, resulting in a non-convex sRGB gamut." A constraint was added to prevent this. (Section: "How Oklab was derived")

**Example 2** (from source): The Luo-Rigg plots show the sRGB gamut as a slice within the full visible gamut, with the sRGB gamut visible as a bounded region in each colour space's ab plane. (Section: "Luo-Rigg dataset and full gamut")

**Example 3** (from source): HSV fails for the Luo-Rigg full gamut plot because "HSV does not handle colors outside sRGB gamut" \u2014 confirming the gamut as a hard limit for HSV. (Section: "Luo-Rigg dataset and full gamut")

# Relationships

## Builds Upon
- **Colour space** \u2014 Gamut is a property of a colour space.
- **sRGB** \u2014 sRGB is the specific colour space defining this gamut.

## Enables
- **Gamut mapping** \u2014 Understanding the sRGB gamut boundary allows mapping out-of-gamut Oklab colours to displayable values.
- **Oklab design** \u2014 The sRGB gamut's shape in Oklab space was a constraint in Oklab's derivation.

## Related
- **D65 whitepoint** \u2014 sRGB is defined with D65.
- **XYZ colour space** \u2014 The visible gamut and sRGB gamut are both expressible in XYZ chromaticity.

## Contrasts With
- **Full visible gamut** \u2014 The set of all colours human eyes can perceive, which is significantly larger than sRGB.
- **Display P3, Rec. 2020** \u2014 Wider gamuts that supersede sRGB for HDR and cinema displays.

# Common Errors

- **Error**: Assuming all real-world colours fall within the sRGB gamut.
  **Correction**: The source shows (via Luo-Rigg plots) that highly saturated real surface colours exist outside sRGB; "Pointer's Gamut \u2014 the set of possible surface colors" is used as a superset in the Oklab derivation data.

# Common Confusions

- **Confusion**: sRGB gamut and sRGB colour space are the same thing.
  **Clarification**: The sRGB colour space includes a gamma encoding curve and whitepoint definition; the gamut is just the set of representable colours. The gamut can be described in other colour spaces (e.g., as a region in XYZ or Oklab).

# Source Reference

"How Oklab was derived" (gamut convexity constraint); "Luo-Rigg dataset and full gamut" (gamut slice in plots); HSV limitation note.

# Verification Notes

- Definition source: Synthesised from references to "sRGB gamut" throughout the source; the source does not define sRGB gamut explicitly.
- Confidence rationale: Medium \u2014 the concept is referenced functionally (gamut convexity, gamut slice, HSV gamut limit) without a formal definition; definition synthesised from usage.
- Uncertainties: The source does not provide explicit sRGB primary chromaticities or a formal gamut definition.
- Cross-reference status: Verified against derivation section and Luo-Rigg discussion.
- Rosetta Stone check: No rosetta stone mappings.
- OCR issues: None significant.
