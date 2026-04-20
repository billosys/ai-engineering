---
# === CORE IDENTIFICATION ===
concept: Includes Directory
slug: includes-directory

# === CLASSIFICATION ===
category: project-structure
subcategory: directories
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
  - "_includes"
  - "includes folder"
  - "snippets directory"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - directory-structure
extends: []
related:
  - layouts-directory
  - include
  - liquid-template-language
  - layout
contrasts_with:
  - layouts-directory

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the directory structure of a Cobalt project?"
  - "What must I know before creating a Cobalt site?"
---

# Quick Definition

The `_includes` directory contains reusable Liquid snippets of content (such as headers, footers, and navigation) that can be embedded in layouts or pages using the `{% include %}` Liquid tag.

# Core Definition

The `_includes` directory holds "Liquid snippets of content to be shared among layouts or pages" (source: Directory doc page). These are partial template files that can be pulled into any layout or page using the Liquid `include` tag. The Layouts doc page explains: "You can use the `include` Liquid tag to pull in shared formatting from the `_includes` directory" (source: Layouts doc page, "Reusing Formatting" section). This enables content reuse without duplication, allowing common elements like headers, footers, and navigation menus to be defined once and included everywhere.

# Prerequisites

- **Directory Structure** -- understanding the overall Cobalt project layout

# Key Properties

1. **Contains reusable Liquid snippets** -- "Liquid snippets of content to be shared among layouts or pages" (source: Directory doc page).
2. **Used via `{% include %}` tag** -- snippets are included in layouts or pages with `{% include "filename.liquid" %}` (source: Layouts doc page).
3. **Shared across layouts and pages** -- the same snippet can be included in multiple layouts and pages (source: Directory doc page).
4. **Underscore-prefixed** -- as an underscore-prefixed directory, `_includes` is hidden from the output and not copied to the destination.
5. **Supports content reuse** -- "While different pages might need different layouts, there is generally some shared formatting, like menus" (source: Layouts doc page).

# Construction / Recognition

## To Construct/Create:
1. Create an `_includes` directory in the project root.
2. Add `.liquid` snippet files (e.g., `header.liquid`, `footer.liquid`).
3. Reference them from layouts or pages using `{% include "filename.liquid" %}`.

## To Identify/Recognize:
1. The `_includes` directory at the project root.
2. Files within it are `.liquid` partial templates meant to be embedded in other files.

# Context & Application

- **Typical contexts**: Sharing common HTML fragments across multiple layouts and pages.
- **Common applications**: Defining a site header, footer, navigation menu, or metadata block once and including it in all layouts.

# Examples

**Example 1** (source: Layouts doc page): Using includes in a layout:
```html
<!DOCTYPE html>
<html>
  <head>
    {% include "head.liquid" %}
  </head>
  <body>
    <header>
      {% include "header.liquid" %}
    </header>
    <main>
      {{ page.content }}
    </main>
    <footer>
      {% include "footer.liquid" %}
    </footer>
  </body>
</html>
```

**Example 2** (source: Directory doc page): Default project structure showing `_includes`:
```
|- _includes
|  |- header.liquid
```

# Relationships

## Builds Upon
- **directory-structure** -- `_includes` is a standard directory in the Cobalt project structure

## Enables
- **include** -- the include mechanism draws its snippets from this directory
- Content reuse across layouts and pages

## Related
- **layouts-directory** -- layouts commonly include snippets from `_includes`
- **liquid-template-language** -- includes are Liquid template files, invoked via the `{% include %}` tag
- **layout** -- layouts frequently use includes for shared formatting

## Contrasts With
- **layouts-directory** -- `_includes` contains small, reusable snippet files; `_layouts` contains full-page wrapper templates that define the overall HTML structure

# Common Errors

- **Error**: Referencing an include file that does not exist in `_includes`.
  **Correction**: Ensure the filename in `{% include "filename.liquid" %}` exactly matches a file in the `_includes` directory.

# Common Confusions

- **Confusion**: Include files are complete, standalone pages.
  **Clarification**: Include files are partial snippets designed to be embedded within other templates. They are not rendered as standalone pages and typically do not have their own frontmatter.

# Source Reference

Directory Structure doc page; Layouts doc page, "Reusing Formatting" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Directory doc page and Layouts doc page
- Confidence rationale: High -- the `_includes` directory and its purpose are explicitly documented with examples
- Uncertainties: None significant
- Cross-reference status: References to directory-structure, layouts-directory, include, liquid-template-language, layout verified against planned card slugs
