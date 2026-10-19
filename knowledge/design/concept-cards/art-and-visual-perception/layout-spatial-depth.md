---
concept: "Spatial Depth in Layout and Interface Design"
slug: "layout-spatial-depth"
category: "layout-composition"
subcategory: "depth-and-layering"
tier: "intermediate"
layer: "2-domain"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "V. Space"
chapter_number: 5
pdf_page: 141
section: "Application to Painting"
extraction_confidence: "medium"
aliases:
  - "UI depth hierarchy"
  - "interface layering"
  - "elevation system"
prerequisites:
  - "depth-levels"
  - "figure-ground"
  - "overlap-depth-cue"
  - "atmospheric-perspective"
extends: []
related:
  - "negative-space"
  - "depth-levels"
  - "size-gradient"
  - "atmospheric-perspective"
  - "perceptual-transparency"
contrasts_with:
  - "flat-design"
answers_questions:
  - "What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "Given a data-rich card (title, status badge, three metrics, timestamp, action button), how do you assign visual hierarchy: what gets the most weight, what gets de-emphasized, and why?"
  - "A dark-mode implementation simply inverts all colours. Text on some backgrounds becomes unreadable. What went wrong?"
  - "How do you systematically audit an existing interface for visual design quality? What checklist of principles and patterns do you evaluate, in what order?"
rosetta_stone:
  -
    domain: "engineering"
    concept: "CSS z-index stacking, elevation tokens, shadow scale"
    rating: "structural"
    note: "Paint and shadow tokens support a chosen convention, not a perceptual or priority metric. Inspected Material Web generated M3 v0.192 has levels 0–5 and values 0,1,3,6,8,12; this is not universal policy."
css_implementation:
  -
    property: "box-shadow"
    example: "box-shadow: 0 2px 4px rgb(0 0 0 / .1); /* optional treatment, not a depth/priority measurement */"
    support: "baseline"
  -
    property: "z-index"
    example: "--z-base: 0; --z-content: 1; --z-nav: 10; --z-modal: 100; /* optional project convention; nested contexts remain local */"
    support: "baseline"
  -
    property: "filter: drop-shadow()"
    example: "filter: drop-shadow(0 4px 8px rgb(0 0 0 / .15)); /* shadow of rendered alpha shape; inspect result */"
    support: "baseline"
---

# Quick Definition

Interface depth treatments can use overlap, shadow, scale, colour or transparency to communicate selected relationships. Paint order and perceived depth do not determine information priority, semantics or a complete widget.

# Core Definition

This presents the represented Arnheim account alongside current analytic qualifications. Original edition, pages, quotations, figures, experiments, physiology and historical claims remain unassessed; the technical constructions below do not certify source fidelity.

Arnheim’s painting account motivates attending to visible relationships rather than relying only on what an observer knows. Its UI application is a separate synthesis. A project may organize overlays with named tokens, local stacking rules or another existing convention. No fixed 3–5 planes, compulsory architecture, stronger shadow for important content or fixed depth-to-attention mapping follows. Flat surfaces can communicate hierarchy through type, colour, contrast, weight, size and spacing.

Retained wording from the represented account (original fidelity unassessed):

"In looking at photographs or representational paintings, the viewer is helped somewhat by what he knows about physical space from his own experience. He knows that a large human figure is meant to be closer by than a small house. The artist, however, cannot rely much on mere knowledge. If he wants a figure to stand out against the background, he must use the direct visual effect of perceptual factors"

"a continuous relief in which areas at different distances border upon one another"

"the number of depth levels in a given pattern is as small as conditions permit"

# Prerequisites

- **Depth Levels** — Selected plane relations supply the vocabulary for discussing layered visibility.
- **Figure-Ground** — Contour ownership and region separation supply the comparison used here.
- **Overlap Depth Cue** — Contour interruption and hidden continuation help compare opaque and layered readings.
- **Atmospheric Perspective** — Medium-related contrast/colour changes are one optional cue family, distinct from blur alone.

# Key Properties

1. Stacking contexts constrain comparable paint order.
2. Shadows are optional rendered cues rather than calibrated distances.
3. Theme changes need actual pair/state review.
4. Semantic priority and foreground placement are distinct.
5. Preserve established project identity, tokens and actual component roles.

# Construction / Recognition

## To Construct/Create:

1. Identify the content, task and actual overlay/visibility requirements.
2. Reuse the project’s ordering and token system where useful.
3. Choose flat or spatial treatments with reasons tied to those requirements.
4. Inspect actual states, semantics, keyboard/focus/reading order and usable rest/fallback behavior.

## To Identify/Recognise (audit):

1. Inventory actual overlapping surfaces and contexts.
2. Compare intended spatial relations with visible overlap, shadow and contrast.
3. Inspect critical text, controls, boundaries and states over their resolved backgrounds.
4. Record dark/other themes, failures and untested behavior separately.

# Context & Application

