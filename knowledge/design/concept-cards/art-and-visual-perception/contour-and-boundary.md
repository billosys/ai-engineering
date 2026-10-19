---
concept: "Contour and Boundary"
slug: "contour-and-boundary"
category: "visual-elements"
subcategory: "shape"
tier: "foundational"
layer: "0-perception"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "II. Shape"
chapter_number: 2
pdf_page: 31
section: "What Is Shape? / The Structural Skeleton"
extraction_confidence: "medium"
aliases:
  - "outline"
  - "edge"
  - "boundary"
  - "silhouette contour"
prerequisites: []
extends: []
related:
  - "visual-shape"
  - "structural-skeleton"
  - "visual-subdivision"
  - "figure-ground"
contrasts_with:
  - "structural-skeleton"
answers_questions:
  - "What are the gestalt principles of perceptual grouping, and how does each one work?"
  - "An icon set mixes outlined and filled styles, some at 16px and some at 24px, some with rounded corners and some with sharp corners. It feels 'off.' What principle was violated?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Boundary of a set in topology"
    rating: "structural"
    note: "For a specified set in an ambient topological space, its boundary is its closure minus its interior. This can model an explicit geometric edge, but an implied contour or contextual boundary assignment is not thereby the same mathematical object."
css_implementation:
  -
    property: "border / outline / box-shadow"
    example: "border: 1px solid currentColor; /* Explicit contour */"
    support: "baseline"
  -
    property: "clip-path"
    example: "clip-path: polygon(50% 0%, 100% 100%, 0% 100%); /* Defines triangle contour */"
    support: "baseline"
  -
    property: "SVG stroke"
    example: "<path stroke='currentColor' stroke-width='2' fill='none' d='M...' />"
    support: "baseline"
---

# Quick Definition

Contour names an explicit or implied boundary in a visual representation: a drawn line, silhouette edge, colour transition or arrangement of endings. Physical boundaries constrain appearance, while viewpoint and context affect which contour and shape a viewer perceives.

# Core Definition

This section presents the represented Arnheim account. Its quotations, page references and historical or experimental reports have not been checked against the unavailable original; current analytic qualifications below do not certify that fidelity.

