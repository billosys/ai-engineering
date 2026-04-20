---
# === CORE IDENTIFICATION ===
concept: Line Spacing
slug: line-spacing

# === CLASSIFICATION ===
category: typography
subcategory: type-formatting
tier: foundational
layer: 2-domain

# === PROVENANCE ===
source: "Butterick's Practical Typography"
source_slug: practical-typography
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Line Spacing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "leading"
  - "line height"
  - "vertical spacing"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - body-text
extends: []
related:
  - point-size
  - line-length
  - font
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"
  - "CQ 18: A card layout uses 16px padding inside cards, 16px between cards, and 16px between card title and body text. Everything feels 'flat.' What principle was violated, and what's the fix?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "line-height"
    example: "body { line-height: 1.35; } /* unitless preferred; 120-145% of font-size */"
    support: baseline
---

# Quick Definition

Line spacing (leading) is the vertical distance between lines of text — optimally 120–145% of the point size, replacing the typewriter-era binary of single or double spacing.

# Core Definition

Butterick states: "For most text, the optimal line spacing is between 120% and 145% of the point size." The traditional term is *leading* (rhymes with *bedding*), named for the strips of lead placed between lines of metal type.

The single/double spacing convention is a typewriter-era limitation: "Originally, a typewriter's platen could only move the paper vertically in units of a single line." Single-spaced text is too dense; double-spaced text is too loose. Neither hits the optimal range.

# Prerequisites

- **Body Text** — Line spacing is one of the four primary body text controls.

# Key Properties

1. **Optimal range**: 120–145% of the point size.
2. **Named "leading"**: Historical term from metal strips between type lines.
3. **Not single or double**: Both are typewriter-era approximations that miss the target.
4. **Font-dependent**: Fonts that appear smaller at the same point size need less line spacing.
5. **Document-length lever**: "Line spacing affects the length of a document more than point size."
6. **Fine control**: Word processors allow precise values via "Exactly" or "Multiple" settings.

# Construction / Recognition

## To Construct/Create:
1. Multiply the point size by 1.2 to 1.45 to get the target range.
2. In Word, use "Exactly" and enter a fixed measurement, or use "Multiple" with values of 1.03–1.24.
3. In CSS, use unitless `line-height` (e.g., `1.35`).
4. Evaluate by reading — the text should feel comfortable, neither cramped nor drifting apart.

## To Identify/Recognise:
1. Text that feels cramped has line spacing below 120%.
2. Text that feels disconnected or "floaty" has line spacing above 145%.

# Context & Application

- **Typical contexts**: Every document and web page with running text.
- **Common applications**: Setting body text readability; adjusting document length.
- **Historical note**: The term "leading" comes from physical strips of lead in letterpress printing.

# Examples

**Example 1** (line-spacing): Butterick shows three versions of the same paragraph at 110% (too tight), 135% (fine), and 170% (too loose).

**Example 2** (line-spacing): "If you need to fit a document onto a certain number of pages, try adjusting the line spacing first."

# Relationships

## Builds Upon
- **Body Text** — Line spacing is one of body text's four primary controls.

## Related
- **Point Size** — Line spacing is calculated as a percentage of point size.
- **Line Length** — Longer lines need more line spacing for vertical tracking.
- **Font** — Different fonts at the same point size may need different line spacing.

# Common Errors

- **Error**: Using only single or double spacing because those are the word processor presets.
  **Correction**: These are typewriter holdovers. Use precise values in the 120–145% range. In Word, "Single" is about 117% and "Double" is about 233% — both miss the target.

# Common Confusions

- **Confusion**: "Single spacing" means optimal line spacing.
  **Clarification**: Single spacing (~117%) is slightly below the optimal 120–145% range. Double spacing (~233%) is far above it. Neither is optimal.

# Source Reference

"Line Spacing" page. "Page Layout" chapter.

# Verification Notes

- Definition source: Direct quotes from line-spacing.md.
- Confidence rationale: High — explicit percentage ranges and clear explanations.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