The inspected [Material Web generated M3 v0.192 elevation file](https://raw.githubusercontent.com/material-components/material-web/main/tokens/versions/v0_192/_md-sys-elevation.scss) has levels 0–5 with values 0,1,3,6,8,12. That named version is not a universal elevation policy or another generation’s 0–24dp system. Other platform conventions require their own versioned evidence. A data card still needs title identity, status meaning, three metric comparisons, timestamp freshness and action clarity; emphasis follows its actual task.

## Cross-Domain Connections

**Engineering → STRUCTURAL**: z-index, box-shadow and drop-shadow implement paint ordering or shadow geometry. They can support a chosen elevation convention but do not directly implement Arnheim’s percept or semantic hierarchy. A shadowless card can be important; a visually prominent heading need not occlude anything.

# Examples

Source-specific examples and quotations below are retained as reports with their original wording and locators. They are not independently checked historical, experimental or universal claims. Applied examples are qualified design proposals.

**Example 1** (p. 168): "The artist, however, cannot rely much on mere knowledge. If he wants a figure to stand out against the background, he must use the direct visual effect of perceptual factors." — Arnheim (principle of active depth cueing)

**Example 2** (p. 182): "Pictorial space, therefore, is best described as a continuous relief in which areas at different distances border upon one another." — Arnheim (the depth relief model)

**Example 3** (p. 160): Economy principle: "the number of depth levels in a given pattern is as small as conditions permit." — Arnheim (minimum viable depth complexity)

**Example 4** (UI): For an incident-response card, status and an anomalous metric may lead; for routine comparison, the three metrics may lead. Preserve title identity, status meaning, three metric labels/values, timestamp freshness and a clear action. Choose size, weight, contrast and spacing for the task; none requires its own depth plane.

**Example 5** (dark mode failure): Retained design scenario: "A dark-mode implementation simply inverts all colours. Text on some backgrounds becomes unreadable." A theme inversion needs actual pair/state diagnosis. Exchanging black and white retains 21:1. Resolve overlay and backdrop colours, inspect semantic roles, boundaries and text, and record the actual failing pairs before assigning a cause.

# Relationships

These are scoped reading connections. Builds Upon supports understanding; Enables names a possible downstream use; Related is an association; Contrasts With names a comparison. They do not establish universal causes, subtypes or verified historical sequences. Ordinary downstream uses are not invented card identities.

## Builds Upon

- **Depth Levels** — Perceived plane descriptions motivate, but do not dictate, UI elevation conventions.
- **Figure-Ground** — Region separation can help distinguish surfaces without deciding every UI’s hierarchy.
- **Overlap Depth Cue** — Visible occlusion can support overlay order.
- **Atmospheric Perspective** — Blur and contrast treatments may suggest recession but are optional and differ from atmospheric physics.

## Enables

- **Consistent Visual Hierarchy** — Depth can contribute attention without becoming information priority.
- **Elevation Design Tokens** — Existing project tokens may encode ordering or shadows when useful; no architecture is mandated.

## Related

- **Negative Space** — Spacing communicates grouping, not a calibrated gap between planes.
- **Size Gradient** — Size can contribute emphasis without proving distance or importance.
- **Perceptual Transparency** — Visible-through treatments may suggest layers; compositing and perception differ.

## Contrasts With

- **Flat Design** — The existing flat-design practice construct reduces depth emphasis; it can retain overlap and shallow planes and is not identical with the historical frontal card.

# Common Errors

- **Error**: Solving every layering issue by increasing z-index or shadow.
  **Correction**: Inspect parent contexts, geometry and the actual visibility need.

- **Error**: Inferring a dark-mode contrast failure from inversion alone.
  **Correction**: Enumerate actual pairs/states and resolve overlays. Black and white exchanged retain 21:1; a failing pair, semantic colour-role error or reversed shadow needs separate diagnosis.

# Common Confusions

- **Confusion**: Every elevation needs a stronger or softer shadow.
  **Clarification**: Chosen lighting and task determine the treatment; no mandatory ladder follows.

- **Confusion**: Spatial clarity establishes an accessible modal.
  **Clarification**: Dialog semantics, focus management, keyboard behavior, reading order and actual preference/fallback checks remain separate. This card supplies a local audit contribution, not a complete ordered audit.

# Source Reference

Chapter V: Space, "Art and Visual Perception," pp. 154–200 (Depth Levels, Application to Painting sections); applied synthesis with UI design practice.

# Verification Notes

The bullets below are preserved historical extraction assertions, not current verification. Frozen confidence, cross-reference, source-reading and OCR claims do not settle original-dependent fidelity. Current same-context review supports only the explicitly scoped technical constructions, contextual teaching and local comparisons; it establishes no browser, observer, comfort or physiological result.

- Definition source: Synthesised and extended from Arnheim's discussion; application to UI design is an original synthesis, not a direct Arnheim claim
- Confidence rationale: Medium — core concepts are from Arnheim; UI application is my synthesis
- Uncertainties: Arnheim does not directly discuss UI design; the mapping is conceptually rigorous but attributable to Arnheim only at the level of source principles
- Cross-reference status: Verified (principles); application synthesised
- Rosetta Stone check: Mapping added — elevation tokens/CSS shadows is rigorous
- OCR issues: None significant
