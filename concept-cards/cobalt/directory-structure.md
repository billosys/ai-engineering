---
# === CORE IDENTIFICATION ===
concept: Directory Structure
slug: directory-structure

# === CLASSIFICATION ===
category: project-structure
subcategory: overview
tier: foundational

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Directory Structure"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "project layout"
  - "project structure"
  - "site structure"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cobalt
extends: []
related:
  - cobalt-init
  - source-directory
  - destination-directory
  - layouts-directory
  - includes-directory
  - defaults-directory
  - cobalt-configuration-file
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the directory structure of a Cobalt project?"
  - "What must I know before creating a Cobalt site?"
---

# Quick Definition

A Cobalt project follows a convention-based directory structure where underscore-prefixed directories (`_layouts`, `_includes`, `_data`, `_sass`, `_site`, `_defaults`, `_drafts`, `_syntaxes`) contain site generation resources, while the source hierarchy is mirrored in the output.

# Core Definition

Cobalt uses a convention-based directory layout where "cobalt mirrors your source file hierarchy in the destination, helping you get closer to a What-You-See-Is-What-You-Get experience" (source: Directory doc page). Files or folders that help generate the site but are not directly part of the output are "hidden" from cobalt by prefixing them with an underscore (`_`) (source: Directory doc page). The root of a Cobalt project contains the `_cobalt.yml` configuration file and a set of special directories, each serving a specific purpose in the site generation process.

# Prerequisites

- **Cobalt** -- understanding of what Cobalt is and how it generates sites

# Key Properties

1. **WYSIWYG hierarchy** -- "cobalt mirrors your source file hierarchy in the destination, helping you get closer to a What-You-See-Is-What-You-Get experience" (source: Directory doc page).
2. **Underscore prefix convention** -- "Files or folders that help generate the site but aren't directly part of the output are 'hidden' from cobalt by prefixing them with a `_`" (source: Directory doc page).
3. **Standard directories** -- the default layout includes `_cobalt.yml`, `_layouts`, `_includes`, `_data`, `_sass`, `_site`, `_defaults`, `posts`, `_drafts`, and `_syntaxes` (source: Directory doc page).
4. **Configurable paths** -- the source directory (`.` by default), destination directory (`_site`), posts directory (`posts`), and drafts directory (`_drafts`) can all be modified in `_cobalt.yml` (source: Directory doc page, Configuration doc page).
5. **Asset pass-through** -- "Other files" (assets) "will be copied directly over from the source directory to the output directory" (source: Directory doc page).

# Construction / Recognition

## To Construct/Create:
1. Run `cobalt init` to generate the standard directory structure.
2. Alternatively, manually create the required directories and `_cobalt.yml`.

## To Identify/Recognize:
1. The presence of `_cobalt.yml` in the root indicates a Cobalt project.
2. Underscore-prefixed directories (`_layouts`, `_includes`, `_site`, etc.) are characteristic of the Cobalt structure.

# Context & Application

- **Typical contexts**: Understanding how to organize content and resources in a Cobalt project.
- **Common applications**: Setting up a new site, migrating content, organizing templates and includes.

# Examples

**Example 1** (source: Directory doc page): The default Cobalt site structure:
```
.
|- _cobalt.yml
|- _layouts
|  |- default.liquid
|- _includes
|  |- header.liquid
|- _data
|  |- movies.json
|- _sass
|  |- base.scss
|- _site
|  |- index.html
|- _defaults
|  |- pages.md
|  |- posts.md
|- posts
|  |- cats.md
|- _drafts
|  |- dogs.md
|- _syntaxes
|  |- language.sublime-syntax
|- index.liquid
```

**Example 2** (source: Directory doc page): Directory descriptions table:

| Directory | Description |
|-----------|-------------|
| `.` | Root directory for content; configurable in `_cobalt.yml` |
| `_cobalt.yml` | Site-wide configuration file |
| `_layouts` | Templates that wrap pages |
| `_includes` | Liquid snippets for shared content |
| `_data` | Data files loaded as `site.data` variable |
| `_sass` | Sass snippets for import into `.scss` files |
| `_site` | Output directory of cobalt |
| `_defaults` | Templates for `cobalt new` based on collection name |
| `posts` | Blog post directory |
| `_drafts` | Draft blog post directory |
| `_syntaxes` | Sublime Text syntax definition files |

# Relationships

## Builds Upon
- **Cobalt** -- the directory structure is fundamental to how Cobalt operates

## Enables
- **source-directory** -- the root (`.` by default) serves as the source directory
- **destination-directory** -- `_site` is the default destination
- **layouts-directory** -- `_layouts` holds layout templates
- **includes-directory** -- `_includes` holds include snippets
- **defaults-directory** -- `_defaults` holds templates for `cobalt new`

## Related
- **cobalt-init** -- generates the standard directory structure
- **cobalt-configuration-file** -- `_cobalt.yml` configures paths within the structure
- **assets** -- non-template files are copied through as assets
- **data-files** -- `_data` directory holds data files

## Contrasts With
- No direct contrasts within scope.

# Common Errors

- **Error**: Placing content files in underscore-prefixed directories and expecting them to appear in the output.
  **Correction**: Underscore-prefixed directories are "hidden" from cobalt. Content files meant for output should be in non-prefixed directories (like `posts` or the root).

- **Error**: Creating a directory named `_posts` instead of `posts`.
  **Correction**: Unlike some other static site generators, Cobalt uses `posts` (without underscore) for the posts directory by default. The `_drafts` directory does use an underscore, but `posts` does not.

# Common Confusions

- **Confusion**: All underscore-prefixed directories serve the same purpose.
  **Clarification**: Each underscore-prefixed directory has a specific role: `_layouts` for templates, `_includes` for snippets, `_data` for data files, `_sass` for Sass imports, `_site` for output, `_defaults` for `cobalt new` templates, `_drafts` for draft posts, and `_syntaxes` for syntax definitions.

# Source Reference

Directory Structure doc page. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Directory doc page
- Confidence rationale: High -- the complete directory structure is explicitly documented with a tree diagram and description table
- Uncertainties: None significant; the documentation is comprehensive
- Cross-reference status: References to cobalt, cobalt-init, source-directory, destination-directory, layouts-directory, includes-directory, defaults-directory, cobalt-configuration-file, assets, data-files verified against planned card slugs
