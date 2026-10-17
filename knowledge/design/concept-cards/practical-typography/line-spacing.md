---
concept: "Line Spacing"
slug: "line-spacing"
category: "typography"
subcategory: "type-formatting"
tier: "foundational"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Line Spacing"
extraction_confidence: "high"
aliases:
  - "leading"
  - "line height"
  - "vertical spacing"
prerequisites:
  - "body-text"
extends: []
related:
  - "point-size"
  - "line-length"
  - "font"
contrasts_with: []
answers_questions:
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"
  - "CQ 18: A card layout uses 16px padding inside cards, 16px between cards, and 16px between card title and body text. Everything feels 'flat.' What principle was violated, and what's the fix?"
rosetta_stone: []
css_implementation:
  -
    property: "line-height"
    example: "body { line-height: 1.35; } /* unitless preferred; 120-145% of font-size */"
    support: "baseline"
---

# Quick Definition

Line spacing (leading) is the vertical allocation between lines. Butterick recommends 120–145% as a rule of thumb for much text; suitability depends on the actual face, script, size, content and environment.

# Core Definition

Butterick recommends 120–145% for much text. Keep this attributed as his rule of thumb rather than a necessary or sufficient comfort test. The traditional term is *leading* (rhymes with *bedding*), named for the strips of lead placed between lines of metal type.

Butterick attributes single/double spacing to typewriter-era constraints. Whether a particular application preset or CSS value is too dense or loose depends on its actual computation and rendered text.

# Prerequisites

- **Body Text** — Line spacing is one of the four primary body text controls.

# Key Properties

1. **Source range**: 120–145% is Butterick’s recommendation, not a universal optimum.
2. **Named "leading"**: Historical term from metal strips between type lines.
3. **Application labels vary**: Butterick discusses typewriter-era conventions; test actual application and CSS output rather than inferring behavior from labels.
4. **Font-dependent**: Different faces may call for different leading; evaluate actual metrics and text.
5. **Document-length lever**: "Line spacing affects the length of a document more than point size."
6. **Application controls**: Butterick discusses "Exactly" and "Multiple" controls in his source context; available controls vary by application/version.

# Construction / Recognition

## To Construct/Create:
1. Treat 1.2–1.45 as Butterick’s candidate range, then evaluate actual line boxes, script and typeface.
2. Word and Pages controls and calibrations are source-era application examples; they are not fixed CSS values or current universal constants.
3. In CSS, a unitless `line-height` is inherited as a number and multiplies each element’s own font size; lengths and percentages compute differently. Review actual line boxes and wrapping.
4. Review actual text and intended reading conditions; this is a judgment check, not a universal comfort measure.

## To Identify/Recognise:
1. Review the rendered passage for the task and typeface; no single percentage diagnoses comfort across users and scripts.

# Context & Application

- **Typical contexts**: Every document and web page with running text.
- **Common applications**: Setting body text readability; adjusting document length.
- **Historical note**: The term "leading" comes from physical strips of lead in letterpress printing.

# Examples

**Example 1** (line-spacing): Butterick compares 110%, 135% and 170% for one paragraph and judges them in that context; these labels are not universal thresholds.

**Example 2** (line-spacing): "If you need to fit a document onto a certain number of pages, try adjusting the line spacing first."

# Relationships

## Builds Upon
- **Body Text** — Line spacing is one of body text's four primary controls.

## Related
- **Point Size** — Butterick relates leading to type size; CSS `line-height` has defined unitless, percentage and length computation rules.
- **Line Length** — Butterick recommends considering leading with measure; judge the actual text and face.
- **Font** — Different faces may call for different leading; review actual text.

# Common Errors

- **Error**: Treating application labels or source-era calibrations as CSS line-height values.
  **Correction**: Translate the intended visual relationship into the target system, then inspect it. CSS unitless, percentage and length values have different computation and inheritance behavior.

# Common Confusions

- **Confusion**: A word-processor “single” or “multiple” setting is interchangeable with a CSS value.
  **Clarification**: Application controls and CSS computation differ; assess the actual output.

# Source Reference

"Line Spacing" page. "Page Layout" chapter.

# Verification Notes

- Claim review: the concept and useful source recommendations are retained with explicit scope; technical corrections above are limited to the assigned paragraph-composition claims.
- Source basis: the prepared Practical Typography pages named in Source Reference were read. Historical extraction confidence is retained as provenance, not treated as proof of current technical correctness.
- Technical review: CSS units, line-height, measurement, paragraph spacing, hyphenation and fragmentation claims were checked against the cited specifications where applicable. No browser, assistive-technology, font-failure or readability study was run.
- Primary definitions: CSS Inline Layout [line-height §5.1](https://www.w3.org/TR/css-inline-3/#propdef-line-height).
- Source-fidelity limit: P10-11 original capture and conversion-fidelity evidence remains open; this correction does not verify fidelity to an immutable original.
- Relationships and competency-question contribution are reconciled in Slice19 batch record; they do not establish whole-card endpoint review or full-corpus closure.
