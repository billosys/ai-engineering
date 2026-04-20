---
# === CORE IDENTIFICATION ===
concept: First-Line Indent
slug: first-line-indent

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
section: "First-Line Indents"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "paragraph indent"
  - "text indent"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - body-text
  - point-size
extends: []
related:
  - paragraph-spacing
  - line-length
contrasts_with:
  - paragraph-spacing

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 13: How does the relationship between inter-group and intra-group spacing communicate which elements belong together (gestalt proximity)?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "text-indent"
    example: "p + p { text-indent: 1em; } /* 1-4x point size; not on first paragraph */"
    support: baseline
---

# Quick Definition

A first-line indent signals a new paragraph by indenting the first line between one and four times the point size — mutually exclusive with space between paragraphs (use one or the other, never both).

# Core Definition

Butterick explains: "A first-line indent is the most common way to signal the start of a new paragraph. The other common way is with space between paragraphs." The critical constraint: "First-line indents and space between paragraphs have the same relationship as belts and suspenders. You only need one to get the job done. Using both is a mistake."

The size range: "A first-line indent should be no smaller than the current point size, or else it'll be hard to notice. It should be no bigger than four times the point size, or else the first line will seem disconnected from the left edge."

# Prerequisites

- **Body Text** — First-line indent is a body text paragraph treatment.
- **Point Size** — Indent size is calculated relative to point size.

# Key Properties

1. **1-4x point size**: At 12pt, that's 12-48 points (0.17-0.67 inches).
2. **Belts and suspenders**: Never combine with space between paragraphs.
3. **Optional on first paragraph**: "A first-line indent on the first paragraph of any text is optional."
4. **Width-sensitive**: Narrow text blocks need smaller indents; wider blocks need larger.
5. **Use formatting, not spaces**: Don't use word spaces or tabs to create indents.

# Construction / Recognition

## To Construct/Create:
1. Set via paragraph formatting (not tabs or spaces).
2. Choose indent size: 1-4x the point size, adjusted for text block width.
3. Omit the indent on the first paragraph after a heading.
4. Do not add space between paragraphs if using first-line indent.

## To Identify/Recognise:
1. Too small: indent is barely visible.
2. Too large: first line seems disconnected from the left margin.

# Context & Application

- **Typical contexts**: Books, long-form documents, academic papers.
- **Common applications**: Paragraph separation in continuous prose.

# Examples

**Example 1** (first-line-indents): Three examples — indent too small (0.3em), too large (2.5em), and correct (1em).

**Example 2** (first-line-indents): "Don't use word spaces or tabs to indent the first line — that's not what they're for."

# Relationships

## Builds Upon
- **Body Text** — A paragraph treatment for body text.
- **Point Size** — Indent size is relative to point size.

## Contrasts With
- **Paragraph Spacing** — Mutually exclusive paragraph separation methods.

## Related
- **Line Length** — Indent size should account for effective line length.

# Common Errors

- **Error**: Using both first-line indent and space between paragraphs.
  **Correction**: "You only need one to get the job done. Using both is a mistake."

# Common Confusions

- **Confusion**: The 0.5-inch indent is a standard size.
  **Clarification**: The correct size depends on the point size (1-4x) and the width of the text block. 0.5 inches may be too large or too small depending on context.

# Source Reference

"First-Line Indents" page. "Page Layout" chapter.

# Verification Notes

- Definition source: Direct quotes from first-line-indents.md.
- Confidence rationale: High — explicit size range and clear rules.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
