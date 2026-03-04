---
concept: feColorMatrix (SVG Filter)
slug: fecolormatrix
category: colour-theory
subcategory: colour-effects
tier: intermediate
layer: 3-implementation
source: "Working With Colors Guide"
source_slug: posts
authors: "Sarah Drasner"
chapter: "Other Nice Color Effects / feColorMatrix"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: medium
aliases:
  - ["feColorMatrix SVG", "SVG color matrix filter", "SVG feColorMatrix"]
prerequisites:
  - rgb-colour-model
  - css-rgba
extends:
  - []
related:
  - mix-blend-mode
contrasts_with:
  - mix-blend-mode
answers_questions: []
rosetta_stone:
  - domain: mathematics
    concept: "Matrix multiplication / linear transformation"
    rating: rigorous
    note: "feColorMatrix applies a 5\u00d74 matrix to each pixel's RGBA colour vector [R, G, B, A, 1]. The operation is literal matrix-vector multiplication: the output colour is the matrix product of the input colour vector and the transformation matrix."
---

# Quick Definition

`feColorMatrix` is an SVG filter primitive that transforms pixel colour values using a 5\u00d74 matrix multiplication, enabling complex colour remapping including hue rotation, saturation adjustment, and arbitrary RGBA channel mixing.

# Core Definition

Drasner describes feColorMatrix as "a filter primitive in SVG that can be applied to HTML elements as well. It's very powerful, and allows you to fine-tune and finesse color. As the name implies, the base markup of `feColorMatrix` uses a matrix of values, and we apply it using its relative id." She provides the example:

```xml
<filter id="imInTheMatrix">
  <feColorMatrix in="SourceGraphic"
    type="matrix"
    values="0 0 0 0 0
            1 1 1 1 0
            0 0 0 0 0
            0 0 0 1 0" />
</filter>
<path filter="url(#imInTheMatrix)" \u2026 />
```

And a hue rotation variant:

```xml
<filter id="imInTheHueMatrix">
  <feColorMatrix in="SourceGraphic"
    type="hueRotate"
    values="150" />
</filter>
```

She notes the `type` attribute supports multiple modes: `matrix` (full 5\u00d74 matrix), `hueRotate`, `saturate`, and `luminanceToAlpha`.

# Prerequisites

- **RGB colour model** \u2014 feColorMatrix operates on RGBA channel values
- **Mathematics (matrix multiplication)** \u2014 The full `matrix` type requires understanding 5\u00d74 matrix-vector products

# Key Properties

1. The `matrix` type applies a 5\u00d74 matrix to each pixel's [R, G, B, A] vector (with an implicit constant 1 as the 5th input element)
2. `hueRotate` type accepts a single angle in degrees and rotates hue of all pixels
3. `saturate` type accepts a scaling value (0 = greyscale, 1 = unchanged, >1 = more saturated)
4. Applied via `filter="url(#filterID)"` on SVG elements; can also be applied to HTML elements via the CSS `filter` property
5. Can be composed with other SVG filter primitives in a filter chain

# Construction / Recognition

## To Construct/Create:
1. Define a `<filter>` element with a unique `id` in SVG `<defs>` or inline
2. Inside the filter, place `<feColorMatrix in="SourceGraphic" type="[type]" values="[values]" />`
3. Reference the filter with `filter="url(#id)"` on the target element
4. For `type="matrix"`: provide 20 space-separated values (5 columns \u00d7 4 rows)
5. For `type="hueRotate"`: provide a single degree value

## To Identify/Recognise:
1. An SVG `<filter>` element containing a `<feColorMatrix>` child
2. Elements with `filter="url(#...)"` referencing such a filter

# Context & Application

- **Typical contexts**: SVG colour manipulation, photo filter effects in CSS/SVG, colour accessibility adjustments (simulating colour blindness), Instagram-style CSS image filters
- **Common applications**: Converting colour images to greyscale; applying hue shifts to all colours uniformly; creating duotone effects; simulating colour vision deficiencies for accessibility testing

## Cross-Domain Connections

**Mathematics \u2192 RIGOROUS**: The `matrix` type is literal matrix-vector multiplication. Each output channel (R_out, G_out, B_out, A_out) is a linear combination of all input channels plus a constant: `R_out = M[0]*R_in + M[1]*G_in + M[2]*B_in + M[3]*A_in + M[4]`. This is identical in structure to a linear transformation in linear algebra, with the 5th column serving as a bias/translation term (homogeneous coordinates).

# Examples

**Example 1** (from source): The matrix `"0 0 0 0 0 / 1 1 1 1 0 / 0 0 0 0 0 / 0 0 0 1 0"` \u2014 this sets R=0, G=R+G+B+A (clamped to 1), B=0, keeping alpha unchanged. In practice this creates a green-channel-only image that produces a green monochrome effect.

**Example 2** (from source): `type="hueRotate" values="150"` \u2014 rotates all hues 150 degrees on the colour wheel, shifting reds toward blue, greens toward red, etc.

# Relationships

## Builds Upon
- **RGB colour model** \u2014 feColorMatrix works on linear RGBA channel values per pixel

## Enables
- **Accessible colour simulation** \u2014 Colour-blindness simulation matrices are a well-known application
- **CSS Instagram-style filters** \u2014 Drasner mentions Una Kravets's CSSgram as combining feColorMatrix-style effects

## Related
- **mix-blend-mode** \u2014 An alternative approach to colour effect compositing; blend modes work between layers while feColorMatrix transforms a single layer's colours
- **CSS filter property** \u2014 feColorMatrix effects can be applied to HTML via CSS `filter: url(#id)` or the shorthand `filter: hue-rotate(150deg)` (which is a simplified CSS equivalent)

## Contrasts With
- **mix-blend-mode** \u2014 Blend modes require two layers to composite; feColorMatrix operates on a single layer's colours independently

# Common Errors

- **Error**: Providing fewer than 20 values for `type="matrix"`.
  **Correction**: The matrix type requires exactly 20 space-separated values (4 rows \u00d7 5 columns). Fewer values will produce unexpected or null results.

- **Error**: Expecting feColorMatrix to work as a CSS property directly.
  **Correction**: feColorMatrix is an SVG filter primitive. To apply it to HTML elements, define the SVG filter in an `<svg>` block and reference it via `filter: url(#id)` in CSS, or use the CSS shorthand equivalents (`hue-rotate()`, `saturate()`, `brightness()`, etc.) for simpler cases.

# Common Confusions

- **Confusion**: `type="saturate"` with a value of 0 removes all saturation (as expected), but values above 1 behave unexpectedly.
  **Clarification**: Values above 1 increase saturation beyond the original; this is valid and useful for increasing colourfulness. There is no inherent upper limit, though values will clamp at displayable gamut boundaries.

# Source Reference

"feColorMatrix" section under "Other Nice Color Effects," Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Definition source: Direct quotes and code examples from Drasner; matrix interpretation synthesised
- Confidence rationale: Medium \u2014 Drasner provides correct overview and examples but directs readers to Una Kravets's article for depth; matrix semantics require supplementary knowledge
- Uncertainties: The specific matrix example's output behaviour requires external verification; Drasner does not explain the matrix values in detail
- Cross-reference status: Not in Ottosson source
- Rosetta Stone check: Mathematics/matrix-multiplication mapping added as rigorous
- OCR issues: None significant
