---
concept: Modular Scale Construction (Procedure)
slug: modular-scale-construction
category: typography
subcategory: type-scale
tier: intermediate
layer: 2-domain
source: "More Meaningful Typography"
source_slug: posts
authors: "Tim Brown"
chapter: "Creating a modular scale for web design"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - [building a modular scale, generating a type scale, constructing a proportional scale]
prerequisites:
  - modular-scale
  - scale-ratio
  - scale-base-unit
extends:
  - modular-scale
related:
  - scale-application-typographic-hierarchy
  - ratio-selection-criteria
  - golden-ratio
contrasts_with:
  - []
answers_questions:
  - "How do you construct a modular scale for a typographic system?"
  - "What distinguishes a modular scale from arbitrary type size selection?"
rosetta_stone:
  - domain: mathematics
    concept: "Computing terms of a geometric sequence: a\u2099 = a\u2080 \u00d7 r\u207f"
    rating: rigorous
    note: "Constructing a modular scale is literally computing terms of a geometric sequence. The procedure is identical; only the naming convention differs."
css_implementation:
  - property: "font-size, width, margin, line-height"
    example: "/* Scale: 18px @ 1:1.618, 190px @ 1:1.618 */ body { font-size: 18px; } h1 { font-size: 29.124px; margin: 44.856px 0 0 307.420px; } h2 { font-size: 190px; } .main { width: 497.406px; } .group { width: 845.479px; }"
    support: baseline
---

# Quick Definition

Modular scale construction is the procedure by which a designer selects a ratio and one or more base values, generates a sequence of proportionally related numbers, and then applies those numbers to all significant measurements in a composition.

# Core Definition

Brown describes the construction process directly: "Making a modular scale is easy. You start with a ratio (for example, 1:1.618) and a number (like 10), then multiply and divide to get many resonant numbers."

The source articulates a multi-step process spanning three phases:
1. **Input selection** \u2014 choosing base typeface, body text size, ratio, and optionally a second important number.
2. **Scale generation** \u2014 multiplying and dividing repeatedly to produce the full sequence.
3. **Application** \u2014 drawing values from the scale for all measurements in the composition (type sizes, widths, margins, line heights).

Brown also describes a fourth element: **documentation** \u2014 commenting the scale URL and origins in the CSS so others can recreate the decisions.

He explicitly endorses improvisation at the application stage: scale values are "educated suggestions," not mandates. Designers may round values, combine values (addition/subtraction of two scale numbers), or break from the scale when a better-looking measurement is found.

# Prerequisites

- **Modular scale** \u2014 Understanding what a modular scale is and why one is being built.
- **Scale ratio** \u2014 How to select and apply a ratio.
- **Base unit** \u2014 How to identify and justify the starting number(s).

# Key Properties

1. **Typeface-first**: Procedure begins by selecting a typeface and finding its optimal body text size \u2014 this is the primary base unit.
2. **Ratio selection precedes generation**: The ratio must be chosen before computation; it is not determined by the output.
3. **Double-stranded option**: A second important number can be added to merge two geometric sequences, providing more values and filling gaps.
4. **Iterative application**: Applying scale values to CSS involves trial, testing in browser, and educated selection among values \u2014 not mechanical assignment.
5. **Documentation in CSS**: Best practice includes a stylesheet comment specifying the scale's starting values and ratio (or a URL to the modularscale.com result), enabling the scale to be recreated.
6. **Permissive improvisation**: The procedure tolerates and endorses deviation when visual judgment overrides mathematical output.

# Construction / Recognition

## To Construct/Create:
1. **Select typeface** \u2014 Choose the body text face before making layout decisions.
2. **Find optimal body size** \u2014 Test the face at various sizes; find the size at which it looks best ("crisp") for the project's rendering conditions.
3. **Choose ratio** \u2014 Select a ratio with meaningful cultural, historical, or contextual relevance (e.g., 1:1.618 for Renaissance humanist contexts).
4. **Identify secondary base (optional)** \u2014 Find a second important number from a key compositional element (large headline, media width, caption size).
5. **Generate scale** \u2014 Multiply and divide from each base by the ratio to produce ascending and descending sequences. Merge sequences if double-stranded.
6. **Apply to CSS** \u2014 Use scale values for font sizes, line heights, column widths, margins. Test in browser; select among adjacent scale values when multiple seem plausible.
7. **Document** \u2014 Add a CSS comment identifying the scale parameters (or linking to the modularscale.com URL).
8. **Improvise as needed** \u2014 When no scale value looks right, combine values (comment math), round values, or use a non-scale value; document any improvisations.

## To Identify/Recognise:
1. Look for a CSS comment at the top of the stylesheet naming scale parameters.
2. Check that font-size, width, and margin values in the CSS correspond to computed values of a geometric sequence with the documented ratio and base.
3. Look for "comment math" in the CSS (e.g., `font-size: 21.178px; /* 27.723 - 6.545 */`) indicating combined scale values.

# Context & Application

