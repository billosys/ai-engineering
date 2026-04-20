---
# === CORE IDENTIFICATION ===
concept: Contour and Boundary
slug: contour-and-boundary

# === CLASSIFICATION ===
category: visual-elements
subcategory: shape
tier: foundational
layer: 0-perception

# === PROVENANCE ===
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: art-and-visual-perception
authors: "Rudolf Arnheim"
chapter: "II. Shape"
chapter_number: 2
pdf_page: 31
section: "What Is Shape? / The Structural Skeleton"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - outline
  - edge
  - boundary
  - silhouette contour

# === TYPED RELATIONSHIPS ===
prerequisites:
  []
extends:
  []
related:
  - visual-shape
  - structural-skeleton
  - visual-subdivision
  - figure-ground
contrasts_with:
  - structural-skeleton

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the gestalt principles of perceptual grouping, and how does each one work?"
  - "An icon set mixes outlined and filled styles, some at 16px and some at 24px, some with rounded corners and some with sharp corners. It feels 'off.' What principle was violated?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: mathematics
    concept: "Boundary of a set in topology"
    rating: structural
    note: "The topological boundary of a region — the set of points that separate inside from outside — corresponds to contour as Arnheim defines it: the physical boundary that delimits a shape without exhausting its perceptual character."

css_implementation:
  - property: "border / outline / box-shadow"
    example: "border: 1px solid currentColor; /* Explicit contour */"
    support: baseline
  - property: "clip-path"
    example: "clip-path: polygon(50% 0%, 100% 100%, 0% 100%); /* Defines triangle contour */"
    support: baseline
  - property: "SVG stroke"
    example: "<path stroke='currentColor' stroke-width='2' fill='none' d='M...' />"
    support: baseline
---

# Quick Definition

Contour is the physical boundary — lines, edges, surfaces — that delimits an object's extent in space and initiates shape perception, while being distinct from the perceived shape itself, which also depends on the structural skeleton the contour generates.

# Core Definition

