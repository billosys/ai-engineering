---
# === CORE IDENTIFICATION ===
concept: Format Field
slug: format-field

# === CLASSIFICATION ===
category: frontmatter
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Frontmatter"
chapter_number: null
pdf_page: null
section: "Field Descriptions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "format"
  - "content format"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - frontmatter
extends: []
related:
  - content-processing-pipeline
  - page
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is frontmatter in Cobalt?"
---

# Quick Definition

The `format` frontmatter field specifies whether a page's content should be processed as `Markdown` (converted to HTML) or left as `Raw` (no conversion). It defaults to `Raw` but is inferred as `Markdown` for files with an `.md` extension.

# Core Definition

The `format` frontmatter field controls the content format parsing applied during the content processing pipeline. It accepts two values: `Raw` and `Markdown`. When set to `Raw` (the default), the content is not converted and passes through as-is after Liquid evaluation. When set to `Markdown`, the content is converted from Markdown to HTML using the CommonMark standard. Cobalt automatically infers `format: Markdown` for files with an `.md` extension, so explicit setting is typically only needed when overriding this inference. (Source: Cobalt Frontmatter documentation, "Field Descriptions" section)

# Prerequisites

- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Format is a frontmatter field.

# Key Properties

1. **Type**: Enum string.
2. **Allowed values**: `Raw`, `Markdown`.
3. **Default**: `Raw`.
4. **Extension inference**: Automatically set to `Markdown` for `.md` files.
5. **Pipeline impact**: Controls step 2 (Markdown-to-HTML conversion) of the content processing pipeline.

# Construction / Recognition

## To Construct/Create:
1. In frontmatter, add: `format: Markdown` or `format: Raw`.
2. Alternatively, use an `.md` file extension for automatic `Markdown` inference.

## To Identify/Recognize:
1. Look for the `format:` key in the frontmatter.
2. If absent, check the file extension -- `.md` implies `Markdown`, other extensions default to `Raw`.

# Context & Application

- **Typical contexts**: Controlling content format for pages that may need explicit format specification.
- **Common applications**: Forcing a `.liquid` file to be treated as Markdown, or preventing an `.md` file from being converted to HTML.

# Examples

**Example 1** (source: Frontmatter documentation): A file named `about.md` without an explicit `format` field will have `format` inferred as `Markdown` due to the `.md` extension.

**Example 2** (source: Frontmatter documentation): A file named `index.liquid` without an explicit `format` field will default to `format: Raw`, meaning its content is not run through Markdown conversion.

# Relationships

## Builds Upon
- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Format is a frontmatter field.

## Enables
- **[Content Processing Pipeline](/concept-cards/cobalt/content-processing-pipeline.md)** -- The format field controls whether the Markdown conversion step occurs.

## Related
- **[Page](/concept-cards/cobalt/page.md)** -- Format determines how page content is processed.

## Contrasts With
- No direct contrast; `Raw` and `Markdown` are the two options within this single field.

# Common Errors

- **Error**: Setting `format: markdown` (lowercase) instead of `format: Markdown`.
  **Correction**: Use the capitalized form `Markdown` (or `Raw`) as specified in the documentation.

# Common Confusions

- **Confusion**: Thinking all pages have their content converted to Markdown.
  **Clarification**: Only files with `format: Markdown` (or inferred from `.md` extension) undergo Markdown conversion. The default is `Raw`.

# Source Reference

Frontmatter, "Field Descriptions" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Frontmatter documentation
- Confidence rationale: The documentation clearly describes the two format values and the inference behavior.
- Uncertainties: Whether the format values are case-sensitive is not explicitly stated, but the documentation consistently uses capitalized forms.
- Cross-reference status: Consistent with Pages documentation (step 2 of pipeline mentions `.md` extension check).
