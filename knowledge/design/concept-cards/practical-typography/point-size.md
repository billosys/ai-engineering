---
# === CORE IDENTIFICATION ===
concept: Point Size
slug: point-size

# === CLASSIFICATION ===
category: typography
subcategory: type-formatting
tier: foundational
layer: 2-domain

# === PROVENANCE ===
source: "Butterick's Practical Typography"
source_slug: practical-typography
authors: "Matthew Butterick"
chapter: "Text Formatting"
chapter_number: null
pdf_page: null
section: "Point Size"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "font size"
  - "type size"
  - "text size"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - body-text
extends: []
related:
  - line-spacing
  - line-length
  - em-unit
  - headings
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 5: What are the basic anatomical parts of a letterform (baseline, x-height, cap height, ascender, descender, counter)?"
  - "CQ 19: A landing page hero section uses a 14px body font, a 16px heading, and a 14px subheading. Why does it feel like nothing stands out?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "font-size"
    example: "body { font-size: 18px; } /* web body text: 15-25px range */"
    support: baseline
---

# Quick Definition

Point size is the measurement of how large a font renders — optimally 10-12 points in print and 15-25 pixels on the web, though different fonts appear different sizes at the same point size.

# Core Definition

Butterick states: "In print, the optimal point size for body text is 10-12 point. On the web, the optimal size is 15-25 pixels."

Crucially, the point-size system is not absolute: "different fonts set at the same point size won't necessarily appear the same on the page." This is because digital fonts are drawn inside a rectangle called the em, and "Two fonts set at the same point size will appear to be different sizes if one occupies less space on its em."

There are 72 points to an inch. Half-point differences are meaningful at body text sizes.

# Prerequisites

- **Body Text** — Point size is one of the four primary body text controls.

# Key Properties

1. **72 points per inch**: The fundamental measurement unit.
2. **Not absolute**: Different fonts appear different sizes at the same point value.
3. **Print range**: 10-12pt for body text (12pt default is often too large).
4. **Web range**: 15-25px for body text (larger to compensate for reading distance and screen rendering).
5. **Half-point sensitivity**: At body text sizes, half-point increments are visually meaningful.
6. **Emphasis tool**: Point size changes can provide emphasis, but subtly — start with half-point increments.

# Construction / Recognition

## To Construct/Create:
1. Start in the recommended range (10-12pt print, 15-25px web).
2. Use your eyes, not the number — compare visually, not numerically.
3. Try intermediate sizes (10.5, 11.5) for fine-tuning.
4. When matching fonts, adjust point size until text blocks occupy the same space.

## To Identify/Recognise:
1. Cannot be determined by measurement alone — only by matching against a known sample in the same font.

# Context & Application

- **Typical contexts**: Every document and website — point size is always specified.
- **Common applications**: Setting body text size; creating heading hierarchy through size variation; matching fonts across documents.
- **Historical note**: The 12pt default comes from typewriter convention, not from optimal readability.

# Examples

**Example 1** (point-size): Three fonts — Sabon, Times New Roman, and Arno — all set at 12 point but appearing different sizes visually.

**Example 2** (point-size): "If you're not required to use 12 point, don't. Try sizes down to 10 point, including intermediate sizes like 10.5 and 11.5."

**Example 3** (point-size): On the web — "the web has a long tradition of teeny fonts. It's time to let it go."

# Relationships

## Builds Upon
- **Body Text** — Point size is one of body text's four primary controls.

## Enables
- **Headings** — Heading hierarchy relies on point size variation.

## Related
- **Em Unit** — The em is the typographic unit underlying point size.
- **Line Spacing** — Should be adjusted when point size changes.
- **Line Length** — Affected by point size choice.

# Common Errors

- **Error**: Using the 12pt default without evaluating whether it's appropriate.
  **Correction**: 12pt is a typewriter convention. Most professionally typeset material uses 10-11pt. Evaluate visually.

- **Error**: Doubling point size for headings (e.g., 12pt body to 24pt heading).
  **Correction**: "There is no typographic universe in which you need to double the point size to achieve emphasis." Use subtler increments.

# Common Confusions

- **Confusion**: Two fonts at the same point size will be the same visual size.
  **Clarification**: Point size is not absolute — it defines the em square, not the apparent letter size. Different fonts use their em space differently.

# Source Reference

"Point Size" page. "Text Formatting" chapter.

# Verification Notes

- Definition source: Direct quotes from point-size.md.
- Confidence rationale: High — explicit numeric ranges and clear explanations.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
