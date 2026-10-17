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
The article presents a compact linear-sRGB implementation and an XYZ-form matrix sequence. In the XYZ form, M1 takes XYZ to approximate LMS-like values; in the RGB implementation, combined coefficients already include the linear-sRGB-to-XYZ stage. The forward route is linear transform → pointwise real cube root → linear transform. Its inverse reverses the stages, followed by sRGB encoding for encoded output. Adjacent linear stages compose, but the complete route is nonlinear. Use a matched published coefficient family; the article's 2021 update refers to its linear-sRGB code, not every XYZ matrix. The article’s structural neural-network comparison is an analogy about stages only; it does not claim biological fidelity, learned equivalence, or a measured performance relationship.

# Prerequisites

- **Oklab** — The target space must be understood.
- **XYZ colour space** — The printed XYZ M1 accepts XYZ; the article’s combined linear-sRGB coefficients fold the sRGB-to-XYZ stage into that route. Neither makes XYZ mandatory for conversion.
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
1. Decode encoded sRGB into linear RGB. For the article’s combined route, let (r,g,b) be those linear values.
2. Compute (l,m,s) = A(r,g,b), where A rows are (0.4122214708,0.5363325363,0.0514459929), (0.2119034982,0.6806995451,0.1073969566), and (0.0883024619,0.2817188376,0.6299787005).
3. Apply the componentwise signed real cube root to get (l′,m′,s′). The real cube root accepts negative intermediates.
4. Compute (L,a,b) = B(l′,m′,s′), where B rows are (0.2104542553,0.7936177850,−0.0040720468), (1.9779984951,−2.4285922050,0.4505937099), and (0.0259040371,0.7827717662,−0.8086757660).
5. To reverse this published rounded family, first use the article’s inverse B rows: (1,0.3963377774,0.2158037573), (1,−0.1055613458,−0.0638541728), (1,−0.0894841775,−1.2914855480). Cube each resulting component, then apply inverse A rows: (4.0767416621,−3.3077115913,0.2309699292), (−1.2684380046,2.6097574011,−0.3413193965), (−0.0041960863,−0.7034186147,1.7076147010).
6. Encode linear RGB only when encoded sRGB output is required. Rounded inverse coefficients are approximate, not exact algebraic inverses.

## To Identify/Recognise:
1. The presence of `cbrtf` (cube root) in implementation is the signature of the Oklab non-linearity.
2. Identify the actual input and output domains of each linear stage and the nonlinear transfer between them; other models use different stage structures and should be compared from their own definitions.

# Context & Application

- **Typical contexts**: Any image processing pipeline that requires perceptually uniform colour operations — saturation adjustment, gradient generation, palette design, greyscale conversion.
- **Common applications**: CSS `oklab()` and `oklch()` syntax, image-processing conversion, and selected interpolation or palette workflows. Actual host support and behaviour are outside this source review.

## Cross-Domain Connections
**Mathematics → RIGOROUS**: For already-linear sRGB, the literal operation is a linear transform, pointwise real cube root, then a linear transform. Encoded sRGB first requires decoding. A neural-network comparison is an optional card-author structural analogy, absent from the prepared article; it does not imply physiology or learned equivalence.

# Examples

**Example 1** (from source): The example table provides four verified reference conversions. E.g., XYZ (1.000, 0.000, 0.000) → Oklab (0.450, 1.236, -0.019); XYZ (0.000, 1.000, 0.000) → Oklab (0.922, -0.671, 0.263). (Section: "Table of example XYZ and Oklab pairs")

**Example 2** (worked calculation using the article’s rounded combined linear-sRGB coefficients): For linear RGB (0.2, 0.4, 0.8), A gives (0.338134103, 0.40057808296, 0.63433098782); componentwise real cube roots give (0.6966740886, 0.7371610748, 0.8592218434); B gives approximately Oklab (0.7281433744, −0.0250833833, −0.0997563344). Reversing with the printed rounded inverse rows gives linear RGB approximately (0.2000000251, 0.3999999984, 0.7999998604). The article presents C++ implementations; these equations are a concise mathematical recipe, not a verbatim full listing. (Section: “Converting from linear sRGB to Oklab”)

# Relationships
## Builds Upon
- **LMS-like intermediate coordinates** — The XYZ form produces these with M1 before a signed real cube root.
- **Matrix transformation in colour conversion** — Linear stages operate on their stated input/output domains.
- **XYZ colour space** — One article route starts at XYZ; the combined linear-sRGB code has different coefficients.

## Enables
- **Colour interpolation** — Convert endpoints to the chosen host interpolation space when needed.
- **Palette construction** — Convert coordinates for candidates, then check gamut and rendered pairs.

## Related
- **D65 whitepoint** — Match the reference conditions expected by the chosen coefficient family.
- **sRGB gamut** — Conversion may produce values outside the destination gamut.

# Common Errors
- **Error**: Applying Oklab matrices to gamma-encoded sRGB.
  **Correction**: Decode encoded sRGB first; the article’s combined coefficients accept linear sRGB only.
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
Formulas and article versions were checked against the prepared source. The pipeline description is exact at the stated stage level; numerical examples use the article's literal coefficient family and ordinary precision. The prepared article compares the transform structure with a simple neural network; this is a structural analogy only, not a claim of biological fidelity, learned equivalence, or measured performance.
