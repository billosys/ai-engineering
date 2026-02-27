---
# === CORE IDENTIFICATION ===
concept: Post
slug: post

# === CLASSIFICATION ===
category: content
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Posts"
chapter_number: null
pdf_page: null
section: "Posts"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "blog post"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - page
extends:
  - page
related:
  - draft
  - frontmatter
  - posts-configuration
  - pagination
  - rss-feed
  - cobalt-publish
contrasts_with:
  - page

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a post in Cobalt?"
  - "How do posts relate to pages in Cobalt?"
  - "What distinguishes a page from a post?"
---

# Quick Definition

A post is a special type of page in Cobalt that lives in the `posts` directory (configurable via `posts.dir`) and supports additional features like drafts, date-based ordering, RSS feeds, and JSON feeds.

# Core Definition

Posts are special pages that reside in a designated directory (default: `posts/`, configurable via `posts.dir` in `_cobalt.yml`). As pages, they go through the same transformation pipeline (Liquid evaluation, Markdown conversion, layout wrapping, and output writing). However, posts gain additional capabilities: they can be marked as drafts, they support chronological ordering (ascending or descending via `posts.order`), they can generate RSS and JSON feeds, and the `cobalt publish` command can manage their publication lifecycle. Posts also support the `publish_date_in_filename` convention for date inference. (Source: Cobalt Posts documentation)

# Prerequisites

- **[Page](/concept-cards/cobalt/page.md)** -- Posts extend the page concept. Understanding pages is required to understand posts.

# Key Properties

1. **Directory-based identification**: Posts are identified by living in the `posts` directory (or the directory specified by `posts.dir`).
2. **Inherits page behavior**: Posts go through the same transformation pipeline as all pages.
3. **Draft support**: Posts can be marked as drafts via frontmatter (`is_draft: true`) or by placement in the drafts directory.
4. **Ordering**: Posts can be sorted in ascending or descending order (default: `Desc`) via `posts.order`.
5. **Feed generation**: Posts support RSS (`posts.rss`) and JSON Feed (`posts.jsonfeed`) generation.
6. **Date in filename**: Posts recognize filename patterns like `YYYY-MM-DD-slug.extension` for date inference.
7. **Pagination support**: Posts support pagination through the paginator system.

# Construction / Recognition

## To Construct/Create:
1. Create a content file with a recognized template extension (e.g., `.md`).
2. Place it in the `posts` directory (or the directory configured via `posts.dir`).
3. Add frontmatter with at least a `title` and optionally a `published_date`.
4. Run `cobalt build` to process the post, or use `cobalt new` to scaffold it.

## To Identify/Recognize:
1. A post is any page that resides within the configured `posts.dir` directory (default: `posts/`).
2. Posts are referenced through the `posts` collection variable in templates.

# Context & Application

- **Typical contexts**: Blog entries, news articles, journal entries, or any chronologically ordered content.
- **Common applications**: Building a blog with Cobalt, generating RSS or JSON feeds, creating paginated post listings.

# Examples

**Example 1** (source: Posts documentation): A file `posts/2016-01-01-my-first-blogpost.md` is automatically recognized as a post. Cobalt infers the `published_date` as `2016-01-01` and the `slug` as `my-first-blogpost` from the filename.

**Example 2** (source: Posts documentation): Posts can be configured in `_cobalt.yml` with a custom directory:
```yaml
posts:
  dir: blog
  order: Desc
  rss: rss.xml
```

# Relationships

## Builds Upon
- **[Page](/concept-cards/cobalt/page.md)** -- Posts are a specialized type of page; they inherit all page behavior.

## Enables
- **[Draft](/concept-cards/cobalt/draft.md)** -- The draft concept applies specifically to posts.
- **[Pagination](/concept-cards/cobalt/pagination.md)** -- Posts can be paginated in index pages.
- **[RSS Feed](/concept-cards/cobalt/rss-feed.md)** -- Posts can generate RSS feeds.

## Related
- **[Posts Configuration](/concept-cards/cobalt/posts-configuration.md)** -- Configuration options specific to posts in `_cobalt.yml`.
- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Posts use frontmatter for metadata like title, date, and draft status.
- **[Cobalt Publish](/concept-cards/cobalt/cobalt-publish.md)** -- The `cobalt publish` command manages post publication.

## Contrasts With
- **[Page](/concept-cards/cobalt/page.md)** -- While posts are pages, standalone pages do not have draft support, chronological ordering, or feed generation. Pages live anywhere in the source directory; posts live specifically in the posts directory.

# Common Errors

- **Error**: Placing a post file outside the `posts` directory and expecting it to be treated as a post.
  **Correction**: Posts must reside in the directory specified by `posts.dir` (default: `posts/`). Files outside this directory are treated as regular pages.

- **Error**: Expecting draft posts to appear in the built site without the `--drafts` flag.
  **Correction**: Draft posts are excluded from builds by default. Use `cobalt build --drafts` or set `include_drafts: true` in `_cobalt.yml`.

# Common Confusions

- **Confusion**: Thinking posts and pages are fundamentally different types in Cobalt.
  **Clarification**: Posts ARE pages. The documentation states "Posts are special pages that live in posts." The distinction is purely based on directory location and the additional features that come with it.

# Source Reference

Posts, "Posts" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Posts documentation
- Confidence rationale: The documentation clearly states "Posts are special pages that live in posts."
- Uncertainties: None significant.
- Cross-reference status: Verified against Pages documentation for consistency.
