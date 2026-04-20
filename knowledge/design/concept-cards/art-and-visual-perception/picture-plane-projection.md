---
# === CORE IDENTIFICATION ===
concept: Picture Plane Projection
slug: picture-plane-projection

# === CLASSIFICATION ===
category: visual-perception
subcategory: null
tier: foundational
layer: 0-perception

# === PROVENANCE ===
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: art-and-visual-perception
authors: "Rudolf Arnheim"
chapter: "III. Form"
chapter_number: 3
pdf_page: 65
section: "Projections"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - projective-image
  - 2D-projection-of-3D
  - retinal-projection
  - orthogonal-projection

# === TYPED RELATIONSHIPS ===
prerequisites:
  - representation-in-art
extends: []
related:
  - canonical-view
  - shape-constancy
  - foreshortening
  - structural-skeleton
contrasts_with:
  - all-around-visual-concept
  - three-dimensional-form

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the gestalt principles of perceptual grouping, and how does each one work?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: mathematics
    concept: "Linear projection / projection operators in linear algebra"
    rating: rigorous
    note: "The picture plane projection is literally a linear projection operator: it maps 3D coordinates to 2D by dropping (or compressing) depth information, and different projection matrices (orthogonal, perspective) correspond to Arnheim's different representational methods."

css_implementation:
  - property: "perspective"
    example: "perspective: 800px;"
    support: baseline
  - property: "transform"
    example: "transform: rotateY(45deg);"
    support: baseline
---

# Quick Definition

Picture plane projection is the reduction of a three-dimensional object to a two-dimensional surface image — a process that always involves selecting one aspect of the object, introducing boundaries where none exist in the object, and concealing all surfaces not visible from the chosen viewpoint.

# Core Definition

Any image on a flat surface is a projection: light travels from the object to the eye (or camera) in straight lines, and only those surfaces whose line-of-sight to the eye is unobstructed appear in the image. The projection depends critically on the angle of observation.

Arnheim analyses several types of projection:
- **Orthogonal projection**: The object plane is perpendicular to the line of sight. The projection most faithfully represents the shape of one face.
- **Central (perspective) projection**: Simulates the geometry of a single eye at a fixed point; produces foreshortening and convergence of parallels.
- **The "Egyptian method"**: Selects for each part of the object the aspect that most clearly shows its structural skeleton, combining multiple viewpoints.

The fundamental problem: "Strictly speaking, the visual concept of anything that has volume can be represented only in a three-dimensional medium... If we wish to make pictures on a plane surface, all we can hope to do is to produce a translation — that is, to present some structural essentials of the visual concept by two-dimensional means." (p. 75)

# Prerequisites

- **Representation in art** — Projection is one method (but not the only valid method) of representation.

# Key Properties

1. **Aspect selection is unavoidable**: Every 2D image can show only one view of a 3D object at a time.
2. **Contour creation**: The projection introduces contour lines where the 3D object has continuous surface curvature.
3. **Hidden surfaces**: All parts of the object whose line-of-sight is blocked by the object itself are absent from the projection.
4. **Constancy correction**: The visual system applies shape and size constancy to partially undo the distortions of projection, reading a trapezoid as a foreshortened square.
5. **Style-relative legitimacy**: No projection method is the single "correct" one — each is a translation with its own virtues and limitations.

# Construction / Recognition

## To Construct/Create:
1. Choose a viewpoint (observation station point).
2. Project straight lines from the viewpoint through each visible point on the object to the picture plane.
3. The intersection points on the picture plane form the projected image.
4. For orthogonal projection, the viewpoint is at infinity in the direction perpendicular to the picture plane.

## To Identify/Recognise:
1. A flat image is always a projection — ask: from what viewpoint? using what projection method?
2. Identify which surfaces of the object are hidden and which are visible.
3. Notice where the projection has introduced contour boundaries (edges) where the 3D object has no actual edge.

# Context & Application

- **Typical contexts**: Technical drawing, photography, painting, digital 3D rendering, UI design (3D transforms), data visualisation (spatial data on flat screens).
- **Common applications**: Choosing camera angles; designing 3D CSS transforms; understanding why isometric vs. perspective diagrams communicate differently; scientific illustration selection of optimal view.

## Cross-Domain Connections

**Mathematics → RIGOROUS**: A projection in the linear algebra sense is exactly what is happening: a linear map from ℝ³ → ℝ² that collapses depth information. Central perspective is a projective (non-linear) transformation; orthogonal projection is a linear one. CSS `perspective` and `transform: rotateY()` implement these mappings in the browser.

# Examples

**Example 1** (p. 70, Fig. 80): A cardboard rectangle cast in shadow by a candle yields innumerable projections. The orthogonal one (rectangle perpendicular to light) looks most like the object. Others look like tilted shapes in 3D space or — in one case — like a flat trapezoid with a compelling independent symmetry that resists 3D interpretation.

**Example 2** (p. 73, Fig. 81): A cube viewed at different angles: from straight-on, one face (a square) dominates; at other angles, multiple faces are visible with foreshortening.

**Example 3** (p. 73): The "hidden surface problem" in computer graphics — determining which surfaces of a solid are visible from a given viewpoint — exactly captures the projection problem Arnheim describes.

# Relationships

## Builds Upon
- **Representation in art** — Projection is one technique of representation; it is not the only valid one.

## Enables
- **Canonical view** — The question of which projection best represents a given object.
- **Foreshortening** — The specific distortion introduced when the line of sight is not perpendicular to the object surface.
- **Shape constancy** — The perceptual mechanism that partially corrects for projection distortions.

## Related
- **Structural skeleton** — The skeleton may be revealed more clearly in some projections than others.
- **Overlapping** — An inevitable consequence of projection: nearer objects block farther ones.

## Contrasts With
- **All-around visual concept** — The mental 3D concept is not bound to any projection; projection always reduces and selects from it.
- **Egyptian method** — Deliberately combines aspects from multiple projection angles rather than committing to one.

# Common Errors

- **Error**: Treating perspective projection as the single "correct" form of visual representation.
  **Correction**: Arnheim shows that multiple projection methods are equally valid translations of the visual concept. Each has its own virtues — perspective captures relative depth; the Egyptian method preserves structural clarity of each part.

- **Error**: Assuming the projection that looks "most realistic" communicates structural essentials most faithfully.
  **Correction**: The most realistic-looking projection (central perspective) often introduces distortions (foreshortening, size variation) that obscure structural properties that simpler projections would preserve.

# Common Confusions

- **Confusion**: "Projection" in the perceptual sense = the retinal image; "projection" in the pictorial sense = the method used in drawing/photography.
  **Clarification**: Arnheim uses "projection" in the pictorial sense primarily — the method by which a 3D object is represented on a flat surface. The retinal projection is the proximal stimulus that the visual system processes, but it is not the same as the pictorial representation.

# Source Reference

Chapter III: Form, "Art and Visual Perception," pp. 70–80 (Projections section).

# Verification Notes

- Definition source: Synthesised from pp. 70–80; key quote from p. 75.
- Confidence rationale: High — the mechanics of projection are described in detail with numerous examples and figures.
- Uncertainties: Arnheim describes projection phenomenologically and perceptually, not with mathematical formulae; the mathematical mapping is my gloss.
- Cross-reference status: Verified — consistent with figures 80, 81, 82 and surrounding text.
- Rosetta Stone check: Linear algebra projection mapping added as rigorous.
- OCR issues: Some figure references in text are corrupted (e.g., "Figure 80a" appears as "Figure 8oc"); content meaning clear from context.
