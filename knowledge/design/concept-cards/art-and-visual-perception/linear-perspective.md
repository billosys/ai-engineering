---
concept: "Linear Perspective"
slug: "linear-perspective"
category: "visual-perception"
subcategory: "depth-cues"
tier: "foundational"
layer: "0-perception"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "V. Space"
chapter_number: 5
pdf_page: 141
section: "Toward a Convergence of Space"
extraction_confidence: "high"
aliases:
  - "central perspective"
  - "convergent perspective"
  - "one-point perspective"
  - "two-point perspective"
prerequisites:
  - "pictorial-space"
  - "size-gradient"
  - "depth-gradient-principle"
extends:
  - "isometric-perspective"
related:
  - "size-gradient"
  - "texture-gradient"
  - "atmospheric-perspective"
  - "height-in-picture-plane"
  - "vanishing-point"
contrasts_with:
  - "isometric-perspective"
  - "flat-pictorial-space"
answers_questions:
  - "What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "How do you systematically audit an existing interface for visual design quality? What checklist of principles and patterns do you evaluate, in what order?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Projective geometry — vanishing points, cross-ratio, perspective transform"
    rating: "rigorous"
    note: "Rigorous for nondegenerate planar projective maps and defined direction families; general 3D projection is not invertible. Cross-ratios require four distinct collinear points and valid domains."
  -
    domain: "mathematics"
    concept: "Linear interpolation / perspective-correct interpolation"
    rating: "rigorous"
    note: "For screen barycentric λ and nonzero homogeneous w, affine-on-triangle attributes use q=(Σλq/w)/(Σλ/w), with nonzero denominator. This is not every CSS animation or arbitrary linear interpolation."
css_implementation:
  -
    property: "perspective"
    example: "perspective: 800px; /* parent perspective on 3D-transformed children */"
    support: "baseline"
  -
    property: "transform: perspective()"
    example: "transform: perspective(600px) rotateY(30deg); /* self transform arrangement */"
    support: "baseline"
---

# Quick Definition

Central perspective maps scene points through a finite projection centre onto an image plane. Each direction family has its own vanishing behavior; appropriate horizontal families share a level horizon, while image-parallel directions have no finite vanishing point.

# Core Definition

This presents the represented Arnheim account alongside current analytic qualifications. Original edition, pages, quotations, figures, experiments, physiology and historical claims remain unassessed; the technical constructions below do not certify source fidelity.

Arnheim discusses pictorial integration, Renaissance representation and artists’ departures from strict construction. The Alberti visual-pyramid account places the eye at the ray apex; a direction-family vanishing point is an image location, not that eye. The pinhole model clarifies projection without establishing that every camera or lens implements an exact pinhole. One-point and two-point are special scene/view cases among the aliases. No current strongest-cue, once-in-history or universal cultural conclusion is inferred.

Retained wording from the represented account (original fidelity unassessed):

"Central perspective is at the same time by far the most realistic way of rendering optical space, and therefore should be expected to be not an esoteric refinement reserved to the happy few, but the method suggested most naturally to everyone by the evidence of visual experience"

# Prerequisites

- **Pictorial Space** — Pictorial spatial readings supply the vocabulary for this particular cue or convention.
- **Size Gradient** — Comparable-size assumptions and projected scale support this spatial comparison.
- **Depth Gradient Principle** — Systematic image-quality changes supply a comparison framework, not a law that every cue is a gradient.

# Key Properties

1. For camera coordinates (X,Y,Z), Z>0 and focal length f>0, x=fX/Z and y=fY/Z.
2. A frontoparallel linear extent L at common Z projects to fL/Z.
3. Direction families with nonzero camera-axis component have finite vanishing points under this model.
4. Only suitable horizontal-world-plane families meet on the level horizon.
5. Several direction-family vanishing points can be mutually consistent.

# Construction / Recognition

## To Construct/Create:

1. Specify camera, image plane and coordinate conventions.
2. Group edges by 3D direction rather than sending all parallels to one point.
3. Use the appropriate horizon for level horizontal directions.
4. Apply depth scaling in camera-axis Z, not arbitrary Euclidean distance.

## To Identify/Recognise:

1. Identify candidate direction families and their projected convergence.
2. Check whether each has a finite vanishing point and whether it is a horizontal family.
3. Inspect size changes and geometry separately from symbolic emphasis.
4. During an audit, check unintended spatial conflicts without requiring strict photographic realism.

# Context & Application

Illustration, architecture, spatial maps, games and CSS transformed scenes can use central perspective. A focal arrangement can contribute attention without deciding the full hierarchy. A local perspective audit cannot replace the complete ordered interface audit. Accurate, calm, flat and stylized imagery remain available according to the task.

## Cross-Domain Connections

