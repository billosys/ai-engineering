---
concept: "Foreshortening"
slug: "foreshortening"
category: "visual-perception"
subcategory: null
tier: "intermediate"
layer: "0-perception"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "III. Form"
chapter_number: 3
pdf_page: 65
section: "Foreshortening"
extraction_confidence: "high"
aliases:
  - "projective-contraction"
  - "oblique-view"
  - "perspective-distortion"
prerequisites:
  - "picture-plane-projection"
  - "structural-skeleton"
  - "shape-constancy"
extends: []
related:
  - "canonical-view"
  - "overlapping-as-depth-cue"
  - "spatial-orientation-of-form"
contrasts_with:
  - "canonical-view"
answers_questions: []
rosetta_stone: []
css_implementation:
  -
    property: "perspective"
    example: ".scene { perspective: 400px; } .scene > .face { transform: rotateX(45deg); } /* Parent perspective affects its transformed child. */"
    support: "baseline"
---

# Quick Definition

In the represented perceptual usage, foreshortening is the projective contraction associated with depth orientation, such as that of a planar face tilted relative to the picture plane — perceived specifically as a *deviation from a structurally simpler pattern* (the "facade" of the object), not as a new shape in its own right.

# Core Definition

This section presents the represented Arnheim account. Its quotations, page references and historical, clinical, cultural or experimental reports have not been checked against the unavailable original. The current analytic qualifications do not certify that fidelity.

Arnheim gives a precise perceptual definition: "It seems best, then, to call a pattern foreshortened when it is perceived as a deviation from a structurally simpler pattern, from which it is derived by a change of orientation in the depth dimension." (p. 208)

This particular perceptual usage distinguishes:
- Geometric contraction as a separate description: a tilted face can contract even under orthographic projection. A front-facing plane need not contract.
- Atypical orthogonal views (sense 2): a top-down view of a sombrero-clad Mexican is not foreshortened in the perceptual sense — we don't see it as a deviation from a "more normal" view; we just see a disk.

Within this account, a perceptual foreshortening reading involves:
1. The shape is perceived as an *oblique* view of something.
2. The "normal" or "facade" of that thing is simultaneously implied.
3. The projection reads as a *deviation* from that implied facade — not as a flat shape in its own right.

Arnheim describes a possible tension between simple flat readings and perceived depth: "The simpler the shape of a two-dimensional pattern, the more it resists being perceived three-dimensionally — it tends to look flat. It is difficult to see a circle as a foreshortened ellipse or a square as a foreshortened rectangle."

In the represented account, symmetrical foreshortened views (head-on from above or below) can "freeze" into a flat reading; this is not a universal geometric or perceptual rule.

Delacroix: "There is always foreshortening, even in an upright figure with its arms hanging downward... The arts of foreshortening and of perspective are one and the same thing."

# Prerequisites

- **Picture plane projection** — Foreshortening is a specific type of projection effect.
- **Structural skeleton** — Foreshortening is perceived relative to the "facade" (the canonical skeleton).
- **Shape constancy** — Constancy can support an object-in-depth reading; this is not a unique necessary mechanism.

# Key Properties

1. **Depth rotation**: Geometric contraction depends on orientation to the image plane, including under parallel orthographic rays. Image-plane roll is different.
2. **Implied facade**: Arnheim's narrower perceptual meaning depends on reading a projected shape relative to an implied face.
3. **Context and simplicity**: A simple outline may favor a flat reading, without preventing a depth interpretation in context.
4. **Symmetry**: Symmetric projections can be ambiguous; symmetry is not a universal failure condition.
5. **Continuity**: Bent and overlapping forms can require careful handling of contour breaks.

# Construction / Recognition

## To Construct/Create:

1. Choose a projection and the object face or axis whose depth rotation matters.
2. Compare silhouette, shading and context for the intended reading.
3. Use asymmetric or symmetric views as the task warrants.
4. Check overlaps and contour continuity rather than assume one angle always conveys depth.

## To Identify/Recognise:

1. Distinguish geometric contraction from Arnheim's reported perceptual reading.
2. Identify the implied facade and the actual projection conditions.
3. If a shape reads flat, inspect context rather than infer a necessary lack of complexity.

# Context & Application

