---
# === CORE IDENTIFICATION ===
concept: Colour Primaries
slug: colour-primaries

# === CLASSIFICATION ===
category: colour-theory
subcategory: colour-systems
tier: foundational
layer: 2-domain

# === PROVENANCE ===
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: art-and-visual-perception
authors: "Rudolf Arnheim"
chapter: "VII. Color"
chapter_number: 7
pdf_page: 371
section: "The Generative Primaries"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - primary colours
  - fundamental primaries (Arnheim)
  - generative primaries (Arnheim)

# === TYPED RELATIONSHIPS ===
prerequisites:
  - hue
extends: []
related:
  - hue
  - saturation
  - complementary-colours
  - colour-harmony
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between hue, saturation/chroma, and lightness/value?"
  - "What are the three components of HSL, and why is HSL more useful than hex notation for palette construction?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: mathematics
    concept: "Basis vectors in a vector space"
    rating: rigorous
    note: "Generative primaries are basis vectors: any colour in the gamut is a linear combination of the three primaries (by Grassmann's laws); the primary triad spans the colour space as a basis spans a vector space."
  - domain: mathematics
    concept: "Linear independence"
    rating: rigorous
    note: "A set of primaries is valid when no primary can be expressed as an additive mixture of the others — analogous to linear independence of basis vectors; red, green, blue are linearly independent in the sense that no one can be produced by combining the other two."

css_implementation:
  - property: "color (RGB primaries for additive)"
    example: "color: rgb(255, 0, 0); /* pure red additive primary */"
    support: baseline
  - property: "color (oklch fundamental hue anchors)"
    example: "/* Fundamental primaries by hue angle: red ≈ 30°, yellow ≈ 110°, blue ≈ 250° (approximate in OKLCH) */"
    support: baseline
---

# Quick Definition

Colour primaries are the minimal set of hues from which a wide range of other colours can be generated — either by physical/physiological mixing (generative primaries) or by perceptual composition (fundamental primaries), with the two sets differing in important ways.

# Core Definition

Arnheim makes a crucial distinction between two entirely different senses of "primary colours," frequently confused in colour theory literature:

**Generative primaries** are "the colors needed to produce a large range of colors physically or physiologically." They are the practical mixing primaries: for additive light mixing (e.g., screens), the generative primaries are red, green, and blue (RGB); for subtractive pigment mixing, they are approximately cyan, magenta, and yellow (CMY). The specific choice of generative primaries is flexible — different applications use different sets. Thomas Young established that three well-chosen wavelengths suffice to produce all visible colours additively.

**Fundamental primaries** are "the basic pure colors on which the sense of sight builds the organization of color patterns perceptually." Arnheim identifies these as red, yellow, and blue — the three hues that are perceptually irreducible (they look like pure elements, not mixtures) and from which all other hues are perceived as combinations. "Blue, yellow, red — are the fundamental primaries. Whether green should be added as a fourth primary has been a matter of controversy" (Chapter VII, p. 380).

Arnheim emphasises: "There is nothing inviolable about either the number or the nature of generative primaries" (p. 379). The choice depends on the application. The fundamental primaries, by contrast, have a perceptual basis — they are the colours that appear irreducible to direct visual inspection.

Note: Arnheim's account predates the mathematical formalisation of colour spaces. Modern colour science treats primaries as basis vectors in a colour space (Grassmann's laws), which is a rigorous mathematical formulation of the generative primary concept.

# Prerequisites

- **Hue** — Primaries are a subset of hues with special compositional properties.

# Key Properties

1. **Two distinct systems** — Generative primaries (mixing basis) vs. fundamental primaries (perceptual basis); confusing the two creates systematic errors.
2. **Three generative primaries suffice** — Any three well-chosen, mutually non-producible hues can serve as generative primaries for a colour system.
3. **Three fundamental primaries** — Red, yellow, and blue are the perceptually irreducible hues; they are the elements of perceptual colour organisation.
4. **Complementary triplet structure** — The three fundamental primaries are mutually exclusive (no one contains the others) and mutually requiring (absence of any one creates perceived incompleteness).
5. **Flexible generative sets** — RGB (screens), CMY (print), and RYB (traditional painting) are all valid generative primary systems for their respective applications.

# Construction / Recognition

## To Construct/Create:
1. Choose the appropriate primary system for your medium:
   - Screen/digital: RGB (additive primaries)
   - Print: CMY(K) (subtractive primaries)
   - Painter's palette: approximately RYB (traditional)
2. For perceptual/compositional analysis, use fundamental primaries (R, Y, B) as the structural anchors.
3. In OKLCH: specify hues near the fundamental primaries as compositional anchors (red ≈ H 20–40°, yellow ≈ H 100–120°, blue ≈ H 240–270°).

