---
# === CORE IDENTIFICATION ===
concept: Site Variable
slug: site-variable

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
section: "Site Variables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "site object"
  - "site data"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - template-variables
extends: []
related:
  - cobalt-configuration-file
  - data-files
  - page-variable
  - collection-variable
contrasts_with:
  - page-variable

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use Liquid template variables in my pages?"
  - "How do data files relate to the site.data variable?"
---

# Quick Definition

The `site` variable is a global Liquid object providing site-wide information drawn from `_cobalt.yml` configuration and data files in the `_data` directory. It includes properties like `site.title`, `site.description`, `site.base_url`, `site.data`, and `site.time`.

# Core Definition

The `site` variable is one of three global Liquid objects in Cobalt (alongside `page` and `collection`). It provides access to site-wide information configured in `_cobalt.yml` and merged data from the `_data` directory. The `site` object has five documented properties: `site.title` (String), `site.description` (String), `site.base_url` (String), `site.data` (Object), and `site.time` (DateTime). The `site.data` property is particularly important as it is "the merged result of data files in the `_data` directory and `site: data` in `_cobalt.yml`." The `site.base_url` is described as "helpful for making absolute URLs, particularly when run within `cobalt serve`." (Source: Cobalt Variables documentation)

# Prerequisites

- **[Template Variables](/concept-cards/cobalt/template-variables.md)** -- Understanding the variable system.

# Key Properties

1. **`site.title`** (String): The title of the entire site, configured in `_cobalt.yml`.
2. **`site.description`** (String): The description of the entire site, configured in `_cobalt.yml`.
3. **`site.base_url`** (String): The URL of the site, useful for making absolute URLs.
4. **`site.data`** (Object): Merged data from `_data` directory files and `site: data` in `_cobalt.yml`.
5. **`site.time`** (DateTime): A `liquid_core::model::DateTime` representing the time of website re-generation.

# Construction / Recognition

## To Construct/Create:
1. Set `title`, `description`, and `base_url` in `_cobalt.yml`.
2. Place data files in the `_data` directory to populate `site.data`.
3. Optionally add inline data under `site: data:` in `_cobalt.yml`.

## To Identify/Recognize:
1. Any variable reference starting with `site.` in a template.

# Context & Application

- **Typical contexts**: Layouts, includes, and any template that needs site-wide information.
- **Common applications**: Setting the HTML `<title>`, generating meta tags, building absolute URLs, accessing shared data.

# Examples

**Example 1** (source: Cobalt Variables documentation): Using site variables in a layout head section:
```html
<head>
  <title>{{ site.title }} - {{ page.title }}</title>
  <meta name="description" content="{{ site.description }}">
  <link rel="canonical" href="{{ site.base_url }}{{ page.permalink }}">
</head>
```

**Example 2** (source: Cobalt Variables documentation): Accessing data files through `site.data`:
```html
{% for breed in site.data.animals.dogs %}
  <li>{{ breed.name }}</li>
{% endfor %}
```

# Relationships

## Builds Upon
- **[Template Variables](/concept-cards/cobalt/template-variables.md)** -- The `site` variable is one of three globals.

## Enables
- **[Data Files](/concept-cards/cobalt/data-files.md)** -- Data files are accessed through `site.data`.

## Related
- **[Cobalt Configuration File](/concept-cards/cobalt/cobalt-configuration-file.md)** -- Site variables are populated from configuration.
- **[Page Variable](/concept-cards/cobalt/page-variable.md)** -- The other primary global variable object.
- **[Collection Variable](/concept-cards/cobalt/collection-variable.md)** -- The third global variable object.

## Contrasts With
- **[Page Variable](/concept-cards/cobalt/page-variable.md)** -- `site` contains site-wide data; `page` contains current-page-specific data.

# Common Errors

- **Error**: Expecting `site.data` to be populated without any data files or configuration.
  **Correction**: Place YAML/JSON/TOML files in the `_data` directory, or add data under `site: data:` in `_cobalt.yml`.

# Common Confusions

- **Confusion**: Confusing `site.data` with `page.data`.
  **Clarification**: `site.data` is merged from `_data` directory files and site configuration. `page.data` is user-defined data from the page's frontmatter.

# Source Reference

Variables documentation, "Site Variables" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Variables documentation
- Confidence rationale: All five properties are explicitly documented with types and descriptions.
- Uncertainties: None.
- Cross-reference status: Verified against Data Files documentation.
