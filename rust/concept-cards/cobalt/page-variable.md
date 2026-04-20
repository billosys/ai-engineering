---
# === CORE IDENTIFICATION ===
concept: Page Variable
slug: page-variable

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
section: "Page Variables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "page object"
  - "page data"
  - "current page variable"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - template-variables
extends: []
related:
  - frontmatter
  - layout
  - site-variable
  - collection-variable
contrasts_with:
  - site-variable

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use Liquid template variables in my pages?"
  - "How does frontmatter relate to Liquid template variables?"
  - "How does a layout relate to page content?"
---

# Quick Definition

The `page` variable is a global Liquid object providing metadata and content for the page currently being rendered, including its title, permalink, tags, categories, published date, and (within layouts) the rendered content and excerpt.

# Core Definition

The `page` variable provides access to all information about the current page being processed. Its properties are populated from the page's frontmatter and computed values. In the context of page content, available properties include: `page.permalink` (String), `page.title` (String), `page.slug` (String), `page.description` (String), `page.categories` (List of Strings), `page.tags` (List of Strings), `page.published_date` (DateTime in `YYYY-MM-DD HH:MM:SS TZ` format), `page.is_draft` (Boolean), `page.file.permalink` (String, relative path to source file), `page.collection` (String, collection slug), `page.data` (Object, user-defined frontmatter data), `page.next` (Object, next page in collection -- posts only), and `page.previous` (Object, previous page in collection -- posts only). Additionally, in the layout context, `page.content` (rendered page content) and `page.excerpt` (rendered excerpt) become available. (Source: Cobalt Variables documentation)

# Prerequisites

- **[Template Variables](/concept-cards/cobalt/template-variables.md)** -- Understanding the variable system.

# Key Properties

1. **`page.permalink`** (String): Relative path to the page.
2. **`page.title`** (String): The title from frontmatter.
3. **`page.slug`** (String): The page identifier from frontmatter.
4. **`page.description`** (String): The description from frontmatter.
5. **`page.categories`** (List of Strings): Hierarchical categories.
6. **`page.tags`** (List of Strings): Tags applied to the page.
7. **`page.published_date`** (DateTime): Initial publication date.
8. **`page.is_draft`** (Boolean): Draft status.
9. **`page.file.permalink`** (String): Relative path to the source file.
10. **`page.collection`** (String): The collection slug (e.g., `"posts"`).
11. **`page.data`** (Object): User-defined data from frontmatter.
12. **`page.next`** / **`page.previous`** (Object): Adjacent pages in collection (posts only).
13. **`page.content`** (String): Rendered page content (layout context only).
14. **`page.excerpt`** (String): Rendered excerpt (layout context only).

# Construction / Recognition

## To Construct/Create:
1. Page variables are automatically populated from frontmatter metadata.
2. Custom data is added via the `data:` field in frontmatter.
3. `page.content` and `page.excerpt` are computed during the build process.

## To Identify/Recognize:
1. Any variable reference starting with `page.` in a template.

# Context & Application

- **Typical contexts**: Layouts (where `page.content` is available), page templates, includes.
- **Common applications**: Rendering page titles in HTML `<title>` tags, inserting page content into layouts, conditional rendering based on draft status, navigation between posts.

# Examples

**Example 1** (source: Cobalt Variables documentation): Using page variables in a layout:
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

**Example 2** (source: Cobalt Variables documentation): Accessing page tags:
```html
{% for tag in page.tags %}
  <span class="tag">{{ tag }}</span>
{% endfor %}
```

# Relationships

## Builds Upon
- **[Template Variables](/concept-cards/cobalt/template-variables.md)** -- The `page` variable is one of three globals.

## Enables
- **[Layout](/concept-cards/cobalt/layout.md)** -- Layouts use `page.content` to insert rendered page content.

## Related
- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Frontmatter values populate most page variable properties.
- **[Site Variable](/concept-cards/cobalt/site-variable.md)** -- The other primary global variable object.
- **[Collection Variable](/concept-cards/cobalt/collection-variable.md)** -- Collection-level metadata.

## Contrasts With
- **[Site Variable](/concept-cards/cobalt/site-variable.md)** -- `page` contains current-page-specific data; `site` contains site-wide data.

# Common Errors

- **Error**: Trying to access `page.content` within the page's own content file.
  **Correction**: `page.content` is only available in the layout context, not within the page body itself.

- **Error**: Using `page.next` or `page.previous` on non-post pages.
  **Correction**: These properties are only available for posts (pages in a collection).

# Common Confusions

- **Confusion**: Confusing `page.data` with `page.title`, `page.description`, etc.
  **Clarification**: `page.title`, `page.description`, etc. are first-class frontmatter fields with specific meaning. `page.data` is the catch-all object for any user-defined frontmatter data beyond the standard fields.

# Source Reference

Variables documentation, "Page Variables" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Variables documentation
- Confidence rationale: All properties are explicitly documented in a table with types and descriptions.
- Uncertainties: None.
- Cross-reference status: Cross-referenced with Layouts documentation for layout-context variables.