## To Identify/Recognise:
1. A generative primary: it cannot be produced by combining other primaries in the set (in the relevant mixing mode).
2. A fundamental primary: it looks irreducible — "it does not look like a mixture."
3. Green looks like a mixture of blue and yellow under some conditions; red, yellow, and blue typically do not (hence Arnheim's RYB fundamental triad).

# Context & Application

- **Typical contexts**: Colour system selection, palette construction, understanding colour models (RGB, HSL, OKLCH), printing, display calibration.
- **Common applications**: Understanding why RGB (screens) and CMY (print) primaries differ; understanding why the traditional painter's RYB primaries don't match either digital system; using the fundamental primary triad as a structural anchoring principle in palette design.

## Cross-Domain Connections

**Mathematics → RIGOROUS**: By Grassmann's laws of colour additivity (1853), colour mixing is a linear operation. Three independent colours that span the colour space function as a basis: any colour C = a·P₁ + b·P₂ + c·P₃, where P₁, P₂, P₃ are the primaries and a, b, c are mixture coefficients (non-negative for real colours within the gamut). This is identical to the structure of a three-dimensional vector space with a basis. The choice of primaries corresponds to a choice of basis — different bases (RGB vs. XYZ vs. LMS) span the same colour space but use different coordinate systems. Grassmann's laws mean that the 3×3 matrix transform between any two sets of primaries (e.g., sRGB → XYZ) is exact and lossless for colours within the gamut.

**Mathematics → RIGOROUS**: Linear independence is required: no primary can be expressed as a positive combination of the other two. In practice, this means the three primaries, when plotted on a chromaticity diagram, form a triangle rather than collapsing into a line.

# Examples

**Example 1** (p. 379): Arnheim's crucial distinction — "One must draw a clear-cut distinction between generative primaries and fundamental primaries." This clarification is Arnheim's specific contribution to the colour theory discussion — many sources confuse the two.

**Example 2** (pp. 379–380): Helmholtz's warning — the popular conviction that RYB are the "naturally best suited" generative primaries is mistaken: "green could not be obtained by combining a pure blue and a pure yellow light." RYB works for pigment mixing but not for light mixing.

**Example 3** (p. 380–381): The fundamental primaries — "Artists, from the English painter Moses Harris in the eighteenth century to Turner and Delacroix, Goethe, Van Gogh, and Albers, have been in agreement that the color system of the painter is based on the triad of red, blue, and yellow."

**Example 4** (p. 381): The complementary triplet structure — "Since the three fundamental primaries are indivisibly pure, they cannot be related to one another on the basis of a common denominator. Each of them completely excludes the other two." Their structural relationship is mutual exclusion and mutual requiring.

# Relationships

## Builds Upon
- **Hue** — Primaries are a subset of hues with special compositional properties.

## Enables
- **Complementary colours** — The primary structure defines the complementary relationships.
- **Colour harmony** — Harmonic schemes (triadic, complementary) are derived from primary structure.
- **Colour systems** — RGB, CMY, and other practical colour models are built on the generative primary concept.

## Related
- **Colour harmony** — Built on the relationships among primaries and their mixtures.
- **Colour constancy** — The visual system's sensitivity to primaries (via opponent-process channels) underlies constancy.

## Contrasts With
- **Secondary colours** — Secondaries are binary mixtures of primaries; they are perceived as compounds, not irreducible elements.

# Common Errors

- **Error**: Assuming the painter's RYB primaries apply to digital colour (screens).
  **Correction**: Screen displays use additive RGB primaries. Mixing red and green light produces yellow, not brown. The generative primaries differ by medium.

- **Error**: Treating the generative primaries as absolute — "there are exactly three primaries."
  **Correction**: Any well-chosen three hues can serve as generative primaries. Hering's opponent-process theory requires six (black/white, red/green, blue/yellow). Arnheim's fundamental primaries are three (R, Y, B). The "number of primaries" depends on the question being asked.

# Common Confusions

- **Confusion**: "Primary colours are the same as the strongest or purest colours."
  **Clarification**: Primaries are defined by their role in a compositional system (generative: can produce others; fundamental: perceptually irreducible), not by their intensity or purity.

- **Confusion**: "Because monitors use RGB and print uses CMY, these are the 'real' primaries."
  **Clarification**: Both are valid generative primary systems for their respective physical mixing modes. Neither is more fundamental than the other in an absolute sense; both differ from Arnheim's fundamental primaries (R, Y, B).

# Source Reference

Chapter VII: Color, "Art and Visual Perception," pp. 378–382 (sections "The Generative Primaries," "The Fundamental Primaries").

# Verification Notes

- Definition source: Synthesised from the "Generative Primaries" and "Fundamental Primaries" sections. Arnheim's distinction is explicit and clearly stated.
- Confidence rationale: High — Arnheim's generative/fundamental distinction is one of his most explicit and carefully developed colour theory contributions.
- Uncertainties: Arnheim predates CIELAB (1976) and OKLAB (2020); his fundamental primaries (R, Y, B) differ from modern colour science's CIE standard. The mathematical (Grassmann/linear algebra) treatment is added as cross-domain extension.
- Cross-reference status: Verified — Grassmann's laws (1853) provide the rigorous mathematical foundation for generative primaries as basis vectors. This is fully consistent with Arnheim's phenomenological account.
- Rosetta Stone check: Mappings added (mathematics: basis vectors in colour space, rigorous; linear independence, rigorous).
- OCR issues: None detected.
