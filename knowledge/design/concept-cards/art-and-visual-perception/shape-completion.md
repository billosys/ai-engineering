---
concept: "Shape Completion"
slug: "shape-completion"
category: "visual-perception"
subcategory: "gestalt laws"
tier: "intermediate"
layer: "0-perception"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "II. Shape"
chapter_number: 2
pdf_page: 31
section: "A Whole Maintains Itself"
extraction_confidence: "high"
aliases:
  - "perceptual closure"
  - "gestalt closure"
  - "perceptual completion"
  - "amodal completion"
prerequisites:
  - "praegnanz"
  - "visual-shape"
extends: []
related:
  - "structural-skeleton"
  - "visual-simplicity"
  - "visual-subdivision"
contrasts_with:
  - "visual-subdivision"
answers_questions:
  - "What are the gestalt principles of perceptual grouping, and how does each one work?"
  - "How does cognitive load theory (intrinsic, extraneous, germane) relate to progressive disclosure and visual hierarchy? When is simplification harmful?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Completion in metric spaces / Cauchy sequence completion"
    rating: "loose"
    note: "Metric completion adjoins limits for Cauchy sequences in a specified metric construction. Perceptual completion supplies a possible continuation from partial cues; it need not be unique, exact, or the reconstruction of the original object."
  -
    domain: "engineering"
    concept: "Error correction / forward error correction (FEC)"
    rating: "structural"
    note: "FEC can recover data using a specified code and redundancy within channel and recovery assumptions. Partial visual cues likewise constrain possibilities, but sight supplies no error-correcting code or guarantee of exact reconstruction."
css_implementation:
  -
    property: "clip-path crops painted shape; overflow cannot undo the clip"
    example: ".circle { width: 6rem; height: 6rem; border-radius: 50%; clip-path: inset(0 35% 0 0); } /* Complete circle geometry remains; right-hand paint is hidden. No essential meaning may rely on inferred continuation. */"
    support: "partial"
  -
    property: "Equal dimensions with border-radius for a circle"
    example: ".circle { width: 6rem; height: 6rem; border-radius: 50%; } /* Author size; equal dimensions make a circle. A crop may suggest continuation, not guarantee it. */"
    support: "baseline"
---

# Quick Definition

Shape completion is the tendency to experience a partial or occluded shape as continuing into a fuller form. Visible cues and context constrain the reading; neither a unique hidden geometry nor reliable recovery of essential meaning is guaranteed.

# Core Definition

This section presents the represented Arnheim account. Its quotations, page references and historical or experimental reports have not been checked against the unavailable original; current analytic qualifications below do not certify that fidelity.

Arnheim reports clinical observations of shape completion: patients with hemianopia (brain damage causing blindness in half the visual field) who are shown half a circle "report seeing a complete circle. On being shown a smaller portion of the circle he will report seeing 'a kind of bow,' and the same is true for half an ellipse. The patient is not merely guessing by inference from past experience, but actually sees either the complete or the incomplete figure" (Chapter II, p. 51). Even afterimages of completed figures are perceived as complete. His proposed neural-field explanation, not established by this current review, is: "when enough of the projected figure is received by the visual cortex, the electrochemical process caused by the projection can complete itself in the brain and thereupon produces the percept of a complete whole in consciousness" (p. 51). Arnheim relates completion to simplicity; the represented cases do not establish a universal ordering of all regular and irregular forms. "An extensive injury... may black out either the right or left half of the visual field completely... if the patient is made to fixate the center of a circle for one tenth of a second... he reports seeing a complete circle" (p. 51).

# Prerequisites

- **Praegnanz** — Shape completion is Praegnanz applied to incomplete stimuli: the brain completes toward the simplest available closed whole.
- **Visual Shape** — Understanding what constitutes a shape (structural skeleton, not merely boundary) is prerequisite to understanding what "completion" means perceptually.

# Key Properties

1. **Shape-dependent** — Simple regular cues may support completion, while irregularity and competing context can weaken it. The quoted case below does not establish a universal boundary: "The patient is also unlikely to see the well-known number 4 in Figure 24 spontaneously" (in a complex camouflage context).
2. **Visible extent** — The reported circle/bow contrast suggests a changed reading, but supplies no universal proportion or sharp threshold for all shapes and observers.
3. **Reported mechanism** — Arnheim proposes electrochemical cortical completion. The represented reports do not independently prove that mechanism or exclude inference and prior experience.
4. **Completion distinctions** — An occluded object may be experienced as continuing without its hidden surface being visibly painted. Distinguish that amodal continuation from visible contour closure and the reported clinical/afterimage phenomena.
5. **Context-dependent** — The same partial shape may complete in one context and fail to complete in another if the context introduces conflicting structural forces.

# Construction / Recognition

## To Construct/Create:
1. Retain distinctive cues to the intended form; there is no general more-than-half/less-than-half visibility rule.
2. Ensure the visible portion has consistent curvature/direction that implies a simple completion.
3. Use a clean context (ground without competing shapes) so the completion is not disrupted by conflicting edges.
4. Make essential meaning available without inferred continuation. A clipped form may suggest more content, but provide explicit usable navigation or labels where required.

## To Identify/Recognise:
1. Compare whether the visible cues suggest the intended fuller shape in the actual context; a legible skeleton alone is not sufficient proof.
2. Is the visible arc/portion consistent with a single simple closed form? (Circle, ellipse, rectangle, regular curve)
3. Is there competing visual context that would disrupt the completion?

