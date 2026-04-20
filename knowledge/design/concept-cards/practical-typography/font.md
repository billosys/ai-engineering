---
# === CORE IDENTIFICATION ===
concept: Font
slug: font

# === CLASSIFICATION ===
category: typography
subcategory: type-elements
tier: foundational
layer: 2-domain

# === PROVENANCE ===
source: "Butterick's Practical Typography"
source_slug: practical-typography
authors: "Matthew Butterick"
chapter: "Font Recommendations"
chapter_number: null
pdf_page: null
section: "Font Basics"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "typeface"
  - "font family"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - body-text
extends: []
related:
  - point-size
  - kerning
  - opentype-features
  - font-pairing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 6: What distinguishes a serif typeface from a sans-serif, and what are the historical/functional reasons for each?"
  - "CQ 26: How do you evaluate and select a typeface pairing for a web application? What properties should contrast, and what should harmonise?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "font-family"
    example: "@font-face { font-family: 'MyFont'; src: url('font.woff2'); } body { font-family: 'MyFont', serif; }"
    support: baseline
---

# Quick Definition

A font is a data file containing letter shapes, spacing, and typographic features — the primary tool for controlling how text appears visually. Professional fonts are a worthwhile investment that improves every document.

# Core Definition

Butterick explains: "Fonts control the visual appearance of all text rendered by a computer." He clarifies their nature: "Fonts are not programs... They're static data files, like MP3s or PDFs. Each font file contains information that defines the shapes of the letters, plus spacing, kerning, OpenType features, and so on."

The historical distinction between "font" (a specific instance) and "typeface" (the overall family) has largely collapsed: in modern usage, "font" covers both senses.

He strongly advocates professional fonts over system and free fonts: "The best professional fonts are better than any system font or free font — and in ways that everyone... can appreciate."

# Prerequisites

- **Body Text** — Font is one of the four primary body text controls.

# Key Properties

1. **Static data files**: Like MP3s or PDFs — not programs.
2. **One file per style**: Roman, italic, bold, bold italic, small caps are separate files within a font family.
3. **Professional > system**: Professional fonts visibly improve every document.
4. **Durable investment**: "They don't break, they don't go obsolete in three years, and they don't need to be upgraded monthly."
5. **Licensed software**: Fonts are sold per-user under license terms.
6. **Names are unreliable**: Same historical names (e.g., Garamond) used by very different fonts. "Stempel Garamond and ITC Garamond are as similar as Bart Simpson and Lisa Simpson."

# Construction / Recognition

## To Construct/Create:
1. For body text, acquire at minimum: roman, italic, bold, bold italic, and roman small caps.
2. Buy from font designers' websites or multi-designer retailers ($20–50 per style).
3. Install via the OS font management tool (Font Book on Mac, Control Panel on Windows).
4. On the web, use `@font-face` declarations with webfont files hosted locally or remotely.

## To Identify/Recognise:
1. Any text displayed on screen or in print is rendered through a font.
2. Professional fonts vs. system fonts: noticeable difference in spacing, consistency, and polish.

# Context & Application

- **Typical contexts**: Every document, web page, and application.
- **Common applications**: Setting body text appearance; establishing document personality; building brand identity.
- **Historical note**: The font/typeface distinction originated in letterpress (where each size had a separate drawer of metal type) but is now largely moot.

# Examples

**Example 1** (font-basics): "What's the difference between a font and a typeface? ... Historically, typeface referred to the overall family and font referred to a specific instance... But... 'technology has changed the meaning of this term.'"

**Example 2** (font-basics): "You can get a top-quality professional-font family for under $200... Best of all, you can put them to work without learning anything new."

# Relationships

## Builds Upon
- **Body Text** — Font is one of body text's four primary controls.

## Enables
- **Font Pairing** — Selecting and combining fonts effectively.
- **Kerning** — Font files contain kerning data that affects letter spacing.
- **OpenType Features** — Professional fonts include OpenType features like ligatures.

## Related
- **Point Size** — Fonts render differently at the same point size due to em sizing.

# Common Errors

- **Error**: Using system default fonts (Calibri, Times New Roman, Arial) for professional documents.
  **Correction**: "The best professional fonts are better than any system font or free font." Invest in professional fonts for body text.

# Common Confusions

- **Confusion**: Font names with the same historical root are the same font.
  **Clarification**: "Stempel Garamond and ITC Garamond are as similar as Bart Simpson and Lisa Simpson." Font names are unreliable quality indicators.

# Source Reference

"Font Basics" page. "Font Recommendations" chapter.

# Verification Notes

- Definition source: Direct quotes from font-basics.md.
- Confidence rationale: High — clear FAQ format with explicit advice.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
