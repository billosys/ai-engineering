---
concept: "LMS Cone Responses"
slug: "lms-cone-responses"
category: "visual-perception"
subcategory: "photoreceptor physiology"
tier: "foundational"
layer: "0-perception"
source: "A Perceptual Color Space for Image Processing"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "Converting from XYZ to Oklab"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "medium"
aliases: []
prerequisites:
  - "colour-space"
extends: []
related:
  - "xyz-colour-space"
  - "oklab"
  - "matrix-transformation-colour"
contrasts_with: []
answers_questions:
  - "How do you convert between colour spaces for image processing?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition
Oklab's lowercase l, m and s are fitted cone-like intermediate coordinates; they are not direct physiological cone measurements or final uppercase Oklab L.

# Core Definition
In the article's XYZ-form expression, M1 multiplies XYZ to produce approximate l, m, s intermediates, followed by a real cube root and a second transform. The separately printed linear-sRGB code folds the sRGB-to-XYZ and XYZ-to-LMS linear stages into coefficients applied directly to linear RGB. These values serve Oklab's fitted model; the article does not establish physiological accuracy or non-negativity over every extended input domain. Signed real cube roots are defined for negative intermediates.

# Prerequisites

- **Colour space** — LMS is itself a colour space; understanding coordinate systems for colour is a prerequisite.
- **XYZ colour space** — LMS values are derived from XYZ via matrix multiplication; XYZ must be understood first.

# Key Properties
1. Lowercase l/m/s denote Oklab intermediates; uppercase L is the final lightness coordinate.
2. The article's printed XYZ M1 acts on XYZ; its separate linear-sRGB implementation combines stages.
3. 'Approximate cone responses' is a model description, not measured biological activity.
4. Negative intermediate values are possible outside restricted inputs and require signed real cube roots.

# Construction / Recognition

## To Construct/Create:
1. Start with normalised XYZ coordinates (D65 whitepoint, white = Y=1).
2. Apply the published XYZ matrix with the stated order: M1 (3×3) × XYZ column (3×1).
3. Apply the componentwise signed real cube root before the second transform; the resulting lowercase l/m/s values are fitted intermediate coordinates, not measured cone responses.

## To Identify/Recognise:
1. LMS is an intermediate step — l, m, s values are not directly presented as the output colour; they are transformed further.
2. In the Oklab C++ code, the intermediate variables named `l`, `m`, `s` (before `cbrtf`) correspond to these cone responses.

# Context & Application

- **Typical contexts**: Colour science pipelines that convert between display colour spaces and perceptual colour spaces.
- **Common applications**: Intermediate computation in the XYZ → Oklab conversion; chromaticity adaptation transforms (von Kries adaptation uses LMS).

# Examples

**Example 1** (from source): In the C++ implementation, the first three lines of `linear_srgb_to_oklab` compute the approximate cone responses l, m, s as linear combinations of the input R, G, B values (with the sRGB→XYZ→LMS matrices concatenated into a single step):
```c
float l = 0.4122214708f * c.r + 0.5363325363f * c.g + 0.0514459929f * c.b;
float m = 0.2119034982f * c.r + 0.6806995451f * c.g + 0.1073969566f * c.b;
float s = 0.0883024619f * c.r + 0.2817188376f * c.g + 0.6299787005f * c.b;
```
(Section: "Converting from linear sRGB to Oklab")

# Relationships
## Builds Upon
- **XYZ colour space** — The article's XYZ-form M1 maps XYZ into fitted l/m/s intermediates.
- **Human photoreceptor biology** — The terminology is cone-like, but the article's values are not established as physiological cone signals.

## Enables
- **Oklab conversion** — These are the article's intermediate coordinates before the cube-root and opponent transform.
- **Perceptual colour modelling** — The fitted transform is one modelling construction; no physiological equivalence is implied.

## Related
- **Matrix transformation in colour conversion** — M1 is a linear matrix stage for the stated input.

## Contrasts With
- **XYZ** — Different coordinate representations; do not infer universal positivity or direct measured biological correspondence.

# Common Errors
- **Error**: Calling the intermediate values exact cone responses or asserting they are non-negative for all physical/extended colours.
  **Correction**: Describe the fitted approximate intermediate and state input-domain conditions.
- **Error**: Applying the printed XYZ M1 directly to RGB.
  **Correction**: Use the appropriate XYZ or combined linear-sRGB coefficient set.

# Common Confusions

- **Confusion**: The lowercase l in the Oklab pipeline is the same as the uppercase L (perceived lightness).
  **Clarification**: The source uses lowercase l, m, s for the cone-response intermediate values and uppercase L for the final perceived lightness coordinate. They are different quantities at different stages of the pipeline.

# Source Reference

"Converting from XYZ to Oklab"; "Converting from linear sRGB to Oklab" sections.

# Verification Notes
The matrix input and signed-root behavior were checked from the prepared article's two implementations. No physiological measurement or universal-domain claim is made.
