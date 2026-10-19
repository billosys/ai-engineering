---
concept: "Depth Levels"
slug: "depth-levels"
category: "visual-perception"
subcategory: "spatial-organisation"
tier: "intermediate"
layer: "0-perception"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "V. Space"
chapter_number: 5
pdf_page: 141
section: "Depth Levels"
extraction_confidence: "high"
aliases:
  - "spatial planes"
  - "depth planes"
  - "pictorial layers"
prerequisites:
  - "figure-ground"
  - "overlap-depth-cue"
  - "pictorial-space"
extends:
  - "figure-ground"
related:
  - "overlap-depth-cue"
  - "perceptual-transparency"
  - "negative-space"
contrasts_with:
  - "figure-ground"
answers_questions:
  - "What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "Given a data-rich card (title, status badge, three metrics, timestamp, action button), how do you assign visual hierarchy: what gets the most weight, what gets de-emphasized, and why?"
  - "How do you systematically audit an existing interface for visual design quality? What checklist of principles and patterns do you evaluate, in what order?"
rosetta_stone:
  -
    domain: "engineering"
    concept: "CSS stacking context / z-index layers"
    rating: "structural"
    note: "Stack levels order eligible paint within comparable contexts; they are not perceived planes or distances."
  -
    domain: "engineering"
    concept: "Layered architecture in UI (DOM tree, stacking contexts, compositing layers)"
    rating: "structural"
    note: "DOM structure, stacking contexts and compositor layers are distinct; none maps one-to-one to perceived depth."
css_implementation:
  -
    property: "z-index"
    example: "position: relative; z-index: 1; /* local stack level, not a perceived distance */"
    support: "baseline"
  -
    property: "isolation: isolate"
    example: "isolation: isolate; /* atomic stacking context, not a new perceived plane */"
    support: "baseline"
---

# Quick Definition

Depth levels describe perceived foreground/background planes or regions at differing distances in a picture. They generalize a two-plane figure-ground description without equating perceived distance with CSS stack levels.

# Core Definition

This presents the represented Arnheim account alongside current analytic qualifications. Original edition, pages, quotations, figures, experiments, physiology and historical claims remain unassessed; the technical constructions below do not certify source fidelity.

Arnheim describes patterns distributed across depth levels and a tendency toward economy: use as few levels as the pattern permits in his analysis. The disk/square and Arp examples concern possible readings, not an algorithm that assigns every image a unique count. A depth relief may be shallow, stepped or continuous. An element can serve as figure against one region and ground for another. In UI work, perceived layering, semantic hierarchy, DOM structure, stacking contexts and compositor layers require separate descriptions.

Retained wording from the represented account (original fidelity unassessed):

"It seems more adequate to speak of patterns distributed over a number of depth levels, the basic figure-ground pattern being a special case, namely an organization of only two levels"

"there is a tendency to simplification by economy, which means that the number of depth levels in a given pattern is as small as conditions permit"

# Prerequisites

- **Figure-Ground** — Contour ownership and region separation supply the comparison used here.
- **Overlap Depth Cue** — Contour interruption and hidden continuation help compare opaque and layered readings.
- **Pictorial Space** — Pictorial spatial readings supply the vocabulary for this particular cue or convention.

# Key Properties

1. Perceived levels need not be discrete numerical distances.
2. A continuous relief and a count of selected planes are different descriptions.
3. Local paint order can contribute to occlusion without defining perceptual depth.
4. The number of useful UI layers depends on content and interaction; no 3–5 rule follows.

# Construction / Recognition

## To Construct/Create:

1. Identify the intended foreground/background relations.
2. Compare overlaps, transparency and shallow or continuous treatments.
3. Choose any numbering convention explicitly; larger z-index is frontward only within the relevant paint-order comparison.
4. Retain established project tokens when useful; avoid inventing unused levels.

## To Identify/Recognise:

1. List which painted surfaces hide which others.
2. Describe which appear to occupy the same or different planes.
3. Inspect changes of perceived depth separately from stacking-context boundaries.
4. For an audit, compare intended relationships, content visibility and actual overlay states.

# Context & Application

