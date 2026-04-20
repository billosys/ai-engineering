---
# === CORE IDENTIFICATION ===
concept: Font Pairing
slug: font-pairing

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
section: "Mixing Fonts"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "mixing fonts"
  - "font combination"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - font
  - body-text
extends: []
related:
  - headings
  - typographic-emphasis
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 26: How do you evaluate and select a typeface pairing for a web application? What properties should contrast, and what should harmonise?"
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []
css_implementation: []
---

# Quick Definition

Font pairing is the art of combining fonts in a document — limited to two (rarely three), with each font assigned a consistent role, and with the understanding that lower contrast between fonts can be more effective than high contrast.

# Core Definition

Butterick frames it as optional: "Mixing fonts is never a requirement — it's an option. You can get plenty of mileage out of one font using variations based on point size, bold or italic, small caps, and so on."

Key principles: "The rule of diminishing returns applies. Most documents can tolerate a second font. Few can tolerate a third. Almost none can tolerate four or more."

On the serif/sans-serif myth: "If you've heard that you can only mix a serif font with a sans serif font, it's not true. On the contrary, much like mixing colors, lower contrast between fonts can be more effective than higher contrast."

A reliable method: "combine fonts by the same font designer."

# Prerequisites

- **Font** — Understanding what fonts are before combining them.
- **Body Text** — Font pairing decisions center on body text.

# Key Properties

1. **Optional**: One font with variations is sufficient.
2. **Diminishing returns**: Two fonts max; three at most; four never.
3. **Consistent roles**: "Most successful when each font has a consistent role."
4. **Low contrast can work**: Serif + serif is fine (e.g., newspapers).
5. **Same-designer trick**: Fonts by the same designer pair reliably.
6. **One font per paragraph**: "It rarely works to have multiple fonts in a single paragraph."

# Construction / Recognition

## To Construct/Create:
1. Start with one font for body text.
2. If needed, add a second font for a specific role (headings, captions, etc.).
3. Consider fonts by the same designer for reliable pairing.
4. Change fonts only at paragraph breaks.
5. Ensure the two fonts are "identifiably different."

## To Identify/Recognise:
1. Good pairing: each font has a clear, consistent role.
2. Bad pairing: fonts compete or feel random.

# Examples

**Example 1** (mixing-fonts): "Look at any American newspaper — typically, the body text and the headlines are both in serif fonts, but different ones." Low-contrast pairing works.

**Example 2** (mixing-fonts): Role-based pairing: "one font for things in the center of the document (body text and headings) and one font for things at the edges (line numbers, footer)."

# Relationships

## Builds Upon
- **Font** — Pairing requires understanding of individual fonts.
- **Body Text** — Pairing decisions start with the body text font.

## Related
- **Headings** — The most common reason for a second font.
- **Typographic Emphasis** — Single-font emphasis often eliminates the need for pairing.

# Common Errors

- **Error**: Using three or more fonts in a single document.
  **Correction**: "Few can tolerate a third. Almost none can tolerate four or more."

# Common Confusions

- **Confusion**: You must pair a serif with a sans serif.
  **Clarification**: "It's not true. Lower contrast between fonts can be more effective than higher contrast."

# Source Reference

"Mixing Fonts" page. "Text Formatting" chapter.

# Verification Notes

- Definition source: Direct quotes from mixing-fonts.md.
- Confidence rationale: High — six explicit principles.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
