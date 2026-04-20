---
concept: CSS mix-blend-mode (Colour Blend Modes)
slug: mix-blend-mode
category: colour-theory
subcategory: colour-effects
tier: intermediate
layer: 3-implementation
source: "Working With Colors Guide"
source_slug: posts
authors: "Sarah Drasner"
chapter: "Other Nice Color Effects / Mix Blend Modes and Background Blend Modes"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - ["blend modes", "mix-blend-mode", "background-blend-mode", "CSS blending"]
prerequisites:
  - rgb-colour-model
  - additive-colour-mixing
extends:
  - []
related:
  - fecolormatrix
contrasts_with:
  - []
answers_questions:
  - "How does CSS mix-blend-mode implement colour blending mathematically?"
rosetta_stone:
  - domain: mathematics
    concept: "Pointwise operations on bounded functions"
    rating: structural
    note: "Blend mode formulas apply arithmetic operations (multiplication, addition, subtraction, division) channel-by-channel to pixel values treated as normalised floats [0,1]. Multiply is literally f(a,b) = a \u00d7 b. The structural analogy to pointwise function composition is exact."
---

# Quick Definition

CSS `mix-blend-mode` composites the colours of overlapping HTML/CSS elements using one of 16 mathematical blend modes inherited from photo-editing software, where each mode applies a per-channel formula to the source (top) and destination (bottom) colours.

# Core Definition

Drasner explains: "If you've used layer effects in Photoshop, you're probably familiar with mix blend modes... Mix and background blend modes composite two different layered images together, and there are 16 modes available." The terminology: "The top image or color is called the source, and the bottom layer is called the destination. The area between the two is where the blending magic happens and is called the backdrop. We're mixing both according to fairly simple mathematical formulas." She provides the key examples: "the color formulas for the blend modes depend on the type of effect used. For instance, multiply is `destination \u00d7 source = backdrop`. Other effects are variations of simple math using subtraction, multiplication, addition, and division. Linear is `A+B\u22121`, while Color Burn is `1\u2212(1\u2212B)\u00f7A`."

# Prerequisites

- **RGB colour model** \u2014 Blend modes operate on normalised RGB channel values (0.0\u20131.0)
- **Additive colour mixing** \u2014 The multiply mode in particular produces subtractive-like effects from additive components

# Key Properties

1. 16 available blend modes including: normal, multiply, screen, overlay, darken, lighten, color-dodge, color-burn, hard-light, soft-light, difference, exclusion, hue, saturation, color, luminosity
2. Multiply: `destination \u00d7 source` \u2014 darkens (analogous to subtractive mixing)
3. Screen: `1 \u2212 (1\u2212A)(1\u2212B)` \u2014 lightens (analogous to additive mixing)
4. Operates per channel in normalised [0,1] space

# Construction / Recognition

## To Construct/Create:
1. Stack two elements using CSS positioning (or use background-blend-mode for multiple backgrounds on one element)
2. Apply `mix-blend-mode: [mode]` to the top element
3. Modes: multiply, screen, overlay, difference are the most commonly used

## To Identify/Recognise:
1. Elements with `mix-blend-mode` set to anything other than `normal`
2. Visual appearance that shows both layers merged rather than one covering the other

# Context & Application

- **Typical contexts**: Photo effects in CSS, design overlays, creative UI treatments, Instagram-filter-style effects
- **Common applications**: Creating colour duotone effects; darkening or lightening images with a colour overlay; combining patterns

## Cross-Domain Connections

**Mathematics \u2192 STRUCTURAL**: Blend mode formulas are pointwise arithmetic operations on colour channel values treated as real numbers in [0,1]. Multiply is exactly f(a,b) = a\u00b7b; Screen is f(a,b) = 1\u2212(1\u2212a)(1\u2212b). These are the same operations as pointwise function multiplication and complement-multiplication in analysis \u2014 the structural mapping is precise, though colour blend modes are defined discretely per pixel.

# Examples

**Example 1** (from source): "multiply is `destination \u00d7 source = backdrop`" \u2014 the canonical blend mode; multiplying a red (1, 0, 0) by a blue (0, 0, 1) produces black (0, 0, 0) because all channels multiply to 0.

**Example 2** (from source): "Color Burn is `1\u2212(1\u2212B)\u00f7A`" \u2014 a more complex formula demonstrating that blend modes can be non-trivial mathematical operations.

# Relationships

## Builds Upon
- **RGB colour model** \u2014 Blend modes operate on per-channel float values

## Enables
- **Complex visual effects** \u2014 Chaining multiple blend modes (as mentioned by Drasner referencing Robin) creates advanced compositing effects

## Related
- **feColorMatrix** \u2014 An SVG filter that provides similar colour manipulation capabilities with matrix operations

# Common Errors

- **Error**: Expecting mix-blend-mode to work if the parent has `overflow: hidden` or `isolation: isolate`.
  **Correction**: `isolation: isolate` on a parent creates a new stacking context that prevents the child's blend mode from compositing with elements outside the isolated container.

# Common Confusions

- **Confusion**: mix-blend-mode and background-blend-mode are the same.
  **Clarification**: `mix-blend-mode` blends an element against other elements behind it; `background-blend-mode` blends multiple background layers within a single element.

# Source Reference

"Mix Blend Modes and Background Blend Modes" section under "Other Nice Color Effects," Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Definition source: Direct quotes from Drasner, including blend mode formulas
- Confidence rationale: High \u2014 formulas and terminology explicitly provided
- Uncertainties: Drasner notes 16 modes are available but does not list all 16; source coverage is overview-level
- Cross-reference status: Not in Ottosson source
- Rosetta Stone check: Mathematics/pointwise-operations mapping added as structural
- OCR issues: None significant
