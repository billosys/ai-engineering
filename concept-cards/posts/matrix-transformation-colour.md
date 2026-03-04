---
concept: Matrix Transformation in Colour Conversion
slug: matrix-transformation-colour
category: colour-theory
subcategory: colour mathematics
tier: intermediate
layer: 2-domain
source: "A Perceptual Color Space for Image Processing"
source_slug: posts
authors: "Bj\u00f6rn Ottosson"
chapter: "Converting from XYZ to Oklab"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - []
prerequisites:
  - colour-space
  - xyz-colour-space
extends:
  - oklab-conversion
related:
  - lms-cone-responses
  - oklab
  - oklab-conversion
contrasts_with:
  - []
answers_questions:
  - "How do you convert between colour spaces for image processing?"
rosetta_stone:
  - domain: mathematics
    concept: "3\u00d73 matrix multiplication (linear map between vector spaces)"
    rating: rigorous
    note: "The M1 and M2 operations in Oklab are literal 3\u00d73 matrix multiplications \u2014 not an analogy but the exact mathematical operation."
css_implementation: []
---

# Quick Definition

Matrix transformation in colour conversion is the use of 3\u00d73 matrix multiplication to linearly map colour coordinates from one space to another, forming the backbone of the Oklab conversion pipeline.

# Core Definition

The source explicitly presents two 3\u00d73 matrices, M1 and M2, as the primary computational operations in converting between XYZ and Oklab:

**M1** (XYZ \u2192 approximate LMS):

M1 = [[+0.8189330101, +0.3618667424, -0.1288597137],
       [+0.0329845436, +0.9293118715, +0.0361456387],
       [+0.0482003018, +0.2643662691, +0.6338517070]]

**M2** (LMS' \u2192 Lab):

M2 = [[+0.2104542553, +0.7936177850, -0.0040720468],
       [+1.9779984951, -2.4285922050, +0.4505937099],
       [+0.0259040371, +0.7827717662, -0.8086757660]]

The source describes the full pipeline as:

(l, m, s)^T = M1 \u00d7 (X, Y, Z)^T   [then cube root]   (L, a, b)^T = M2 \u00d7 (l', m', s')^T

The inverse pipeline uses M2\u207b\u00b9 and M1\u207b\u00b9. The source notes the matrices were updated in 2021 for higher precision.

# Prerequisites

- **Colour space** \u2014 Understanding that colour coordinates are vectors is required.
- **XYZ colour space** \u2014 M1 takes XYZ as input.

# Key Properties

1. A 3\u00d73 matrix transforms a 3-component colour vector (e.g., XYZ) to another 3-component colour vector (e.g., LMS).
2. Matrix operations are linear: they preserve the relationship between mixed colours (if C = 0.5\u00b7A + 0.5\u00b7B in input, then M\u00b7C = 0.5\u00b7M\u00b7A + 0.5\u00b7M\u00b7B).
3. Invertible matrices allow round-trip conversion; both M1 and M2 must be non-singular.
4. In Oklab, the two matrix steps bracket a non-linear step (cube root); the matrices themselves are purely linear.
5. Concatenating multiple linear transforms into a single matrix is valid: the C++ code combines the sRGB\u2192XYZ and XYZ\u2192LMS steps into one set of coefficients.

# Construction / Recognition

## To Construct/Create:
1. Define the source and target colour space axes.
2. Find (or optimise) the 3\u00d73 coefficient matrix that maps basis colours correctly.
3. Apply: output = M \u00d7 input (standard matrix-vector multiplication).
4. For the inverse: output = M\u207b\u00b9 \u00d7 input (compute the inverse matrix once, apply as a new matrix).

## To Identify/Recognise:
1. Three dot products of the input vector with three coefficient rows \u2014 visible in the C++ code as three weighted sums of r, g, b.
2. The pattern: output_channel = c1\u00b7in1 + c2\u00b7in2 + c3\u00b7in3 for each of three output channels.

# Context & Application

- **Typical contexts**: All colour space conversions in image processing and display pipeline engineering; the sRGB \u2192 XYZ matrix is ubiquitous.
- **Common applications**: GPU shader colour conversion (matrix operations are hardware-accelerated); the Oklab C++ code; CSS Color Level 4 conversion algorithms; ICC profile conversion.

## Cross-Domain Connections

**Mathematics \u2192 RIGOROUS**: The M1 and M2 steps in Oklab conversion are literal 3\u00d73 matrix multiplications \u2014 linear maps between 3-dimensional real vector spaces. This is not an analogy: the operation is mathematically identical to applying a linear transformation in R\u00b3. The invertibility condition (det(M) \u2260 0) must hold for the round-trip conversion to be exact.

# Examples

**Example 1** (from source): M1 is applied to XYZ coordinates to produce approximate cone responses. For D65 white (X=0.950, Y=1.000, Z=1.089), M1 produces l\u2248m\u2248s\u22481 (confirmed by the fact that D65 maps to L=1, a=0, b=0 after the full pipeline). (Section: "Converting from XYZ to Oklab")

**Example 2** (from source): In C++ the two matrix steps are implemented as explicit weighted sums. The first group of three lines computes M1 (combined with sRGB\u2192XYZ); the final three lines of the return statement compute M2. (Section: "Converting from linear sRGB to Oklab")

# Relationships

## Builds Upon
- **Colour space** \u2014 Matrix transforms map between colour spaces.
- **Linear algebra (3\u00d73 matrices)** \u2014 The operation is standard matrix-vector multiplication.

## Enables
- **Oklab conversion** \u2014 M1 and M2 are the two linear steps of the conversion.
- **LMS cone responses** \u2014 M1 produces the approximate cone response vector.
- **All colour space interoperability** \u2014 Virtually all colour space conversions rely on 3\u00d73 matrix steps.

## Related
- **XYZ colour space** \u2014 The source space for M1.
- **Oklab** \u2014 The target space of the combined M1+nonlinearity+M2 pipeline.

## Contrasts With
- **Non-linear colour operations** \u2014 The cube root step in Oklab is non-linear and cannot be represented as a matrix; only the bracketing linear steps are matrices.

# Common Errors

- **Error**: Applying the M1 matrix to gamma-encoded sRGB values instead of linear sRGB.
  **Correction**: The matrix assumes linear input. Decode gamma first.

- **Error**: Confusing the concatenated sRGB-form matrix coefficients in the C++ code with the XYZ-form M1 matrix values given separately.
  **Correction**: The C++ code concatenates sRGB\u2192XYZ and XYZ\u2192LMS into one step; the numerical coefficients differ from the standalone M1 but produce the same result.

# Common Confusions

- **Confusion**: Inverting a colour space conversion means negating the matrix.
  **Clarification**: The inverse is the matrix inverse (M\u207b\u00b9), not the negation (-M). The source explicitly states: "going from Oklab to XYZ is done with M2\u207b\u00b9 and M1\u207b\u00b9."

# Source Reference

"Converting from XYZ to Oklab"; "Converting from linear sRGB to Oklab"; "How Oklab was derived" (matrices M1 and M2 as parameters to optimise).

# Verification Notes

- Definition source: Matrix values and pipeline structure are direct transcription from the source. The description of the operations is explicit.
- Confidence rationale: High \u2014 matrix values, their role, and the inverse pipeline are all explicitly given.
- Uncertainties: None significant.
- Cross-reference status: Verified against C++ code listing and example table.
- Rosetta Stone check: Mathematics/linear-map mapping added as rigorous.
- OCR issues: LaTeX matrix notation extracted from katex-mathml context.
