---
concept: "HSL Colour Space"
slug: "hsl"
category: "colour-theory"
subcategory: "colour-models"
tier: "foundational"
layer: "2-domain"
source: "Okhsv and Okhsl"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "HSL"
chapter_number: null
pdf_page: null
section: "Color spaces for color picking"
extraction_confidence: "high"
aliases:
  -
    - "Hue Saturation Lightness"
    - "HSLA"
prerequisites: []
extends: []
related:
  - "hsv"
  - "hsl-css-syntax"
  - "okhsl"
contrasts_with:
  - "hsv"
  - "okhsl"
answers_questions:
  - "What distinguishes Okhsl from Okhsv, and when would you use each?"
rosetta_stone: []
css_implementation:
  -
    property: "color / background-color"
    example: "hsl(150, 50%, 50%);"
    support: "baseline"
  -
    property: "color / background-color"
    example: "hsla(150, 50%, 50%, 0.5);"
    support: "baseline"
---

# Quick Definition


HSL is an RGB-derived coordinate transformation using hue, saturation and lightness. The normalized classic formulas below apply to encoded sRGB r,g,b∈[0,1]; HSL S is not CIE saturation, and HSL L is not physical brightness or perceptual lightness.

# Core Definition


For encoded sRGB let M=max(r,g,b), m=min(r,g,b), Δ=M−m, and L=(M+m)/2. Then HSL S=0 when Δ=0; otherwise S=Δ/(1−|2L−1|). For Δ>0, define h′=(g−b)/Δ when M=r, (b−r)/Δ+2 when M=g, and (r−g)/Δ+4 when M=b; H=60·(h′ mod 6) degrees. Hue is powerless for achromatic colours. The model is a transform from a source RGB space, not an independent perceptual space. This formula is a bounded normalized example, distinct from CSS syntax rules and extended values. CSS HSL resolves to sRGB: modern syntax accepts numeric or percentage S/L on a 0–100 reference scale, while legacy comma syntax requires percentages; hue angles wrap. Sass examples are historical Sass, not standalone CSS.

# Prerequisites

- **RGB colour model** — HSL is a transformation of RGB values to alternative coordinates

# Key Properties


1. HSL parameters are derived from a specified RGB encoding; the classic formulas here use encoded sRGB in [0,1].
2. S=0 gives gray at every L; hue is powerless whenever Δ=0. Black and white make the saturation denominator degenerate, so use the Δ=0 branch.
3. HSL L=(M+m)/2 is not WCAG relative luminance or a perceptually uniform brightness scale.
4. CSS modern HSL accepts S/L numbers or percentages on a 0–100 reference scale; legacy comma syntax requires percentages. Hue wraps, and HSL resolves to sRGB.

# Construction / Recognition

## To Construct/Create:

1. For classic encoded sRGB, calculate M, m, Δ and L=(M+m)/2.
2. If Δ=0, set S=0 and use a conventional hue only if an interface needs one. Otherwise calculate S=Δ/(1−|2L−1|) and hue from the channel ordering.
3. For CSS, follow the selected modern or legacy syntax. Modern numeric S/L use 0–100 reference values; legacy comma syntax requires percentages.
4. Check rendered output for the actual destination and use relative luminance, not HSL L, for contrast calculations.

## To Identify/Recognise:

1. Recognize modern space-separated/slash syntax and legacy comma syntax as distinct accepted forms.
2. Modern S/L numbers and percentages both use a 0–100 reference range; the legacy comma form requires percentages.
3. Hue is an angle that wraps; S=0 makes hue powerless.
4. Sass code and preprocessor functions must be identified as Sass, not standalone CSS.

# Context & Application

- **Typical contexts**: CSS colour authoring, design tool colour pickers, generative colour loops in JavaScript/Sass
- **Common applications**: Drasner notes that "looping through the hue from 0 to 360 will give you a full range," making HSL well-suited for generative colour sequences; adjusting lightness/saturation for hover states; theming

# Examples


**Example 1** (from prepared Drasner source): `hsla(150, 50%, 50%, 0.5)` is a legacy comma-form example.

**Example 2** (current CSS syntax): `hsl(180 100 50 / 50%)` and `hsl(180 100% 50% / 50%)` use equivalent modern S/L reference values; `hsl(180, 100, 50)` is invalid legacy syntax because S/L need percentages.

**Example 3** (arithmetic witness, encoded sRGB): r,g,b=(.8,.2,.2) gives Δ=.6, L=.5 and S=.6; neutral (.5,.5,.5) gives S=0 and no measured hue.

# Relationships

## Builds Upon

- **sRGB colour model** — CSS HSL resolves to sRGB; classic equations here use encoded sRGB in [0,1].

## Enables

- **Okhsl** — Ottosson introduces a distinct Oklab-derived alternative for picker use, not a numeric-compatible replacement.
- **Generative colour** — Hue iteration can enumerate coordinates; it does not promise even perceived steps.

## Related

- **HSV** — Both re-parameterize RGB but their saturation and third-coordinate definitions differ.
- **Munsell colour system** — Drasner makes an attributed conceptual comparison; it does not show direct derivation.

## Contrasts With

- **Okhsl** — Different formulas and parameter meanings; matching labels do not make values interchangeable.
- **HSV** — HSL S and HSV S use different formulas.

# Common Errors


**Error**: Assuming HSL grey occurs only at L=.5, or that S=0 has a meaningful hue.
  **Correction**: S=0 is gray at every L, and hue is powerless for achromatic values.

**Error**: Using HSL L as brightness or contrast luminance.
  **Correction**: It is an RGB-derived coordinate; compute contrast from the actual rendered pair.

**Error**: Treating modern numeric S/L as 0–1 or allowing bare numbers in legacy comma syntax.
  **Correction**: Modern numeric S/L use the 0–100 reference scale; legacy comma syntax requires percentages.

# Common Confusions

- **Confusion**: HSL Saturation represents true perceptual saturation.
  **Clarification**: Ottosson notes it "is not comparable to" true saturation; the original paper called it "relative chroma," which is more accurate.

- **Confusion**: HSL is a colour space in its own right.
  **Clarification**: Ottosson notes "HSL and HSV are not quite color spaces on their own, they are transformations from a source RGB color space." The precise values depend on which RGB primaries are used.

# Source Reference

"HSL" section under "Color spaces for color picking," Okhsv and Okhsl; "HSL Values" section, Working With Colors Guide.

# Verification Notes



This full available-evidence review checked the classic normalized encoded-sRGB formula against the prepared picker article and checked CSS syntax against CSS Color 4 CRD 2026-10-09 §§7–7.2 and the linked accepted `hsl-css-syntax` card. Formula examples are bounded arithmetic witnesses, not a claim about all CSS extended values. Prepared Drasner syntax is distinguished from current CSS; original capture fidelity, browser behavior and actual rendered contrast were not tested. Extraction-confidence metadata remains unchanged.
