---
concept: "Point Size"
slug: "point-size"
category: "typography"
subcategory: "type-formatting"
tier: "foundational"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Text Formatting"
chapter_number: null
pdf_page: null
section: "Point Size"
extraction_confidence: "high"
aliases:
  - "font size"
  - "type size"
  - "text size"
prerequisites:
  - "body-text"
extends: []
related:
  - "line-spacing"
  - "line-length"
  - "em-unit"
  - "headings"
contrasts_with: []
answers_questions:
  - "CQ 5: What are the basic anatomical parts of a letterform (baseline, x-height, cap height, ascender, descender, counter)?"
  - "CQ 19: A landing page hero section uses a 14px body font, a 16px heading, and a 14px subheading. Why does it feel like nothing stands out?"
rosetta_stone: []
css_implementation:
  -
    property: "font-size"
    example: "body { font-size: 18px; } /* web body text: 15-25px range */"
    support: "baseline"
---

# Quick Definition

Point size is a nominal type-size measure, not a direct measure of visible letter height. Butterick recommends 10–12pt for print body text and 15–25px for web body text; these are contextual suggestions, not universal or accessibility thresholds.

# Core Definition

Butterick recommends 10–12pt print and 15–25px web body text. Preserve these as his rules of thumb, not universal optima: rendered appearance depends on the typeface, script, content, environment and reader settings.

Crucially, the point-size system is not absolute: "different fonts set at the same point size won't necessarily appear the same on the page." This is because digital fonts are drawn inside a rectangle called the em, and "Two fonts set at the same point size will appear to be different sizes if one occupies less space on its em."

CSS defines 72pt per CSS inch and 96px per CSS inch. These are CSS reference lengths, not promises about physical screen inches or device pixels. Butterick’s half-point emphasis advice is a source recommendation to evaluate in context.

# Prerequisites

- **Body Text** — Point size is one of the four primary body text controls.

# Key Properties

1. A nominal size does not equal cap height, x-height, visible glyph bounds or line-box height.
2. Different fonts can look different at the same nominal size.
3. The 10–12pt print and 15–25px web ranges and half-point emphasis are Butterick’s recommendations, not universal thresholds.
4. CSS points and pixels are reference lengths; do not equate CSS px with physical/device pixels.
5. Compare actual content and preserve user text resizing.

# Construction / Recognition

## To Construct/Create:
1. Use Butterick’s suggested ranges only as candidates; choose from the task, script, content and user needs.
2. Compare representative rendered content, not numbers alone.
3. Butterick’s half-point increments are examples to consider, not a universal threshold.
4. When matching fonts, adjust point size until text blocks occupy the same space.

## To Identify/Recognise:
1. Cannot be determined by measurement alone — only by matching against a known sample in the same font.

# Context & Application

- **Typical contexts**: Documents and websites where text size must be chosen or reviewed.
- **Common applications**: Setting body text size; creating heading hierarchy through size variation; matching fonts across documents.
- **Historical note**: Butterick discusses historical conventions; this card does not establish the cause of any current default or a universal readability optimum.

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
- **Em Unit** — Nominal size relates to the em coordinate space, not a fixed cap height, x-height or visible outline extent.
- **Line Spacing** — Review leading when point size changes; the suitable line box depends on the face and actual content.
- **Line Length** — Affected by point size choice.

# Common Errors

- **Error**: Using the 12pt default without evaluating whether it's appropriate.
  **Correction**: Use Butterick’s print range as an attributed starting point; review the typeface, script, output conditions and reader needs.

- **Error**: Doubling point size for headings (e.g., 12pt body to 24pt heading).
  **Correction**: "There is no typographic universe in which you need to double the point size to achieve emphasis." Use subtler increments.

# Common Confusions

- **Confusion**: Nominal size specifies visible letter height.
  **Clarification**: It does not specify cap height, x-height or all glyph bounds; inspect the actual face and rendered text.

# Source Reference

"Point Size" page. "Text Formatting" chapter.

# Verification Notes

- Claim review: the concept and useful source recommendations are retained with explicit scope; technical corrections above are limited to the assigned paragraph-composition claims.
- Source basis: the prepared Practical Typography pages named in Source Reference were read. Historical extraction confidence is retained as provenance, not treated as proof of current technical correctness.
- Technical review: CSS units, line-height, measurement, paragraph spacing, hyphenation and fragmentation claims were checked against the cited specifications where applicable. No browser, assistive-technology, font-failure or readability study was run.
- Primary definitions: CSS Values and Units [absolute lengths §6.2](https://www.w3.org/TR/css-values-4/#absolute-lengths) and [font-relative lengths §6.1.1](https://www.w3.org/TR/css-values-4/#font-relative-lengths); OpenType [FUnits and the em square](https://learn.microsoft.com/en-us/typography/opentype/spec/ttch01#funits-and-the-em-square).
- Source-fidelity limit: P10-11 original capture and conversion-fidelity evidence remains open; this correction does not verify fidelity to an immutable original.
- Relationships and competency-question contribution are reconciled in Slice19 batch record; they do not establish whole-card endpoint review or full-corpus closure.
