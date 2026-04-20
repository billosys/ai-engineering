---
# === CORE IDENTIFICATION ===
concept: Contour Rivalry
slug: contour-rivalry

# === CLASSIFICATION ===
category: visual-perception
subcategory: perceptual-organisation
tier: intermediate
layer: 0-perception

# === PROVENANCE ===
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: art-and-visual-perception
authors: "Rudolf Arnheim"
chapter: "V. Space"
chapter_number: 5
pdf_page: 141
section: "Contour Rivalry"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - border rivalry
  - shared contour ambiguity
  - contour ownership

# === TYPED RELATIONSHIPS ===
prerequisites:
  - figure-ground
extends:
  - figure-ground
related:
  - spatial-ambiguity-paradox
  - negative-space
  - overlap-depth-cue
contrasts_with:
  - clear-figure-ground

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the gestalt principles of perceptual grouping, and how does each one work?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: engineering
    concept: "Border/outline ownership in CSS — which element 'owns' the boundary?"
    rating: structural
    note: "In CSS, borders belong to individual elements and cannot be 'shared' — a conceptual contrast to the perceptual phenomenon where contours are claimed by one of two adjacent surfaces."

css_implementation:
  - property: "border"
    example: "/* CSS borders belong to individual elements — no perceptual contour rivalry possible */"
    support: baseline
  - property: "outline"
    example: "/* Use gap between adjacent elements (not shared borders) to prevent visual rivalry */"
    support: baseline
---

# Quick Definition

Contour rivalry occurs when two adjacent shapes both "claim" a shared boundary line, creating visual tension and instability at the border. Each shape attempts to use the contour as its own edge, but perceptually a contour can belong to only one shape at a time.

# Core Definition

Arnheim describes contour rivalry as a direct consequence of contour one-sidedness: "A contour can be monopolized by one of the surfaces bordering on it" (p. 64). When two competing surfaces of similar visual strength both claim a shared boundary, the result is unstable.

"When two similarly qualified competing surfaces both claim the contour, we observe what is known as contour rivalry. Perceived as a whole, the figure looks stable enough, but when we concentrate on the common central vertical we notice a tug-of-war. The sharing of borders is uncomfortable, and the two hexagons exhibit an urge to pull apart" (p. 65).

The underlying cause is the asymmetric nature of figure-ground contour ownership: in any stable figure-ground relationship, the contour belongs to the figure — it is the figure's boundary. The ground has no boundary; it continues beneath the figure. When two surfaces are equally qualified to be figure, neither can fully claim the contour, creating instability.

Perceptual resolution: the visual system often simplifies the situation by assigning contour ownership clearly (one surface becomes figure, claiming the boundary). When this cannot occur, the image oscillates or the two shapes pull apart, as children and brain-perturbed subjects have been shown to draw them as separate shapes with gaps between them.

# Prerequisites

- **Figure-Ground** — Contour rivalry is a breakdown of the stable figure-ground relationship where contour ownership is unambiguous.

# Key Properties

1. Contours can perceptually belong to only one of the two surfaces they separate.
2. When two adjacent surfaces have equal claim to the contour, rivalry results.
3. Rivalry is perceived as visual tension, instability, or an "urge" for the shapes to separate.
4. Under degraded conditions (brief exposure, brain perturbation), rivalry is resolved by drawing the shapes apart with gaps.
5. Convexity wins over concavity for contour ownership (other factors being equal).
6. Symmetry of shape predisposes a region to claim the contour.

# Construction / Recognition

## To Construct/Create (intentionally):
1. Place two shapes of equal visual strength adjacent to each other, sharing a border.
2. Both shapes should have comparable enclosedness, size, and symmetry.
3. The shared boundary will be perceptually unstable — each shape will seem to "want" the contour.

## To Identify/Recognise:
1. Find adjacent shapes sharing a boundary.
2. Ask: which shape "owns" this boundary? Is the answer clear or ambiguous?
3. If staring at the shared boundary creates oscillation or tension, contour rivalry is present.

# Context & Application

