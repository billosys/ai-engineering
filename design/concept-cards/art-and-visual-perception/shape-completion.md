---
# === CORE IDENTIFICATION ===
concept: Shape Completion
slug: shape-completion

# === CLASSIFICATION ===
category: visual-perception
subcategory: gestalt laws
tier: intermediate
layer: 0-perception

# === PROVENANCE ===
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: art-and-visual-perception
authors: "Rudolf Arnheim"
chapter: "II. Shape"
chapter_number: 2
pdf_page: 31
section: "A Whole Maintains Itself"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - perceptual closure
  - gestalt closure
  - perceptual completion
  - amodal completion

# === TYPED RELATIONSHIPS ===
prerequisites:
  - praegnanz
  - visual-shape
extends:
  []
related:
  - structural-skeleton
  - visual-simplicity
  - visual-subdivision
contrasts_with:
  - visual-subdivision

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the gestalt principles of perceptual grouping, and how does each one work?"
  - "How does cognitive load theory (intrinsic, extraneous, germane) relate to progressive disclosure and visual hierarchy? When is simplification harmful?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone:
  - domain: mathematics
    concept: "Completion in metric spaces / Cauchy sequence completion"
    rating: loose
    note: "Mathematical completion fills in missing elements to make an incomplete structure whole; perceptual completion analogously 'fills in' missing shape segments to produce a complete, stable whole — the analogy is loose because mathematical completion is exact, perceptual completion is probabilistic."
  - domain: engineering
    concept: "Error correction / forward error correction (FEC)"
    rating: structural
    note: "The perceptual system reconstructs complete shapes from partial input just as forward error correction reconstructs the original signal from a corrupted or incomplete transmission — both use redundancy and structural expectations to fill gaps."

css_implementation:
  - property: "clip-path with overflow: visible (implying continuation outside bounds)"
    example: "clip-path: inset(0); overflow: visible; /* element continues visually beyond visible area, implying completion */"
    support: partial
  - property: "border-radius on partially visible elements"
    example: "/* A circle partially behind a container edge is perceived as continuing as a circle */ .circle { border-radius: 50%; }"
    support: baseline
---

# Quick Definition

Shape completion is the perceptual tendency to experience partial or fragmented shapes as complete wholes, driven by the brain's field processes seeking the simplest available closed structure.

# Core Definition

Arnheim provides direct neurological evidence for shape completion: patients with hemianopia (brain damage causing blindness in half the visual field) who are shown half a circle "report seeing a complete circle. On being shown a smaller portion of the circle he will report seeing 'a kind of bow,' and the same is true for half an ellipse. The patient is not merely guessing by inference from past experience, but actually sees either the complete or the incomplete figure" (Chapter II, p. 51). Even afterimages of completed figures are perceived as complete. Arnheim's explanation: "when enough of the projected figure is received by the visual cortex, the electrochemical process caused by the projection can complete itself in the brain and thereupon produces the percept of a complete whole in consciousness" (p. 51). The degree of completion depends on simplicity: simple shapes (circles, squares) complete more readily than complex irregular ones. "An extensive injury... may black out either the right or left half of the visual field completely... if the patient is made to fixate the center of a circle for one tenth of a second... he reports seeing a complete circle" (p. 51).

# Prerequisites

- **Praegnanz** — Shape completion is Praegnanz applied to incomplete stimuli: the brain completes toward the simplest available closed whole.
- **Visual Shape** — Understanding what constitutes a shape (structural skeleton, not merely boundary) is prerequisite to understanding what "completion" means perceptually.

# Key Properties

1. **Simplicity-dependent** — Simple shapes (circles, ellipses, squares) complete readily; complex or irregular shapes do not. "The patient is also unlikely to see the well-known number 4 in Figure 24 spontaneously" (in a complex camouflage context).
2. **Threshold effect** — Below a critical proportion of the shape visible, completion fails and partial form is seen instead (arc, bow, etc.) — not a gradual fade but a perceptual threshold.
3. **Neurologically grounded** — Completion is not intellectual inference from experience but an electrochemical field process in the visual cortex.
4. **Amodal** — The completed portion of the shape is perceived even though it does not stimulate any retinal receptors (amodal completion).
5. **Context-dependent** — The same partial shape may complete in one context and fail to complete in another if the context introduces conflicting structural forces.

# Construction / Recognition

## To Construct/Create:
1. Show enough of the shape that the structural skeleton is legible (typically more than half for complex shapes, less for simple ones).
2. Ensure the visible portion has consistent curvature/direction that implies a simple completion.
3. Use a clean context (ground without competing shapes) so the completion is not disrupted by conflicting edges.
4. Trust the viewer to complete simple geometric shapes when partially revealed — this is reliable.

