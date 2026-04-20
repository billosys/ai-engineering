---
# === CORE IDENTIFICATION ===
concept: Paginator Variable
slug: paginator-variable

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
section: "Paginator"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "paginator object"
  - "paginator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pagination
  - post
  - template-variables
extends:
  - pagination
related:
  - pagination-include-types
  - page-variable
  - collection-variable
  - for-block
contrasts_with:
  - collection-variable

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does pagination relate to posts?"
  - "How do I configure pagination?"
---

# Quick Definition
The `paginator` variable is a Liquid template object available on pages with pagination activated, providing access to the current page of posts and navigation metadata for moving between paginated index pages.

# Core Definition
In a page with pagination activated, the `paginator` object replaces the `collection` variable for accessing posts. It exposes properties for the current page's posts (`pages`), total counts (`total_pages`, `total_indexes`), the current index (`index`), permalink information for the current, previous, next, first, and last pages, and an `indexes` array for meta paginators (source: Cobalt docs, "Posts" page, "Paginator" section).

# Prerequisites
- Pagination must be activated on the page via frontmatter (see `pagination`)
- Understanding of Liquid template variables and iteration (see `template-variables`, `for-block`)

# Key Properties
1. **`pages`** (Array of Object): The list of page objects belonging to the current pagination index. Each element has the same properties as a page variable.
2. **`total_pages`** (Integer): Total number of posts/pages contained in this paginator.
3. **`index`** (Integer): The current pagination index number.
4. **`index_permalink`** (String): The relative URL path of the current pagination index.
5. **`total_indexes`** (Integer): Total number of pagination pages (index pages) created.
6. **`previous_index_permalink`** (String): Relative URL of the previous page. Nil if no previous page exists.
7. **`next_index_permalink`** (String): Relative URL of the next page. Nil if no next page exists.
8. **`first_index_permalink`** (String): Relative URL of the first page in the pagination.
9. **`last_index_permalink`** (String): Relative URL of the last page in the pagination.
10. **`next_index`** (Integer): Page number of the next index.
11. **`previous_index`** (Integer): Page number of the previous index.
12. **`indexes`** (Array of Paginators): Present only on meta paginators (Tags, Categories, Dates); contains the list of sub-paginators.

# Construction / Recognition
## To Use:
1. Ensure pagination is activated on the page via frontmatter.
2. Access posts using `paginator.pages` in a `for` loop.
3. Use navigation properties to build previous/next links.

## Navigation pattern:
```html
{% if paginator.previous_index %}
  <a href="/{{ paginator.previous_index_permalink }}">Previous</a>
{% endif %}
{% if paginator.next_index %}
  <a href="/{{ paginator.next_index_permalink }}">Next</a>
{% endif %}
<div>{{ paginator.index }} / {{ paginator.total_indexes }}</div>
```

# Context & Application
- **Typical contexts**: Blog index templates, archive templates, tag/category listing templates.
- **When to use**: Whenever you need to iterate over posts on a paginated page or build navigation links.
- **Scope**: Available only on pages where `pagination` is set in the frontmatter.

# Examples
**Example 1** (source: Cobalt docs, Posts page): Iterating over paginated posts

```html
<ul>
  {% for page in paginator.pages %}
    <li><a href="/{{ page.permalink }}">{{ page.title }}</a></li>
  {% endfor %}
</ul>
```

**Example 2** (source: Cobalt docs, Posts page): Full navigation with first/last links

```html
<div>
  {% if paginator.previous_index %}
    <a href="/{{ paginator.previous_index_permalink }}">Previous</a>
  {% endif %}
  {% if paginator.next_index %}
    <a href="/{{ paginator.next_index_permalink }}">Next</a>
  {% endif %}
  <div>{{ paginator.index }} / {{ paginator.total_indexes }}</div>
  {% if paginator.previous_index %}
    <a href="/{{ paginator.first_index_permalink }}">First</a>
  {% endif %}
  {% if paginator.next_index %}
    <a href="/{{ paginator.last_index_permalink }}">Last</a>
  {% endif %}
</div>
```

# Relationships
## Builds Upon
- `pagination`: The paginator is created when pagination is activated.
- `template-variables`: The paginator is a template variable available during Liquid rendering.

## Enables
- Navigation UI between paginated pages.
- Per-page post listings in blog archives.

## Related
- `page-variable`: Each element in `paginator.pages` has the same properties as a page variable.
- `for-block`: Used to iterate over `paginator.pages`.

## Contrasts With
- `collection-variable`: Without pagination, posts are accessed via `collection`; with pagination, they are accessed via `paginator.pages`.

# Common Errors
1. **Using `paginator` on a page without pagination activated**: The paginator is undefined unless pagination is configured in the frontmatter.
2. **Checking `previous_index_permalink` without first checking `previous_index`**: The permalink may be nil, so always guard with a conditional.

# Common Confusions
1. **`total_pages` vs. `total_indexes`**: `total_pages` is the total number of posts in the paginator, while `total_indexes` is the total number of pagination pages (index pages).
2. **`index` meaning**: `index` refers to the current pagination page number, not the array index of a post.

# Source Reference
- Cobalt Documentation, "Docs::Posts" page, "Paginator" section.

# Verification Notes
- All fields and their types are documented directly in the source table. Navigation example is taken verbatim from the docs.
