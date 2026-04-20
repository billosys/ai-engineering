---
# === CORE IDENTIFICATION ===
concept: Typographic Grids
slug: typographic-grids

# === CLASSIFICATION ===
category: layout-composition
subcategory: grid-systems
tier: intermediate
layer: 2-domain

# === PROVENANCE ===
source: "Butterick's Practical Typography"
source_slug: practical-typography
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Grids"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "layout grids"
  - "page grids"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - page-layout-maxims
extends: []
related:
  - page-margins
  - tables
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 7: What is a grid system, and what problem does it solve in visual composition?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "display: grid"
    example: ".layout { display: grid; grid-template-columns: 1fr 2fr; gap: 1rem; }"
    support: baseline
---

# Quick Definition

A typographic grid is a system of horizontal and vertical lines that guides layout choices toward consistency — useful as a starting point but not a guarantee of quality, because "if you take ugly shit and align it to a grid — it's still ugly shit."

# Core Definition

Butterick defines: "A grid is a system of horizontal and vertical lines that can guide layout choices." But he cautions: "In the words of Dutch designer Wim Crouwel, 'The grid is like the lines on a football field. You can play a great game in the grid or a lousy game.'"

Grids guide three things: "positioning (= where an element goes on a page), sizing (= the height and width of an element), or alignment (= how two elements relate to each other)."

Key principle: "A coarser, simpler grid encourages more consistency, because there are fewer ways to align items. A complicated grid, by contrast, might as well be no grid at all."

# Prerequisites

- **Page Layout Maxims** — Grids implement maxims #5 (consistency) and #6 (relate elements).

# Key Properties

1. **Guide, not guarantee**: "The grid might be the starting point. But the eye must always be the final judge."
2. **Three functions**: Positioning, sizing, alignment.
3. **Simpler is better**: Coarser grids encourage more consistency.
4. **Can be emergent**: "A grid can emerge from experimentation rather than being defined in advance."
5. **Not everything on-grid**: Some elements can deviate if they look right.
6. **Mathematical ratios optional**: "These ratios don't guarantee a good layout on their own."
7. **Music analogy**: "Music that was locked perfectly to a grid would sound sterile and boring."

# Construction / Recognition

## To Construct/Create:
1. Start with a simple grid (e.g., `1rem` or pica-based).
2. Derive a coarser grid for text block positioning.
3. Allow deviations when the eye demands them.
4. On the web: use CSS Grid or `rem`/`vw` units.

## To Identify/Recognise:
1. Consistent alignment of elements signals a grid.
2. Random or messy element placement suggests no grid (or too complex a grid).

# Context & Application

- **Typical contexts**: Page layouts, web designs, multi-element documents.
- **Common applications**: Aligning text blocks, images, and margins; creating consistent multi-page layouts.
- **Historical note**: "Grids have been part of page layout since the Gutenberg Bible."

# Examples

**Example 1** (grids): The 960 grid system — "proved that if you take ugly shit and align it to a grid — it's still ugly shit."

**Example 2** (grids): Butterick's music analogy — "performers don't rigidly adhere to these grids. Indeed, music that was locked perfectly to a grid would sound sterile and boring."

# Relationships

## Builds Upon
- **Page Layout Maxims** — Grids serve consistency (maxim #5) and element-relating (maxim #6).

## Related
- **Page Margins** — Margins define the grid's outer boundaries.
- **Tables** — Tables implement grid-like layouts at the content level.

# Common Errors

- **Error**: Treating grid alignment as sufficient proof of quality.
  **Correction**: "The eye must always be the final judge." Grid alignment is necessary but not sufficient.

# Common Confusions

- **Confusion**: Good layout requires a mathematical grid or modular scale.
  **Clarification**: Grids "don't have to be rigid or symmetric." Emergent grids from visual experimentation work as well as predefined ones.

# Source Reference

"Grids" page. "Page Layout" chapter.

# Verification Notes

- Definition source: Direct quotes from grids.md.
- Confidence rationale: High — five explicit tips with clear philosophy.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
