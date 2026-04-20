---
# === CORE IDENTIFICATION ===
concept: Overlap as Depth Cue
slug: overlap-depth-cue

# === CLASSIFICATION ===
category: visual-perception
subcategory: depth-cues
tier: foundational
layer: 0-perception

# === PROVENANCE ===
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: art-and-visual-perception
authors: "Rudolf Arnheim"
chapter: "V. Space"
chapter_number: 5
pdf_page: 141
section: "Depth by Overlapping"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - occlusion
  - interposition
  - superposition
  - overlapping

# === TYPED RELATIONSHIPS ===
prerequisites:
  - figure-ground
  - pictorial-space
extends:
  - []
related:
  - depth-levels
  - transparency-perceptual
  - size-gradient
contrasts_with:
  - size-gradient
  - atmospheric-perspective

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the gestalt principles of perceptual grouping, and how does each one work?"
  - "What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "How do you systematically audit an existing interface for visual design quality? What checklist of principles and patterns do you evaluate, in what order?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: engineering
    concept: "z-index / CSS stacking context"
    rating: rigorous
    note: "Overlap is the perceptual mechanism that z-index exploits: the element with higher z-index visually occludes elements below, establishing the 'in front of' relationship."

css_implementation:
  - property: "z-index"
    example: "z-index: 2; /* overlaps z-index: 1 elements */"
    support: baseline
  - property: "position"
    example: "position: absolute; /* enables z-index-based overlap */"
    support: baseline
---

# Quick Definition

Overlap (occlusion) is a depth cue in which one object appears to lie in front of another because its contour interrupts and hides part of the second object. The interrupted object is perceived as complete and continuing behind the occluding one.

# Core Definition

Arnheim explains overlap as arising from the perceptual drive toward simplicity. When one shape interrupts the contour of another, the incomplete shape appears to continue behind the occluding element — because completing the shape produces a structurally simpler percept than accepting an irregular fragment. "When one of the components actually cuts off a part of the other, the perceptual urge to see a superposition becomes compelling because it serves to complete the incomplete shape" (p. 280).

The mechanism depends on the principle of good continuation and closure: the occluded shape is seen as the simplest complete form of which the visible fragment is a projection. The occluding element claims the shared boundary; the occluded element is left without a border at the intersection and is therefore seen as continuing behind.

Helmholtz's rule (cited by Arnheim): the object whose contour continues uninterrupted at the intersection is perceived as lying in front. This is a useful heuristic but the overall structural simplicity of the shapes determines the outcome.

# Prerequisites

- **Figure-Ground** — The occluding element acts as figure; the occluded element's ground-like continuation behind it is the mechanism of perceived depth.
- **Pictorial Space** — Overlap is one of the primary constructors of pictorial space.

# Key Properties

1. The occluding element claims the shared contour; the occluded element is borderless at the junction and is perceived as complete-but-hidden.
2. The depth cue derives from simplicity: the visual system chooses the interpretation (superposition) that yields the most regular, complete shapes.
3. Overlap is the simplest and most unambiguous depth cue — it works without size variation, perspective, or atmospheric effects.
4. It creates visual tension: the occluded shape "strives" to free itself from the interference with its completeness. This tension is a source of visual dynamics.
5. The perceptual effect of overlap can override actual physical depth: Kopfermann's experiment showed overlap perception dominating even when physical distances contradicted it.

# Construction / Recognition

## To Construct/Create:
1. Position element A so its boundary interrupts the contour of element B.
2. Ensure A's contour continues smoothly at the intersection (no break).
3. The element with the simpler, more complete shape will typically be perceived as in front.
4. Use overlap to sequence elements in depth without perspective: overlapping series (A over B over C) create a depth chain.

## To Identify/Recognise:
1. Find points where contours meet and one line stops while the other continues.
2. The element with the continuing contour is perceptually in front.
3. If both contours are interrupted at the junction (mutual overlap), ambiguity or tension results.

# Context & Application

