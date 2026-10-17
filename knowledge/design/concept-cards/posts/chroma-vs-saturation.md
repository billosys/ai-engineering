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
Chroma is a model-specific colourfulness coordinate; saturation is an appearance term or a model parameter whose meaning depends on its definition. HSL/HSV saturation parameters are not interchangeable with CIE perceptual saturation.

# Core Definition
Ottosson describes HSL's parameter as roughly chroma relative to the most colourful colour at the same model lightness and hue, and notes that “relative chroma” is the more accurate name. HSV uses a different model-specific parameter. CIE chroma relates colourfulness to a similarly illuminated achromatic reference; CIE saturation relates it to the stimulus's own brightness. These terms should not be collapsed into a general formula. The prepared picker discussion compares orthogonal-chroma and orthogonal-saturation goals; these are design goals, not proof that either parameter is perceptually independent across all conditions. HSLuv's attributed rescaling and its gamut-shape tradeoff remain useful examples, not universal numerical tests.

# Prerequisites

- **HSL colour space** — The confusion arises specifically in HSL's naming convention
- **HSV colour space** — HSV Saturation is also a relative quantity but differently defined from HSL Saturation

# Key Properties
1. Oklab C = hypot(a,b) within that coordinate model; its perceptual interpretation is approximate.
2. CIE chroma and saturation use different reference relationships; neither yields a universal C/L rule.
3. HSL and HSV parameters named saturation have different model definitions and are not CIE perceptual saturation.
4. HSLuv's attributed saturation rescales chroma relative to an sRGB boundary; retain that as a model-specific comparison.
5. Picker goals such as holding chroma or saturation while changing other coordinates require explicit model definitions and validation.

# Construction / Recognition

## To Identify/Recognise:
1. Identify whether “saturation” means a CIE appearance term or a named HSL/HSV/HSLuv parameter.
2. For an HSL or HSV control, inspect its model formula; do not infer CIE saturation from the label.
3. The attributed HSLuv comparison concerns its chroma rescaling and gamut shape; it is not a universal test for perceptual smoothness.

# Context & Application

- **Typical contexts**: Colour model design, perceptual colour science, colour picker implementation, data visualisation colour scale design
- **Common applications**: Understanding what a "saturation" slider actually does in different tools; designing colour palettes where colourfulness should remain constant across lightness variations

# Examples

**Example 1** (from source): "Not the same as 'saturation' in HSV" — Ottosson makes explicit that HSL Saturation and HSV Saturation are different quantities sharing the same label.

**Example 2** (from source): HSLuv's "Saturation" is described as "based on chroma as defined in CIELChuv, but rescaled to be relative to the most saturated sRGB color of the same 'lightness' and 'hue'" — this rescaling is what makes HSLuv Saturation non-smooth: the uneven gamut shape causes abrupt chroma jumps when hue is changed at constant HSLuv Saturation.

# Relationships

## Builds Upon
- **Perceptual colour science** — The distinction is defined by how the visual system processes colour signals

## Enables
- **Orthogonal colour properties** — Recognising the distinction enables understanding why Orthogonal Chroma and Orthogonal Saturation are separate goals
- **Okhsl design** — Okhsl's saturation parameter is designed to be smoothly varying in a way that HSL's is not

## Related
- **Munsell colour system** — Uses Chroma (not Saturation) as an independent dimension
- **Okhsl / Okhsv** — Both provide saturation parameters that are defined carefully to avoid confusion

# Common Errors
- **Error**: Assuming HSL and HSV saturation are the same quantity.
  **Correction**: They are different model parameters.
- **Error**: Calling chroma absolute/context-free or saturation universally relative to maximum same-L/hue chroma.
  **Correction**: State the model or CIE appearance definition.
- **Error**: Treating a pale pastel, a fixed 50% lightness, or a universal maximum-chroma location as a general perceptual test.
  **Correction**: Remove these unverified tests; evaluate a defined model and context.

# Common Confusions
- **Confusion**: HSL/HSV saturation equals perceptual saturation or can be derived as C/L.
  **Clarification**: These are model-specific parameters; CIE defines appearance terms through their reference relationships.
- **Confusion**: Chroma is independent of lightness in every perceptual sense.
  **Clarification**: Oklab coordinates are distinct by construction, but perception and available gamut can depend on lightness and hue.

# Source Reference

"HSL" section under "Color spaces for color picking" and "What makes a good color picker?" section, Okhsv and Okhsl (Björn Ottosson).

# Verification Notes
This bounded consistency repair uses Ottosson's prepared picker discussion for HSL/HSV/HSLuv distinctions and CIE S 017:2020 terms 17-22-073/074. Existing source citation and header remain frozen. Other edges, questions and unrelated card claims were not reviewed or accepted.
