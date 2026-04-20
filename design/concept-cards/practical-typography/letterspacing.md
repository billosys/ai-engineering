---
# === CORE IDENTIFICATION ===
concept: Letterspacing
slug: letterspacing

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
section: "Letterspacing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "tracking"
  - "character spacing"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - font
extends: []
related:
  - kerning
  - all-caps
  - small-caps
contrasts_with:
  - kerning

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 11: What distinguishes a spacing system from arbitrary padding values — what problem does constraint solve?"
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "letter-spacing"
    example: ".caps { letter-spacing: 0.05em; } /* 5-12% for caps/small caps */"
    support: baseline
---

# Quick Definition

Letterspacing (tracking) is the uniform adjustment of horizontal space between all letter pairs — mandatory at 5-12% for all caps and small caps, but generally unnecessary for lowercase body text.

# Core Definition

Butterick defines: "Letterspacing (also known as character spacing or tracking) is the adjustment of the horizontal white space between the letters in a block of text. Unlike kerning, which affects only designated pairs of letters, letterspacing affects every pair."

The key rule: "Capital letters usually appear at the beginning of a word or sentence, so they're designed to fit correctly next to lowercase letters. But when you use capital letters together, that spacing looks too tight. That's why you always add 5-12% extra letterspacing to text in all caps or small caps."

For lowercase: "Lowercase letters don't ordinarily need letterspacing."

# Prerequisites

- **Font** — Letterspacing adjusts the font's built-in character spacing.

# Key Properties

1. **Uniform adjustment**: Affects every letter pair equally (unlike kerning).
2. **5-12% for caps**: Mandatory when using all caps or small caps.
3. **Not for lowercase**: "Lowercase letters don't ordinarily need letterspacing."
4. **Size-sensitive**: Particularly important at small point sizes with caps.
5. **Don't overdo it**: "If the spaces between letters are large enough to fit more letters, you've gone overboard."
6. **Exception for small text**: Body text below 9pt may benefit from added letterspacing.

# Construction / Recognition

## To Construct/Create:
1. In CSS: `letter-spacing: 0.05em` to `0.12em` (5-12% of font size).
2. In Word: Font > Advanced > Spacing, enter 0.6-1.4 points per 12pt of font size.
3. Include letterspacing in paragraph/character styles that use caps or small caps.

## To Identify/Recognise:
1. Caps without letterspacing look cramped.
2. Over-letterspaced text has visible gaps between characters.

# Context & Application

- **Typical contexts**: All caps headings, small caps passages, very small text.
- **Common applications**: Navigation labels, acronyms, headings in caps.

# Examples

**Example 1** (letterspacing): Caps without letterspacing (too tight) vs. with 5-12% (comfortable).

**Example 2** (letterspacing): Frederic Goudy's famous quip: "Anyone who would letterspace lowercase would steal sheep."

# Relationships

## Builds Upon
- **Font** — Letterspacing modifies the font's default spacing.

## Contrasts With
- **Kerning** — Kerning adjusts specific pairs; letterspacing adjusts all pairs.

## Related
- **All Caps** — Always letterspace caps.
- **Small Caps** — Always letterspace small caps.

# Common Errors

- **Error**: Using all caps or small caps without adding letterspacing.
  **Correction**: Always add 5-12% extra letterspacing to caps and small caps text.

# Common Confusions

- **Confusion**: Letterspacing is the same as kerning.
  **Clarification**: Kerning adjusts specific pairs; letterspacing adjusts all pairs uniformly. Different tools for different problems.

# Source Reference

"Letterspacing" page. "Text Formatting" chapter.

# Verification Notes

- Definition source: Direct quotes from letterspacing.md.
- Confidence rationale: High — explicit percentage ranges and clear rules.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
