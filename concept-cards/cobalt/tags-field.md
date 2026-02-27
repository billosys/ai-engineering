---
# === CORE IDENTIFICATION ===
concept: Tags Field
slug: tags-field

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
  - "tags"
  - "page tags"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - frontmatter
extends: []
related:
  - categories-field
  - pagination
  - page-variable
contrasts_with:
  - categories-field

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is frontmatter in Cobalt?"
---

# Quick Definition

The `tags` frontmatter field is a list of strings that attaches flat, non-hierarchical labels to a page. Tags are used primarily with the pagination system for tag-based post indexing.

# Core Definition

The `tags` frontmatter field is a list of strings that assigns tags (flat labels) to a page. It defaults to `~` (null). Unlike categories, tags are non-hierarchical and are not used in permalink templates. Tags are primarily leveraged by the pagination system: when pagination is configured with `include: Tags`, Cobalt creates separate paginated indexes for each tag value, enabling tag-based post archives and tag clouds. Tags are accessible in templates via the `page.tags` variable. (Source: Cobalt Frontmatter documentation, "Field Descriptions" section; Posts documentation, "Pagination" section)

# Prerequisites

- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Tags is a frontmatter field.

# Key Properties

1. **Type**: List of strings.
2. **Default**: `~` (null).
3. **Non-hierarchical**: Tags are flat labels with no ordering significance.
4. **Pagination integration**: Used with `include: Tags` in pagination configuration.
5. **Template access**: Available via `page.tags` in Liquid templates.

# Construction / Recognition

## To Construct/Create:
1. In frontmatter, add a YAML list:
   ```yaml
   tags:
     - rust
     - programming
     - tutorial
   ```

## To Identify/Recognize:
1. Look for `tags:` in the frontmatter, followed by a YAML list.

# Context & Application

- **Typical contexts**: Labeling blog posts with topics, keywords, or themes.
- **Common applications**: Creating tag-based archives, building tag clouds, filtering posts by topic.

# Examples

**Example 1** (source: Posts documentation): Using tags with pagination to create tag-based indexes:
```yaml
---
pagination:
  include: Tags
  permalink_suffix: "./{{num}}/"
---
```
With a post tagged `my_tag`, this generates pages like `/tags_page/my_tag/index.html`.

**Example 2** (source: Posts documentation): Displaying a tag cloud using the meta paginator:
```html
{% if paginator.indexes %}
  <h1>Tags</h1>
  {% for ptag in paginator.indexes %}
    <a href="/{{ ptag.index_permalink }}/">
      {{ ptag.index_title }} ({{ ptag.total_pages }})
    </a>
  {% endfor %}
{% endif %}
```

# Relationships

## Builds Upon
- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Tags is a frontmatter field.

## Enables
- **[Pagination](/concept-cards/cobalt/pagination.md)** -- Tags can be used as the indexing basis for pagination.

## Related
- **[Categories Field](/concept-cards/cobalt/categories-field.md)** -- Categories are a related but distinct organizational mechanism.
- **[Page Variable](/concept-cards/cobalt/page-variable.md)** -- Tags are accessible via `page.tags` in templates.

## Contrasts With
- **[Categories Field](/concept-cards/cobalt/categories-field.md)** -- Categories are hierarchical and integrate with permalink templates. Tags are flat labels primarily used for pagination. Categories default to `[]`; tags default to `~` (null).

# Common Errors

- **Error**: Trying to use `{{tags}}` in a permalink template.
  **Correction**: Tags are not available as permalink template variables. Use `{{categories}}` for URL path construction, or use tags via the pagination system.

# Common Confusions

- **Confusion**: Thinking tags and categories serve the same purpose.
  **Clarification**: Tags are flat, non-hierarchical labels. Categories are hierarchical and can be incorporated into permalink URL structures. They serve complementary but distinct organizational purposes.

# Source Reference

Frontmatter, "Field Descriptions" section; Posts, "Pagination" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Frontmatter documentation; pagination usage from Posts documentation.
- Confidence rationale: The field description is clear, and the pagination integration is demonstrated with examples.
- Uncertainties: Whether tags affect anything beyond pagination (e.g., filtering in collection variables) is not explicitly documented.
- Cross-reference status: Verified across Frontmatter and Posts documentation.
