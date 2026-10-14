---
concept: "Modular Scale Construction (Procedure)"
slug: "modular-scale-construction"
category: "typography"
subcategory: "type-scale"
tier: "intermediate"
layer: "2-domain"
source: "More Meaningful Typography"
source_slug: "posts"
authors: "Tim Brown"
chapter: "Creating a modular scale for web design"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "high"
aliases:
  -
    - "building a modular scale"
    - "generating a type scale"
    - "constructing a proportional scale"
prerequisites:
  - "modular-scale"
  - "scale-ratio"
  - "scale-base-unit"
extends:
  - "modular-scale"
related:
  - "scale-application-typographic-hierarchy"
  - "ratio-selection-criteria"
  - "golden-ratio"
contrasts_with: []
answers_questions:
  - "How do you construct a modular scale for a typographic system?"
  - "What distinguishes a modular scale from arbitrary type size selection?"
rosetta_stone:
  -
    domain: "mathematics"
    concept: "Computing terms of a geometric sequence: aₙ = a₀ × rⁿ"
    rating: "rigorous"
    note: "Generating each strand computes a*r^n from its own declared base and ratio. Sorting the combined values of multiple strands is a separate operation; the merged list need not itself be geometric."
css_implementation:
  -
    property: "font-size, width, margin, line-height"
    example: "/* Scale: 18px @ 1:1.618, 190px @ 1:1.618 */ body { font-size: 18px; } h1 { font-size: 29.124px; margin: 44.856px 0 0 307.420px; } h2 { font-size: 190px; } .main { width: 497.406px; } .group { width: 845.479px; }"
    support: "baseline"
---

# Quick Definition

Modular-scale construction is one procedure for declaring a positive ratio `r>0` and one or more positive starting values `a>0`, generating each corresponding strand as `a*r^n`, and considering selected values for a composition. In a strand, `v[n+1]/v[n]=r` in declared index order; `r>1` rises as `n` increases, `0<r<1` falls, and `r=1` repeats a value. A sorted merge is a list of options, not generally one geometric sequence, and using it for every measurement is optional.

# Core Definition

Brown describes the construction process directly: "Making a modular scale is easy. You start with a ratio (for example, 1:1.618) and a number (like 10), then multiply and divide to get many resonant numbers."

The article's example spans three phases:
1. **Contextual input selection** — Brown begins with an already selected typeface and text, tests a body-text size, chooses a ratio for that project, and adds an optional second important number.
2. **Scale generation** — each starting value and its declared ratio generate a strand by multiplication or division.
3. **Application** — Brown tries selected scale values for type sizes, widths, margins and line height, then adjusts where the result does not suit the composition. This is an approach, not a universal requirement.

Brown also describes a fourth element: **documentation** — commenting the scale URL and origins in the CSS so others can recreate the decisions.

He explicitly endorses improvisation at the application stage: scale values are "educated suggestions," not mandates. In his example he rounds values, combines values through comment math, and uses non-scale values when they better fit the design. These are source-specific examples, not required procedures.

# Prerequisites

- **Modular scale** — Understanding what a modular scale is and why one is being built.
- **Scale ratio** — How to select and apply a ratio.
- **Base unit** — How to identify and justify the starting number(s).

# Key Properties

1. **Typeface-first in Brown's example**: He has selected a typeface and text, then tests a body-text size as one starting value. Projects may begin from other fixed or contextual inputs.
2. **Ratio selection precedes generation**: The ratio must be chosen before computation; it is not determined by the output.
3. **Multi-strand option**: Brown says a double-stranded construction can start from two numbers or two ratios. Each generates its own strand; sorting their union may add options or fill gaps, but does not generally preserve one adjacent ratio.
4. **Iterative application**: Applying scale values to CSS involves trial, testing in browser, and educated selection among values — not mechanical assignment.
5. **Documentation in Brown's workflow**: He records the scale inputs or calculator URL in a stylesheet comment so others can recreate his example. Projects may document their own decisions in a suitable form.
6. **Permissive improvisation**: The procedure tolerates and endorses deviation when visual judgment overrides mathematical output.

# Construction / Recognition

## To Construct/Create:
1. **Optional typeface-first route** — Brown selects the text face before layout decisions in his example; another project may have fixed or independent inputs.
2. **If using Brown's route, test a body size** — He looks for a size that works for his design goals and rendering, calling the chosen 18px Minion size crisp. This example does not set a universal optimal size.
3. **Declare a ratio for each strand** — Brown chooses `1:1.618` for historical and cultural reasons specific to his Minion/Renaissance example. A project's ratio choice is contextual, not governed by a universal preference rule.
4. **Identify secondary base (optional)** — Find a second important number from a key compositional element (large headline, media width, caption size).
5. **Generate scale** — For each declared base `a>0` and ratio `r>0`, generate exact terms `v[n]=a*r^n`; adjacent indexed terms satisfy `v[n+1]/v[n]=r`. For `r>1`, increasing `n` raises values and decreasing `n` lowers them; for `0<r<1` the value direction reverses; `r=1` repeats the base. Merge sequences if double-stranded.
6. **Apply selected values if useful** — Brown tests type sizes, line height, column widths and margins in the browser. Keep independent, fixed or optical values where they work better.
7. **Document** — Add a CSS comment identifying the scale parameters (or linking to the modularscale.com URL).
8. **Improvise as needed** — When no scale value looks right, combine values (comment math), round values, or use a non-scale value; document any improvisations.

