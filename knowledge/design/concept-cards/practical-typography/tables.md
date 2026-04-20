---
# === CORE IDENTIFICATION ===
concept: Tables
slug: tables

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
section: "Tables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "data tables"
  - "layout tables"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - body-text
extends: []
related:
  - rules-and-borders
  - typographic-grids
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 7: What is a grid system, and what problem does it solve in visual composition?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "display: grid / table"
    example: "td { padding: 0.3em 0.5em; border: none; } /* remove borders, add cell padding */"
    support: baseline
---

# Quick Definition

Tables are the best tool for gridded or complex layouts — but default formatting has two defects that must always be fixed: remove cell borders (start with none, add back selectively) and increase cell margins/padding.

# Core Definition

Butterick identifies tables as essential: "A table is usually the right solution for layout problems where white-space characters aren't up to the task." They serve two purposes: "spreadsheet-style grids of numbers" and "layouts where text needs to be positioned side-by-side."

Two mandatory formatting fixes:
1. **Cell borders**: "Turn off all the cell borders to start, and then turn them back on as needed." Default borders make tables "cluttered and difficult to read."
2. **Cell margins**: "The default cell margins, especially in Word, are too tight." Start around 0.03 inches and increase by 0.01 inch increments.

# Prerequisites

- **Body Text** — Tables contain and organize body text.

# Key Properties

1. **Remove borders first**: "The text in the cells will create an implied grid."
2. **Increase cell padding**: Default cell margins are too tight.
3. **Gentle increments**: "A little goes a long way — start around 0.03 inches."
4. **Asymmetric padding OK**: "Top and bottom margins can be bigger than side margins."
5. **CSS Grid alternative**: Modern web layouts can use CSS Grid instead of HTML tables.

# Construction / Recognition

## To Construct/Create:
1. Insert table with appropriate rows and columns.
2. Remove all cell borders.
3. Increase cell margins/padding from default.
4. Add borders back selectively where they improve legibility.
5. Consider CSS Grid for web layouts — "more flexible" than table markup.

## To Identify/Recognise:
1. Cluttered table: too many visible borders, tight cell margins.
2. Clean table: minimal borders, generous padding, content creates implied grid.

# Examples

**Example 1** (tables): Same data shown with full cell borders (cluttered) vs. no borders (clean) — the borderless version is more readable.

**Example 2** (tables): Same data with default tight cell margins (dense) vs. increased margins (not dense) — spacing dramatically improves legibility.

# Relationships

## Builds Upon
- **Body Text** — Tables organize body text and data.

## Related
- **Rules and Borders** — Table borders follow rule/border principles.
- **Typographic Grids** — Tables are a content-level grid implementation.

# Common Errors

- **Error**: Keeping default cell borders on all cells.
  **Correction**: "Turn off all the cell borders to start, and then turn them back on as needed."

# Common Confusions

- **Confusion**: Tables need visible borders to be readable.
  **Clarification**: "The text in the cells will create an implied grid. Cell borders can make the grid cluttered." Remove borders; rely on content alignment and cell padding.

# Source Reference

"Tables" page. "Page Layout" chapter.

# Verification Notes

- Definition source: Direct quotes from tables.md.
- Confidence rationale: High — two explicit formatting fixes with examples.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
