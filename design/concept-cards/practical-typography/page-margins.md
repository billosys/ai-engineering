---
# === CORE IDENTIFICATION ===
concept: Page Margins
slug: page-margins

# === CLASSIFICATION ===
category: layout-composition
subcategory: spacing-systems
tier: intermediate
layer: 2-domain

# === PROVENANCE ===
source: "Butterick's Practical Typography"
source_slug: practical-typography
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Page Margins"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "margins"
  - "page insets"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - line-length
extends: []
related:
  - body-text
  - typographic-grids
  - responsive-typography
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "CQ 7: What is a grid system, and what problem does it solve in visual composition?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "margin, padding, max-width"
    example: ".content { max-width: 65ch; margin: 0 auto; padding: 0 2rem; }"
    support: baseline
---

# Quick Definition

Page margins set the boundaries of the text block and are the primary mechanism for controlling line length — one inch is almost never enough for proportional fonts, and white space is a feature, not a flaw.

# Core Definition

Butterick states: "Page margins set the default territory your text occupies on the page. Because they determine the maximum width of the text block, page margins have the greatest effect on line length."

The one-inch default is inadequate: "Most word processors default to page margins of one inch... for proportional fonts, they're too small." At 12pt, "left and right page margins of 1.5-2.0 inches will usually give you a comfortable line length."

On "fear of white space": "A lot of mediocre typography results from a perceived need to fill space... Work outward from the text, not inward from the page edges."

# Prerequisites

- **Line Length** — Margins exist to produce correct line length.

# Key Properties

1. **Primary line-length control**: Greatest effect on text block width.
2. **One inch is not enough**: Default margins produce overly long lines.
3. **1.5-2.0 inches at 12pt**: Typical range for print.
4. **Focus on line length**: "Don't take that range as an absolute — focus on getting the number of characters per line into the right range."
5. **Don't fear white space**: "The pleasure of reading an effectively designed document will soon outweigh the unfamiliarity of extra white space."
6. **Margins can differ**: Top, bottom, left, right can all be different sizes. Asymmetric layouts are fine with at least 1 inch difference.
7. **Web too**: "Web pages need big margins too" — screen edges are not text boundaries.

# Construction / Recognition

## To Construct/Create:
1. Start from the line-length target (45-90 characters).
2. In print at 12pt: try 1.5-2.0 inch left/right margins.
3. On the web: use max-width on text containers, not just viewport edges.
4. For vertical centering: make bottom margin ~0.25 inches larger than top.

## To Identify/Recognise:
1. Lines over 90 characters: margins are too narrow.
2. Document feels cramped: increase margins.
3. Document feels wasteful: the text is actually more readable.

# Examples

**Example 1** (page-margins): The document exercise — Document A (1" margins, 12pt, double-spaced) vs. Document B (2" margins, 11pt, 15pt line spacing). B looks more professional AND contains equal or more words per page.

**Example 2** (page-margins): "Do any magazines run text in a single block on the page with one-inch margins? No — never." Professional publishing always addresses line length.

# Relationships

## Builds Upon
- **Line Length** — Margins are the primary tool for setting line length.

## Related
- **Body Text** — Margins frame the body text block.
- **Typographic Grids** — Margins define the grid's outer boundaries.
- **Responsive Typography** — Web margins must adapt to viewport width.

# Common Errors

- **Error**: Using one-inch margins as the default for all documents.
  **Correction**: "One inch is not enough" for proportional fonts. Increase to 1.5-2.0 inches (at 12pt) or whatever achieves 45-90 characters per line.

# Common Confusions

- **Confusion**: Larger margins waste space and reduce content per page.
  **Clarification**: Butterick demonstrates that smaller text + larger margins often yields equal or more words per page while looking more professional and being more comfortable to read.

# Source Reference

"Page Margins" page. "Page Layout" chapter.

# Verification Notes

- Definition source: Direct quotes from page-margins.md.
- Confidence rationale: High — explicit ranges with demonstration exercise.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
