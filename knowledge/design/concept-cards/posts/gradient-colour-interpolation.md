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

CSS gradients define geometry and colour stops; CSS Images specifies an optional interpolation method for the gradient line, using CSS Color interpolation rules. The current CSS Images 4 Editor’s Draft default is Oklab; name the space for numerical examples and do not infer implementation support from draft text.

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

- **RGB colour model** — Gradient colors are interpolated in the selected space; RGB is one option, and the channel path depends on that choice
- **Additive colour mixing** — The interpolation space is a selected CSS colour space; sRGB components are encoded and are not physical light-addition values

# Key Properties

1. CSS stops accept positions appropriate to the gradient type (length/percentage or angle/percentage); SVG offsets use their own syntax and may be normalized fractions or percentages
2. Intermediate colours follow the selected interpolation space and method; name the space for numerical results
3. CSS supports `linear-gradient()`, `radial-gradient()`, and `conic-gradient()` as gradient types
4. CSS Color interpolation uses premultiplied alpha for non-opaque colours, with hue-specific rules where applicable; transparent endpoint channels do not create visible colour
5. CSS Images defines gradient syntax and delegates colour interpolation to CSS Color; the current editor draft is not browser-support evidence

# Construction / Recognition

## To Construct/Create:
1. Use `background: linear-gradient(direction, color-stop-1, color-stop-2, ...)`
2. Direction: `to right`, `to bottom`, `45deg`, etc.
3. CSS colour stops may have a CSS `<length-percentage>` position (or `<angle-percentage>` for conic gradients); SVG `<stop offset>` has separate syntax. CSS stops can extend outside the 0–100% range
4. Optionally add explicit positions: `linear-gradient(to right, red 0%, blue 50%, green 100%)`

## To Identify/Recognise:
1. `linear-gradient()`, `radial-gradient()`, `conic-gradient()` in a `background` property
2. The classic "hue mudding" in the middle of a gradient between complementary colours (e.g. red to cyan produces grey in the middle in sRGB interpolation)

# Context & Application

- **Typical contexts**: CSS backgrounds, SVG fills, UI decoration, image masks, colour scales in data visualisation
- **Common applications**: Background gradients; gradient text effects; creating smooth colour transitions between sections; SVG gradient fills for icons or illustrations

## Cross-Domain Connections

**Mathematics → RIGOROUS (bounded)**: For two stops and a fixed interpolation parameter, each applicable component follows the specified interpolation operation in the selected space; hue and alpha follow their specified rules, including premultiplication. This exact operation does not imply physical light addition or perceptual uniformity.

# Examples

**Example 1** (from source — SVG): The `<linearGradient>` with transparent white at offset 0 and opaque black at offset 0.3 is an SVG stop example. Separately, under CSS explicit sRGB interpolation, opaque `rgb(255 0 0)` to `rgb(0 0 255)` at t=0.5 gives normalized `(0.5, 0, 0.5, 1)`; transparent white to opaque black at t=0.5 gives `(0, 0, 0, 0.5)` after unpremultiplication.

**Example 2** (from source): Drasner references using gradients "as a mask" and combined with animation — demonstrating gradients as dynamic compositing elements, not just static fills.

# Relationships

## Builds Upon
- **RGB colour model** — RGB is one available coordinate system for interpolation; the selected gradient space determines the interpolated components

## Enables
- **Colour scale design** — Gradient interpolation is the foundation of continuous colour scales in data visualisation

## Related
- **CSS rgba()** — Used in gradient stops for transparency
- **feColorMatrix** — An alternative way to perform colour transformations on gradient-filled SVG elements

# Common Errors

- **Error**: Treating a keyword or an unspecified space as a universal numeric interpolation example.
  **Correction**: State the space and exact endpoint colors. For explicit sRGB interpolation, opaque `rgb(255 0 0)` and `rgb(0 0 255)` yield `(0.5, 0, 0.5, 1)` at t=0.5; another interpolation space can yield a different midpoint.

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
- Rosetta Stone check: Mathematics/component interpolation is rigorous only for the specified operation and stated hue/alpha rules
- OCR issues: CodePen embed fallbacks noted; SVG code block cleanly extracted
