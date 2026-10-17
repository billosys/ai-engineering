---
concept: "First-Line Indent"
slug: "first-line-indent"
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
section: "First-Line Indents"
extraction_confidence: "high"
aliases:
  - "paragraph indent"
  - "text indent"
prerequisites:
  - "body-text"
  - "point-size"
extends: []
related:
  - "paragraph-spacing"
  - "line-length"
contrasts_with:
  - "paragraph-spacing"
answers_questions:
  - "CQ 13: How does the relationship between inter-group and intra-group spacing communicate which elements belong together (gestalt proximity)?"
rosetta_stone: []
css_implementation:
  -
    property: "text-indent"
    example: "p + p { text-indent: 1em; } /* 1-4x point size; not on first paragraph */"
    support: "baseline"
---

# Quick Definition

A first-line indent can signal a new paragraph. Butterick suggests one to four times the type size and often treats it as an alternative to paragraph spacing; these are contextual recommendations, not universal minima or a ban on combining treatments.

# Core Definition

Butterick explains: "A first-line indent is the most common way to signal the start of a new paragraph. The other common way is with space between paragraphs." The critical constraint: Butterick’s belt-and-suspenders analogy recommends a single default treatment. It is advice, not an incompatibility theorem; a deliberate combination may serve a specific hierarchy.

Butterick suggests an indent from one to four times the point size and says to adjust for text-block width. This is his prose recommendation, not a universal minimum or script-independent rule.

# Prerequisites

- **Body Text** — First-line indent is a body text paragraph treatment.
- **Point Size** — Butterick relates the suggested indent to nominal point size; size and visibility still depend on the font and text-block width.

# Key Properties

1. **Attributed range**: Butterick suggests 1–4 times the point size, adjusted for text-block width; it is not a script-independent requirement.
2. **Alternative treatment**: The source generally favors indent or paragraph spacing, not a universal prohibition on combining them.
3. **Optional on first paragraph**: "A first-line indent on the first paragraph of any text is optional."
4. **Width-sensitive**: Narrow text blocks need smaller indents; wider blocks need larger.
5. **Use formatting, not spaces**: Don't use word spaces or tabs to create indents.

# Construction / Recognition

## To Construct/Create:
1. Set via paragraph formatting (not tabs or spaces).
2. Choose indent size: 1-4x the point size, adjusted for text block width.
3. Butterick says a first-paragraph indent is optional.
4. Choose indent, paragraph spacing or a deliberate combination for the content.

## To Identify/Recognise:
1. Too small: indent is barely visible.
2. Too large: first line seems disconnected from the left margin.

# Context & Application

- **Typical contexts**: Books, long-form documents, academic papers.
- **Common applications**: Paragraph separation in continuous prose.

# Examples

**Example 1** (first-line-indents): Butterick compares .3em, 2.5em and 1em for one particular text-block width; this does not establish that 2.5em always fails.

**Example 2** (first-line-indents): "Don't use word spaces or tabs to indent the first line — that's not what they're for."

# Relationships

## Builds Upon
- **Body Text** — A paragraph treatment for body text.
- **Point Size** — Indent size is relative to point size.

## Contrasts With
- **Paragraph Spacing** — Contrasting default treatments in Butterick’s advice; not a universal incompatibility.

## Related
- **Line Length** — Review indent against the actual text-block width and passage.

# Common Errors

- **Error**: Applying a repeated tab or space as paragraph indentation.
  **Correction**: Use paragraph formatting such as CSS `text-indent`; consider the content and chosen separation treatment.

# Common Confusions

- **Confusion**: The 0.5-inch indent is a standard size.
  **Clarification**: Butterick’s suggested 1–4× range and the text-block width are contextual considerations; 0.5 inches is not a universal standard.

# Source Reference

"First-Line Indents" page. "Page Layout" chapter.

# Verification Notes

- Claim review: source advice is attributed and scoped; the technical corrections in this assigned card are summarized in the changed teaching above.
- Source basis: the prepared Practical Typography page named in Source Reference was read. Extraction confidence is provenance, not a current technical proof.
- Technical review: relevant CSS behavior was checked against the cited primary specifications. No browser, assistive-technology, font-failure or readability study was run.
- Source-fidelity limit: P10-11 original capture and conversion-fidelity evidence remains open.
- Relationship and competency-question contribution is reconciled in Slice19 batch record; this does not establish whole-card endpoint review or full-corpus closure.
