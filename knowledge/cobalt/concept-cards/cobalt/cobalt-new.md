---
# === CORE IDENTIFICATION ===
concept: cobalt new
slug: cobalt-new

# === CLASSIFICATION ===
category: cli
subcategory: commands
tier: foundational

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Usage"
chapter_number: null
pdf_page: null
section: "new"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "new command"
  - "create page"
  - "create post"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cobalt-init
  - installation
extends: []
related:
  - cobalt-publish
  - defaults-directory
  - page
  - post
  - draft
  - frontmatter
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a new page or post?"
  - "What distinguishes cobalt new from manual file creation?"
---

# Quick Definition

`cobalt new` creates a new page or post file from a template in the `_defaults` directory, generating a slug-based filename with pre-populated frontmatter.

# Core Definition

The `cobalt new` command creates a new content file (page or post) from the templates stored in the `_defaults` directory. The command takes a title argument and generates a file with a slug-based filename. The type of file created (page or post) depends on the target directory. By default, the file is created in the current directory; the `--file` flag can specify a target directory or full file path. "You can modify the template used for `new` by editing the files in `_defaults`" (source: Usage doc page, "new" section). New posts start as drafts by default (source: Getting Started page, "Add a Page" section).

# Prerequisites

- **Installation** -- Cobalt must be installed
- **cobalt init** -- a Cobalt site must exist with the `_defaults` directory

# Key Properties

1. **Title-to-slug conversion** -- a title like "Cats Around the World" produces the filename `cats-around-the-world.md` (source: Getting Started page, Usage doc page).
2. **Directory determines type** -- "The type of file created is based on which directory you put it in" (source: Getting Started page).
3. **`--file` flag** -- controls the target directory or filename: `--file posts` creates in the posts directory; `--file posts/cats.md` specifies an exact path (source: Usage doc page, "new" section).
4. **Template-based** -- files are initialized from templates in `_defaults` based on the collection name (source: Usage doc page, "new" section).
5. **Posts start as drafts** -- "Posts start out as 'drafts'" (source: Getting Started page).

# Construction / Recognition

## To Construct/Create:
1. Run `cobalt new "Title"` to create a page in the current directory.
2. Run `cobalt new "Title" --file posts` to create a post in the `posts` directory.
3. Run `cobalt new "Title" --file posts/custom-name.md` to specify an exact filename.

## To Identify/Recognize:
1. Files created by `cobalt new` have slug-based filenames derived from the provided title.
2. The file contents are populated from the corresponding `_defaults` template.

# Context & Application

- **Typical contexts**: Adding new content to a Cobalt site, starting a new blog post or page.
- **Common applications**: Creating blog posts with proper frontmatter, generating pages with consistent structure from templates.

# Examples

**Example 1** (source: Usage doc page): Create a page in the current directory:
```console
$ # Creates page `cats-around-the-world.md` in the current directory
$ cobalt new "Cats Around the World"
```

**Example 2** (source: Usage doc page): Create a post in the `posts` directory:
```console
$ # Creates post `cats-around-the-world.md` in the `posts` directory
$ cobalt new "Cats Around the World" --file posts
```

**Example 3** (source: Usage doc page): Create a post with a custom filename:
```console
$ # Creates post `cats.md` in the `posts` directory
$ cobalt new "Cats Around the World" --file posts/cats.md
```

# Relationships

## Builds Upon
- **cobalt init** -- init creates the `_defaults` directory from which `new` draws templates
- **defaults-directory** -- `cobalt new` uses templates from `_defaults`

## Enables
- **cobalt publish** -- new posts are created as drafts and need to be published
- **cobalt build** -- new content can then be built into the site
- **cobalt serve** -- new content can be previewed (drafts with `--drafts` flag)

## Related
- **page** -- `cobalt new` can create pages
- **post** -- `cobalt new` can create posts
- **draft** -- new posts start as drafts by default
- **frontmatter** -- new files are created with pre-populated frontmatter

## Contrasts With
- **Manual file creation** -- `cobalt new` generates files from `_defaults` templates with proper slug-based naming and pre-populated frontmatter, whereas manual file creation requires the author to set up all frontmatter fields and naming conventions themselves

# Common Errors

- **Error**: Creating a post but forgetting to use `--file posts`, resulting in a page instead of a post.
  **Correction**: Use `cobalt new "Title" --file posts` to ensure the file is created in the posts directory and treated as a post.

# Common Confusions

- **Confusion**: `cobalt new` creates a published, visible post.
  **Clarification**: Posts created by `cobalt new` start as drafts. They will not appear in `cobalt serve` without the `--drafts` flag, and they must be published with `cobalt publish` before `cobalt build` will include them.

- **Confusion**: `cobalt new` is the only way to create content files.
  **Clarification**: You can also create Markdown files manually. `cobalt new` provides convenience by generating slug-based filenames and populating frontmatter from `_defaults` templates, but manual creation is equally valid.

# Source Reference

Usage doc page, "new" section; Getting Started page, "Add a Page" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Usage doc page ("new" section) and Getting Started page
- Confidence rationale: High -- the command, its flags, and behavior are clearly documented with multiple examples
- Uncertainties: The exact content of the default templates in `_defaults` is not shown in the documentation
- Cross-reference status: References to cobalt-publish, defaults-directory, page, post, draft, frontmatter verified against planned card slugs
