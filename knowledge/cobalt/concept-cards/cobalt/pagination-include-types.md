---
# === CORE IDENTIFICATION ===
concept: Pagination Include Types
slug: pagination-include-types

# === CLASSIFICATION ===
category: pagination
tier: advanced

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Docs::Posts"
chapter_number: null
pdf_page: null
section: "Pagination"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "pagination include modes"
  - "pagination indexing modes"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pagination
  - paginator-variable
  - post
extends:
  - pagination
related:
  - frontmatter
  - template-variables
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I configure pagination?"
  - "What must I know before configuring pagination?"
---

# Quick Definition
The pagination `include` field determines how posts are grouped and indexed across paginated pages, with four modes: All, Tags, Categories, and Dates, where Tags, Categories, and Dates produce "meta paginators" that contain sub-paginators.

# Core Definition
The `include` field in the pagination frontmatter is mandatory and accepts one of four values: `All`, `Tags`, `Categories`, or `Dates`. The `All` mode creates a single linear pagination through all posts. The `Tags`, `Categories`, and `Dates` modes create a "meta paginator" -- a special paginator whose `indexes` field contains an array of sub-paginators, one per tag, category, or date grouping. For the `Dates` mode, the `date_index` field defines which date granularity to use (e.g., `["Year", "Month"]`), and the values must be in logical order (source: Cobalt docs, "Posts" page, "Pagination" section).

# Prerequisites
- Understanding of pagination activation and configuration (see `pagination`)
- Understanding of the paginator variable and its fields (see `paginator-variable`)
- For Tags/Categories modes: posts must have tags or categories set in their frontmatter

# Key Properties
1. **All mode**: Creates a flat pagination of all posts, split by `per_page`. No meta paginator; `paginator.indexes` is not present.
2. **Tags mode**: Creates a meta paginator listing all tags, with each tag having its own sub-paginator of posts. The `paginator.indexes` field contains the list of tag paginators.
3. **Categories mode**: Functions identically to Tags mode but groups posts by categories instead.
4. **Dates mode**: Groups posts by date fields. Requires `date_index` to define granularity. Valid values for `date_index` elements are: `Year`, `Month`, `Day`, `Hour`, `Minute`.
5. **Meta paginator**: When using Tags, Categories, or Dates, the first paginator is a meta paginator with an `indexes` array. Each element in `indexes` is itself a paginator with `index_title`, `index_permalink`, `total_pages`, and `pages`.
6. **date_index ordering**: The `date_index` array must be in logical chronological order. `["Year", "Month"]` is valid; `["Month", "Year"]` triggers an error.

# Construction / Recognition
## To Construct/Create:
1. Set `include: All` for a simple paginated list of all posts.
2. Set `include: Tags` to group posts by their tags (each tag gets its own paginated sub-list).
3. Set `include: Categories` to group posts by categories.
4. Set `include: Dates` with `date_index: ["Year", "Month"]` (or other valid combinations) to group by date.

## Meta paginator detection pattern:
```html
{% if paginator.indexes %}
  <!-- Meta paginator: list all tags/categories/date groups -->
  {% for sub in paginator.indexes %}
    <a href="/{{ sub.index_permalink }}/">
      {{ sub.index_title }} ({{ sub.total_pages }})
    </a>
  {% endfor %}
{% else %}
  <!-- Normal paginator: list posts -->
  {% for page in paginator.pages %}
    <li><a href="/{{ page.permalink }}">{{ page.title }}</a></li>
  {% endfor %}
{% endif %}
```

# Context & Application
- **Typical contexts**: Tag cloud pages, category archives, year/month archives, blog indexes.
- **When to use All**: When you want a simple chronological blog index split across pages.
- **When to use Tags/Categories**: When you want per-tag or per-category archive pages.
- **When to use Dates**: When you want year/month or year/month/day archive pages.

# Examples
**Example 1** (source: Cobalt docs, Posts page): Tag cloud with meta paginator

```html
{% if paginator.indexes %}
  <h1>Tags</h1>
  <p>
    {% for ptag in paginator.indexes %}
      <span>
        <a href="/{{ ptag.index_permalink }}/"
           style="font-size: {{ ptag.total_pages | times: 4 | plus: 80 }}%">
          {{ ptag.index_title }} ({{ ptag.total_pages }})
        </a>
      </span>
    {% endfor %}
  </p>
{% else %}
  <h1>Tag: {{ paginator.index_title }}</h1>
  <ul>
    {% for page in paginator.pages %}
      <li><a href="/{{ page.permalink }}">{{ page.title }}</a></li>
    {% endfor %}
  </ul>
{% endif %}
```

**Example 2** (source: Cobalt docs, Posts page): Tags permalink structure

```yaml
permalink: /tags
pagination:
  include: Tags
  permalink_suffix: ./{{num}}/
```

Generates:
- `/tags/index.html` (meta paginator)
- `/tags/my_tag/index.html` (tag paginator page 1)
- `/tags/my_tag/2/index.html` (tag paginator page 2)

# Relationships
## Builds Upon
- `pagination`: The include types are a required setting within pagination configuration.
- `paginator-variable`: Each include type produces paginator objects with specific fields.

## Enables
- Tag cloud pages and per-tag archives.
- Category-based navigation.
- Date-based archives (year/month).

## Related
- `frontmatter`: Posts must have tags, categories, or published_date set for the respective modes to work.

## Contrasts With
- Different include types are mutually exclusive on a single page; each page can only have one `include` mode.

# Common Errors
1. **Using Dates without `date_index`**: The Dates mode requires `date_index` to be specified.
2. **Invalid `date_index` order**: Values must be in logical order (Year before Month before Day, etc.).
3. **Expecting `paginator.indexes` on All mode**: The `indexes` field is only present on meta paginators (Tags, Categories, Dates).

# Common Confusions
1. **Meta paginator vs. normal paginator**: The same template page renders both; you must check `paginator.indexes` to distinguish between them.
2. **Each tag/category/date group can itself be paginated**: Each sub-paginator has its own `per_page` pagination, so tags with many posts will have multiple pages.

# Source Reference
- Cobalt Documentation, "Docs::Posts" page, "Pagination" section (fields: include, date_index, indexes).

# Verification Notes
- All four include types and the meta paginator concept are documented directly in the source. The tag cloud example is taken from the docs.
