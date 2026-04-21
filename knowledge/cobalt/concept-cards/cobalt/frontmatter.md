---
# === CORE IDENTIFICATION ===
concept: Frontmatter
slug: frontmatter

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
section: "Frontmatter"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "front matter"
  - "YAML frontmatter"
  - "page metadata"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - page
extends: []
related:
  - title-field
  - published-date-field
  - format-field
  - layout-field
  - is-draft-field
  - slug-field
  - excerpt
  - categories-field
  - tags-field
  - data-field
  - cobalt-configuration-file
  - page-variable
contrasts_with:
  - data-files

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is frontmatter in Cobalt?"
  - "How does _cobalt.yml relate to frontmatter defaults?"
  - "What distinguishes frontmatter data from data files?"
---

# Quick Definition

Frontmatter is optional YAML metadata placed at the top of a content file, delimited by `---` above and below, that controls how Cobalt processes and renders the page.

# Core Definition

All pages in Cobalt optionally support having metadata associated with them, called the frontmatter. The frontmatter is formatted using YAML and surrounded, above and below, with `---` delimiters. Frontmatter fields control page processing behavior such as the title, publication date, layout selection, permalink generation, draft state, content format, and more. Cobalt provides sensible defaults for all frontmatter fields, and some values (such as `slug`, `title`, `published_date`, `format`, and `is_draft`) can be inferred from the filename or file location. Site-wide frontmatter defaults can be configured in `_cobalt.yml` via the `default`, `pages.default`, and `posts.default` settings. (Source: Cobalt Frontmatter documentation)

# Prerequisites

- **[Page](/concept-cards/cobalt/page.md)** -- Frontmatter is metadata for pages; understanding pages is a prerequisite.

# Key Properties

1. **YAML format**: Frontmatter uses YAML syntax.
2. **Delimited by `---`**: The frontmatter block is surrounded above and below by triple dashes.
3. **Optional**: Pages can exist without frontmatter; defaults will be used.
4. **Default values**: All fields have defaults (e.g., `format: Raw`, `is_draft: false`, `permalink: path`).
5. **Filename inference**: Some fields can be inferred from the filename (slug, title, published_date, format, is_draft).
6. **Configurable defaults**: `_cobalt.yml` allows setting site-wide frontmatter defaults.

# Construction / Recognition

## To Construct/Create:
1. At the very top of a content file, add a line containing only `---`.
2. Write YAML key-value pairs for the desired metadata fields.
3. Close the frontmatter block with another line containing only `---`.
4. Write the page content below the closing delimiter.

## To Identify/Recognize:
1. Look for `---` as the first line of a content file.
2. The frontmatter block ends at the next `---` line.
3. Content between the delimiters is YAML metadata.

# Context & Application

- **Typical contexts**: Every content file in a Cobalt site can use frontmatter to configure its behavior.
- **Common applications**: Setting page titles, specifying layouts, configuring permalinks, marking posts as drafts, adding tags and categories.

# Examples

**Example 1** (source: Frontmatter documentation):
```
---
title:   My first Blogpost
published_date:    2016-01-01 21:00:00 +0100
layout: posts.liquid
---
Hey there this is my first blogpost and this is super awesome.

My Blog is lorem ipsum like, yes it is..
```

**Example 2** (source: Frontmatter documentation): The complete default frontmatter:
```yaml
---
title: ~
description: ~
published_date: ~
format: Raw
layout: ~
is_draft: false
permalink: path
slug: ~
excerpt_separator: "\n\n"
excerpt: ~
categories: []
tags: ~
data: {}
---
```

# Relationships

## Builds Upon
- **[Page](/concept-cards/cobalt/page.md)** -- Frontmatter is metadata that belongs to pages.

## Enables
- **[Title Field](/concept-cards/cobalt/title-field.md)** -- One of the frontmatter fields.
- **[Published Date Field](/concept-cards/cobalt/published-date-field.md)** -- One of the frontmatter fields.
- **[Layout Field](/concept-cards/cobalt/layout-field.md)** -- One of the frontmatter fields.
- **[Permalink Templates](/concept-cards/cobalt/permalink-templates.md)** -- Permalinks are configured via frontmatter.

## Related
- **[Cobalt Configuration File](/concept-cards/cobalt/cobalt-configuration-file.md)** -- Configuration file can set site-wide frontmatter defaults.
- **[Page Variable](/concept-cards/cobalt/page-variable.md)** -- Frontmatter values are accessible through the `page` variable in templates.

## Contrasts With
- **[Data Files](/concept-cards/cobalt/data-files.md)** -- Data files provide external data that is loaded separately, while frontmatter is inline metadata within a content file. Frontmatter data is per-page; data files can be shared across the site.

# Common Errors

- **Error**: Forgetting the closing `---` delimiter, causing the entire file to be interpreted as YAML.
  **Correction**: Always ensure frontmatter is enclosed between two `---` lines.

- **Error**: Using invalid YAML syntax in frontmatter (e.g., tabs instead of spaces).
  **Correction**: YAML requires spaces for indentation, not tabs. Validate YAML syntax if builds fail.

# Common Confusions

- **Confusion**: Thinking frontmatter data and data files serve the same purpose.
  **Clarification**: Frontmatter data (`data` field) is per-page metadata defined inline, accessible via `page.data`. Data files are separate files loaded site-wide via `site.data` or page-level `data` configuration. They serve different organizational purposes.

# Source Reference

Frontmatter, "Frontmatter" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Frontmatter documentation
- Confidence rationale: The documentation provides a clear definition, complete default values, and field descriptions.
- Uncertainties: None -- frontmatter is thoroughly documented.
- Cross-reference status: Verified against Pages, Posts, and Configuration documentation.
