---
# === CORE IDENTIFICATION ===
concept: Headings
slug: headings

# === CLASSIFICATION ===
category: typography
subcategory: type-elements
tier: intermediate
layer: 2-domain

# === PROVENANCE ===
source: "Butterick's Practical Typography"
source_slug: practical-typography
authors: "Matthew Butterick"
chapter: "Text Formatting"
chapter_number: null
pdf_page: null
section: "Headings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "headers"
  - "heading hierarchy"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - body-text
  - typographic-emphasis
  - point-size
extends: []
related:
  - all-caps
  - typographic-color
  - line-spacing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"
  - "CQ 19: A landing page hero section uses a 14px body font, a 16px heading, and a 14px subheading. Why does it feel like nothing stands out?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "font-size, font-weight, margin"
    example: "h2 { font-size: 1.1em; font-weight: bold; margin-top: 1.5em; margin-bottom: 0.5em; }"
    support: baseline
---

# Quick Definition

Headings are structural signposts that reveal argument structure — limited to two or three levels, emphasized subtly through space, bold, and small size increments rather than aggressive formatting like all caps, underlining, or doubling the point size.

# Core Definition

Butterick identifies two intertwined problems: "Headings present two problems: structural and typographic. Cure the structural problem and the typographic problem becomes simpler."

The structural fix: "Limit yourself to three levels of headings. Two is better." Too many levels lead to "increasingly desperate attempts to make them visually distinct."

Nine typographic parameters for headings:
1. Don't use all caps.
2. Don't underline.
3. Don't center.
4. "The best way to emphasize a heading is by putting space above and below."
5. Use bold, not italic.
6. "It's fine to make the point size bigger, but just a little. Use the smallest increment necessary."
7. Only two levels of indenting.
8. Suppress hyphenation in headings.
9. Use keep-with-next to prevent awkward breaks.

# Prerequisites

- **Body Text** — Headings supplement and contrast with body text.
- **Typographic Emphasis** — Headings use emphasis tools.
- **Point Size** — Heading size is relative to body text size.

# Key Properties

1. **Fewer levels**: Two or three maximum — "With more than three levels, that task becomes hopelessly confusing."
2. **Subtle emphasis**: "Use the smallest increment necessary to make a visible difference."
3. **Space is the best tool**: "Space above and below... is both subtle and effective."
4. **Bold over italic**: "For headings, bold is easier to read than italic."
5. **Small size increments**: "If your text is set in 12 point, you needn't go up to 14 or 15. Try 12.5 or 13."
6. **Modular scale skepticism**: Butterick rejects modular scale for heading sizes — "When your headings look right, they are right. The ratio is irrelevant."

# Construction / Recognition

## To Construct/Create:
1. Simplify your outline — aim for two levels of headings.
2. Add space above and below headings.
3. Optionally bold the heading text.
4. Increase point size by the smallest visible increment.
5. Suppress hyphenation; use keep-with-next paragraph.

## To Identify/Recognise:
1. Good headings: reader can orient themselves from headings alone.
2. Bad headings: "trainwrecks" of mixed formatting with too many levels.

# Context & Application

- **Typical contexts**: Reports, articles, books, web pages — any multi-section document.
- **Common applications**: Section structure, navigation, argument signposting.

# Examples

**Example 1** (headings): A "trainwreck" heading with excessive numbering, all caps, bold, underline, and indentation — "5(a)(1)(iv) The Target Market Has Expressed a Preference for Copious Banner Advertising."

**Example 2** (headings): "If you're using bold in your heading, you can also try *reducing* the point size by a half or full point" — subtlety works.

# Relationships

## Builds Upon
- **Body Text** — Headings exist relative to the body text.
- **Typographic Emphasis** — Headings use bold and size variation.
- **Point Size** — Size differentiation creates heading hierarchy.

## Related
- **All Caps** — Butterick advises against caps in headings.
- **Typographic Color** — Bold headings create color contrast.
- **Line Spacing** — Space above and below is the best heading emphasis.

# Common Errors

- **Error**: Using too many heading levels with increasingly desperate formatting.
  **Correction**: "Limit yourself to three levels of headings. Two is better." Simplify the structure first.

- **Error**: Doubling the point size for headings.
  **Correction**: "Use the smallest increment necessary to make a visible difference." Try 12.5pt or 13pt, not 14pt or 15pt.

# Common Confusions

- **Confusion**: Headings should be formatted as aggressively as possible to grab attention.
  **Clarification**: "Headings are signposts for readers that reveal the structure of your argument." Subtle, consistent formatting works better than aggressive treatment.

# Source Reference

"Headings" page. "Text Formatting" chapter.

# Verification Notes

- Definition source: Direct quotes from headings.md.
- Confidence rationale: High — nine explicit rules with clear reasoning.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
