---
concept: Scale Ratio
slug: scale-ratio
category: typography
subcategory: type-scale
tier: foundational
layer: 2-domain
source: "More Meaningful Typography"
source_slug: posts
authors: "Tim Brown"
chapter: "Modular scales and how they apply to web design"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - [ratio, proportion, typographic ratio]
prerequisites:
  - []
extends:
  - []
related:
  - modular-scale
  - golden-ratio
  - perfect-fourth-ratio
  - perfect-fifth-ratio
  - ratio-selection-criteria
contrasts_with:
  - []
answers_questions:
  - "Why must visual scales be geometric (multiplicative) rather than arithmetic (additive)?"
  - "How do you select an appropriate scale ratio for a given design context?"
rosetta_stone:
  - domain: music
    concept: "Interval ratio \u2014 the frequency ratio between two tones defining a musical interval (e.g., 3:2 for a perfect fifth)"
    rating: rigorous
    note: "Typographic scale ratios derived from musical intervals carry identical numeric values. The ratio 4:3 (perfect fourth) applied to frequencies produces a musical interval; applied to type sizes produces a scale step. Same number, different domain."
  - domain: mathematics
    concept: "Common ratio of a geometric sequence"
    rating: rigorous
    note: "The scale ratio is precisely the common ratio r in the geometric sequence a, ar, ar\u00b2, ar\u00b3. This is a definitional identity, not an analogy."
css_implementation:
  - property: "font-size (computed from ratio)"
    example: "/* Base 18px, ratio 1.618 */ font-size: 18px; /* step 0 */ font-size: 29.124px; /* step 1: 18 \u00d7 1.618 */ font-size: 47.124px; /* step 2: 18 \u00d7 1.618\u00b2 */"
    support: baseline
---

# Quick Definition

A scale ratio is the fixed multiplier that generates every value in a modular scale \u2014 the single number by which you multiply to move one step up the scale, or divide to move one step down.

# Core Definition

The scale ratio is the defining parameter of a modular scale. Brown states: "You start with a ratio (for example, 1:1.618) and a number (like 10), then multiply and divide to get many resonant numbers." The ratio is not decorative \u2014 it is the generative engine. Every pair of adjacent values in the scale shares the same ratio.

A ratio expresses a proportion between two quantities. Brown uses the notation "1:1.618" throughout, where the left term is always 1 and the right term is the multiplier. Equivalently, the ratio can be expressed as a single decimal (1.618) representing how much larger each successive scale step is relative to the previous.

The source emphasises that the ratio should be "meaningful" \u2014 chosen for cultural, historical, or contextual reasons, not arbitrarily. For Brown's Minion/Renaissance typography example, he chose 1:1.618 because golden-ratio proportions are historically connected to Renaissance book design and page layout.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. **Generative**: The ratio alone (together with a base number) is sufficient to produce the entire scale \u2014 infinitely in both directions.
2. **Constant**: The same ratio applies between every adjacent pair of values in the scale; it does not vary across the scale.
3. **Meaningful selection**: Brown argues ratios should be chosen for relevance to the project's design, content, history, or cultural context \u2014 not for convenience.
4. **Determines scale character**: A smaller ratio (e.g., 1.125) produces closely spaced values suitable for subtle hierarchy; a larger ratio (e.g., 1.618) produces widely spaced values with dramatic contrast between levels.

# Construction / Recognition

## To Construct/Create:
1. Identify the design context and its relevant cultural, historical, or aesthetic associations.
2. Select a ratio that fits: ratios with harmonic grounding (derived from musical intervals or geometry) are preferred over arbitrary decimals.
3. Express the ratio in the form 1:N where N is the multiplier (e.g., 1:1.333 for the perfect fourth).
4. Apply: next value = current value \u00d7 N; previous value = current value / N.

## To Identify/Recognise:
1. Take any two adjacent values in a claimed scale and divide the larger by the smaller.
2. If the result is consistent across all adjacent pairs, that quotient is the scale ratio.
3. Check designer's CSS comments \u2014 Tim Brown's practice is to document the scale in the stylesheet header (e.g., "18px @ 1:1.618").

# Context & Application

