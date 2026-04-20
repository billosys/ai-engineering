---
# === CORE IDENTIFICATION ===
concept: Figure-Ground
slug: figure-ground

# === CLASSIFICATION ===
category: visual-perception
subcategory: perceptual-organisation
tier: foundational
layer: 0-perception

# === PROVENANCE ===
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: art-and-visual-perception
authors: "Rudolf Arnheim"
chapter: "V. Space"
chapter_number: 5
pdf_page: 141
section: "Figure and Ground"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - figure/ground
  - positive and negative space
  - foreground-background

# === TYPED RELATIONSHIPS ===
prerequisites:
  - []
extends:
  - []
related:
  - depth-levels
  - pictorial-space
  - contour-rivalry
  - negative-space
contrasts_with:
  - depth-levels

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the gestalt principles of perceptual grouping, and how does each one work?"
  - "What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "How do you systematically audit an existing interface for visual design quality? What checklist of principles and patterns do you evaluate, in what order?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: engineering
    concept: "z-index layering (foreground vs background elements)"
    rating: rigorous
    note: "The figure-ground distinction is the simplest case of z-index logic: foreground elements have higher z-index than background elements."
  - domain: mathematics
    concept: "Set partitioning (complementary sets)"
    rating: structural
    note: "Figure and ground are complementary: every region of the visual field belongs to one or the other, making them a partition of the image plane."

css_implementation:
  - property: "z-index"
    example: "z-index: 1; /* figure */ z-index: 0; /* ground */"
    support: baseline
  - property: "background-color"
    example: "background-color: var(--surface-ground);"
    support: baseline
---

# Quick Definition

Figure-ground is the perceptual organisation of the visual field into a bounded, object-like shape (figure) that stands in front of an unbounded, continuous background (ground). It is the most elementary form of spatial depth in pictures.

# Core Definition

Arnheim, following Edgar Rubin, defines figure-ground as a two-plane spatial organisation where one surface is enclosed and perceived as an object (figure), while the other is unbounded and experienced as a continuous backdrop (ground). The figure appears denser, more object-like, and lies in front of the ground. The contour that separates them belongs perceptually to the figure, not the ground.

