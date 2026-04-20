---
# === CORE IDENTIFICATION ===
concept: Curly Quotes
slug: curly-quotes

# === CLASSIFICATION ===
category: typography
subcategory: type-composition
tier: foundational
layer: 2-domain

# === PROVENANCE ===
source: "Butterick's Practical Typography"
source_slug: practical-typography
authors: "Matthew Butterick"
chapter: "Type Composition"
chapter_number: null
pdf_page: null
section: "Straight and Curly Quotes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "smart quotes"
  - "typographer's quotes"
  - "proper quotation marks"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - typewriter-habits
extends: []
related:
  - sentence-spacing
  - hyphens-and-dashes
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "q element / content"
    example: "q { quotes: '\\201C' '\\201D' '\\2018' '\\2019'; } /* Unicode curly quotes */"
    support: baseline
---

# Quick Definition

Curly quotes are the correctly shaped quotation marks used in professional typography — with distinct opening and closing forms — replacing the ambidextrous straight quotes inherited from typewriter character sets.

# Core Definition

Butterick states: "Straight quotes are a typewriter habit. In traditional printing, all quotation marks were curly." There are four curly quote characters: opening single, closing single, opening double, and closing double — as opposed to the two straight characters.

Straight quotes originated because "typewriter character sets were limited by mechanical constraints and physical space. By replacing the curly opening and closing quotes with ambidextrous straight quotes, two slots became available for other characters."

His rule is absolute: "Straight quotes should never, ever appear in your documents."

# Prerequisites

- **Typewriter Habits** — Straight quotes are the #1 typewriter habit to eliminate.

# Key Properties

1. **Four distinct characters**: Opening and closing forms for both single and double quotes.
2. **Always use curly**: "Straight quotes should never, ever appear in your documents."
3. **Smart-quote feature**: Word processors auto-convert straight to curly — "Smart quotes are typically turned on by default."
4. **30-year feature**: "Smart-quote substitution has been built into word processors for nearly 30 years."
5. **Most grievous error**: "That's why straight quotes are one of the most grievous and inept typographic errors."
6. **Exception**: Acceptable in email and code syntax.

# Construction / Recognition

## To Construct/Create:
1. Enable smart quotes in your word processor (usually on by default).
2. When pasting text with straight quotes, use search-and-replace to convert them.
3. On Mac: option+[ for open double, option+shift+[ for close double, option+] for open single, option+shift+] for close single.
4. In HTML: use `&ldquo;` `&rdquo;` `&lsquo;` `&rsquo;` or UTF-8 encoding.
5. The HTML `<q>` tag automatically appends curly quotes when a `lang` attribute is set.

## To Identify/Recognise:
1. Straight quotes are vertical and ambidextrous (same glyph for open and close).
2. Curly quotes curve or angle — opening quotes face right, closing quotes face left.

# Context & Application

- **Typical contexts**: All typeset documents — books, articles, reports, web pages.
- **Common applications**: Quotation marks in running text; apostrophes.
- **Exception**: Code syntax, email, and contexts where smart-quote conversion may corrupt data.

# Examples

**Example 1** (straight-and-curly-quotes): Straight quotes in "That's a 'magic' shoe." (wrong) vs. curly quotes (right).

**Example 2** (straight-and-curly-quotes): "Confidential to computer scientists: straight quotes and backticks in software code should never be converted to curly quotes."

# Relationships

## Builds Upon
- **Typewriter Habits** — Straight quotes are typewriter habit #1.

## Related
- **Sentence Spacing** — Another typewriter habit to correct.
- **Hyphens and Dashes** — Another character-level typewriter habit.

# Common Errors

- **Error**: Leaving straight quotes in typeset documents.
  **Correction**: Enable smart quotes. After pasting text, use search-and-replace to convert any remaining straight quotes.

# Common Confusions

- **Confusion**: Smart quotes should be applied everywhere, including code.
  **Clarification**: "Straight quotes and backticks in software code should never be converted to curly quotes. Those marks are, of course, part of the code syntax."

# Source Reference

"Straight and Curly Quotes" page. "Type Composition" chapter.

# Verification Notes

- Definition source: Direct quotes from straight-and-curly-quotes.md.
- Confidence rationale: High — absolute rule with detailed instructions.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
