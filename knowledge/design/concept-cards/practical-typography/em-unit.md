---
# === CORE IDENTIFICATION ===
concept: Em Unit
slug: em-unit

# === CLASSIFICATION ===
category: typography
subcategory: type-formatting
tier: foundational
layer: 2-domain

# === PROVENANCE ===
source: "Butterick's Practical Typography"
source_slug: practical-typography
authors: "Matthew Butterick"
chapter: "Appendix"
chapter_number: null
pdf_page: null
section: "Em Sizing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "em"
  - "em square"
  - "em sizing"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - point-size
extends: []
related:
  - font
  - hyphens-and-dashes
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 5: What are the basic anatomical parts of a letterform (baseline, x-height, cap height, ascender, descender, counter)?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "em (CSS unit)"
    example: "p { text-indent: 1em; margin-bottom: 0.5em; } /* 1em = element's computed font-size */"
    support: baseline
---

# Quick Definition

The em is the fundamental typographic unit of measurement — equal to the point size of the font — that defines the maximum vertical space a font's characters can occupy. It explains why different fonts appear different sizes at the same point size.

# Core Definition

Butterick explains: "The em size of a font is the same as its point size. This was true for hundreds of years of metal type." In digital type, "the em is implemented in software rather than metal. But it still represents the same thing: the maximum vertical size of the letters in the font."

This is why point size is not absolute: "Two fonts set at the same point size will appear to be different sizes if one occupies less space on its em."

The em is *not* the letter M: "the word em denotes a typographer's measurement, not the letter M." The en is half the em. In traditional print shops, they were called "mutton" and "nut" to disambiguate.

# Prerequisites

- **Point Size** — The em is the unit that underlies point size measurement.

# Key Properties

1. **Equal to point size**: A 12pt font has a 12pt em.
2. **Maximum vertical space**: Defines the bounding box, not any specific letter height.
3. **Not the letter M**: Despite the homophony, em is a unit of measurement.
4. **En = half em**: The en is half the width of the em.
5. **Explains apparent size differences**: Fonts that use their em space differently appear different sizes at the same point setting.
6. **Consistent for centuries**: The concept has survived the transition from metal to digital type.

# Construction / Recognition

## To Construct/Create:
1. In CSS, `1em` equals the computed font-size of the element.
2. In print, 1em = the point size of the current font.
3. Em dashes and en dashes are named for these units (though modern digital versions often run narrower).

## To Identify/Recognise:
1. Cannot be directly measured from printed output — it defines the bounding box, not visible letter edges.
2. Two fonts at the same point size looking different sizes demonstrates the em at work.

# Context & Application

- **Typical contexts**: Understanding font metrics; CSS relative sizing; typographic measurement.
- **Common applications**: Em-based CSS units for scalable layouts; understanding why fonts look different at the same nominal size; dash sizing conventions.
- **Historical note**: Butterick recounts a 2012 Michigan Supreme Court case that turned on the legal definition of point size and em sizing.

# Examples

**Example 1** (em-sizing): "Why not just make the point size equal to something specific, like the height of the capital H?" — Because "since fonts vary widely in their design, there's no character you could pick that would always be consistent."

**Example 2** (em-sizing): The Michigan ballot case — a citizen's group was challenged because opposing counsel argued "14-point" meant the size of capital letters, not the em. The Supreme Court correctly upheld the traditional definition.

# Relationships

## Builds Upon
- **Point Size** — The em is the unit of measurement underlying point size.

## Related
- **Font** — Each font uses its em space differently, causing apparent size variation.
- **Hyphens and Dashes** — Em dash and en dash are named for these units.

# Common Errors

- **Error**: Assuming the em is the width of the letter "M".
  **Correction**: "The word em denotes a typographer's measurement, not the letter M." The em equals the point size of the font.

# Common Confusions

- **Confusion**: Point size directly measures the height of capital letters.
  **Clarification**: Point size defines the em square — the maximum bounding box. Capital letters, ascenders, and descenders all fit within it, but different fonts apportion the space differently.

# Source Reference

"Em Sizing" page. "Appendix" chapter.

# Verification Notes

- Definition source: Direct quotes from em-sizing.md.
- Confidence rationale: High — clear technical explanation with historical examples.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
