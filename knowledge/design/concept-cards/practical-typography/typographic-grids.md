---
concept: "Typographic Grids"
slug: "typographic-grids"
category: "layout-composition"
subcategory: "grid-systems"
tier: "intermediate"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Page Layout"
chapter_number: null
pdf_page: null
section: "Grids"
extraction_confidence: "high"
aliases:
  - "layout grids"
  - "page grids"
prerequisites:
  - "page-layout-maxims"
extends: []
related:
  - "page-margins"
  - "tables"
contrasts_with: []
answers_questions:
  - "CQ 7: What is a grid system, and what problem does it solve in visual composition?"
rosetta_stone: []
css_implementation:
  -
    property: "display: grid"
    example: ".layout { display: grid; grid-template-columns: 1fr 2fr; gap: 1rem; }"
    support: "baseline"
---

# Quick Definition

A typographic grid is a set of horizontal and vertical references for positioning, sizing and aligning content. It can make repeated relationships easier to coordinate; grid alignment is neither necessary nor sufficient for good composition.

# Core Definition

Butterick defines the grid as a guide to layout choices and uses Wim Crouwel's football-field analogy: the same field can host a good or poor game. The guide can organize positioning, size and alignment without deciding whether those choices serve the content.

His preference for a coarser, simpler grid reduces the number of alignment choices. Treat that as a starting option, not proof that complex grids are bad. Grids can emerge through experimentation, accommodate asymmetry and allow deliberate deviations when content or optical judgment calls for them.

A conceptual typographic grid need not use CSS Grid. The latter is a particular web layout mechanism. Proportional choices, font-relative units and viewport units are options, not required values or quality guarantees. [CSS Grid's ordering guidance](https://www.w3.org/TR/css-grid-2/#order-accessibility) distinguishes visual placement from meaningful source order; visual reordering cannot repair a broken reading sequence.

# Prerequisites

- **Page Layout Maxims** — Consistency and relating elements explain why a grid can help; the maxims do not require one.

# Key Properties

1. **Guidance**: Coordinates references without guaranteeing a successful result.
2. **Three uses**: Position, size and alignment can share repeatable relationships.
3. **Contextual complexity**: Start simply when useful; add tracks or exceptions to serve actual content.
4. **Emergence**: Alignment choices can reveal a grid after experimentation.
5. **Deliberate deviation**: Not every element needs the same reference or interval.
6. **Optional proportions**: Ratios or units can coordinate choices without establishing harmony.
7. **Meaningful order**: Preserve the source sequence alongside visual arrangement; actual output still needs review.

# Construction / Recognition

## To Construct/Create:
1. Identify repeated relationships and content constraints before choosing a mechanism.
2. Try a small set of horizontal/vertical references or an emergent alignment scheme.
3. Coordinate positions, dimensions and spaces where that serves the task; add complexity for content needs.
4. Keep justified optical deviations, asymmetry and semantic source order.
5. On the web, choose suitable CSS mechanisms and inspect enlarged text, fallback, reflow and reading order in actual output.

## To Identify/Recognise:
1. Repeated alignment references can reveal a grid even when it is not visibly drawn.
2. Disorder does not prove the absence of a grid; an existing grid may fail to serve the content. An ungridded composition can also work.

# Context & Application

- **Typical contexts**: Multi-element documents, page spreads and web compositions with recurring relationships.
- **Common applications**: Coordinating text blocks, images, margins and interior spacing across instances.
- **Historical note**: Butterick reports grids in the Gutenberg Bible and describes an illustrated spread; this batch does not independently verify that history or the original illustration.

# Examples

**Example 1** (grids): Butterick criticizes confidence in the 960px grid system as sufficient for quality. His forceful example and Crouwel's football analogy illustrate that alignment alone cannot judge a page; they are not a measured comparison of 960px designs.

**Example 2** (grids): Butterick responds to Bringhurst's musical-scale analogy by emphasizing performers' deviations and the typographer's eye. This is an attributed analogy, not a universal law that rhythm locked to a grid is sterile or that musical ratios improve visual quality.

His practical examples start with a 1rem grid tied to the viewport through a media query, or 1vw, and with a print pica grid (one pica = 12pt). He derives a coarser grid for text blocks while allowing indents of 2.5 picas (= 30pt). These are source options; this guide prescribes none of those units, values or mechanisms. He also dislikes baseline-grid rigidity for his book/web work while acknowledging their use in wide multicolumn layouts.

# Relationships

## Builds Upon
- **Page Layout Maxims** — Shared alignment references can serve consistency and relating new elements, the source's maxims #5 and #6.

## Related
- **Page Margins** — Margins can supply outer references, while grid relationships may also organize interior content and spacing.
- **Tables** — Tables have grid-like alignment; tabular data adds meaningful row/column associations that arbitrary layout tracks do not supply.

# Common Errors

- **Error**: Treating alignment, a simple grid or CSS Grid as a necessary or sufficient quality test.
  **Correction**: Check whether relationships serve content, semantics and context, allowing justified differences. Review actual output where behavior matters.

# Common Confusions

- **Confusion**: A conceptual grid requires mathematical ratios, symmetric tracks or a particular CSS mechanism.
  **Clarification**: It can emerge from coordinated choices and admit exceptions. No general equivalence in quality between emergent and predefined grids is established here.

# Source Reference

"Grids" page. "Page Layout" chapter.

# Verification Notes

- Available-source comparison: whole prepared grids.md; football, 960px, pica, rem/vw and music examples retained with attribution. Original illustration/capture fidelity remains P10-11-blocked.
- Correctness/scope: conceptual grid separated from CSS Grid; repeatable references address coordination, not proof of beauty. Current Grid ordering guidance supports the source-order limit, not observed browser behavior.
- Local outcome: one prerequisite and two related premises checked; CQ 7's conceptual definition and coordination problem can be answered locally. No rendered quality, global union or historical acceptance follows.
- Prior extraction confidence, metadata and conversion/Rosetta observations remain historical, not refreshed uncertainty-free verification.
- Unrun: actual visual/browser/enlargement/AT, hosted output and full-corpus reconciliation.
