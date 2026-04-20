---
# === CORE IDENTIFICATION ===
concept: Rules and Borders
slug: rules-and-borders

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
section: "Rules and Borders"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "lines and boxes"
  - "horizontal rules"
  - "dividers"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - body-text
extends: []
related:
  - tables
  - headings
  - typewriter-habits
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "border"
    example: "hr { border: none; border-top: 0.5pt solid #333; } /* classic half-point rule */"
    support: baseline
---

# Quick Definition

Rules (lines) and borders (boxes) should be used sparingly and thinly (0.5-1pt) — space above and below often works better, thick borders are "chartjunk" that upstages the data, and never make rules from repeated characters.

# Core Definition

Butterick defines: "In traditional printing terminology, a rule is a line; a border is a box." Both should be used sparingly: "Do you really need a rule or border to make a visual distinction? You can usually get equally good results by increasing the space above and below the text."

For borders: "Set the thickness between half a point and one point." Thicker borders "create noise that upstages the information inside. You want to see the data, not the lines around the data."

He cites Edward Tufte's concept of "chartjunk" — "markings that are unnecessary to communicate visual information."

# Prerequisites

- **Body Text** — Rules and borders organize body text elements.

# Key Properties

1. **Use sparingly**: Try space above/below first.
2. **0.5-1pt thickness**: For borders around content.
3. **No patterns**: "Don't use patterned borders (dots, dashes, double lines)."
4. **Rules have more latitude**: Can be thicker than borders since they don't accumulate.
5. **Heading rules above**: "Try putting it above the heading (rather than below)" to separate sections correctly.
6. **Never from characters**: "Never make rules and borders out of repeated typographic characters."
7. **Chartjunk**: Thick grid lines are unnecessary visual noise.

# Construction / Recognition

## To Construct/Create:
1. First try space above/below instead of a rule.
2. If a rule is needed, use 0.5-1pt solid line.
3. For tables, start with no borders and add back selectively.
4. For heading rules, place above the heading.

## To Identify/Recognise:
1. Chartjunk: thick borders that draw attention away from content.
2. Clean rules: thin, subtle lines that organize without dominating.

# Examples

**Example 1** (rules-and-borders): Same table with thick borders (wrong/cluttered) vs. thin borders (right/clean).

**Example 2** (rules-and-borders): Heading rules — placing the rule above separates the previous section from the current heading, not the heading from its own content.

# Relationships

## Builds Upon
- **Body Text** — Rules and borders organize body text.

## Related
- **Tables** — Table formatting is the primary context for border decisions.
- **Headings** — Rules can supplement heading hierarchy.
- **Typewriter Habits** — Making rules from repeated characters is a typewriter habit.

# Common Errors

- **Error**: Using thick borders around every table cell.
  **Correction**: "Thicker borders are counterproductive — they create noise that upstages the information inside." Use 0.5-1pt or no borders.

# Common Confusions

- **Confusion**: More visible borders make tables easier to read.
  **Clarification**: The opposite is usually true. Data creates its own visual grid; heavy borders obscure rather than clarify.

# Source Reference

"Rules and Borders" page. "Page Layout" chapter.

# Verification Notes

- Definition source: Direct quotes from rules-and-borders.md.
- Confidence rationale: High — clear thickness guidelines and Tufte reference.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