- **Typical contexts**: Any modular scale construction; type hierarchy planning; spacing system design.
- **Common applications**: Selecting the ratio before building a modular scale; documenting the ratio in CSS comments so future designers can recreate the scale.
- **Historical/stylistic notes**: Brown drew his 1:1.618 choice from Renaissance typography practice. Other practitioners choose ratios from musical intervals (see Musical Intervals as Ratio Sources), from geometric proportions found in nature, or from dimensions meaningful to a specific project.

## Cross-Domain Connections

**Music \u2192 RIGOROUS**: Musical interval ratios (derived from harmonic series integer ratios) produce exactly the numeric values used as typographic scale ratios. The ratio 3:2 defines both the perfect fifth in music and, when used as a typographic multiplier, produces a bold type scale. The numbers are identical; the domain of application differs.

**Mathematics \u2192 RIGOROUS**: The scale ratio is the common ratio r of a geometric sequence. Every property of geometric sequences (exponential growth, constant relative step size, multiplicative reversibility) applies directly to typographic modular scales.

# Examples

**Example 1** (from source, "Creating a modular scale for web design"): Brown chose ratio 1:1.618 (golden ratio) for his Minion/Renaissance example. Justification given: "It is a beautiful proportion with historical and cultural connections that make sense for the typefaces I've chosen and the text I'm setting... Page and textblock proportions in Renaissance works were based on the golden mean."

**Example 2** (from source, "Modular scales and how they apply to web design"): The introductory worked example uses ratio 1:1.618 with base 10, producing the sequence 2.360, 3.819, 6.180, 10.000, 16.180, 26.179, 42.358.

# Relationships

## Builds Upon
- (None in this source \u2014 the ratio is a primitive input to the scale system.)

## Enables
- **Modular scale** \u2014 The ratio is the scale's generative parameter; no scale exists without it.
- **Modular scale construction (procedure)** \u2014 The ratio is the required second input (alongside the base unit) to the construction procedure.

## Related
- **Golden ratio** \u2014 One specific, historically prominent scale ratio (1.618).
- **Perfect fourth ratio** \u2014 Another specific ratio (1.333), derived from music.
- **Perfect fifth ratio** \u2014 Another specific ratio (1.5), derived from music.
- **Ratio selection criteria** \u2014 The guidelines for choosing an appropriate ratio.

## Contrasts With
- **Arbitrary multipliers** \u2014 Choosing a multiplier (e.g., 1.25 or 2) without grounding in geometric, musical, or cultural significance; Brown argues this produces less meaningful results.

# Common Errors

- **Error**: Choosing a ratio because it is a "round" or easily divisible number rather than because it has harmonic or cultural meaning.
  **Correction**: Brown argues ratio selection should be grounded in context: the ratio "should be meaningful to a project's design, content, or both."

- **Error**: Using a ratio that is too large for the design context, creating extreme size jumps that overwhelm the hierarchy.
  **Correction**: Match ratio size to the degree of contrast needed. A large ratio (1.618) suits display/editorial contexts; a smaller ratio may be more appropriate for dense informational UIs.

# Common Confusions

- **Confusion**: The ratio and the base number are interchangeable \u2014 it doesn't matter which you change.
  **Clarification**: They have completely different effects. Changing the base number shifts all values uniformly up or down. Changing the ratio alters the spacing between scale steps \u2014 the fundamental character of the scale.

# Source Reference

"Modular scales and how they apply to web design"; "Creating a modular scale for web design" \u2014 More Meaningful Typography, Tim Brown (A List Apart, May 2011)

# Verification Notes

- Definition source: Synthesised from procedural description \u2014 "You start with a ratio (for example, 1:1.618) and a number (like 10), then multiply and divide to get many resonant numbers." No single-sentence definition of "ratio" as a standalone term is given; the concept is defined through use.
- Confidence rationale: High \u2014 the ratio is central to every example and procedure in the article.
- Uncertainties: The source does not explicitly explain why geometric (multiplicative) ratios are perceptually preferable to arithmetic progressions. This is domain knowledge; it should not be attributed to this source directly.
- Cross-reference status: Verified.
- Rosetta Stone check: Mapping added \u2014 music/interval-ratio (rigorous), mathematics/common-ratio (rigorous).
- OCR issues: None significant in the relevant sections.