Arnheim establishes that "the physical shape of an object is determined by its boundaries — the rectangular edge of a piece of paper, the two surfaces delimiting the sides and the bottom of a cone" (Chapter II, p. 36). However, contour alone does not constitute shape. Light "travels in straight lines, and therefore the projections formed on the retinas correspond only to those parts of the outer surface that are linked to the eyes by straight lines" — a viewpoint-based account of visible surfaces, not proof that every contour is a physical or incomplete edge. More importantly, "in speaking of 'shape' we refer to two quite different properties of visual objects: (1) the actual boundaries produced by the artist: the lines, masses, volumes, and (2) the structural skeleton created in perception by these material shapes, but rarely coinciding with them" (p. 63). A contour can exist without being seen as a closed shape (as in virtual boundaries created by line endings, as in Pio Semproni's figure, p. 58), and a recognisable shape can be depicted by its structural axis alone, without any outline.

# Prerequisites

No internal prerequisite is recorded in this extraction; this is not evidence that no other concept could aid understanding.

# Key Properties

1. **Physical vs. perceptual** — Material edges and markings can supply cues; perceived boundary organisation also includes implied contours and contextual assignment.
2. **Viewpoint-dependent** — What contours are visible depends on the angle of observation; "the eyes receive information only about outer, not inner, shapes."
3. **Virtual contour** — Contour can be implied without being drawn: a sequence of line endings, dot arrays, or colour transitions can constitute a perceived boundary without a continuous line.
4. **Not identical to shape** — Axes, interior features and context can contribute to shape character beyond a literal contour.

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

**Mathematics → STRUCTURAL**: For a specified set A in an ambient topological space, the boundary is closure(A) minus interior(A). It need not separate space into two simple regions. This models some geometric edges, not every physical, implied or contextually assigned contour; the ambient topology and set must first be specified.

# Examples

**Example 1** (p. 58–59): In Pio Semproni's drawing, the outlines of a white figure are rendered entirely by the endings of vertical background lines — "each of which contributes a point-sized element to the virtual boundary." Contour without a continuous line.

**Example 2** (p. 37): "When a person who has been asked what a winding staircase looks like describes with his finger a rising spiral, he is not giving the outline but the characteristic main axis, actually nonexistent in the object." The axis (structural skeleton) can substitute for the contour in communicating shape.

**Example 3** (p. 19–20, implied): Camouflage works by disrupting the contour's ability to generate a clear structural skeleton: the represented account describes changed crossings and symmetries as obscuring a reading. This is a contextual illustration, not proof that a uniquely defined skeleton is destroyed.

# Relationships

The following are scoped conceptual reading connections. In the represented account, simplicity, axes and grouping explain one another; these links do not establish causal neural mechanisms. Unnamed downstream uses and ordinary comparisons are not automatically resolved card identities.

## Builds Upon
- (No internal prerequisite recorded in this extraction; this is not proof of absence.)

## Enables
- **Visual Shape** — Explicit and implied boundaries constrain perceived shape without determining it alone.
- **Structural Skeleton** — Contour cues can support an inferred axis framework in Arnheim's simplicity account; this is not a unique extraction algorithm.
- **Visual Subdivision** — Boundaries between regions are what enable the visual field to be parsed into distinct objects.

## Related
- **Figure-Ground Relationship** — Contour is shared between figure and ground; which region "owns" the contour determines which is seen as figure.
- **Perceptual Grouping by Similarity** — Similarity of contour shape is a grouping factor across separate elements.

## Contrasts With
- **Structural Skeleton** — Contour is the material input; the skeleton is the perceptual output. They often differ significantly: the same contour can generate different skeletons in different contexts, and the same skeleton can be embodied by very different contours.

# Common Errors

- **Error**: Assuming that defining the outline precisely defines the perceived shape.
  **Correction**: Inspect contour, interior relationships and perceived axes together. Similar axis descriptions need not produce the same category or appearance.

- **Error**: Using explicit outlines as the only way to define shape.
  **Correction**: Virtual contours from endings, transitions or textures can suggest a boundary; they need not look or function exactly like a drawn outline.

# Common Confusions

- **Confusion**: Contour and silhouette are the same thing.
  **Clarification**: A silhouette is the filled form defined by the outer contour; contour refers specifically to the boundary edge. An outlined icon has explicit contour lines; a filled icon's contour is the silhouette edge. Even with matched outer geometry, fill, stroke and context can change visual weight and perceived organisation.

# Source Reference

Chapter II: Shape, "Art and Visual Perception," pp. 36–38, 58–59, 63–65. Sections: "What Is Shape?" and "The Structural Skeleton."

# Verification Notes

The bullets below preserve historical extraction assertions, including their confidence, cross-reference, OCR and source-reading claims; they are not current verification. The represented original edition/page basis is unavailable, so fidelity of all quotations, locators, figures, experiments and historical claims remains unassessed. Current technical corrections and scoped analogies do not establish a neural mechanism, cultural universality or measured usability.

- Definition source: Synthesised from pp. 36, 63 — Arnheim discusses contour/boundary as the physical basis of shape perception and explicitly distinguishes it from the structural skeleton.
- Confidence rationale: Medium — contour is not defined as a named concept in a dedicated section; the distinction from skeleton is clearly made but the definition must be assembled from multiple passages.
- Uncertainties: Arnheim does not use "contour" as a technical term with a single clean definition; this card synthesises his usage.
- Cross-reference status: Verified — connects to visual-shape, structural-skeleton, visual-subdivision.
- Rosetta Stone check: Mapping added (mathematics/topology boundary, structural).
- OCR issues: None relevant to this section.
