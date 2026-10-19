---
concept: "Overlapping as Depth Cue"
slug: "overlapping-as-depth-cue"
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
section: "Overlapping"
extraction_confidence: "high"
aliases:
  - "superposition"
  - "occlusion"
  - "overlap-hierarchy"
prerequisites:
  - "picture-plane-projection"
  - "structural-skeleton"
extends: []
related:
  - "foreshortening"
  - "canonical-view"
  - "perceptual-grouping-similarity"
contrasts_with: []
answers_questions:
  - "What are the gestalt principles of perceptual grouping, and how does each one work?"
  - "How does the relationship between inter-group and intra-group spacing communicate which elements belong together (gestalt proximity)?"
rosetta_stone:
  -
    domain: "engineering"
    concept: "CSS z-index / stacking contexts"
    rating: "structural"
    note: "CSS stacking contexts order atomic paint groups. A descendant with a large z-index cannot escape its ancestor's context to outrank another context. Paint order may contribute to occlusion but is not semantic priority or a calibrated perceived distance."
  -
    domain: "music"
    concept: "Harmonic counterpoint (two voices sharing a compositional space)"
    rating: "structural"
    note: "The quoted chord comparison is attributed to Arnheim. Simultaneous and successive presentation organize relations differently, without a universal law that chords or overlapping visuals are more intense."
css_implementation:
  -
    property: "z-index"
    example: "z-index: 10; position: relative;"
    support: "baseline"
  -
    property: "mix-blend-mode"
    example: "mix-blend-mode: multiply;"
    support: "baseline"
---

# Quick Definition

Occluding overlap occurs when one form hides part of another and can cue foreground/background order. Authored overlap need not originate in a physical 3D scene, and depth order does not by itself determine semantic importance.

# Core Definition

This section presents the represented Arnheim account. Its quotations, page references and historical, clinical, cultural or experimental reports have not been checked against the unavailable original. The current analytic qualifications do not certify that fidelity.

Arnheim analyses overlapping as a perceptual and compositional device using the following reported conditions for the opaque occlusion reading:

"A requirement for the adequate perception of overlap — or superposition — is that the units which, because of projection, touch each other in the same plane must be seen as: (a) separate from each other and (b) belonging to different planes." (p. 238)

Two additional principles govern when overlapping is perceived:
1. **Incompleteness cue**: The rear element must look *incomplete* — its outline truncated or hidden — for the observer to perceive that the front element is in front of it. If both look complete, an occlusion interpretation may be weaker or ambiguous; transparent overlap can preserve both outlines.
2. **Simplicity principle applies**: When two overlapping units together form a particularly simple overall shape, they may be seen as one object rather than two.

Overlapping serves multiple functions in composition:
- **Depth indication**: In the opaque reading, the concealing unit is in front; this need not signal priority.
- **Formal intensification**: "Overlapping intensifies the formal relation by concentrating it within a more tightly integrated pattern. The connection is not only closer but also more dynamic."
- **Hierarchical establishment**: "Overlapping establishes a hierarchy by creating a distinction between dominating and subservient units."
- **Spatial symmetry**: Overlapping can show spatial arrangements (groups of three symmetrical to a figure in the scene) that would be impossible to show clearly in a flat arrangement.

# Prerequisites

- **Picture plane projection** — Supplies a context for discussing depth on a plane; authored overlap need not depict a physical 3D scene.
- **Structural skeleton** — Axes and contours can help an observer infer a partly hidden form, without uniquely determining it.

# Key Properties

1. **Occlusion cue**: A truncated contour can support a rear-object interpretation.
2. **Asymmetry**: In opaque overlap one form can hide another; transparent treatments differ.
3. **Depth versus priority**: Foreground/background order is distinct from importance.
4. **Compositional relation**: Overlap can change the relation of forms without always intensifying it.
5. **Completion**: Hidden portions may admit more than one interpretation.

# Construction / Recognition

## To Construct/Create:

1. If opaque occlusion is intended, use a contour interruption that suggests which form is in front.
2. Check whether hidden portions remain understandable enough for the task; several completions may be possible.
3. Inspect whether a combined outline reads as one form or several; either can be intended.
4. Compare overlap with separation, transparency or blending for the actual content.

## To Identify/Recognise:
1. Find elements that touch or intersect — check whether one appears incomplete.
2. If the rear element appears incomplete and the front element unimpaired: overlapping is functioning.
3. If both outlines remain complete, compare side-by-side and transparent-overlap readings in context.
4. CSS paint order can create occlusion. Nested stacking contexts are atomic groups; local z-index values are not global depth values.

# Context & Application

