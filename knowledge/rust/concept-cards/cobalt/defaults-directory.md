---
# === CORE IDENTIFICATION ===
concept: Defaults Directory
slug: defaults-directory

# === CLASSIFICATION ===
category: project-structure
subcategory: directories
tier: intermediate

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
  - "_defaults"
  - "defaults folder"
  - "new templates"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - directory-structure
  - cobalt-new
extends: []
related:
  - cobalt-init
  - page
  - post
  - frontmatter
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes cobalt new from manual file creation?"
  - "What is the directory structure of a Cobalt project?"
---

# Quick Definition

The `_defaults` directory contains template files (e.g., `pages.md`, `posts.md`) that `cobalt new` uses to initialize new content files, with each template corresponding to a collection name.

# Core Definition

The `_defaults` directory holds the templates that the `cobalt new` command uses when creating new content files. As documented: "`_defaults` -- `cobalt new` initializes files from here based on the collection name" (source: Directory doc page). The Usage doc page confirms: "You can modify the template used for `new` by editing the files in `_defaults`" (source: Usage doc page, "new" section). By default, the directory contains `pages.md` and `posts.md`, which serve as templates for creating new pages and posts respectively. Customizing these templates allows teams to enforce consistent frontmatter structure and default values across all new content.

# Prerequisites

- **Directory Structure** -- understanding the overall Cobalt project layout
- **cobalt new** -- understanding the command that uses these templates

# Key Properties

1. **Templates for `cobalt new`** -- "`cobalt new` initializes files from here based on the collection name" (source: Directory doc page).
2. **Collection-name-based** -- template files are matched to collections by filename (e.g., `pages.md` for pages, `posts.md` for posts).
3. **Customizable** -- "You can modify the template used for `new` by editing the files in `_defaults`" (source: Usage doc page).
4. **Default contents** -- contains `pages.md` and `posts.md` by default (source: Directory doc page tree diagram).
5. **Underscore-prefixed** -- as an underscore-prefixed directory, `_defaults` is hidden from the output and not copied to the destination.

# Construction / Recognition

## To Construct/Create:
1. The `_defaults` directory is created by `cobalt init`.
2. Edit `_defaults/pages.md` to customize the template for new pages.
3. Edit `_defaults/posts.md` to customize the template for new posts.

## To Identify/Recognize:
1. The `_defaults` directory at the project root.
2. Contains `.md` files named after collections (e.g., `pages.md`, `posts.md`).
3. These files contain the frontmatter and content that will be used as starting templates by `cobalt new`.

# Context & Application

- **Typical contexts**: Enforcing consistent content structure across a site, customizing the starting frontmatter for new content.
- **Common applications**: Adding custom frontmatter fields to the default template, including boilerplate content in new posts, standardizing metadata across a team.

# Examples

**Example 1** (source: Directory doc page): Default project structure showing `_defaults`:
```
|- _defaults
|  |- pages.md
|  |- posts.md
```

**Example 2** (source: Usage doc page): The `_defaults` directory is referenced in the context of `cobalt new`:
```console
$ cobalt new "Cats Around the World"
```
This creates a new file initialized from the appropriate template in `_defaults` based on the target collection.

# Relationships

## Builds Upon
- **directory-structure** -- `_defaults` is a standard directory in the Cobalt project structure
- **cobalt-new** -- the templates in `_defaults` are consumed by the `cobalt new` command

## Enables
- Consistent content creation through standardized templates
- Custom frontmatter defaults for new pages and posts

## Related
- **cobalt-init** -- init creates the `_defaults` directory with default templates
- **page** -- `_defaults/pages.md` serves as the template for new pages
- **post** -- `_defaults/posts.md` serves as the template for new posts
- **frontmatter** -- the templates in `_defaults` define the default frontmatter for new content

## Contrasts With
- No direct contrasts within scope.

# Common Errors

- **Error**: Deleting the `_defaults` directory and then running `cobalt new`, which may fail or produce files without expected frontmatter.
  **Correction**: Keep the `_defaults` directory with at least the standard template files for the collections you use.

# Common Confusions

- **Confusion**: The `_defaults` directory affects existing content files.
  **Clarification**: Templates in `_defaults` are only used when creating new files with `cobalt new`. They have no effect on existing pages or posts.

- **Confusion**: The `_defaults` directory is the same as the `default` frontmatter setting in `_cobalt.yml`.
  **Clarification**: `_defaults` contains file templates for `cobalt new`. The `default` setting in `_cobalt.yml` specifies site-wide default frontmatter values that are applied to all pages/posts during build, regardless of how they were created.

# Source Reference

Directory Structure doc page; Usage doc page, "new" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Directory doc page and Usage doc page
- Confidence rationale: High -- the `_defaults` directory and its purpose are explicitly documented, though the actual contents of the default templates are not shown
- Uncertainties: The exact contents of the default `pages.md` and `posts.md` templates are not shown in the documentation
- Cross-reference status: References to directory-structure, cobalt-new, cobalt-init, page, post, frontmatter verified against planned card slugs