- **Typical contexts**: Figure drawing, architectural drawing, product visualisation, 3D CSS transforms, animation.
- **Common applications**: Drawing hands reaching toward the viewer (extreme foreshortening); perspective text in CSS (`perspective` + `rotateX`); 3D product renders at non-canonical angles; cinematic Dutch tilt as an image-plane roll, distinct from the depth rotation that geometrically foreshortens a face.

# Examples

The following are reported source examples and interpretations, with their original wording and locators retained for inspection. They are not independently checked historical, experimental or universal claims.

**Example 1** (p. 208): A profile view of a face does not count as foreshortening — it has its own independent structural skeleton. But an oblique three-quarter view does count, because the observer reads it as a deviation from the frontal symmetry that is simultaneously implied.

**Example 2** (p. 210): "It is difficult to see a circle as a foreshortened ellipse" — a circle is too simple to resist as an autonomous flat shape. A table top in a strongly depth-indicating pictorial environment illustrates how context can support that reading; the unusual quoted wording remains unassessed in its original context.

**Example 3** (p. 208): "A foreshortening of a face, brought about by a turn to an oblique position, is not perceived as a pattern in its own right but as a mere variation of the frontal symmetry" — the frontal symmetry is the implied reference.

# Relationships

These are scoped conceptual reading connections. Prerequisites support understanding rather than assert a universal developmental sequence; related links and contrasts specify comparisons, not causal or subtype laws. Unresolved ordinary comparisons below are not invented card identities.

## Builds Upon
- **Picture plane projection** — Projection defines the mapping in which contraction is described.
- **Structural skeleton** — The implied facade is described by its characteristic axes and correspondences.
- **Shape constancy** — Shape constancy helps explain a stable object reading across views, without uniquely determining it.

## Enables
- **Depth representation** — It is one depth cue; other cues can suffice without it.
- **Visual representation of complex pose and motion** — It can help depict pose; static motion representation does not universally depend on it.

## Related
- **Overlapping** — Occlusion and geometric contraction can co-occur but are separate operations.
- **Canonical view** — An informative canonical aspect can itself be foreshortened; the comparison is not an exclusive opposition.

## Contrasts With
- **Orthogonal projection** — Orthographic projection uses parallel rays normal to the image plane and can contract a tilted face; it is not synonymous with front-facing.
- **Egyptian method** — The Egyptian composite method can favor informative aspects over one consistent camera.

# Common Errors

- **Error**: Treating a sphere and a tilted flat disk as having the same orientation-dependent silhouette.
  **Correction**: Rotating a sphere leaves its silhouette invariant under the same viewing conditions. Under orthographic projection, a flat disk tilted 60° from front-facing has one projected dimension multiplied by cos(60°)=1/2. Shading and context can support depth readings; a circle is not automatically an incorrect sphere outline.

- **Error**: Using head-on symmetrical views for extreme perspective effects (top-down or bottom-up views).
  **Correction**: The represented account warns of a possible flat reading. Compare actual context; symmetric views can still convey depth and may be required for documentation.

# Common Confusions

- **Confusion**: All distortion in a projection is foreshortening.
  **Clarification**: Foreshortening specifically refers to projective contraction that implies a 3D deviation from a reference view. That narrower perceptual reading need not occur whenever geometry contracts. The unusual quoted circle-as-foreshortened-ellipse wording above is preserved; its original context remains unavailable.

# Source Reference

Chapter III: Form, "Art and Visual Perception," pp. 206–215 (Foreshortening section).

# Verification Notes

The bullets below preserve historical extraction assertions, including confidence, cross-reference, OCR and source-reading claims; they are not current verification. Original-dependent fidelity remains unassessed. Current technical corrections and analogies establish neither a neural mechanism nor cultural universality or measured usability.

- Definition source: Direct quote from p. 208; synthesised from surrounding discussion.
- Confidence rationale: High — Arnheim provides an explicit, three-part typology of "foreshortening" senses and identifies the perceptually precise definition.
- Uncertainties: The Delacroix quote is cited without source by Arnheim; context makes the meaning clear.
- Cross-reference status: Verified — consistent with projection discussion earlier in chapter.
- Rosetta Stone check: No strong formal mappings; CSS perspective noted as implementation.
- OCR issues: "Dingfront" is Arnheim's translation of Wertheimer's term; correct.
