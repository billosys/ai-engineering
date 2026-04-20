---
# === CORE IDENTIFICATION ===
concept: Typographic Emphasis
slug: typographic-emphasis

# === CLASSIFICATION ===
category: typography
subcategory: type-formatting
tier: intermediate
layer: 2-domain

# === PROVENANCE ===
source: "Butterick's Practical Typography"
source_slug: practical-typography
authors: "Matthew Butterick"
chapter: "Text Formatting"
chapter_number: null
pdf_page: null
section: "Bold or Italic"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "bold or italic"
  - "text emphasis"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - body-text
  - font
extends: []
related:
  - all-caps
  - small-caps
  - headings
  - typographic-color
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"
  - "CQ 19: A landing page hero section uses a 14px body font, a 16px heading, and a 14px subheading. Why does it feel like nothing stands out?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "font-weight, font-style"
    example: "em { font-style: italic; } strong { font-weight: bold; }"
    support: baseline
---

# Quick Definition

Typographic emphasis uses bold or italic — never both simultaneously — sparingly, because when everything is emphasized, nothing is emphasized.

# Core Definition

Butterick's two rules: "Bold or italic — think of them as mutually exclusive. That is rule #1." And "Rule #2: use bold and italic as little as possible. They are tools for emphasis. But if everything is emphasized, then nothing is emphasized."

The choice between bold and italic depends on the font type: "With a serif font, use italic for gentle emphasis, or bold for heavier emphasis." For sans serif: "skip italic and use bold for emphasis" because "most sans serif italic fonts just have a gentle slant that doesn't stand out on the page."

# Prerequisites

- **Body Text** — Emphasis is applied relative to the body text baseline.
- **Font** — Serif vs. sans serif determines the emphasis strategy.

# Key Properties

1. **Mutually exclusive**: Bold or italic, never both together.
2. **Use sparingly**: "If everything is emphasized, then nothing is emphasized."
3. **Serif strategy**: Italic for gentle emphasis, bold for heavier.
4. **Sans serif strategy**: Bold only — sans serif italics are too subtle.
5. **Roman is the baseline**: Unemphasized text is called *roman*.
6. **Not for long stretches**: "Bold and italic are fine for short bits of text, but not for long stretches."

# Construction / Recognition

## To Construct/Create:
1. Decide: does this need gentle or strong emphasis?
2. For serif: italic = gentle, bold = strong.
3. For sans serif: bold = all emphasis (skip italic).
4. Never combine bold and italic. Never underline bold text.
5. Keep emphasized passages short.

## To Identify/Recognise:
1. Overemphasis: whole paragraphs in bold or italic.
2. Double emphasis: bold italic text, or underlined bold.

# Context & Application

- **Typical contexts**: Body text where specific words or phrases need to stand out.
- **Common applications**: Key terms, foreign words (italic), warnings or labels (bold).

# Examples

**Example 1** (bold-or-italic): An "overemphasizer" who "won't hesitate to run the whole paragraph in bold type" — self-defeating because "it gives you nowhere to go when you need to emphasize a word."

**Example 2** (bold-or-italic): "Some fonts have both a bold style and a semibold style. You can use either for emphasis." Butterick prefers bold for greater contrast.

# Relationships

## Builds Upon
- **Body Text** — Emphasis contrasts with the body text baseline.
- **Font** — Serif vs. sans serif determines the approach.

## Related
- **All Caps** — Another emphasis option for short text.
- **Small Caps** — A subtler emphasis alternative.
- **Headings** — Heading hierarchy uses emphasis tools.
- **Typographic Color** — Bold creates darker color on the page.

# Common Errors

- **Error**: Running entire paragraphs in bold or italic.
  **Correction**: "This habit wears down your readers' retinas and their patience." Keep emphasis to short phrases.

# Common Confusions

- **Confusion**: Bold italic is stronger emphasis than bold alone.
  **Clarification**: Bold and italic are mutually exclusive tools. Combining them is not "more emphasis" — it's typographic noise.

# Source Reference

"Bold or Italic" page. "Text Formatting" chapter.

# Verification Notes

- Definition source: Direct quotes from bold-or-italic.md.
- Confidence rationale: High — two explicit rules with clear reasoning.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
