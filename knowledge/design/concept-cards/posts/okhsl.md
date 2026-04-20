---
concept: Okhsl Colour Space
slug: okhsl
category: colour-theory
subcategory: colour-models
tier: advanced
layer: 2-domain
source: "Okhsv and Okhsl"
source_slug: posts
authors: "Bj\u00f6rn Ottosson"
chapter: "Okhsl"
chapter_number: null
pdf_page: null
section: "Introducing two new color spaces: Okhsv and Okhsl"
extraction_confidence: high
aliases:
  - ["Ok HSL"]
prerequisites:
  - hsl
  - colour-gamut
  - orthogonal-colour-properties
extends:
  - hsl
related:
  - okhsv
  - colour-picker-design-principles
contrasts_with:
  - hsl
  - okhsv
answers_questions:
  - "What distinguishes Okhsl from Okhsv, and when would you use each?"
  - "What makes a colour picker perceptually well-designed?"
rosetta_stone:
  - domain: music
    concept: "Equal temperament tuning"
    rating: rigorous
    note: "Okhsl achieves perceptual uniformity in colour the same way equal temperament achieves perceptual uniformity in pitch: equal numerical steps (slider increments) produce equal perceived differences, regardless of where on the scale you start."
---

# Quick Definition

Okhsl is a colour space designed by Bj\u00f6rn Ottosson as a perceptually-improved replacement for HSL, built on the Oklab colour space. It maps the sRGB gamut to a cylinder while achieving orthogonal lightness and hue \u2014 properties HSL lacks.

# Core Definition

Ottosson introduces Okhsl as part of a pair: "For consistency with the naming of Oklab, these new color spaces will be called Okhsl and Okhsv." Okhsl is derived from OkLCh (the cylindrical form of Oklab): "To derive Okhsl we also start with OkLCh. L_r and h are kept as is, with L_r referred to as l instead for consistency." The lightness L_r is a new perceptual lightness estimate introduced in the same post, which "closely matches the lightness estimate of CIELab overall." The saturation parameter s is constructed using three chroma reference values \u2014 C_0 (hue-independent, used for low-saturation colours), C_mid (an optimised smooth mid-range value), and C_max (the maximum chroma in the sRGB gamut for the given lightness and hue) \u2014 interpolated so that: at s=0 the slope matches C_0; at s=0.8 the value matches C_mid; at s=1.0 it reaches C_max. This construction keeps the interior of the colour space smooth while confining the gamut irregularity to the high-saturation edge. "Altogether this gives a model with a simple geometrical shape that has parameters for lightness and hue that closely match perception."

# Prerequisites

- **HSL colour space** \u2014 Okhsl is designed as a drop-in improvement for HSL pickers
- **Colour gamut** \u2014 The sRGB gamut shape drives the construction of C_0, C_mid, and C_max
- **Orthogonal colour properties** \u2014 Okhsl is designed to achieve Orthogonal Lightness and Orthogonal Hue

# Key Properties

1. Achieves Orthogonal Lightness (yes) and Orthogonal Hue (yes) \u2014 improvements over HSL (both no)
2. Uses a cylindrical shape identical to HSL in structure, making it a usable drop-in replacement
3. Saturation varies smoothly even where the gamut boundary is irregular, by using a three-point interpolation (C_0, C_mid, C_max)
4. Does NOT achieve Orthogonal Chroma (no) \u2014 the price paid for the simple cylindrical shape

# Construction / Recognition

## To Construct/Create:
1. Convert sRGB to linear sRGB
2. Convert to Oklab using the Oklab matrix transform
3. Compute hue h from atan2(b, a)
4. Apply the toe function to obtain L_r from L
5. Compute C_0, C_mid, C_max for the given h and L_r
6. Interpolate to obtain s from chroma C using the three-point scheme
7. The result is (h, s, l=L_r)

## To Identify/Recognise:
1. A constant-lightness hue ring in Okhsl shows visually uniform brightness across all hues (unlike HSL, which shows yellow as much brighter than blue)
2. Moving the saturation slider from 0 to 1 produces a smooth, gradual colour change without abrupt jumps (unlike HSLuv)

# Context & Application

- **Typical contexts**: Colour picker design, programmatic colour manipulation where lightness constancy matters, design system palette generation
- **Common applications**: Generating accessible colour palettes by stepping lightness uniformly; creating harmonious colour scales where all hues at the same Okhsl lightness appear equally bright

## Cross-Domain Connections

**Music \u2192 RIGOROUS**: Equal temperament divides the octave into 12 equal semitones so that every half-step sounds the same size regardless of starting pitch. Okhsl achieves the analogous goal for colour: equal-sized slider steps in lightness or hue produce equally-perceived colour differences regardless of starting position. Both are deliberate calibration systems designed to make a non-linear perceptual continuum behave linearly for practical use.

# Examples

**Example 1** (from source): "Altogether this gives a model with a simple geometrical shape that has parameters for lightness and hue that closely match perception. The model is quite different from regular HSL, in order to achieve a better lightness estimate. I believe Okhsl delivers a better overall compromise, and keeps many of the benefits of Lab-like color spaces, without the complexity of an irregular shape."

**Example 2** (from source \u2014 summary table): Okhsl achieves Orthogonal Lightness: yes; Orthogonal Hue: yes; Simple Geometrical Shape: yes; Varies Smoothly: yes; Orthogonal Chroma: no; Max Chroma at Edge: no.

# Relationships

## Builds Upon
- **Oklab** \u2014 Okhsl derives its hue and lightness from Oklab coordinates
- **HSL** \u2014 Okhsl was designed as a structural successor to HSL for picker use

## Enables
- **Perceptually uniform colour pickers** \u2014 Okhsl enables pickers where lightness feels consistent across hues
- **Accessible colour palette generation** \u2014 Uniform lightness enables all-hue palettes with consistent perceived contrast

## Related
- **Okhsv** \u2014 Sibling space optimised for a different set of tradeoffs (Value-based rather than Lightness-based)

## Contrasts With
- **HSL** \u2014 HSL has non-orthogonal lightness and hue; Okhsl corrects both
- **Okhsv** \u2014 Okhsv preserves maximum chroma at the edge (good for finding vivid colours); Okhsl prioritises orthogonal lightness (good for uniform brightness)
- **HSLuv** \u2014 HSLuv also attempts uniform lightness but fails on smooth saturation variation; Okhsl is smoother

# Common Errors

- **Error**: Assuming Okhsl Saturation values are directly comparable to HSL Saturation values.
  **Correction**: The two saturation parameters are differently constructed; they share a 0\u20131 range but represent different quantities.

# Common Confusions

- **Confusion**: Okhsl and Okhsv are the same space with a different axis name.
  **Clarification**: They are distinct spaces with different constructions. Okhsl prioritises orthogonal lightness (good for creating palettes with consistent perceived brightness); Okhsv preserves the HSV-style "value" axis where the most vivid colours appear at the edge at V=1.

# Source Reference

"Okhsl" and "Introducing two new color spaces: Okhsv and Okhsl" sections, Okhsv and Okhsl (Bj\u00f6rn Ottosson).

# Verification Notes

- Definition source: Direct quotes and close paraphrase from Ottosson
- Confidence rationale: High \u2014 Okhsl is defined, derived, and fully documented in source including C++ implementation
- Uncertainties: The saturation construction involves an optimised polynomial (C_mid); details require reference to source code
- Cross-reference status: Not present in Drasner source
- Rosetta Stone check: Music/equal-temperament mapping added as rigorous
- OCR issues: Mathematical notation rendered via KaTeX; cleaned for extraction
