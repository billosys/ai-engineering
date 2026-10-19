---
concept: "Overlap as Depth Cue"
slug: "overlap-depth-cue"
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
section: "Depth by Overlapping"
extraction_confidence: "high"
aliases:
  - "occlusion"
  - "interposition"
  - "superposition"
  - "overlapping"
prerequisites:
  - "figure-ground"
  - "pictorial-space"
extends: []
related:
  - "depth-levels"
  - "perceptual-transparency"
  - "size-gradient"
contrasts_with:
  - "size-gradient"
  - "atmospheric-perspective"
answers_questions:
  - "What are the gestalt principles of perceptual grouping, and how does each one work?"
  - "What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "How do you systematically audit an existing interface for visual design quality? What checklist of principles and patterns do you evaluate, in what order?"
rosetta_stone:
  -
    domain: "engineering"
    concept: "z-index / CSS stacking context"
    rating: "structural"
    note: "Paint order can yield occlusion only with intersecting painted geometry and appropriate alpha in comparable contexts. It supplies no global distance or semantic priority."
css_implementation:
  -
    property: "z-index"
    example: "position: relative; z-index: 2; /* eligible paint order in relevant context */"
    support: "baseline"
  -
    property: "position"
    example: "position: absolute; /* layout choice; painted intersection/alpha determine hiding */"
    support: "baseline"
---

# Quick Definition

Occluding overlap can cue depth when one visible boundary interrupts another form and that form is read as continuing behind it. Paint order, actual occlusion and perceived depth are separate conditions.

# Core Definition

This presents the represented Arnheim account alongside current analytic qualifications. Original edition, pages, quotations, figures, experiments, physiology and historical claims remain unassessed; the technical constructions below do not certify source fidelity.

Arnheim explains superposition through a preference for complete regular forms over irregular fragments. Good continuation can guide a hidden-contour reading; amodal completion behind an occluder is related to, but not identical with, visible closure of a gap. Helmholtz’s uninterrupted-contour heuristic is reported here with the surrounding global-structure qualification. The Philostratus and Kopfermann cases remain source reports, not proof that overlap always dominates physical depth, other cues or attention.

Retained wording from the represented account (original fidelity unassessed):

"When one of the components actually cuts off a part of the other, the perceptual urge to see a superposition becomes compelling because it serves to complete the incomplete shape"

# Prerequisites

- **Figure-Ground** — Contour ownership and region separation supply the comparison used here.
- **Pictorial Space** — Pictorial spatial readings supply the vocabulary for this particular cue or convention.

# Key Properties

1. Opaque painted overlap can hide part of a rear form.
2. A visible contour interruption can support completion behind it without determining unique hidden geometry.
3. Transparency can retain information from both regions.
4. A shadow can suggest layering without being the object’s literal occlusion of another contour.
5. No universal cue-strength, calmness or intensity ranking is established.

# Construction / Recognition

## To Construct/Create:

1. If opaque depth order helps, position one painted region across another.
2. Check contour interruption and whether the hidden content remains understandable.
3. Compare separation, transparency and overlap for the supplied task.
4. Use semantics and states to establish interaction rather than assuming a foreground object is clickable.

## To Identify/Recognise:

1. Locate contour junctions and interruptions.
2. Distinguish rendered masking from the inferred complete form.
3. Inspect alpha and context where the boundary is weak.
4. During an audit, compare intended order, hidden content and actual overlay states.

# Context & Application

Cards, modals, menus, illustrations and charts can use overlap. A FAB may occlude list content and suggest a separate layer, but the button still needs an appropriate role, label, focus behavior and placement that preserves the task. Overlap can be calm or energetic; it is not forbidden in data tables.

## Cross-Domain Connections

**Engineering → STRUCTURAL**: z-index orders eligible boxes within relevant stacking contexts. Contexts are atomic groups, so a child at 999 in a lower parent cannot outrank a higher sibling context at 2. Occlusion also needs intersecting painted geometry and appropriate alpha. Position:absolute is one arrangement, not the sole way to overlap. Shadows are optional cues, not physical distance or priority.

# Examples

Source-specific examples and quotations below are retained as reports with their original wording and locators. They are not independently checked historical, experimental or universal claims. Applied examples are qualified design proposals.

**Example 1** (p. 280): "When one of the components actually cuts off a part of the other, the perceptual urge to see a superposition becomes compelling because it serves to complete the incomplete shape." — Arnheim

**Example 2** (p. 308): Arnheim cites the Greek sophist Philostratus describing a painting in which soldiers are depicted successively more occluded — "some are seen in full figure, others with the legs hidden, others from the waist up" — as a spatial ordering device.

**Example 3** (p. 316): Kopfermann's experiment: a larger triangle seen overlapping a smaller one in a composite view even when physically the smaller is in front, demonstrating that overlap perception can override physical reality.

**Example 4** (UI): A floating action button can visibly hide part of a list. This suggests separation only in context and does not supply its label, semantics, focus behavior or task priority.

# Relationships

These are scoped reading connections. Builds Upon supports understanding; Enables names a possible downstream use; Related is an association; Contrasts With names a comparison. They do not establish universal causes, subtypes or verified historical sequences. Ordinary downstream uses are not invented card identities.

## Builds Upon

- **Figure-Ground** — An occluding surface can claim a contour while another is read as continuing behind.
- **Simplicity Principle (Gestalt)** — Good continuation and simplicity can favor a hidden-form candidate; amodal completion is not identical with visible closure.

## Enables

- **Depth Levels** — Occlusion can organize several front/behind relations.
- **Perceptual Transparency** — A visible-through layer is an overlapping case with different visibility.
- **Visual Tension** — The represented account uses tension expressively; overlap need not always intensify it.

## Related

- **Size Gradient** — Scale and occlusion can be compared or combined under scene assumptions.
- **Depth Levels** — Occluding relations can contribute a multilevel depth reading.

## Contrasts With

- **Size Gradient** — Scaling and contour interruption are different observations; conditional independence is not implied.
- **Atmospheric Perspective** — Haze/contrast change differs from contour interruption, although they can co-occur.

# Common Errors

- **Error**: Equating a physically nearer or higher-z element with guaranteed perceived frontness.
  **Correction**: Check actual painted overlap, context and reading. The Kopfermann report illustrates a particular conflict.

- **Error**: Assuming overlap always creates unwanted tension.
  **Correction**: Judge the actual composition and task.

# Common Confusions

- **Confusion**: Overlap is the same as z-index.
  **Clarification**: Paint order can produce visible interruption; perceived occlusion needs the relevant geometry and context.

- **Confusion**: Completion means visible closure.
  **Clarification**: Continuing a hidden contour is an amodal reading; filling a visible gap and reading a closed outline are related but distinct.

# Source Reference

Chapter V: Space, "Art and Visual Perception," pp. 278–316 (Depth by Overlapping section).

# Verification Notes

The bullets below are preserved historical extraction assertions, not current verification. Frozen confidence, cross-reference, source-reading and OCR claims do not settle original-dependent fidelity. Current same-context review supports only the explicitly scoped technical constructions, contextual teaching and local comparisons; it establishes no browser, observer, comfort or physiological result.

- Definition source: Synthesised from Arnheim's detailed discussion of overlap, pp. 278–316; Helmholtz rule quoted directly
- Confidence rationale: Arnheim's treatment is precise and extensively illustrated with figures and experiments
- Uncertainties: None significant
- Cross-reference status: Verified
- Rosetta Stone check: Mapping added — z-index/stacking context is a rigorous engineering implementation
- OCR issues: Some figure numbers have OCR artifacts; no impact on conceptual content
