---
concept: "Colour Picker Design Principles"
slug: "colour-picker-design-principles"
category: "interaction-design"
subcategory: "colour-controls"
tier: "intermediate"
layer: "2-domain"
source: "Okhsv and Okhsl"
source_slug: "posts"
authors: "Björn Ottosson"
chapter: "What makes a good color picker?"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "high"
aliases:
  -
    - "colour space design goals"
    - "picker design criteria"
prerequisites:
  - "colour-picker"
  - "colour-gamut"
  - "hsl"
  - "hsv"
extends:
  - "colour-picker"
related:
  - "okhsl"
  - "okhsv"
  - "orthogonal-colour-properties"
contrasts_with: []
answers_questions:
  - "What makes a colour picker perceptually well-designed?"
rosetta_stone: []
css_implementation: []
---

# Quick Definition

A formal set of eight properties proposed by Ottosson for evaluating how well a colour space serves as the basis for a colour picker, covering perceptual independence of axes, geometric simplicity, and uniformity of change.

# Core Definition

Ottosson proposes the following properties as the framework for evaluating colour spaces designed for colour picking:

- **Orthogonal Lightness** — Hue/Chroma/Saturation can be altered, while keeping perceived Lightness constant
- **Orthogonal Chroma** — Lightness/Hue can be altered, while keeping perceived Chroma constant
- **Orthogonal Saturation** — Lightness/Hue can be altered, while keeping perceived Saturation constant
- **Orthogonal Hue** — Lightness/Chroma/Saturation can be altered, while keeping perceived Hue constant
- **Simple Geometrical Shape** — Fit the target gamut into a cylinder or other simple shape, so that parameters can be altered independently without resulting in colors outside the target gamut
- **Max Chroma at Edge** — Make it easy to find the strongest color of a given hue, by placing the strongest color on edge of the color volume
- **Varies Smoothly** — Vary smoothly with each parameter; no discontinuous or abrupt changes
- **Varies Evenly** — The perceived magnitude of the change in color caused by changing a parameter should be uniform for all values of the parameter

Critically, Ottosson notes: "These properties are in conflict, so designing a color space for color picking is about finding which tradeoffs to make. In particular, independent control of hue, lightness and chroma can not be achieved in a color space that also maps sRGB to a simple geometrical shape."

# Prerequisites

- **Colour picker** — These principles only make sense in the context of picker design
- **Colour gamut** — The geometrical shape property requires understanding what the target gamut is
- **Perceptual colour properties** — Requires familiarity with lightness, chroma, saturation, hue as perceptual concepts

# Key Properties

1. Orthogonality of axes (4 properties) — whether moving one slider affects other perceived properties
2. Geometric tractability (2 properties) — whether the gamut maps to a simple shape and whether extremes are findable
3. Behavioural uniformity (2 properties) — whether changes are smooth and perceptually equal across the slider range

# Construction / Recognition

## To Identify/Recognise:
1. A picker based on a colour space with orthogonal hue will show the same hue appearance regardless of lightness/saturation changes
2. A picker with "Varies Evenly" will make equal slider movements produce equally-perceptible colour differences
3. A picker with "Simple Geometrical Shape" never produces grey or black in an unexpected location on the picker surface

# Context & Application

- **Typical contexts**: Colour picker software design, colour space research, evaluation of existing picker implementations
- **Common applications**: Comparing HSL, HSV, HSLuv, NCS, and Oklab-based pickers against each other; guiding the design of future picker colour spaces

## Cross-Domain Connections

**Music → LOOSE**: Equal temperament in music and perceptual uniformity in colour pickers share the goal of making all equally-spaced steps appear/sound equally different. However, equal temperament is a deliberate compromise of pure intervals, while colour uniformity is a measurement goal. The analogy is useful for intuition but not rigorous.

# Examples

**Example 1** (from source): Ottosson's comparison table shows HSV achieves "yes" for Simple Geometrical Shape and Max Chroma at Edge, but "no" for Orthogonal Lightness and Chroma, and "no" for Varies Evenly. This pattern drives the design of Okhsv.

**Example 2** (from source): Okhsl achieves "yes" for Orthogonal Lightness and Orthogonal Hue, "yes" for Simple Geometrical Shape, and "yes" for Varies Smoothly — a substantially better profile than HSL.

# Relationships

## Builds Upon
- **Colour gamut** — The geometrical shape criterion is gamut-relative
- **Perceptual colour science** — The orthogonality criteria depend on perceptual measurement

## Enables
- **Okhsl / Okhsv design** — These new spaces were designed explicitly against this framework
- **Comparative colour space evaluation** — Provides vocabulary and criteria for systematic comparison

## Related
- **Orthogonal colour properties** — The four orthogonality properties form a subset of this framework

## Contrasts With
- **Naive simplicity** — HSL and HSV were designed for computational simplicity, not against this principled framework

# Common Errors

- **Error**: Assuming all eight properties can be satisfied simultaneously.
  **Correction**: Ottosson explicitly states they are in conflict; the design challenge is choosing which tradeoffs to make.

# Common Confusions

- **Confusion**: "Varies Evenly" and "Orthogonal Hue" mean the same thing.
  **Clarification**: "Varies Evenly" means equal slider steps produce equally large perceptual differences for the same axis; "Orthogonal Hue" means changing lightness or chroma does not also change the perceived hue.

# Source Reference

"What makes a good color picker?" section, Okhsv and Okhsl (Björn Ottosson).

# Verification Notes

- Definition source: Direct quotes from Ottosson's bulleted list
- Confidence rationale: High — the properties are exhaustively listed and applied to a comparison table
- Uncertainties: The properties are Ottosson's own formulation; they are not a published standard
- Cross-reference status: Verified within Ottosson source only
- Rosetta Stone check: Loose music/equal-temperament analogy noted but not added as rigorous mapping
- OCR issues: None significant
