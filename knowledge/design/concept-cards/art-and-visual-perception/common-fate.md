---
concept: "Common Fate"
slug: "common-fate"
category: "visual-perception"
subcategory: "gestalt grouping"
tier: "foundational"
layer: "0-perception"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "VIII. Movement"
chapter_number: 8
pdf_page: 395
section: "When Do We See Motion?"
extraction_confidence: "medium"
aliases:
  - "law of common fate"
  - "synchronous motion grouping"
  - "co-motion grouping"
prerequisites:
  - "visual-perception"
  - "gestalt-theory-in-art"
extends:
  - "gestalt-theory-in-art"
related:
  - "phi-phenomenon"
  - "implied-motion"
  - "visual-rhythm"
contrasts_with:
  - "figure-ground"
answers_questions:
  - "What are the gestalt principles of perceptual grouping, and how does each one work?"
  - "How does the relationship between inter-group and intra-group spacing communicate which elements belong together (gestalt proximity)?"
rosetta_stone:
  -
    domain: "music"
    concept: "Parallel voice leading as coordinated change"
    rating: "structural"
    note: "Parallel direction can be compared with visual co-motion; register, timbre, interval and context affect voice independence, so fusion is not guaranteed."
  -
    domain: "engineering"
    concept: "Pub/sub coordination and visible shared change"
    rating: "structural"
    note: "Subscription can coordinate updates; actual starts and trajectories, not subscription or equal CSS duration alone, can supply a grouping cue."
css_implementation:
  -
    property: "animation"
    example: "animation: fadeIn 0.3s ease both; /* coordinate actual starts; grouping remains contextual */"
    support: "baseline"
  -
    property: "transition"
    example: "transition: opacity 200ms, transform 200ms; /* equal durations alone do not synchronize changes */"
    support: "baseline"
---

# Quick Definition

Common fate describes grouping through shared movement, especially common direction and speed. Broader synchronous changes can also cue grouping; their effect depends on the whole display and task.

# Core Definition

This presents the represented Arnheim account. Original edition/context, quotation fidelity, page bases, historical reports, experiments and physiology remain unassessed because the required original is unavailable. The current analytic corrections do not certify that fidelity.

Common fate is a classical Gestalt grouping principle. Shared motion can help several elements appear related. This differs from identifying one object across successive frames. The prior extraction connects both topics to Arnheim’s temporal-grouping discussion and quotes: "the familiar principles of grouping also play their parts. An object in motion is the more likely to preserve its identity the less it changes in size, shape, brightness, color, or speed." That passage concerns correspondence across time; it does not alone demonstrate grouping of several objects.

Shared motion and synchronous change are contextual grouping cues, not a rule that equivalence along any dimension always groups. Static birds pointing along similar axes can suggest a shared trajectory, but a still image does not exhibit actual co-motion.

# Prerequisites

- **Gestalt Theory** — Common fate is one gestalt grouping principle among several (proximity, similarity, continuity, closure); understanding the overall gestalt framework is necessary to understand common fate's role.
- **Visual Perception** — Basic understanding of figure-ground and perceptual grouping as active, constructive processes.

# Key Properties

1. Common direction and speed over an overlapping interval can support grouping.
2. Shared movement can compete with proximity and similarity; no cue always wins.
3. Synchronous fading or flashing is a broader shared-change case, distinct from common displacement.
4. Static aligned bird silhouettes can suggest a trajectory; this is a qualified implied-motion comparison.
5. Motion contrast with the surround and other grouping cues affect the interpretation.

# Construction / Recognition

## To Construct/Create:

1. For a proposed moving group, coordinate actual starts, directions and trajectories, then inspect the rendered result.
2. In a still, use aligned directional forms to suggest a shared trajectory without claiming temporal co-motion.
3. For card-grid entrances or exits, compare synchronous and staggered changes against the intended relationship.
4. Different group trajectories can help differentiate sets, alongside labels and spatial grouping.

## To Identify/Recognise:

1. Observe which elements actually move or change together, rather than inferring synchrony from equal CSS durations.
2. Separate grouping of multiple elements from correspondence of one element across frames.
3. Compare the display with shared motion removed while keeping relevant static cues; report the actual observation and its limits.

# Context & Application

- **Typical contexts**: UI animation, data visualisation, interactive choreography, iconography, layout design, dashboard animation, game UI.
- **Common applications**: Coordinated card entrances, list items scrolling together and chart-series highlights can suggest a set. Their grouping and meaning still depend on the visible pattern, labels, surrounding cues and task.

## Cross-Domain Connections