## To Identify/Recognise:
1. Does the partial shape have a clear, simple structural skeleton? If yes, completion will occur.
2. Is the visible arc/portion consistent with a single simple closed form? (Circle, ellipse, rectangle, regular curve)
3. Is there competing visual context that would disrupt the completion?

# Context & Application

- **Typical contexts**: Partially-revealed interface elements, off-screen content indicators, logo design with negative space, responsive design where elements are partially clipped, image carousels where adjacent cards are partially visible.
- **Common applications**: A carousel component that partially reveals the edge of the next card relies on shape completion — the viewer perceives the full card as continuing beyond the visible area. A circle-shaped avatar clipped at the bottom of a screen is perceived as a circle, not a semicircle. Designers can exploit shape completion to imply off-screen content without showing it.

## Cross-Domain Connections

**Engineering → STRUCTURAL**: Forward error correction (FEC) in data transmission reconstructs a complete message from a partial, corrupted, or noisy input using structural redundancy and prediction. Shape completion does the same: the visual system uses the visible portion's structural properties to reconstruct the complete form, treating the missing portion as "noise" or "occlusion."

# Examples

**Example 1** (p. 51): Hemianopia patients shown half a circle "report seeing a complete circle" — neurological evidence that completion is a cortical field process, not intellectual inference.

**Example 2** (p. 51): When shown a "smaller portion of the circle he will report seeing 'a kind of bow'" — demonstrating the threshold: below sufficient visible extent, completion fails and partial form is seen.

**Example 3** (p. 51): "Even the afterimages of completed figures are perceived as complete" — the completion persists in the afterimage, confirming it is a cortical (not retinal) process.

**Example 4** (p. 48–50): Distorting goggles (Ivo Kohler's experiments): the visual system gradually re-establishes stable simplicity even with prismatically distorted input — related tendency of the whole to maintain itself.

# Relationships

## Builds Upon
- **Praegnanz** — Completion is Praegnanz driving partial shapes toward their simplest complete form.
- **Visual Shape** — The shape that gets completed must have a legible structural skeleton.

## Enables
- (No direct downstream concepts within Chapter II — this is a mid-level principle)

## Related
- **Structural Skeleton** — Completion operates by extending the structural skeleton of the visible portion; a clear skeleton facilitates completion.
- **Visual Simplicity** — Simpler shapes complete more readily and more reliably.
- **Visual Subdivision** — Completion works against subdivision: where subdivision tries to separate a field into distinct units, completion tries to unify partial shapes into wholes.

## Contrasts With
- **Visual Subdivision** — Subdivision breaks the field into separate units; completion resists this by unifying partial forms. Both are applications of Praegnanz in opposing directions.

# Common Errors

- **Error**: Assuming viewers will complete any partial shape.
  **Correction**: Completion is reliable only for simple shapes with clear structural skeletons. Complex or irregular partial shapes do not complete — they are seen as partial or fragmentary.

- **Error**: Relying on completion to save poorly designed partial reveals.
  **Correction**: Completion requires the visible portion to contain a legible skeleton. A poorly cropped logo or icon (where the crop cuts through structurally important features) will not complete — it will look broken.

# Common Confusions

- **Confusion**: Shape completion is the same as the gestalt law of closure.
  **Clarification**: Closure (closing open outlines into bounded regions) is related but distinct. Shape completion in Arnheim's sense specifically concerns the perceptual filling-in of physically absent shape portions — amodal completion. Closure concerns the tendency to perceive open outlines as closed. Both are driven by Praegnanz.

- **Confusion**: Completion is an intellectual inference from past experience.
  **Clarification**: Arnheim explicitly distinguishes completion from inference: the hemianopia patient "is not merely guessing by inference from past experience, but actually sees" the complete figure. Completion is a cortical field process, not a cognitive deduction.

# Source Reference

Chapter II: Shape, "Art and Visual Perception," pp. 50–52. Section: "A Whole Maintains Itself."

# Verification Notes

- Definition source: Direct quotes from pp. 51–52; neurological evidence from hemianopia studies cited explicitly by Arnheim.
- Confidence rationale: High — Arnheim provides experimental evidence and explicit mechanistic explanation for shape completion.
- Uncertainties: The exact thresholds for completion (how much of a shape must be visible) are described qualitatively (circle completes, "smaller portion" gives a bow) rather than quantitatively.
- Cross-reference status: Verified — connects to praegnanz, visual-shape, structural-skeleton.
- Rosetta Stone check: Mappings added (mathematics/completion loose; engineering/FEC structural).
- OCR issues: None relevant to this section.
