---
# === CORE IDENTIFICATION ===
concept: Title Field
slug: title-field

# === CLASSIFICATION ===
category: frontmatter
subcategory: null
tier: foundational

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
  - "title"
  - "page title"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - frontmatter
extends: []
related:
  - page-variable
  - slug-field
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is frontmatter in Cobalt?"
---

# Quick Definition

The `title` field is a frontmatter string that specifies the user-friendly name of a page. It defaults to `~` (null) but can be inferred from the filename's slug portion.

# Core Definition

The `title` frontmatter field is a string that provides the user-friendly name of a page. When not explicitly set in the frontmatter, it defaults to `~` (null/empty). However, Cobalt can infer a title from the filename by performing a "best-effort" transformation of the slug portion of the filename into a human-readable title. The title is accessible in templates via the `page.title` variable. (Source: Cobalt Frontmatter documentation, "Field Descriptions" section)

# Prerequisites

- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- The title is a frontmatter field; understanding frontmatter is required.

# Key Properties

1. **Type**: String.
2. **Default**: `~` (null).
3. **Filename inference**: If not set, Cobalt infers a title from the slug portion of the filename as a best-effort transformation.
4. **Template access**: Available via `page.title` in Liquid templates.
5. **Usage**: Used for display in templates, page listings, RSS feeds, and more.

# Construction / Recognition

## To Construct/Create:
1. In the frontmatter block, add `title: My Page Title`.
2. Alternatively, rely on Cobalt's automatic inference from the filename.

## To Identify/Recognize:
1. Look for the `title:` key in the frontmatter YAML block.
2. If absent, the title is inferred from the filename slug.

# Context & Application

- **Typical contexts**: Every page and post typically has a title for display purposes.
- **Common applications**: Displaying page titles in headers, navigation menus, post listings, RSS feeds, and browser title bars.

# Examples

**Example 1** (source: Frontmatter documentation):
```yaml
---
title: My first Blogpost
published_date: 2016-01-01 21:00:00 +0100
layout: posts.liquid
---
```

**Example 2** (source: Frontmatter documentation): For a file named `my-first-post.md`, if no `title` is set in frontmatter, Cobalt infers the title from the slug portion `my-first-post`, likely producing something like "My first post".

# Relationships

## Builds Upon
- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Title is one of the standard frontmatter fields.

## Enables
- **[Page Variable](/concept-cards/cobalt/page-variable.md)** -- The title is exposed as `page.title` in templates.

## Related
- **[Slug Field](/concept-cards/cobalt/slug-field.md)** -- The title can be inferred from the slug, and both derive from the filename.

## Contrasts With
- No direct contrast.

# Common Errors

- **Error**: Expecting the title to automatically generate a slug for permalinks.
  **Correction**: The `slug` and `title` are separate fields. The slug is derived from the filename, not from the title.

# Common Confusions

- **Confusion**: Thinking the title field is required.
  **Clarification**: The title is optional and defaults to null. If not set, Cobalt will attempt to infer it from the filename.

# Source Reference

Frontmatter, "Field Descriptions" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Frontmatter documentation
- Confidence rationale: Field description table explicitly defines the title field.
- Uncertainties: The exact algorithm for "best-effort" title inference from slug is not documented in detail.
- Cross-reference status: Consistent with frontmatter example and defaults.
