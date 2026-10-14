---
concept: "Scale Ratio"
slug: "scale-ratio"
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
    - "ratio"
    - "proportion"
    - "typographic ratio"
prerequisites: []
extends: []
related:
  - "modular-scale"
  - "golden-ratio"
  - "perfect-fourth-ratio"
  - "perfect-fifth-ratio"
  - "ratio-selection-criteria"
contrasts_with: []
answers_questions:
  - "Why must visual scales be geometric (multiplicative) rather than arithmetic (additive)?"
  - "How do you select an appropriate scale ratio for a given design context?"
rosetta_stone:
  -
    domain: "music"
    concept: "Interval ratio — the frequency ratio between two tones defining a musical interval (e.g., 3:2 for a perfect fifth)"
    rating: "rigorous"
    note: "Typographic scale ratios derived from musical intervals carry identical numeric values. The ratio 4:3 (perfect fourth) applied to frequencies produces a musical interval; applied to type sizes produces a scale step. Same number, different domain."
  -
    domain: "mathematics"
    concept: "Common ratio of a geometric sequence"
    rating: "rigorous"
    note: "For one declared geometric strand, the scale ratio is its common ratio r. These mathematical properties apply to that strand, not generally to the adjacent values of a merged multi-strand list."
css_implementation:
  -
    property: "font-size (computed from ratio)"
    example: "/* Base 18px, ratio 1.618 */ font-size: 18px; /* step 0 */ font-size: 29.124px; /* step 1: 18 × 1.618 */ font-size: 47.123px; /* step 2: 18 × 1.618² */"
    support: "baseline"
---

# Quick Definition

A scale ratio is the declared multiplier `r>0` in one strand `v[n]=a*r^n` with `a>0`. In declared index order, `v[n+1]=v[n]*r` and `v[n+1]/v[n]=r`; when `r>1`, values rise as `n` increases, when `0<r<1` they fall, and `r=1` repeats the same value. “Up” and “down” describe value direction, which depends on `r`, not index direction alone. A construction with several strands can have more than one declared ratio.

# Core Definition

For one strand, a positive base `a>0` and ratio `r>0` determine exact values `v[n]=a*r^n` for integer `n`, and adjacent indexed terms satisfy `v[n+1]/v[n]=r`. Brown writes: "You start with a ratio (for example, 1:1.618) and a number (like 10), then multiply and divide to get many resonant numbers." In a multi-strand construction, each strand has its own inputs; adjacent values in the sorted union do not generally share one ratio.

A ratio expresses a proportion between two quantities. Brown uses notation such as `1:1.618`, where the left term is 1 and the right term is the multiplier. The decimal `1.618` represents the multiplier; it approximates, but is not equal to, the golden ratio. For `r>1`, each next indexed value is larger than the previous; for `0<r<1` it is smaller, and `r=1` repeats it.

Brown explains why `1:1.618` felt meaningful for his Minion/Renaissance example, citing historical and cultural connections. That is his contextual rationale; the article does not establish that every project must choose a historically grounded ratio or that such a choice guarantees a better result.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. **Generative within one strand**: A declared positive base `a>0` and ratio `r>0` generate exact values `a*r^n` for integer steps `n`, with `v[n+1]/v[n]=r`. A multi-strand construction has separate inputs for each strand.
2. **Constant within a strand**: Exact adjacent indexed terms satisfy `v[n+1]/v[n]=r`; rounded displayed values may not yield exactly constant quotients. The adjacent sorted values of a multi-strand merge generally have different quotients.
3. **Contextual selection**: Begin with the content, hierarchy and constraints of the design context. Brown’s historical and cultural rationale for `1.618` is optional context for his example, not a universal selection rule.
4. **Step spacing within a strand**: For `r>1`, ratios nearer 1 produce smaller multiplicative increases between indexed steps than larger ratios. At `r=1` values repeat; for `0<r<1`, describe the factor and value direction explicitly. Suitability for a hierarchy depends on content and rendered results.

# Construction / Recognition

## To Construct/Create:
1. Identify the content, hierarchy and constraints that the scale is meant to serve. Cultural, historical or aesthetic associations may be considered when relevant; Brown’s 1.618 example is one contextual choice.
2. If using a geometric strand, declare its ratio for the project. Brown gives a contextual reason for his choice; he does not establish a universal preference for musical or geometric origins.
3. The ratio may be written as `1:N` where `N` is the multiplier. Decimal `1.333` approximates `4/3`; decimal `1.618` approximates φ; preserve exact `1.5 (=3:2)` for the perfect-fifth ratio.
4. Apply in declared indexed order: `v[n+1]=v[n]*r` and `v[n-1]=v[n]/r`. Value direction is ascending with increasing `n` only when `r>1`; it reverses for `0<r<1`, and `r=1` repeats a value.

