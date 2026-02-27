---
# === CORE IDENTIFICATION ===
concept: Content Processing Pipeline
slug: content-processing-pipeline

# === CLASSIFICATION ===
category: content
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Pages"
chapter_number: null
pdf_page: null
section: "Pages"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "page transformation pipeline"
  - "content transformation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - page
extends: []
related:
  - liquid-template-language
  - layout
  - format-field
  - cobalt-build
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a page in Cobalt?"
---

# Quick Definition

The content processing pipeline is the four-step transformation that every Cobalt page undergoes: Liquid template evaluation, Markdown-to-HTML conversion (for `.md` files), layout wrapping, and writing the result to the destination directory.

# Core Definition

When Cobalt builds a site, each page goes through a defined sequence of transformations: (1) Evaluate Liquid template expressions in the content, (2) if the file has an `.md` extension, convert the Markdown content to HTML, (3) wrap the resulting content in a Liquid layout template (if a layout is specified), and (4) write the final results to a parallel location in the `destination` directory with an `.html` extension. This pipeline can be customized via frontmatter -- for example, the `format` field controls whether Markdown conversion occurs, and the `layout` field determines which template wraps the content. (Source: Cobalt Pages documentation)

# Prerequisites

- **[Page](/concept-cards/cobalt/page.md)** -- The pipeline operates on pages; understanding what a page is provides necessary context.

# Key Properties

1. **Step 1 - Liquid evaluation**: All Liquid template expressions in the content are evaluated first.
2. **Step 2 - Markdown conversion**: If the file has an `.md` extension, Markdown is converted to HTML using the CommonMark standard.
3. **Step 3 - Layout wrapping**: The content is wrapped in a Liquid layout template, if one is specified.
4. **Step 4 - File writing**: The final output is written to the destination directory with an `.html` extension.
5. **Ordered execution**: The steps execute in sequence; Liquid is evaluated before Markdown conversion.
6. **Customizable**: The `format` frontmatter field can override Markdown conversion, and the `layout` field controls layout wrapping.

# Construction / Recognition

## To Construct/Create:
1. This is an automatic process -- it is not manually constructed.
2. Create a page file and run `cobalt build` to trigger the pipeline.

## To Identify/Recognize:
1. Observe that content files in the source directory are transformed into HTML files in the destination directory.
2. The pipeline is the mechanism behind this transformation.

# Context & Application

- **Typical contexts**: Every `cobalt build` invocation triggers the pipeline for all pages.
- **Common applications**: Understanding the pipeline helps debug issues with template evaluation order, Markdown rendering, or layout application.

# Examples

**Example 1** (source: Pages documentation): A file `about.md` containing Liquid expressions and Markdown content will first have its Liquid expressions evaluated, then its Markdown converted to HTML, then be wrapped in the layout specified by its frontmatter `layout` field, and finally be written to `_site/about.html`.

**Example 2** (source: Pages documentation): A file `index.liquid` (not `.md`) will have Liquid expressions evaluated and be wrapped in a layout, but the Markdown conversion step is skipped because the file does not have an `.md` extension.

# Relationships

## Builds Upon
- **[Page](/concept-cards/cobalt/page.md)** -- The pipeline processes pages.

## Enables
- **[Syntax Highlighting](/concept-cards/cobalt/syntax-highlighting.md)** -- Code highlighting happens during the Liquid/Markdown processing stages.

## Related
- **[Liquid Template Language](/concept-cards/cobalt/liquid-template-language.md)** -- Step 1 of the pipeline evaluates Liquid expressions.
- **[Layout](/concept-cards/cobalt/layout.md)** -- Step 3 wraps content in a layout template.
- **[Format Field](/concept-cards/cobalt/format-field.md)** -- Controls whether Markdown conversion (step 2) occurs.
- **[Cobalt Build](/concept-cards/cobalt/cobalt-build.md)** -- The build command triggers the pipeline.

## Contrasts With
- No direct contrast; this is the only processing pipeline in Cobalt.

# Common Errors

- **Error**: Using Liquid syntax that depends on HTML structure in a Markdown file, not realizing Liquid is evaluated before Markdown conversion.
  **Correction**: Remember the order: Liquid is evaluated first (step 1), then Markdown is converted (step 2). Plan your templates accordingly.

# Common Confusions

- **Confusion**: Thinking Markdown is converted before Liquid expressions are evaluated.
  **Clarification**: Liquid template expressions are always evaluated first (step 1), then Markdown is converted to HTML (step 2). This order matters when Liquid expressions generate Markdown content.

# Source Reference

Pages, "Pages" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Pages documentation, which lists the four transformation steps explicitly.
- Confidence rationale: The four steps are enumerated clearly in the documentation.
- Uncertainties: The documentation lists the steps concisely; finer details of each step (e.g., which Liquid variables are available at each stage) are not fully detailed.
- Cross-reference status: Consistent with Frontmatter documentation (format field) and Layout references.
