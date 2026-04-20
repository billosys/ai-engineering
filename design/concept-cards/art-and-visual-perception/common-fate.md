---
# === CORE IDENTIFICATION ===
concept: Common Fate
slug: common-fate

# === CLASSIFICATION ===
category: visual-perception
subcategory: gestalt grouping
tier: foundational
layer: 0-perception

# === PROVENANCE ===
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: art-and-visual-perception
authors: "Rudolf Arnheim"
chapter: "VIII. Movement"
chapter_number: 8
pdf_page: 395
section: "When Do We See Motion?"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - law of common fate
  - synchronous motion grouping
  - co-motion grouping

# === TYPED RELATIONSHIPS ===
prerequisites:
  - visual-perception
  - gestalt-theory-in-art
extends:
  - gestalt-theory-in-art
related:
  - phi-phenomenon
  - implied-motion
  - visual-rhythm
contrasts_with:
  - figure-ground

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the gestalt principles of perceptual grouping, and how does each one work?"
  - "How does the relationship between inter-group and intra-group spacing communicate which elements belong together (gestalt proximity)?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: music
    concept: "Voice leading — independent voices that move in parallel motion are perceived as grouped"
    rating: structural
    note: "In counterpoint, voices moving in the same direction at the same time (parallel motion) are perceptually fused into a single unit, structurally identical to how elements sharing a visual trajectory are grouped by common fate."
  - domain: engineering
    concept: "Pub/sub event synchronisation — components that respond to the same event are functionally grouped"
    rating: structural
    note: "Common fate in interaction design: UI elements that animate in synchrony in response to the same user trigger are perceptually grouped as a unit, mirroring pub/sub coupling."

css_implementation:
  - property: "animation"
    example: "animation: fadeIn 0.3s ease both; /* applied to multiple sibling elements simultaneously */"
    support: baseline
  - property: "transition"
    example: "transition: opacity 200ms, transform 200ms; /* same timing = common fate grouping */"
    support: baseline
---

# Quick Definition

Common fate is the gestalt grouping principle by which visual elements that move in the same direction at the same time are perceived as belonging together as a single group — even when static cues (proximity, similarity) would otherwise separate them.

# Core Definition

Common fate is one of the classical gestalt principles of perceptual grouping, stating that elements sharing the same direction and speed of motion are perceived as a unified group. Arnheim addresses this principle in the context of motion perception throughout Chapter VIII, particularly in discussing how gestalt grouping principles — which unite static elements — also operate in the temporal dimension to link elements across frames and movements. As Arnheim notes discussing stroboscopic motion: "the familiar principles of grouping also play their parts. An object in motion is the more likely to preserve its identity the less it changes in size, shape, brightness, color, or speed." When multiple objects share identical motion characteristics, common fate groups them into a perceptual unit that moves as one.

Common fate is the motion-domain instantiation of the broader gestalt insight that the visual system groups elements that are perceptually equivalent along any dimension — with motion being one of the most powerful such dimensions.

# Prerequisites

- **Gestalt Theory** — Common fate is one gestalt grouping principle among several (proximity, similarity, continuity, closure); understanding the overall gestalt framework is necessary to understand common fate's role.
- **Visual Perception** — Basic understanding of figure-ground and perceptual grouping as active, constructive processes.

# Key Properties

1. Operates in the temporal dimension: elements must share the same motion direction and speed at the same time.
2. Can override static grouping cues: elements that are spatially distant or dissimilar in appearance may still be grouped if they share the same motion.
3. Works both for literal physical motion (animation) and for implied synchronous motion in static images (e.g., a formation of birds whose silhouettes all point in the same direction).
4. Particularly strong when motion contrast is high: elements that move together in one direction while background elements remain stationary are strongly grouped.
5. Interacts with other grouping principles: common fate reinforces proximity and similarity grouping when these cues align with motion direction.

# Construction / Recognition

## To Construct/Create:
1. Animate multiple elements to move simultaneously with the same direction, speed, and easing — they will be perceived as a group.
2. In static compositions, align the directional axes of multiple forms to suggest they share a trajectory.
3. Use synchronised enter/exit animations to indicate that elements belong to the same logical group.
4. Exploit common fate to visually separate groups: animate group A leftward and group B rightward to emphasise their distinction.

## To Identify/Recognise:
1. In animated interfaces: elements that move in synchrony (same timing, same direction) are being grouped by common fate.
2. In static images: clusters of forms with aligned directional orientations imply common fate.
3. Check: if you isolate any one element from a moving group, does it still appear to belong to that group? If the motion is its only grouping cue, common fate is operative.

# Context & Application