## To Identify/Recognise:
1. In a claimed single strand, preserve declared index order and calculate `v[n+1]/v[n]`; dividing the larger value by the smaller discards direction and may return `1/r`.
2. Compare exact terms when asserting an exactly constant quotient; rounded displays may only approximate it. Do not use this test on a sorted multi-strand union as though it were one strand.
3. Check designer's CSS comments — Tim Brown's practice is to document the scale in the stylesheet header (e.g., "18px @ 1:1.618").

# Context & Application

- **Typical contexts**: Any modular scale construction; type hierarchy planning; spacing system design.
- **Common applications**: Selecting the ratio before building a modular scale; documenting the ratio in CSS comments so future designers can recreate the scale.
- **Historical/stylistic notes**: Brown explains his `1.618` choice through historical and cultural connections to his chosen typefaces and text. Other practitioners' ratio-selection rationales are outside the source passages reviewed here.

## Cross-Domain Connections

**Music → SHARED CONSTRUCTION**: A selected musical interval ratio such as `3:2` can be reused as the multiplier for one typographic strand. The numeric construction is shared; a musical scale as a whole is not thereby a geometric type strand, and auditory harmony does not establish visual harmony.

**Mathematics → RIGOROUS WITHIN ONE STRAND**: For a strand with declared positive base `a>0` and ratio `r>0`, exact values `a*r^n` have indexed quotient `v[n+1]/v[n]=r`. A merged multi-strand list generally does not inherit a common ratio across its adjacent sorted values.

# Examples

**Example 1** (Brown's contextual choice, "Creating a modular scale for web design"): Brown chose decimal ratio `1.618` for his Minion/Renaissance example and gives historical and cultural reasons connected to his selected typefaces and text. The decimal approximates, but is not exactly, the golden ratio `φ`; this example is not a universal recommendation.

**Example 2** (source transcription, "Modular scales and how they apply to web design"): Brown prints `2.360, 3.819, 6.180, 10.000, 16.180, 26.179, 42.358` for base 10 and ratio `1.618`. The downward printed figures are retained as source report. Independent calculation from the exact base and decimal ratio, rounded half-even to three places, gives `2.361, 3.820, 6.180, 10.000, 16.180, 26.179, 42.358`.

# Relationships

## Builds Upon
- (None in this source — the ratio is a primitive input to the scale system.)

## Enables
- **Modular scale** — A declared ratio generates one geometric strand. A modular construction may use separate strand inputs; visual scales may also use additive or independently selected values.
- **Modular scale construction (procedure)** — The ratio is an input to a ratio-generated construction, alongside its positive base; other visual scale choices may be additive or independent.

## Related
- **Golden ratio** — One specific, historically prominent scale ratio (1.618).
- **Perfect fourth ratio** — Decimal `1.333` approximates the exact ratio `4/3`, derived from music.
- **Perfect fifth ratio** — Exact ratio `1.5 (=3:2)`, derived from music.
- **Ratio selection criteria** — The guidelines for choosing an appropriate ratio.

## Contrasts With
- **Independent measurement choices** — Values selected without one shared geometric ratio; they may still suit a project's content, interaction or optical needs.

# Common Errors

- **Error**: Treating one ratio origin as required for every typographic scale.
  **Correction**: Brown explains the contextual reason for his choice. A project may use a geometric ratio when it helps, or select independent values when that construction does not suit its content or task.

- **Error**: Assuming a ratio alone guarantees a suitable hierarchy.
  **Correction**: Check the generated values with actual content and rendered type. The article's 1.618 example does not establish that ratio as suitable for other projects or contexts.

# Common Confusions

- **Confusion**: The ratio and the base number are interchangeable — it doesn't matter which you change.
  **Clarification**: Within one strand, changing the base scales every term by the same factor; changing the ratio changes the relative step size. In a multi-strand construction, record each strand's own inputs.

# Source Reference

"Modular scales and how they apply to web design"; "Creating a modular scale for web design" — More Meaningful Typography, Tim Brown (A List Apart, May 2011)

# Verification Notes

- Historical extraction note: The prior record synthesized Brown's procedural description, retained extraction confidence `high`, and marked the cross-reference “Verified.” These are historical extraction observations, not current source-fidelity or semantic-review results.
- Current scoped review: Prepared article lines 109–189 support Brown's contextual ratio example and ratio-and-number procedure. Independent calculations use exact decimal `1.618`; it approximates `φ`, not equals it.
- Answerability: The retained CQ asking why visual scales “must” be geometric has a false universal premise. They need not be; a geometric strand is one available construction. The retained ratio-selection CQ is answerable only as a contextual decision, not a universal rule.
- Relationships: The exact roster contains `golden-ratio` and `ratio-selection-criteria`; `perfect-fourth-ratio` and `perfect-fifth-ratio` have no exact slug endpoint. Preserve those two unresolved references for owner review; existence of other endpoints does not itself establish edge warrant.
- Limits: Prepared-source support is not original-source fidelity; capture identity, conversion lineage and original-to-prepared comparison remain unresolved. The old extraction-confidence value is unchanged. CDC independent review is pending.
