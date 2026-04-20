---
# === CORE IDENTIFICATION ===
concept: Paragraph Flow Control
slug: paragraph-flow-control

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
section: "Widow and Orphan Control"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "widow and orphan control"
  - "straggler control"
  - "page break management"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - body-text
extends: []
related:
  - line-spacing
  - headings
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []
css_implementation: []
---

# Quick Definition

Widow and orphan control prevents single paragraph lines from appearing isolated at the top (widow) or bottom (orphan) of a page — optional, since the blank lines it creates at page bottoms can be more annoying than the problem it solves.

# Core Definition

Butterick defines: "When only the last line of the paragraph appears at the top of the second page, that line is called a widow. When only the first line of the paragraph appears at the bottom of the first page, that line is called an orphan."

His stance is pragmatic: "Do you need widow and orphan control? Try it. See how it looks." He approaches it like ligatures — "I only use it if widows and orphans are causing a visible problem. Otherwise, I find that the blank lines at the bottom of the page are more annoying."

Widows are more distracting than orphans because "widows can be any length, even a single word."

# Prerequisites

- **Body Text** — Widow/orphan control manages body text flow across pages.

# Key Properties

1. **Widows**: Last line of paragraph alone at top of next page.
2. **Orphans**: First line of paragraph alone at bottom of page.
3. **All-or-nothing**: Word processors can't control widows and orphans separately.
4. **Trade-off**: Curing them creates blank lines at page bottoms.
5. **Optional**: Use only if the problems are visually distracting.
6. **Widows worse than orphans**: Widows can be a single word; orphans are at least a full line.
7. **Not applicable to web**: Web content doesn't span pages.

# Construction / Recognition

## To Construct/Create:
1. In Word: Paragraph > Line and Page Breaks > Widow/Orphan control.
2. In Pages: Format > More > Prevent widow & orphan lines.
3. Evaluate whether the cure (blank lines) is worse than the disease.
4. Fix individual widows with judicious editing rather than global settings.

## To Identify/Recognise:
1. Widow: a short line (possibly one word) alone at the top of a page.
2. Orphan: first line of a paragraph alone at the bottom of a page.

# Examples

**Example 1** (widow-and-orphan-control): Butterick's pragmatic approach — "Try it. See how it looks."

# Relationships

## Builds Upon
- **Body Text** — A body text page-flow concern.

## Related
- **Line Spacing** — Line spacing adjustments can mitigate widows/orphans.
- **Headings** — Keep-with-next prevents headings from orphaning.

# Common Errors

- **Error**: Always enabling widow and orphan control without evaluating the result.
  **Correction**: Check whether the blank lines at page bottoms are more or less distracting than the widows and orphans themselves.

# Common Confusions

- **Confusion**: Widows and orphans are equally problematic.
  **Clarification**: Widows are more distracting because they "can be any length, even a single word." Orphans are at least a full line.

# Source Reference

"Widow and Orphan Control" page. "Page Layout" chapter.

# Verification Notes

- Definition source: Direct quotes from widow-and-orphan-control.md.
- Confidence rationale: High — clear definitions and pragmatic advice.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
