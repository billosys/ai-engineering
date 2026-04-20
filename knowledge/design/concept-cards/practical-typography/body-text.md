---
# === CORE IDENTIFICATION ===
concept: Body Text
slug: body-text

# === CLASSIFICATION ===
category: typography
subcategory: type-elements
tier: foundational
layer: 2-domain

# === PROVENANCE ===
source: "Butterick's Practical Typography"
source_slug: practical-typography
authors: "Matthew Butterick"
chapter: "Text Formatting"
chapter_number: null
pdf_page: null
section: "Body Text"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "body copy"
  - "running text"
  - "main text"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - typography
extends: []
related:
  - point-size
  - line-spacing
  - line-length
  - font
  - headings
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "CQ 1: What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?"
  - "CQ 12: How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient?"

# === VISUAL DESIGN EXTENSIONS ===
rosetta_stone: []

css_implementation:
  - property: "font-size, line-height, max-width"
    example: "body { font-size: clamp(1rem, 0.5rem + 1.5vi, 1.25rem); line-height: 1.35; max-width: 65ch; }"
    support: baseline
---

# Quick Definition

Body text is the default text of a document — the running paragraphs that make up the bulk of the content. Because there is more body text than anything else, it determines the overall typographic quality.

# Core Definition

Butterick identifies body text as the primary determinant of document quality: "The typographic quality of your document is determined largely by how the body text looks. Why? Because there's more body text than anything else. So start every project by making the body text look good. Then worry about the rest."

The appearance of body text is controlled by four primary decisions: point size, line spacing, line length, and font.

# Prerequisites

- **Typography** — Body text is the central element that typography governs.

# Key Properties

1. **Highest volume**: More body text than any other element in most documents.
2. **Four key controls**: Point size, line spacing, line length, and font.
3. **Priority element**: Should be designed first — everything else is secondary.
4. **Determines overall quality**: If body text looks good, the document looks good.

# Construction / Recognition

## To Construct/Create:
1. Choose a font (professional, not system default).
2. Set point size: 10-12pt in print, 15-25px on web.
3. Set line spacing: 120-145% of point size.
4. Set line length: 45-90 characters per line.
5. Evaluate by reading a full paragraph — it should feel comfortable and natural.

## To Identify/Recognise:
1. The default text style in a document — the running paragraphs.
2. Not headings, captions, footnotes, or other auxiliary text.

# Context & Application

- **Typical contexts**: Every document with running text — reports, articles, books, web pages, emails.
- **Common applications**: Setting the baseline typographic quality of any document; the first design decision in any project.

# Examples

**Example 1** (typography-in-ten-minutes): "The typographic quality of your document is determined largely by how the body text looks... So start every project by making the body text look good."

**Example 2** (body-text): Butterick recommends serif fonts for body text in print, but notes that on screen, both serif and sans-serif can work well.

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

- **Error**: Spending time on headings, logos, or decorative elements before setting body text.
  **Correction**: Always start with body text — it has the biggest impact on overall quality.

# Common Confusions

- **Confusion**: Body text is the least important element because it's "just the regular text."
  **Clarification**: Body text is the MOST important because it constitutes the majority of the document. Getting body text right is the single biggest improvement you can make.

# Source Reference

"Body Text" page and "Typography in Ten Minutes" page. "Text Formatting" chapter.

# Verification Notes

- Definition source: Direct quotes from body-text.md and typography-in-ten-minutes.md.
- Confidence rationale: High — Butterick is emphatic and explicit about body text's primacy.
- Uncertainties: None.
- Cross-reference status: All referenced slugs correspond to planned cards.
- Rosetta Stone check: Checked against 0010 tables. No direct mappings found.
- OCR issues: None — HTML conversion.