## To Identify/Recognise:
1. Look for a CSS comment at the top of the stylesheet naming scale parameters.
2. For each claimed strand, compare its declared base and ratio with the values attributed to it. A merged list and improvised CSS values require separate interpretation.
3. Look for "comment math" in the CSS (e.g., `font-size: 21.178px; /* 27.723 - 6.545 */`) indicating combined scale values.

# Context & Application

- **Typical contexts**: Beginning of a web design project; redesign; building a new type system.
- **Common applications**: Full-page layout with modular scale; establishing a type hierarchy; providing a documented measurement rationale for a design system.
- **Historical/stylistic notes**: Brown paraphrases Mark Boulton’s “canvas in” and “content out” positions and presents his content-out approach as an inversion of the then-common web design workflow. This is Brown’s historical framing, not a claim that every design workflow is inverted.

## Cross-Domain Connections

**Mathematics → RIGOROUS WITHIN EACH STRAND**: For declared positive base `a>0` and ratio `r>0`, a strand has exact terms `a*r^n` for integer `n`, with `v[n+1]/v[n]=r`. Merging and sorting multiple generated strands is a distinct operation; the result need not be geometric.

# Examples

**Example 1** (source transcription, "Modular scales and how they apply to web design"): Brown prints the base-10 ascending values `10.000, 16.180, 26.179, 42.358` and descending values `10.000, 6.180, 3.819, 2.360` for decimal ratio `1.618`. The descending figures are reported source text. Independent calculation from the exact base and ratio, rounded half-even to three places, gives `2.361, 3.820, 6.180, 10.000, 16.180, 26.179, 42.358`.

**Example 2** (Brown's source example, "Creating a modular scale for web design"): (a) Typeface: Minion Pro. (b) Body size: 18px, tested until crisp for this design. (c) Decimal ratio: `1.618`, chosen for his stated Renaissance context and an approximation to the golden ratio. (d) Second important number: 190px for the `h2`, tested until it would anchor his composition. (e) Scale generated at modularscale.com. (f) Source-reported applied values include 29.124px (`h1`), 497.406px (main column), 845.479px (container), and margins 44.856px, 27.723px and 307.420px. These are historical example reports, not defaults or recalculated values.

**Example 3** (from source, "Applying a modular scale in web design" — improvisation): Sidebar font-size: 15px, not present in the scale, used because "15px Minion Pro Caption sure looks good next to 18px Minion Pro." Intro paragraph: 21.178px, documented as `27.723 - 6.545` (combining two scale values). Left margin on h2: 20px ("Optical alignment of T stem to left edge of .side"), not from scale, "emerged from the lay of the letterforms."

# Relationships

## Builds Upon
- **Modular scale** — Procedure operationalises the concept.
- **Scale ratio** — The ratio is the procedure's second required input.
- **Base unit** — The base unit is the procedure's first required input.

## Enables
- **Scale application to typographic hierarchy** — The constructed scale is the prerequisite for applying values to type sizes.
- **Typographic rhythm via modular scale** — A scale is one possible source for coordinating selected measures, while independent and optical values remain available.

## Related
- **Ratio selection criteria** — The procedure depends on ratio selection; the criteria for selecting well are a related concept.
- **Double-stranded modular scale** — An extension of the construction procedure using two base values.

## Contrasts With
- **Grid-first design** — Brown contrasts his content-out workflow with canvas-in approaches; this card does not treat a grid as incompatible with a modular scale.

# Common Errors

- **Error**: Treating Brown's body-text starting point as a rule for every construction.
  **Correction**: Brown tests a size for his selected typeface and design; a project may have fixed or independently chosen inputs. His one-pixel observation concerns the rendering sensitivity he describes, not a universal base-selection requirement.

- **Error**: Applying scale values mechanically to every measurement without visual testing.
  **Correction**: "I alternate between CSS editor and browser, checking to see how each value looks" (Brown). The scale guides; visual judgment decides.

- **Error**: Failing to document the scale parameters in the CSS.
  **Correction**: "Leave a note about my scale. This serves two purposes: first, it lets people know I'm using a modular scale; and second, it provides a means of recreating the scale, so that my decisions can be studied and my measurements can be accurately changed and built upon."

# Common Confusions

- **Confusion**: A double-stranded scale must use one common ratio.
  **Clarification**: Brown says the two strands can be generated from two starting numbers or two starting ratios. Each strand has its own declared base and ratio. His example uses 18px and 190px with `1:1.618`; that example does not constrain other constructions. A sorted merge is not generally geometric.

# Source Reference

"Modular scales and how they apply to web design"; "Creating a modular scale for web design"; "Applying a modular scale in web design" — More Meaningful Typography, Tim Brown (A List Apart, May 2011)

# Verification Notes

- Historical extraction note: The prior record synthesized Brown's three article sections, assigned extraction confidence `high`, and recorded the cross-reference as “Verified.” Those are historical extraction observations, not current source-fidelity or semantic-review results.
- Current scoped review: The prepared article at lines 133–337 supports Brown's contextual inputs, two-starting-number-or-ratio wording, examples and departures. Exact mathematical outcomes are checked separately below and in the batch record.
- Technical scope: Each strand is geometric under its declared inputs; a sorted multi-strand union need not be. No scale is required for every measurement.
- Limits: Prepared text includes HTML/CSS conversion residue; immutable capture identity, conversion lineage and original-to-prepared fidelity remain unresolved. The old extraction-confidence value is retained without upgrade. CDC independent review is pending.
