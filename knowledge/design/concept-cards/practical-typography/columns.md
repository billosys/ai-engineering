---
concept: "Columns"
slug: "columns"
category: "layout-composition"
subcategory: "layout-patterns"
tier: "intermediate"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Columns"
extraction_confidence: "high"
aliases:
  - "multi-column layout"
  - "newspaper columns"
prerequisites:
  - "line-length"
  - "line-spacing"
extends: []
related:
  - "page-margins"
  - "paragraph-spacing"
  - "typographic-grids"
contrasts_with: []
answers_questions:
  - "CQ 7: What is a grid system, and what problem does it solve in visual composition?"
rosetta_stone: []
css_implementation:
  -
    property: "columns"
    example: "article { columns: 18rem; column-gap: 2em; } /* candidate width; check actual flow and reading order */"
    support: "baseline"
---

# Quick Definition

Columns divide a flow into narrower measures. Their number, width, gaps and reading path depend on the content and medium; they can support print or web composition without a universal column-count or fixed-height rule.

# Core Definition

Butterick recommends two or three columns on a standard 8.5″ × 11″ page and considers four too many in that setting. Preserve this as his print preference: four columns are not inherently invalid, and no count alone proves legibility.

For coordinated baselines he suggests paragraph gaps of zero or whole multiples of line spacing. This can support a baseline rhythm when line boxes, starting positions and layout are compatible; the arithmetic alone cannot guarantee alignment across different fonts, headings or fragmented content.

Butterick favors web columns for short text or link lists fitting one screen, arguing from the web page's indefinite bottom edge. A practical concern to assess is the travel down a long column before returning to the next. This is a usability concern and contextual preference, not a CSS requirement for finite fixed height. [CSS Multi-column Layout Level 1](https://www.w3.org/TR/css-multicol-1/#columns) lets width and count respond to available inline size. A requested width is flexible; used count and width, and the actual count after fragmentation, can differ from specified values.

# Prerequisites

- **Line Length** — Column width is one way to control measure; assess actual text.
- **Line Spacing** — Leading and line boxes matter when considering baseline coordination.

# Key Properties

1. **Measure**: Columns can shorten lines without enlarging the page's outer margins.
2. **Contextual count**: Butterick's two/three-column example is not a universal maximum.
3. **Optional baseline rhythm**: Compatible starts, line boxes and spacing matter in addition to paragraph-gap multiples.
4. **Adaptive geometry**: CSS width/count and gaps negotiate the available inline size.
5. **Reading path**: Prose ordinarily flows down a column before continuing to the next; inspect vertical travel, enlargement and navigation in the actual output.

# Construction / Recognition

## To Construct/Create:
1. Identify the content's reading sequence and available print or screen area.
2. Choose candidate width/count and gap; review actual measure rather than forcing a count.
3. If baseline alignment serves the task, coordinate line boxes, starts and paragraph spacing, then inspect the result.
4. Allow web column count to adapt; fixed block height is not a prerequisite.
5. Check enlarged text, fallback, column transitions and whether returning to the next column creates excessive travel.

## To Identify/Recognise:
1. A multi-column text flow continues through successive columns rather than treating each as an independent item.
2. Apparent baseline drift calls for inspecting the line boxes and starts as well as paragraph gaps.

# Context & Application

- **Typical contexts**: Print reports/newsletters, web text flows or link lists when their reading path suits the task.
- **Common applications**: Narrowing measures and coordinating repeated alignment tracks.
- **Historical note**: Butterick invokes newspaper baselines as an example; this does not establish the history of every column convention.

# Examples

**Example 1** (columns): Butterick's US-letter example prefers two or three columns over four. Font, content, gaps and margins still determine the resulting measure and appearance.

**Example 2** (columns): His zero-gap or one-line-gap paragraph options can preserve a baseline rhythm with compatible line boxes and starts. They do not alone prove alignment.

Analytic CSS illustration: assume horizontal text, a 16px root and element font, `columns: 18rem`, `column-gap: 2em`, auto count and a container content width with no further constraints or explicit column breaks. A 16rem container gives one 16rem used column; a 40rem container gives two 19rem used columns. The requested 18rem is not a fixed used width. This is specification arithmetic, not a browser witness, conformance result or fixed-height requirement.

# Relationships

## Builds Upon
- **Line Length** — Understanding measure helps choose a candidate column width; no optimal measure is guaranteed.
- **Line Spacing** — Understanding leading helps evaluate baseline coordination.

## Related
- **Page Margins** — Outer margins and interior columns both affect the space available for text measures.
- **Paragraph Spacing** — Gaps participate in baseline rhythm with compatible line boxes and starts; multiples alone are insufficient.
- **Typographic Grids** — Repeated column tracks can supply alignment references within a conceptual grid; not every grid is a multicol flow.

# Common Errors

- **Error**: Treating a two/three-column preference or paragraph-gap multiple as an invariant of good layout.
  **Correction**: Check content, measure, line boxes and reading path; retain justified counts and optical exceptions.

# Common Confusions

- **Confusion**: CSS columns require a finite fixed height and only work for one screen of content.
  **Clarification**: CSS supports adaptive columns without that prerequisite. Long flows still need an actual assessment of column transitions and excessive vertical travel.

# Source Reference

"Columns" page. "Page Layout" chapter.

# Verification Notes

- Available-source comparison: whole prepared columns.md; count/baseline examples and short-web-flow preference retained with attribution. Original capture/fidelity remains P10-11-blocked.
- Current support: CSS multicol width/count and used-size algorithm; the two examples are analytic under explicit assumptions, not rendered observations.
- Local outcome: two prerequisite and three related premises checked; CQ7 receives the column-track component of a grid definition/problem explanation, not complete global acceptance.
- Historical metadata, extraction confidence and earlier conversion/Rosetta observations are retained records, not current verification evidence. No uncertainty-free original comparison is available.
- Unrun: browser flow/enlargement, AT, hosted output and full-corpus reconciliation.
