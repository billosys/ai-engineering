---
# === CORE IDENTIFICATION ===
concept: Data Field
slug: data-field

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
  - "data"
  - "custom data"
  - "user-defined data"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - frontmatter
extends: []
related:
  - page-variable
  - data-files
  - site-variable
  - permalink-template-variables
contrasts_with:
  - data-files

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is frontmatter in Cobalt?"
  - "What distinguishes frontmatter data from data files?"
---

# Quick Definition

The `data` frontmatter field is a YAML object for storing arbitrary user-defined data on a page. Its values are accessible in templates via `page.data` and can also be used in permalink templates.

# Core Definition

The `data` frontmatter field is a YAML object (key-value map) that allows users to attach arbitrary custom data to a page. It defaults to `{}` (an empty object). The data is accessible in Liquid templates via the `page.data` variable, enabling template logic based on custom metadata. Additionally, the `data` field is available as a variable in permalink templates, allowing custom data to influence URL generation. This provides flexibility for site authors to extend the frontmatter schema with domain-specific metadata without modifying Cobalt's core behavior. (Source: Cobalt Frontmatter documentation, "Field Descriptions" section; Permalink Templates documentation)

# Prerequisites

- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Data is a frontmatter field.

# Key Properties

1. **Type**: Object (YAML key-value map).
2. **Default**: `{}` (empty object).
3. **Arbitrary structure**: Users can define any key-value pairs.
4. **Template access**: Available via `page.data` in Liquid templates.
5. **Permalink integration**: Available as the `{{data}}` variable in permalink templates.
6. **Per-page scope**: Data is specific to the page it is defined on.

# Construction / Recognition

## To Construct/Create:
1. In frontmatter, add a YAML object:
   ```yaml
   data:
     route: posts
     custom_key: custom_value
   ```

## To Identify/Recognize:
1. Look for `data:` in the frontmatter, followed by a YAML object/map.

# Context & Application

- **Typical contexts**: Attaching custom metadata to pages for use in templates.
- **Common applications**: Storing navigation routing data, custom template variables, page-specific configuration, or any domain-specific metadata.

# Examples

**Example 1** (source: Frontmatter documentation): The Cobalt documentation pages themselves use the data field for routing:
```yaml
---
title: "Docs::Pages"
layout: docs.liquid
data:
  route: pages
---
```
The `route` value is accessible in templates as `page.data.route`.

**Example 2** (source: Permalink Templates documentation): The `data` variable is listed as an available permalink template variable, meaning custom data can influence URL generation.

# Relationships

## Builds Upon
- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Data is a frontmatter field.

## Enables
- No concepts directly enabled.

## Related
- **[Page Variable](/concept-cards/cobalt/page-variable.md)** -- Data values are accessible via `page.data` in templates.
- **[Permalink Template Variables](/concept-cards/cobalt/permalink-template-variables.md)** -- Data is available in permalink templates.
- **[Site Variable](/concept-cards/cobalt/site-variable.md)** -- The site variable (`site.data`) provides site-wide data, complementing per-page data.

## Contrasts With
- **[Data Files](/concept-cards/cobalt/data-files.md)** -- Frontmatter data is per-page inline metadata (defined in the frontmatter of each content file). Data files are separate files that provide data accessible site-wide via `site.data`. They serve different scoping purposes.

# Common Errors

- **Error**: Putting complex data structures in frontmatter data when a data file would be more appropriate.
  **Correction**: For large or shared data, consider using data files instead of the `data` frontmatter field. Frontmatter data is best for small, page-specific values.

# Common Confusions

- **Confusion**: Confusing frontmatter `data` (per-page, inline) with data files (site-wide, separate files) or `site.data` (site-wide configuration data).
  **Clarification**: Frontmatter `data` is defined per-page in the frontmatter and accessed via `page.data`. Data files are separate files loaded site-wide. `site.data` is configured in `_cobalt.yml`. All three are different mechanisms for providing data to templates.

# Source Reference

Frontmatter, "Field Descriptions" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Frontmatter documentation
- Confidence rationale: The documentation describes the field type, default, and access pattern clearly.
- Uncertainties: The exact behavior of nested data objects in permalink templates is not fully documented.
- Cross-reference status: Verified against Permalink Templates documentation (data listed as template variable) and Configuration documentation (site.data is a separate concept).
