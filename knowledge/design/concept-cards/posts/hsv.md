---
concept: "HSV Colour Space"
slug: "hsv"
category: "colour-theory"
subcategory: "colour-models"
tier: "foundational"
layer: "2-domain"
source: "Okhsv and Okhsl"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "HSV"
chapter_number: null
pdf_page: null
section: "Color spaces for color picking"
extraction_confidence: "high"
aliases:
  -
    - "Hue Saturation Value"
    - "HSB"
    - "Hue Saturation Brightness"
prerequisites: []
extends: []
related:
  - "hsl"
  - "okhsv"
  - "colour-gamut"
contrasts_with:
  - "hsl"
  - "okhsv"
answers_questions:
  - "What distinguishes Okhsl from Okhsv, and when would you use each?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition


HSV (also called HSB) re-parameterizes an RGB cube using hue, saturation and value. For normalized encoded sRGB r,g,b in [0,1], V is the maximum encoded component; it is not physical brightness or perceptual lightness.

# Core Definition


Ottosson describes HSV saturation as relative to the maximum for the same hue at V=1 and notes hue distortion. For encoded sRGB components r,g,b∈[0,1], let M=max(r,g,b), m=min(r,g,b), and Δ=M−m. Then V=M and S=0 when M=0, otherwise S=Δ/M. For Δ>0, define h′=(g−b)/Δ when M=r, (b−r)/Δ+2 when M=g, and (r−g)/Δ+4 when M=b; H=60·(h′ mod 6) degrees (equivalently a normalized turn). Hue has no measured value at achromatic colours (Δ=0). This is an RGB coordinate transformation, commonly applied to encoded sRGB, not a perceptual colour appearance model. At S<1, the other channel contributions mean the result is not simply a fully saturated hue mixed only with black.

# Prerequisites

- **RGB colour model** — HSV is a cylindrical re-parameterisation of RGB

# Key Properties


1. V=0 gives black; S=0 gives a neutral axis at every V. Hue is powerless when Δ=0.
2. At V=1 and S=1, the model reaches a primary/secondary edge for its hue; this is the source’s “Max Chroma at Edge” criterion, not a universal perceptual maximum claim.
3. The encoded sRGB cube maps to bounded HSV coordinates; coordinate independence does not imply perceptual independence.
4. Equal hue-angle steps need not be equally perceived; the source reports hue shifts and subjective comparisons.

# Construction / Recognition

## To Construct/Create:

1. For the classic normalized encoded-sRGB model, choose hue in turns or degrees, saturation S∈[0,1], and value V∈[0,1].
2. S=0 produces gray for any hue; V=0 produces black.
3. Interpret V as max(r,g,b), not brightness. Changing S at fixed V changes channel proportions, not merely the amount of a saturated hue mixed with black.

## To Identify/Recognise:

1. A square saturation/value field plus hue slider is one common interface arrangement, not part of the HSV definition.
2. Derive the coordinate convention from the RGB encoding and formula; do not infer model identity from a widget alone.
3. Hue is undefined/powerless at gray and black even when software stores a conventional numeric hue.

# Context & Application

- **Typical contexts**: Digital painting applications (Photoshop, Procreate, GIMP), colour pickers in design tools, image processing
- **Common applications**: Holding numeric H and S controls fixed while changing V to explore candidates; selecting a maximum-chroma candidate at S=1, V=1 for the specified encoded-sRGB model and hue. Changing V does not guarantee preserved perceived hue or saturation, or a specified brightness.

# Examples

**Example 1** (source description): Ottosson reports a purple shift as deep-blue HSV saturation decreases. This is attributed to the plotted example; the figure was not independently inspected. It does not assign perceived hue to the neutral endpoint, where Δ=0 and hue is powerless.

**Example 2** (from source): The comparison table shows that HSV achieves "yes" for Simple Geometrical Shape and Max Chroma at Edge, but "no" for Orthogonal Lightness and Orthogonal Chroma, and only "partial" for Orthogonal Hue and Saturation.

# Relationships

## Builds Upon

- **RGB colour model** — The classic equations re-parameterize a specified RGB representation; the formulas in this card are for encoded sRGB.

## Enables

- **Okhsv** — Ottosson presents a different Oklab-derived picker construction with familiar value-like controls; the coordinates are not numerically interchangeable.
- **HWB colour model** — HSV and HWB have an algebraic relationship for the same RGB convention; structural similarity to NCS does not make them equivalent.

## Related

- **HSL** — Both are RGB transformations but define S and the third coordinate differently.
- **Natural Colour System (NCS)** — Ottosson notes a structural similarity; NCS has a separate perceptual notation and sample context.

## Contrasts With

- **Okhsv** — Distinct coordinate construction and source-reported tradeoffs; avoid “drop-in” or numeric-compatibility claims.
- **HSL** — For encoded sRGB (.8,.2,.2), HSV gives S=.75,V=.8 while HSL gives S=.6,L=.5; their saturation and third-coordinate definitions differ.

# Common Errors


**Error**: Treating Value as physical brightness or lightness.
  **Correction**: V is the largest encoded RGB component. Relative luminance and perceptual lightness use different definitions.

**Error**: Describing S<1 as only mixing the fully saturated hue with black.
  **Correction**: HSV scales the channel distance from the maximum; at fixed V the channels vary together according to hue and S.

**Error**: Assuming hue stays perceptually fixed as S changes.
  **Correction**: The source documents hue distortions; describe this as its attributed example and not a universal quantified result.

# Common Confusions

- **Confusion**: HSV Saturation and HSL Saturation mean the same thing.
  **Clarification**: For classic encoded-sRGB formulas, HSV S=Δ/M when M>0, while HSL S=Δ/(1−|2L−1|) when Δ>0; both use S=0 for Δ=0. Ottosson's rough appearance account of HSV saturation relative to a same-hue maximum at V=1 is not the formula's universal perceptual meaning or CIE saturation.

# Source Reference

"HSV" section under "Color spaces for color picking," Okhsv and Okhsl (Björn Ottosson).

# Verification Notes


This full available-evidence review checked the encoded-sRGB equations and bounded claims against the complete prepared picker article, with Oklab/chroma terminology from the accepted Slice17 endpoint. The RGB witness is arithmetic, not perceptual measurement. Source-table ratings and hue examples are attributed, subjective and scoped to the article. No picker, display, browser or accessibility behavior was tested; figures and original capture fidelity remain unverified. Extraction-confidence metadata is unchanged.
