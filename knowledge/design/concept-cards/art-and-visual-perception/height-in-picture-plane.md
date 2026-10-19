---
concept: "Height in Picture Plane as Depth Cue"
slug: "height-in-picture-plane"
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
section: "Gradients Create Depth"
extraction_confidence: "medium"
aliases:
  - "vertical position in picture plane"
  - "height gradient"
  - "elevation depth cue"
  - "baseline convention"
prerequisites:
  - "pictorial-space"
extends: []
related:
  - "size-gradient"
  - "atmospheric-perspective"
  - "texture-gradient"
  - "linear-perspective"
contrasts_with: []
answers_questions: []
rosetta_stone:
  -
    domain: "engineering"
    concept: "Coordinate systems: screen y-axis vs. world y-axis"
    rating: "structural"
    note: "With screen y increasing downward, lower means larger y. Horizon/ground-plane assumptions can support distance inference; page position alone does not set hierarchy."
css_implementation:
  -
    property: "margin-top / top"
    example: "top: 20px; /* positioned geometry only; screen-down y increases downward */"
    support: "baseline"
---

# Quick Definition

Under a level ground-plane view, contacts of equally elevated objects below the horizon approach the horizon as distance increases. This conditional image-position cue does not rank ordinary page content.

# Core Definition

This presents the represented Arnheim account alongside current analytic qualifications. Original edition, pages, quotations, figures, experiments, physiology and historical claims remain unassessed; the technical constructions below do not certify source fidelity.

Arnheim discusses a height gradient alongside size in children’s baseline conventions and Seurat. The geometric reading requires camera/eye height and comparable scene elevations; arbitrary objects at different physical heights cannot be ordered from image y alone. For points above eye level, increasing distance approaches the horizon from above. That is a conditional geometric reversal, not a rule for every cloud or elevated structure.

Retained wording from the represented account (original fidelity unassessed):

"This device [size gradient], together with a height gradient that correlates depth with vertical distance from the base line of the picture, goes a long way toward satisfying spatial needs"

# Prerequisites

- **Pictorial Space** — Pictorial spatial readings supply the vocabulary for this particular cue or convention.

# Key Properties

1. Name the horizon, camera orientation and compared scene heights.
2. Below the horizon, comparable ground contacts can rise toward it with distance.
3. Above it, comparable elevated points can move downward toward the horizon.
4. In a screen-down coordinate convention, lower on screen means increasing y.
5. Information priority and reading order are separate from ground-plane inference.

# Construction / Recognition

## To Construct/Create:

1. Establish the intended ground plane and horizon.
2. Position comparable contacts under the selected projection.
3. Combine with size or overlap if useful rather than treating them as obligatory.

## To Identify/Recognise:

1. Find the horizon and identify comparable object contacts.
2. Check the scene-height assumptions.
3. Distinguish projected position from page hierarchy.

# Context & Application

Landscapes, bird’s-eye illustrations, Seurat’s figures and spatial maps provide examples. Flat UI layouts can place important information high or low according to task and reading conventions. A top heading is not thereby a distant object; this card does not answer the full hierarchy question.

## Cross-Domain Connections

**Engineering → STRUCTURAL**: With screen y increasing downward, lower means larger y. For a level pinhole camera at height h>0 above a ground plane, a ground point can have y_screen=y_horizon+fh/Z for Z>0; increasing Z approaches the horizon from below. This model does not apply to arbitrary page boxes or prescribe CSS top/bottom values.

# Examples

Source-specific examples and quotations below are retained as reports with their original wording and locators. They are not independently checked historical, experimental or universal claims. Applied examples are qualified design proposals.

**Example 1** (p. 564): "A height gradient that correlates depth with vertical distance from the base line of the picture, goes a long way toward satisfying spatial needs." — Arnheim

**Example 2** (children's art): In early children's drawings, a ground line (baseline) at the bottom of the picture and the sky at the top is the most elementary expression of height-in-plane depth convention. Objects rest on the baseline (closest) and recede upward.

**Example 3** (Seurat): In An Afternoon on the Grande Jatte, figures of decreasing size are distributed not just smaller but progressively higher in the picture plane, combining both depth cues systematically.

# Relationships

These are scoped reading connections. Builds Upon supports understanding; Enables names a possible downstream use; Related is an association; Contrasts With names a comparison. They do not establish universal causes, subtypes or verified historical sequences. Ordinary downstream uses are not invented card identities.

## Builds Upon

- **Pictorial Space** — Image-position changes can contribute depth under ground/horizon assumptions.

## Enables

- **Combined Depth Cue System** — Height can combine with size or overlap without being obligatory.

## Related

- **Size Gradient** — Comparable objects may approach the horizon while shrinking; arbitrary object heights defeat the simple inference.
- **Linear Perspective** — A level central projection explains the ground-contact formula under stated heights.
- **Atmospheric Perspective** — Haze can co-occur in landscapes without determining the position inference.

## Contrasts With

- No named contrast — No named typed contrast is recorded; height can still conflict with other scene cues.

# Common Errors

- **Error**: Using vertical page position to infer importance or physical distance universally.
  **Correction**: Check whether a ground-plane scene is actually depicted.

- **Error**: Demanding size variation whenever height is used.
  **Correction**: Additional cues can help, but adequacy depends on the content and task.

# Common Confusions

- **Confusion**: Higher on a page must mean either more important or farther away.
  **Clarification**: Information hierarchy and a conditional scene-projection cue have different premises.

# Source Reference

Chapter V: Space, "Art and Visual Perception," pp. 562–566 (Gradients Create Depth section).

# Verification Notes

The bullets below are preserved historical extraction assertions, not current verification. Frozen confidence, cross-reference, source-reading and OCR claims do not settle original-dependent fidelity. Current same-context review supports only the explicitly scoped technical constructions, contextual teaching and local comparisons; it establishes no browser, observer, comfort or physiological result.

- Definition source: Synthesised from discussion in Chapter V (Space), pp. 562–566
- Confidence rationale: Medium — Arnheim mentions height gradient as one component of the spatial system; no extended dedicated discussion
- Uncertainties: Limited direct quotation; synthesised from brief mentions alongside the more detailed size gradient discussion
- Cross-reference status: Verified
- Rosetta Stone check: Mapping added — coordinate system note is structural
- OCR issues: None significant
