---
concept: "Picture Plane Projection"
slug: "picture-plane-projection"
category: "visual-perception"
subcategory: null
tier: "foundational"
layer: "0-perception"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "III. Form"
chapter_number: 3
pdf_page: 65
section: "Projections"
extraction_confidence: "high"
aliases:
  - "projective-image"
  - "2D-projection-of-3D"
prerequisites:
  - "representation-in-art"
extends: []
related:
  - "canonical-view"
  - "shape-constancy"
  - "foreshortening"
  - "structural-skeleton"
contrasts_with: []
answers_questions: []
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Linear projection / projection operators in linear algebra"
    rating: "structural"
    note: "Orthographic P(x,y,z)=(x,y) is linear. Cartesian perspective P=(x/z,y/z), z>0, is nonlinear: P(2v)=P(v), not 2P(v). A homogeneous matrix followed by division does not make the final Cartesian map linear. Egyptian composites need not implement one camera; visibility is a separate condition."
css_implementation:
  -
    property: "perspective"
    example: "perspective: 800px;"
    support: "baseline"
  -
    property: "transform"
    example: "transform: rotateY(45deg);"
    support: "baseline"
---

# Quick Definition

Picture plane projection maps spatial geometry to a plane under specified projection conditions. Choosing aspects, depicting contours and deciding which surfaces are visible are related but distinct operations; authored composites need not use one camera.

# Core Definition

This section presents the represented Arnheim account. Its quotations, page references and historical, clinical, cultural or experimental reports have not been checked against the unavailable original. The current analytic qualifications do not certify that fidelity.

For a geometric image, specify the mapping from object coordinates to the image plane. Opaque rendering then needs a visibility rule to hide blocked surfaces; wireframes and transparent renderings can show more. Retinal optics, camera projection and authored pictorial representation are distinct levels. Not every flat image is one geometric projection.

Arnheim analyses several types of projection:
- **Orthogonal projection**: Rays are parallel and normal to the image plane. An object face may be tilted, so it can still be foreshortened; a front-facing plane preserves its shape under this mapping.
- **Central (perspective) projection**: Uses rays through a finite center; depth-dependent division can produce scale changes and vanishing points. Not every family of parallels converges to a finite vanishing point.
- **The "Egyptian method"**: Selects for each part of the object the aspect that most clearly shows its structural skeleton, combining multiple viewpoints as an authored convention rather than one camera projection.

The fundamental problem: "Strictly speaking, the visual concept of anything that has volume can be represented only in a three-dimensional medium... If we wish to make pictures on a plane surface, all we can hope to do is to produce a translation — that is, to present some structural essentials of the visual concept by two-dimensional means." (p. 75)

# Prerequisites

- **Representation in art** — Projection is one method (but not the only valid method) of representation.

# Key Properties

1. **Aspect selection**: A single-view projection selects one aspect; composites and multiview diagrams can show several.
2. **Silhouette**: A projected surface can produce an apparent contour where no material edge exists.
3. **Visibility is separate**: Opaque occlusion, transparency and wireframe conventions decide what is shown beyond the coordinate map.
4. **Perceptual reading**: Shape constancy can support an object reading without exactly inverting a projection.
5. **Task suitability**: Orthographic, perspective and composite treatments support different tasks; no one method is universally correct.

# Construction / Recognition

## To Construct/Create:

1. Choose image plane, object geometry and a projection model.
2. For central perspective use rays through a finite center; for orthographic projection use parallel rays normal to the plane.
3. Map geometry to the plane, then specify opaque visibility, wireframe or transparency.
4. Choose one view or an authored multiview convention according to the task.

## To Identify/Recognise:

1. Ask whether the image uses a single geometric projection or an authored composite.
2. Distinguish mapping from which surfaces the visibility convention retains.
3. Separate apparent contours from material edges.

# Context & Application

- **Typical contexts**: Technical drawing, photography, painting, digital 3D rendering, UI design (3D transforms), data visualisation (spatial data on flat screens).
- **Common applications**: Choosing camera angles; designing 3D CSS transforms; understanding why isometric vs. perspective diagrams communicate differently; scientific illustration selection of optimal view.

## Cross-Domain Connections

**Mathematics → STRUCTURAL**: Orthographic P(x,y,z)=(x,y) is a linear map ℝ³→ℝ². Perspective P(x,y,z)=(x/z,y/z), z>0, is nonlinear: for v=(2,4,2), P(v)=(1,2)=P(2v), whereas 2P(v)=(2,4). A matrix in homogeneous coordinates followed by division does not make the final Cartesian map linear. The formal mapping is specified here; it does not encompass every pictorial method. CSS parent `perspective` supplies perspective to transformed children; a self `perspective()` function is a different declaration arrangement.

# Examples

The following are reported source examples and interpretations, with their original wording and locators retained for inspection. They are not independently checked historical, experimental or universal claims.

**Example 1** (p. 70, Fig. 80): A cardboard rectangle cast in shadow by a candle yields innumerable projections. The front-facing aspect (rectangle perpendicular to light) is reported as looking most like the object. A finite candle emits diverging rays, so this shadow setup alone is not an orthographic ray construction. Others look like tilted shapes in 3D space or — in one case — like a flat trapezoid with a compelling independent symmetry that resists 3D interpretation.

**Example 2** (p. 73, Fig. 81): A cube viewed at different angles: from straight-on, one face (a square) dominates; at other angles, multiple faces are visible with foreshortening.

**Example 3** (p. 73): The "hidden surface problem" in computer graphics — determining which surfaces of a solid are visible from a given viewpoint — is a separate visibility task associated with opaque rendering, not the coordinate projection map alone.

# Relationships

These are scoped conceptual reading connections. Prerequisites support understanding rather than assert a universal developmental sequence; related links and contrasts specify comparisons, not causal or subtype laws. Unresolved ordinary comparisons below are not invented card identities.

## Builds Upon
- **Representation in art** — Projection is a technique used within representation; it is not the only valid pictorial convention.

## Enables
- **Canonical view** — Aspect selection asks what the task needs visible.
- **Foreshortening** — A tilted face can contract under orthographic as well as perspective projection.
- **Shape constancy** — Projection supplies changing images in relation to which constancy is discussed, rather than a prerequisite brain mechanism.

## Related
- **Structural skeleton** — Some aspects reveal characteristic axes better for a given task.
- **Overlapping** — Opaque visibility can cause occlusion; the mapping alone does not require it.

## Contrasts With
- **All-around visual concept** — An all-around visual concept is an ordinary conceptual comparison with a selected view, not a resolved card identity.
- **Egyptian method** — The Egyptian method can combine aspects instead of selecting one camera.

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

The bullets below preserve historical extraction assertions, including confidence, cross-reference, OCR and source-reading claims; they are not current verification. Original-dependent fidelity remains unassessed. Current technical corrections and analogies establish neither a neural mechanism nor cultural universality or measured usability.

- Definition source: Synthesised from pp. 70–80; key quote from p. 75.
- Confidence rationale: High — the mechanics of projection are described in detail with numerous examples and figures.
- Uncertainties: Arnheim describes projection phenomenologically and perceptually, not with mathematical formulae; the mathematical mapping is my gloss.
- Cross-reference status: Verified — consistent with figures 80, 81, 82 and surrounding text.
- Rosetta Stone check: Linear algebra projection mapping added as rigorous.
- OCR issues: Some figure references in text are corrupted (e.g., "Figure 80a" appears as "Figure 8oc"); content meaning clear from context.
