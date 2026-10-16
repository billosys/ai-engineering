---
concept: "feColorMatrix (SVG Filter)"
slug: "fecolormatrix"
category: "colour-theory"
subcategory: "colour-effects"
tier: "intermediate"
layer: "3-implementation"
source: "Working With Colors Guide"
source_slug: "posts"
authors: "Sarah Drasner"
chapter: "Other Nice Color Effects / feColorMatrix"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "medium"
aliases:
  -
    - "feColorMatrix SVG"
    - "SVG color matrix filter"
    - "SVG feColorMatrix"
prerequisites:
  - "rgb-colour-model"
  - "css-rgba"
extends: []
related:
  - "mix-blend-mode"
contrasts_with:
  - "mix-blend-mode"
answers_questions: []
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Affine transformation in homogeneous coordinates"
    rating: "rigorous"
    note: "The 20 SVG matrix values form four output rows with five input coefficients for [R, G, B, A, 1]. The constant term makes the RGBA mapping affine; this is a concrete matrix operation, not a five-component pixel."
---

# Quick Definition

`feColorMatrix` is an SVG filter primitive. Its `matrix` type has four output rows and five coefficients per row, multiplying the input components `[R, G, B, A, 1]`; the constant column supplies an affine bias. SVG also defines `hueRotate`, `saturate` and `luminanceToAlpha` types.

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
<path filter="url(#imInTheMatrix)" … />
```

And a hue rotation variant:

```xml
<filter id="imInTheHueMatrix">
  <feColorMatrix in="SourceGraphic"
    type="hueRotate"
    values="150" />
