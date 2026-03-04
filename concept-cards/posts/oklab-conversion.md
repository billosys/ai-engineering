---
concept: Oklab Conversion (sRGB to Oklab)
slug: oklab-conversion
category: colour-theory
subcategory: colour space conversion
tier: intermediate
layer: 2-domain
source: "A Perceptual Color Space for Image Processing"
source_slug: posts
authors: "Bj\u00f6rn Ottosson"
chapter: "Implementation"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - []
prerequisites:
  - oklab
  - xyz-colour-space
  - lms-cone-responses
  - matrix-transformation-colour
extends:
  - oklab
related:
  - d65-whitepoint
  - gamut-srgb
contrasts_with:
  - []
answers_questions:
  - "How do you convert between colour spaces for image processing?"
rosetta_stone:
  - domain: mathematics
    concept: "Composed function: affine transform \u2192 pointwise nonlinearity \u2192 affine transform"
    rating: rigorous
    note: "The sRGB\u2192Oklab conversion is exactly this structure: matrix multiply (M1), then cube-root applied elementwise, then matrix multiply (M2)."
css_implementation:
  - property: "color"
    example: "color: oklab(0.7 0.1 -0.08);"
    support: baseline
---

# Quick Definition

The sRGB-to-Oklab conversion is a three-step pipeline: (1) a 3\u00d73 matrix multiplication to approximate cone responses, (2) a cube-root non-linearity applied elementwise, and (3) a second 3\u00d73 matrix multiplication to produce the final L, a, b coordinates.

# Core Definition

The source provides both the matrix form and the C++ implementation explicitly. The conversion from linear sRGB to Oklab proceeds as:

**Step 1**: Multiply by M1 (concatenating the sRGB\u2192XYZ and XYZ\u2192LMS transforms) to get approximate cone responses (l, m, s).

**Step 2**: Apply cube-root (\u03b3 = 1/3):
l' = l^(1/3), m' = m^(1/3), s' = s^(1/3)

**Step 3**: Multiply by M2 to get (L, a, b):

M2 = [[+0.2104542553, +0.7936177850, -0.0040720468],
       [+1.9779984951, -2.4285922050, +0.4505937099],
       [+0.0259040371, +0.7827717662, -0.8086757660]]

In C++:
```c
Lab linear_srgb_to_oklab(RGB c) {
    float l = 0.4122214708f*c.r + 0.5363325363f*c.g + 0.0514459929f*c.b;
    float m = 0.2119034982f*c.r + 0.6806995451f*c.g + 0.1073969566f*c.b;
    float s = 0.0883024619f*c.r + 0.2817188376f*c.g + 0.6299787005f*c.b;
    float l_ = cbrtf(l);
    float m_ = cbrtf(m);
    float s_ = cbrtf(s);
    return {
        0.2104542553f*l_ + 0.7936177850f*m_ - 0.0040720468f*s_,
        1.9779984951f*l_ - 2.4285922050f*m_ + 0.4505937099f*s_,
        0.0259040371f*l_ + 0.7827717662f*m_ - 0.8086757660f*s_,
    };
}
```

The inverse (Oklab to linear sRGB) applies M2\u207b\u00b9, cubing, then M1\u207b\u00b9.

# Prerequisites

- **Oklab** \u2014 The target space must be understood.
- **XYZ colour space** \u2014 M1 implicitly encodes the sRGB\u2192XYZ\u2192LMS chain.
- **LMS cone responses** \u2014 The intermediate l, m, s values are approximate cone responses.
- **Matrix transformation in colour conversion** \u2014 The algorithm consists of matrix multiplications.

# Key Properties

