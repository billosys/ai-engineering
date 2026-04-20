---
# === CORE IDENTIFICATION ===
concept: Ligatures
slug: ligatures

# === CLASSIFICATION ===
category: typography
subcategory: type-composition
tier: intermediate
layer: 2-domain

# === PROVENANCE ===
source: "Butterick's Practical Typography"
source_slug: practical-typography
authors: "Matthew Butterick"
chapter: "Type Composition"
chapter_number: null
pdf_page: null
section: "Ligatures"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "character ligatures"
  - "fi ligature"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - font
extends: []
related:
  - opentype-features
  - kerning
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 5: What are the basic anatomical parts of a letterform (baseline, x-height, cap height, ascender, descender, counter)?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "font-variant-ligatures / font-feature-settings"
    example: "body { font-variant-ligatures: common-ligatures; text-rendering: optimizeLegibility; }"
    support: baseline
---

# Quick Definition

Ligatures are combined letterforms that solve visual collisions between adjacent characters — mandatory only when f and i collide, otherwise a stylistic choice that Butterick generally keeps turned off.

# Core Definition

Butterick explains: "Ligatures were invented to solve a practical typesetting problem. In the days of metal fonts, certain characters had features that physically collided with other characters."

The modern rule: "The only time ligatures are mandatory is when you have an actual overlap between the letters f and i." Beyond that, "ligatures are largely a stylistic choice. To my eye, they can make body text look somewhat quaint or old-fashioned."

# Prerequisites

- **Font** — Ligatures are features of specific fonts.

# Key Properties

1. **f-i collision**: The primary mandatory use case.
2. **Mostly optional**: "Unless characters are actually colliding, I generally keep ligatures turned off."
3. **OpenType feature**: Activated via `liga` tag.
4. **Don't insert manually**: "Manual ligatures can confuse spelling checkers, hyphenation engines, and search indexers."
5. **Not always connecting**: "Ligatures don't always connect two glyphs — sometimes they create separation."

# Construction / Recognition

## To Construct/Create:
1. In Word: Font > Advanced > Ligatures > Standard Only.
2. In CSS: `font-variant-ligatures: common-ligatures` or `text-rendering: optimizeLegibility`.
3. Check bold and italic styles separately for fi collision.

## To Identify/Recognise:
1. Visual overlap between f and i (or f and other letters) = ligatures needed.
2. No overlap = ligatures optional.

# Examples

**Example 1** (ligatures): Font with fi collision (wrong) vs. same font with ligatures on (right).

# Relationships

## Builds Upon
- **Font** — Ligatures are font-specific features.

## Related
- **OpenType Features** — Ligatures are accessed as OpenType features.
- **Kerning** — Both address letter spacing issues.

# Common Errors

- **Error**: Manually inserting ligature characters.
  **Correction**: Use automated ligature features. Manual insertion "can confuse spelling checkers, hyphenation engines, and search indexers."

# Common Confusions

- **Confusion**: Ligatures should always be turned on.
  **Clarification**: Only mandatory for actual visual collisions (primarily fi). Otherwise, a stylistic choice.

# Source Reference

"Ligatures" page. "Type Composition" chapter.

# Verification Notes

- Definition source: Direct quotes from ligatures.md.
- Confidence rationale: High — clear mandatory/optional distinction.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
