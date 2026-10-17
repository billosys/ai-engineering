---
concept: "Orthogonal Colour Properties"
slug: "orthogonal-colour-properties"
category: "colour-theory"
subcategory: "colour-spaces"
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
    - "independent colour axes"
    - "colour axis independence"
prerequisites:
  - "colour-gamut"
  - "hsl"
  - "hsv"
extends:
  - "colour-picker-design-principles"
related:
  - "okhsl"
  - "okhsv"
  - "chroma-vs-saturation"
contrasts_with: []
answers_questions:
  - "What makes a colour picker perceptually well-designed?"
  - "What distinguishes chroma from saturation in a colour space?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Orthogonal basis vectors in a vector space"
    rating: "loose"
    note: "Numeric colour-model parameters and equal frequency ratios/Euclidean basis vectors do not establish equal visual or auditory differences or perceptual independence."
---

# Quick Definition


Orthogonal colour properties are proposed picker goals about changing one perceived attribute while holding another constant. They are not equivalent to perpendicular numeric basis vectors or independent model parameters.

# Core Definition


Ottosson lists four distinct goals: hold perceived lightness while changing hue/chroma/saturation; hold perceived chroma while changing lightness/hue; hold perceived saturation while changing lightness/hue; and hold perceived hue while changing the other named attributes. The article says these goals conflict with simple sRGB gamut geometry. A model may define independent coordinates without perceptual independence, and a perpendicular basis in Euclidean mathematics does not establish colour appearance. The article’s ratings are subjective and scoped to its sRGB comparison.

# Prerequisites


- **Colour gamut** — The source describes a tradeoff between sRGB gamut geometry and control goals.
- **Perceptual colour concepts** — The four criteria name desired appearance behavior, distinct from numeric parameter independence.

# Key Properties


1. Orthogonal Lightness, Chroma, Saturation and Hue are distinct proposed criteria.
2. Numeric independence, perpendicular basis vectors and perceptual independence are different claims.
3. The source table rates Okhsl yes for Orthogonal Lightness/Hue, no for Orthogonal Chroma/Saturation; Okhsv yes for Orthogonal Hue, partial for Orthogonal Saturation, and no for Orthogonal Lightness/Chroma. These ratings are subjective and sRGB-scoped.
4. No such rating proves exact visual invariance across people, contexts, displays or gamut mapping.

# Construction / Recognition

## To Identify/Recognise:

1. Specify which attribute is held and which parameter changes; do not use “orthogonal” without its intended perceptual criterion.
2. Hue shifts reported for HSV and chroma variation reported for HSLuv are attributed examples from the source, not new experiments.
3. To evaluate an actual interface, inspect the rendered output under its target conditions.

# Context & Application

- **Typical contexts**: Colour space design, evaluation of colour pickers, perceptual colour science
- **Common applications**: Understanding why certain colour pickers feel more intuitive; designing colour scales for data visualisation

## Cross-Domain Connections


**Mathematics → LOOSE**: Numeric colour-model parameters and equal frequency ratios/Euclidean basis vectors provide limited structural analogies. They do not establish equal visual or auditory differences or perceptual independence. The mapping is not rigorous.

# Examples


**Example 1** (source table): The author’s subjective comparison reports Okhsl yes for Orthogonal Lightness and Hue; Okhsv yes for Orthogonal Hue and no for Orthogonal Lightness. Both are rated no for Orthogonal Chroma. These are source-reported sRGB judgments, not universal guarantees.

**Example 2** (source description): The article attributes HSV blue-to-purple shifts and HSLuv chroma changes to examples; figures were not independently inspected and are not new empirical tests.

# Relationships

## Builds Upon

- **Perceptual colour science** — The criteria name desired changes in perceived attributes; ratings are source judgments, not measurement results.

## Enables

- **Okhsl / Okhsv design** — Ottosson compares their tradeoffs using these proposed labels.

## Related

- **Colour picker design principles** — These four goals form part of the article’s eight-criterion framework.
- **Chroma vs saturation** — Their distinction matters because the framework lists both orthogonal chroma and orthogonal saturation.

# Common Errors


**Error**: Assuming numeric independence or mathematical orthogonality proves perceptual independence.
  **Correction**: The picker criteria name desired appearance behavior. Evaluate the actual model and viewing/rendering conditions; do not promote a structural analogy into evidence.

# Common Confusions


**Confusion**: Orthogonal Saturation and Orthogonal Chroma are the same property.
  **Clarification**: They are separate proposed goals. HSL/HSV labels, CIE appearance terms and model coordinates have different definitions; state which one is meant.

# Source Reference

"What makes a good color picker?" section, Okhsv and Okhsl (Björn Ottosson).

# Verification Notes


This full available-evidence review checked the four goal definitions and cited model ratings against the complete prepared picker article. Ratings remain subjective source comparisons scoped to sRGB; they are not new measurements of perceptual independence. Figures were not independently inspected. The mathematics analogy is explicitly loose and does not establish perceptual or sensory equality. Extraction-confidence metadata is unchanged.