1. Input must be linear sRGB (gamma must be decoded before conversion).
2. Three steps: M1 \u00d7 (r,g,b) \u2192 cube root \u2192 M2 \u00d7 (l',m',s').
3. The matrices were updated 2021-01-25 for higher precision; current matrices are derived from a high-precision sRGB matrix and exactly matching D65 values.
4. The algorithm is bijective (invertible): Oklab to sRGB uses M2\u207b\u00b9 then cubing then M1\u207b\u00b9.
5. Available in public domain and MIT licence.

# Construction / Recognition

## To Construct/Create:
1. Ensure input RGB is linear (not gamma-encoded sRGB).
2. Compute l = 0.4122214708\u00b7r + 0.5363325363\u00b7g + 0.0514459929\u00b7b (and similarly for m, s).
3. Apply cube root: l' = cbrt(l), m' = cbrt(m), s' = cbrt(s).
4. Compute L = 0.2104542553\u00b7l' + 0.7936177850\u00b7m' - 0.0040720468\u00b7s'.
5. Compute a = 1.9779984951\u00b7l' - 2.4285922050\u00b7m' + 0.4505937099\u00b7s'.
6. Compute b = 0.0259040371\u00b7l' + 0.7827717662\u00b7m' - 0.8086757660\u00b7s'.

## To Identify/Recognise:
1. The presence of `cbrtf` (cube root) in implementation is the signature of the Oklab non-linearity.
2. The two-matrix structure (M1 and M2) distinguishes Oklab from CIELAB (which uses a different non-linearity and single-matrix structure).

# Context & Application

- **Typical contexts**: Any image processing pipeline that requires perceptually uniform colour operations \u2014 saturation adjustment, gradient generation, palette design, greyscale conversion.
- **Common applications**: CSS `oklab()` and `oklch()` functions (browser-native); Photoshop gradient interpolation; game engine colour systems.

## Cross-Domain Connections

**Mathematics \u2192 RIGOROUS**: The sRGB\u2192Oklab conversion is the composition of two affine transforms (matrix multiplications) with a pointwise non-linear function (cube root) in between. This pattern \u2014 linear transform, then nonlinearity, then linear transform \u2014 is also the structure of a single layer in a neural network (minus the optimisation), and more precisely corresponds to the IPT family of colour transforms from which Oklab inherits its architecture.

# Examples

**Example 1** (from source): The example table provides four verified reference conversions. E.g., XYZ (1.000, 0.000, 0.000) \u2192 Oklab (0.450, 1.236, -0.019); XYZ (0.000, 1.000, 0.000) \u2192 Oklab (0.922, -0.671, 0.263). (Section: "Table of example XYZ and Oklab pairs")

**Example 2** (from source): The full C++ code listing for both `linear_srgb_to_oklab` and `oklab_to_linear_srgb` is provided verbatim. (Section: "Converting from linear sRGB to Oklab")

# Relationships

## Builds Upon
- **LMS cone responses** \u2014 Step 1 produces approximate cone responses.
- **Matrix transformation in colour conversion** \u2014 Both M1 and M2 multiplications.
- **XYZ colour space** \u2014 M1 encodes the sRGB\u2192XYZ\u2192LMS chain.

## Enables
- **Colour interpolation (perceptual)** \u2014 Colours must first be converted to Oklab to interpolate perceptually.
- **Palette construction in Oklab** \u2014 Requires conversion from sRGB to Oklab to manipulate L, C, h.

## Related
- **D65 whitepoint** \u2014 The matrices are calibrated for D65 normalisation.
- **gamut-srgb** \u2014 Conversions operate within (or out of) the sRGB gamut.

# Common Errors

- **Error**: Applying the conversion to gamma-encoded sRGB values (e.g., HTML hex colours) without first linearising.
  **Correction**: Decode gamma first. The source notes: "To compute linear sRGB values, see my previous post."

- **Error**: Using the pre-2021-01-25 matrices, which differ slightly after the third decimal.
  **Correction**: The updated matrices (given in the source) use higher-precision sRGB coefficients and exactly matching D65 values.

# Common Confusions

- **Confusion**: The M1 matrix in the XYZ-form equations and the coefficient rows in the sRGB C++ code are different things.
  **Clarification**: The C++ code combines the sRGB\u2192XYZ and XYZ\u2192LMS steps into a single matrix (M_combined = M1 \u00d7 M_sRGB_to_XYZ), so the coefficients differ numerically from the XYZ-form M1, but the operations are equivalent.

# Source Reference

"Converting from XYZ to Oklab"; "Converting from linear sRGB to Oklab"; C++ code listing.

# Verification Notes

- Definition source: Direct transcription of matrix values, C++ code, and conversion steps from the source.
- Confidence rationale: High \u2014 the full implementation is explicitly provided in the source with numerical coefficients.
- Uncertainties: The concatenation of sRGB\u2192XYZ and XYZ\u2192LMS into the single C++ coefficient rows is inferred from context (not stated explicitly in the article prose).
- Cross-reference status: Verified against example table.
- Rosetta Stone check: Mathematics/composed-function mapping added as rigorous.
- OCR issues: LaTeX matrix content extracted from katex-mathml context; HTML spans ignored.
