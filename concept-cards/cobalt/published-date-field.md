---
# === CORE IDENTIFICATION ===
concept: Published Date Field
slug: published-date-field

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
  - "published_date"
  - "publication date"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - frontmatter
extends: []
related:
  - permalink-template-variables
  - posts-configuration
  - cobalt-publish
  - page-variable
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is frontmatter in Cobalt?"
---

# Quick Definition

The `published_date` field is a frontmatter field that records when a page was initially published, using the format `YYYY-MM-DD HH:MM:SS TZ`. It can be inferred from filenames that follow date-prefixed naming conventions.

# Core Definition

The `published_date` frontmatter field is a datetime value that records the date a page was initially published. It uses the format `YYYY-MM-DD HH:MM:SS TZ` (e.g., `2016-01-01 21:00:00 +0100`). The field defaults to `~` (null). Cobalt can infer the published date from filenames that follow the pattern `YYYY-MM-DD-slug.extension` or `YYYY-MM-DD slug.extension`; this inference occurs during `build` but not during `publish` (which manages its own date handling). The published date is used for post ordering and is available as template variables (`year`, `month`, `day`, etc.) in permalink templates. (Source: Cobalt Frontmatter documentation, "Field Descriptions" section)

# Prerequisites

- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- The published date is a frontmatter field.

# Key Properties

1. **Type**: Datetime string.
2. **Format**: `YYYY-MM-DD HH:MM:SS TZ`.
3. **Default**: `~` (null).
4. **Filename inference**: Inferred from `YYYY-MM-DD` prefix in filenames during `build`.
5. **Permalink integration**: Decomposed into `year`, `month`, `i_month`, `day`, `i_day`, `hour`, `minute`, `second` for permalink templates.
6. **Post ordering**: Used as a criterion for sorting posts (along with `weight`).

# Construction / Recognition

## To Construct/Create:
1. In frontmatter, add: `published_date: 2016-01-01 21:00:00 +0100`.
2. Alternatively, name the file with a date prefix: `2016-01-01-my-post.md`.
3. Use `cobalt publish` to have the date set automatically.

## To Identify/Recognize:
1. Look for the `published_date:` key in the frontmatter YAML block.
2. Check the filename for a `YYYY-MM-DD` prefix.

# Context & Application

- **Typical contexts**: Blog posts and any content where publication date matters.
- **Common applications**: Sorting posts chronologically, generating date-based permalink URLs, displaying dates in templates.

# Examples

**Example 1** (source: Frontmatter documentation):
```yaml
---
title: My first Blogpost
published_date: 2016-01-01 21:00:00 +0100
layout: posts.liquid
---
```

**Example 2** (source: Frontmatter documentation): A file named `2016-01-01-my-post.md` will have its `published_date` inferred as `2016-01-01` during build.

# Relationships

## Builds Upon
- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Published date is a frontmatter field.

## Enables
- **[Permalink Template Variables](/concept-cards/cobalt/permalink-template-variables.md)** -- The published date is decomposed into year, month, day, etc. for use in permalink templates.

## Related
- **[Posts Configuration](/concept-cards/cobalt/posts-configuration.md)** -- The `posts.order` setting uses published_date for sorting.
- **[Cobalt Publish](/concept-cards/cobalt/cobalt-publish.md)** -- The publish command manages the published_date and can prepend it to the filename.
- **[Page Variable](/concept-cards/cobalt/page-variable.md)** -- Available as `page.published_date` in templates.

## Contrasts With
- No direct contrast.

# Common Errors

- **Error**: Using an incorrect date format (e.g., `MM/DD/YYYY` instead of `YYYY-MM-DD HH:MM:SS TZ`).
  **Correction**: Always use the `YYYY-MM-DD HH:MM:SS TZ` format for published_date values.

# Common Confusions

- **Confusion**: Expecting the filename date inference to work during `cobalt publish`.
  **Clarification**: Filename date inference (from `YYYY-MM-DD-slug.extension`) is only recognized during `build`. The `publish` command manages the `published_date` independently and prepends the date to the filename by default.

# Source Reference

Frontmatter, "Field Descriptions" and "Overriding defaults from filename" sections. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Frontmatter documentation
- Confidence rationale: The documentation explicitly describes the format, inference behavior, and default value.
- Uncertainties: The exact behavior when time zone is omitted is not documented.
- Cross-reference status: Verified against Permalink Templates documentation (template variables use published_date components).
