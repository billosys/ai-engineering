---
# === CORE IDENTIFICATION ===
concept: OpenType Features
slug: opentype-features

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
section: "OpenType Features"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "OT features"
  - "OpenType layout features"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - font
extends: []
related:
  - small-caps
  - ligatures
  - alternate-figures
  - kerning
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "font-feature-settings"
    example: "body { font-feature-settings: 'kern' 1, 'liga' 1; } .sc { font-feature-settings: 'smcp' 1; }"
    support: baseline
---

# Quick Definition

OpenType features are layout capabilities embedded in fonts that enable typographic luxuries like small caps, alternate figures, ligatures, and ordinals — but usable only when both the font and the application support them.

# Core Definition

Butterick explains: "OpenType includes layout features — commonly known as OpenType features — that allow fonts to specify alternate letterforms, and rules for how they should be inserted into the text."

The catch: "Merely selecting an OpenType font doesn't make its features available. Rather, your typesetting program also has to support the features you want to use." This means "you can only use a given feature if it's supported by both the font and the application."

Type designers add features at their discretion: "an OpenType-format font can have any number of OpenType features, including none."

# Prerequisites

- **Font** — OpenType features are embedded in font files.

# Key Properties

1. **Dual requirement**: Both font and application must support the feature.
2. **Designer discretion**: Features vary per font.
3. **Key features**: Small caps (`smcp`), ligatures (`liga`), kerning (`kern`), alternate figures, ordinals, fractions.
4. **Best support**: Professional page-layout apps (InDesign, Illustrator).
5. **Web support**: All major desktop browsers; spottier on mobile.
6. **Word support**: Limited — ligatures, alternate figures, stylistic sets (Word 2010+).

# Construction / Recognition

## To Construct/Create:
1. In Word: Font > Advanced > Advanced Typography panel.
2. In Pages: Font panel (Cmd+T) > gear icon > Typography.
3. In CSS: `font-feature-settings` with feature tags.
4. Check font specimen sheets for available features.

## To Identify/Recognise:
1. Professional fonts with OpenType features: specimen sheets list available features.
2. Active features: alternate letterforms appear in the text.

# Examples

**Example 1** (opentype-features): OpenType enabled small caps, ligatures, and alternate figures — "luxuries" that "had previously been difficult or impossible."

# Relationships

## Builds Upon
- **Font** — OpenType features are part of font files.

## Related
- **Small Caps** — Accessed via `smcp` OpenType feature.
- **Ligatures** — Accessed via `liga` OpenType feature.
- **Alternate Figures** — Accessed via OpenType figure features.
- **Kerning** — Accessed via `kern` OpenType feature.

# Common Errors

- **Error**: Assuming OpenType features are automatically active.
  **Correction**: Features must be explicitly enabled in most applications. Check both font support and application support.

# Common Confusions

- **Confusion**: All OpenType fonts have the same features.
  **Clarification**: "Type designers add these features at their discretion. An OpenType-format font can have any number of OpenType features, including none."

# Source Reference

"OpenType Features" page. "Text Formatting" chapter.

# Verification Notes

- Definition source: Direct quotes from opentype-features.md.
- Confidence rationale: High — clear explanation of dual-requirement constraint.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