- **Typical contexts**: UI layering (cards, modals, tooltips, floating elements), illustration, data visualisation (overlapping bars, scatter plots), poster design, icon design.
- **Common applications**: Drop shadows simulate overlap by implying that an element is above its background. Modal dialogs overlap the underlying content. Navigation menus overlap page content. In data viz, overlapping elements signal the same spatial region being claimed by multiple data points.

## Cross-Domain Connections

**Engineering → RIGOROUS**: CSS z-index and stacking contexts directly implement overlap. When two positioned elements occupy the same screen coordinates, the one with higher z-index occludes the other — precisely the perceptual mechanism Arnheim describes. Box-shadow is a visual cue that implies overlap (the casting element is above the receiving surface).

# Examples

**Example 1** (p. 280): "When one of the components actually cuts off a part of the other, the perceptual urge to see a superposition becomes compelling because it serves to complete the incomplete shape." — Arnheim

**Example 2** (p. 308): Arnheim cites the Greek sophist Philostratus describing a painting in which soldiers are depicted successively more occluded — "some are seen in full figure, others with the legs hidden, others from the waist up" — as a spatial ordering device.

**Example 3** (p. 316): Kopfermann's experiment: a larger triangle seen overlapping a smaller one in a composite view even when physically the smaller is in front, demonstrating that overlap perception can override physical reality.

**Example 4** (UI): A floating action button in a mobile app overlaps the list below it. The overlap tells users the FAB is a separate, elevated interactive layer.

# Relationships

## Builds Upon
- **Figure-Ground** — Overlap depends on the ability of one surface to claim a contour while another is left borderless.
- **Simplicity Principle (Gestalt)** — The visual system chooses the simplest interpretation: complete shapes in superposition over irregular fragments in the same plane.

## Enables
- **Depth Levels** — Overlap is the primary mechanism for creating chains of depth levels.
- **Perceptual Transparency** — A special case of overlap where the occluded surface remains visible through the occluding one.
- **Visual Tension** — The striving of the occluded shape for completeness generates perceptual dynamics.

## Related
- **Size Gradient** — Often accompanies overlap to reinforce spatial ordering.
- **Depth Levels** — Overlap is how multiple depth levels are constructed.

## Contrasts With
- **Size Gradient** — Size gradient works through scaling, overlap works through interruption; they are independent depth cues that typically reinforce each other.
- **Atmospheric Perspective** — Works through degradation of clarity, not occlusion.

# Common Errors

- **Error**: Assuming that the physically closer element will always appear in front visually.
  **Correction**: Perceptual overlap is determined by contour continuity and shape simplicity, not physical distance. Arnheim's Kopfermann example shows physical distance can be overruled.

- **Error**: Ignoring the visual tension generated by overlap when designing layouts.
  **Correction**: Overlapping elements create dynamic tension. When tension is undesirable (calm layouts, data tables), avoid overlap. When energy and depth are desired, use overlap deliberately.

# Common Confusions

- **Confusion**: Overlap and z-index are the same concept.
  **Clarification**: z-index controls rendering order but does not by itself create the perceptual depth cue. The visual experience of depth from overlap requires the occluding element to visibly interrupt the contour of the occluded one.

- **Confusion**: Any element placed on top of another creates overlap depth.
  **Clarification**: Only when the top element visibly interrupts the contour of the bottom element does the depth cue operate. If both elements are fully visible with no boundary interruption (e.g., a transparent overlay), other depth cues (transparency, shadow) must carry the depth information.

# Source Reference

Chapter V: Space, "Art and Visual Perception," pp. 278–316 (Depth by Overlapping section).

# Verification Notes

- Definition source: Synthesised from Arnheim's detailed discussion of overlap, pp. 278–316; Helmholtz rule quoted directly
- Confidence rationale: Arnheim's treatment is precise and extensively illustrated with figures and experiments
- Uncertainties: None significant
- Cross-reference status: Verified
- Rosetta Stone check: Mapping added — z-index/stacking context is a rigorous engineering implementation
- OCR issues: Some figure numbers have OCR artifacts; no impact on conceptual content
