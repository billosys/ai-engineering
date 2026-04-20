---
# === CORE IDENTIFICATION ===
concept: Template Variables
slug: template-variables

# === CLASSIFICATION ===
category: templating
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Variables"
chapter_number: null
pdf_page: null
section: "Variables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Liquid variables"
  - "template data"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - liquid-template-language
  - output-tags
extends: []
related:
  - site-variable
  - page-variable
  - collection-variable
  - frontmatter
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use Liquid template variables in my pages?"
  - "How does frontmatter relate to Liquid template variables?"
---

# Quick Definition

Template variables are the data objects that Cobalt makes available within Liquid templates, organized into three global categories: `site` (site-wide configuration), `page` (current page metadata and content), and `collection` (collection-level data such as posts).

# Core Definition

Cobalt exposes a variety of data as Liquid variables for use in templates. As the documentation states: "Cobalt makes a variety of data available as Liquid variables." These variables are organized into three top-level global objects: `site` (site-wide information from `_cobalt.yml` and data files), `page` (information about the current page being rendered), and `collection` (information about collections, with `posts` being the built-in collection). Variables are accessed using dot notation within output tags (`{{ site.title }}`) or logic tags (`{% if page.is_draft %}`). This system is useful for "theming" and "easier maintenance for only having one place to update things." (Source: Cobalt Variables documentation)

# Prerequisites

- **[Liquid Template Language](/concept-cards/cobalt/liquid-template-language.md)** -- Variables are accessed through Liquid syntax.
- **[Output Tags](/concept-cards/cobalt/output-tags.md)** -- Variables are most commonly rendered via output tags.

# Key Properties

1. **Three global objects**: `site`, `page`, and `collection`.
2. **Dot notation access**: Properties are accessed via dots (e.g., `site.title`, `page.tags`).
3. **Type variety**: Variables can be Strings, Objects, Lists, Booleans, or DateTimes.
4. **Context sensitivity**: Some variables (like `page.content` and `page.excerpt`) are only available in layouts, not in page content itself.
5. **User-defined data**: The `page.data` object contains user-defined frontmatter data.
6. **Data file integration**: The `site.data` object includes data from `_data` directory files.

# Construction / Recognition

## To Construct/Create:
1. Site variables are populated from `_cobalt.yml` configuration.
2. Page variables are populated from frontmatter and computed during build.
3. Collection variables are populated from collection configuration in `_cobalt.yml`.
4. Custom data is added via frontmatter `data:` field or `_data` directory files.

## To Identify/Recognize:
1. Used within `{{ }}` or `{% %}` delimiters in templates.
2. Start with one of the three global prefixes: `site.`, `page.`, or `collections.`.

# Context & Application

- **Typical contexts**: Layouts, page templates, includes -- anywhere Liquid is processed.
- **Common applications**: Rendering page titles, building navigation from site data, conditional rendering based on page metadata, iterating over collection items.

# Examples

**Example 1** (source: Cobalt Variables documentation): Using variables in a page layout:
```html
<html>
  <head>
    <title>{{ page.title }}</title>
  </head>
  <body>
    {{ page.content }}
  </body>
</html>
```

**Example 2** (source: Cobalt Variables documentation): Variables are useful for theming and maintenance -- defining a site title once in `_cobalt.yml` and referencing it everywhere as `{{ site.title }}`.

# Relationships

## Builds Upon
- **[Liquid Template Language](/concept-cards/cobalt/liquid-template-language.md)** -- Variables are accessed through Liquid syntax.
- **[Output Tags](/concept-cards/cobalt/output-tags.md)** -- The primary way to render variables.

## Enables
- **[Site Variable](/concept-cards/cobalt/site-variable.md)** -- The `site` global object.
- **[Page Variable](/concept-cards/cobalt/page-variable.md)** -- The `page` global object.
- **[Collection Variable](/concept-cards/cobalt/collection-variable.md)** -- The `collection` global object.

## Related
- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Frontmatter values populate page variables.
- **[Data Files](/concept-cards/cobalt/data-files.md)** -- Data files populate `site.data`.
- **[Cobalt Configuration File](/concept-cards/cobalt/cobalt-configuration-file.md)** -- Configuration populates site variables.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Trying to access `page.content` within a page's own content (rather than in a layout).
  **Correction**: `page.content` and `page.excerpt` are only available in the layout context, not within the page content itself.

# Common Confusions

- **Confusion**: Thinking `page.data` and `site.data` are the same thing.
  **Clarification**: `page.data` is user-defined data from the page's frontmatter. `site.data` is merged data from the `_data` directory and `_cobalt.yml`.

# Source Reference

Variables documentation, "Variables", "Global variables", "Site Variables", "Page Variables", and "Collection Variables" sections. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Variables documentation
- Confidence rationale: The documentation provides comprehensive tables of all available variables with types and descriptions.
- Uncertainties: None.
- Cross-reference status: Fully verified against the Variables documentation.