Key factors that determine which region becomes figure (Rubin's rules, as cited by Arnheim):
1. **Enclosure**: the surrounded area tends to be figure.
2. **Size**: the smaller area tends to be figure.
3. **Symmetry**: the more symmetrical region tends to be figure.
4. **Convexity**: convex regions tend to be figure; concave regions tend to be ground.
5. **Brightness**: brighter regions tend toward figure; saturated red advances more than blue.
6. **Orientation**: regions whose axes align with vertical/horizontal framework of the visual field tend to become figure.
7. **Motion**: a moving element against a stationary ground strongly acquires figure character.

The relationship is dynamic, not static: figure has active, advancing character; ground is passive, recessive, and "continues beneath" the figure.

# Prerequisites

None — figure-ground is perceptually primitive; it requires no learned concepts.

# Key Properties

1. Contour ownership: the shared boundary belongs to the figure, leaving the ground without a boundary of its own.
2. Figure appears denser, more solid, more object-like than ground.
3. Ground is perceived as continuous, passing behind the figure uninterrupted.
4. The relationship is often ambiguous (reversible figure-ground patterns).
5. Figure-ground is the minimum case of pictorial space — the simplest possible depth relationship.
6. Negative space (ground regions) must be actively managed in composition; they have perceptual weight and shape.

# Construction / Recognition

## To Construct/Create:
1. Create an enclosed bounded region against an unbounded surround — this is the minimal figure-ground.
2. Reinforce figure quality: make the figure smaller, more symmetrical, more convex, brighter, or more saturated than its ground.
3. Manage negative spaces actively — they have their own shape and will be perceived.
4. Avoid ambiguous figure-ground when clarity is needed; exploit it deliberately when ambiguity is desired.

## To Identify/Recognise:
1. Which region is enclosed/bounded? That is the figure candidate.
2. Which region continues beneath? That is the ground.
3. Is the boundary ambiguous — can either region claim it? If so, figure-ground rivalry exists.
4. Check: does the "figure" have greater density, more solidity, more convexity?

# Context & Application

- **Typical contexts**: All visual design. Every element on a screen, page, or canvas is figure against some ground.
- **Common applications**: UI element visibility (button vs. background), text legibility (type as figure against page ground), icon design (positive shape vs. negative space), logo design (exploiting ambiguous figure-ground for double-readings), layout (ensuring content elements have sufficient figure quality against background).

## Cross-Domain Connections

**Engineering → RIGOROUS**: z-index implements figure-ground — elements with higher z-index claim the "figure" position visually. Background colours define the ground; foreground UI components define the figure.

**Mathematics → STRUCTURAL**: Figure and ground partition the image plane into complementary sets. The boundary (contour) is the interface between them, and its "ownership" is a perceptual asymmetry, not a geometric one.

# Examples

**Example 1** (p. 107): "The surrounded surface tends to be seen as figure, the surrounding, unbounded one as ground." — Arnheim paraphrasing Rubin.

**Example 2** (p. 109): The goblet / two-faces ambiguity — the goblet is an enclosed symmetric form; the two facing profiles are the concave negative spaces. Either region can flip to figure.

**Example 3** (p. 180): Douris's Greek cup — the carefully shaped negative black spaces between the figures are strong enough in figure quality to create a continuous interlocking surface of red and black.

**Example 4** (UI): A modal overlay exploits figure-ground: the darkened scrim is ground, the modal card is figure. The scrim's continuous expanse and lower brightness reinforce its ground status.

# Relationships

## Builds Upon
- Nothing — this is a foundational perceptual primitive.

## Enables
- **Depth Levels** — Extending figure-ground to multiple overlapping planes.
- **Overlap Depth Cue** — Depends on figure-ground: the occluded element is forced behind.
- **Negative Space** — The ground in a composition is what designers call negative space.
- **Pictorial Space** — Figure-ground is the simplest possible pictorial space.

## Related
- **Contour Rivalry** — What happens when two adjacent regions equally claim a shared boundary.
- **Pictorial Space** — Figure-ground is the two-plane special case of pictorial space.

## Contrasts With
- **Depth Levels** — Figure-ground requires one unbounded region; depth levels extend the concept to multiple bounded planes, none needing to be endless.

# Common Errors

- **Error**: Treating background (ground) elements as perceptually neutral or irrelevant.
  **Correction**: Ground regions have shape, perceptual weight, and can acquire figure quality. Negative spaces in a layout actively affect the reading of the composition.

- **Error**: Relying on colour alone to distinguish figure from ground.
  **Correction**: Colour is only one of many figure-ground cues. Enclosed shape, size, symmetry, and convexity are equally or more powerful.

# Common Confusions

- **Confusion**: Figure = foreground element; ground = background layer.
  **Clarification**: While roughly true, the distinction is perceptual, not just about layering. A large, bright, convex background shape can become figure; a small, dim, irregular foreground shape can recede to ground.

- **Confusion**: Figure-ground is fixed by the image.
  **Clarification**: Figure-ground is often ambiguous and can flip. Artists exploit this intentionally; designers usually must prevent unintended reversals.

# Source Reference

Chapter V: Space, "Art and Visual Perception," pp. 101–115 (Figure and Ground section, with depth levels discussion extending to p. 120).

# Verification Notes

- Definition source: Synthesised from discussion in Chapter V (Space), pp. 101–115; direct references to Rubin's rules are cited explicitly by Arnheim
- Confidence rationale: Figure-ground is one of the most extensively discussed concepts in the chapter; Arnheim's account of Rubin's factors is precise
- Uncertainties: Page numbers approximate (chapter begins at pdf_page 141, section on Figure and Ground follows depth levels intro)
- Cross-reference status: Verified
- Rosetta Stone check: Mapping added — z-index is rigorous; mathematical partition is structural
- OCR issues: None significant