# Context & Application

- **Typical contexts**: Partially-revealed interface elements, off-screen content indicators, logo design with negative space, responsive design where elements are partially clipped, image carousels where adjacent cards are partially visible.
- **Common applications**: A carousel edge can suggest another card, and a clipped circular avatar can suggest continuation. The viewer may instead see a partial form; neither hidden content nor full-circle recognition is guaranteed. A crop can suggest off-screen continuation, with explicit navigation and essential meaning available independently. In the header example a 6rem by 6rem box with 50% radii defines complete circle geometry, while inset(0 35% 0 0) hides part of its paint. overflow: visible cannot cancel that clip; the remaining paint is not itself a complete visible circle.

## Cross-Domain Connections

**Engineering → STRUCTURAL**: FEC recovers data using a specified code and redundancy under channel and recovery assumptions. Partial visual cues constrain possible continuations, but are not a code or guarantee of the original hidden form. The shared structure is reasoning with incomplete input, not exact reconstruction by sight.

# Examples

**Example 1** (p. 51): Hemianopia patients shown half a circle "report seeing a complete circle" — a reported clinical observation, not an independently verified demonstration of a particular cortical mechanism.

**Example 2** (p. 51): When shown a "smaller portion of the circle he will report seeing 'a kind of bow'" — a reported change of experience; it does not specify a universal geometric threshold.

**Example 3** (p. 51): "Even the afterimages of completed figures are perceived as complete" — a reported afterimage observation, insufficient here to confirm cortical rather than retinal causation.

**Example 4** (p. 48–50): Distorting goggles (Ivo Kohler's experiments): the visual system gradually re-establishes stable simplicity even with prismatically distorted input — related tendency of the whole to maintain itself.

# Relationships

The following are scoped conceptual reading connections. In the represented account, simplicity, axes and grouping explain one another; these links do not establish causal neural mechanisms. Unnamed downstream uses and ordinary comparisons are not automatically resolved card identities.

## Builds Upon
- **Praegnanz** — Completion is Praegnanz driving partial shapes toward their simplest complete form.
- **Visual Shape** — Understanding visible form helps describe a proposed completion, without a necessary-and-sufficient skeleton test.

## Enables
- (No named direct downstream relation recorded within Chapter II; this does not exclude generative use in cropped compositions.)

## Related
- **Structural Skeleton** — Completion operates by extending the structural skeleton of the visible portion; a clear skeleton facilitates completion.
- **Visual Simplicity** — Regular visible cues may support completion in this account; a universal reliability ordering is not established.
- **Visual Subdivision** — Completion works against subdivision: where subdivision tries to separate a field into distinct units, completion tries to unify partial shapes into wholes.

## Contrasts With
- **Visual Subdivision** — Subdivision breaks the field into separate units; completion resists this by unifying partial forms. Both are applications of Praegnanz in opposing directions.

# Common Errors

- **Error**: Assuming viewers will complete any partial shape.
  **Correction**: Simple regular cues may help, but completion is not guaranteed for simple forms or excluded for complex ones. Compare the actual crop and context and preserve essential meaning independently.

- **Error**: Relying on completion to save poorly designed partial reveals.
  **Correction**: Distinctive contour and axis cues can aid completion, without a necessary-and-sufficient skeleton test. A crop through discriminating features can make a logo or icon ambiguous; inspect what remains rather than assuming one inevitable reading.

# Common Confusions

- **Confusion**: Shape completion is the same as the gestalt law of closure.
  **Clarification**: Closure (closing open outlines into bounded regions) is related but distinct. Shape completion in Arnheim's sense specifically concerns the perceptual filling-in of physically absent shape portions — amodal completion. Closure concerns the tendency to perceive open outlines as closed. Both are driven by Praegnanz.

- **Confusion**: Completion is an intellectual inference from past experience.
  **Clarification**: Arnheim explicitly distinguishes completion from inference: the hemianopia patient "is not merely guessing by inference from past experience, but actually sees" the complete figure. This preserves Arnheim's distinction between seeing and guessing; it does not independently establish a cortical field mechanism or rule out learned expectations.

# Source Reference

Chapter II: Shape, "Art and Visual Perception," pp. 50–52. Section: "A Whole Maintains Itself."

# Verification Notes

The bullets below preserve historical extraction assertions, including their confidence, cross-reference, OCR and source-reading claims; they are not current verification. The represented original edition/page basis is unavailable, so fidelity of all quotations, locators, figures, experiments and historical claims remains unassessed. Current technical corrections and scoped analogies do not establish a neural mechanism, cultural universality or measured usability.

- Definition source: Direct quotes from pp. 51–52; neurological evidence from hemianopia studies cited explicitly by Arnheim.
- Confidence rationale: High — Arnheim provides experimental evidence and explicit mechanistic explanation for shape completion.
- Uncertainties: The exact thresholds for completion (how much of a shape must be visible) are described qualitatively (circle completes, "smaller portion" gives a bow) rather than quantitatively.
- Cross-reference status: Verified — connects to praegnanz, visual-shape, structural-skeleton.
- Rosetta Stone check: Mappings added (mathematics/completion loose; engineering/FEC structural).
- OCR issues: None relevant to this section.
