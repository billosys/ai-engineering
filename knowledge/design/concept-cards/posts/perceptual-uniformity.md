---
concept: "Perceptual Uniformity (Colour)"
slug: "perceptual-uniformity"
category: "visual-perception"
subcategory: "colour psychophysics"
tier: "foundational"
layer: "0-perception"
source: "A Perceptual Color Space for Image Processing"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "Motivation and derivation of Oklab"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "high"
aliases: []
prerequisites: []
extends: []
related:
  - "colour-space"
  - "oklab"
  - "colour-space-comparison"
contrasts_with: []
answers_questions:
  - "What makes a colour space perceptually uniform, and why does it matter for design?"
  - "What is the mathematical relationship between perceptual uniformity in colour and equal temperament in music?"
rosetta_stone:
  -
    domain: "music"
    concept: "Equal temperament (12-TET)"
    rating: "loose"
    note: "Loose analogy only: equal-tempered frequency ratios and fitted colour models are different mathematics; neither establishes universal equal auditory or visual distance."
  -
    domain: "mathematics"
    concept: "Metric space with uniform distance function"
    rating: "structural"
    note: "An ideal metric would correspond to perceived difference under stated conditions; practical fitted models only approximate that correspondence."
css_implementation:
  -
    property: "color"
    example: "color: oklch(70% 0.15 180);"
    support: "baseline"
---

# Quick Definition
Perceptual uniformity is an ideal in which coordinate differences correspond consistently to perceived differences under stated conditions; practical colour models only approximate it.

# Core Definition
A uniform colour space aims to make equal coordinate differences correspond to equal perceived differences. Actual agreement depends on model, dataset, viewing conditions, display and gamut. Oklab is a fitted approximation, not an exact or universal law. Its coordinates are designed to reduce cross-effects, but that goal does not make axes perceptually independent in every context. A constant-L/C hue sweep is an example construction; it must be checked for destination gamut and rendering.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Uniformity is an ideal/model property assessed against specified observations and conditions.
2. Oklab approximates perceptual behaviour; equal numerical distance is not guaranteed to mean equal appearance everywhere.
3. Model-coordinate independence is a design goal, not a universal perceptual result.
4. A hue sweep holds L and C constant while varying h; output gamut and context affect the result.

# Construction / Recognition

## To Construct/Create:
1. Name the colour model and viewing/output conditions.
2. Select equal coordinate increments as a model-based candidate.
3. Render/check the result and compare the relevant colour differences; avoid a universal-equality claim.

## To Identify/Recognise:
1. Ask which dataset, difference metric and conditions support a uniformity claim.
2. For a hue sweep, identify constant L and C with varying hue, then check actual gamut/rendering.
3. Numerical equality alone does not establish equal visual appearance.

# Context & Application
- **Typical contexts**: Comparing a model against specified perceptual data and conditions.
- **Common applications**: Coordinate-based candidates for grey ramps, hue sweeps or interpolation, followed by gamut and rendered-pair checks; these do not guarantee unchanged hue, lightness or saturation.

## Cross-Domain Connections
**Music → LOOSE analogy**: A 12-tone equal-tempered frequency ratio and a fitted three-dimensional colour transform are different mathematics. Neither establishes universal equal auditory or visual distance. **Mathematical operation**: The stated coordinate calculation can be rigorous as arithmetic while its perceptual interpretation remains approximate.

# Examples
**Example 1** (source description): Ottosson describes an Oklab hue sweep with constant L/C and varying h, alongside an HSV comparison. This is attributed to that example; the image was not independently inspected, and it is not a universal guarantee. (Section: “Comparing Oklab to HSV”)

# Relationships
## Builds Upon
- **Colour space** — Uniformity is assessed for a model under conditions.

## Enables
- **Colour interpolation** — Approximate uniformity may inform path selection but does not guarantee rendered evenness.
- **Palette construction** — Coordinates provide candidates for later gamut, rendering and pair checks.

## Related
- **Oklab** — A fitted approximate model.
- **Colour-space-comparison** — The article reports dataset- and metric-specific results.

## Contrasts With
- **Nonuniform models** — Equal coordinate steps may not correspond consistently to observed differences.

# Common Errors
- **Error**: Saying constant L/C appears equally light/colourful across every hue or display.
  **Correction**: Describe the constant-L/C, varying-h hue-sweep construction and qualify the appearance claim.
- **Error**: Treating a loose music analogy as a mathematical or perceptual equivalence.
  **Correction**: State the literal operation separately from its limited analogy.

# Common Confusions
- **Confusion**: A perceptually motivated space makes every equal coordinate step visually equal.
  **Clarification**: Uniformity is an approximate model fit assessed under conditions; it is not an all-context guarantee.

# Source Reference

"Motivation and derivation of Oklab" and "Comparison with other color spaces" sections; no page numbers (web article).

# Verification Notes
The uniformity definition and Oklab scope were checked against CSS Color 4 CRD 2026-10-09 §9.2 and Ottosson's stated model goals. Music comparisons remain loose analogies; no psychophysical investigation was performed.
