---
concept: "Colour Primaries"
slug: "colour-primaries"
category: "colour-theory"
subcategory: "colour-systems"
tier: "foundational"
layer: "2-domain"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "VII. Color"
chapter_number: 7
pdf_page: 371
section: "The Generative Primaries"
extraction_confidence: "high"
aliases:
  - "primary colours"
  - "fundamental primaries (Arnheim)"
  - "generative primaries (Arnheim)"
prerequisites:
  - "hue"
extends: []
related:
  - "hue"
  - "saturation"
  - "complementary-colours"
  - "colour-harmony"
contrasts_with: []
answers_questions:
  - "What is the difference between hue, saturation/chroma, and lightness/value?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Basis vectors in a vector space"
    rating: "rigorous"
    note: "In a fixed linear tristimulus model, independent primary vectors form a basis. Nonnegative bounded mixtures cover their gamut, not all visible colours; encoding, pigment mixing and clipping are separate."
  -
    domain: "mathematics"
    concept: "Linear independence"
    rating: "rigorous"
    note: "A nonsingular primary matrix expresses linear independence over real coefficients. Excluding only positive mixtures of the other two is insufficient."
css_implementation:
  -
    property: "color (RGB primaries for additive)"
    example: "color: rgb(255, 0, 0); /* specified sRGB red primary, bounded gamut */"
    support: "baseline"
  -
    property: "color (optional oklch hue candidates)"
    example: "/* Optional OKLCH hue candidates, not physical primary conversion: red near30deg, yellow near110deg, blue near250deg; check actual gamut */"
    support: "baseline"
---

# Quick Definition

Colour primaries are chosen elements of a specified mixing or compositional system. Arnheim distinguishes generative mixing primaries from his fundamental perceptual RYB account; neither makes three real lights span every visible colour.

# Core Definition

This presents the represented Arnheim account. Exact edition, pages, quotations, named examples, figures, experiments, historical claims and physiological explanations remain unassessed against the unavailable original. Current analytic qualifications do not certify source fidelity.

Arnheim makes a crucial distinction between two entirely different senses of "primary colours," frequently confused in colour theory literature:

**Generative primaries** are "the colors needed to produce a large range of colors physically or physiologically." They are the practical mixing primaries: for additive light mixing (e.g., screens), the generative primaries are red, green, and blue (RGB); for subtractive pigment mixing, they are approximately cyan, magenta, and yellow (CMY). The specific choice of generative primaries is flexible — different applications use different sets. Three independent tristimulus coordinates can describe colour matches under stated observer/reference conditions, but nonnegative mixtures of three real lights cover only their bounded gamut.

**Fundamental primaries** are "the basic pure colors on which the sense of sight builds the organization of color patterns perceptually." Arnheim identifies these as red, yellow, and blue — his represented RYB perceptual framework, not a universal modern trichromatic basis. "Blue, yellow, red — are the fundamental primaries. Whether green should be added as a fourth primary has been a matter of controversy" (Chapter VII, p. 380).

Arnheim emphasises: "There is nothing inviolable about either the number or the nature of generative primaries" (p. 379). The choice depends on the application. The fundamental primaries, by contrast, have a perceptual basis — they are the colours that appear irreducible to direct visual inspection.

A linear tristimulus basis is a current analytic comparison, not a chronology or a claim that pigment mixing and all colour conversions are linear.

# Prerequisites

- **Hue** — Supplies the chromatic vocabulary for selected primary roles.

# Key Properties

1. **Different questions** — Mixing choices and a source's perceptual/compositional primaries are distinct.
2. **Bounded physical gamut** — Three real display primaries do not generate every visible colour with nonnegative channel amounts.
3. **Source-specific fundamentals** — The represented RYB account and green controversy are historical claims, not a modern universal.
4. **Linear basis** — An invertible three-channel linear-response basis spans its vector space; negative coordinates can be outside physical gamut.
5. **Medium/model** — RGB additive, idealised CMY subtractive and artists' RYB conventions need their own materials, whitepoint and scope.

# Construction / Recognition

## To Construct/Create:
1. Identify the medium, chosen primary spectra/materials, observer/reference conditions and whitepoint.
2. Use RGB for a specified additive display model; CMY(K) is a print convention with material limits, and RYB an artist convention.
3. Use Arnheim's fundamental triad only for its attributed compositional analysis. Approximate OKLCH red/yellow/blue angles are candidate labels, not primary conversions.

## To Identify/Recognise:
1. A mixing primary is defined relative to the chosen set and operation.
2. Distinguish a nonsingular linear tristimulus basis from the weaker test that no colour is a positive mixture of the other two.
3. Treat "it does not look like a mixture." as the represented source's irreducibility criterion, not a physical spectral test.

# Context & Application

Colour-system selection separates coordinate specification from pigment and emitted-light mixing. Hue names identify chromatic families; saturation/chroma and light-dark attributes describe other aspects in declared models. A fixed RYB triad is not required for a supplied brand palette.

## Cross-Domain Connections

