---
concept: "Gamut (sRGB)"
slug: "gamut-srgb"
category: "colour-theory"
subcategory: "colour gamuts"
tier: "foundational"
layer: "2-domain"
source: "A Perceptual Color Space for Image Processing"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "How Oklab was derived"
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
  - "oklab"
  - "xyz-colour-space"
  - "colour-space-comparison"
contrasts_with: []
answers_questions:
  - "What makes a colour space perceptually uniform, and why does it matter for design?"
rosetta_stone: []
css_implementation:
  -
    property: "color"
    example: "color(display-p3 1 0 0); /* wider than sRGB */"
    support: "partial"
---

# Quick Definition
sRGB gamut is the bounded set of colours representable by the sRGB encoding and primaries; its chromaticity triangle is a projection of a three-dimensional colour volume.

# Core Definition
Distinguish a coordinate value being syntactically valid, a colour being mathematically convertible, and its being representable in the destination sRGB gamut. A practical linear-sRGB check tests all channels against [0,1] with an explicitly stated numerical tolerance. The familiar triangle is a chromaticity projection, not the full 3D gamut. A local blue-fold constraint does not prove global convexity. Wide-gamut primaries and HDR are distinct properties; P3 or Rec.2020 do not universally supersede sRGB. Pointer's cited dataset is a bounded empirical surface-colour dataset, not all physically possible colours.

# Prerequisites

- **Colour space** — Gamut is a property of a colour space.
- **D65 whitepoint** — sRGB uses D65; the gamut is defined relative to this white.

# Key Properties
1. The chromaticity triangle is a projection; the bounded sRGB gamut has three dimensions.
2. Valid Oklab/OkLCh coordinates can convert outside sRGB. Conversion is not gamut mapping.
3. Test destination linear RGB using a declared tolerance.
4. Wide gamut and HDR are distinct; the appropriate destination depends on task and output.
5. The Pointer dataset does not exhaust physically possible colours.

# Construction / Recognition

## To Construct/Create:
1. The sRGB gamut in Oklab is the image of the unit cube [0,1]³ in (R,G,B) space under the linear_srgb_to_oklab transform.
2. To check if an Oklab colour is within sRGB: convert to linear sRGB and verify all three channels are in [0, 1].

## To Identify/Recognise:
1. In the Luo-Rigg plots: the sRGB gamut appears as a bounded region inside the larger visible gamut boundary.
2. Colours outside sRGB: conversion to linear sRGB produces values < 0 or > 1 on at least one channel.

# Context & Application
- **Typical contexts**: Web and display work where sRGB is a relevant target; actual devices and host defaults vary.
- **Common applications**: Check target linear RGB after conversion, then select a mapping/rendering policy for out-of-gamut colours.

# Examples
**Example 1** (source report): Ottosson says a blue-fold constraint was added after an earlier Oklab version showed a local non-convex sRGB boundary. This local design history does not prove global convexity. (Section: “How Oklab was derived”)

**Example 2** (source description): The article describes Luo–Rigg plots of sRGB within a wider dataset/gamut comparison. Plot images were not independently inspected; this does not establish all visible colours. (Section: “Luo-Rigg dataset and full gamut”)

**Example 3** (source quote): The article says HSV does not handle colours outside sRGB in its described plot. Scope that statement to the cited model and data. (Section: “Luo-Rigg dataset and full gamut”)

# Relationships
## Builds Upon
- **Colour space** — Gamut is the representable subset under a specified space/device definition.
- **sRGB** — The primaries, transfer encoding and bounds define this destination gamut.

## Enables
- **Gamut mapping** — Out-of-gamut coordinates require an explicit destination mapping policy.
- **Oklab design** — The article reports a local sRGB boundary constraint in its model derivation; it does not establish global convexity.

## Related
- **D65 whitepoint** — sRGB uses a D65 reference.
- **XYZ colour space** — Gamut boundaries can be represented in chromaticity coordinates, which are a projection.

## Contrasts With
- **Wider gamuts** — P3/Rec.2020 have different primaries and bounds; they do not inherently supersede sRGB for every task or imply HDR.

# Common Errors
- **Error**: Treating a plotted triangle as the complete RGB gamut or inferring global convexity from one boundary constraint.
  **Correction**: State the projection and prove any global geometric claim separately.
- **Error**: Treating a valid coordinate as displayable in sRGB.
  **Correction**: Convert, test the destination gamut, then select a mapping/rendering policy.

# Common Confusions

- **Confusion**: sRGB gamut and sRGB colour space are the same thing.
  **Clarification**: The sRGB colour space includes a gamma encoding curve and whitepoint definition; the gamut is just the set of representable colours. The gamut can be described in other colour spaces (e.g., as a region in XYZ or Oklab).

# Source Reference

"How Oklab was derived" (gamut convexity constraint); "Luo-Rigg dataset and full gamut" (gamut slice in plots); HSV limitation note.

# Verification Notes
CSS Color 4 CRD 2026-10-09 §§13–14 distinguishes interpolation, gamut mapping and display. Pointer evidence is limited to its empirical dataset. No gamut map or browser render was tested here.
