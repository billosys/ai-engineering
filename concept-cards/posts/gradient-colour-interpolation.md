---
concept: Gradient Colour Interpolation (CSS)
slug: gradient-colour-interpolation
category: colour-theory
subcategory: colour-effects
tier: intermediate
layer: 3-implementation
source: "Working With Colors Guide"
source_slug: posts
authors: "Sarah Drasner"
chapter: "Color Properties / Gradients"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: medium
aliases:
  - ["CSS gradients", "linear-gradient", "radial-gradient", "color stops", "SVG gradient"]
prerequisites:
  - rgb-colour-model
  - additive-colour-mixing
extends:
  - []
related:
  - css-rgba
  - hsl-css-syntax
contrasts_with:
  - []
answers_questions: []
rosetta_stone:
  - domain: mathematics
    concept: "Linear interpolation (lerp)"
    rating: rigorous
    note: "CSS gradient colour stops are computed by linearly interpolating between stop colours in sRGB space (or another colour space in CSS Color 4). The value at position t between stop A and stop B is exactly lerp(A, B, t) = A + t(B-A) applied per channel \u2014 a direct mathematical identity."
---

# Quick Definition

CSS gradient colour interpolation blends between two or more colour stops along a gradient, computing intermediate colours by linear interpolation between the specified stop values in sRGB channel space.

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

- **RGB colour model** \u2014 Intermediate gradient colours are computed by interpolating RGB channel values
- **Additive colour mixing** \u2014 The interpolation happens in the additive sRGB space

# Key Properties

1. Colour stops specify a colour and an optional position (0%\u2013100% or 0.0\u20131.0)
2. Intermediate colours are computed by linear interpolation between adjacent stops in sRGB
3. CSS supports `linear-gradient()`, `radial-gradient()`, and `conic-gradient()` as gradient types
4. Transparency (via rgba() or hsla() stops) is interpolated in the alpha channel independently
5. CSS Color 4 allows specifying the interpolation colour space (e.g. in Oklab), but browser support varies

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

**Mathematics \u2192 RIGOROUS**: CSS gradient interpolation between two stops is linear interpolation (lerp): for position t \u2208 [0,1] between stop A and stop B, the computed colour per channel is `A + t*(B - A)`. This is identical to the mathematical definition of lerp applied component-wise to the colour vector.

# Examples

**Example 1** (from source \u2014 SVG): The `<linearGradient>` with stops from white (opacity 0) at offset 0 to black (opacity 1) at offset 0.3, demonstrating opacity interpolation in an SVG gradient.

**Example 2** (from source): Drasner references using gradients "as a mask" and combined with animation \u2014 demonstrating gradients as dynamic compositing elements, not just static fills.

# Relationships

## Builds Upon
- **RGB colour model** \u2014 Interpolation operates on RGB channel values

## Enables
- **Colour scale design** \u2014 Gradient interpolation is the foundation of continuous colour scales in data visualisation

## Related
- **CSS rgba()** \u2014 Used in gradient stops for transparency
- **feColorMatrix** \u2014 An alternative way to perform colour transformations on gradient-filled SVG elements

# Common Errors

- **Error**: Expecting a gradient between red and green to pass through yellow in the middle.
  **Correction**: In sRGB interpolation, red (255, 0, 0) to green (0, 255, 0) passes through brown/olive (128, 128, 0) \u2014 not yellow (255, 255, 0). To get a perceptually pleasing rainbow effect, interpolate through hue using multiple stops or use a different colour space (e.g. Oklab interpolation in CSS Color 4).

# Common Confusions

- **Confusion**: The "direction" in `linear-gradient` refers to the direction the gradient flows.
  **Clarification**: `to right` means the gradient flows from left to right \u2014 the first colour stop appears on the left and the last on the right. The direction keyword specifies the ending side/corner, not the starting side.

# Source Reference

"Gradients" section under "Color Properties," Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Definition source: Direct quotes and code examples from Drasner; interpolation mechanism synthesised from standard CSS knowledge
- Confidence rationale: Medium \u2014 Drasner covers gradients adequately but does not explain the interpolation mechanism explicitly; the lerp characterisation is synthesised
- Uncertainties: CSS Color 4 gradient interpolation in non-sRGB spaces (Oklab, etc.) is not mentioned in source; this is a significant omission for modern usage
- Cross-reference status: Not in Ottosson source
- Rosetta Stone check: Mathematics/lerp mapping added as rigorous
- OCR issues: CodePen embed fallbacks noted; SVG code block cleanly extracted
