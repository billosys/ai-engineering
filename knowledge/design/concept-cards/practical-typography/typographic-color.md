---
# === CORE IDENTIFICATION ===
concept: Typographic Color
slug: typographic-color

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
section: "Color"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "color in typography"
  - "typographic colour"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - body-text
  - typographic-emphasis
extends: []
related:
  - font
  - point-size
  - small-caps
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "color"
    example: "body { color: #333; } /* dark gray can be more comfortable than black on screen */"
    support: baseline
---

# Quick Definition

Typographic color has two meanings: (1) the overall darkness/lightness of a text block as determined by font weight, size, and spacing — even when all text is black; and (2) literal color applied to type, which should be used with restraint.

# Core Definition

Butterick distinguishes the dual meaning: "Typographers will sometimes speak of a font as creating a certain color on the page — even when it's black. Used this way, the word encapsulates a set of hard-to-quantify characteristics like darkness, contrast, rhythm, and texture."

For literal color, key principles: "On a page of text, nothing draws the eye more powerfully than a contrast between light and dark colors. This is why a bold font creates more emphasis than an italic font." And: "The perceived intensity of colored type depends not just on the color, but also the size and weight of the font."

Body text in print "must always be set in black type. No exceptions." On screen: "Consider making your text dark gray rather than black" because screens project light rather than reflecting it.

# Prerequisites

- **Body Text** — Color decisions start with the body text.
- **Typographic Emphasis** — Bold/italic create different typographic color.

# Key Properties

1. **Dual meaning**: Typographic color (density/texture) vs. literal color (hue).
2. **Light-dark contrast**: Most powerful visual attention mechanism.
3. **Size and weight interact**: "A thin or small font can carry a more intense color than a heavy or large font."
4. **Print: always black**: Body text in print must be black. No exceptions.
5. **Screen: dark gray**: "Dark-gray text can be more comfortable to read than black text" on screens.
6. **Less is more**: "When everything is emphasized, nothing is emphasized."
7. **Web links**: Color is the idiomatic signal for clickability — don't use it on non-clickable text.

# Construction / Recognition

## To Construct/Create:
1. Print body text: always black.
2. Screen body text: consider dark gray (#333 or similar).
3. Use color sparingly for emphasis — only where size and weight alone are insufficient.
4. For professionally printed materials, prefer multiple shades of one color over contrasting colors.

## To Identify/Recognise:
1. Consistent typographic color: text block appears even in density.
2. Inconsistent color: light and dark patches that distract from reading.

# Context & Application

- **Typical contexts**: Body text color, emphasis decisions, web link styling.
- **Common applications**: Setting body text darkness; choosing heading color; web link colors.
- **Historical note**: "Red has been the favored second color in typography for hundreds of years."

# Examples

**Example 1** (color): "A bold font creates more emphasis than an italic font" — because bold creates greater color contrast with surrounding text.

**Example 2** (color): On screen, "dark-gray text can be more comfortable to read than black text" because screens project light.

# Relationships

## Builds Upon
- **Body Text** — Typographic color is primarily a body text concern.
- **Typographic Emphasis** — Bold/italic differ in the color they produce.

## Related
- **Font** — Different fonts produce different typographic color at the same settings.
- **Point Size** — Size affects the perceived intensity of color.
- **Small Caps** — Real vs. fake small caps differ primarily in typographic color consistency.

# Common Errors

- **Error**: Using colored text for emphasis in printed body text.
  **Correction**: "At a typical body-text point size, color isn't effective as a form of emphasis." Use bold or italic instead.

# Common Confusions

- **Confusion**: Typographic "color" means hue.
  **Clarification**: In typography, "color" primarily refers to the overall visual density of a text block — darkness, rhythm, and texture — even when all text is black.

# Source Reference

"Color" page. "Text Formatting" chapter.

# Verification Notes

- Definition source: Direct quotes from color.md.
- Confidence rationale: High — clear dual definition with practical rules.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
