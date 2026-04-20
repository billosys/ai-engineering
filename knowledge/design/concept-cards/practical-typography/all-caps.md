---
# === CORE IDENTIFICATION ===
concept: All Caps
slug: all-caps

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
section: "All Caps"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "uppercase"
  - "capitalization"
  - "caps"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - typographic-emphasis
extends: []
related:
  - small-caps
  - letterspacing
  - kerning
  - headings
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "text-transform"
    example: ".caps { text-transform: uppercase; letter-spacing: 0.05em; }"
    support: baseline
---

# Quick Definition

All-caps text is best used sparingly — fine for short labels under one line — but never for whole paragraphs, because capital letters create a uniform rectangular contour that is harder to read than varied lowercase shapes.

# Core Definition

Butterick explains why caps reduce legibility: "We read more lowercase text, so as a matter of habit, lowercase is more familiar and thus more legible. Furthermore, cognitive research has suggested that the shapes of lowercase letters — some tall (d h k l), some short (a e n s), some descending (g y p q) — create a varied visual contour that helps our brain recognize words. Capitalization homogenizes these shapes, leaving a rectangular contour."

All-caps paragraphs are "self-defeating typography": "if you need readers to pay attention to an important part of your document, the last thing you want is for them to skim over it."

# Prerequisites

- **Typographic Emphasis** — All caps is one of several emphasis tools.

# Key Properties

1. **Short only**: "Fine for less than one line."
2. **Harder to read**: Rectangular contour vs. varied lowercase shapes.
3. **Self-defeating at length**: Long caps text causes readers to skim.
4. **Always letterspace**: "Always add letterspacing to caps to make them easier to read."
5. **Always kern**: Ensure kerning is turned on with caps.
6. **Prefer formatting over typing**: Apply all-caps formatting via text-transform rather than retyping in caps.

# Construction / Recognition

## To Construct/Create:
1. Apply via formatting (text-transform: uppercase) rather than caps lock.
2. Add 5-12% letterspacing.
3. Ensure kerning is on.
4. Limit to short labels, headings under one line, headers, footers, captions.

## To Identify/Recognise:
1. Long all-caps passages signal amateur typography.
2. Unletterspaced caps look too tight.

# Context & Application

- **Typical contexts**: Short headings, labels, captions, headers/footers, letterhead.
- **Common applications**: Table of contents headers, business card elements, navigation labels.
- **Legal note**: The Ninth Circuit has ruled that caps lock is not a "make conspicuous" button — conspicuousness requires more than just capitalization.

# Examples

**Example 1** (all-caps): A full paragraph in all caps demonstrating reader fatigue — "DO YOU ENJOY READING THIS? I DOUBT IT."

**Example 2** (all-caps): Better alternatives to emphasize a paragraph: "Use rules and borders. Add a heading. Run it in a larger point size. But don't capitalize it."

# Relationships

## Builds Upon
- **Typographic Emphasis** — All caps is an emphasis option alongside bold/italic.

## Related
- **Small Caps** — A more refined alternative to all caps.
- **Letterspacing** — Mandatory companion to all caps.
- **Kerning** — Must be active when using caps.
- **Headings** — Caps are sometimes used in headings (but Butterick advises against it).

# Common Errors

- **Error**: Capitalizing entire paragraphs for emphasis or "conspicuousness."
  **Correction**: All-caps paragraphs are self-defeating. Use rules, borders, headings, or larger point size instead.

# Common Confusions

- **Confusion**: All caps conveys authority and importance.
  **Clarification**: All caps primarily conveys reduced legibility. For emphasis at paragraph scale, virtually any other technique works better.

# Source Reference

"All Caps" page. "Text Formatting" chapter.

# Verification Notes

- Definition source: Direct quotes from all-caps.md.
- Confidence rationale: High — emphatic advice with clear reasoning.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
