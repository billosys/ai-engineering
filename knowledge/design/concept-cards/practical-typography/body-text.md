---
concept: "Body Text"
slug: "body-text"
category: "typography"
subcategory: "type-elements"
tier: "foundational"
layer: "2-domain"
source: "Butterick's Practical Typography"
source_slug: "practical-typography"
authors: "Matthew Butterick"
chapter: "Text Formatting"
chapter_number: null
pdf_page: null
section: "Body Text"
extraction_confidence: "high"
aliases:
  - "body copy"
  - "running text"
  - "main text"
prerequisites:
  - "typography"
extends: []
related:
  - "point-size"
  - "line-spacing"
  - "line-length"
  - "font"
  - "headings"
contrasts_with: []
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"
rosetta_stone: []
css_implementation:
  -
    property: "font-size, line-height, max-width"
    example: ".prose { font-size: 1rem; line-height: 1.35; max-width: 65ch; } /* illustrative; test actual text, fonts and user overrides */"
    support: "baseline"
---

# Quick Definition

Body text is the running prose of a document. Where prose dominates, reviewing it early is a useful way to establish a candidate type treatment; task, interface, language and supplied identity may make other content equally important.

# Core Definition

Butterick recommends starting with body text because it occupies much of many documents and strongly affects their overall appearance. Treat this as useful advice for prose-dominated work, not a universal priority or a guarantee of quality.

The appearance of body text is controlled by four primary decisions: point size, line spacing, line length, and font.

# Prerequisites

- **Typography** — Body text is the central element that typography governs.

# Key Properties

1. **Highest volume**: More body text than any other element in most documents.
2. **Four key controls**: Point size, line spacing, line length, and font.
3. **Contextual priority**: Often useful to review early when prose dominates, while other tasks may have different priorities.
4. **One contribution**: Body text affects a document, but does not alone establish its overall quality.

# Construction / Recognition

## To Construct/Create:
1. Preserve supplied typefaces and assets; compare available candidates with representative content and suitable fallbacks.
2. Treat Butterick’s 10–12pt print and 15–25px web suggestions as his recommendations, not thresholds for every script, audience or device.
3. Treat his 120–145% leading and 45–90 character measure suggestions as starting points; inspect rendered lines and the actual reading task.
4. Review a representative passage with the intended fonts, language and layout, then check user enlargement and reflow. These checks do not establish conformance or universal comfort.

## To Identify/Recognise:
1. The default text style in a document — the running paragraphs.
2. Not headings, captions, footnotes, or other auxiliary text.

# Context & Application

- **Typical contexts**: Documents with running text, including reports, articles, books, web pages and emails.
- **Common applications**: Establishing a candidate treatment for prose-heavy content; another task or supplied identity may lead the work.

# Examples

**Example 1** (typography-in-ten-minutes): Butterick’s prose-first recommendation is useful when running text dominates; it is not a universal project sequence or proof of quality.

**Example 2** (body-text): Butterick recommends serif fonts for body text in print while noting that both serif and sans-serif can work on screen; treat these as contextual source recommendations.

# Relationships

## Builds Upon
- **Typography** — Body text is the primary application of typographic skill.

## Enables
- **Point Size** — Point size is one of the four body text controls.
- **Line Spacing** — Line spacing is one of the four body text controls.
- **Line Length** — Line length is one of the four body text controls.
- **Font** — Font is one of the four body text controls.

## Related
- **Headings** — Headings contrast with and supplement body text.

# Common Errors

- **Error**: Treating a source recommendation as a universal sequence.
  **Correction**: For prose-heavy work, beginning with a representative body passage can expose useful type and measure choices. Follow the task and supplied identity where another element leads.

# Common Confusions

- **Confusion**: Body text has the same priority in every artifact.
  **Clarification**: Its prominence depends on content and task. Butterick’s emphasis explains his advice for documents dominated by prose; it is not a quality guarantee.

# Source Reference

"Body Text" page and "Typography in Ten Minutes" page. "Text Formatting" chapter.

# Verification Notes

- Claim review: the concept and useful source recommendations are retained with explicit scope; technical corrections above are limited to the assigned paragraph-composition claims.
- Source basis: the prepared Practical Typography pages named in Source Reference were read. Historical extraction confidence is retained as provenance, not treated as proof of current technical correctness.
- Technical review: CSS units, line-height, measurement, paragraph spacing, hyphenation and fragmentation claims were checked against the cited specifications where applicable. No browser, assistive-technology, font-failure or readability study was run.
- Primary definitions: CSS Values and Units [font-relative lengths §6.1.1](https://www.w3.org/TR/css-values-4/#font-relative-lengths) and [absolute lengths §6.2](https://www.w3.org/TR/css-values-4/#absolute-lengths) support the unit distinctions; no behavioral usability test was run.
- Source-fidelity limit: P10-11 original capture and conversion-fidelity evidence remains open; this correction does not verify fidelity to an immutable original.
- Relationships and competency-question contribution are reconciled in Slice19 batch record; they do not establish whole-card endpoint review or full-corpus closure.
