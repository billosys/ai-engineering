---
# === CORE IDENTIFICATION ===
concept: Foreshortening
slug: foreshortening

# === CLASSIFICATION ===
category: visual-perception
subcategory: null
tier: intermediate
layer: 0-perception

# === PROVENANCE ===
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: art-and-visual-perception
authors: "Rudolf Arnheim"
chapter: "III. Form"
chapter_number: 3
pdf_page: 65
section: "Foreshortening"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - projective-contraction
  - oblique-view
  - perspective-distortion

# === TYPED RELATIONSHIPS ===
prerequisites:
  - picture-plane-projection
  - structural-skeleton
  - shape-constancy
extends: []
related:
  - canonical-view
  - overlapping
  - spatial-orientation-of-form
contrasts_with:
  - orthogonal-projection
  - canonical-view

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the gestalt principles of perceptual grouping, and how does each one work?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "perspective"
    example: "perspective: 400px; transform: rotateX(45deg);"
    support: baseline
---

# Quick Definition

Foreshortening is the projective contraction of a visual form when it is not parallel to the picture plane — perceived specifically as a *deviation from a structurally simpler pattern* (the "facade" of the object), not as a new shape in its own right.

# Core Definition

Arnheim gives a precise perceptual definition: "It seems best, then, to call a pattern foreshortened when it is perceived as a deviation from a structurally simpler pattern, from which it is derived by a change of orientation in the depth dimension." (p. 208)

This rules out:
- Mere geometric contraction (sense 1): a head-on front view is geometrically "complete" but is not perceptually foreshortened.
- Atypical orthogonal views (sense 2): a top-down view of a sombrero-clad Mexican is not foreshortened in the perceptual sense — we don't see it as a deviation from a "more normal" view; we just see a disk.

True perceptual foreshortening requires:
1. The shape is perceived as an *oblique* view of something.
2. The "normal" or "facade" of that thing is simultaneously implied.
3. The projection reads as a *deviation* from that implied facade — not as a flat shape in its own right.

Key tension: for foreshortening to work, the projection must not be too simple. "The simpler the shape of a two-dimensional pattern, the more it resists being perceived three-dimensionally — it tends to look flat. It is difficult to see a circle as a foreshortened ellipse or a square as a foreshortened rectangle."

Symmetrical foreshortened views (head-on from above or below) are particularly risky because the symmetry makes the projection "freeze" into a self-contained flat pattern.

Delacroix: "There is always foreshortening, even in an upright figure with its arms hanging downward... The arts of foreshortening and of perspective are one and the same thing."

# Prerequisites

- **Picture plane projection** — Foreshortening is a specific type of projection effect.
- **Structural skeleton** — Foreshortening is perceived relative to the "facade" (the canonical skeleton).
- **Shape constancy** — Foreshortening is perceived as such only when constancy reads the distorted projection as implying a 3D structure.

# Key Properties

1. **Obliqueness required**: Foreshortening requires a depth-dimension turn; purely lateral reorientation is not foreshortening.
2. **Facade simultaneously implied**: The "normal" view must be visible as a reference for the deviated projection to read as foreshortened rather than as a new shape.
3. **Simplicity paradox**: Simple projections (circles, squares) resist foreshortening reads; complex projections more readily imply a "reference shape" from which they deviate.
4. **Symmetry freezes**: Symmetrical foreshortened views risk becoming self-contained patterns rather than implying depth.
5. **Continuity disruption**: In bent or overlapping forms, foreshortening disrupts the continuity of outlines — one of the main challenges for draftsmen.

# Construction / Recognition

## To Construct/Create:
1. Ensure the projection's structural pattern implies a simpler reference from which it deviates.
2. Avoid having the foreshortened shape be too simple or symmetrical (it will resist depth interpretation).
3. Use asymmetry and obliqueness to imply depth: the observer should be able to infer the "facade" the projection deviates from.
4. Handle overlaps and discontinuities carefully — where the outline breaks, the unity of the underlying form must still be perceptible.

