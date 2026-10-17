---
concept: "Okhsv Colour Space"
slug: "okhsv"
category: "colour-theory"
subcategory: "colour-models"
tier: "advanced"
layer: "2-domain"
source: "Okhsv and Okhsl"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "Okhsv"
chapter_number: null
pdf_page: null
section: "Introducing two new color spaces: Okhsv and Okhsl"
extraction_confidence: "high"
aliases:
  -
    - "Ok HSV"
prerequisites:
  - "hsv"
  - "colour-gamut"
  - "orthogonal-colour-properties"
extends:
  - "hsv"
related:
  - "okhsl"
  - "colour-picker-design-principles"
contrasts_with:
  - "hsv"
  - "okhsl"
answers_questions:
  - "What distinguishes Okhsl from Okhsv, and when would you use each?"
  - "What makes a colour picker perceptually well-designed?"
rosetta_stone:
  -
    domain: "music"
    concept: "Equal temperament tuning"
    rating: "loose"
    note: "Numeric colour-model parameters and equal frequency ratios/Euclidean basis vectors do not establish equal visual or auditory differences or perceptual independence."
---

# Quick Definition


Okhsv is an Oklab-derived coordinate model proposed as an sRGB picker tradeoff. The source rates its profile subjectively; it does not promise equal brightness, even change, universal HSL/HSV compatibility, or a complete conversion implementation.

# Core Definition


The source toe constants are k1=.206, k2=.03 and k3=(1+k1)/(1+k2); toe(L)=(k3L−k1+sqrt((k3L−k1)^2+4k2k3L))/2 and toe_inv(l)=l(l+k1)/(k3(l+k2)). Ottosson derives Okhsv from Oklab polar coordinates. The article’s figures use lightness-like Lr vertically and C·Lr/L horizontally, not plain C. A hue-specific cusp anchors a triangular gamut construction; the remapping approximates it with a curved top and compensating v adjustment, with a further low-saturation correction. This is an approximation within the article’s sRGB target, not a physical perceptual cylinder. The source table rates Okhsv yes for Orthogonal Hue, Simple Geometrical Shape, Max Chroma at Edge and Varies Smoothly; no for Orthogonal Lightness, Orthogonal Chroma and Varies Evenly; Orthogonal Saturation is partial. A constant-v band therefore does not promise equal brightness. The related Okhwb coordinates are w=(1−s)v and b=1−v; inverse s=1−w/(1−b), v=1−b is valid only for b≠1. At black b=1 the coordinates are degenerate.

# Prerequisites


- **HSV colour space** — Provides a familiar comparison in the article; Okhsv coordinates are not numerically compatible by name.
- **Colour gamut** — The article’s cusp and remapping discussion is for the sRGB target.
- **Orthogonal colour properties** — The source uses these as comparison labels; its ratings are subjective and scope-limited.

# Key Properties


1. The illustrated cross-section uses axes Lr and C·Lr/L; its triangular remapping and curved-top compensation are approximate.
2. The source’s cusp maps to s=1,v=1 for the specified hue; this is the author’s Max Chroma at Edge criterion within the target construction.
3. Okhsv is rated no for Orthogonal Lightness and Varies Evenly; constant v is not equal physical or perceived brightness.
4. Okhwb has w=(1−s)v and b=1−v. Inversion divides by 1−b and is undefined at black (b=1).
5. These are article-specific sRGB constructions, not universal display properties or proof of current tool adoption.

# Construction / Recognition

## To Construct/Create:

1. Decode encoded sRGB and use the matched complete Oklab conversion. For C>0, derive C=hypot(a,b), h=atan2(b,a)/(2π) modulo 1, normalizing a,b only when C>0.
2. For exact neutral, set s=0 and v=toe(L), use h=0 only as a serialization convention, and skip chroma normalization/cusp helpers. Canonical black (0,0,0) and white (0,0,1) in (h,s,v) are explicit conventions for degenerate coordinates.
3. For chromatic inputs, follow the source’s hue cusp, triangular approximation, curved-top compensation and low-saturation correction; its helpers include omitted gamut code and are not a full robust converter.
4. To convert to Okhwb use w=(1−s)v and b=1−v. Invert only when b≠1: v=1−b and s=1−w/(1−b). Black requires a separate degenerate branch.