</filter>
```

She notes the `type` attribute supports multiple modes: `matrix` (full 5×4 matrix), `hueRotate`, `saturate`, and `luminanceToAlpha`.

# Prerequisites

- **RGB colour model** — feColorMatrix operates on RGBA channel values
- **Mathematics (matrix multiplication)** — The `matrix` type supplies 20 coefficients as four output rows with five input columns `[R, G, B, A, 1]`

# Key Properties

1. The `matrix` type uses four output rows × five input columns `[R, G, B, A, 1]` (20 values); the bias term makes the mapping affine
2. SVG `hueRotate` accepts an angle and applies its predefined matrix operation; it is not identical to HSL hue rotation
3. `saturate` type accepts a scaling value (0 = greyscale, 1 = unchanged, >1 = more saturated)
4. Applied via `filter="url(#filterID)"` on SVG elements; can also be applied to HTML elements via the CSS `filter` property
5. Can be composed with other SVG filter primitives in a filter chain

# Construction / Recognition

## To Construct/Create:
1. Define a `<filter>` element with a unique `id` in SVG `<defs>` or inline
2. Inside the filter, place `<feColorMatrix in="SourceGraphic" type="[type]" values="[values]" />`
3. Reference the filter with `filter="url(#id)"` on the target element
4. For `type="matrix"`, provide 20 values as four output rows of five coefficients for `[R, G, B, A, 1]`
5. For `type="hueRotate"`: provide a single degree value

## To Identify/Recognise:
1. An SVG `<filter>` element containing a `<feColorMatrix>` child
2. Elements with `filter="url(#...)"` referencing such a filter

# Context & Application

- **Typical contexts**: SVG colour manipulation, photo filter effects in CSS/SVG, illustrative colour transformations (not, by themselves, validated colour-vision simulations), Instagram-style CSS image filters
- **Common applications**: Converting colour images to greyscale; applying hue shifts to all colours uniformly; creating duotone effects; exploring channel remapping; a matrix alone does not validate colour-vision-deficiency simulation or accessibility

## Cross-Domain Connections

**Mathematics → RIGOROUS (bounded)**: For each input pixel, the specified four rows multiply `[R,G,B,A,1]`; the first four columns weight RGBA and the fifth supplies the constant. This is exact homogeneous matrix multiplication for the stated input and coefficients before the specified clipping; it does not imply a five-component pixel.

# Examples

**Example 1** (from source): The matrix `"0 0 0 0 0 / 1 1 1 1 0 / 0 0 0 0 0 / 0 0 0 1 0"` — this sets R=0, G=R+G+B+A (clamped to 1), B=0, keeping alpha unchanged. For opaque black `(0,0,0,1)`, the second row produces green `1` because its alpha coefficient is `1`; this example does not simply extract the input green channel. The result may be clipped.

**Example 2** (from source): `type="hueRotate" values="150"` applies the SVG-defined matrix operation. It is not a promise of an HSL hue-wheel rotation; CSS `hue-rotate()` is a separate filter function.

# Relationships

## Builds Upon
- **RGB colour model** — `feColorMatrix` transforms per-pixel RGBA components; SVG filter operations use the specified filter colour-interpolation space

## Enables
- **Accessible colour simulation** — A matrix can be used to explore a colour transformation, but an arbitrary matrix is not validated as a colour-vision simulation or accessibility test
- **CSS Instagram-style filters** — Drasner mentions Una Kravets's CSSgram as combining feColorMatrix-style effects

## Related
- **mix-blend-mode** — An alternative approach to colour effect compositing; blend modes work between layers while feColorMatrix transforms a single layer's colours
- **CSS filter property** — SVG filters can be referenced from CSS; CSS `hue-rotate()` is separately defined and is not an equivalent spelling of SVG `hueRotate`

## Contrasts With
- **mix-blend-mode** — Blend modes combine a source with a backdrop; `feColorMatrix` transforms filter input components within a filter chain

# Common Errors

- **Error**: Providing fewer than 20 values for `type="matrix"`.
  **Correction**: The matrix type is defined as four output rows with five coefficients each. This definition does not establish a malformed-input fallback result.

- **Error**: Treating similarly named CSS filter functions as equivalent SVG filter operations.
  **Correction**: `feColorMatrix` is an SVG filter primitive and can be referenced by CSS `filter: url(#id)`. SVG filter primitives use the selected filter interpolation space (default `linearRGB`); CSS filter functions operate in sRGB. Similar names do not establish equivalent rendering.

# Common Confusions

- **Confusion**: `type="saturate"` with a value of 0 removes all saturation (as expected), but values above 1 behave unexpectedly.
  **Clarification**: Values above 1 increase saturation beyond the original; this is valid and useful for increasing colourfulness. There is no inherent upper limit, though values will clamp at displayable gamut boundaries.

# Source Reference

"feColorMatrix" section under "Other Nice Color Effects," Working With Colors Guide (Sarah Drasner).

# Verification Notes

- Iteration02 scope: The current technical support below uses the prepared text and linked rules; this correction does not assess fidelity to the unavailable original capture or browser behavior. Extraction-confidence metadata is unchanged. Retained extraction/provenance remarks below are predecessor assertions present at source 19c7a08a; their authorship is not inferred here, and they are not new current results. Where this iteration clarifies a note, that clarification scopes a prior assertion rather than recording a new extraction or verification result.

- Current SVG support: [Filter Effects 1 §§9.1, 9.6 and 10](https://www.w3.org/TR/filter-effects-1/) defines matrix rows, unpremultiplied components, clipping and the default `linearRGB` filter space. Its `hue-rotate()` function is separately defined. The linked W3C document is a 2018 Working Draft.

- Definition source: Direct quotes and code examples from Drasner; matrix interpretation synthesised
- Confidence rationale: Medium — Drasner provides correct overview and examples but directs readers to Una Kravets's article for depth; matrix semantics require supplementary knowledge
- Verification scope: The displayed example’s output is calculated from its four rows and `[R,G,B,A,1]`; clipping applies after the matrix operation. This is a specification-based calculation, not runtime observation.
- Cross-reference status: Not in Ottosson source
- Rosetta Stone check: Mathematics/homogeneous matrix multiplication is rigorous for the stated four-row, five-input operation before clipping
- OCR issues: None significant