## To Identify/Recognise:
1. Ask: does this projection imply a simpler reference shape from which it deviates?
2. If yes: is the implied reference shape recognisable and visually present (even if not directly shown)?
3. If a shape reads as flat rather than foreshortened, the projection may be too simple.

# Context & Application

- **Typical contexts**: Figure drawing, architectural drawing, product visualisation, 3D CSS transforms, animation.
- **Common applications**: Drawing hands reaching toward the viewer (extreme foreshortening); perspective text in CSS (`perspective` + `rotateX`); 3D product renders at non-canonical angles; cinematic Dutch tilt (extreme oblique orientation).

# Examples

**Example 1** (p. 208): A profile view of a face does not count as foreshortening — it has its own independent structural skeleton. But an oblique three-quarter view does count, because the observer reads it as a deviation from the frontal symmetry that is simultaneously implied.

**Example 2** (p. 210): "It is difficult to see a circle as a foreshortened ellipse" — a circle is too simple to resist as an autonomous flat shape. Only when the context forces a depth interpretation (e.g., a table top in a strongly depth-indicating pictorial environment) does the circle read as foreshortened.

**Example 3** (p. 208): "A foreshortening of a face, brought about by a turn to an oblique position, is not perceived as a pattern in its own right but as a mere variation of the frontal symmetry" — the frontal symmetry is the implied reference.

# Relationships

## Builds Upon
- **Picture plane projection** — Foreshortening is a class of projective distortion.
- **Structural skeleton** — The "facade" that is deviated from is the canonical structural skeleton.
- **Shape constancy** — Without constancy, foreshortening would not read as 3D deviation; it would just be a distorted flat shape.

## Enables
- **Depth representation** — Foreshortening is the primary pictorial cue for depth in single-viewpoint representation.
- **Visual representation of complex pose and motion** — Action, gesture, and spatial complexity in static images depend on foreshortening.

## Related
- **Overlapping** — Both foreshortening and overlapping deal with how 3D volumes project onto 2D surfaces; they often occur together.
- **Canonical view** — Foreshortening is defined relative to the canonical view (the facade) from which it deviates.

## Contrasts With
- **Orthogonal projection** — The "face-on" view that shows the structural skeleton directly, without foreshortening.
- **Egyptian method** — Uses canonical views for each part, avoiding foreshortening in favour of structural clarity.

# Common Errors

- **Error**: Drawing a circle to represent a foreshortened sphere or disk.
  **Correction**: A circle is too simple — it reads as a flat circle, not a foreshortened disc. Add shading, ellipse shape, or context to force the foreshortening read.

- **Error**: Using head-on symmetrical views for extreme perspective effects (top-down or bottom-up views).
  **Correction**: These symmetrical extremes freeze into flat, self-contained patterns. Asymmetric oblique angles produce more convincing foreshortening.

# Common Confusions

- **Confusion**: All distortion in a projection is foreshortening.
  **Clarification**: Foreshortening specifically refers to projective contraction that implies a 3D deviation from a reference view. A distorted shape that has its own independent visual structure is not foreshortening — it is a new shape.

# Source Reference

Chapter III: Form, "Art and Visual Perception," pp. 206–215 (Foreshortening section).

# Verification Notes

- Definition source: Direct quote from p. 208; synthesised from surrounding discussion.
- Confidence rationale: High — Arnheim provides an explicit, three-part typology of "foreshortening" senses and identifies the perceptually precise definition.
- Uncertainties: The Delacroix quote is cited without source by Arnheim; context makes the meaning clear.
- Cross-reference status: Verified — consistent with projection discussion earlier in chapter.
- Rosetta Stone check: No strong formal mappings; CSS perspective noted as implementation.
- OCR issues: "Dingfront" is Arnheim's translation of Wertheimer's term; correct.
