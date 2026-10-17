---
concept: "Paragraph Spacing"
slug: "paragraph-spacing"
category: "typography"
subcategory: "layout-spacing"
tier: "intermediate"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Space Between Paragraphs"
extraction_confidence: "high"
aliases:
  - "space between paragraphs"
  - "paragraph gap"
prerequisites:
  - "body-text"
  - "point-size"
extends: []
related:
  - "first-line-indent"
  - "line-spacing"
contrasts_with:
  - "first-line-indent"
answers_questions:
  - "CQ 13: How does the relationship between inter-group and intra-group spacing communicate which elements belong together (gestalt proximity)?"
  - "CQ 18: A card layout uses 16px padding inside cards, 16px between cards, and 16px between card title and body text. Everything feels 'flat.' What principle was violated, and what's the fix?"
rosetta_stone: []
css_implementation:
  -
    property: "margin-bottom"
    example: "p { margin-bottom: 0.75em; } /* 50-100% of body text size */"
    support: "baseline"
---

# Quick Definition

Paragraph spacing can signal new paragraphs. Butterick suggests 50–100% of body text size and usually treats this as an alternative to first-line indent; these are recommendations to judge with the actual content and layout.

# Core Definition

Butterick explains: "Space between paragraphs is an alternative to a first-line indent for signaling the start of a new paragraph." Butterick suggests 50–100% of body text size as a source recommendation, not a required minimum across scripts and layouts.

Critical implementation note: "The worst way to put space between paragraphs is to insert an extra carriage return." Use the paragraph formatting controls instead.

Butterick describes how word processors in his source context handle adjacent paragraph spacing and prefers space-after. CSS adjacent positive block margins collapse only in specified conditions; gaps and other formatting contexts differ.

# Prerequisites

- **Body Text** — Paragraph spacing is set relative to body text size.
- **Point Size** — Butterick relates his suggested paragraph gap to body text size.

# Key Properties

1. **Attributed suggestion**: Butterick suggests 50–100% of body text size; judge the result in context.
2. **Alternative treatment**: Butterick advises against routinely combining paragraph gaps and first-line indents; context may justify a deliberate combination.
3. **Prefer paragraph styling**: It is usually easier to maintain than repeated blank paragraphs.
4. **Application-specific behavior**: Word’s description of adjacent paragraph spacing is not a universal CSS rule. Adjacent positive block margins collapse only under specified conditions; gaps and other formatting contexts differ.
5. **Prefer space-after**: More predictable behavior across paragraph boundaries.

# Construction / Recognition

## To Construct/Create:
1. In Word: Paragraph > Spacing > After.
2. In Pages: Format > Style > Spacing > After Paragraph.
3. In CSS: `margin-bottom` on paragraph elements.
4. Consider whether to use spacing, indentation or a deliberate combination.

## To Identify/Recognise:
1. Too little: paragraphs run together without clear separation.
2. Too much: paragraphs seem disconnected from each other.

# Examples

**Example 1** (space-between-paragraphs): Butterick recommends relying on space-after and using space-before only in special circumstances like block quotations.

# Relationships

## Builds Upon
- **Body Text** — A paragraph treatment for body text.
- **Point Size** — Spacing is a fraction of the point size.

## Contrasts With
- **First-Line Indent** — Common alternative paragraph separation treatments; the source recommends choosing one as a default.

## Related
- **Line Spacing** — Both are vertical spacing controls but at different scales.

# Common Errors

- **Error**: Inserting extra carriage returns to create space between paragraphs.
  **Correction**: Use paragraph formatting controls (space after). Carriage returns create inconsistent spacing and layout problems.

# Common Confusions

- **Confusion**: Adjacent paragraph margins always add or always collapse.
  **Clarification**: CSS margin collapse depends on block-flow conditions; a gap or other formatting context can produce a different result.

# Source Reference

"Space Between Paragraphs" page. "Page Layout" chapter.

# Verification Notes

- Claim review: source advice is attributed and scoped; the technical corrections in this assigned card are summarized in the changed teaching above.
- Source basis: the prepared Practical Typography page named in Source Reference was read. Extraction confidence is provenance, not a current technical proof.
- Technical review: relevant CSS behavior was checked against the cited primary specifications. No browser, assistive-technology, font-failure or readability study was run.
- Primary definitions: CSS 2.2 [collapsing margins §8.3.1](https://www.w3.org/TR/CSS22/box.html#collapsing-margins).
- Source-fidelity limit: P10-11 original capture and conversion-fidelity evidence remains open.
- Relationship and competency-question contribution is reconciled in Slice19 batch record; this does not establish whole-card endpoint review or full-corpus closure.
