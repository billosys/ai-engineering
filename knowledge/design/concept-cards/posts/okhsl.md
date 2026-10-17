---
concept: "Okhsl Colour Space"
slug: "okhsl"
category: "colour-theory"
subcategory: "colour-models"
tier: "advanced"
layer: "2-domain"
source: "Okhsv and Okhsl"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "Okhsl"
chapter_number: null
pdf_page: null
section: "Introducing two new color spaces: Okhsv and Okhsl"
extraction_confidence: "high"
aliases:
  -
    - "Ok HSL"
prerequisites:
  - "hsl"
  - "colour-gamut"
  - "orthogonal-colour-properties"
extends:
  - "hsl"
related:
  - "okhsv"
  - "colour-picker-design-principles"
contrasts_with:
  - "hsl"
  - "okhsv"
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


Okhsl is an Oklab-derived picker coordinate model introduced by Björn Ottosson. Its nonlinear remapping aims for a convenient sRGB picker compromise; its source comparison rates the goals subjectively and does not promise exact perceptual uniformity, accessibility, or numeric compatibility with HSL.

# Core Definition


The source toe constants are k1=.206, k2=.03 and k3=(1+k1)/(1+k2); toe(L)=(k3L−k1+sqrt((k3L−k1)^2+4k2k3L))/2 and toe_inv(l)=l(l+k1)/(k3(l+k2)). Ottosson derives Okhsl from Oklab in polar form. For non-neutral input, hue comes from the a,b direction and chroma C; a nonlinear toe maps base Oklab lightness L to picker lightness l=toe(L). Saturation is constructed from three hue/lightness-dependent references: C=0 with initial slope C0 at s=0, C=Cmid at s=.8, and C=Cmax at s=1. C0 is a derivative/slope, not the chroma value at s=0. The source uses a piecewise rational mapping and inverse, not C=s·Cmax. Its helper get_Cs receives base Oklab L and unit a/b; compute those references before replacing L with toe(L). In the source’s comparison, Okhsl is rated yes for orthogonal lightness, orthogonal hue, simple geometry and smooth change; no for orthogonal chroma, orthogonal saturation, max chroma at edge and even change. These are subjective sRGB judgments, not guarantees.

# Prerequisites


- **HSL colour space** — Familiar H/S/L labels provide a comparison route, but Okhsl has a distinct construction and values.
- **Colour gamut** — The article’s C0, Cmid and Cmax references are calculated for its sRGB target and hue/lightness conditions.
- **Orthogonal colour properties** — The source uses these as proposed comparison goals; the table is subjective and sRGB-scoped.

# Key Properties


1. Okhsl’s picker lightness l is nonlinear toe(L), where L is base Oklab lightness; l is not the argument to get_Cs.
2. The s-to-C mapping uses C0 as the initial slope, Cmid at s=.8 and Cmax at s=1, with rational piecewise functions.
3. Exact neutral input has C=0 and powerless hue: choose s=0, l=toe(L), and a conventional h=0 only for a serialized coordinate; do not normalize a,b by C or call gamut-cusp helpers.
4. Black and white have degenerate hue/saturation coordinates; use explicit canonical coordinates only as a recipe convention. Near-neutral classification needs a declared tolerance.
5. Source ratings are subjective and scoped to sRGB. “Smooth” is not “even,” and no universal drop-in or accessibility result follows.

# Construction / Recognition

## To Construct/Create:

1. Decode encoded sRGB, convert through the complete Oklab pipeline, then derive base L, C and h from a,b. For C>0, h=atan2(b,a)/(2π) modulo 1; normalize a,b by C only in this chromatic case.
2. For exact neutral C=0, set s=0 and l=toe(L); use h=0 as an explicit powerless-hue convention. Handle canonical black as (0,0,0) and white as (0,0,1) in (h,s,l), without zero-divisor helper calls.
3. For chromatic values compute get_Cs(base L, unit a/b), yielding C0,Cmid,Cmax. Forward s-to-C uses two rational branches: for s<.8, t=1.25s, k1=.8C0, k2=1−k1/Cmid, C=t·k1/(1−k2t); otherwise t=(s−.8)/.2, k0=Cmid, k1=.2·Cmid²·1.25²/C0, k2=1−k1/(Cmax−Cmid), C=k0+t·k1/(1−k2t). The inverse uses t=C/(k1+k2C), s=.8t below Cmid; above, t=(C−Cmid)/(k1+k2(C−Cmid)), s=.8+.2t. These formulas require valid source helper outputs and nonzero denominators; set l=toe(L).
4. In reverse, recover base L=toe_inv(l) before get_Cs, then map s to C, construct Oklab a,b from C and h, and run the matched inverse conversion and encoding.
5. State helper domains and gamut assumptions. The article excerpts depend on omitted gamut helpers and are not a complete robust converter.