Arnheim establishes that "the physical shape of an object is determined by its boundaries — the rectangular edge of a piece of paper, the two surfaces delimiting the sides and the bottom of a cone" (Chapter II, p. 36). However, contour alone does not constitute shape. Light "travels in straight lines, and therefore the projections formed on the retinas correspond only to those parts of the outer surface that are linked to the eyes by straight lines" — meaning contour is always partial, viewpoint-dependent. More importantly, "in speaking of 'shape' we refer to two quite different properties of visual objects: (1) the actual boundaries produced by the artist: the lines, masses, volumes, and (2) the structural skeleton created in perception by these material shapes, but rarely coinciding with them" (p. 63). A contour can exist without being seen as a closed shape (as in virtual boundaries created by line endings, as in Pio Semproni's figure, p. 58), and a recognisable shape can be depicted by its structural axis alone, without any outline.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. **Physical vs. perceptual** — Contour is the physical edge; the structural skeleton it generates is the perceptual outcome.
2. **Viewpoint-dependent** — What contours are visible depends on the angle of observation; "the eyes receive information only about outer, not inner, shapes."
3. **Virtual contour** — Contour can be implied without being drawn: a sequence of line endings, dot arrays, or colour transitions can constitute a perceived boundary without a continuous line.
4. **Not identical to shape** — The structural skeleton rarely coincides with the literal contour; shape character is determined by the skeleton.

# Construction / Recognition

## To Construct/Create:
1. Draw or define the actual boundary (outline, edge, silhouette).
2. Separately identify the structural skeleton the contour implies — the dominant axes, symmetry lines, major directional forces.
3. Verify that the skeleton communicates the intended shape character (not just that the outline is "correct").
4. Consider virtual contour: can the boundary be implied without being drawn? (Useful for negative space, overlapping shapes, halftone-like structures.)

## To Identify/Recognise:
1. Is the boundary continuous (explicit contour) or implied (virtual contour from line endings, colour differences, texture gradients)?
2. Does the literal boundary match the perceived shape character? If not, the structural skeleton is diverging from the contour — a significant perceptual fact.

# Context & Application

- **Typical contexts**: Illustration, icon design, logo design, typographic letterform design, UI component styling.
- **Common applications**: A designer choosing between a filled shape and an outlined shape is choosing different contour strategies. An outlined icon creates contour as the primary shape element; a filled icon creates contour as the silhouette edge. Both generate structural skeletons, but the visual weight and figure-ground relationship differ significantly.

## Cross-Domain Connections

**Mathematics → STRUCTURAL**: The topological boundary of a region partitions space into interior and exterior. Arnheim's contour is precisely this: the locus of points where the object gives way to its surroundings. The structural skeleton, however, is an additional perceptual construction not captured by the topological boundary.

# Examples

**Example 1** (p. 58–59): In Pio Semproni's drawing, the outlines of a white figure are rendered entirely by the endings of vertical background lines — "each of which contributes a point-sized element to the virtual boundary." Contour without a continuous line.

**Example 2** (p. 37): "When a person who has been asked what a winding staircase looks like describes with his finger a rising spiral, he is not giving the outline but the characteristic main axis, actually nonexistent in the object." The axis (structural skeleton) can substitute for the contour in communicating shape.

**Example 3** (p. 19–20, implied): Camouflage works by disrupting the contour's ability to generate a clear structural skeleton: when angles are changed to crossings and symmetries are broken, the shape's contour is present but its skeleton is destroyed.

# Relationships

## Builds Upon
- (None — foundational concept)

## Enables
- **Visual Shape** — Contour is the physical input from which perceptual shape is constructed.
- **Structural Skeleton** — The skeleton is created by contour through the operation of Praegnanz; it is the simplest structure the contour permits.
- **Visual Subdivision** — Boundaries between regions are what enable the visual field to be parsed into distinct objects.

## Related
- **Figure-Ground Relationship** — Contour is shared between figure and ground; which region "owns" the contour determines which is seen as figure.
- **Perceptual Grouping by Similarity** — Similarity of contour shape is a grouping factor across separate elements.

## Contrasts With
- **Structural Skeleton** — Contour is the material input; the skeleton is the perceptual output. They often differ significantly: the same contour can generate different skeletons in different contexts, and the same skeleton can be embodied by very different contours.

# Common Errors

- **Error**: Assuming that defining the outline precisely defines the perceived shape.
  **Correction**: The structural skeleton — not the outline — determines shape character. Two contours that generate the same skeleton will be perceived as the same shape type.

- **Error**: Using explicit outlines as the only way to define shape.
  **Correction**: Virtual contours (created by line endings, colour transitions, texture edges) are perceptually equivalent to drawn outlines when sufficiently consistent.

# Common Confusions

- **Confusion**: Contour and silhouette are the same thing.
  **Clarification**: A silhouette is the filled form defined by the outer contour; contour refers specifically to the boundary edge. An outlined icon has explicit contour lines; a filled icon's contour is the silhouette edge. Both generate the same structural skeleton if the shape is identical.

# Source Reference

Chapter II: Shape, "Art and Visual Perception," pp. 36–38, 58–59, 63–65. Sections: "What Is Shape?" and "The Structural Skeleton."

# Verification Notes

- Definition source: Synthesised from pp. 36, 63 — Arnheim discusses contour/boundary as the physical basis of shape perception and explicitly distinguishes it from the structural skeleton.
- Confidence rationale: Medium — contour is not defined as a named concept in a dedicated section; the distinction from skeleton is clearly made but the definition must be assembled from multiple passages.
- Uncertainties: Arnheim does not use "contour" as a technical term with a single clean definition; this card synthesises his usage.
- Cross-reference status: Verified — connects to visual-shape, structural-skeleton, visual-subdivision.
- Rosetta Stone check: Mapping added (mathematics/topology boundary, structural).
- OCR issues: None relevant to this section.
