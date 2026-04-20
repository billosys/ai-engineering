---
# === CORE IDENTIFICATION ===
concept: Line Length
slug: line-length

# === CLASSIFICATION ===
category: typography
subcategory: type-formatting
tier: foundational
layer: 2-domain

# === PROVENANCE ===
source: "Butterick's Practical Typography"
source_slug: practical-typography
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Line Length"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "measure"
  - "line measure"
  - "column width"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - body-text
extends: []
related:
  - point-size
  - line-spacing
  - page-margins
  - responsive-typography
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "CQ 18: A card layout uses 16px padding inside cards, 16px between cards, and 16px between card title and body text. Everything feels 'flat.' What principle was violated, and what's the fix?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "max-width"
    example: "p { max-width: 65ch; } /* ~2.5 alphabets; within 45-90 char range */"
    support: baseline
---

# Quick Definition

Line length is the horizontal measure of a text block — optimally 45–90 characters per line (2–3 lowercase alphabets), with shorter lines being more comfortable to read.

# Core Definition

Butterick states: "Aim for an average line length of 45–90 characters, including spaces." He notes that "overly long lines are a common problem, but they're easy to correct."

The measure should be counted in characters per line, not inches or centimeters, because "the point size of the font affects the number of characters per inch. Whereas characters per line works at any point size."

A quick alternative: the alphabet test — "You should be able to fit between two and three alphabets on a line."

# Prerequisites

- **Body Text** — Line length is one of the four primary body text controls.

# Key Properties

1. **Optimal range**: 45–90 characters per line including spaces.
2. **Alphabet test**: 2–3 lowercase alphabets should fit on a line.
3. **Measured in characters**: Not inches — character count is font-size independent.
4. **Readability driver**: "Shorter lines are more comfortable to read than longer lines" because the eye must track vertically from line end to next line start.
5. **Set via margins**: Adjusted primarily through page margins, not paragraph indent.
6. **Web problem**: "The major flaw in many responsive web layouts? Insufficient attention to line length."

# Construction / Recognition

## To Construct/Create:
1. Set page margins so that body text falls within 45–90 characters per line.
2. Use word count to check: select a few lines and count characters with spaces.
3. Alternatively, type 2–3 lowercase alphabets — if they fit on one line, you're in range.
4. In CSS, use `max-width` with `ch` units (e.g., `65ch`).
5. Account for indented sections — they should also remain within the range.

## To Identify/Recognise:
1. Lines that feel exhausting to read are likely too long (>90 characters).
2. Lines that feel choppy or fragmented are likely too short (<45 characters).

# Context & Application

- **Typical contexts**: Every document and web page with running text.
- **Common applications**: Setting page margins; constraining text blocks on wide screens; responsive web layout design.

# Examples

**Example 1** (line-length): "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefgh = 2.31 alphabets" — a properly measured line.

**Example 2** (line-length): On responsive web design — insufficient line length control is the "major flaw" in many responsive layouts.

# Relationships

## Builds Upon
- **Body Text** — Line length is one of body text's four primary controls.

## Related
- **Point Size** — Affects how many characters fit per inch.
- **Line Spacing** — Longer lines need more line spacing for vertical tracking.
- **Page Margins** — The primary mechanism for controlling line length.
- **Responsive Typography** — Line length must adapt to viewport width.

# Common Errors

- **Error**: Using one-inch margins regardless of page size or font size.
  **Correction**: One-inch margins on letter-sized paper with a 12pt font often produce lines over 90 characters. Adjust margins to hit the 45–90 character target.

# Common Confusions

- **Confusion**: Measuring line length in inches or centimeters.
  **Clarification**: Characters per line is the correct metric. The same inch of text contains different character counts at different point sizes.

# Source Reference

"Line Length" page. "Page Layout" chapter.

# Verification Notes

- Definition source: Direct quotes from line-length.md.
- Confidence rationale: High — explicit character count ranges and clear heuristics.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
