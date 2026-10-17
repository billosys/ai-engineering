---
concept: "Chroma vs Saturation (Colour Picker Context)"
slug: "chroma-vs-saturation"
category: "colour-theory"
subcategory: "colour-properties"
tier: "intermediate"
layer: "2-domain"
source: "Okhsv and Okhsl"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "HSL"
chapter_number: null
pdf_page: null
section: "Color spaces for color picking"
extraction_confidence: "high"
aliases:
  -
    - "saturation vs chroma"
    - "colorfulness"
prerequisites:
  - "hsl"
  - "hsv"
extends: []
related:
  - "orthogonal-colour-properties"
  - "okhsl"
  - "okhsv"
contrasts_with: []
answers_questions:
  - "What distinguishes chroma from saturation in a colour space?"
  - "What makes a colour picker perceptually well-designed?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition
In CIE appearance terminology, chroma relates colourfulness to the brightness of a similarly illuminated achromatic reference, while saturation relates it to the area’s own brightness. Oklab C and HSL/HSV “saturation” are model coordinates or parameters, not automatically those CIE attributes.

# Core Definition

Ottosson describes HSL saturation as roughly chroma relative to the most colourful colour at the same HSL lightness and hue, and says “relative chroma” is more accurate; HSV saturation has a different RGB-model definition. CIE defines saturation as colourfulness of an area judged in proportion to its brightness, and chroma as colourfulness judged in proportion to the brightness of a similarly illuminated area that appears grey, white or highly transmitting ([saturation, 17-22-073](https://cie.co.at/eilvterm/17-22-073); [chroma, 17-22-074](https://cie.co.at/eilvterm/17-22-074)). The entries' notes condition approximate constancy on viewing and luminance conditions; chroma's notes also distinguish related and unrelated colours and surface luminance factor. These appearance terms do not yield a universal formula for HSL/HSV saturation. Oklab C=hypot(a,b) is a model coordinate, not CIE chroma by itself. The picker article separately proposes orthogonal chroma and orthogonal saturation goals; those labels do not prove perceptual independence. HSLuv and the newer picker models provide specific construction tradeoffs, not general tests of colour appearance.

# Prerequisites

- **HSL colour space** — The confusion arises specifically in HSL's naming convention
- **HSV colour space** — HSV Saturation is also a relative quantity but differently defined from HSL Saturation

# Key Properties

1. Oklab C=hypot(a,b) is a coordinate formula within that model; its perceptual interpretation depends on the model and conditions.
2. CIE saturation relates colourfulness to an area's own brightness; CIE chroma uses the brightness of a similarly illuminated achromatic reference. Both terms are conditioned by their viewing definitions; neither gives a universal C/L conversion.
3. HSL and HSV saturation are distinct parameters derived from encoded RGB formulas.
4. HSLuv and Okhsl/Okhsv define their own mappings; do not treat the shared word “saturation” as interchangeability.
5. Independent numeric parameters, perceptual independence and even appearance steps are separate questions.

# Construction / Recognition

## To Identify/Recognise:

1. Identify whether “saturation” names a CIE appearance attribute or a particular model parameter.
2. For HSL/HSV, state the RGB encoding and formula; for Okhsl/Okhsv, state the Oklab-derived construction and output convention.
3. Do not infer perceptual smoothness or evenness from a parameter’s name or range.

# Context & Application

- **Typical contexts**: Colour model design, perceptual colour science, colour picker implementation, data visualisation colour scale design
- **Common applications**: Understanding what a "saturation" slider actually does in different tools; designing colour palettes where model-specific colourfulness coordinates are deliberately compared

# Examples

**Example 1** (from source): "Not the same as 'saturation' in HSV" — Ottosson makes explicit that HSL Saturation and HSV Saturation are different quantities sharing the same label.

**Example 2** (from source): HSLuv's "Saturation" is described as "based on chroma as defined in CIELChuv, but rescaled to be relative to the most saturated sRGB color of the same 'lightness' and 'hue'" — this rescaling is what makes HSLuv Saturation non-smooth: the uneven gamut shape causes a reported chroma variation when hue is changed at constant HSLuv Saturation; this is source-attributed and not a newly tested universal behavior.

# Relationships

## Builds Upon

- **Perceptual colour science** — CIE appearance terminology and RGB-model parameters need distinct definitions and reference conditions.

## Enables

- **Orthogonal colour properties** — Distinguishing chroma from saturation clarifies two separate proposed picker criteria.
- **Okhsl design** — The article’s saturation mapping is model-specific and should be explained separately from HSL/HSV saturation.

## Related

- **Munsell colour system** — Munsell Chroma is an HVC system coordinate, not a context-free absolute transferable measure.
- **Okhsl / Okhsv** — Both use model-specific saturation-like controls; the shared label does not imply interchangeability.

# Common Errors

**Error**: Treating HSL/HSV saturation as a CIE appearance measure or as C/L.
  **Correction**: Keep the model-specific formulas and CIE terminology distinct.

**Error**: Treating chroma as a context-free quantity or as a universal maximum at one lightness.
  **Correction**: State the coordinate system, reference conditions and gamut; perception and available chroma can vary with context, hue and lightness.

# Common Confusions

**Confusion**: A model with numerically separate coordinates has perceptually independent attributes.
  **Clarification**: Coordinate construction, basis geometry and perceived appearance are distinct. The article’s picker goals are proposals, not universal proofs.

# Source Reference

"HSL" section under "Color spaces for color picking" and "What makes a good color picker?" section, Okhsv and Okhsl (Björn Ottosson).

# Verification Notes

This full available-evidence review checked the card’s teaching and relationships against the prepared picker article, the accepted Slice17 Oklab/chroma endpoint, and CIE S 017:2020 entries 17-22-073/074 (definitions and notes) at https://cie.co.at/eilvterm/17-22-073 and https://cie.co.at/eilvterm/17-22-074. The bounded CSS/HTML/NCS sources were consulted only where relevant. Corrected and retained claims are scoped to their named model/source; unsupported universal tests and maxima were removed or qualified. Extraction-confidence metadata remains predecessor metadata and was not recalculated. The prepared text does not establish original capture fidelity; figures, inaccessible Munsell-owner material, browser behavior and accessibility behavior were not independently checked.