**Mathematics → RIGOROUS**, within stated domains: a central projection ℝ³→ℝ² loses depth. A nondegenerate mapping between planes can instead be a homography, preserving incidence and cross-ratio for four distinct collinear points where the map is defined; collapse and poles require care. **Mathematics → RIGOROUS**, for projected triangles and attributes affine on the original triangle: screen barycentric λi and nonzero homogeneous wi give q=(Σλiqi/wi)/(Σλi/wi), with nonzero denominator. This is perspective-correct attribute interpolation, not a claim that all CSS animation interpolates 1/Z. [CSS Transforms 2](https://www.w3.org/TR/css-transforms-2/#perspective-property) distinguishes parent perspective on 3D-transformed children from a self perspective() transform.

# Examples

Source-specific examples and quotations below are retained as reports with their original wording and locators. They are not independently checked historical, experimental or universal claims. Applied examples are qualified design proposals.

**Example 1** (p. 612): "Central perspective is so violent and intricate a deformation of the normal shape of things that it came about only as the final result of prolonged exploration and in response to very particular cultural needs." — Arnheim

**Example 2** (p. 731): Leonardo's description: "Perspective employs in distances two opposite pyramids, one of which has its apex in the eye and its base as far away as the horizon."

**Example 3** (p. 735): Leonardo's Last Supper — vanishing point placed at the figure of Christ at center, making central perspective serve both spatial and hierarchical-symbolic purposes.

**Example 4** (p. 704): Henry Moore's Tube Shelter Perspective — "the objectively static theme of two rows of sleepers in an underground tube acquires through perspective contraction the dramatic impact appropriate to the representation of an air-raid shelter."

**Example 5** (CSS): Parent perspective:800px supplies a shared perspective to 3D-transformed children, as distinct from each child’s own perspective() function. It does not give every untransformed child a new 3D arrangement.

# Relationships

These are scoped reading connections. Builds Upon supports understanding; Enables names a possible downstream use; Related is an association; Contrasts With names a comparison. They do not establish universal causes, subtypes or verified historical sequences. Ordinary downstream uses are not invented card identities.

## Builds Upon

- **Size Gradient** — The pinhole model produces a size gradient along camera-axis Z.
- **Depth Gradient Principle** — It supplies defined geometric changes to compare with gradient readings.
- **Isometric Perspective** — The preserved extends connection elaborates the contrast of parallel and central systems, not a mathematical subtype or independently verified history.

## Enables

- **Pyramidal Space** — Arnheim’s pyramidal reading is compared with the defined projection, without a perceptual metric theorem.
- **Vanishing Point Symbolism** — Focal placement can carry intended or attributed meaning without a universal code.

## Related

- **Size Gradient** — Comparable frontoparallel extents obey fL/Z in the stated model.
- **Texture Gradient** — A projected checkerboard can combine convergence and texture changes.
- **Atmospheric Perspective** — Atmospheric effects can accompany geometry but require distinct medium assumptions.

## Contrasts With

- **Isometric Perspective** — Parallel and central projections preserve different relations and have different scale behavior.
- **Flat Pictorial Space** — Flat/composite conventions can preserve selected information without maximizing or eliminating depth.

# Common Errors

- **Error**: Sending all parallel lines to one horizon point or using 1/d for arbitrary radial distance.
  **Correction**: Specify direction families and axial Z.

- **Error**: Treating strict perspective as the only correct representation.
  **Correction**: Choose it, a parallel view, flat/composite aspects or deliberate departures for the actual information and expression.

# Common Confusions

- **Confusion**: The vanishing point is the eye or where space ends.
  **Clarification**: It is the image of a direction at infinity; the eye is the finite projection centre.

- **Confusion**: Multiple vanishing points prove ambiguity.
  **Clarification**: Different direction families normally have different points. Historical discovery and symbolism remain attributed source interpretations.

# Source Reference

Chapter V: Space, "Art and Visual Perception," pp. 590–765 (Toward a Convergence of Space, The Two Roots of Central Perspective, Not a Faithful Projection, Pyramidal Space, The Symbolism of a Focused World, Centrality and Infinity).

# Verification Notes

The bullets below are preserved historical extraction assertions, not current verification. Frozen confidence, cross-reference, source-reading and OCR claims do not settle original-dependent fidelity. Current same-context review supports only the explicitly scoped technical constructions, contextual teaching and local comparisons; it establishes no browser, observer, comfort or physiological result.

- Definition source: Synthesised from extensive discussion in Chapter V, pp. 590–765; multiple direct quotations
- Confidence rationale: High — linear perspective is one of the most extensively and precisely discussed topics in the chapter
- Uncertainties: None significant
- Cross-reference status: Verified
- Rosetta Stone check: Mappings added — projective geometry is rigorous; perspective-correct interpolation is rigorous
- OCR issues: Some running header OCR duplications; no impact on content