- **Typical contexts**: Beginning of a web design project; redesign; building a new type system.
- **Common applications**: Full-page layout with modular scale; establishing a type hierarchy; providing a documented measurement rationale for a design system.
- **Historical/stylistic notes**: Brown notes this approach aligns with "content-out" design (from Mark Boulton), in contrast to "canvas-in" design that starts with viewport/grid dimensions. The procedure inverts conventional web design workflow.

## Cross-Domain Connections

**Mathematics \u2192 RIGOROUS**: Scale construction is the computation of terms in a geometric sequence. Phase 2 (scale generation) is precisely: for i in integers: value = base \u00d7 ratio^i. The procedure is mathematically identical to generating a geometric sequence; only the naming and application context differ.

# Examples

**Example 1** (from source, "Modular scales and how they apply to web design" \u2014 simple scale): Starting number 10, ratio 1:1.618. Ascending: 10 \u00d7 1.618 = 16.180; 16.180 \u00d7 1.618 = 26.179; 26.179 \u00d7 1.618 = 42.358. Descending: 10 / 1.618 = 6.180; 6.180 / 1.618 = 3.819; 3.819 / 1.618 = 2.360.

**Example 2** (from source, "Creating a modular scale for web design" \u2014 full project): (a) Typeface: Minion Pro. (b) Body size: 18px (tested on Web Font Specimen until crisp). (c) Ratio: 1:1.618 (golden ratio, chosen for Renaissance cultural fit). (d) Second base: 190px (h2 headline, tested until it "anchor[s] the composition"). (e) Scale generated at modularscale.com. (f) Values applied: 29.124px (h1), 497.406px (main column), 845.479px (container), 44.856px and 27.723px and 307.420px (margins).

**Example 3** (from source, "Applying a modular scale in web design" \u2014 improvisation): Sidebar font-size: 15px, not present in the scale, used because "15px Minion Pro Caption sure looks good next to 18px Minion Pro." Intro paragraph: 21.178px, documented as `27.723 - 6.545` (combining two scale values). Left margin on h2: 20px ("Optical alignment of T stem to left edge of .side"), not from scale, "emerged from the lay of the letterforms."

# Relationships

## Builds Upon
- **Modular scale** \u2014 Procedure operationalises the concept.
- **Scale ratio** \u2014 The ratio is the procedure's second required input.
- **Base unit** \u2014 The base unit is the procedure's first required input.

## Enables
- **Scale application to typographic hierarchy** \u2014 The constructed scale is the prerequisite for applying values to type sizes.
- **Typographic rhythm via modular scale** \u2014 Consistent proportional spacing depends on having a scale to draw from.

## Related
- **Ratio selection criteria** \u2014 The procedure depends on ratio selection; the criteria for selecting well are a related concept.
- **Double-stranded modular scale** \u2014 An extension of the construction procedure using two base values.

## Contrasts With
- **Grid-first design** \u2014 Starting with a grid and pouring content in; Brown argues this is less web-native than starting with type and building outward.

# Common Errors

- **Error**: Generating the scale from an arbitrarily chosen base number rather than from the body text size.
  **Correction**: Find the optimal body text size through careful testing before beginning scale construction. "One pixel of font-size up or down can completely change how a typeface looks."

- **Error**: Applying scale values mechanically to every measurement without visual testing.
  **Correction**: "I alternate between CSS editor and browser, checking to see how each value looks" (Brown). The scale guides; visual judgment decides.

- **Error**: Failing to document the scale parameters in the CSS.
  **Correction**: "Leave a note about my scale. This serves two purposes: first, it lets people know I'm using a modular scale; and second, it provides a means of recreating the scale, so that my decisions can be studied and my measurements can be accurately changed and built upon."

# Common Confusions

- **Confusion**: The double-stranded scale uses a different ratio from the single-stranded scale.
  **Clarification**: A double-stranded scale uses the same ratio as a single-stranded scale, but with two different starting numbers. The result is two geometric sequences with the same ratio, merged and sorted. Brown's example uses ratio 1:1.618 for both strands (18px and 190px).

# Source Reference

"Modular scales and how they apply to web design"; "Creating a modular scale for web design"; "Applying a modular scale in web design" \u2014 More Meaningful Typography, Tim Brown (A List Apart, May 2011)

# Verification Notes

- Definition source: Synthesised from the full procedural account across three sections; individual steps are directly supported by source text.
- Confidence rationale: High \u2014 the article is primarily a worked example of this procedure, with explicit steps and actual CSS values.
- Uncertainties: The source does not address what to do when a scale produces unusable values for all steps in a particular range \u2014 whether to change ratio, base, or tolerate improvisation throughout. The improvisation guidance is permissive but not fully systematic.
- Cross-reference status: Verified.
- Rosetta Stone check: Mapping added \u2014 mathematics/geometric-sequence-computation (rigorous).
- OCR issues: CSS code blocks contain some HTML artifacts (escaped characters, line-break issues in figure captions) \u2014 ignored; article prose is clean.
