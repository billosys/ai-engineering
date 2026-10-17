---
concept: "Oklab Conversion (sRGB to Oklab)"
slug: "oklab-conversion"
category: "colour-theory"
subcategory: "colour space conversion"
tier: "intermediate"
layer: "2-domain"
source: "A Perceptual Color Space for Image Processing"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "Implementation"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "high"
aliases: []
prerequisites:
  - "oklab"
  - "xyz-colour-space"
  - "lms-cone-responses"
  - "matrix-transformation-colour"
extends:
  - "oklab"
related:
  - "d65-whitepoint"
  - "gamut-srgb"
contrasts_with: []
answers_questions:
  - "How do you convert between colour spaces for image processing?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Linear transform → pointwise real cube root → linear transform"
    rating: "rigorous"
    note: "For already-linear sRGB, the article's route is a linear transform, pointwise real cube root, then a linear transform; encoded sRGB must first be decoded. This is rigorous for the stated composition."
css_implementation:
  -
    property: "color"
    example: "color: oklab(0.7 0.1 -0.08);"
    support: "baseline"
---

# Quick Definition
Oklab conversion from encoded sRGB first decodes to linear sRGB, applies a linear transform, a real cube-root stage and another linear transform; reverse conversion reverses those stages and re-encodes when encoded output is wanted.

# Core Definition
The article presents a compact linear-sRGB implementation and an XYZ-form matrix sequence. In the XYZ form, M1 takes XYZ to approximate LMS-like values; in the RGB implementation, combined coefficients already include the linear-sRGB-to-XYZ stage. The forward route is linear transform → pointwise real cube root → linear transform. Its inverse reverses the stages, followed by sRGB encoding for encoded output. Adjacent linear stages compose, but the complete route is nonlinear. Use a matched published coefficient family; the article's 2021 update refers to its linear-sRGB code, not every XYZ matrix. The neural-network comparison is an analogy, not a biological or learned equivalence.

# Prerequisites

- **Oklab** — The target space must be understood.
- **XYZ colour space** — M1 implicitly encodes the sRGB→XYZ→LMS chain.
- **LMS cone responses** — The intermediate l, m, s values are approximate cone responses.
- **Matrix transformation in colour conversion** — The algorithm consists of matrix multiplications.

# Key Properties
1. Decode encoded sRGB before using linear-sRGB conversion coefficients.
2. Distinguish the XYZ M1 input from the article's combined linear-sRGB coefficients.
3. The full transformation includes pointwise real cube roots; adjacent linear stages alone compose.
4. The inverse reverses stages; re-encode only when encoded sRGB output is needed.
5. The article's 2021 update note applies to its linear-sRGB code. Rounded coefficients do not promise exact equality.

# Construction / Recognition

## To Construct/Create:
1. Ensure input RGB is linear (not gamma-encoded sRGB).
2. Compute l = 0.4122214708·r + 0.5363325363·g + 0.0514459929·b (and similarly for m, s).
3. Apply cube root: l' = cbrt(l), m' = cbrt(m), s' = cbrt(s).
4. Compute L = 0.2104542553·l' + 0.7936177850·m' - 0.0040720468·s'.
5. Compute a = 1.9779984951·l' - 2.4285922050·m' + 0.4505937099·s'.
6. Compute b = 0.0259040371·l' + 0.7827717662·m' - 0.8086757660·s'.

## To Identify/Recognise:
1. The presence of `cbrtf` (cube root) in implementation is the signature of the Oklab non-linearity.
2. The two-matrix structure (M1 and M2) distinguishes Oklab from CIELAB (which uses a different non-linearity and single-matrix structure).

# Context & Application

- **Typical contexts**: Any image processing pipeline that requires perceptually uniform colour operations — saturation adjustment, gradient generation, palette design, greyscale conversion.
- **Common applications**: CSS `oklab()` and `oklch()` functions (browser-native); Photoshop gradient interpolation; game engine colour systems.

## Cross-Domain Connections
**Mathematics → RIGOROUS**: For already-linear sRGB, the literal operation is a linear transform, pointwise real cube root, then a linear transform. Encoded sRGB first requires decoding. The neural-network comparison is a structural analogy only; it does not imply physiology or learned equivalence.

# Examples

**Example 1** (from source): The example table provides four verified reference conversions. E.g., XYZ (1.000, 0.000, 0.000) → Oklab (0.450, 1.236, -0.019); XYZ (0.000, 1.000, 0.000) → Oklab (0.922, -0.671, 0.263). (Section: "Table of example XYZ and Oklab pairs")

**Example 2** (from source): The full C++ code listing for both `linear_srgb_to_oklab` and `oklab_to_linear_srgb` is provided verbatim. (Section: "Converting from linear sRGB to Oklab")

# Relationships

## Builds Upon
- **LMS cone responses** — Step 1 produces approximate cone responses.
- **Matrix transformation in colour conversion** — Both M1 and M2 multiplications.
- **XYZ colour space** — M1 encodes the sRGB→XYZ→LMS chain.

## Enables
- **Colour interpolation (perceptual)** — Colours must first be converted to Oklab to interpolate perceptually.
- **Palette construction in Oklab** — Requires conversion from sRGB to Oklab to manipulate L, C, h.

## Related
- **D65 whitepoint** — The matrices are calibrated for D65 normalisation.
- **gamut-srgb** — Conversions operate within (or out of) the sRGB gamut.

# Common Errors
- **Error**: Applying Oklab matrices to gamma-encoded sRGB.
  **Correction**: Decode first, or use the article's explicitly combined formula with its stated input.
- **Error**: Saying the printed XYZ M1 accepts RGB or dates from the 2021 update.
  **Correction**: Keep XYZ and combined RGB forms and their source notes separate.
- **Error**: Calling the complete pipeline linear or affine.
  **Correction**: Name the pointwise real cube-root stage.

# Common Confusions

- **Confusion**: The M1 matrix in the XYZ-form equations and the coefficient rows in the sRGB C++ code are different things.
  **Clarification**: The C++ code combines the sRGB→XYZ and XYZ→LMS steps into a single matrix (M_combined = M1 × M_sRGB_to_XYZ), so the coefficients differ numerically from the XYZ-form M1, but the operations are equivalent.

# Source Reference

"Converting from XYZ to Oklab"; "Converting from linear sRGB to Oklab"; C++ code listing.

# Verification Notes
Formulas and article versions were checked against the prepared source. The pipeline description is exact at the stated stage level; numerical examples use the article's literal coefficient family and ordinary precision. The article's neural-network comparison is retained only as analogy.
