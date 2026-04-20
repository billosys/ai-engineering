---
# === CORE IDENTIFICATION ===
concept: Small Caps
slug: small-caps

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
section: "Small Caps"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "SC"
  - "smcp"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - typographic-emphasis
  - font
extends: []
related:
  - all-caps
  - letterspacing
  - kerning
  - opentype-features
  - typographic-color
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "font-variant"
    example: ".sc { font-variant-caps: small-caps; letter-spacing: 0.05em; }"
    support: baseline
---

# Quick Definition

Small caps are short capital letters calibrated to blend with lowercase text — a refined alternative to bold, italic, or all caps for emphasis — but only genuine small caps from professional fonts, never the fake scaled-down versions word processors generate.

# Core Definition

Butterick defines: "Small caps are short capital letters designed to blend with lowercase text. They're usually slightly taller than lowercase letters." He distinguishes real from fake: "Small-cap formatting works by scaling down regular caps. But compared to the other characters in the font, the fake small caps that result are too tall, and their vertical strokes are too light."

Two rules: "Don't click on the small-cap formatting box in your word processor. Ever." And "The rules for all caps also apply to small caps: use small caps sparingly, add letterspacing, and turn on kerning."

# Prerequisites

- **Typographic Emphasis** — Small caps are an emphasis alternative.
- **Font** — Requires a professional font with real small caps (OpenType `smcp` feature).

# Key Properties

1. **Real vs. fake**: Word processor small caps are scaled fakes — visually inferior.
2. **Calibrated color**: Real small caps have stroke weight calibrated to match surrounding text.
3. **Requires professional fonts**: Not included with system fonts.
4. **OpenType feature**: Accessed via the `smcp` feature tag.
5. **Always letterspace**: Same rules as all caps.
6. **CSS support**: `font-variant-caps: small-caps` now safely accesses OpenType small caps.

# Construction / Recognition

## To Construct/Create:
1. Use a professional font with real small caps (check OpenType features).
2. Never use the word processor's small-cap formatting button.
3. Access via OpenType features or dedicated small-cap font files.
4. Add 5-12% letterspacing and ensure kerning is on.

## To Identify/Recognise:
1. Fake small caps: strokes look too light compared to surrounding text.
2. Real small caps: consistent stroke weight and height calibrated to blend.

# Context & Application

- **Typical contexts**: Abbreviations, acronyms, headings, citations.
- **Common applications**: Emphasis alternative to bold/italic; legal citations; bibliographic references.

# Examples

**Example 1** (small-caps): "Witness Protection" in fake small caps vs. real — fake has visibly thinner strokes and wrong height.

**Example 2** (small-caps): A bibliographic citation using real small caps for the book title — consistent typographic color.

# Relationships

## Builds Upon
- **Typographic Emphasis** — Small caps are a refined emphasis tool.
- **Font** — Only professional fonts include real small caps.

## Related
- **All Caps** — Small caps follow the same spacing rules.
- **Letterspacing** — Mandatory with small caps.
- **Kerning** — Must be active.
- **OpenType Features** — Small caps are accessed as the `smcp` feature.
- **Typographic Color** — The key difference between real and fake small caps is color consistency.

# Common Errors

- **Error**: Using the word processor's small-cap formatting button.
  **Correction**: "This option does not produce small caps. It produces inferior counterfeits." Use OpenType features or dedicated small-cap font files.

# Common Confusions

- **Confusion**: Small caps are just smaller versions of regular capitals.
  **Clarification**: Real small caps are separately designed letterforms with calibrated stroke weight and height, not mechanically scaled capitals.

# Source Reference

"Small Caps" page. "Text Formatting" chapter.

# Verification Notes

- Definition source: Direct quotes from small-caps.md.
- Confidence rationale: High — clear rules with visual examples.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
