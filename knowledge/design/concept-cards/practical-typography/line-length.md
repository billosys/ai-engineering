---
concept: "Line Length"
slug: "line-length"
category: "typography"
subcategory: "type-formatting"
tier: "foundational"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Line Length"
extraction_confidence: "high"
aliases:
  - "measure"
  - "line measure"
  - "column width"
prerequisites:
  - "body-text"
extends: []
related:
  - "point-size"
  - "line-spacing"
  - "page-margins"
  - "responsive-typography"
contrasts_with: []
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "CQ 18: A card layout uses 16px padding inside cards, 16px between cards, and 16px between card title and body text. Everything feels 'flat.' What principle was violated, and what's the fix?"
rosetta_stone: []
css_implementation:
  -
    property: "max-width"
    example: "p { max-width: 65ch; } /* illustrative width; count actual rendered text */"
    support: "baseline"
---

# Quick Definition

Line length is the horizontal measure of rendered text. Butterick suggests 45–90 characters including spaces, or roughly 2–3 lowercase alphabets, as a rule of thumb; measure representative text rather than treating it as a universal comfort test.

# Core Definition

Butterick states: "Aim for an average line length of 45–90 characters, including spaces." He notes that "overly long lines are a common problem, but they're easy to correct."

Butterick favors character counts over physical measures because type size affects characters per unit width. Actual line composition still depends on glyph advances, shaping, spaces, language, font fallback and writing mode; review the rendered passage.

A quick alternative: the alphabet test — "You should be able to fit between two and three alphabets on a line."

# Prerequisites

- **Body Text** — Line length is one of the four primary body text controls.

# Key Properties

1. **Source range**: Butterick suggests 45–90 characters including spaces.
2. **Approximate visual check**: His 2–3 lowercase alphabet comparison is a rule of thumb, not a cross-script test.
3. **Measure actual lines**: Counts depend on actual text, font, shaping, size, language and layout.
4. **Reading consideration**: Butterick favors shorter lines because of return-sweep effort; the effect depends on task and readers.
5. **Print method**: Butterick discusses page margins as a primary way to adjust print measure; web text blocks can use max-width or other layout constraints.
6. **Web problem**: "The major flaw in many responsive web layouts? Insufficient attention to line length."

# Construction / Recognition

## To Construct/Create:
1. Treat the 45–90 range as a starting point, not a universal target.
2. Count several actual rendered lines, including spaces.
3. Use the alphabet comparison only as Butterick’s Latin-script illustration; inspect the content’s actual language and writing mode.
4. CSS `ch` is based on the zero glyph advance (with specification fallbacks), not an average character. It can provide an approximate width; count and review real rendered lines.
5. Review indented passages separately; the suggested range is not a universal requirement.

## To Identify/Recognise:
1. Assess the actual passage and reading task; these character boundaries do not diagnose comfort by themselves.

# Context & Application

- **Typical contexts**: Every document and web page with running text.
- **Common applications**: Setting page margins; constraining text blocks on wide screens; responsive web layout design.

# Examples

**Example 1** (line-length): Butterick’s Latin alphabet illustration gives 2.31 alphabets for that line; it is not a cross-script measure or universal comfort test.

**Example 2** (line-length): On responsive web design — insufficient line length control is the "major flaw" in many responsive layouts.

# Relationships

## Builds Upon
- **Body Text** — Line length is one of body text's four primary controls.

## Related
- **Point Size** — Affects how many characters fit per inch.
- **Line Spacing** — Butterick relates line length and leading; review their interaction with the selected face and content.
- **Page Margins** — Butterick discusses margins for print measure; web layout may use text-container max-width or other constraints.
- **Responsive Typography** — Review measure as available width and content change; font size need not track viewport width.

# Common Errors

- **Error**: Using one-inch margins regardless of page size or font size.
  **Correction**: Use the source’s example as a contextual print observation; assess actual line breaks rather than assuming a universal 45–90 character requirement.

# Common Confusions

- **Confusion**: A width unit guarantees a character count.
  **Clarification**: Count actual rendered lines when the question concerns line length. `ch` is an approximate width, not a character-count guarantee.

# Source Reference

"Line Length" page. "Page Layout" chapter.

# Verification Notes

- Claim review: source advice is attributed and scoped; the technical corrections in this assigned card are summarized in the changed teaching above.
- Source basis: the prepared Practical Typography page named in Source Reference was read. Extraction confidence is provenance, not a current technical proof.
- Technical review: relevant CSS behavior was checked against the cited primary specifications. No browser, assistive-technology, font-failure or readability study was run.
- Primary definitions: CSS Values and Units [font-relative lengths §6.1.1](https://www.w3.org/TR/css-values-4/#font-relative-lengths), including the `ch` definition and fallback.
- Source-fidelity limit: P10-11 original capture and conversion-fidelity evidence remains open.
- Relationship and competency-question contribution is reconciled in Slice19 batch record; this does not establish whole-card endpoint review or full-corpus closure.
