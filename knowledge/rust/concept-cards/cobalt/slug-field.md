---
# === CORE IDENTIFICATION ===
concept: Slug Field
slug: slug-field

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
  - "slug"
  - "URL slug"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - frontmatter
extends: []
related:
  - permalink-templates
  - permalink-template-variables
  - title-field
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is frontmatter in Cobalt?"
  - "How do I set up permalink templates?"
---

# Quick Definition

The `slug` frontmatter field is a path-friendly string used in permalink templates. It defaults to null but is inferred from the filename (specifically the slug portion, excluding any date prefix and extension).

# Core Definition

The `slug` frontmatter field is a string that provides a path-friendly name for use in permalink templates. It defaults to `~` (null). When not explicitly set, Cobalt infers the slug from the filename, recognizing patterns like `slug.extension`, `YYYY-MM-DD-slug.extension`, and `YYYY-MM-DD slug.extension`. In permalink templates, the `slug` variable can be used with the `{{slug}}` placeholder to construct clean URLs. For example, in a permalink pattern like `/{{categories}}/{{slug}}`, the slug determines the final path segment. (Source: Cobalt Frontmatter documentation, "Field Descriptions" section; Permalink Templates documentation)

# Prerequisites

- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Slug is a frontmatter field.

# Key Properties

1. **Type**: String.
2. **Default**: `~` (null, inferred from filename).
3. **Filename inference**: Extracted from the filename, stripping any `YYYY-MM-DD-` prefix and the file extension.
4. **Path-friendly**: Designed to be safe for use in URLs.
5. **Permalink usage**: Used as the `{{slug}}` variable in permalink templates.
6. **Title derivation**: The `title` field can be inferred from the slug as a best-effort transformation.

# Construction / Recognition

## To Construct/Create:
1. In frontmatter, add: `slug: my-custom-slug`.
2. Or rely on filename inference from files named `my-post.md` or `2024-01-01-my-post.md`.

## To Identify/Recognize:
1. Look for `slug:` in the frontmatter.
2. If absent, derive it from the filename (the portion before the extension, after any date prefix).

# Context & Application

- **Typical contexts**: Building custom permalink URLs, providing clean URL paths.
- **Common applications**: Customizing the URL path of a page independently of its filename, using in permalink templates.

# Examples

**Example 1** (source: Frontmatter documentation): For a file named `2016-01-01-my-first-post.md`, the inferred slug is `my-first-post`.

**Example 2** (source: Permalink Templates documentation): Using slug in a permalink template:
```yaml
---
title: Corgi
categories:
  - Animals
  - Dogs
permalink: /{{categories}}/{{slug}}
---
```
If the slug is `corgi`, this results in the URL `animals/dogs/corgi/index.html`.

# Relationships

## Builds Upon
- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Slug is a frontmatter field.

## Enables
- **[Permalink Templates](/concept-cards/cobalt/permalink-templates.md)** -- The slug is a key variable in permalink template construction.
- **[Permalink Template Variables](/concept-cards/cobalt/permalink-template-variables.md)** -- Slug is one of the available template variables.

## Related
- **[Title Field](/concept-cards/cobalt/title-field.md)** -- Title can be inferred from the slug.

## Contrasts With
- No direct contrast.

# Common Errors

- **Error**: Including file extension or date prefix in the slug value.
  **Correction**: The slug should be just the path-friendly name portion (e.g., `my-post`, not `2024-01-01-my-post.md`).

# Common Confusions

- **Confusion**: Thinking slug and title are the same thing.
  **Clarification**: The slug is a path-friendly string for URLs (e.g., `my-first-post`), while the title is a human-readable name (e.g., `My First Post`). The title can be derived from the slug, but they serve different purposes.

# Source Reference

Frontmatter, "Field Descriptions" and "Overriding defaults from filename" sections. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Frontmatter and Permalink Templates documentation
- Confidence rationale: The documentation clearly defines the slug field, its inference behavior, and its use in permalink templates.
- Uncertainties: None significant.
- Cross-reference status: Verified across Frontmatter and Permalink Templates documentation.
