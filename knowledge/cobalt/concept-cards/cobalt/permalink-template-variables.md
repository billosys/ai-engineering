---
# === CORE IDENTIFICATION ===
concept: Permalink Template Variables
slug: permalink-template-variables

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
section: "Template Variables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "permalink variables"
  - "URL template variables"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - permalink-templates
extends: []
related:
  - slug-field
  - categories-field
  - published-date-field
  - data-field
  - frontmatter
contrasts_with:
  - template-variables

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I set up permalink templates?"
  - "What is a permalink in Cobalt?"
---

# Quick Definition

Permalink template variables are Liquid-style placeholders (e.g., `{{slug}}`, `{{year}}`, `{{categories}}`) that are replaced with dynamic values derived from the file path, frontmatter, and publication date when Cobalt generates a page's URL.

# Core Definition

Cobalt permalink templates support a set of variables that are substituted with actual values when generating a page's URL. The available variables are: `parent` (directory path to the file), `name` (filename without extension), `ext` (output file extension), `slug` (the page's slug from frontmatter), `categories` (frontmatter categories joined with `/` and lowercased), `year` (published_date's year), `i_month` (month without leading zero), `month` (month with leading zero), `i_day` (day without leading zero), `day` (day with leading zero), `hour` (24-hour clock with leading zero), `minute` (with leading zero), `second` (with leading zero), and `data` (the frontmatter data object). These variables are used within `{{` and `}}` delimiters in permalink templates. (Source: Cobalt Permalink Templates documentation, "Template Variables" section)

# Prerequisites

- **[Permalink Templates](/concept-cards/cobalt/permalink-templates.md)** -- Variables are used within permalink templates.

# Key Properties

1. **File-derived variables**: `parent` (directory path), `name` (filename without extension), `ext` (output extension).
2. **Frontmatter-derived variables**: `slug`, `categories`, `data`.
3. **Date-derived variables**: `year`, `month`, `i_month`, `day`, `i_day`, `hour`, `minute`, `second` (from `published_date`).
4. **Categories formatting**: Categories list is lowercased and joined with `/` (e.g., `["Animals", "Dogs"]` becomes `animals/dogs`).
5. **Leading zeros**: `month`, `day`, `hour`, `minute`, `second` include leading zeros; `i_month` and `i_day` do not.
6. **Liquid-style syntax**: Variables use `{{variable}}` delimiters.

# Construction / Recognition

## To Construct/Create:
1. Use variables in permalink templates with `{{` and `}}` delimiters:
   ```yaml
   permalink: /{{year}}/{{month}}/{{slug}}
   ```

## To Identify/Recognize:
1. Look for `{{variable_name}}` patterns within permalink template strings.
2. The available variable names are: `parent`, `name`, `ext`, `slug`, `categories`, `year`, `i_month`, `month`, `i_day`, `day`, `hour`, `minute`, `second`, `data`.

# Context & Application

- **Typical contexts**: Customizing URL structures in Cobalt pages and posts.
- **Common applications**: Creating date-based blog URLs (`/{{year}}/{{month}}/{{slug}}`), category-based hierarchies (`/{{categories}}/{{slug}}`), mirroring file structure (`/{{parent}}/{{name}}{{ext}}`).

# Examples

**Example 1** (source: Permalink Templates documentation): Using categories and slug:
```yaml
title: Corgi
categories:
  - Animals
  - Dogs
permalink: /{{categories}}/{{slug}}
```
For a file with slug `corgi`, this produces the URL `animals/dogs/corgi/index.html`.

**Example 2** (source: Permalink Templates documentation): The built-in `path` style is equivalent to the template `/{parent}/{name}{ext}`. For a file `some/other/file.md`, `parent` is `some/other`, `name` is `file`, and `ext` is `.html`, producing the URL `some/other/file.html`.

**Example 3** (source: Permalink Templates documentation): Using file-path variables. For a file `posts/some/file.md`:
- `parent` = `posts/some`
- `name` = `file`
- `ext` = `.html` (output extension)

# Relationships

## Builds Upon
- **[Permalink Templates](/concept-cards/cobalt/permalink-templates.md)** -- Variables are the building blocks of permalink templates.

## Enables
- No concepts directly enabled.

## Related
- **[Slug Field](/concept-cards/cobalt/slug-field.md)** -- Provides the `{{slug}}` variable value.
- **[Categories Field](/concept-cards/cobalt/categories-field.md)** -- Provides the `{{categories}}` variable value.
- **[Published Date Field](/concept-cards/cobalt/published-date-field.md)** -- Provides `{{year}}`, `{{month}}`, `{{day}}`, etc. values.
- **[Data Field](/concept-cards/cobalt/data-field.md)** -- Provides the `{{data}}` variable value.
- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Most variable values originate from frontmatter fields.

## Contrasts With
- **[Template Variables](/concept-cards/cobalt/template-variables.md)** -- Permalink template variables are a distinct set from the Liquid template variables used in page content. They share some names (slug, categories) but operate in different contexts (URL generation vs. content rendering).

# Common Errors

- **Error**: Using `{{title}}` in a permalink template (title is not a permalink variable).
  **Correction**: Use `{{slug}}` instead. The title is not available as a permalink variable; the slug is the path-friendly equivalent.

- **Error**: Confusing `month` (with leading zero) and `i_month` (without leading zero).
  **Correction**: Use `month` for zero-padded months (e.g., `01`) and `i_month` for unpadded months (e.g., `1`).

# Common Confusions

- **Confusion**: Thinking `ext` refers to the source file extension.
  **Clarification**: `ext` is the OUTPUT file extension (typically `.html`), not the source extension (e.g., `.md`).

- **Confusion**: Thinking all Liquid template variables are available in permalink templates.
  **Clarification**: Permalink templates have their own specific set of variables. Not all page/site template variables are available in permalink templates.

# Source Reference

Permalink Templates, "Template Variables" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Permalink Templates documentation, "Template Variables" section
- Confidence rationale: The documentation provides a complete table of all available variables with descriptions and examples.
- Uncertainties: The behavior of `{{data}}` in permalink templates (how an object is serialized to a URL path segment) is not fully explained.
- Cross-reference status: Verified against Frontmatter documentation (slug, categories, published_date references).
