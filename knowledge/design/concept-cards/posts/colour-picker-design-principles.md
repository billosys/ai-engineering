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


Eight criteria proposed by Ottosson for comparing colour spaces as colour-picker bases. They cover perceptual control goals, target-gamut geometry, and the smoothness or evenness of parameter change; they are proposed, sometimes conflicting criteria, not a published universal standard.

# Core Definition


Ottosson’s eight proposed goals are Orthogonal Lightness, Orthogonal Chroma, Orthogonal Saturation, Orthogonal Hue, Simple Geometrical Shape, Max Chroma at Edge, Varies Smoothly, and Varies Evenly. The first four describe desired control over named perceived attributes; the next two concern the target gamut shape and access to an edge; the final pair distinguish continuity from equal perceived change. The article says these goals conflict and compares models for sRGB. Its table is explicitly subjective: a “yes” records the author’s assessment for that discussion, not proof of exact perception or a universal model ranking.

# Prerequisites


- **Colour picker** — These criteria are proposed for comparing picker coordinate choices and behavior.
- **Colour gamut** — Geometric criteria require a named target gamut.
- **Perceptual colour properties** — The criteria distinguish lightness, chroma, saturation and hue as intended appearance outcomes from numeric axes.

# Key Properties


1. Four distinct perceptual-control goals: lightness, chroma, saturation and hue.
2. Two target-geometry goals: simple shape and maximum chroma at an edge.
3. Two behavior goals: continuous variation and equally perceived change are not the same.
4. The first comparison table reports HSV, HSL, HSLuv, Lab-like and NCS profiles; a later table compares Okhsv and Okhsl. Munsell is historical context, not a rated table profile. Ratings remain subjective and scoped to the article’s sRGB discussion.

# Construction / Recognition

## To Identify/Recognise:

1. Treat a “yes” as the source author’s scoped comparison, not direct evidence that all users see the same result.
2. A numeric slider that changes one coordinate does not establish perceptual independence.
3. “Varies Smoothly” concerns abrupt/discontinuous changes; “Varies Evenly” concerns perceived change magnitude across the parameter range.
4. Widget layout and accessibility need separate, task-specific review.

# Context & Application

- **Typical contexts**: Colour picker software design, colour space research, evaluation of existing picker implementations
- **Common applications**: Comparing the first table’s HSV, HSL, HSLuv, Lab-like and NCS profiles, then the later Okhsv/Okhsl comparison, against the eight criteria; guiding discussion of picker tradeoffs. Munsell provides historical context, not a rated profile.

## Cross-Domain Connections


**Music → LOOSE**: Picker parameters and equal frequency ratios or Euclidean basis vectors can offer limited structural analogies. They do not establish equal visual or auditory differences, nor perceptual independence. The analogy is not a rigorous cross-domain mapping.

# Examples


**Example 1** (from source): The author’s subjective sRGB table rates HSV yes for Simple Geometrical Shape and Max Chroma at Edge, no for Orthogonal Lightness and Orthogonal Chroma, partial for Orthogonal Hue and Saturation, and no for Varies Evenly. This is a scoped reported comparison.

**Example 2** (from source): Okhsl is rated yes for Orthogonal Lightness, Orthogonal Hue, Simple Geometrical Shape and Varies Smoothly; it is no for Orthogonal Chroma, Orthogonal Saturation, Max Chroma at Edge and Varies Evenly. The table does not establish exact perceptual uniformity.

# Relationships

## Builds Upon

- **Colour gamut** — Simple-shape and edge criteria depend on the specified target gamut.
- **Perceptual colour science** — The first four criteria name desired appearance behavior; a rating alone does not prove it.

## Enables

- **Okhsl / Okhsv design** — Ottosson evaluates these against the proposed criteria for his sRGB discussion.
- **Comparative colour-space evaluation** — The criteria offer a source-specific vocabulary; they are not a published universal standard.

## Related

- **Orthogonal colour properties** — Four criteria concern distinct desired perceptual controls.

## Contrasts With

- **Unqualified simplicity claims** — The article describes tradeoffs among geometry and perceptual goals; no general historical claim about why HSL/HSV were designed is made here.

# Common Errors


**Error**: Assuming all eight criteria can be satisfied simultaneously, or that the comparison table proves universal quality.
  **Correction**: The author describes tradeoffs and presents subjective judgments for an sRGB discussion. State the selected task and destination, then assess actual output and interaction.

# Common Confusions

- **Confusion**: "Varies Evenly" and "Orthogonal Hue" mean the same thing.
  **Clarification**: "Varies Evenly" means equal slider steps produce equally large perceptual differences for the same axis; "Orthogonal Hue" means changing lightness or chroma does not also change the perceived hue.

# Source Reference

"What makes a good color picker?" section, Okhsv and Okhsl (Björn Ottosson).

# Verification Notes


This full available-evidence review checked all eight stated goals and comparison profiles against the complete prepared picker article. Ratings are recorded as source-author judgments for the sRGB discussion; they are not an independent perceptual experiment or universal standard. Figures were not visually inspected. The analogy is explicitly loose and does not establish equal sensory differences or independence. No widget/accessibility behavior was tested; extraction-confidence metadata is unchanged.
