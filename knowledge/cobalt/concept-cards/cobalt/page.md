---
# === CORE IDENTIFICATION ===
concept: Page
slug: page

# === CLASSIFICATION ===
category: content
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Pages"
chapter_number: null
pdf_page: null
section: "Pages"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "content page"
  - "site page"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - frontmatter
  - content-processing-pipeline
  - layout
  - cobalt-configuration-file
  - permalink-templates
contrasts_with:
  - post
  - assets

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a page in Cobalt?"
  - "How do posts relate to pages in Cobalt?"
  - "What distinguishes a page from a post?"
---

# Quick Definition

A page is any file in Cobalt's source directory that has a recognized template extension, is not hidden, and is not excluded through ignore patterns. Pages are the fundamental content unit in Cobalt, processed through a transformation pipeline and written to the destination directory.

# Core Definition

In Cobalt, a page is any file found in the `source` directory that meets three criteria: (1) it has an extension listed in `template_extensions` (default: `md`, `liquid`), (2) it is not hidden (no leading `.` or `_` in the filename), and (3) it is not excluded through `ignore` patterns in the configuration. Pages go through a multi-step transformation pipeline and are output as HTML files in the `destination` directory. All content in Cobalt is fundamentally a page; posts are a specialized subset of pages. (Source: Cobalt Pages documentation)

# Prerequisites

Foundational concept with no prerequisites. Understanding pages requires only basic familiarity with static site generators.

# Key Properties

1. **File location**: Must reside within the configured `source` directory.
2. **Extension matching**: The file extension must be in the `template_extensions` list (defaults to `md` and `liquid`).
3. **Visibility**: Files with a leading `.` or `_` in the name are hidden and not treated as pages.
4. **Exclusion**: Files matching `ignore` patterns in `_cobalt.yml` are skipped.
5. **Output**: Pages are written to a parallel location in the `destination` directory with an `.html` extension.
6. **Customizable behavior**: Page processing can be customized via frontmatter metadata.

# Construction / Recognition

## To Construct/Create:
1. Place a file with a recognized template extension (e.g., `.md`, `.liquid`) in the `source` directory.
2. Ensure the filename does not begin with `.` or `_`.
3. Optionally add frontmatter metadata at the top of the file.
4. Run `cobalt build` to process the page.

## To Identify/Recognize:
1. Check that the file is in the `source` directory.
2. Verify the file extension is listed in `template_extensions`.
3. Confirm the filename does not start with `.` or `_`.
4. Confirm the file is not excluded by an `ignore` pattern.

# Context & Application

- **Typical contexts**: Building static websites with Cobalt, creating content pages like "About", "Contact", or any standalone page.
- **Common applications**: Any content that should be rendered to HTML and served as part of the site. Pages form the basis of all content in Cobalt, with posts being a specialized type of page.

# Examples

**Example 1** (source: Pages documentation): A file `about.md` placed in the source directory with frontmatter will be processed through the transformation pipeline and written to `_site/about.html` (assuming default configuration).

**Example 2** (source: Pages documentation): A file named `_hidden.md` would NOT be treated as a page because its filename begins with an underscore.

# Relationships

## Builds Upon
- No prerequisites -- pages are the foundational content type.

## Enables
- **[Post](/concept-cards/cobalt/post.md)** -- Posts are a specialized type of page that live in a specific directory.
- **[Content Processing Pipeline](/concept-cards/cobalt/content-processing-pipeline.md)** -- Pages are the input to the content processing pipeline.

## Related
- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Pages optionally support frontmatter metadata.
- **[Layout](/concept-cards/cobalt/layout.md)** -- Pages are wrapped in layout templates during processing.
- **[Cobalt Configuration File](/concept-cards/cobalt/cobalt-configuration-file.md)** -- Configuration determines which files are treated as pages.

## Contrasts With
- **[Post](/concept-cards/cobalt/post.md)** -- Posts are special pages that live in the posts directory, support drafts, and have additional features like RSS feeds and ordering.
- **[Assets](/concept-cards/cobalt/assets.md)** -- Assets are files that do not have template extensions and are copied as-is to the destination.

# Common Errors

- **Error**: Naming a file with a leading underscore (e.g., `_mypage.md`) and expecting it to be processed as a page.
  **Correction**: Remove the leading underscore. Files starting with `.` or `_` are hidden and not treated as pages.

- **Error**: Using a file extension not listed in `template_extensions` and expecting it to be processed.
  **Correction**: Either rename the file to use a recognized extension (e.g., `.md`) or add the desired extension to `template_extensions` in `_cobalt.yml`.

# Common Confusions

- **Confusion**: Thinking pages and posts are entirely separate content types.
  **Clarification**: Posts ARE pages -- they are a specialized subset of pages that live in the posts directory and have additional features. All posts are pages, but not all pages are posts.

# Source Reference

Pages, "Pages" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Pages documentation
- Confidence rationale: The documentation explicitly defines what constitutes a page with clear criteria.
- Uncertainties: None -- the definition is precise and well-documented.
- Cross-reference status: Verified against Posts documentation which describes posts as "special pages."
