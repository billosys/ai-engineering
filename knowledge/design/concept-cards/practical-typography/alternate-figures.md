---
# === CORE IDENTIFICATION ===
concept: Alternate Figures
slug: alternate-figures

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
section: "Alternate Figures"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "alternate numerals"
  - "figure styles"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - font
  - opentype-features
extends: []
related:
  - all-caps
  - body-text
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 5: What are the basic anatomical parts of a letterform (baseline, x-height, cap height, ascender, descender, counter)?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "font-variant-numeric"
    example: ".body { font-variant-numeric: oldstyle-nums proportional-nums; } .table { font-variant-numeric: lining-nums tabular-nums; }"
    support: baseline
---

# Quick Definition

Alternate figures are variant number designs — lining vs. oldstyle, tabular vs. proportional — that suit different typographic contexts: lining for caps, oldstyle for body text, tabular for aligned columns, proportional for running text.

# Core Definition

Butterick explains that figures present a design challenge because they "rely on shapes that are found nowhere in the uppercase and lowercase alphabets." Type designers address this with alternate figure sets.

Two independent axes: **lining vs. oldstyle** (height) and **tabular vs. proportional** (width). Lining figures "line up at the top and bottom" like caps; oldstyle figures "are designed to look more like lowercase letters." Tabular figures have fixed widths for column alignment; proportional figures have natural widths.

The defaults are always safe: "It's never wrong to use the default figures in your font."

# Prerequisites

- **Font** — Alternate figures are font-specific features.
- **OpenType Features** — Alternate figures are accessed as OpenType features.

# Key Properties

1. **Two axes**: Lining/oldstyle (height) and tabular/proportional (width).
2. **Four combinations**: Lining proportional, lining tabular, oldstyle proportional, oldstyle tabular.
3. **Defaults are fine**: "It's never wrong to use the default figures."
4. **Lining for caps**: "Lining figures are always preferred for all caps text."
5. **Oldstyle for body**: Work best in lowercase body text.
6. **Tabular for columns**: Essential for vertically aligned grids of numbers.
7. **Proportional for prose**: Better even spacing in running text.

# Construction / Recognition

## To Construct/Create:
1. In Word: Font > Advanced > Number spacing / Number forms menus.
2. In CSS: `font-variant-numeric: oldstyle-nums proportional-nums` (or other combinations).
3. Check if your font has alternates: type zeros above ones — same length = tabular.

## To Identify/Recognise:
1. Lining: all digits same height, aligned with caps.
2. Oldstyle: digits have ascenders and descenders like lowercase.
3. Tabular: zeros and ones occupy the same width.
4. Proportional: narrow digits (1) take less space than wide digits (0).

# Examples

**Example 1** (alternate-figures): Oldstyle figures with caps text ("TOP 40 IN 1987") — looks wrong because oldstyle descends below baseline.

**Example 2** (alternate-figures): Proportional figures in a column — numbers don't align vertically. Tabular figures in the same column — numbers align correctly.

# Relationships

## Builds Upon
- **Font** — Alternate figures are font-specific.
- **OpenType Features** — Accessed as OpenType features.

## Related
- **All Caps** — Lining figures are mandatory with caps.
- **Body Text** — Oldstyle proportional figures suit body text.

# Common Errors

- **Error**: Using oldstyle figures with all-caps text.
  **Correction**: "With caps, you should not use oldstyle figures. They look wrong." Use lining figures.

# Common Confusions

- **Confusion**: The figure style in the default position is the only option.
  **Clarification**: Professional fonts may include all four combinations. Check OpenType features for alternatives.

# Source Reference

"Alternate Figures" page. "Text Formatting" chapter.

# Verification Notes

- Definition source: Direct quotes from alternate-figures.md.
- Confidence rationale: High — systematic explanation of all four combinations.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
