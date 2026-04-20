---
# === CORE IDENTIFICATION ===
concept: Justified Text
slug: justified-text

# === CLASSIFICATION ===
category: typography
subcategory: type-formatting
tier: intermediate
layer: 2-domain

# === PROVENANCE ===
source: "Butterick's Practical Typography"
source_slug: practical-typography
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Justified Text"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "full justification"
  - "justified alignment"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - body-text
  - line-length
extends: []
related:
  - hyphenation
  - line-spacing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "text-align"
    example: "p { text-align: justify; hyphens: auto; } /* always pair with hyphenation */"
    support: baseline
---

# Quick Definition

Justified text aligns both left and right edges by adjusting word spacing — a matter of personal preference, not a professional requirement, but it always requires hyphenation and works better in professional layout programs than word processors.

# Core Definition

Butterick defines: "Justified text is spaced so the left and right sides of the text block both have a clean edge." It "works by adding white space between the words in each line so all the lines are the same length."

The key constraint: "If you're using justified text, you must also turn on hyphenation to prevent gruesomely large spaces between words."

Importantly: "Justification is a matter of personal preference. It is not a signifier of professional typography." And: "if I'm making a word-processor document or web page, I'll always left-align the text, because justification can look clunky and coarse."

# Prerequisites

- **Body Text** — Justification is a body text alignment choice.
- **Line Length** — Justification requires adequate line length to distribute space.

# Key Properties

1. **Personal preference**: "Not a signifier of professional typography."
2. **Requires hyphenation**: Mandatory to prevent large word gaps.
3. **Tool-dependent quality**: "The justification engine of a word processor or web browser is rudimentary compared to that of a professional page-layout program."
4. **Word spacing only**: "Put it between the words" — never distribute extra space between characters.
5. **Left-align as default**: Butterick prefers left-aligned text for word processors and web.

# Construction / Recognition

## To Construct/Create:
1. Set text alignment to justified.
2. Turn on hyphenation (mandatory).
3. Ensure adequate line length (justification fails on narrow columns without hyphenation).
4. In high-end programs: distribute space between words only, not characters.

## To Identify/Recognise:
1. Clean edges on both sides of the text block.
2. Poor justification: visible "rivers" of white space through the paragraph.

# Examples

**Example 1** (justified-text): Justified text with and without hyphenation — without hyphenation, "gruesomely large spaces between words."

**Example 2** (justified-text): "Most major U.S. newspapers and magazines use a mix of justified and left-aligned text. Books, on the other hand, tend to be justified."

# Relationships

## Builds Upon
- **Body Text** — Justification is a body text formatting choice.
- **Line Length** — Adequate width needed for good justification.

## Related
- **Hyphenation** — Mandatory companion to justification.
- **Line Spacing** — Part of the overall body text formatting system.

# Common Errors

- **Error**: Using justified text without hyphenation.
  **Correction**: "You must also turn on hyphenation to prevent gruesomely large spaces between words."

# Common Confusions

- **Confusion**: Justified text is more professional than left-aligned.
  **Clarification**: "Justification is a matter of personal preference. It is not a signifier of professional typography."

# Source Reference

"Justified Text" page. "Page Layout" chapter.

# Verification Notes

- Definition source: Direct quotes from justified-text.md.
- Confidence rationale: High — clear rules and explicit preference statement.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