- **Typical contexts**: Layout where elements abut without spacing, icon design, border-heavy table layouts, adjacent card grids.
- **Common applications**: In UI design, contour rivalry is generally avoided by introducing spacing (negative space) between adjacent elements. When two elements share a border (e.g., table cells, adjacent buttons), the border ambiguity can create visual tension. Designers resolve this by: (1) making one element clearly figure (higher contrast, enclosure); (2) introducing a gap (negative space prevents rivalry by giving each element its own contour); (3) using a neutral divider line that "belongs" to neither element.

## Cross-Domain Connections

**Engineering → STRUCTURAL**: In CSS, borders belong to individual elements and cannot be shared perceptually. The `border-collapse: collapse` CSS property in tables creates shared cell borders — which can produce mild contour rivalry. The standard resolution is to use `border-collapse: separate` with `border-spacing` to introduce gaps. This is a CSS implementation of the "pull apart" resolution Arnheim identifies.

# Examples

**Example 1** (p. 65): "When two similarly qualified competing surfaces both claim the contour, we observe what is known as contour rivalry. Perceived as a whole, the figure looks stable enough, but when we concentrate on the common central vertical we notice a tug-of-war." — Arnheim

**Example 2** (p. 73): "When young children were asked by Piaget to copy geometric designs in which circles or triangles touched each other, they often eliminated the contact in their reproductions." — Arnheim (showing the perceptual pressure to resolve rivalry by separation)

**Example 3** (p. 73): "People were asked to draw a honeycomb pattern. They often made the hexagons independent of one another by leaving space between them, and even emphasized the interstices by shading the figures." — Arnheim

**Example 4** (UI): Adjacent card components with no gap between them create contour rivalry at their shared edges. The standard resolution in design systems is a minimum gap (e.g., 8px or 16px spacing) between adjacent cards.

# Relationships

## Builds Upon
- **Figure-Ground** — Contour rivalry is the instability case of the figure-ground relationship when contour ownership is ambiguous.

## Enables
- **Spatial Ambiguity/Paradox** — Contour rivalry is one source of visual ambiguity.
- **Negative Space Design** — One resolution of contour rivalry is introducing negative space between adjacent elements.

## Related
- **Spatial Ambiguity/Paradox** — Contour rivalry is a specific, localised form of spatial ambiguity.
- **Negative Space** — Negative space (gaps between elements) is the primary preventive measure against contour rivalry.
- **Overlap Depth Cue** — Overlap resolves contour rivalry by assigning the contour to the front element.

## Contrasts With
- **Clear Figure-Ground** — Stable, unambiguous figure-ground assignment where contour ownership is clear.

# Common Errors

- **Error**: Placing adjacent UI elements with no gap, assuming the shared border is visually stable.
  **Correction**: Shared borders are subject to contour rivalry. Introduce spacing between elements (padding, margin, gap) to give each element its own unambiguous contour.

- **Error**: Using `border-collapse: collapse` in tables without considering the visual tension at shared cell borders.
  **Correction**: For data tables where cell boundaries are important visual signals (not just separators), `border-collapse: separate` with explicit spacing prevents the rivalry ambiguity.

# Common Confusions

- **Confusion**: Contour rivalry only occurs between shapes of equal size.
  **Clarification**: Rivalry occurs when two surfaces are equally qualified by all figure-determining factors (size, symmetry, convexity, enclosure). Unequal elements can still produce rivalry if the factors happen to be balanced.

- **Confusion**: A thin divider line between two shapes resolves contour rivalry.
  **Clarification**: A thin divider line is itself a shape — it introduces a three-element system (left shape, divider, right shape) that can resolve the rivalry if the divider is clearly a separate, neutral element. But if the divider is too thin to register as an independent shape, it may still be claimed by one of the adjacent shapes.

# Source Reference

Chapter V: Space, "Art and Visual Perception," pp. 63–75 (Contour Rivalry section).

# Verification Notes

- Definition source: Synthesised from Arnheim's discussion, pp. 63–75; key quotes cited directly
- Confidence rationale: High — Arnheim gives contour rivalry a dedicated section with precise examples and experimental evidence
- Uncertainties: None significant
- Cross-reference status: Verified
- Rosetta Stone check: Mapping added — CSS border ownership is structural
- OCR issues: None significant