## To Identify/Recognise:

1. Distinguish this Oklab-derived construction from HSV by its hue/chroma pipeline and nonlinear toe.
2. The source comparison says its constant-v bands do not achieve orthogonal lightness; do not call them equal brightness.
3. Hue is powerless at C=0; any stored zero is a convention. For near-neutrals, state a numerical tolerance before branching.

# Context & Application

- **Typical contexts**: Colour picker design for applications where finding vivid/saturated colours is important, digital painting, graphic design tools
- **Common applications**: Selecting the most vivid colour for a given hue; adjusting brightness of a colour while preserving its saturation relative to maximum

## Cross-Domain Connections


**Music → LOOSE**: Okhsv’s numeric hue coordinate and equal frequency ratios offer only a limited structural analogy. Equal numeric steps do not establish equal visual or auditory differences or perceptual independence.

# Examples


**Example 1** (source description): The article describes hue-specific Oklab-derived cross-sections remapped toward a simple picker shape; the diagrams are attributed and were not independently inspected.

**Example 2** (source table): The subjective sRGB profile rates Okhsv yes for hue, simple geometry, maximum chroma at edge and smooth variation; no for orthogonal lightness, orthogonal chroma and even variation; orthogonal saturation is partial.

**Example 3** (algebraic boundary): At s=.4,v=.5, Okhwb gives w=.3,b=.5; inverse recovers s=.4,v=.5. At black s=0,v=0 gives w=0,b=1 and the inverse denominator is zero, so black must be handled separately.

# Relationships

## Builds Upon

- **Oklab** — The source derives hue/chroma through Oklab-based coordinates; perceptual uniformity remains approximate.
- **HSV** — The construction is intended to offer a familiar value-like control tradeoff, not a drop-in with numerically compatible values.

## Enables

- **Picker candidates** — Can inform an Oklab-derived sRGB picker candidate; host controls, output checks and accessibility require separate assessment.

## Related

- **Okhsl** — Sibling mapping with a different tradeoff profile; matching numbers do not imply matching colours.
- **Okhwb** — Whiteness/blackness reparameterization with a singular black boundary in the inverse.

## Contrasts With

- **HSV** — Distinct coordinate construction and parameter meanings; not numeric-compatible by name.
- **Okhsl** — Source ratings differ for Orthogonal Lightness and Max Chroma at Edge; both are rated no for Varies Evenly. Claims remain source-attributed and sRGB-scoped.

# Common Errors


**Error**: Calling constant-v Okhsv bands equal-brightness or perceptually even.
  **Correction**: The source rates Orthogonal Lightness and Varies Evenly no.

**Error**: Using C alone as the figure’s horizontal axis.
  **Correction**: The article labels the axis C·Lr/L.

**Error**: Inverting Okhwb at b=1 or dividing a,b by C for a neutral.
  **Correction**: Handle exact neutral/black separately; use the stated convention and avoid zero divisors.

**Error**: Calling the excerpt a complete robust converter.
  **Correction**: It depends on omitted gamut helpers; this card records the method and boundaries, not a library.

# Common Confusions


**Confusion**: Okhsv corrects every HSV problem or guarantees all hues look equally bright.
  **Clarification**: The source claims a qualified improvement and rates Orthogonal Lightness and Varies Evenly no. Use its tradeoff profile for the stated sRGB context.

# Source Reference

"Okhsv" section under "Introducing two new color spaces: Okhsv and Okhsl," Okhsv and Okhsl (Björn Ottosson).

# Verification Notes


This full available-evidence review checked the construction, figure-axis labels, toe/conversion boundaries, Okhwb relation and comparison profile against the complete prepared picker article and accepted Slice17 Oklab/conversion terminology. The inverse-boundary examples are algebraic checks; omitted gamut helpers were not executed. Figures were not visually inspected. Original capture fidelity, actual widget/browser behavior and accessibility remain unverified; extraction-confidence metadata is unchanged.
