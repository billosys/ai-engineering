---
# === CORE IDENTIFICATION ===
concept: Paragraph Spacing
slug: paragraph-spacing

# === CLASSIFICATION ===
category: typography
subcategory: layout-spacing
tier: intermediate
layer: 2-domain

# === PROVENANCE ===
source: "Butterick's Practical Typography"
source_slug: practical-typography
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Space Between Paragraphs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "space between paragraphs"
  - "paragraph gap"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - body-text
  - point-size
extends: []
related:
  - first-line-indent
  - line-spacing
contrasts_with:
  - first-line-indent

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 13: How does the relationship between inter-group and intra-group spacing communicate which elements belong together (gestalt proximity)?"
  - "CQ 18: A card layout uses 16px padding inside cards, 16px between cards, and 16px between card title and body text. Everything feels 'flat.' What principle was violated, and what's the fix?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "margin-bottom"
    example: "p { margin-bottom: 0.75em; } /* 50-100% of body text size */"
    support: baseline
---

# Quick Definition

Paragraph spacing uses 50-100% of the body text size as vertical space between paragraphs — an alternative to first-line indent, never used simultaneously with it, and never created by inserting extra carriage returns.

# Core Definition

Butterick explains: "Space between paragraphs is an alternative to a first-line indent for signaling the start of a new paragraph." The size: "A space equal to 50-100% of the body text size will usually suffice."

Critical implementation note: "The worst way to put space between paragraphs is to insert an extra carriage return." Use the paragraph formatting controls instead.

Word processors collapse adjacent paragraph spacing: "the space between two paragraphs is the larger of the space after the first paragraph and the space before the second paragraph." Butterick prefers using space-after consistently.

# Prerequisites

- **Body Text** — Paragraph spacing is set relative to body text size.
- **Point Size** — Spacing is calculated as a percentage of the point size.

# Key Properties

1. **50-100% of body text size**: The recommended range.
2. **Mutually exclusive with indent**: Never combine with first-line indent.
3. **Never use carriage returns**: Use paragraph formatting controls.
4. **Word processors collapse**: Adjacent space-before and space-after use the larger value, not the sum.
5. **Prefer space-after**: More predictable behavior across paragraph boundaries.

# Construction / Recognition

## To Construct/Create:
1. In Word: Paragraph > Spacing > After.
2. In Pages: Format > Style > Spacing > After Paragraph.
3. In CSS: `margin-bottom` on paragraph elements.
4. Remove any first-line indent when using paragraph spacing.

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
- **First-Line Indent** — Mutually exclusive paragraph separation methods.

## Related
- **Line Spacing** — Both are vertical spacing controls but at different scales.

# Common Errors

- **Error**: Inserting extra carriage returns to create space between paragraphs.
  **Correction**: Use paragraph formatting controls (space after). Carriage returns create inconsistent spacing and layout problems.

# Common Confusions

- **Confusion**: Space-before and space-after are additive between paragraphs.
  **Clarification**: Word processors use the larger value, not the sum. 6pt after + 6pt before = 6pt between, not 12pt.

# Source Reference

"Space Between Paragraphs" page. "Page Layout" chapter.

# Verification Notes

- Definition source: Direct quotes from space-between-paragraphs.md.
- Confidence rationale: High — explicit percentage range and clear rules.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
