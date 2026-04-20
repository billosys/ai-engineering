---
# === CORE IDENTIFICATION ===
concept: Site Options
slug: site-options

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
section: "Site options"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "site configuration"
  - "site metadata"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cobalt-configuration-file
extends: []
related:
  - site-variable
  - posts-configuration
  - rss-feed
contrasts_with:
  - build-options

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I configure site-wide settings?"
---

# Quick Definition

Site options are the settings under the `site:` key in `_cobalt.yml` that define site-wide metadata including the title, description, base URL, sitemap path, and custom site data.

# Core Definition

Site options are a group of configuration settings nested under the `site:` key in `_cobalt.yml`. They define site-wide metadata: `title` (the site title), `description` (a site description), `base_url` (the root URL used for making paths absolute in RSS feeds and available as `site.base_url` in Liquid templates), `sitemap` (relative path for generating a sitemap XML file), and `data` (an arbitrary object of values accessible via the `site.data` template variable). All site option values default to `~` (null). These values are primarily consumed by templates through the `site` variable and by feed generation. (Source: Cobalt Configuration documentation, "Site options" section)

# Prerequisites

- **[Cobalt Configuration File](/concept-cards/cobalt/cobalt-configuration-file.md)** -- Site options are a section within `_cobalt.yml`.

# Key Properties

1. **`site.title`**: String, the site title (default: `~`).
2. **`site.description`**: String, a description of the site (default: `~`).
3. **`site.base_url`**: String, the root URL for the site (default: `~`); used for absolute paths in RSS and in Liquid templates.
4. **`site.sitemap`**: String, relative path for sitemap XML generation (default: `~`).
5. **`site.data`**: Object, custom values accessible via `site.data` in templates (default: `~`).
6. **Template access**: All site options are accessible via the `site` Liquid variable.

# Construction / Recognition

## To Construct/Create:
1. In `_cobalt.yml`, add settings under the `site:` key:
   ```yaml
   site:
     title: "My Blog"
     description: "A blog about things"
     base_url: "https://example.com"
     sitemap: sitemap.xml
     data:
       author: "Jane Doe"
   ```

## To Identify/Recognize:
1. Look for the `site:` key in `_cobalt.yml`.
2. Nested keys include `title`, `description`, `base_url`, `sitemap`, and `data`.

# Context & Application

- **Typical contexts**: Configuring site metadata for templates, RSS feeds, and sitemaps.
- **Common applications**: Setting the site title for use in page headers, providing a base URL for feed generation, adding custom site-wide data for templates.

# Examples

**Example 1** (source: Configuration documentation): Default site options:
```yaml
site:
  title: ~
  description: ~
  base_url: ~
  sitemap: ~
  data: ~
```

**Example 2** (source: Configuration documentation): Using `base_url` in a Liquid template:
```liquid
{{ site.base_url }}/docs
```
This constructs an absolute URL by prepending the site's base URL.

# Relationships

## Builds Upon
- **[Cobalt Configuration File](/concept-cards/cobalt/cobalt-configuration-file.md)** -- Site options are a section within the configuration file.

## Enables
- **[Site Variable](/concept-cards/cobalt/site-variable.md)** -- The `site` template variable is populated from site options.
- **[RSS Feed](/concept-cards/cobalt/rss-feed.md)** -- The `base_url` is used for absolute paths in RSS feeds.

## Related
- **[Posts Configuration](/concept-cards/cobalt/posts-configuration.md)** -- Posts-specific title and description fall back to site title and description.

## Contrasts With
- **[Build Options](/concept-cards/cobalt/build-options.md)** -- Build options control the build process; site options define site metadata.

# Common Errors

- **Error**: Omitting a trailing slash on `base_url` or including one inconsistently.
  **Correction**: Be consistent with trailing slashes on `base_url` to avoid double-slash or missing-slash issues in generated URLs.

# Common Confusions

- **Confusion**: Thinking `site.data` and the frontmatter `data` field are the same.
  **Clarification**: `site.data` is site-wide data defined in `_cobalt.yml` and accessed via `{{ site.data }}`. The frontmatter `data` field is per-page data accessed via `{{ page.data }}`. They are separate scopes.

# Source Reference

Configuration, "Site options" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Configuration documentation, "Site options" section
- Confidence rationale: Each setting is explicitly described in a table with type and description.
- Uncertainties: None -- all five site options are clearly documented.
- Cross-reference status: Verified against template variable references in the documentation.
