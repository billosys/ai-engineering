---
concept: LMS Cone Responses
slug: lms-cone-responses
category: visual-perception
subcategory: photoreceptor physiology
tier: foundational
layer: 0-perception
source: "A Perceptual Color Space for Image Processing"
source_slug: posts
authors: "Bj\u00f6rn Ottosson"
chapter: "Converting from XYZ to Oklab"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: medium
aliases:
  - []
prerequisites:
  - colour-space
extends:
  - []
related:
  - xyz-colour-space
  - oklab
  - matrix-transformation-colour
contrasts_with:
  - []
answers_questions:
  - "How do you convert between colour spaces for image processing?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition

LMS cone responses are the outputs of the three types of colour-sensitive photoreceptors in the human eye \u2014 Long (L), Medium (M), and Short (S) wavelength cones \u2014 which together form the biological basis for colour perception.

# Core Definition

The source introduces LMS responses as an intermediate computational step in converting colours to Oklab. Given XYZ coordinates, the first matrix multiplication (M1) converts them to "approximate cone responses":

(l, m, s)^T = M1 \u00d7 (X, Y, Z)^T

The matrix M1 is:

M1 = [[+0.8189330101, +0.3618667424, -0.1288597137],
       [+0.0329845436, +0.9293118715, +0.0361456387],
       [+0.0482003018, +0.2643662691, +0.6338517070]]

The source uses lowercase (l, m, s) to denote these approximate cone-space values, distinguishing them from the final Oklab coordinate L (perceived lightness). The word "approximate" signals that M1 does not correspond to a standard cone-response matrix but is instead optimised for Oklab's perceptual goals.

# Prerequisites

- **Colour space** \u2014 LMS is itself a colour space; understanding coordinate systems for colour is a prerequisite.
- **XYZ colour space** \u2014 LMS values are derived from XYZ via matrix multiplication; XYZ must be understood first.

# Key Properties

1. Three channels (l, m, s) corresponding to the long-, medium-, and short-wavelength cone responses.
2. In the Oklab pipeline, LMS values are intermediate \u2014 they are further processed by a cube-root non-linearity and a second matrix.
3. The M1 matrix in Oklab produces "approximate" cone responses, not exact CIE cone-response values.
4. All three components are non-negative for colours within the physical gamut (visible spectrum).

# Construction / Recognition

## To Construct/Create:
1. Start with normalised XYZ coordinates (D65 whitepoint, white = Y=1).
2. Apply M1 matrix multiplication: multiply the 3\u00d71 XYZ column vector by the 3\u00d73 matrix M1.
3. Result is the (l, m, s) approximate cone response tuple.

## To Identify/Recognise:
1. LMS is an intermediate step \u2014 l, m, s values are not directly presented as the output colour; they are transformed further.
2. In the Oklab C++ code, the intermediate variables named `l`, `m`, `s` (before `cbrtf`) correspond to these cone responses.

# Context & Application

- **Typical contexts**: Colour science pipelines that convert between display colour spaces and perceptual colour spaces.
- **Common applications**: Intermediate computation in the XYZ \u2192 Oklab conversion; chromaticity adaptation transforms (von Kries adaptation uses LMS).

# Examples

**Example 1** (from source): In the C++ implementation, the first three lines of `linear_srgb_to_oklab` compute the approximate cone responses l, m, s as linear combinations of the input R, G, B values (with the sRGB\u2192XYZ\u2192LMS matrices concatenated into a single step):
```c
float l = 0.4122214708f * c.r + 0.5363325363f * c.g + 0.0514459929f * c.b;
float m = 0.2119034982f * c.r + 0.6806995451f * c.g + 0.1073969566f * c.b;
float s = 0.0883024619f * c.r + 0.2817188376f * c.g + 0.6299787005f * c.b;
```
(Section: "Converting from linear sRGB to Oklab")

# Relationships

## Builds Upon
- **XYZ colour space** \u2014 LMS is derived from XYZ via matrix multiplication.
- **Human photoreceptor biology** \u2014 The three channels correspond to the three types of cone cells in the human retina.

## Enables
- **Oklab conversion** \u2014 LMS is the required intermediate space before the cube-root non-linearity.
- **Perceptual colour modelling** \u2014 Working in a cone-like space is the foundation of perceptually motivated colour spaces.

## Related
- **Matrix transformation in colour conversion** \u2014 The M1 operation is a canonical matrix transform.

## Contrasts With
- **XYZ** \u2014 XYZ is a linear transform of LMS (they represent the same physical information but with different axes).

# Common Errors

- **Error**: Treating the l, m, s in Oklab's M1 output as identical to standard CIE LMS cone fundamentals.
  **Correction**: The source explicitly calls these "approximate" cone responses; M1 is optimised for Oklab's perceptual error, not for exact physiological accuracy.

# Common Confusions

- **Confusion**: The lowercase l in the Oklab pipeline is the same as the uppercase L (perceived lightness).
  **Clarification**: The source uses lowercase l, m, s for the cone-response intermediate values and uppercase L for the final perceived lightness coordinate. They are different quantities at different stages of the pipeline.

# Source Reference

"Converting from XYZ to Oklab"; "Converting from linear sRGB to Oklab" sections.

# Verification Notes

- Definition source: The source states "XYZ coordinates are converted to an approximate cone responses" \u2014 direct quote. The word "approximate" is explicit in the source.
- Confidence rationale: Medium \u2014 the source uses LMS as a computational step without explaining the underlying physiology; the biological definition was inferred from the colour science context.
- Uncertainties: The source does not discuss LMS cone fundamentals in depth or compare M1 to standard LMS matrices (e.g., Hunt-Pointer-Est\u00e9vez). The characterisation as "approximate" is noted but not elaborated.
- Cross-reference status: Verified against C++ code listing.
- Rosetta Stone check: No rosetta stone mappings.
- OCR issues: LaTeX matrix equations extracted from context; katex spans ignored.