UI overlays and data visualisations can use layering to express relationships. For a card with title, status, three metrics, time and action, the task determines emphasis: an urgent status or critical metric may lead, the title identifies the subject, time establishes freshness, and the action needs an understandable role. This card contributes plane/grouping analysis, not a full assignment of typographic weights or an entire ordered interface audit.

## Cross-Domain Connections

**Engineering → STRUCTURAL**: A stacking context is an atomic paint group in its parent. A child at z-index:999 inside a context below a sibling context at 2 cannot escape that parent order. Integers are not physical distances or semantic priorities. isolation:isolate creates a context; compositor-layer allocation is a separate implementation decision. See [CSS 2.2 stacking](https://www.w3.org/TR/CSS22/visuren.html#layers).

# Examples

Source-specific examples and quotations below are retained as reports with their original wording and locators. They are not independently checked historical, experimental or universal claims. Applied examples are qualified design proposals.

**Example 1** (p. 158): "It seems more adequate to speak of patterns distributed over a number of depth levels, the basic figure-ground pattern being a special case, namely an organization of only two levels." — Arnheim

**Example 2** (p. 160): Disk on square — "The principle of economy would of course favour a one-plane solution as the simplest. This leaves us with a smaller number of planes—that is, with a spatially simpler pattern." — Arnheim

**Example 3** (p. 164): The Arp woodcut analysis — Arnheim describes how the same image can be perceived as a 1-, 2-, 3-, or 4-plane depth arrangement depending on which perceptual factors dominate.

**Example 4** (p. 182): "Pictorial space, therefore, is best described as a continuous relief in which areas at different distances border upon one another." — Arnheim

**Example 5** (UI): A project may order wallpaper (-1), body (0), header (1), dropdown (2), scrim (99), dialog (100) and tooltip (200) within suitable contexts. These illustrative values are local paint conventions, not measured planes or guaranteed priority.

# Relationships

These are scoped reading connections. Builds Upon supports understanding; Enables names a possible downstream use; Related is an association; Contrasts With names a comparison. They do not establish universal causes, subtypes or verified historical sequences. Ordinary downstream uses are not invented card identities.

## Builds Upon

- **Figure-Ground** — The two-plane figure-ground account is conceptually elaborated to multiple planes.
- **Overlap Depth Cue** — Occlusion can support order between selected regions.
- **Pictorial Space** — Depth relief is a vocabulary for describing a pictorial reading.

## Enables

- **Visual Hierarchy** — Layering can contribute salience without setting information priority.
- **Spatial Organisation** — Plane relations are one description of spatial organization.

## Related

- **Perceptual Transparency** — An underlying region can remain visible through an interpreted front layer.
- **Negative Space** — Intervening shapes can contribute grouping without being a calibrated inter-plane distance.

## Contrasts With

- **Figure-Ground** — Compare a selected two-plane account with a multilevel or continuous description; no infinite physical ground is required.

# Common Errors

- **Error**: Treating each z-index integer or compositor layer as a perceived plane.
  **Correction**: Inspect comparable contexts and actual painted overlap. Use project-specific ordering only where it serves real overlays; neither a token hierarchy nor a fixed number of planes is required.

# Common Confusions

- **Confusion**: More levels necessarily create richer space.
  **Clarification**: Added planes can help a task or obscure relationships. Arnheim’s economy account is a contextual guide, not a measured UI complexity law.

# Source Reference

Chapter V: Space, "Art and Visual Perception," pp. 154–198 (Depth Levels section and Application to Painting).

# Verification Notes

The bullets below are preserved historical extraction assertions, not current verification. Frozen confidence, cross-reference, source-reading and OCR claims do not settle original-dependent fidelity. Current same-context review supports only the explicitly scoped technical constructions, contextual teaching and local comparisons; it establishes no browser, observer, comfort or physiological result.

- Definition source: Synthesised from discussion in Chapter V (Space), pp. 154–198; key quote cited directly
- Confidence rationale: High — Arnheim devotes an extended section to depth levels and gives precise examples
- Uncertainties: None significant
- Cross-reference status: Verified
- Rosetta Stone check: Mappings added — CSS stacking context is rigorous
- OCR issues: None significant
