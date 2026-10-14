---
concept: "Modular Scale (Typography)"
slug: "modular-scale"
category: "typography"
subcategory: "type-scale"
tier: "foundational"
layer: "2-domain"
source: "More Meaningful Typography"
source_slug: "posts"
authors: "Tim Brown"
chapter: "Modular scales and how they apply to web design"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: "high"
aliases:
  -
    - "type scale"
    - "proportional scale"
    - "harmonious scale"
prerequisites: []
extends: []
related:
  - "scale-ratio"
  - "golden-ratio"
  - "modular-scale-construction"
  - "scale-application-typographic-hierarchy"
contrasts_with: []
answers_questions:
  - "What distinguishes a modular scale from arbitrary type size selection?"
  - "What makes a type hierarchy feel harmonious vs arbitrary?"
rosetta_stone:
  -
    domain: "music"
    concept: "Reuse of a selected musical interval ratio"
    rating: "rigorous"
    note: "A selected musical interval ratio can be reused as the numeric multiplier of a typographic strand. This is a shared construction, not a claim that every musical scale has one constant adjacent ratio or that auditory harmony guarantees visual harmony."
  -
    domain: "mathematics"
    concept: "Geometric sequence — a sequence where each term is the previous term multiplied by a constant ratio"
    rating: "rigorous"
    note: "For one strand with a declared base a and ratio r, values a*r^n form a geometric sequence. Combining or sorting multiple strands does not generally retain a constant ratio between adjacent merged values."
css_implementation:
  -
    property: "font-size"
    example: "font-size: 18px; /* scale origin */ font-size: 29.124px; /* scale step */ font-size: 190px; /* scale origin (second strand) */"
    support: "baseline"
  -
    property: "width / margin / line-height"
    example: "width: 497.406px; /* scale-derived measure */ margin: 44.856px 0 0 307.420px; /* scale-derived spacing */"
    support: "baseline"
---

# Quick Definition

A modular scale uses one or more ratio-generated strands as a source of proportional values. Each individual strand is geometric; combining and sorting strands does not generally leave one constant ratio between adjacent values. Designers may use selected values as a guide for a composition.

# Core Definition

Tim Brown defines a modular scale through both paraphrase and direct quotation: "A modular scale is a sequence of numbers that relate to one another in a meaningful way." He then quotes Robert Bringhurst: "A modular scale, like a musical scale, is a prearranged set of harmonious proportions."

For one strand, choose a positive base `a>0` and ratio `r>0`; its exact terms are `v[n]=a*r^n` for integer `n`, with `v[n+1]/v[n]=r` in the declared indexed order. When `r>1`, increasing `n` gives ascending values and decreasing `n` gives descending values; when `0<r<1`, value direction reverses, and `r=1` repeats the same value. A multi-strand construction generates each strand from its own starting number or ratio, then may combine and sort the results. Brown describes using scale values for type sizes, line height, line length, margins, column widths and more; this is his design approach, not a requirement that every measurement use one scale.

# Prerequisites

This is a foundational concept with no prerequisites within this source. It is introduced directly via definition and example in the opening paragraphs.

# Key Properties

1. **Ratio-derived strands**: Each strand is generated from its declared positive base and ratio (`a>0`, `r>0`; for example, `a*r^n`). A construction may combine multiple strands.
2. **Geometric within a strand**: In declared index order, exact terms satisfy `v[n+1]/v[n]=r`; rounded displays may not preserve an exactly constant quotient. For `r>1`, increasing the index raises values; for `0<r<1`, it lowers them; `r=1` repeats one value. Adjacent values in a merged list need not share that ratio.
3. **Possible applications**: Brown's article draws on scale values for type sizes, line height, line length, margins and column widths. A project may choose independent or optical values where they fit better.
4. **Declared starting values**: A strand needs a positive base. Brown's example starts with a tested body-text size and a second important number; that typeface-first choice is his contextual method, not a universal requirement.
5. **Can be multi-stranded**: Brown describes using two starting numbers or two starting ratios and combining the resulting scales. The sorted union provides additional options, but need not be geometric or guarantee visual or auditory harmony.

