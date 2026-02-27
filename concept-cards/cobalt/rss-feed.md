---
# === CORE IDENTIFICATION ===
concept: RSS Feed
slug: rss-feed

# === CLASSIFICATION ===
category: feeds
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Docs::RSS"
chapter_number: null
pdf_page: null
section: "RSS"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "RSS generation"
  - "RSS 2.0 feed"
  - "syndication feed"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - post
  - cobalt-configuration-file
  - frontmatter
extends: []
related:
  - site-variable
  - posts-configuration
  - cobalt-build
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I set up RSS feeds?"
---

# Quick Definition
Cobalt generates an RSS 2.0 feed file from posts metadata when the required fields (`posts.title`, `posts.description`, `posts.rss`, and `site.base_url`) are configured in `_cobalt.yml`, and posts have `title` and `published_date` in their frontmatter.

# Core Definition
Cobalt can automatically generate an RSS 2.0 compliant feed file from the metadata of posts in the `_posts` directory. To enable RSS generation, four fields must be provided in `_cobalt.yml`: `posts.title` (the feed title), `posts.description` (the feed description), `posts.rss` (the output path for the RSS file, e.g., `rss.xml`), and `site.base_url` (the root URL for the site). None of these fields are optional, as they are required by the RSS 2.0 specification. Additionally, each post must provide `title` and `published_date` in its frontmatter (source: Cobalt docs, "RSS" page).

# Prerequisites
- Understanding of posts and their frontmatter (see `post`, `frontmatter`)
- Understanding of the Cobalt configuration file (see `cobalt-configuration-file`)
- Posts must have `title` and `published_date` set in their frontmatter

# Key Properties
1. **RSS 2.0 compliant**: The generated feed follows the RSS 2.0 specification.
2. **Four required configuration fields**: All of the following must be set in `_cobalt.yml`:
   - `posts.title`: Title for the RSS feed
   - `posts.description`: Description for the RSS feed
   - `posts.rss`: Output path for the generated RSS file (e.g., `rss.xml`)
   - `site.base_url`: The site's root URL, used to construct absolute URLs
3. **Post frontmatter requirements**: Each post must have `title` and `published_date` in its frontmatter.
4. **No optional fields**: All four configuration fields are mandatory per the RSS 2.0 spec.

# Construction / Recognition
## To Construct/Create:
1. Add the required fields to `_cobalt.yml`:
```yaml
posts:
  title: My blog!
  description: Blog description
  rss: rss.xml
site:
  base_url: http://example.com
```
2. Ensure all posts have `title` and `published_date` in their frontmatter.
3. Run `cobalt build`; the RSS file will be generated at the path specified by `posts.rss`.

# Context & Application
- **Typical contexts**: Blog syndication, allowing readers to subscribe to content updates via RSS readers.
- **When to use**: When you want readers to be able to follow your blog through RSS.
- **Scope**: Site-wide; generates a single RSS feed file for all posts.

# Examples
**Example 1** (source: Cobalt docs, RSS page): Complete RSS configuration

`_cobalt.yml`:
```yaml
posts:
  title: My blog!
  description: Blog description
  rss: rss.xml
site:
  base_url: http://example.com
```

Post frontmatter:
```yaml
---
title: "My First Post"
published_date: "2024-01-15 12:00:00 +0000"
---
```

After building, `rss.xml` will be generated in the destination directory containing an RSS 2.0 compliant feed.

# Relationships
## Builds Upon
- `post`: RSS feeds are generated from post metadata.
- `cobalt-configuration-file`: All required fields are in `_cobalt.yml`.
- `frontmatter`: Posts must provide title and published_date.

## Enables
- RSS-based subscription to the site's content.
- Integration with RSS readers and aggregators.

## Related
- `site-variable`: `site.base_url` is used to construct absolute URLs in the feed.
- `posts-configuration`: The `posts.title`, `posts.description`, and `posts.rss` fields are part of the posts configuration block.

## Contrasts With
- JSON Feed: Cobalt also supports JSON Feed output via `posts.jsonfeed`, which is a separate configuration.

# Common Errors
1. **Missing required fields**: If any of the four required fields are not set, the RSS file will not be generated correctly.
2. **Missing `published_date` in post frontmatter**: Posts without `published_date` may cause RSS generation issues.
3. **Relative base_url**: The `site.base_url` should be an absolute URL including the protocol (e.g., `http://example.com`).

# Common Confusions
1. **RSS path is relative to destination**: The `posts.rss` value (e.g., `rss.xml`) specifies the output path within the destination directory.
2. **RSS vs. JSON Feed**: Cobalt supports both RSS (`posts.rss`) and JSON Feed (`posts.jsonfeed`); they are configured independently.

# Source Reference
- Cobalt Documentation, "Docs::RSS" page.

# Verification Notes
- All required fields and their mandatory nature are explicitly documented in the source: "None of these fields are optional, as by the RSS 2.0 spec."
