---
concept: "Visible Motor Forces"
slug: "visible-motor-forces"
category: "visual-perception"
subcategory: "motion perception"
tier: "intermediate"
layer: "0-perception"
source: "Art and Visual Perception: A Psychology of the Creative Eye"
source_slug: "art-and-visual-perception"
authors: "Rudolf Arnheim"
chapter: "VIII. Movement"
chapter_number: 8
pdf_page: 395
section: "Visible Motor Forces"
extraction_confidence: "medium"
aliases:
  - "perceptual causality"
  - "perceived causality"
  - "motor force perception"
prerequisites:
  - "visual-perception"
  - "implied-motion"
extends:
  - "implied-motion"
related:
  - "phi-phenomenon"
  - "stroboscopic-motion"
  - "physiognomic-perception"
  - "arnheim-expression-theory"
contrasts_with: []
answers_questions:
  - "How do you design the states of an interactive component (default, hover, active, focus, disabled, loading, error)? What visual properties change for each state, and why?"
rosetta_stone:
  -
    domain: "engineering"
    concept: "Physics-based animation parameters and candidate causal cues"
    rating: "structural"
    note: "Mass/damping/spring computations determine a simulation trajectory, not an exact perceived force or guaranteed naturalness; actual observer/task response is separate."
  -
    domain: "engineering"
    concept: "Direct manipulation / implemented input and visible response"
    rating: "structural"
    note: "Drag/pinch/scroll can support a perceived connection, but software response, physical force, latency and experienced causation remain distinct and need actual checks."
css_implementation:
  -
    property: "transition"
    example: "transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1); /* candidate overshoot, not a mass/damping model */"
    support: "baseline"
  -
    property: "animation"
    example: "@keyframes bounce { 0% { transform: translateY(0); } 60% { transform: translateY(-20px); } 80% { transform: translateY(-10px); } 100% { transform: translateY(0); } }"
    support: "baseline"
---

# Quick Definition

Visible motor forces name experienced causation and dynamic character in moving visual events. Arnheim treats these as direct perceptual qualities; perceived causation is distinct from actual physical force and simulation accuracy.

# Core Definition

This presents the represented Arnheim account. Original edition/context, quotation fidelity, page bases, historical reports, experiments and physiology remain unassessed because the required original is unavailable. The current analytic corrections do not certify that fidelity.

This is the represented Arnheim account of perceived impacts, impulses and causal relations. Directness is its theoretical claim, not proof that learning, inference or observer context never contribute.

Arnheim opens the section by distinguishing geometric from dynamic accounts of motion: "Geometrically, locomotion can be defined as a mere change of location, but for the naive observer, just as for the physicist, displacements are dynamic. The behavior of forces is always the more important part of the story. Artistically it is these forces that give an event visual expression and endow it with life."

The represented Michotte experiments describe a moving square reaching another and the second moving as if launched. The impression can persist despite physically absurd conditions, such as a wooden ball and projected light disk. Arnheim’s reported conclusion is: "Michotte demonstrates that causality is as much an aspect of the percept itself as the shape, color, and movement of the objects." The original experiment’s stimuli, timing and results remain unchecked here; no universal causal gate follows.

The represented organic/inorganic distinction compares apparent self-initiation with external displacement. These can be expressive interpretations of specific sequences; self-motion is not proof of life and externally caused motion need not look mechanical to every viewer.

# Prerequisites

- **Implied Motion** — Supplies a comparison with static directional qualities; temporal perceived causation is an elaboration, not literal subtyping of a still-image event.
- **Visual Perception** — The general framework of perceptual qualities as direct and immediate.

# Key Properties

1. Arnheim presents causal impression as part of the percept; the present review does not establish an exhaustive perceptual mechanism.
2. The represented absurd-condition examples distinguish experienced cause from knowledge of physical possibility.
3. Apparent self-initiation and external displacement can contribute to organic/mechanical readings in context.
4. A gentle/violent/hesitant character is an interpretation, not identical to numeric force magnitude.
5. The represented performance claim, "what counts for artistic performance is the dynamics conveyed to the audience visually; for dynamics alone is responsible for expression and meaning," is an artistic position, not exclusion of content or other modalities in every task.

# Construction / Recognition

## To Construct/Create:
1. To convey causality: ensure the timing and spatial relationship between interacting objects matches the structural pattern of the causal relationship (contact → response, with appropriate delay and response magnitude).
2. Compare anticipation and direction changes if proposing self-initiated character; neither guarantees an organic interpretation.
3. Use overshoot, rebound or decay as candidate cues; simulation mass/damping do not map exactly to perceived force.
4. For UI, keep input/response behavior identifiable and timely for the task. Active feedback can use direction or displacement, while labels, role/name/state and rest/reduced-motion meaning remain available.

## To Identify/Recognise:
1. Ask: does the motion appear to be caused by forces internal or external to the moving object?
2. Check: does the relationship between interacting elements convey causality directly (one thing appears to push, attract, or restrain another)?
3. Identify: what is the perceived magnitude and character of the force (gentle, violent, hesitant, decisive)?
4. Test: does removing the causal relationship (replacing it with simultaneous but disconnected movement) eliminate the force perception?

# Context & Application

- **Typical contexts**: Physics-based animation, direct manipulation interfaces, game UI, loading animations, micro-interactions, motion design for feedback states.
- **Common applications**: Candidate spring/rebound, inertial scrolling, drag resistance, elastic overscroll and button-depression metaphors relate input to visible behavior. Content receives computed displacement, not literal momentum transmitted by the thumb.