# Construction / Recognition

## To Construct/Create:
1. Declare a positive base `a>0` and ratio `r>0` for each strand. Brown's example starts from 18px after testing Minion body text; this is a contextual choice, not a required base-selection method.
2. Choose a ratio if a ratio-generated strand serves the design context; Brown's example uses `1:1.618`, whose decimal multiplier 1.618 approximates the golden ratio.
3. For the independent base-18 example at `r = 1.618`, calculate from the base: `18*r = 29.124` and `18*r² = 47.123` after half-even rounding to three decimals. Do not reuse rounded terms as the next input.
4. For this independent calculation from the exact base, divide by successive powers of the selected ratio; at `r = 1.618`, `18/r` rounds to `11.125` to three decimals. Brown's separate printed example for base 10 reports `3.819` and `2.360` descending; those are retained as his printed values, not verified recalculations.
5. Optionally: introduce a second important number (e.g., a large headline size) to create a double-stranded scale, merging both sequences in ascending order.
6. Consider values for the measurements where the chosen scale helps; Brown also describes trying alternatives and improvising when the scale values do not suit the composition.

## To Identify/Recognise:
1. For a claimed single strand, compare successive values with its declared ratio. In a sorted multi-strand list, adjacent values need not share one multiplier.
2. Check if the designer's stylesheet comments reference a ratio and a starting size (e.g., "18px @ 1:1.618").
3. Check which CSS values Brown identifies as scale-derived, and distinguish them from his independent, optical or improvised values.

# Context & Application