## To Identify/Recognise:

1. The construction uses an Oklab-derived hue/chroma and a nonlinear lightness toe, not HSL’s RGB formula.
2. Hue is powerless at C=0; a stored zero hue is convention, not measurement.
3. Compare the source table as an author-reported sRGB profile. Equal numeric changes or matching HSL labels do not establish equal appearance or interchangeable values.

# Context & Application


- **Typical contexts**: Candidate controls for a picker where an Oklab-derived lightness coordinate and a smooth chroma mapping are useful tradeoffs.
- **Common applications**: Generate candidates, convert for the specified destination, then inspect gamut and actual rendered pairs. The source comparison alone does not establish contrast or accessibility.

## Cross-Domain Connections


**Music → LOOSE**: Okhsl parameters and equal frequency ratios can serve as a limited analogy for model coordinates and chosen steps. Numeric steps do not establish equal visual or auditory differences or perceptual independence; the mapping is not rigorous.

# Examples


**Example 1** (from source): The article proposes an Okhsl compromise with parameters that “closely match perception”; this is the author’s qualified claim, not a universal guarantee. Figures were not independently inspected.

**Example 2** (source table): The subjective sRGB comparison rates Orthogonal Lightness/Hue, Simple Geometrical Shape and Varies Smoothly yes; Orthogonal Chroma/Saturation, Max Chroma at Edge and Varies Evenly no.

**Example 3** (synthetic arithmetic witness, not a measured colour): With C0=.1, Cmid=.12, Cmax=.2, the source’s rational construction gives C(0)=0, C(.4)=.048, C(.8)=.12, C(.9)=.1488 and C(1)=.2. The linear shortcut s·Cmax gives .16 at s=.8 and therefore does not reproduce the reference.

# Relationships

## Builds Upon

- **Oklab** — The article derives chroma and hue from Oklab coordinates and then remaps them.
- **HSL** — Familiar parameter labels and picker context do not establish numeric compatibility.

## Enables

- **Picker candidates** — Its stated coordinate tradeoffs can inform a candidate control; output and interaction still need task-specific review.
- **Palette candidates** — It can generate coordinates for evaluation, but equal lightness values do not certify contrast or accessibility.

## Related

- **Okhsv** — Sibling mapping with a value-like coordinate and a different profile of tradeoffs; their values are not interchangeable.

## Contrasts With


- **HSL** — Distinct underlying RGB versus Oklab-derived constructions; do not equate corresponding values.
- **Okhsv** — Different coordinate mappings and source-reported tradeoff profiles.
- **HSLuv** — The article gives an attributed comparison of mapping tradeoffs; it is not a general measurement of user experience.

# Common Errors


**Error**: Feeding toe(L) into get_Cs or using C=s·Cmax.
  **Correction**: Calculate the three references from base Oklab L first; use the source’s piecewise rational mapping.

**Error**: Dividing a,b by C or using a cusp helper at a neutral.
  **Correction**: Branch on C=0, set s=0 and l=toe(L), and use a stated conventional hue.

**Error**: Treating Okhsl as an accessible palette guarantee or universal drop-in HSL replacement.
  **Correction**: It is a distinct coordinate model; verify destination output, actual pairs and interaction for the use case.

# Common Confusions


**Confusion**: Okhsl and Okhsv are the same space with one renamed axis.
  **Clarification**: They use distinct remappings and tradeoffs. Neither model name makes corresponding numbers equivalent to each other or to HSL.

# Source Reference

"Okhsl" and "Introducing two new color spaces: Okhsv and Okhsl" sections, Okhsv and Okhsl (Björn Ottosson).

# Verification Notes


This full available-evidence review checked the construction, toe order, helper inputs, rational saturation map and table profile against the complete prepared picker article and accepted Slice17 Oklab/conversion terminology. The synthetic fixture is arithmetic only, not a measured colour. Exact neutral conventions are explicit recipes; omitted gamut helpers were not executed. Figures were not visually inspected; original capture fidelity, browser behavior and accessibility remain unverified. Extraction-confidence metadata is unchanged.
