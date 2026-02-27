---
# === CORE IDENTIFICATION ===
concept: Pagination
slug: pagination

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
  - "post pagination"
  - "paginator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - post
  - frontmatter
  - cobalt-configuration-file
extends:
  - post
related:
  - paginator-variable
  - pagination-include-types
  - collection-variable
  - template-variables
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does pagination relate to posts?"
  - "How do I configure pagination?"
  - "What must I know before configuring pagination?"
---

# Quick Definition
Pagination is Cobalt's system for splitting posts across multiple index pages, activated through frontmatter configuration on the page that serves as the index.

# Core Definition
Pagination in Cobalt enables splitting a collection of posts into multiple pages. It is activated by adding a `pagination` block to the frontmatter of the page that will serve as the index page. When pagination is active, posts are accessed through the `paginator` object instead of the `collection` variable. The `include` field is mandatory and determines the indexing mode (All, Tags, Categories, or Dates), while other fields such as `per_page`, `permalink_suffix`, `order`, `sort_by`, and `date_index` have default values (source: Cobalt docs, "Posts" page, "Pagination" section).

# Prerequisites
- Understanding of posts and how they are organized in Cobalt (see `post`)
- Understanding of frontmatter configuration (see `frontmatter`)
- Familiarity with the Cobalt configuration file `_cobalt.yml` (see `cobalt-configuration-file`)
- Understanding of Liquid template expressions for rendering paginated content

# Key Properties
1. **Activation via frontmatter**: Pagination is turned on by adding a `pagination:` block in the page's frontmatter; there is no global pagination toggle.
2. **Mandatory `include` field**: The `include` field must be set to one of `All`, `Tags`, `Categories`, or `Dates` to define the indexing mode.
3. **Default values**: `per_page` defaults to 5, `order` defaults to `Desc`, `sort_by` defaults to `["published_date"]`, `permalink_suffix` defaults to `./{{ num }}/`.
4. **Replaces `collection` variable**: When pagination is active on a page, the `paginator` object replaces the `collection` variable for accessing posts.
5. **Permalink suffix concatenation**: The `permalink_suffix` is concatenated to the page's `permalink` after removing any file extension.
6. **Multi-criteria sorting**: Posts can be sorted by multiple criteria simultaneously via the `sort_by` array.

# Construction / Recognition
## To Construct/Create:
1. Create a page that will act as the index for your posts (e.g., `index.liquid` or `blog.liquid`).
2. Add a `pagination:` block to the page's frontmatter.
3. Set the mandatory `include` field to one of: `All`, `Tags`, `Categories`, or `Dates`.
4. Optionally configure `per_page`, `permalink_suffix`, `order`, `sort_by`, and `date_index`.
5. Use the `paginator` object in the template to access posts and navigate between pages.

## Example frontmatter:
```yaml
---
pagination:
  include: All
  per_page: 5
  permalink_suffix: "./{{ num }}/"
  order: Desc
  sort_by: ["published_date"]
---
```

# Context & Application
- **Typical contexts**: Blog index pages, archive pages, tag listing pages, category listing pages, date-based archives.
- **When to use**: When you have many posts and want to split them across multiple pages rather than listing all on one page.
- **Scope**: Pagination applies to the page where it is defined in the frontmatter; each page can have its own pagination settings.

# Examples
**Example 1** (source: Cobalt docs, Posts page): Basic "All posts" pagination

Frontmatter:
```yaml
permalink: /
pagination:
  include: All
  permalink_suffix: ./{{num}}/
```

Generated output pages:
- `/index.html` (first page)
- `/all/2/index.html` (second page, etc.)

**Example 2** (source: Cobalt docs, Posts page): Tag-based pagination

Frontmatter:
```yaml
permalink: /tags
pagination:
  include: Tags
  permalink_suffix: ./{{num}}/
```

Generated output:
- `/tags/index.html` (meta paginator listing all tags)
- `/tags/my_tag/index.html` (first page of posts tagged "my_tag")
- `/tags/my_tag/2/index.html` (second page of that tag)

# Relationships
## Builds Upon
- `post`: Pagination operates on the posts collection.
- `frontmatter`: Pagination is configured through frontmatter.
- `cobalt-configuration-file`: Posts directory and sorting defaults come from `_cobalt.yml`.

## Enables
- `paginator-variable`: The paginator object is the runtime interface for accessing paginated data.
- `pagination-include-types`: The include modes (All, Tags, Categories, Dates) define how posts are grouped.

## Related
- `collection-variable`: Without pagination, posts are accessed through the collection variable; with pagination, the paginator replaces it.
- `template-variables`: The paginator is one of several template variables available during rendering.

## Contrasts With
- `collection-variable`: The collection variable lists all posts at once, while pagination splits them across pages.

# Common Errors
1. **Forgetting the mandatory `include` field**: Pagination will not activate without the `include` field set.
2. **Using `collection` instead of `paginator`**: When pagination is active, posts must be accessed through `paginator.pages`, not `collection`.
3. **Invalid `date_index` ordering**: For `include: Dates`, the `date_index` values must be in logical order (e.g., `["Year", "Month"]` is valid; `["Month", "Year"]` triggers an error).

# Common Confusions
1. **Pagination vs. collection**: Pagination and collection access are mutually exclusive on a given page -- when pagination is active, the `paginator` object replaces `collection`.
2. **Permalink suffix behavior**: The suffix is appended to the permalink after removing the file extension, which can produce unexpected paths if not understood.

# Source Reference
- Cobalt Documentation, "Docs::Posts" page, "Pagination" section.

# Verification Notes
- Extracted from the `posts.md` source file. All configuration fields, default values, and examples are directly documented in the source.
