---
# === CORE IDENTIFICATION ===
concept: Hyphenation
slug: hyphenation

# === CLASSIFICATION ===
category: typography
subcategory: type-composition
tier: intermediate
layer: 2-domain

# === PROVENANCE ===
source: "Butterick's Practical Typography"
source_slug: practical-typography
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Hyphenation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "automatic hyphenation"
  - "word breaking"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - justified-text
  - line-length
extends: []
related:
  - hyphens-and-dashes
  - headings
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "hyphens"
    example: "p { hyphens: auto; } /* requires lang attribute on html element */"
    support: baseline
---

# Quick Definition

Hyphenation is the automated breaking of words between lines to create more consistent text blocks — mandatory for justified text, optional for left-aligned, and should be suppressed in headings.

# Core Definition

Butterick defines: "Hyphenation is the automated process of breaking words between lines to create more consistency across a text block."

The rule is context-dependent: "In justified text, hyphenation is mandatory." Without it, justified text develops "gruesomely large spaces between words." For left-aligned text, "hyphenation evens the irregular right edge of the text, called the rag. Hyphenation is optional for left-aligned text."

As line length decreases, "hyphenation becomes essential" because shorter lines have fewer possible break points.

# Prerequisites

- **Justified Text** — Hyphenation is mandatory for justification.
- **Line Length** — Shorter lines increase the need for hyphenation.

# Key Properties

1. **Mandatory for justified text**: Prevents large word spaces.
2. **Optional for left-aligned**: Evens the rag but isn't required.
3. **Essential for short lines**: Fewer break points make hyphenation necessary.
4. **Suppress in headings**: Hyphenation in short text "often causes more problems than it solves."
5. **Limited web support**: CSS `hyphens: auto` has spotty browser support.

# Construction / Recognition

## To Construct/Create:
1. In Word: Page Layout > Hyphenation > Automatic.
2. In Pages: Document > Hyphenation checkbox.
3. In CSS: `hyphens: auto` (requires `lang` attribute on `html` element).
4. Suppress in heading styles: use `hyphens: none`.

## To Identify/Recognise:
1. Justified text without hyphenation: visible rivers of white space.
2. Over-hyphenation: too many consecutive lines ending with hyphens.

# Examples

**Example 1** (hyphenation): A heading hyphenated across three lines ("contradic-tions" and "use-less") vs. the same heading unhyphenated — the unhyphenated version is clearer.

# Relationships

## Builds Upon
- **Justified Text** — Hyphenation is a requirement for justified alignment.
- **Line Length** — Line length determines the urgency of hyphenation.

## Related
- **Hyphens and Dashes** — Automatic hyphens are distinct from editorial hyphens.
- **Headings** — Suppress hyphenation in headings.

# Common Errors

- **Error**: Using justified text without turning on hyphenation.
  **Correction**: "If you're using justified text, you must also turn on hyphenation to prevent gruesomely large spaces between words."

# Common Confusions

- **Confusion**: Hyphenation always improves text.
  **Clarification**: For left-aligned text, hyphenation is optional. In headings, it should be suppressed. The value depends on the context.

# Source Reference

"Hyphenation" page. "Page Layout" chapter.

# Verification Notes

- Definition source: Direct quotes from hyphenation.md.
- Confidence rationale: High — clear conditional rules.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
