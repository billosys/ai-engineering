---
# === CORE IDENTIFICATION ===
concept: Assets
slug: assets

# === CLASSIFICATION ===
category: assets
tier: foundational

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Docs::Assets"
chapter_number: null
pdf_page: null
section: "Assets"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "static assets"
  - "non-page files"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - page
  - directory-structure
  - cobalt-configuration-file
  - sass-scss-support
  - cobalt-build
contrasts_with:
  - page

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an asset in Cobalt?"
---

# Quick Definition
Assets are any non-page files found in the source directory -- such as images, CSS, JavaScript, and other static files -- that are mirrored directly to the destination directory during the build process.

# Core Definition
In Cobalt, assets are defined as any file in the `source` directory that is not classified as a page. A file is a page if it has an extension listed in `template_extensions` (default: `.md`, `.liquid`), is not hidden (no leading `.` or `_`), and is not excluded through `ignore` patterns. Any file that does not meet the page criteria is treated as an asset and is copied (mirrored) directly to the corresponding location in the `destination` directory without any template processing or transformation (source: Cobalt docs, "Assets" page).

# Prerequisites
Foundational concept with no strict prerequisites. Understanding the following enhances comprehension:
- The distinction between source and destination directories
- What constitutes a page in Cobalt

# Key Properties
1. **Definition by exclusion**: Assets are any files that are not pages. If a file does not have a template extension and is not hidden or ignored, it is an asset.
2. **Direct mirroring**: Assets are copied as-is to the destination directory, preserving their relative path from the source.
3. **No template processing**: Unlike pages, assets are not processed through the Liquid template engine or Markdown converter.
4. **Common types**: Images (`.png`, `.jpg`, `.svg`), stylesheets (`.css`), JavaScript (`.js`), fonts, favicons, and other static resources.
5. **Sass exception**: Sass/SCSS files are a special category of asset that undergoes compilation to CSS rather than simple copying (see `sass-scss-support`).

# Construction / Recognition
## To Construct/Create:
1. Place any non-template file in the `source` directory.
2. Ensure the file does not have a `template_extensions` extension (`.md` or `.liquid` by default).
3. Run `cobalt build`; the file will appear in the same relative location in the `destination` directory.

## To Recognize:
- Any file in the source that is not a `.md` or `.liquid` file (or other configured template extensions) and is not hidden or ignored.

# Context & Application
- **Typical contexts**: Images for blog posts, CSS stylesheets, JavaScript files, fonts, favicon files, downloadable documents.
- **When to use**: For any static file that should appear in the built site without modification.
- **Scope**: All non-page, non-hidden, non-ignored files in the source directory.

# Examples
**Example 1** (source: Cobalt docs, Assets page): Image and CSS files

If the source directory contains:
```
source/
  images/
    logo.png
  css/
    style.css
  index.md
```

After `cobalt build`, the destination will contain:
```
_site/
  images/
    logo.png
  css/
    style.css
  index.html
```

The `.png` and `.css` files are assets (mirrored directly); `index.md` is a page (processed and converted to `.html`).

# Relationships
## Builds Upon
- None; this is a foundational concept.

## Enables
- Serving static resources (images, styles, scripts) alongside the generated HTML.
- `sass-scss-support`: Sass files are a special asset type that is compiled rather than copied.

## Related
- `page`: Pages are the complement of assets -- files that undergo template processing.
- `directory-structure`: Assets must be in the source directory.
- `cobalt-configuration-file`: The `template_extensions` and `ignore` settings determine which files are pages vs. assets.

## Contrasts With
- `page`: Pages have template extensions and are processed through Liquid and Markdown; assets are copied as-is.

# Common Errors
1. **Accidentally naming an asset with a template extension**: A file named `data.md` would be treated as a page, not an asset, even if it is not intended as content.
2. **Placing assets in hidden directories**: Files in directories starting with `.` or `_` are ignored by default and will not appear in the destination.

# Common Confusions
1. **Assets vs. pages**: The distinction is based solely on file extension and naming conventions, not content or intent.
2. **Sass files as assets**: While Sass files are technically assets (non-page files), they undergo compilation rather than direct copying, making them a special case.

# Source Reference
- Cobalt Documentation, "Docs::Assets" page.

# Verification Notes
- The definition is brief in the source but clear: "Assets are any non-page files found in the source, like images, css, etc. These will be mirrored directly in the destination directory."
