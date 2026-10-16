---
concept: "CSS mix-blend-mode (Colour Blend Modes)"
slug: "mix-blend-mode"
category: "colour-theory"
subcategory: "colour-effects"
tier: "intermediate"
layer: "3-implementation"
source: "Working With Colors Guide"
source_slug: "posts"
authors: "Sarah Drasner"
chapter: "Other Nice Color Effects / Mix Blend Modes and Background Blend Modes"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "high"
aliases:
  -
    - "blend modes"
    - "mix-blend-mode"
    - "background-blend-mode"
    - "CSS blending"
prerequisites:
  - "rgb-colour-model"
  - "additive-colour-mixing"
extends: []
related:
  - "fecolormatrix"
contrasts_with: []
answers_questions:
  - "How does CSS mix-blend-mode implement colour blending mathematically?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Pointwise operations on bounded functions"
    rating: "structural"
    note: "Separable blend modes apply a component-wise function to source and backdrop colour components. Non-separable modes operate on colour relationships across components; blending is followed by alpha compositing."
---

# Quick Definition

CSS `mix-blend-mode` selects a blend function between an element’s source colour and its backdrop. The blend result then participates in alpha compositing. Separable modes such as multiply and screen use component-wise formulas; hue, saturation, color and luminosity are non-separable. The available mode set is defined by the specification, not a fixed count in this card.

# Core Definition

Drasner explains: "If you've used layer effects in Photoshop, you're probably familiar with mix blend modes... Mix and background blend modes composite two different layered images together, and there are 16 modes available." This is the prepared article’s count, not a current exhaustive count asserted by this card. The terminology distinguishes the source (top element) from the destination (bottom element) and the backdrop (the already-composited content behind the source). The specification uses backdrop colour in the blend function, then applies compositing. She provides examples and shorthand formulas: multiply as `destination × source`, and a prepared-source line calling `A+B−1` “Linear.” That name is not a CSS blend-mode value, and the expression alone is not a complete blend-and-composite algorithm. Color-burn also requires its defined clipped branches.

# Prerequisites

- **RGB colour model** — Blend modes operate on normalised RGB channel values (0.0–1.0)
- **Additive colour mixing** — The multiply mode in particular produces subtractive-like effects from additive components

# Key Properties

1. Blend modes include separable and non-separable functions; consult the current specification for the defined values
2. Multiply: `destination × source` — darkens (analogous to subtractive mixing)
3. Screen: `1 − (1−A)(1−B)` — lightens (analogous to additive mixing)
4. Separable blend functions operate per component on normalized colour values; non-separable modes depend on relationships across components

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

**Mathematics → STRUCTURAL**: Separable modes such as multiply and screen apply a component-wise function to source and backdrop channels. Non-separable modes such as hue, saturation, color and luminosity operate on relationships among colour components; the separable arithmetic analogy does not cover them.

# Examples

**Example 1** (prepared-source shorthand): Drasner writes multiply as `destination × source = backdrop`. In the blend-function stage, multiplying opaque red `(1, 0, 0)` and opaque blue `(0, 0, 1)` produces black `(0, 0, 0)` because every channel product is zero; the blend result then enters the separate compositing stage.

**Example 2** (from source): Drasner gives the abbreviated color-burn expression `1−(1−B)÷A`. For normalized backdrop `Cb` and source `Cs`, the defined separable blend function is: if `Cb==1`, return 1; else if `Cs==0`, return 0; otherwise return `1−min(1,(1−Cb)/Cs)`. This blend function is followed by, and is distinct from, alpha compositing.

# Relationships

## Builds Upon
- **RGB colour model** — Separable modes use component functions; non-separable modes use relationships among colour components

## Enables
- **Complex visual effects** — Blend modes can be combined in layered compositions; resulting appearance depends on backdrop, alpha, stacking and isolation

## Related
- **feColorMatrix** — An SVG filter that provides similar colour manipulation capabilities with matrix operations

# Common Errors

- **Error**: Expecting mix-blend-mode to work if the parent has `overflow: hidden` or `isolation: isolate`.
  **Correction**: `isolation: isolate` makes the element a group whose descendants blend internally; the group is then composited with the external backdrop as a unit. `overflow` controls clipping/scrolling and does not itself mean isolation.

# Common Confusions

- **Confusion**: mix-blend-mode and background-blend-mode are the same.
  **Clarification**: `mix-blend-mode` blends an element against other elements behind it; `background-blend-mode` blends multiple background layers within a single element.

# Source Reference

"Mix Blend Modes and Background Blend Modes" section under "Other Nice Color Effects," Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Current model: [Compositing and Blending 1 §§3.4.1–3.4.3, 5.1, 7, 10.1–10.3](https://www.w3.org/TR/compositing-1/) distinguishes backdrop, blend function, alpha compositing, separable/non-separable modes and isolation. Color-burn uses defined clipped branches.

- Definition source: Direct quotes from Drasner, including blend mode formulas
- Confidence rationale: Medium — Drasner supplies examples, but some terminology and formulas need the normative qualification above
- Uncertainties: Drasner notes 16 modes are available but does not list all 16; source coverage is overview-level
- Cross-reference status: Not in Ottosson source
- Rosetta Stone check: Mathematics/pointwise-operations mapping added as structural
- OCR issues: None significant
