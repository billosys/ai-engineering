---
# === CORE IDENTIFICATION ===
concept: Cobalt Configuration File
slug: cobalt-configuration-file

# === CLASSIFICATION ===
category: configuration
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Configuration"
chapter_number: null
pdf_page: null
section: "Config File"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "_cobalt.yml"
  - "config file"
  - "site configuration"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - build-options
  - site-options
  - posts-configuration
  - frontmatter
  - cobalt-build
  - directory-structure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the `_cobalt.yml` configuration file?"
  - "How does _cobalt.yml relate to frontmatter defaults?"
  - "How do I configure site-wide settings?"
---

# Quick Definition

`_cobalt.yml` is Cobalt's site-wide configuration file, written in YAML, that specifies build options, site metadata, page/post defaults, and other settings that control how the site is generated.

# Core Definition

`_cobalt.yml` is the central configuration file for a Cobalt static site, located in the project root directory. It allows specifying site-wide options and defaults for pages. The configuration is organized into several sections: build options (source directory, template extensions, drafts inclusion, ignore patterns, destination), site options (title, description, base URL, sitemap, site data), global page/post defaults (frontmatter defaults, syntax highlighting), pages-specific defaults, posts-specific options (directory, drafts directory, ordering, feed generation, filename conventions), and asset options (Sass compilation settings). All settings have sensible defaults, making the file entirely optional -- Cobalt works without it using built-in defaults. (Source: Cobalt Configuration documentation, "Config File" section)

# Prerequisites

Foundational concept with no prerequisites. The configuration file is one of the first things a user encounters when setting up a Cobalt site.

# Key Properties

1. **Filename**: `_cobalt.yml`.
2. **Format**: YAML.
3. **Location**: Project root directory (alongside the source directory).
4. **Optional**: All settings have defaults; the file is not required.
5. **Sections**: Build options, site options, global defaults, pages defaults, posts options, asset options.
6. **Frontmatter defaults**: The `default`, `pages.default`, and `posts.default` sections set site-wide frontmatter defaults.
7. **CLI override**: Some settings can be overridden via command-line flags.

# Construction / Recognition

## To Construct/Create:
1. Create a file named `_cobalt.yml` in the project root.
2. Add YAML configuration for desired sections (build, site, pages, posts, etc.).
3. Alternatively, run `cobalt init` to generate a default configuration.

## To Identify/Recognize:
1. Look for a file named `_cobalt.yml` in the project root directory.
2. The file contains YAML configuration with sections like `source:`, `site:`, `posts:`, etc.

# Context & Application

- **Typical contexts**: Every Cobalt project can have a `_cobalt.yml` for site-wide configuration.
- **Common applications**: Setting the site title and description, configuring the build destination, enabling RSS feeds, setting default frontmatter values, customizing post directories.

# Examples

**Example 1** (source: Configuration documentation): The complete default `_cobalt.yml`:
```yml
# Build options
source: "."
template_extensions:
  - md
  - liquid
include_drafts: false
ignore:
destination: _site

# Site options
site:
  title: ~
  description: ~
  base_url: ~
  sitemap: ~
  data: ~

# Page/Post options
default:
  excerpt_separator: "\n\n"
  is_draft: false
syntax_highlight:
  theme: "base16-ocean.dark"
  enabled: true
assets:
  sass:
    style: Nested
pages:
  default: {}
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

**Example 2** (source: Configuration documentation): Configuring ignore patterns to unignore the `.well-known/` folder:
```yaml
ignore:
  - "!.well-known"
  - "!.well-known/**/*"
```

# Relationships

## Builds Upon
- No prerequisites -- this is a foundational configuration concept.

## Enables
- **[Build Options](/concept-cards/cobalt/build-options.md)** -- Build-specific settings within `_cobalt.yml`.
- **[Site Options](/concept-cards/cobalt/site-options.md)** -- Site metadata settings within `_cobalt.yml`.
- **[Posts Configuration](/concept-cards/cobalt/posts-configuration.md)** -- Posts-specific settings within `_cobalt.yml`.

## Related
- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- `_cobalt.yml` can set site-wide frontmatter defaults via the `default`, `pages.default`, and `posts.default` sections.
- **[Cobalt Build](/concept-cards/cobalt/cobalt-build.md)** -- The build command reads `_cobalt.yml` to determine how to generate the site.
- **[Directory Structure](/concept-cards/cobalt/directory-structure.md)** -- `_cobalt.yml` lives in the project root and configures directory paths.

## Contrasts With
- No direct contrast.

# Common Errors

- **Error**: Placing `_cobalt.yml` inside the `source` directory instead of the project root.
  **Correction**: `_cobalt.yml` must be in the project root directory, not inside the source directory.

- **Error**: Using incorrect YAML syntax (e.g., tabs instead of spaces).
  **Correction**: YAML requires spaces for indentation. Validate your YAML if Cobalt fails to read the configuration.

# Common Confusions

- **Confusion**: Thinking `_cobalt.yml` is required for Cobalt to work.
  **Clarification**: `_cobalt.yml` is optional. Cobalt works with sensible defaults for all settings. The file is only needed to customize behavior.

- **Confusion**: Thinking frontmatter defaults in `_cobalt.yml` override explicit frontmatter in content files.
  **Clarification**: Frontmatter values set in `_cobalt.yml` (via `default`, `pages.default`, `posts.default`) provide defaults that are overridden by explicit values in individual content files' frontmatter.

# Source Reference

Configuration, "Config File" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Configuration documentation
- Confidence rationale: The documentation provides the complete default configuration file with all sections and their descriptions.
- Uncertainties: The exact precedence order among `default`, `pages.default`, and `posts.default` is not explicitly documented but implied (more specific overrides general).
- Cross-reference status: Verified against Frontmatter, Pages, and Posts documentation.
