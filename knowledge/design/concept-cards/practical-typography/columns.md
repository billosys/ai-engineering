---
# === CORE IDENTIFICATION ===
concept: Columns
slug: columns

# === CLASSIFICATION ===
category: layout-composition
subcategory: layout-patterns
tier: intermediate
layer: 2-domain

# === PROVENANCE ===
source: "Butterick's Practical Typography"
source_slug: practical-typography
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Columns"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "multi-column layout"
  - "newspaper columns"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - line-length
  - line-spacing
extends: []
related:
  - page-margins
  - paragraph-spacing
  - typographic-grids
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 7: What is a grid system, and what problem does it solve in visual composition?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "columns"
    example: "article { columns: 2; column-gap: 2em; }"
    support: baseline
---

# Quick Definition

Columns are an easy way to achieve shorter, more legible line lengths without large page margins — two or three columns work on a standard page (four is too many), but columns are less useful on the web where pages have no fixed bottom edge.

# Core Definition

Butterick endorses columns pragmatically: "Columns are an easy way to get a shorter and more legible line length without using large page margins." The constraint is simple: "On a standard 8.5″ × 11″ page, two or three columns are fine. Four is too many."

For professional results, align baselines across columns: "columns look neatest when the rows of text are aligned vertically between columns (i.e., as if they were sitting on the same baseline)." This requires ensuring that space between paragraphs is a whole multiple of the line spacing — "set space between paragraphs to zero, or set it to be the same as the line spacing."

On the web: "columns need to fit inside a fixed vertical space. But by its nature, a web page has an indefinite bottom edge." CSS columns work only for small amounts of text or link lists that fit on a single screen.

# Prerequisites

- **Line Length** — Columns exist to achieve better line length.
- **Line Spacing** — Baseline alignment across columns requires careful line spacing coordination.

# Key Properties

1. **Shortens line length**: Primary benefit — avoids overly wide text blocks.
2. **2-3 columns max**: On a standard page; four is too many.
3. **Baseline alignment**: Rows should align across columns for a neat appearance.
4. **Paragraph spacing constraint**: Must be zero or a whole multiple of line spacing to maintain baseline alignment.
5. **Print, not web**: CSS columns exist but are impractical for long content due to indefinite page height.

# Construction / Recognition

## To Construct/Create:
1. Choose 2 or 3 columns for a standard page.
2. Note the line spacing value.
3. Set paragraph spacing to zero or a whole multiple of line spacing.
4. Verify baseline alignment visually across columns.
5. On web, use only for short content that fits one screen.

## To Identify/Recognise:
1. Well-set columns: baselines align across columns; comfortable line length.
2. Poorly-set columns: rows drift out of alignment between columns due to non-multiple paragraph spacing.

# Context & Application

- **Typical contexts**: Long print documents, newsletters, reports.
- **Common applications**: Reducing line length on wide pages; newspaper-style layouts.
- **Historical note**: Multi-column layout is a newspaper convention adapted to word processors and desktop publishing.

# Examples

**Example 1** (columns): Two or three columns on an 8.5″ × 11″ page produce comfortable line lengths without large margins.

**Example 2** (columns): Baseline alignment requires paragraph spacing to be zero or equal to line spacing — the two most common options.

# Relationships

## Builds Upon
- **Line Length** — Columns are a mechanism for achieving optimal line length.
- **Line Spacing** — Baseline alignment requires line spacing awareness.

## Related
- **Page Margins** — An alternative way to shorten line length (wider margins vs. more columns).
- **Paragraph Spacing** — Must coordinate with line spacing for baseline alignment in columns.
- **Typographic Grids** — Columns are a basic grid structure.

# Common Errors

- **Error**: Using four or more columns on a standard page.
  **Correction**: "Four is too many." Stick to two or three on 8.5″ × 11″.

# Common Confusions

- **Confusion**: CSS columns work well for long-form web content.
  **Clarification**: "Columns need to fit inside a fixed vertical space. But by its nature, a web page has an indefinite bottom edge." Use only for short content that fits on one screen.

# Source Reference

"Columns" page. "Page Layout" chapter.

# Verification Notes

- Definition source: Direct quotes from columns.md.
- Confidence rationale: High — clear guidance on column count and baseline alignment.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to existing cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
