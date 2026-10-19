---
concept: "Contour Rivalry"
slug: "contour-rivalry"
category: "visual-perception"
subcategory: "perceptual-organisation"
tier: "intermediate"
layer: "0-perception"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "V. Space"
chapter_number: 5
pdf_page: 141
section: "Contour Rivalry"
extraction_confidence: "high"
aliases:
  - "border rivalry"
  - "shared contour ambiguity"
  - "contour ownership"
prerequisites:
  - "figure-ground"
extends:
  - "figure-ground"
related:
  - "spatial-ambiguity-paradox"
  - "negative-space"
  - "overlap-depth-cue"
contrasts_with:
  - "clear-figure-ground"
answers_questions: []
rosetta_stone:
  -
    domain: "engineering"
    concept: "Border/outline ownership in CSS — which element 'owns' the boundary?"
    rating: "structural"
    note: "CSS border geometry differs from perceptual ownership. Collapsed table borders use grid lines and conflict resolution; separate borders and gaps do not guarantee a stable percept."
css_implementation:
  -
    property: "border"
    example: "border: 1px solid currentColor; /* authored boundary; inspect perceived ownership */"
    support: "baseline"
  -
    property: "outline"
    example: "outline: 2px solid currentColor; outline-offset: 2px; /* inspect actual component/focus state */"
    support: "baseline"
---

# Quick Definition

Contour rivalry is the reported instability of a shared perceptual boundary when adjacent regions compete to own it. Perceptual contour ownership differs from which CSS element specifies a border.

# Core Definition

This presents the represented Arnheim account alongside current analytic qualifications. Original edition, pages, quotations, figures, experiments, physiology and historical claims remain unassessed; the technical constructions below do not certify source fidelity.

Arnheim describes contour one-sidedness and a tug-of-war between similarly qualified surfaces. In this account, the figure claims a boundary and the ground is experienced as continuing behind it; reversals and competing readings can occur. The reported hexagons, Piaget copies and honeycomb drawings illustrate this account, without establishing that every touching pair is unstable. Convexity, symmetry, enclosure and context can favor a reading; they are not a universal winner algorithm. The developmental and clinical observations remain reports requiring original evidence.

Retained wording from the represented account (original fidelity unassessed):

"A contour can be monopolized by one of the surfaces bordering on it"

"When two similarly qualified competing surfaces both claim the contour, we observe what is known as contour rivalry. Perceived as a whole, the figure looks stable enough, but when we concentrate on the common central vertical we notice a tug-of-war. The sharing of borders is uncomfortable, and the two hexagons exhibit an urge to pull apart"

# Prerequisites

- **Figure-Ground** — Contour ownership and region separation supply the comparison used here.

# Key Properties

1. Authored borders and perceived boundaries are different constructs.
2. Adjacent regions can admit stable or competing ownership readings.
3. Gaps, enclosure or contrast changes can alter a reading; none guarantees a cure.
4. A clear-figure-ground condition means a stable local ownership reading, not a separate card identity.

# Construction / Recognition

## To Construct/Create (intentionally):

1. If ambiguity serves the composition, place similarly organized shapes along a common boundary.
2. Vary enclosure, symmetry and surrounding context to explore alternative readings.
3. Treat any actual rivalry as an observation to inspect, not a consequence guaranteed by adjacency.

## To Identify/Recognise:

1. Locate the shared visible boundary.
2. Ask which region seems bounded and whether the reading reverses.
3. Compare the intended task with what the boundary communicates.

# Context & Application

Table cells, adjacent buttons, cards and icons can use shared boundaries successfully. Inspect their actual reading before changing spacing or contrast. A divider may read as a separate shape, but neutrality is not assured by its DOM ownership.

## Cross-Domain Connections

**Engineering → STRUCTURAL**: CSS border declarations specify paint geometry. In the [CSS 2.2 collapsed table model](https://www.w3.org/TR/CSS22/tables.html#collapsing-borders), borders lie on cell grid lines and competing styles are selected by conflict rules. Separate borders and border-spacing provide another geometry; neither model determines perceptual ownership or prevents rivalry.

# Examples

Source-specific examples and quotations below are retained as reports with their original wording and locators. They are not independently checked historical, experimental or universal claims. Applied examples are qualified design proposals.

**Example 1** (p. 65): "When two similarly qualified competing surfaces both claim the contour, we observe what is known as contour rivalry. Perceived as a whole, the figure looks stable enough, but when we concentrate on the common central vertical we notice a tug-of-war." — Arnheim

**Example 2** (p. 73): "When young children were asked by Piaget to copy geometric designs in which circles or triangles touched each other, they often eliminated the contact in their reproductions." — Arnheim (showing the perceptual pressure to resolve rivalry by separation)

**Example 3** (p. 73): "People were asked to draw a honeycomb pattern. They often made the hexagons independent of one another by leaving space between them, and even emphasized the interstices by shading the figures." — Arnheim

**Example 4** (UI): Adjacent cards can use a common border successfully. Inspect an actual competing-boundary reading before trying a gap, contrast change or another separator; no mandatory 8px or 16px minimum follows.

# Relationships

These are scoped reading connections. Builds Upon supports understanding; Enables names a possible downstream use; Related is an association; Contrasts With names a comparison. They do not establish universal causes, subtypes or verified historical sequences. Ordinary downstream uses are not invented card identities.

## Builds Upon

- **Figure-Ground** — Figure-ground ownership supplies the comparison in which rivalry is described.

## Enables

- **Spatial Ambiguity/Paradox** — Competing ownership can yield one local kind of ambiguity.
- **Negative Space Design** — Spacing is one possible compositional response, without a guaranteed cure.

## Related

- **Spatial Ambiguity/Paradox** — Rivalry concerns a shared boundary rather than every global paradox.
- **Negative Space** — Gaps change region geometry and may alter the reading.
- **Overlap Depth Cue** — Occlusion can favor an ownership reading when the painted contour actually interrupts another.

## Contrasts With

- **Clear Figure-Ground** — This existing local condition means stable ownership under the selected reading; it is not a new card.

# Common Errors

- **Error**: Treating CSS border ownership as proof of perceptual stability.
  **Correction**: Inspect the visible boundary and surrounding shapes. Use collapsed or separate table borders as the data requires; no collapse ban or mandatory 8/16px card gap follows.

# Common Confusions

- **Confusion**: Rivalry requires equal-sized shapes.
  **Clarification**: The represented account concerns competing figure factors, not size equality alone.

- **Confusion**: A divider always resolves ownership.
  **Clarification**: It can introduce a third visible shape or still be read as a neighboring edge; inspect the result.

# Source Reference

Chapter V: Space, "Art and Visual Perception," pp. 63–75 (Contour Rivalry section).

# Verification Notes

The bullets below are preserved historical extraction assertions, not current verification. Frozen confidence, cross-reference, source-reading and OCR claims do not settle original-dependent fidelity. Current same-context review supports only the explicitly scoped technical constructions, contextual teaching and local comparisons; it establishes no browser, observer, comfort or physiological result.

- Definition source: Synthesised from Arnheim's discussion, pp. 63–75; key quotes cited directly
- Confidence rationale: High — Arnheim gives contour rivalry a dedicated section with precise examples and experimental evidence
- Uncertainties: None significant
- Cross-reference status: Verified
- Rosetta Stone check: Mapping added — CSS border ownership is structural
- OCR issues: None significant
