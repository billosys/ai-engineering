---
concept: "Matrix Transformation in Colour Conversion"
slug: "matrix-transformation-colour"
category: "colour-theory"
subcategory: "colour mathematics"
tier: "intermediate"
layer: "2-domain"
source: "A Perceptual Color Space for Image Processing"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "Converting from XYZ to Oklab"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "high"
aliases: []
prerequisites:
  - "colour-space"
  - "xyz-colour-space"
extends:
  - "oklab-conversion"
related:
  - "lms-cone-responses"
  - "oklab"
  - "oklab-conversion"
contrasts_with: []
answers_questions:
  - "How do you convert between colour spaces for image processing?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "3×3 matrix multiplication (linear map between vector spaces)"
    rating: "rigorous"
    note: "The M1 and M2 operations in Oklab are literal 3×3 matrix multiplications — not an analogy but the exact mathematical operation."
css_implementation: []
---

# Quick Definition
A matrix transformation applies a linear map to coordinates; an affine map additionally permits a translation term.

# Core Definition
For column vectors, a zero-bias matrix operation is linear. Oklab's conversion uses linear transforms around a pointwise real cube-root stage; the complete route is therefore nonlinear. The article prints an XYZ-to-LMS matrix and separately gives combined linear-sRGB coefficients. Do not apply one coefficient set to the other's input. Rounded published coefficients and finite floating-point arithmetic do not guarantee exact round-trip identity.

# Prerequisites

- **Colour space** — Understanding that colour coordinates are vectors is required.
- **XYZ colour space** — M1 takes XYZ as input.

# Key Properties
1. A matrix with no added offset is a linear transformation, not a general affine transformation.
2. Adjacent linear stages may be composed; a nonlinear pointwise cube root cannot be absorbed into one linear matrix.
3. Oklab's XYZ and combined linear-sRGB coefficient rows have different inputs.
4. Rounded coefficients and finite precision produce approximate numerical round trips.

# Construction / Recognition

## To Construct/Create:
1. Define the source and target colour space axes.
2. Find (or optimise) the 3×3 coefficient matrix that maps basis colours correctly.
3. Apply: output = M × input (standard matrix-vector multiplication).
4. For the inverse: output = M⁻¹ × input (compute the inverse matrix once, apply as a new matrix).

## To Identify/Recognise:
1. Three dot products of the input vector with three coefficient rows — visible in the C++ code as three weighted sums of r, g, b.
2. The pattern: output_channel = c1·in1 + c2·in2 + c3·in3 for each of three output channels.

# Context & Application
- **Typical contexts**: Colour-conversion stages that use linear matrices, including the article's Oklab route.
- **Common applications**: Express a specified linear stage compactly; identify input/output coordinate domains before composing matrices.

## Cross-Domain Connections
**Mathematics → RIGOROUS**: The stated M1 and M2 operations are literal matrix multiplications (linear maps for the stated coordinates). The complete conversion includes a nonlinear cube-root stage, and rounded coefficients/finite precision do not guarantee an exact round trip.

# Examples

**Example 1** (from source): M1 is applied to XYZ coordinates to produce approximate cone responses. For D65 white (X=0.950, Y=1.000, Z=1.089), M1 produces l≈m≈s≈1 (confirmed by the fact that D65 maps to L=1, a=0, b=0 after the full pipeline). (Section: "Converting from XYZ to Oklab")

**Example 2** (from source): In C++ the two matrix steps are implemented as explicit weighted sums. The first group of three lines computes M1 (combined with sRGB→XYZ); the final three lines of the return statement compute M2. (Section: "Converting from linear sRGB to Oklab")

# Relationships
## Builds Upon
- **Colour space** — Compatible matrices map between specified coordinate representations.
- **Linear algebra (3×3 matrices)** — Matrix-vector multiplication is the literal operation.

## Enables
- **Oklab conversion** — The article uses linear stages before and after a pointwise nonlinearity.
- **LMS-like intermediates** — The XYZ-form M1 produces fitted approximate values.
- **Colour conversion** — Some routes use 3×3 matrices; not all conversions consist only of them.

## Related
- **XYZ colour space** — Input to the article's printed XYZ-form M1.
- **Oklab** — Its full pipeline includes matrices and a nonlinear stage.

## Contrasts With
- **Nonlinear colour operations** — A pointwise real cube root cannot be represented by a single fixed linear matrix.

# Common Errors
- **Error**: Calling every matrix operation affine or claiming every colour conversion uses a single 3×3 matrix.
  **Correction**: Specify the actual linear/nonlinear stages and coordinate domains.
- **Error**: Demanding exact identity from rounded tables or mixing coefficient families.
  **Correction**: Use internally matched published coefficients and allow finite numeric tolerance.

# Common Confusions

- **Confusion**: Inverting a colour space conversion means negating the matrix.
  **Clarification**: The inverse is the matrix inverse (M⁻¹), not the negation (-M). The source explicitly states: "going from Oklab to XYZ is done with M2⁻¹ and M1⁻¹."

# Source Reference

"Converting from XYZ to Oklab"; "Converting from linear sRGB to Oklab"; "How Oklab was derived" (matrices M1 and M2 as parameters to optimise).

# Verification Notes
The transformation stages were checked against Ottosson's printed formulas. Exact algebraic composition is distinguished from finite numerical results; no general-purpose converter was introduced.