- **Typical contexts**: All 2D composition; CSS layering (z-index, position); card UI patterns; photo collages; data visualisation (overlapping bars or lines).
- **Common applications**: Modal dialogs over backgrounds (scoped paint order contributes to layering; semantic priority and widget behavior need their own design); overlapping card components; data charts where series overlap; drop shadows creating the perception of layering without actual occlusion.

## Cross-Domain Connections

**Engineering → STRUCTURAL**: A stacking context is an atomic paint group within its parent. A child with z-index:999 remains below a sibling context at z-index:2 if its own context is below that sibling. Paint order can yield occlusion but supplies neither a semantic importance scale nor perceived distance.

**Music → STRUCTURAL**: Arnheim compares simultaneous overlap with simultaneous tones in a chord, versus successive tones. This is an attributed compositional analogy, not a universal chord-intensity or visual-intimacy law.

# Examples

The following are reported source examples and interpretations, with their original wording and locators retained for inspection. They are not independently checked historical, experimental or universal claims.

**Example 1** (pp. 238–240): Arnheim's Picasso figures (Fig. 92): in version (a), the breast renders the arm clearly incomplete — overlap is perceived. In version (b), both elements are complete — they read as ambiguously side-by-side.

**Example 2** (p. 282): "In music the effect of harmony or disharmony is similarly more compelling when several tones are combined in one chord rather than played in succession. Overlapping intensifies the formal relation by concentrating it within a more tightly integrated pattern."

**Example 3** (p. 284): Egyptian relief of King Sethos with Isis: "King Sethos is in front and complete, whereas Isis, who gives his majesty the support of her godship, endures all the inconveniences that befall a seat. Thus, overlapping establishes a hierarchy by creating a distinction between dominating and subservient units."

# Relationships

These are scoped conceptual reading connections. Prerequisites support understanding rather than assert a universal developmental sequence; related links and contrasts specify comparisons, not causal or subtype laws. Unresolved ordinary comparisons below are not invented card identities.

## Builds Upon
- **Picture plane projection** — Projection is one context for planar depth cues; occlusion needs separate visibility conditions.

## Enables
- **Depth in pictorial composition** — It is a useful pictorial depth cue without being necessary in every image.
- **Visual hierarchy in layout** — Layering can serve UI hierarchy when purpose supports it; paint order alone does not define priority.

## Related
- **Foreshortening** — Contraction and occlusion can co-occur while remaining separate cues.
- **Gestalt proximity** — The actual perceptual-grouping-similarity premise treats proximity as a location-based grouping cue. Compare spacing and overlap with shape, similarity and context; overlap does not always outweigh proximity.

## Contrasts With
- **Side-by-side arrangement** — Side-by-side forms can retain strong relations through alignment, spacing or similarity; the comparison is not a universal intensity ranking.

# Common Errors

- **Error**: Making overlapping elements both complete (e.g., a semi-transparent front element that doesn't occlude the rear element's outline).
  **Correction**: For the opaque-occlusion reading discussed here, truncation is useful. Transparent overlap is legitimate: alpha compositing combines partially transparent surfaces, while blend modes specify color combination and can also apply to opaque painted content. They are distinct operations.

- **Error**: Assuming z-index order equals importance in UI design.
  **Correction**: Z-index participates in scoped paint order, not importance or measured distance. The dominating element (front) may be a modal dialog (temporarily important) or a persistent header (structurally important); the meaning depends on context.

# Common Confusions

- **Confusion**: Overlapping and transparency are the same thing.
  **Clarification**: Alpha transparency permits underlying color to contribute to a composite; occlusion hides an underlying region, and blend modes specify a separate color-combination operation. The reported analysis emphasizes truncation for opaque occlusion. Alpha transparency and blend modes are separate operations; a transparent overlapping design can still communicate layers.

# Source Reference

Chapter III: Form, "Art and Visual Perception," pp. 226–306 (Overlapping section and What Good Does Overlapping Do?).

# Verification Notes

The bullets below preserve historical extraction assertions, including confidence, cross-reference, OCR and source-reading claims; they are not current verification. Original-dependent fidelity remains unassessed. Current technical corrections and analogies establish neither a neural mechanism nor cultural universality or measured usability.

- Definition source: Direct quote from p. 238; synthesised from pp. 226–306.
- Confidence rationale: High — extended discussion with explicit principles and numerous examples.
- Uncertainties: The music analogy is Arnheim's own (p. 282), not my inference.
- Cross-reference status: Verified — consistent with later chapters' discussion of figure-ground (Ch. V).
- Rosetta Stone check: CSS z-index mapping added as rigorous; music counterpoint mapping added as structural.
- OCR issues: "averline or auromorphism" in source appears to be OCR corruption of "overlap or superposition"; meaning clear from context.