**Mathematics → RIGOROUS**: Under fixed observer/reference conditions, let the columns of an invertible matrix P be primary tristimulus vectors. Then x=P·c and c=P⁻¹x are literal basis operations. Nonnegative bounded coefficients describe only a realizable gamut; imaginary/negative coordinates can represent values outside it. Encoded RGB must be decoded before linear-light operations. Pigment spectra, nonlinear encoding, clipping and appearance adaptation are separate stages, so a 3×3 step is not a universally exact/lossless full conversion.

**Mathematics → RIGOROUS**: Linear independence means the only real linear combination yielding zero has all coefficients zero. Merely excluding positive mixtures of the other two is insufficient. A nondegenerate primary triangle is a useful chromaticity check under its normalization assumptions, not a proof that its gamut contains every colour.

# Examples

These are retained reported examples from the existing extraction, not independently verified quotations, figures, experiments or historical conclusions.

**Example 1** (p. 379): Arnheim's crucial distinction — "One must draw a clear-cut distinction between generative primaries and fundamental primaries." This clarification is Arnheim's specific contribution to the colour theory discussion — many sources confuse the two.

**Example 2** (pp. 379–380): Helmholtz's warning — the popular conviction that RYB are the "naturally best suited" generative primaries is mistaken: "green could not be obtained by combining a pure blue and a pure yellow light." RYB works for pigment mixing but not for light mixing.

**Example 3** (p. 380–381): The fundamental primaries — "Artists, from the English painter Moses Harris in the eighteenth century to Turner and Delacroix, Goethe, Van Gogh, and Albers, have been in agreement that the color system of the painter is based on the triad of red, blue, and yellow."

**Example 4** (p. 381): The complementary triplet structure — "Since the three fundamental primaries are indivisibly pure, they cannot be related to one another on the basis of a common denominator. Each of them completely excludes the other two." Their structural relationship is mutual exclusion and mutual requiring.

# Relationships

## Builds Upon
- **Hue** — Supplies the chromatic-family vocabulary for comparing selected primary roles.

## Enables
- **Complementary colours** — Complementarity depends on the specified operation and primary/whitepoint choices.
- **Colour harmony** — Triadic/complementary schemes are options within a chosen system.
- **Colour systems** — Generative primaries support a model with defined conditions and gamut.

## Related
- **Colour harmony** — Compositional roles differ from light summation.
- **Colour constancy** — Both concern colour interpretation, but Arnheim's RYB primaries do not establish cone/opponent mechanisms.

## Contrasts With
- **Secondary colours** — Local mixture-role construct; a binary mixture is defined by its actual model/material, not universally perceived as a compound.

# Common Errors

- **Error**: Assuming the painter's RYB primaries apply to digital colour (screens).
  **Correction**: For full specified RGB red and green emitted-light contributions, addition gives RGB yellow. Pigment recipes and CSS interpolation are separate operations.

- **Error**: Treating the generative primaries as absolute — "there are exactly three primaries."
  **Correction**: A three-dimensional linear colour-matching model uses three independent coordinates; real devices can use other primary counts. The "number of primaries" depends on the question: Hering's opponent descriptions, Arnheim's fundamental RYB and additive display primaries have different roles.

# Common Confusions

- **Confusion**: "Primary colours are the same as the strongest or purest colours."
  **Clarification**: Primaries are defined by their role in a compositional system (generative: can produce others; fundamental: perceptually irreducible), not by their intensity or purity.

- **Confusion**: "Because monitors use RGB and print uses CMY, these are the 'real' primaries."
  **Clarification**: Both are valid generative primary systems for their respective physical mixing modes. Neither is more fundamental than the other in an absolute sense; both differ from Arnheim's fundamental primaries (R, Y, B).

# Source Reference

Chapter VII: Color, "Art and Visual Perception," pp. 378–382 (sections "The Generative Primaries," "The Fundamental Primaries").

# Verification Notes

Current bounded review separates appearance, model coordinates and rendering operations as explained above. Technical corrections and local relationship/CQ decisions are same-context proposals; original fidelity and actual rendered/observer outcomes remain unassessed. Extraction-confidence metadata is unchanged.

Legacy extraction notes below are preserved as historical assertions from the predecessor card, **not current verification results**. In particular, their equivalence, chronology, physiology and “Verified” claims are not adopted by this review.

- Definition source: Synthesised from the "Generative Primaries" and "Fundamental Primaries" sections. Arnheim's distinction is explicit and clearly stated.
- Confidence rationale: High — Arnheim's generative/fundamental distinction is one of his most explicit and carefully developed colour theory contributions.
- Uncertainties: Arnheim predates CIELAB (1976) and OKLAB (2020); his fundamental primaries (R, Y, B) differ from modern colour science's CIE standard. The mathematical (Grassmann/linear algebra) treatment is added as cross-domain extension.
- Cross-reference status: Verified — Grassmann's laws (1853) provide the rigorous mathematical foundation for generative primaries as basis vectors. This is fully consistent with Arnheim's phenomenological account.
- Rosetta Stone check: Mappings added (mathematics: basis vectors in colour space, rigorous; linear independence, rigorous).
- OCR issues: None detected.