- **Typical contexts**: Brown demonstrates modular-scale use in web typography. Other media and projects may use proportional values where they serve the task; this card does not establish a universal method for them.
- **Common applications**: Setting font-size hierarchy (body, caption, h3, h2, h1, display); deriving column widths and margins from the same ratio as type sizes; establishing line-height relationships.
- **Historical/stylistic notes**: Brown quotes Robert Bringhurst's description of modular scales and gives a Renaissance-related rationale for his own golden-ratio example. This article does not establish concept priority or independently verify the cited book history. Brown built modularscale.com as a computational tool.
- **Tool reference**: modularscale.com (Tim Brown's calculator, not a concept in itself).

## Cross-Domain Connections

**Music → SHARED CONSTRUCTION**: Brown quotes Bringhurst's comparison of a modular scale to a musical scale and uses a selected ratio as a typographic multiplier. A particular musical interval ratio can therefore be reused in one typographic strand. This does not mean every musical scale has a single constant adjacent ratio, nor that auditory harmony establishes visual harmony.

**Mathematics → RIGOROUS WITHIN A STRAND**: With declared positive base `a>0` and ratio `r>0`, one strand has exact terms `a*r^n` for integer `n`, with adjacent indexed quotient `v[n+1]/v[n]=r`. A sorted union of strands is a separate construction and need not itself be geometric.

# Examples

**Example 1** (Brown's contextual example, "Creating a modular scale for web design"): After testing Minion, Brown chose 18px for body text and decimal ratio `1.618`, which approximates the golden ratio. He added 190px as a second important number for the `h2`. The source reports scale-associated values including 29.124px `h1`, 497.406px main column, 845.479px container and margins 44.856px, 27.723px and 29.124px. These are historical example values, not defaults or independently recalculated values.

**Example 2** (source transcription, "Modular scales and how they apply to web design"): Brown prints the base-10 sequence as `10.000, 16.180, 26.179, 42.358` ascending and `10.000, 6.180, 3.819, 2.360` descending using decimal ratio `1.618`. These descending printed values are preserved as the article's report. Independent calculation from exact base 10 and `r=1.618`, rounded half-even to three places, gives `2.361, 3.820, 6.180, 10.000, 16.180, 26.179, 42.358`.

# Relationships

## Builds Upon
- **Scale ratio** — An operational input to each ratio-generated strand; a multi-strand construction may use more than one ratio.
- **Base unit** — A positive starting value is an input to a strand; Brown's example chooses one for its project context.

## Enables
- **Scale application to typographic hierarchy** — Brown uses scale values when setting type sizes; selecting values from a scale is one available approach.
- **Typographic rhythm via modular scale** — Scale values can be used to coordinate selected measurements; Brown also documents independent and optical adjustments.
- **Modular scale construction (procedure)** — The procedure is the operationalisation of this concept.

## Related
- **Golden ratio** — Brown's historically contextual choice for the Minion/Renaissance web example; not a default for other projects.
- **Musical intervals as ratio sources** — A selected interval ratio can be reused as a strand multiplier; that shared construction does not transfer an auditory harmony judgment.

## Contrasts With
- **Arbitrary measurement** — Selecting sizes from convenient or habitual values (multiples of 10, viewport fractions, guesses) without proportional logic.
- **Additive/arithmetic progressions** — Sequences that increase by a fixed amount (e.g., 10, 14, 18, 22) rather than multiplying by one common ratio within a strand.

# Common Errors

- **Error**: Treating a modular scale as a requirement that all measurements come from it.
  **Correction**: Brown demonstrates applying selected scale values across several measurements, while also endorsing improvisation. Choose fixed, independent, fluid or optical values when they better fit the project.

- **Error**: Treating scale values as inviolable and forcing every measurement to match exactly, even when the result looks wrong.
  **Correction**: Tim Brown explicitly endorses improvisation: "Math is no substitute for an experienced designer's eye, but it can provide both hints and constraints for decision making. Consider the scale's numbers educated suggestions."

- **Error**: Building a scale without grounding the base number in a meaningful typographic decision.
  **Correction**: Brown starts with a body-text size that suits his selected typeface and design. That is one contextual method; a project may have fixed inputs or choose other values.

# Common Confusions

- **Confusion**: A modular scale is the same as an arbitrary list of "nice" type sizes.
  **Clarification**: Values in one declared strand follow repeated multiplication by its ratio. A multi-strand scale combines such strands; its adjacent sorted values need not share one ratio. A list chosen independently is not a geometric strand merely because its values look orderly.

- **Confusion**: The scale only applies to font sizes.
  **Clarification**: Brown's example applies selected scale values to type sizes, widths and margins, but also uses a 15px sidebar size and 20px optical margin outside the scale. These are examples of one approach, not universal measurement rules.

- **Confusion**: You must use a value from the scale for every CSS measurement.
  **Clarification**: Brown explicitly improvises (e.g., 15px sidebar font-size, 20px optical-alignment margin) and documents "comment math" showing when and how he combines or departs from scale values.

# Source Reference

"Modular scales and how they apply to web design"; "Creating a modular scale for web design"; "Applying a modular scale in web design" — More Meaningful Typography, Tim Brown (A List Apart, May 2011)

# Verification Notes

- Historical extraction note: The prior record quotes Brown's definition and Bringhurst's comparison and records the extractor's confidence as `high`. That confidence describes the extraction act; it is not current claim verification.
- Current scoped review: The prepared Brown article passages at lines 30, 109–189, 190–337 and 352–356 support the attributed definition, examples, contextual method and improvisation described above. The source prints descending base-10 values `3.819` and `2.360`; independent arithmetic from `r=1.618` yields different rounded values.
- Technical scope: One declared strand is geometric; a sorted multi-strand union is not generally so. No perceptual, readability, accessibility or universal harmony result is inferred.
- Relationships and questions: See this card's preserved relation/CQ lists; source-supported directional interpretations, editorial dependencies and unresolved endpoint warrant are itemized in the Slice12 batch record.
- Limits: Prepared text is readable and locally mapped, but immutable capture identity, conversion lineage and original-to-prepared fidelity remain unresolved. CDC independent review is pending. The old OCR observation remains attributed to the prior extraction; it does not establish source fidelity.
