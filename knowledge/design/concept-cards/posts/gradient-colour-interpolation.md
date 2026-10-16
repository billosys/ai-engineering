---
concept: "Gradient Colour Interpolation (CSS)"
slug: "gradient-colour-interpolation"
category: "colour-theory"
subcategory: "colour-effects"
tier: "intermediate"
layer: "3-implementation"
source: "Working With Colors Guide"
source_slug: "posts"
authors: "Sarah Drasner"
chapter: "Color Properties / Gradients"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "medium"
aliases:
  -
    - "CSS gradients"
    - "linear-gradient"
    - "radial-gradient"
    - "color stops"
    - "SVG gradient"
prerequisites:
  - "rgb-colour-model"
  - "additive-colour-mixing"
extends: []
related:
  - "css-rgba"
  - "hsl-css-syntax"
contrasts_with: []
answers_questions: []
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Linear interpolation (lerp)"
    rating: "rigorous"
    note: "For each component CSS interpolates linearly in a selected gradient colour space, the result follows lerp exactly; hue and alpha follow their specified rules. This mathematical identity does not imply physical light addition or describe gradient compositing."
---

# Quick Definition

CSS gradients define geometry and colour stops; CSS Images specifies an optional interpolation method for the gradient line, using CSS Color interpolation rules. Name a colour space for numerical examples; do not assume a universal default across syntax, specifications or implementations.

# Core Definition

Drasner explains: "Linear gradients work by designating a direction. From/to (depending on the browser prefix) top, bottom, left, right, degrees, or radial-gradients. We then specify color stops and the color we want at each stop. These can accept transparency too." She also covers SVG gradients: "Gradients are similarly easy to create in SVG. We define a block that you reference with an id." Her SVG example:

```xml
<linearGradient id="Gradient">
  <stop id="stop1" offset="0" stop-color="white" stop-opacity="0" />
  <stop id="stop2" offset="0.3" stop-color="black" stop-opacity="1" />
</linearGradient>
```

She notes gradients "support opacity so we can have some nice effects and layer effects like animate them as a mask." She also mentions gradient text in WebKit.

# Prerequisites

- **RGB colour model** — Intermediate gradient colours are computed by interpolating RGB channel values
- **Additive colour mixing** — The interpolation space is a selected CSS colour space; sRGB components are encoded and are not physical light-addition values

# Key Properties

1. Colour stops specify a colour and an optional position (0%–100% or 0.0–1.0)
2. Intermediate colours follow the selected interpolation space and method; name the space for numerical results
3. CSS supports `linear-gradient()`, `radial-gradient()`, and `conic-gradient()` as gradient types
4. CSS Color interpolation premultiplies non-opaque colours by alpha before interpolating; this avoids treating hidden transparent RGB components as visible colour
5. CSS Images defines gradient syntax and delegates colour interpolation to CSS Color; the current editor draft is not browser-support evidence

# Construction / Recognition

## To Construct/Create:
1. Use `background: linear-gradient(direction, color-stop-1, color-stop-2, ...)`
2. Direction: `to right`, `to bottom`, `45deg`, etc.
3. Colour stops: any CSS colour value optionally followed by a position
4. Optionally add explicit positions: `linear-gradient(to right, red 0%, blue 50%, green 100%)`

## To Identify/Recognise:
1. `linear-gradient()`, `radial-gradient()`, `conic-gradient()` in a `background` property
2. The classic "hue mudding" in the middle of a gradient between complementary colours (e.g. red to cyan produces grey in the middle in sRGB interpolation)

# Context & Application

- **Typical contexts**: CSS backgrounds, SVG fills, UI decoration, image masks, colour scales in data visualisation
- **Common applications**: Background gradients; gradient text effects; creating smooth colour transitions between sections; SVG gradient fills for icons or illustrations

## Cross-Domain Connections

**Mathematics → STRUCTURAL**: Within a selected colour space, interpolation varies components between stops according to the specified method. Hue handling and non-opaque colours have additional rules, including premultiplied alpha; this does not imply physical light addition or perceptual uniformity.

# Examples

**Example 1** (from source — SVG): The `<linearGradient>` with stops from white (opacity 0) at offset 0 to black (opacity 1) at offset 0.3, demonstrating opacity interpolation in an SVG gradient.

**Example 2** (from source): Drasner references using gradients "as a mask" and combined with animation — demonstrating gradients as dynamic compositing elements, not just static fills.

# Relationships

## Builds Upon
- **RGB colour model** — Interpolation operates on RGB channel values

## Enables
- **Colour scale design** — Gradient interpolation is the foundation of continuous colour scales in data visualisation

## Related
- **CSS rgba()** — Used in gradient stops for transparency
- **feColorMatrix** — An alternative way to perform colour transformations on gradient-filled SVG elements

# Common Errors

- **Error**: Expecting a gradient between red and green to pass through yellow in the middle.
  **Correction**: In explicitly named sRGB interpolation, opaque red and green produce midpoint `(0.5, 0.5, 0, 1)` in normalized components. Other interpolation spaces produce different paths; no space guarantees a perceptually perfect rainbow.

# Common Confusions

- **Confusion**: Gradient geometry determines its colour interpolation.
  **Clarification**: The gradient line and stop positions define geometry; interpolation space and path are separate choices.

# Source Reference

"Gradients" section under "Color Properties," Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Gradient grammar and interpolation: [CSS Images 4 §§3.1, 3.5.2](https://drafts.csswg.org/css-images-4/) delegates interpolation to CSS Color 4 §§13.1–13.4; the gradient line uses premultiplied alpha. CSS Images 4 is an Editor’s Draft dated 2026-10-08, not browser-support evidence.

- Definition source: Direct quotes and code examples from Drasner; interpolation mechanism synthesised from standard CSS knowledge
- Confidence rationale: Medium — Drasner covers gradients adequately but does not explain the interpolation mechanism explicitly; the lerp characterisation is synthesised
- Uncertainties: The prepared source does not describe interpolation algorithms. CSS Images 4 is an Editor’s Draft and this card does not claim implementation support or original-source fidelity.
- Cross-reference status: Not in Ottosson source
- Rosetta Stone check: Mathematics/lerp mapping qualified as structural
- OCR issues: CodePen embed fallbacks noted; SVG code block cleanly extracted
