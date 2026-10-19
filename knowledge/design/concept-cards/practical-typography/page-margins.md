---
concept: "Page Margins"
slug: "page-margins"
category: "layout-composition"
subcategory: "spacing-systems"
tier: "intermediate"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Page Margins"
extraction_confidence: "high"
aliases:
  - "margins"
  - "page insets"
prerequisites:
  - "line-length"
extends: []
related:
  - "body-text"
  - "typographic-grids"
  - "responsive-typography"
contrasts_with: []
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "CQ 7: What is a grid system, and what problem does it solve in visual composition?"
rosetta_stone: []
css_implementation:
  -
    property: "margin, padding, max-width"
    example: ".content { max-width: 65ch; margin: 0 auto; padding: 0 2rem; }"
    support: "baseline"
---

# Quick Definition

Page margins bound the available text area and interact with measure, type and medium. Butterick's wider US-letter print margins are contextual recommendations; there is no inch-based default for all print or web text.

# Core Definition

For a single text block on a page of fixed width, increasing left/right margins reduces its available width. On 8.5″ × 11″ US-letter paper, one-inch side margins leave 6.5 inches; two-inch side margins leave 4.5 inches. These dimensions do not establish actual character counts or legibility.

Butterick criticizes the one-inch word-processor default for proportional type on US-letter paper and suggests 1.5–2.0-inch sides at 12pt. He explicitly says not to treat that range as absolute: judge line length with the actual font and passage. This is print advice, not a web default or a universal rejection of one-inch margins.

His web advice also centers on measure. A containing block, `max-width`, padding and margins can constrain running text as available width changes. The existing `65ch` CSS example is a candidate: `ch` uses the zero glyph advance with specification fallbacks, not an exact character count. Text, shaping, spaces and fallback affect actual line composition.

A gutter is additional inner-edge space for binding; it changes sides in a mirrored duplex layout. Margins need not be symmetric. Butterick suggests trying a bottom margin about 0.25 inch larger for apparent vertical centering, or at least a 1-inch left/right difference for obvious asymmetry. Both are optical suggestions in print, not mandatory offsets.

# Prerequisites

- **Line Length** — Understanding measure helps assess margins; width alone is not a complete readability test.

# Key Properties

1. **Available measure**: Outer margins constrain a single text block; columns and other containers can constrain it further.
2. **Print context**: Butterick's 1.5–2.0 inches assumes his 12pt US-letter example, not every page or font.
3. **Actual lines**: His 45–90-character rule of thumb is contextual; inspect the actual passage rather than infer character count from `ch` or inches.
4. **White space**: Space can serve framing, hierarchy and navigation without proving a particular reader response.
5. **Gutter**: Binding space serves a production need and may alternate inner sides.
6. **Asymmetry**: Unequal margins are possible; his 1-inch and 0.25-inch adjustments are optional print candidates.
7. **Web adaptation**: Fit the container and reading context; neither fixed-inch margins nor viewport-scaled type is required.

# Construction / Recognition

## To Construct/Create:
1. Identify the page/container, medium, binding and content roles.
2. Choose candidate measure, font, size and leading together; test actual lines.
3. For Butterick's 12pt US-letter scenario, compare his suggested margins with the task's constraints.
4. On the web, constrain the text container while preserving usable width under enlargement and reflow.
5. Adjust asymmetry or vertical position only where the actual composition benefits.

## To Identify/Recognise:
1. Wide or cramped lines call for inspecting font, size, containers and margins together.
2. Extra white space is neither proof of waste nor proof of better reading; inspect the task and output.

# Examples

**Example 1** (page-margins): Butterick's US-letter exercise uses the same text of at least 1000 words in two word-processor documents. A has 1″ margins on every side, Times New Roman 12pt, Word “Double” leading (reported as 28pt; otherwise use exactly 28pt), a 0.5″ first-line indent and no paragraph gaps. B has 2″ margins on every side, Times New Roman 11pt, exactly 15pt leading, the same 0.5″ indent and no paragraph gaps. He asks the reader to print, compare book-like appearance and comfort, and use word count to compare words per page; he guesses the reader answers B to all three. This record did not render/print the documents or measure their counts. Size, leading and available area all change, so the example does not isolate a margin effect.

**Example 2** (page-margins): Butterick invokes magazines using columns and books using smaller sheets to argue against treating US-letter dimensions as a typographic ideal. His “never” rhetoric and account of 1921/1980 US-government paper standards are attributed source statements, not independently verified history or a claim that no book uses letter dimensions.

His optional ratio example uses 2.23″ margins on US-letter: the text block is 4.04″ × 6.54″, a height/width ratio of about 1.619. That arithmetic is close to the golden ratio; it establishes neither visual quality nor a required layout.

# Relationships

## Builds Upon
- **Line Length** — Measure supplies a reason to choose margins; they are one control among font, size, columns and container constraints.

## Related
- **Body Text** — Margins frame prose when the page contains running text; they need not determine every content role.
- **Typographic Grids** — Margins can supply outer alignment references for a conceptual grid; not every grid is bounded by page margins.
- **Responsive Typography** — Container and margin choices may adapt with available width and content; font size need not track the viewport.

# Common Errors

- **Error**: Applying a one-inch default or a 1.5–2.0-inch correction to all media.
  **Correction**: Retain the source's print assumptions, then assess actual measure and constraints. Web text can use bounded containers and contextual insets.

# Common Confusions

- **Confusion**: Wider margins alone guarantee either fewer words per page or more comfortable reading.
  **Clarification**: Word count also depends on font, leading, page area and content. Butterick's A/B exercise changes several variables and reports an expected judgment; it is not a measured result here.

# Source Reference

"Page Margins" page. "Page Layout" chapter.

# Verification Notes

- Available-source comparison: whole prepared page-margins.md; print/web distinction, gutter, both source examples, optical offsets and ratio illustration retained with scope. Original capture/lineage remains P10-11-blocked.
- Correctness: 6.5″/4.5″ measures and 4.04″ × 6.54″ ratio are arithmetic only; no word counts, comfort, paper history or rendered results were verified.
- Local outcome: one prerequisite and three related premises checked. CQ 1 receives framing/role-spacing and CQ 7 outer grid-reference components; neither accepts their global unions.
- Historical confidence/metadata and conversion/Rosetta observations are not refreshed semantic or original-fidelity results.
- Unrun: actual print/browser/enlargement/AT, hosted output and full-corpus reconciliation.
