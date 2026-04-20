---
# === CORE IDENTIFICATION ===
concept: Kerning
slug: kerning

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
section: "Kerning"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "kern pairs"
  - "pair kerning"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - font
extends: []
related:
  - letterspacing
  - optical-vs-metric-spacing
  - opentype-features
contrasts_with:
  - letterspacing

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 5: What are the basic anatomical parts of a letterform (baseline, x-height, cap height, ascender, descender, counter)?"
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "font-kerning / font-feature-settings"
    example: "body { font-kerning: normal; text-rendering: optimizeLegibility; }"
    support: baseline
---

# Quick Definition

Kerning is the adjustment of spacing between specific letter pairs to improve visual consistency — built into fonts by designers and always turned on, distinct from letterspacing which affects all pairs uniformly.

# Core Definition

Butterick defines: "Kerning is the adjustment of specific pairs of letters to improve spacing and fit. (It's distinct from letterspacing, which affects all pairs.) Most fonts come with hundreds and sometimes thousands of kerning pairs inserted by the font designer."

The rule is simple: "Always use kerning." For most users, built-in kerning is sufficient: "For professional typographers, [manual kerning] is a mandatory skill, but for everyone else, the built-in kerning is just fine."

# Prerequisites

- **Font** — Kerning data is embedded in font files.

# Key Properties

1. **Pair-specific**: Adjusts specific problematic letter combinations.
2. **Built into fonts**: Hundreds to thousands of pairs per font.
3. **Always on**: "Always use kerning."
4. **Distinct from letterspacing**: Kerning = specific pairs; letterspacing = all pairs.
5. **Manual kerning optional**: Built-in is adequate for non-professionals.

# Construction / Recognition

## To Construct/Create:
1. In Word: Font > Advanced > check "Kerning for fonts 8 Points and above."
2. In Pages: kerning is on by default.
3. In CSS: `font-kerning: normal` or `text-rendering: optimizeLegibility`.
4. Include kerning settings in paragraph/character style definitions.

## To Identify/Recognise:
1. Without kerning: visible gaps between certain pairs (e.g., AV, To, Wa).
2. With kerning: consistent spacing across all letter pairs.

# Context & Application

- **Typical contexts**: All typeset text — kerning should always be active.
- **Common applications**: Ensuring consistent letter spacing, especially important at larger sizes (headings) and with all caps.

# Examples

**Example 1** (kerning): Kerning "reduces the large gaps between certain letter pairs, making them consistent with the rest of the font."

# Relationships

## Builds Upon
- **Font** — Kerning data is part of the font file.

## Contrasts With
- **Letterspacing** — Letterspacing affects all pairs uniformly; kerning adjusts specific pairs.

## Related
- **Optical vs. Metric Spacing** — InDesign's "optical" spacing overrides font kerning data.
- **OpenType Features** — Kerning is activated as an OpenType feature (`kern`).

# Common Errors

- **Error**: Leaving kerning turned off (the default in some word processors).
  **Correction**: Always turn on kerning. In Word, you must manually enable it.

# Common Confusions

- **Confusion**: Kerning and letterspacing are the same thing.
  **Clarification**: Kerning adjusts specific problematic pairs. Letterspacing (tracking) adjusts all pairs uniformly. They serve different purposes.

# Source Reference

"Kerning" page. "Text Formatting" chapter.

# Verification Notes

- Definition source: Direct quotes from kerning.md.
- Confidence rationale: High — clear definition and simple rule.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