- **Typical contexts**: UI animation, data visualisation, interactive choreography, iconography, layout design, dashboard animation, game UI.
- **Common applications**: Simultaneous entrance animations for card grids signal they are a set; list items that scroll together as a unit are perceived as belonging together; charts where multiple data series share coordinated highlight animations feel relationally linked.

## Cross-Domain Connections

**Music → STRUCTURAL**: In counterpoint, voices moving in parallel motion (same direction, same interval distance) fuse perceptually — listeners struggle to hear them as independent voices. This is the auditory analogue of visual common fate: synchronous parallel motion produces grouping regardless of other distinctions between the voices.

**Engineering → STRUCTURAL**: In UI event systems, components subscribed to the same event and triggering the same animation form a common-fate group from the user's perspective. Designing for common fate means coupling animation triggers intentionally to communicate which components belong to the same conceptual group.

# Examples

**Example 1** (p. 395, Stroboscopic Movement / grouping section): Arnheim discusses how gestalt grouping principles operate temporally as well as spatially — similarity of location, similarity of role in the whole, and similarity of trajectory all contribute to perceptual identity across time. When elements share these properties across motion, they group.

**Example 2** (p. 395, "The interaction of shape and motion," Metzger experiments): W. Metzger's experiments on crossing paths show that moving objects that share a consistent trajectory are more likely to be seen as a continuous unit than as two objects that exchange direction at an intersection — demonstrating that common fate (consistent trajectory) overrides positional cues.

# Relationships

## Builds Upon
- **Gestalt Theory** — Common fate is a direct extension of gestalt grouping into the temporal/motion domain.
- **Gestalt Similarity** — Common fate can be understood as "similarity of motion" — a temporal variant of the spatial similarity principle.

## Enables
- **Animation Choreography** — Common fate is the perceptual basis for coordinated UI animation: deliberate timing synchrony signals logical grouping.
- **Data Visualisation Coordination** — In animated charts, common fate allows the designer to group related data series through synchronised transitions.

## Related
- **Phi Phenomenon** — Phi phenomenon explains how discrete frames produce apparent continuous motion; common fate explains how multiple objects moving together are grouped as a unit.
- **Implied Motion** — A static composition can imply common fate when multiple forms share the same directional orientation.
- **Visual Rhythm** — Visual rhythm across static elements can be understood as spatial common fate: repeated directional accents create a sense of shared movement.

## Contrasts With
- **Figure-Ground** — Figure-ground separates objects from background based on static cues; common fate is a grouping principle that can override figure-ground separation when motion is shared.

# Common Errors

- **Error**: Assuming common fate only applies to elements moving in literally the same direction.
  **Correction**: Common fate also operates when elements share the same temporal pattern — elements that animate in and out at the same moment are grouped even if their individual motions differ.

- **Error**: Staggering all animations by default without considering common fate grouping.
  **Correction**: Stagger (sequential delay) breaks common fate grouping, causing elements to appear independent. Use synchronous timing to communicate group membership; use stagger to emphasise sequence or independence.

# Common Confusions

- **Confusion**: Common fate and proximity are the same principle in motion contexts.
  **Clarification**: Proximity groups elements based on spatial closeness; common fate groups them based on shared motion direction/timing. Elements can be spatially distant yet grouped by common fate (e.g., two distant elements that both flash at the same moment).

- **Confusion**: Common fate is only relevant in animated or video contexts.
  **Clarification**: While most powerful in animation, common fate also operates in static images through implied motion — forms with identical directional orientation imply they share a trajectory, producing weak common fate grouping.

# Source Reference

Chapter VIII: Movement, "Art and Visual Perception," pp. 395–434. Common fate is addressed as part of the gestalt grouping discussion in "When Do We See Motion?" and in the "Stroboscopic Movement" section.

# Verification Notes

- Definition source: Synthesised from gestalt grouping discussion in Chapter VIII; common fate as a named principle is part of the gestalt canon Arnheim invokes throughout the chapter, though he does not isolate it in a dedicated sub-section.
- Confidence rationale: Medium — the principle is implicit in Arnheim's discussion of grouping principles operating temporally, but the term "common fate" is not always used explicitly in the OCR-visible text; the concept is clearly present.
- Uncertainties: Cannot confirm exact page of "common fate" label due to OCR omissions; the principle is verifiable from the visible discussion of temporal grouping and the Metzger crossing-paths experiments.
- Cross-reference status: Verified against gestalt-theory-in-art existing card.
- Rosetta Stone check: Music and engineering mappings added as STRUCTURAL.
- OCR issues: Many lines in source file were omitted; synthesis based on visible sections and section headings.
