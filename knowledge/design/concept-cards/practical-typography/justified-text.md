---
concept: "Justified Text"
slug: "justified-text"
category: "typography"
subcategory: "type-formatting"
tier: "intermediate"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Justified Text"
extraction_confidence: "high"
aliases:
  - "full justification"
  - "justified alignment"
prerequisites:
  - "body-text"
  - "line-length"
extends: []
related:
  - "hyphenation"
  - "line-spacing"
contrasts_with: []
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
rosetta_stone: []
css_implementation:
  -
    property: "text-align"
    example: "p { text-align: justify; hyphens: auto; } /* illustrative; Butterick recommends hyphenation for suitable prose; check language, resources and output */"
    support: "baseline"
---

# Quick Definition

Justified text aligns both edges by adjusting spacing. Butterick treats it as a preference, recommends hyphenation and favors left alignment for word-processor and web work; these are recommendations, not CSS validity rules or universal professional rankings.

# Core Definition

Butterick defines: "Justified text is spaced so the left and right sides of the text block both have a clean edge." It "works by adding white space between the words in each line so all the lines are the same length."

Butterick recommends hyphenation with justification to reduce conspicuous word gaps. Results depend on script, line measure, language data and the layout engine; setting a property alone does not guarantee useful hyphenation.

Importantly: "Justification is a matter of personal preference. It is not a signifier of professional typography." And: "if I'm making a word-processor document or web page, I'll always left-align the text, because justification can look clunky and coarse."

# Prerequisites

- **Body Text** — Justification is a body text alignment choice.
- **Line Length** — Measure affects spacing distribution; Butterick’s adequate-width advice is contextual.

# Key Properties

1. **Personal preference**: "Not a signifier of professional typography."
2. **Source recommendation**: Butterick recommends hyphenation to reduce conspicuous gaps; it is not a CSS validity condition.
3. **Tool-dependent output**: Butterick compares the engines available in his context; this card does not establish a current universal engine ranking.
4. **Spacing advice**: Butterick recommends putting expansion between words; actual justification behavior depends on script and engine.
5. **Left-align as default**: Butterick prefers left-aligned text for word processors and web.

# Construction / Recognition

## To Construct/Create:
1. Set text alignment to justified.
2. Consider hyphenation where suitable language resources are available and inspect the result.
3. Compare actual line measures and spacing.
4. Treat Butterick’s word-spacing preference as advice; engine behavior varies.

## To Identify/Recognise:
1. Clean edges on both sides of the text block.
2. Poor justification: visible "rivers" of white space through the paragraph.

# Examples

**Example 1** (justified-text): Justified text with and without hyphenation — without hyphenation, "gruesomely large spaces between words."

**Example 2** (justified-text): "Most major U.S. newspapers and magazines use a mix of justified and left-aligned text. Books, on the other hand, tend to be justified."

# Relationships

## Builds Upon
- **Body Text** — Justification is a body text formatting choice.
- **Line Length** — Available measure affects justification; review the actual text and engine output.

## Related
-  **Hyphenation** — Butterick recommends it with justification; actual support and breaks are conditional.
- **Line Spacing** — Part of the overall body text formatting system.

# Common Errors

- **Error**: Assuming a CSS alignment or hyphenation declaration guarantees typographic quality.
  **Correction**: Butterick recommends pairing justification with hyphenation; inspect the actual language- and engine-specific result.

# Common Confusions

- **Confusion**: Justified text is more professional than left-aligned.
  **Clarification**: "Justification is a matter of personal preference. It is not a signifier of professional typography."

# Source Reference

"Justified Text" page. "Page Layout" chapter.

# Verification Notes

- Claim review: source advice is attributed and scoped; the technical corrections in this assigned card are summarized in the changed teaching above.
- Source basis: the prepared Practical Typography page named in Source Reference was read. Extraction confidence is provenance, not a current technical proof.
- Technical review: relevant CSS behavior was checked against the cited primary specifications. No browser, assistive-technology, font-failure or readability study was run.
- Primary definitions: CSS Text [hyphenation §5.3](https://www.w3.org/TR/css-text-3/#hyphenation) is relevant to word breaking; this is not an engine comparison.
- Source-fidelity limit: P10-11 original capture and conversion-fidelity evidence remains open.
- Relationship and competency-question contribution is reconciled in Slice19 batch record; this does not establish whole-card endpoint review or full-corpus closure.
