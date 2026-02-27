---
# === CORE IDENTIFICATION ===
concept: Posts Configuration
slug: posts-configuration

# === CLASSIFICATION ===
category: configuration
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Configuration"
chapter_number: null
pdf_page: null
section: "Pages and Posts"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "posts settings"
  - "posts config"
  - "posts: section"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cobalt-configuration-file
  - post
extends: []
related:
  - draft
  - frontmatter
  - rss-feed
  - cobalt-publish
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I configure site-wide settings?"
  - "How does _cobalt.yml relate to frontmatter defaults?"
---

# Quick Definition

Posts configuration is the set of options under the `posts:` key in `_cobalt.yml` that control how Cobalt handles blog posts, including their directory location, drafts directory, sort order, feed generation, filename conventions, and default frontmatter values.

# Core Definition

The posts configuration section in `_cobalt.yml` (under the `posts:` key) provides settings specific to the posts collection. Options include: `title` (collection title, falls back to `site.title`), `description` (collection description, falls back to `site.description`), `dir` (directory where posts live, relative to source, default: `"posts"`), `drafts_dir` (directory for draft posts, relative to source, default: `"_drafts"`), `order` (sort order for the posts variable, `Asc` or `Desc`, default: `Desc`), `rss` (path for RSS feed file), `jsonfeed` (path for JSON Feed file), `publish_date_in_filename` (whether `cobalt publish` prepends `YYYY-MM-DD-` to filenames, default: `true`), and `default` (default frontmatter values for posts). Additionally, there is a global `default:` section and a `pages:` section for page-specific defaults. Syntax highlighting settings (`syntax_highlight.theme` and `syntax_highlight.enabled`) and asset settings (`assets.sass.style`) are also configured at this level. (Source: Cobalt Configuration documentation, "Pages and Posts" section)

# Prerequisites

- **[Cobalt Configuration File](/concept-cards/cobalt/cobalt-configuration-file.md)** -- Posts configuration is a section within `_cobalt.yml`.
- **[Post](/concept-cards/cobalt/post.md)** -- Understanding posts is needed to configure them.

# Key Properties

1. **`posts.title`**: String, title for the posts collection (falls back to `site.title`).
2. **`posts.description`**: String, description for the posts collection (falls back to `site.description`).
3. **`posts.dir`**: String, directory for posts relative to source (default: `"posts"`).
4. **`posts.drafts_dir`**: String, directory for draft posts relative to source (default: `"_drafts"`).
5. **`posts.order`**: `Asc` or `Desc`, sort order (default: `Desc`).
6. **`posts.rss`**: String, path for RSS feed generation (default: `~`).
7. **`posts.jsonfeed`**: String, path for JSON Feed generation (default: `~`).
8. **`posts.publish_date_in_filename`**: Boolean, whether to prepend date to filename on publish (default: `true`).
9. **`posts.default`**: Frontmatter object, default frontmatter values for posts.
10. **Global `default`**: Frontmatter defaults applied to all pages and posts (e.g., `excerpt_separator`, `is_draft`).
11. **`pages.default`**: Frontmatter defaults applied to non-post pages.

# Construction / Recognition

## To Construct/Create:
1. In `_cobalt.yml`, add settings under the `posts:` key:
   ```yaml
   posts:
     dir: blog
     drafts_dir: _drafts
     order: Desc
     rss: rss.xml
     jsonfeed: feed.json
     publish_date_in_filename: true
     default:
       layout: post.liquid
   ```

## To Identify/Recognize:
1. Look for the `posts:` key in `_cobalt.yml`.
2. Also check the global `default:` and `pages:` keys for related page/post defaults.

# Context & Application

- **Typical contexts**: Configuring a blog within a Cobalt site.
- **Common applications**: Changing the posts directory, enabling RSS or JSON feed generation, setting default layouts for all posts, configuring sort order.

# Examples

**Example 1** (source: Configuration documentation): Default posts configuration:
```yaml
posts:
  title: ~
  description: ~
  dir: posts
  drafts_dir: _drafts
  order: Desc
  rss: ~
  jsonfeed: ~
  publish_date_in_filename: true
  default: {}
```

**Example 2** (source: Configuration documentation): Global defaults that apply to all pages and posts:
```yaml
default:
  excerpt_separator: "\n\n"
  is_draft: false
syntax_highlight:
  theme: "base16-ocean.dark"
  enabled: true
```

# Relationships

## Builds Upon
- **[Cobalt Configuration File](/concept-cards/cobalt/cobalt-configuration-file.md)** -- Posts configuration is a section within the config file.
- **[Post](/concept-cards/cobalt/post.md)** -- These settings control post behavior.

## Enables
- **[RSS Feed](/concept-cards/cobalt/rss-feed.md)** -- Enabled by setting `posts.rss` to a file path.
- **[Draft](/concept-cards/cobalt/draft.md)** -- The `posts.drafts_dir` setting defines where drafts live.

## Related
- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- The `default`, `pages.default`, and `posts.default` sections set frontmatter defaults.
- **[Cobalt Publish](/concept-cards/cobalt/cobalt-publish.md)** -- The `publish_date_in_filename` setting affects publish behavior.

## Contrasts With
- No direct contrast within this documentation scope.

# Common Errors

- **Error**: Setting `posts.dir` to a directory that does not exist.
  **Correction**: Ensure the posts directory exists within the source directory.

- **Error**: Setting `rss` or `jsonfeed` but not configuring `site.base_url`, resulting in relative URLs in feeds.
  **Correction**: Set `site.base_url` in the site options to ensure feeds contain absolute URLs.

# Common Confusions

- **Confusion**: Thinking `posts.default` overrides explicit frontmatter in post files.
  **Clarification**: `posts.default` provides default values that are used only when a field is not explicitly set in the post's own frontmatter. Explicit frontmatter always takes precedence.

- **Confusion**: Not understanding the precedence between `default`, `pages.default`, and `posts.default`.
  **Clarification**: The global `default` applies to all content. `pages.default` adds page-specific defaults. `posts.default` adds post-specific defaults. More specific defaults override more general ones.

# Source Reference

Configuration, "Pages and Posts" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Configuration documentation, "Pages and Posts" section
- Confidence rationale: Each setting is explicitly described in tables with type and description.
- Uncertainties: The exact precedence order among default levels (global vs. pages vs. posts) is implied but not explicitly documented.
- Cross-reference status: Verified against Posts documentation (dir, drafts_dir references).
