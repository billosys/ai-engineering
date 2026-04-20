---
# === CORE IDENTIFICATION ===
concept: Block Quotation
slug: block-quotation

# === CLASSIFICATION ===
category: typography
subcategory: type-elements
tier: intermediate
layer: 2-domain

# === PROVENANCE ===
source: "Butterick's Practical Typography"
source_slug: practical-typography
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Block Quotations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "block quote"
  - "extract"
  - "long quotation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - body-text
  - point-size
  - line-spacing
extends: []
related:
  - first-line-indent
  - line-length
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "CQ 13: How does the relationship between inter-group and intra-group spacing communicate which elements belong together (gestalt proximity)?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "margin, font-size, line-height"
    example: "blockquote { margin: 1em 2em; font-size: 0.95em; line-height: 1.3; }"
    support: baseline
---

# Quick Definition

Block quotations are formatted by reducing point size and line spacing slightly, indenting 0.5-1 inch on the left (and optionally the right), and omitting quotation marks — but overuse is self-defeating because readers skip long quoted blocks.

# Core Definition

Butterick's formatting recipe: "Reduce the point size and line spacing slightly. Indent the text block between half an inch and a full inch on the left side, and optionally the same on the right. Or on the web, about 2-5 ems."

But he warns against overuse: "Block quotations sometimes become, like all caps, a form of self-defeating typography." The writer signals "this source is really important" but the reader receives "here's something long and dull... I can't be bothered to summarize it!" The reader's next thought: "Great — I can skip this."

# Prerequisites

- **Body Text** — Block quotations modify body text formatting.
- **Point Size** — Reduced slightly for the quotation.
- **Line Spacing** — Reduced slightly for the quotation.

# Key Properties

1. **Reduce size and spacing**: Slightly smaller point size and line spacing.
2. **Indent 0.5-1 inch**: Left side (optionally right); 2-5 ems on web.
3. **No quotation marks**: The indentation makes them redundant.
4. **Self-defeating if overused**: Long block quotes cause readers to skip.
5. **Edit and integrate**: Better to summarize and integrate than to dump long quotes.

# Construction / Recognition

## To Construct/Create:
1. Reduce point size slightly from body text.
2. Reduce line spacing proportionally.
3. Indent left side 0.5-1 inch (or 2-5em on web).
4. Optionally indent right side equally.
5. Remove quotation marks.
6. Keep block quotes as short as possible.

## To Identify/Recognise:
1. Indented text block with smaller type.
2. Overuse: long quoted passages that readers skip.

# Examples

**Example 1** (block-quotations): The self-defeating signal: writer thinks "This source is really important!" but reader thinks "Great — I can skip this."

# Relationships

## Builds Upon
- **Body Text** — Modifies body text formatting.
- **Point Size** — Uses reduced point size.
- **Line Spacing** — Uses reduced line spacing.

## Related
- **First-Line Indent** — Block quote indentation is a related spacing concept.
- **Line Length** — Indentation reduces effective line length.

# Common Errors

- **Error**: Using long block quotations as a substitute for summarizing.
  **Correction**: "If you want readers to pay attention to quoted material, edit it carefully and integrate it into the text."

# Common Confusions

- **Confusion**: Longer block quotations show more thorough research.
  **Clarification**: Long block quotes signal laziness to readers, not thoroughness. Readers skip them.

# Source Reference

"Block Quotations" page. "Page Layout" chapter.

# Verification Notes

- Definition source: Direct quotes from block-quotations.md.
- Confidence rationale: High — clear formatting recipe and usage warning.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
