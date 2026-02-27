---
# === CORE IDENTIFICATION ===
concept: Layout Field
slug: layout-field

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
  - "layout"
  - "layout template"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - frontmatter
extends: []
related:
  - layout
  - content-processing-pipeline
  - page
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is frontmatter in Cobalt?"
---

# Quick Definition

The `layout` frontmatter field specifies which layout template file wraps the page content during rendering. It accepts a string (the layout filename) or `null` for no layout.

# Core Definition

The `layout` frontmatter field is a string (or null) that identifies which Liquid layout template should wrap the page's content during step 3 of the content processing pipeline. Layout templates reside in the `_layouts/` directory and provide a common structure (e.g., HTML skeleton, navigation, footer) around page content. When set to `~` (null, the default), no layout wrapping occurs. When set to a string value such as `posts.liquid`, the corresponding layout file is used to wrap the rendered content. (Source: Cobalt Frontmatter documentation, "Field Descriptions" section)

# Prerequisites

- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Layout is a frontmatter field.

# Key Properties

1. **Type**: String or null.
2. **Default**: `~` (null -- no layout).
3. **Layout directory**: Layout files reside in the `_layouts/` directory.
4. **Pipeline stage**: Applied in step 3 of the content processing pipeline (after Liquid evaluation and Markdown conversion).
5. **Liquid template**: Layouts are Liquid templates that receive the page content.

# Construction / Recognition

## To Construct/Create:
1. In frontmatter, add: `layout: posts.liquid` (or any layout filename from `_layouts/`).
2. Set to `~` or omit to disable layout wrapping.

## To Identify/Recognize:
1. Look for the `layout:` key in the frontmatter YAML block.
2. The value references a file in the `_layouts/` directory.

# Context & Application

- **Typical contexts**: Wrapping page content in a consistent site-wide HTML structure.
- **Common applications**: Applying different layouts to different types of pages (e.g., `posts.liquid` for blog posts, `default.liquid` for regular pages).

# Examples

**Example 1** (source: Frontmatter documentation):
```yaml
---
title: My first Blogpost
published_date: 2016-01-01 21:00:00 +0100
layout: posts.liquid
---
```
This page will be wrapped in the `_layouts/posts.liquid` layout template.

**Example 2** (source: Frontmatter documentation): A page with `layout: ~` (or no layout field) will have its content rendered without any layout wrapper.

# Relationships

## Builds Upon
- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Layout is a frontmatter field.

## Enables
- No concepts directly enabled.

## Related
- **[Layout](/concept-cards/cobalt/layout.md)** -- The layout concept (template files in `_layouts/`) is what this field references.
- **[Content Processing Pipeline](/concept-cards/cobalt/content-processing-pipeline.md)** -- Layout wrapping is step 3 of the pipeline.

## Contrasts With
- No direct contrast.

# Common Errors

- **Error**: Specifying a layout filename that does not exist in the `_layouts/` directory.
  **Correction**: Ensure the layout file exists in `_layouts/` and the name matches exactly.

# Common Confusions

- **Confusion**: Thinking layout wrapping happens before Liquid evaluation.
  **Clarification**: The content processing pipeline runs Liquid evaluation first (step 1), then Markdown conversion (step 2), then layout wrapping (step 3). The layout template receives already-processed content.

# Source Reference

Frontmatter, "Field Descriptions" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Frontmatter documentation
- Confidence rationale: The field is clearly described in the field descriptions table and demonstrated in examples.
- Uncertainties: The exact mechanism by which content is injected into the layout (e.g., `{{ content }}` variable) is not detailed in the Frontmatter page itself but is covered in the Layouts documentation.
- Cross-reference status: Consistent with Pages documentation (step 3 references layouts).
