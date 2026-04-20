---
concept: Okhsv Colour Space
slug: okhsv
category: colour-theory
subcategory: colour-models
tier: advanced
layer: 2-domain
source: "Okhsv and Okhsl"
source_slug: posts
authors: "Bj\u00f6rn Ottosson"
chapter: "Okhsv"
chapter_number: null
pdf_page: null
section: "Introducing two new color spaces: Okhsv and Okhsl"
extraction_confidence: high
aliases:
  - ["Ok HSV"]
prerequisites:
  - hsv
  - colour-gamut
  - orthogonal-colour-properties
extends:
  - hsv
related:
  - okhsl
  - colour-picker-design-principles
contrasts_with:
  - hsv
  - okhsl
answers_questions:
  - "What distinguishes Okhsl from Okhsv, and when would you use each?"
  - "What makes a colour picker perceptually well-designed?"
rosetta_stone:
  - domain: music
    concept: "Equal temperament tuning"
    rating: rigorous
    note: "Like Okhsl, Okhsv makes perceptual hue steps uniform across the hue circle, analogous to equal temperament making semitone intervals perceptually equal across pitch registers."
---

# Quick Definition

Okhsv is a colour space designed by Bj\u00f6rn Ottosson as a perceptually-improved replacement for HSV, built on the Oklab colour space. It retains HSV's cylindrical shape and its "max chroma at edge" property while correcting HSV's severe hue distortions.

# Core Definition

Ottosson derives Okhsv from OkLCh: "To derive Okhsv, we will start with OkLCh, use its estimate for hue, h, as is and introduce s and v parameters that are calculated based on lightness, L_r, and chroma, C." The construction remaps the sRGB gamut cross-sections (which are triangular in OkLCh space) into a square by stretching the lower part of the triangle. The key step locates the "cusp" of each hue's triangular cross-section \u2014 the point of maximum chroma \u2014 and maps it to the corner (s=1, v=1). After this remapping, a small curve at the top of the triangle is removed by scaling v. An additional adjustment makes saturation more uniform for low-saturation colours. The result is "a new model with a simple geometrical shape and a hue parameter that closely matches perception. Overall the space will be very familiar to someone who is used to HSV, but with improved perceptual uniformity." Okhsv can also be converted to HWB (hue, whiteness, blackness) form using the relationships: w = (1-s)v and b = 1-v.

# Prerequisites

- **HSV colour space** \u2014 Okhsv is designed as a structural successor to HSV
- **Colour gamut** \u2014 The triangular cross-sections of the sRGB gamut in OkLCh drive the construction
- **Orthogonal colour properties** \u2014 Okhsv is designed to achieve Orthogonal Hue

# Key Properties

1. Achieves Orthogonal Hue (yes) and Simple Geometrical Shape (yes) \u2014 same as HSV, but with perceptual hue accuracy
2. Achieves Max Chroma at Edge (yes) \u2014 the most vivid colour for any hue is at s=1, v=1
3. Does NOT achieve Orthogonal Lightness (no) \u2014 the cusp varies in lightness across hues
4. Saturation is adjusted for low-saturation uniformity: "This makes it easier to compare saturation values for different colors, when saturation is low"

# Construction / Recognition

## To Construct/Create:
1. Convert sRGB to Oklab
2. Compute chroma C and hue h from Oklab a,b components
3. Find the cusp (L_cusp, C_cusp) for the given hue
4. Compute L_r using the toe function
5. Remap the triangular gamut cross-section to a square to obtain s and v
6. Apply a final v-scaling to remove the curved top
7. Apply low-saturation uniformity adjustment to s

## To Identify/Recognise:
1. A constant-v horizontal band in Okhsv shows equal perceived brightness across hues (much better than HSV)
2. The most saturated version of any hue always appears at the top-right corner of the picker square

# Context & Application

- **Typical contexts**: Colour picker design for applications where finding vivid/saturated colours is important, digital painting, graphic design tools
- **Common applications**: Selecting the most vivid colour for a given hue; adjusting brightness of a colour while preserving its saturation relative to maximum

## Cross-Domain Connections

**Music \u2192 RIGOROUS**: Okhsv's perceptually uniform hue is analogous to equal temperament: stepping the hue angle by equal amounts produces equally-perceived hue changes, just as equal-tempered semitones produce equally-perceived pitch intervals.

# Examples

**Example 1** (from source): The series of images showing the OkLCh cross-section for yellow, blue, and magenta hues being progressively remapped \u2014 from irregular triangle to square \u2014 illustrates the Okhsv construction process visually.

**Example 2** (from source \u2014 summary table): Okhsv achieves: Orthogonal Hue: yes; Simple Geometrical Shape: yes; Max Chroma at Edge: yes; Varies Smoothly: yes; Orthogonal Lightness: no; Orthogonal Chroma: no; Varies Evenly: no.

# Relationships

## Builds Upon
- **Oklab** \u2014 Okhsv derives hue from Oklab's perceptually uniform hue angle
- **HSV** \u2014 Okhsv is a structural drop-in for HSV, retaining its shape and conventions

## Enables
- **Perceptual HSV-style pickers** \u2014 Enables pickers that feel like HSV but with correct hue representation

## Related
- **Okhsl** \u2014 Sibling space prioritising orthogonal lightness instead of max-chroma-at-edge
- **Okhwb** \u2014 A whiteness/blackness reparameterisation of Okhsv, analogous to HWB for HSV

## Contrasts With
- **HSV** \u2014 HSV has severe hue distortions (purple shift in deep blues); Okhsv corrects these
- **Okhsl** \u2014 Okhsl achieves orthogonal lightness (uniform brightness across hues at constant L); Okhsv does not

# Common Errors

- **Error**: Treating Okhsv Value as equivalent to perceived luminance.
  **Correction**: Value in Okhsv, like in HSV, is not perceptual luminance \u2014 it is a normalised position within the gamut triangle remapped to [0,1]. Yellow's cusp is at high perceptual lightness; blue's is at low perceptual lightness.

# Common Confusions

- **Confusion**: Okhsv corrects all of HSV's problems.
  **Clarification**: Okhsv corrects HSV's hue distortions (the most significant problem) but does not achieve Orthogonal Lightness. The lightness axis still changes with hue. Use Okhsl if consistent perceived brightness across hues is required.

# Source Reference

"Okhsv" section under "Introducing two new color spaces: Okhsv and Okhsl," Okhsv and Okhsl (Bj\u00f6rn Ottosson).

# Verification Notes

- Definition source: Direct quotes and close paraphrase from Ottosson
- Confidence rationale: High \u2014 Okhsv is defined, derived, and documented with C++ implementation in source
- Uncertainties: The cusp-finding algorithm references a separate post on sRGB gamut clipping
- Cross-reference status: Not present in Drasner source
- Rosetta Stone check: Music/equal-temperament mapping added as rigorous
- OCR issues: KaTeX math notation cleaned for extraction
