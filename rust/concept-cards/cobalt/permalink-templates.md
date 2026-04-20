---
# === CORE IDENTIFICATION ===
concept: Permalink Templates
slug: permalink-templates

# === CLASSIFICATION ===
category: permalink
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Permalink Templates"
chapter_number: null
pdf_page: null
section: "Permalink Templates"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "permalink"
  - "permalink configuration"
  - "URL template"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - frontmatter
extends: []
related:
  - permalink-template-variables
  - pretty-urls
  - slug-field
  - categories-field
  - page-variable
  - cobalt-configuration-file
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a permalink in Cobalt?"
  - "How do I set up permalink templates?"
  - "What distinguishes path permalink style from custom?"
---

# Quick Definition

Permalink templates define the relative URL structure for Cobalt pages. They are configured in the frontmatter `permalink` field and support Liquid template variables for dynamic URL construction. The default permalink style is `path`, which mirrors the source file's directory structure.

# Core Definition

Permalinks refer to the relative URL for pages in Cobalt. The permalink system provides a flexible way to build URLs by leveraging Liquid template variables. Permalinks are configured in the page's frontmatter via the `permalink` field and must start with a `/`. They can be set to: (1) a literal path like `/some/other/file.html`, (2) a template using variables like `/{{categories}}/{{slug}}`, or (3) a built-in style name like `path`. The default is `path`, which uses the template `/{parent}/{name}{ext}` to mirror the source file's directory structure and filename. Permalink defaults are commonly set site-wide in `_cobalt.yml` via the `default`, `pages.default`, or `posts.default` sections. When the permalink omits a file extension, Cobalt creates "pretty URLs" by generating `index.html` inside a folder. (Source: Cobalt Permalink Templates documentation)

# Prerequisites

- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Permalinks are configured via the frontmatter `permalink` field.

# Key Properties

1. **Configured in frontmatter**: Via the `permalink` field.
2. **Must start with `/`**: Permalink templates must begin with a forward slash.
3. **Template variables**: Supports Liquid-style `{{variable}}` placeholders.
4. **Built-in styles**: `path` is the only documented built-in style, mapping to `/{parent}/{name}{ext}`.
5. **Default**: `path`.
6. **Pretty URLs**: Omitting the file extension creates folder-based URLs with `index.html`.
7. **Site-wide defaults**: Can be set in `_cobalt.yml` for consistent URL patterns.

# Construction / Recognition

## To Construct/Create:
1. In frontmatter, set the `permalink` field:
   ```yaml
   permalink: /blog/{{year}}/{{month}}/{{slug}}
   ```
2. Or use the built-in style:
   ```yaml
   permalink: path
   ```
3. Or set a literal path:
   ```yaml
   permalink: /some/specific/path.html
   ```

## To Identify/Recognize:
1. Look for the `permalink:` field in the frontmatter.
2. If not set, the default `path` style is used.
3. Permalink templates contain `{{variable}}` placeholders for dynamic URL segments.

# Context & Application

- **Typical contexts**: Controlling URL structure for pages and posts.
- **Common applications**: Creating date-based blog URLs, category-based URL hierarchies, clean/pretty URLs without file extensions.

# Examples

**Example 1** (source: Permalink Templates documentation): A literal permalink:
```yaml
title: My first Blogpost
layout: posts.liquid
permalink: /some/other/file.html
```
Result: URL is `your-website.com/some/other/file.html`, and `page.permalink` is `some/other/file.html`.

**Example 2** (source: Permalink Templates documentation): A template-based permalink with categories:
```yaml
title: Corgi
layout: posts.liquid
categories:
  - Animals
  - Dogs
permalink: /{{categories}}/{{slug}}
```
Result: URL is `your-website.com/animals/dogs/corgi/index.html` (pretty URL), and `page.permalink` is `animals/dogs/corgi`.

**Example 3** (source: Permalink Templates documentation): The built-in `path` style for a file `some/other/file.md`:
```yaml
title: My first Blogpost
layout: posts.liquid
permalink: path
```
Result: URL is `your-website.com/some/other/file.html`, and `page.permalink` is `some/other/file.html`.

# Relationships

## Builds Upon
- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Permalinks are configured via frontmatter.

## Enables
- **[Pretty URLs](/concept-cards/cobalt/pretty-urls.md)** -- Omitting the file extension triggers pretty URL generation.
- **[Permalink Template Variables](/concept-cards/cobalt/permalink-template-variables.md)** -- Template variables provide the dynamic parts of permalink patterns.

## Related
- **[Slug Field](/concept-cards/cobalt/slug-field.md)** -- The `slug` is a commonly used permalink variable.
- **[Categories Field](/concept-cards/cobalt/categories-field.md)** -- Categories are used in permalink templates as `{{categories}}`.
- **[Cobalt Configuration File](/concept-cards/cobalt/cobalt-configuration-file.md)** -- Permalink defaults can be set site-wide.
- **[Page Variable](/concept-cards/cobalt/page-variable.md)** -- The resulting permalink is accessible as `page.permalink`.

## Contrasts With
- No direct contrast within the Cobalt documentation. The `path` built-in style contrasts with custom template-based permalinks (see CQ52).

# Common Errors

- **Error**: Forgetting the leading `/` in a permalink template.
  **Correction**: Permalink templates must start with `/`. The documentation states: "Permalinks templates must start with a `/`."

- **Error**: Using a variable that has no value (e.g., `{{year}}` without a `published_date`).
  **Correction**: Ensure the frontmatter fields referenced by permalink variables are populated.

# Common Confusions

- **Confusion**: Thinking `page.permalink` includes the domain name.
  **Clarification**: `page.permalink` is a relative path (e.g., `some/other/file.html`), not an absolute URL. It does not include the domain or the leading `/`.

- **Confusion**: Thinking the `path` style and a custom permalink are fundamentally different systems.
  **Clarification**: The `path` style is simply a shorthand for the template `/{parent}/{name}{ext}`. Both built-in styles and custom templates use the same underlying permalink template engine.

# Source Reference

Permalink Templates, "Permalink Templates" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Permalink Templates documentation
- Confidence rationale: The documentation provides clear examples, variable lists, and built-in style descriptions.
- Uncertainties: Only one built-in style (`path`) is documented; there may be others not listed.
- Cross-reference status: Verified against Frontmatter documentation (permalink field) and Configuration documentation (default frontmatter).