**Music → STRUCTURAL**: Parallel voice leading offers a comparison of coordinated change. Direction, register, timbre, interval and musical context can affect perceived independence; parallel motion does not invariably fuse voices or reproduce visual grouping.

**Engineering → STRUCTURAL**: A shared pub/sub event can coordinate UI updates. Subscription is a software relationship; only the resulting visible timing and trajectories can supply shared-change cues. Equal durations alone establish neither common starts nor perceptual grouping.

# Examples

These preserve the represented account’s examples and artistic judgments. Their original context and reported results remain unassessed; they are not universal laws or fresh observer measurements.

**Example 1** (p. 395, Stroboscopic Movement / grouping section): The represented Arnheim account relates similarity of location, role and trajectory to preserving identity across time. That is a correspondence example, not by itself a demonstration that multiple simultaneous objects form a group.

**Example 2** (p. 395, "The interaction of shape and motion," Metzger experiments): The represented Metzger crossing-path case concerns seeing consistent trajectories rather than exchanging directions at an intersection. It illustrates across-time correspondence; it is not interchangeable with the card/list/chart grouping applications.

# Relationships

## Builds Upon
- **Gestalt Theory** — Common fate is a direct extension of gestalt grouping into the temporal/motion domain.
- **Gestalt Similarity** — Common fate can be understood as "similarity of motion" — a temporal variant of the spatial similarity principle.

## Enables
- **Animation Choreography** — A possible use of shared visible change to suggest grouping; equal declarations do not guarantee the effect.
- **Data Visualisation Coordination** — Coordinated chart highlights can suggest related series; their meaning also needs data context and identifiable labels.

## Related
- **Phi Phenomenon** — Temporal apparent motion concerns motion percepts; common fate concerns grouping. The phi card distinguishes broader historical usage from precise pure-phi/beta terminology.
- **Implied Motion** — Static aligned forms may suggest a shared trajectory; a still does not demonstrate simultaneous displacement.
- **Visual Rhythm** — Repeated spatial accents can accompany aligned forms; spatial rhythm is not literally shared movement.

## Contrasts With
- **Figure-Ground** — Figure/surround organization and grouping are different questions. Motion can contribute to both; figure-ground is not static-only and shared motion need not erase their distinction.

# Common Errors

- **Error**: Assuming common fate only applies to elements moving in literally the same direction.
  **Correction**: Broader synchronous change can cue grouping even with differing trajectories. Keep this distinct from the narrower common-direction case; neither guarantees a result for every display.

- **Error**: Staggering all animations by default without considering common fate grouping.
  **Correction**: Stagger (sequential delay) changes temporal relations; it need not destroy grouping supported by overlap, sequence, proximity or other cues. Choose and inspect the pattern for the task.

# Common Confusions

- **Confusion**: Common fate and proximity are the same principle in motion contexts.
  **Clarification**: Proximity groups elements based on spatial closeness; common fate groups them based on shared motion direction/timing. Elements can be spatially distant yet grouped by common fate (e.g., two distant elements that both flash at the same moment).

- **Confusion**: Common fate is only relevant in animated or video contexts.
  **Clarification**: Static directional alignment may suggest a shared trajectory. Calling that implied common fate is an analogy; it is not a measured strength of co-motion grouping.

# Source Reference

Chapter VIII: Movement, "Art and Visual Perception," pp. 395–434. Common fate is addressed as part of the gestalt grouping discussion in "When Do We See Motion?" and in the "Stroboscopic Movement" section.

# Verification Notes

- Current review boundary: the legacy extraction notes below are preserved provenance, not this review’s original-source verification. Current technical/interpretive qualifications above and local relationship/CQ checks do not establish historical fidelity or measured observer behavior.

- Definition source: Synthesised from gestalt grouping discussion in Chapter VIII; common fate as a named principle is part of the gestalt canon Arnheim invokes throughout the chapter, though he does not isolate it in a dedicated sub-section.
- Confidence rationale: Medium — the principle is implicit in Arnheim's discussion of grouping principles operating temporally, but the term "common fate" is not always used explicitly in the OCR-visible text; the concept is clearly present.
- Uncertainties: Cannot confirm exact page of "common fate" label due to OCR omissions; the principle is verifiable from the visible discussion of temporal grouping and the Metzger crossing-paths experiments.
- Cross-reference status: Verified against gestalt-theory-in-art existing card.
- Rosetta Stone check: Music and engineering mappings added as STRUCTURAL.
- OCR issues: Many lines in source file were omitted; synthesis based on visible sections and section headings.