## Cross-Domain Connections

**Engineering → STRUCTURAL**: A spring simulation computes values from mass, damping and other parameters. Those outputs may suggest a force, but numeric fidelity supplies no one-to-one match to perceived causation or naturalness. A drawn rebound can differ from an accurate physical model and still fit the intended task.

**Engineering → STRUCTURAL**: Dragging, pinching and inertial scrolling connect input with visible response. Implemented behavior, response latency and perceived connection need their actual checks; the metaphor does not turn a gesture into a literal force on screen content.

# Examples

These preserve the represented account’s examples and artistic judgments. Their original context and reported results remain unassessed; they are not universal laws or fresh observer measurements.

**Example 1** (p. 395, Visible Motor Forces — Michotte): "Michotte demonstrates that causality is as much an aspect of the percept itself as the shape, color, and movement of the objects. Whether and to what extent causality is seen depends exclusively upon the perceptual conditions. Strong causality results even in situations where practical experience must call it absurd."

**Example 2** (p. 395, Visible Motor Forces — organic/inorganic distinction): The represented moving-bar comparison contrasts rigid translation with a bar appearing to "step" as if walking. Mechanical/alive are reported readings of that display, not a biological classification or universal structural guarantee.

**Example 3** (p. 395, Visible Motor Forces — camera motion): Arnheim notes that camera movements fulfil their function "only when they convey expressive impulses and responses rather than merely the mechanical effect of physical action." The camera's motion must be perceived as caused by and expressing the dynamics of the filmed event, not as arbitrary mechanical displacement.

# Relationships

## Builds Upon
- **Implied Motion** — Compares still directional character with temporal causal impression; neither is a literal subtype of the other.
- **Gestalt Theory** — The represented direct-perception position relates to whole-configuration organization, without proving a particular neural mechanism.

## Enables
- **Physics-Based Animation Design** — Simulations supply trajectories that can be evaluated as candidate visual cues; computational parameters are not perceptual measurements.
- **Direct Manipulation Design** — A useful input/response connection can support interaction; actual behavior and perceived causation are separate checks.

## Related
- **Stroboscopic Motion** — Stroboscopic motion provides the frames; visible motor forces are the perceived dynamics within those frames.
- **Physiognomic Perception** — Dynamic character offers a comparison with expressive seeing, not a demonstrated common mechanism.

## Contrasts With
- **Mere Locomotion** — Arnheim distinguishes mere displacement (change of position without perceived force) from visible motor forces (motion as experienced by the naive observer, saturated with dynamic quality). "Movement looks dead when it gives the impression of mere displacement."

# Common Errors

- **Error**: Assuming that physically accurate simulation always produces the most perceptually natural animation.
  **Correction**: Arnheim's framework (and Michotte's evidence) shows that perceptual causality depends on structural pattern, not physical accuracy. Cartoon physics (exaggerated anticipation, overshoot, squash-and-stretch) often produces more compelling visible motor forces than physically accurate but perceptually ambiguous simulations.

- **Error**: Treating animation response latency as a purely technical issue.
  **Correction**: Input-to-response delay can affect the interaction, but no universal approximately 100ms preservation/breaking gate is established. Distinguish input processing, frame production and presentation, and inspect the actual task/device/observer conditions.

# Common Confusions

- **Confusion**: Visible motor forces require the objects to actually collide or touch.
  **Clarification**: The represented experiments distinguish physical contact from perceived causal relations. Timing, separation and display conditions must be stated; force at a distance is not guaranteed by any one pattern.

- **Confusion**: Visible motor forces are only relevant for realistic/physical animation styles.
  **Clarification**: Abstract or minimal animation can invite dynamic readings. A modal that "snaps" or "floats" may suggest different character in context; not every animation establishes a perceived force.

# Source Reference

Chapter VIII: Movement, "Art and Visual Perception," pp. 395–434. See especially the "Visible Motor Forces" section (section heading at line 204 of source file).

# Verification Notes

The reported square that "launches" or "pushes" another concerns experienced cause, not literal contact force. The statement "what counts for artistic performance is the dynamics conveyed to the audience visually; for dynamics alone is responsible for expression and meaning." is an artistic position. A simulation that "feels right" still needs actual task/observer evidence.

- Current review boundary: the legacy extraction notes below are preserved provenance, not this review’s original-source verification. Current technical/interpretive qualifications above and local relationship/CQ checks do not establish historical fidelity or measured observer behavior.

- Definition source: Synthesised from "Visible Motor Forces" section; Michotte's experiments are discussed explicitly; the distinction between dynamic and geometric accounts of motion is stated at the section's opening.
- Confidence rationale: Medium — the section is clearly identified and the core claims visible; some detail was in OCR-omitted lines.
- Uncertainties: The specific Michotte experiments described (which squares, which conditions) were partially in omitted lines; the key claims (causality is perceived, not inferred; paradoxical causality still perceived) were in visible text.
- Cross-reference status: Verified connections to implied-motion and physiognomic-perception.
- Rosetta Stone check: Engineering mappings (physics-based animation, direct manipulation) added as RIGOROUS and STRUCTURAL respectively.
- OCR issues: Some lines in "Visible Motor Forces" section were omitted; synthesis from visible text and section structure.
