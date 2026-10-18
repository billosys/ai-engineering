---
concept: "Headings"
slug: "headings"
category: "typography"
subcategory: "type-elements"
tier: "intermediate"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Text Formatting"
chapter_number: null
pdf_page: null
section: "Headings"
extraction_confidence: "high"
aliases:
  - "headers"
  - "heading hierarchy"
prerequisites:
  - "body-text"
  - "typographic-emphasis"
  - "point-size"
extends: []
related:
  - "all-caps"
  - "typographic-color"
  - "line-spacing"
contrasts_with: []
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"
  - "CQ 19: A landing page hero section uses a 14px body font, a 16px heading, and a 14px subheading. Why does it feel like nothing stands out?"
rosetta_stone: []
css_implementation:
  -
    property: "font-size, font-weight, margin"
    example: "h2 { font-size: 1.1em; font-weight: bold; margin-top: 1.5em; margin-bottom: 0.5em; }"
    support: "baseline"
---

# Quick Definition

Headings are structural signposts whose visual treatment can distinguish levels and guide scanning; choose their semantic level from the content structure, then style them for the task.

# Core Definition

Butterick recommends clear contrast between headings and surrounding text, with spacing and restrained type choices. His preferences for two or three levels, subtle size increments, and avoiding caps or centering are contextual advice, not universal rules. The document's hierarchy comes from its content structure; CSS size does not determine the HTML heading level.

# Prerequisites

- **Body Text** — A heading's treatment is judged in relation to surrounding text.
- **Typographic Emphasis** — Weight, size, and other emphasis choices may help distinguish levels, depending on available faces.
- **Point Size** — Size can contribute to visual hierarchy; no specific increment is required.

# Key Properties

1. **Structural role**: Select the heading element/level from the outline and relationships of the content.
2. **Visible distinction**: Use size, weight, spacing, colour, or other properties as appropriate to create a perceivable hierarchy.
3. **Contextual levels**: Two or three visual levels may be enough in a short document, but the needed structure varies.
4. **Available face matters**: Check whether the intended bold or italic face exists; a serif/sans label alone does not establish its appearance.
5. **Output behavior**: Breaks and keep-with-next settings need checking in the actual medium; advice about page composition is not a browser pagination guarantee.

# Construction / Recognition

## To Construct/Create:
1. Outline the content and choose semantic heading levels from that structure.
2. Assign visual styles that make levels and their relation to body text clear.
3. Compare size, weight, spacing, and colour on actual content; a scale can help but does not prove correctness or beauty.
4. Preserve reading order and check breaks in the intended output.

## To Identify/Recognise:
1. Check that headings communicate the document outline and are visually distinguishable.
2. A CSS size change alone does not justify changing the semantic level.

# Context & Application

Use in documents, web pages, and interfaces. A 12-to-12.5-point increment may be too subtle in one context; 12-to-24 points may be suitable in another. Neither choice is intrinsically correct or wrong without the content and output.

# Examples

**Example 1** (headings): Butterick's `5(a)(1)(iv)` example shows how deeply nested signposting can leave a heading over-formatted and hard to scan. Inspect whether the content structure needs that many levels and whether the visual treatment makes the hierarchy legible; the example is not a universal level ban.

**Example 2** (headings): Butterick notes that a relatively heavy bold heading can look darker than intended; trying it half a point or a full point smaller may optically compensate. Compare relative weight, size, spacing, and signposting in context rather than always enlarging headings.

# Relationships

## Builds Upon
- **Body Text** — Visual heading hierarchy is seen against surrounding body text; this does not determine the semantic outline.
- **Typographic Emphasis** — Weight and size variation can contribute to the visual treatment when appropriate.
- **Point Size** — Size can distinguish a heading, but no fixed increment or point-size hierarchy is established here.

## Related
- **All Caps** — Caps are one possible treatment; Butterick advises against them in headings, a contextual preference rather than a ban.
- **Typographic Color** — Colour can contribute to contrast; evaluate actual foreground/background pairs.
- **Line Spacing** — Space around a heading can distinguish it; “best” is context-dependent and the endpoint's broader claim is not accepted here.

# Common Errors

- **Error**: Choosing an HTML heading level to obtain a desired font size.
  **Correction**: Keep the semantic level aligned with content structure and set visual appearance separately.

# Common Confusions

- **Confusion**: A heading is defined by bold or large styling.
  **Clarification**: Structure gives the heading its semantic role; CSS appearance is separate. HTML heading elements represent section headings, not merely visual styles.

# Source Reference

"Headings" page. "Text Formatting" chapter.

# Verification Notes

- Teaching focus: derive semantic levels from structure; distinguish levels visually; use multiple possible visual properties; select sizes and spacing contextually; inspect actual reading order and output behavior. These focus points are separate from the five review dimensions recorded in the batch assessment.
- Support: Butterick's page provides contextual visual advice. The HTML Standard defines headings structurally and distinguishes `em` stress from `strong` importance; the full guide is the source for the semantics distinction.
- Limitation: no rendered document, browser pagination, or assistive-technology output was tested. HTML semantics do not guarantee a particular visual result.
- Confidence records extraction confidence, not proof that a particular hierarchy works for every audience.
- Cross-reference identities and literal source reference are retained. Original capture fidelity remains a Project10-11 dependency.
