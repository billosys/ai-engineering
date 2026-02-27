---
# === CORE IDENTIFICATION ===
concept: Categories Field
slug: categories-field

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
  - "categories"
  - "page categories"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - frontmatter
extends: []
related:
  - tags-field
  - permalink-template-variables
  - permalink-templates
  - pagination
contrasts_with:
  - tags-field

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is frontmatter in Cobalt?"
---

# Quick Definition

The `categories` frontmatter field is a list of strings that defines the hierarchical categorization of a page. Categories are used in permalink templates (joined with `/`) and in pagination for category-based indexing.

# Core Definition

The `categories` frontmatter field is a list of strings that assigns hierarchical categories to a page. It defaults to an empty list (`[]`). Categories serve two primary purposes: (1) they can be used in permalink templates via the `{{categories}}` variable, where the list values are lowercased and joined with `/` (e.g., categories `["Animals", "Dogs"]` become `animals/dogs` in the permalink), and (2) they can be used with the pagination system's `include: Categories` mode to create category-based post indexes. (Source: Cobalt Frontmatter documentation, "Field Descriptions" section; Permalink Templates documentation)

# Prerequisites

- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Categories is a frontmatter field.

# Key Properties

1. **Type**: List of strings.
2. **Default**: `[]` (empty list).
3. **Hierarchical**: The list order implies hierarchy (e.g., `["Animals", "Dogs"]` means Animals > Dogs).
4. **Permalink integration**: Joined with `/` and lowercased for use in permalink templates as `{{categories}}`.
5. **Pagination integration**: Used with `include: Categories` in pagination configuration.

# Construction / Recognition

## To Construct/Create:
1. In frontmatter, add a YAML list:
   ```yaml
   categories:
     - Animals
     - Dogs
   ```

## To Identify/Recognize:
1. Look for `categories:` in the frontmatter, followed by a YAML list.

# Context & Application

- **Typical contexts**: Organizing blog posts or pages into hierarchical groupings.
- **Common applications**: Generating category-based URL paths via permalink templates, creating category archives via pagination.

# Examples

**Example 1** (source: Permalink Templates documentation):
```yaml
---
title: Corgi
layout: posts.liquid
categories:
  - Animals
  - Dogs
permalink: /{{categories}}/{{slug}}
---
```
This produces the URL: `animals/dogs/corgi/index.html`. The categories `["Animals", "Dogs"]` are lowercased and joined with `/` to form `animals/dogs`.

**Example 2** (source: Posts documentation): Using categories with pagination:
```yaml
---
pagination:
  include: Categories
---
```
This creates separate paginated indexes for each category.

# Relationships

## Builds Upon
- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Categories is a frontmatter field.

## Enables
- **[Permalink Template Variables](/concept-cards/cobalt/permalink-template-variables.md)** -- Categories provides the `{{categories}}` variable for permalink templates.
- **[Pagination](/concept-cards/cobalt/pagination.md)** -- Categories can be used as the indexing basis for pagination.

## Related
- **[Tags Field](/concept-cards/cobalt/tags-field.md)** -- Tags are a related but distinct organizational mechanism.
- **[Permalink Templates](/concept-cards/cobalt/permalink-templates.md)** -- Categories are commonly used in permalink patterns.

## Contrasts With
- **[Tags Field](/concept-cards/cobalt/tags-field.md)** -- Categories are hierarchical (ordered list implying parent-child relationships) while tags are flat labels. Categories are integrated into permalink templates; tags are primarily used for pagination-based indexing.

# Common Errors

- **Error**: Using categories in a permalink template but having an empty categories list.
  **Correction**: Ensure categories are populated in frontmatter when using `{{categories}}` in permalink templates, or the category path segment will be empty.

# Common Confusions

- **Confusion**: Thinking categories and tags are interchangeable.
  **Clarification**: Categories are hierarchical (the list order matters) and integrate with permalink templates. Tags are flat labels primarily used for pagination indexing. They serve different organizational purposes.

# Source Reference

Frontmatter, "Field Descriptions" section; Permalink Templates, "Template Variables" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Frontmatter and Permalink Templates documentation
- Confidence rationale: The documentation clearly describes the field type, default, and behavior in permalink templates with examples.
- Uncertainties: The precise behavior when categories contain special characters is not documented.
- Cross-reference status: Verified across Frontmatter, Permalink Templates, and Posts (pagination) documentation.
