---
concept: "Convexity and Concavity in Depth Perception"
slug: "convexity-concavity-depth"
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
section: "Concavity in Sculpture"
extraction_confidence: "medium"
aliases:
  - "convex-concave figure-ground"
  - "surface curvature depth cue"
  - "sculptural depth"
prerequisites:
  - "figure-ground"
  - "pictorial-space"
extends:
  - "figure-ground"
related:
  - "contour-rivalry"
  - "negative-space"
  - "depth-levels"
contrasts_with:
  - "flat-pictorial-space"
answers_questions: []
rosetta_stone:
  -
    domain: "engineering"
    concept: "CSS convex vs. concave UI elements — raised buttons vs. inset fields"
    rating: "structural"
    note: "Outer and inset shadows can suggest relief under a lighting convention; they do not guarantee contour ownership, clickability or a receptive state."
css_implementation:
  -
    property: "box-shadow"
    example: "box-shadow: 0 2px 4px rgb(0 0 0 / .2); /* optional raised treatment */"
    support: "baseline"
  -
    property: "box-shadow (inset)"
    example: "box-shadow: inset 0 2px 4px rgb(0 0 0 / .2); /* optional recessed treatment; check state */"
    support: "baseline"
---

# Quick Definition

Convex and concave contours can contribute to figure-ground and relief readings. Arnheim interprets convexity as advancing and concavity as receptive; those expressive tendencies do not determine every depth or interaction outcome.

# Core Definition

This presents the represented Arnheim account alongside current analytic qualifications. Original edition, pages, quotations, figures, experiments, physiology and historical claims remain unassessed; the technical constructions below do not certify source fidelity.

Arnheim develops Rubin’s convexity tendency into an account of sculptural expansion and recession. His Archipenko and Henry Moore examples give surrounding concave space an active role rather than treating it as mere absence. A convex outline in a flat drawing, a physically curved sculpture and a CSS inset shadow are distinct constructions. UI relief can suggest raised or recessed surfaces under a chosen lighting convention, but cannot establish clickability, receptiveness or a universal nearer/farther order.

Retained wording from the represented account (original fidelity unassessed):

"convexity makes for figure, concavity for ground"

"seems to expand and to rise"

"the surrounding space, instead of passively consenting to be displaced by the statue, assumes an active role. It invades the body and seizes the contour surfaces of the concave units"

"Convexity and concavity are not only mutually exclusive, they are also opposites dynamically, the one actively expanding, the other passively withdrawing"

# Prerequisites

- **Figure-Ground** — Contour ownership and region separation supply the comparison used here.
- **Pictorial Space** — Pictorial spatial readings supply the vocabulary for this particular cue or convention.

# Key Properties

1. Convexity is defined relative to a chosen region and its contour.
2. Figure-ground factors and surrounding context can compete.
3. Concave space can acquire figure quality in the represented sculpture account.
4. Inset and outer shadows can suggest relief without producing physical curvature or complete controls.

# Construction / Recognition

## To Construct/Create:

1. Choose a raised, inset or flat treatment that fits the actual component and state.
2. Use an explicit lighting convention if simulated relief helps.
3. Keep visible labels, boundaries and focus states understandable without the shadow.

## To Identify/Recognise:

1. Identify which region makes an edge convex or concave.
2. Separate the contour shape from any shading-based relief.
3. Check whether the intended object or space is actually legible.

# Context & Application

Buttons, inputs, icons, sculpture and neumorphic treatments provide comparisons. An inset button can intentionally represent a pressed state; an outward shadow is not obligatory. Flat controls remain available.

## Cross-Domain Connections

**Engineering → STRUCTURAL**: box-shadow and inset box-shadow paint different shadow geometries. These can suggest raised or recessed treatments under a chosen lighting interpretation; they do not directly implement Rubin’s contour-ownership tendency or guarantee an affordance.

# Examples

Source-specific examples and quotations below are retained as reports with their original wording and locators. They are not independently checked historical, experimental or universal claims. Applied examples are qualified design proposals.

**Example 1** (p. 134): "Convexity makes for figure, concavity for ground." — Arnheim, citing Rubin's rule.

**Example 2** (p. 85): "Convexity and concavity are not only mutually exclusive, they are also opposites dynamically, the one actively expanding, the other passively withdrawing." — Arnheim

**Example 3** (p. 228): Henry Moore's sculpture — "The convexity of all form in the Maillol preserves an active element in spite of the essentially passive subject matter. In Moore's work a passive and receptive quality is obtained not only through the attitude of the woman, but even more compellingly through the hollowness of shape." — Arnheim

**Example 4** (neumorphic UI): A neumorphic button can use upper-left light and lower-right dark shadows to suggest relief; an inset treatment can indicate a pressed state or recess. This is a chosen visual convention, with actual labels, contrast and interaction checked separately.

# Relationships

These are scoped reading connections. Builds Upon supports understanding; Enables names a possible downstream use; Related is an association; Contrasts With names a comparison. They do not establish universal causes, subtypes or verified historical sequences. Ordinary downstream uses are not invented card identities.

## Builds Upon

- **Figure-Ground** — Convexity is one reported factor among competing figure-ground tendencies.

## Enables

- **Active vs. Passive Surface Design** — Raised/recessed interpretations can contribute to expression without assigning universal active/passive roles.
- **Tactile UI Affordances** — Relief can suggest a state, but labels, semantics and actual interaction establish its use.

## Related

- **Contour Rivalry** — Adjacent convex/concave regions can compete; this does not force rivalry.
- **Negative Space** — Concave regions can function as intervening space or acquire figure quality.

## Contrasts With

- **Flat Pictorial Space** — Flat treatments may reduce relief yet retain curved contours, shallow layers or overlap.

# Common Errors

- **Error**: Declaring inset button shadows a perceptual contradiction.
  **Correction**: Check the component’s actual pressed/unpressed states, labels and interaction. Relief is an optional cue, with its own contrast and state limits.

# Common Confusions

- **Confusion**: Concavity has no figure quality.
  **Clarification**: Moore and Archipenko are represented counterexamples; enclosure and context can make the surrounding space active. No rule makes every unbounded concavity passive.

# Source Reference

Chapter V: Space, "Art and Visual Perception," pp. 130–135, 214–254 (Figure and Ground rules; Concavity in Sculpture section).

# Verification Notes

The bullets below are preserved historical extraction assertions, not current verification. Frozen confidence, cross-reference, source-reading and OCR claims do not settle original-dependent fidelity. Current same-context review supports only the explicitly scoped technical constructions, contextual teaching and local comparisons; it establishes no browser, observer, comfort or physiological result.

- Definition source: Synthesised from discussion in Chapter V, primarily the concavity in sculpture section and figure-ground rules
- Confidence rationale: Medium — convexity principle is stated precisely in the context of figure-ground rules; application to sculpture is extended; application to 2D design and UI is my synthesis
- Uncertainties: Arnheim does not discuss UI directly; UI application is an original synthesis
- Cross-reference status: Verified (principles); UI application is synthesised
- Rosetta Stone check: Mapping added — CSS inset/outset shadows is structural
- OCR issues: None significant
