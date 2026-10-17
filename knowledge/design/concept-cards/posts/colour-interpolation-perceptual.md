---
concept: "Colour Interpolation (Perceptual)"
slug: "colour-interpolation-perceptual"
category: "colour-theory"
subcategory: "colour operations"
tier: "intermediate"
layer: "2-domain"
source: "A Perceptual Color Space for Image Processing"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "Blending colors"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "high"
aliases: []
prerequisites:
  - "oklab"
  - "perceptual-uniformity"
  - "oklab-conversion"
extends:
  - "perceptual-uniformity"
related:
  - "chroma-perceptual"
  - "lightness-perceptual"
  - "colour-space-comparison"
contrasts_with: []
answers_questions:
  - "How do you construct a palette that changes lightness uniformly across hues?"
  - "What makes a colour space perceptually uniform, and why does it matter for design?"
rosetta_stone:
  -
    domain: "music"
    concept: "Glissando / pitch slide in equal temperament"
    rating: "loose"
    note: "Loose analogy only: equal-tempered frequency ratios and fitted colour models are different mathematics; neither establishes universal equal auditory or visual distance."
css_implementation:
  -
    property: "background"
    example: "background: linear-gradient(in oklab, red, blue);"
    support: "experimental"
  -
    property: "background"
    example: "background: linear-gradient(in oklch, red, blue);"
    support: "baseline"
---

# Quick Definition
Colour interpolation computes a path in a selected representation and host-defined interpolation space. Cartesian Oklab and polar OkLCh interpolation trace different paths; approximate uniformity is not a guarantee of even appearance.

# Core Definition
Ottosson describes even transitions as a design requirement and illustrates selected blends. For Cartesian Oklab, component-wise lerp is p(t)=(1−t)p₀+t p₁; only t=0.5 is the arithmetic midpoint. In OkLCh, hue is angular and needs an explicit path rule; hue is powerless at C=0. Results depend on endpoints, interpolation space, hue rule, alpha treatment, gamut mapping and rendering. Encoded-sRGB interpolation is a valid selected or legacy method; a different space produces a different path, not an intrinsically correct one.

# Prerequisites

- **Oklab** — The interpolation is performed in Oklab coordinates.
- **Perceptual uniformity** — An approximate model property can inform a chosen interpolation path, but it is not required for interpolation to be mathematically defined. Compare the actual rendered result.
- **Oklab conversion** — For the article’s Oklab example, convert endpoints into Oklab and convert to the selected output representation. Other spaces and output targets are also valid.

# Key Properties
1. Cartesian Oklab and polar OkLCh interpolation are not interchangeable.
2. Only t=0.5 is the arithmetic midpoint.
3. State degree/radian handling, hue wrap choice, powerless hue at C=0 and alpha behavior where relevant.
4. CSS host syntax selects interpolation space; an `oklab()` endpoint or keyframe alone does not instruct a gradient's interpolation space.
5. The article's Photoshop/browser adoption claim is its dated 2025 report, not a current support test.

# Construction / Recognition

## To Construct/Create:
1. Convert endpoints into the intended space and apply component-wise lerp for Cartesian Oklab.
2. For OkLCh, specify hue direction/wrap and handle powerless hue.
3. Apply the host's alpha rule, convert to the destination and check gamut/rendering.

## To Identify/Recognise:
1. Identify interpolation space, hue rule, alpha behavior and endpoints.
2. Compare the rendered samples for the use case; do not infer universal evenness from a space name.

# Context & Application
- **Typical contexts**: CSS gradients and colour tools when a host permits explicit interpolation-space selection.
- **Common applications**: `linear-gradient(in oklab, red, blue)` explicitly requests Oklab interpolation; support depends on the host and was not tested here.

## Cross-Domain Connections
**Music → LOOSE analogy**: Numeric colour interpolation and musical interval spacing are different operations and perceptual questions. Neither an equal-tempered ratio nor a fitted colour model proves equal auditory or visual distance.

# Examples
**Example 1** (source description): Ottosson reports selected white/blue blend comparisons. The plot was not visually inspected; this claim is limited to the article's stated endpoints and models. (Section: “Blending colors”)

**Example 2** (source description): The article describes a constant-L/C Oklab hue sweep and HSV comparison. It is not a universal guarantee and the image was not independently inspected. (Section: “Comparing Oklab to HSV”)

# Relationships
## Builds Upon
- **Perceptual uniformity** — An approximate goal relevant to a chosen path.
- **Oklab** — One possible host-selected interpolation space.

## Enables
- **Gradient design** — Explicit syntax documents the selected path.

## Related
- **Chroma (perceptual)** — C may be held or varied as a coordinate.
- **Lightness (perceptual)** — L may be held or varied as a coordinate.

## Contrasts With
- **sRGB interpolation** — A different valid path; compare actual results for the endpoints and host.

# Common Errors
- **Error**: Claiming Oklab always gives even transitions, or that encoded-sRGB interpolation is intrinsically wrong.
  **Correction**: Treat space choice as path selection and inspect the actual rendered result.
- **Error**: Using a colour endpoint as a gradient-space instruction.
  **Correction**: Select the host interpolation space explicitly, for example `linear-gradient(in oklab, red, blue)`.
- **Error**: Interpolating hue without a wrap rule or handling C=0.
  **Correction**: State the angular path and powerless-hue behavior.

# Common Confusions
- **Confusion**: Oklab is universally superior to CIELAB or sRGB interpolation.
  **Clarification**: The result depends on task, host, endpoints and rendering; selected article examples are not universal.

# Source Reference

"Blending colors"; requirements list in "Motivation and derivation of Oklab" (blending requirement); "Comparing Oklab to HSV".

# Verification Notes
Ottosson's blend examples are attributed descriptions; embedded plots were not visually inspected. CSS Color 4 CRD 2026-10-09 §§13.1–13.5 and 14.1.6 specifies host interpolation, hue and alpha behavior; it is a work-in-progress Candidate Recommendation Draft. No current browser/Photoshop support test is claimed.
