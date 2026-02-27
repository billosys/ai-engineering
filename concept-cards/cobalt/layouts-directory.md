---
# === CORE IDENTIFICATION ===
concept: Layouts Directory
slug: layouts-directory

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
  - "_layouts"
  - "layouts folder"
  - "template directory"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - directory-structure
extends: []
related:
  - includes-directory
  - layout
  - liquid-template-language
  - template-variables
contrasts_with:
  - includes-directory

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the directory structure of a Cobalt project?"
  - "What must I know before creating a Cobalt site?"
---

# Quick Definition

The `_layouts` directory contains Liquid template files that define the common HTML structure wrapping page content, selected via the `layout` field in each page's frontmatter.

# Core Definition

The `_layouts` directory holds layout templates that provide the common formatting for pages in a Cobalt site. As described in the Directory doc page: "`_layouts` -- Templates that wrap pages. The layout is chosen in the frontmatter" (source: Directory doc page). Layouts are compiled as Liquid templates and can use the `include` tag to pull in shared formatting from the `_includes` directory (source: Layouts doc page). A layout template accesses the wrapped page's content through the `{{ page.content }}` variable (source: Layouts doc page).

# Prerequisites

- **Directory Structure** -- understanding the overall Cobalt project layout

# Key Properties

1. **Contains Liquid templates** -- "Layouts are templates in the `_layouts` directory that contain the common formatting for your pages. They are compiled as liquid templates" (source: Layouts doc page).
2. **Wraps page content** -- layouts use `{{ page.content }}` to insert the page's rendered content (source: Layouts doc page).
3. **Selected via frontmatter** -- "The layout is chosen in the frontmatter" of each page (source: Directory doc page).
4. **Supports includes** -- "You can use the `include` Liquid tag to pull in shared formatting from the `_includes` directory" (source: Layouts doc page).
5. **Underscore-prefixed** -- as an underscore-prefixed directory, `_layouts` is hidden from the output and not copied to the destination.

# Construction / Recognition

## To Construct/Create:
1. Create a `_layouts` directory in the project root.
2. Add `.liquid` template files (e.g., `default.liquid`) containing HTML structure with `{{ page.content }}` for content insertion.
3. Reference layouts from page frontmatter using the `layout` field.

## To Identify/Recognize:
1. The `_layouts` directory at the project root.
2. Files within it are `.liquid` templates with HTML structure and Liquid template expressions.

# Context & Application

- **Typical contexts**: Defining the HTML wrapper (head, header, footer, navigation) for site pages.
- **Common applications**: Creating a default layout for all pages, creating specialized layouts for different page types (blog posts, landing pages, documentation).

# Examples

**Example 1** (source: Layouts doc page): A layout template using includes:
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

**Example 2** (source: Directory doc page): Default project structure showing `_layouts`:
```
|- _layouts
|  |- default.liquid
```

# Relationships

## Builds Upon
- **directory-structure** -- `_layouts` is a standard directory in the Cobalt project structure

## Enables
- **layout** -- layouts defined in `_layouts` are applied to pages
- **content-processing-pipeline** -- layout wrapping is step 3 of page processing (after Liquid evaluation and Markdown conversion)

## Related
- **includes-directory** -- layouts commonly use `{% include %}` to pull shared snippets from `_includes`
- **liquid-template-language** -- layouts are written in Liquid
- **template-variables** -- layouts access variables like `page.content`, `site.title`, etc.

## Contrasts With
- **includes-directory** -- `_layouts` contains full-page wrapper templates; `_includes` contains reusable snippets included within layouts or pages

# Common Errors

- **Error**: Forgetting to include `{{ page.content }}` in a layout template.
  **Correction**: Without `{{ page.content }}`, the page's actual content will not appear in the rendered output. Always include this variable where the content should be inserted.

# Common Confusions

- **Confusion**: Layouts and includes serve the same purpose.
  **Clarification**: Layouts are full-page wrapper templates that define the overall HTML structure. Includes are smaller, reusable snippets (headers, footers, navigation) that can be embedded within layouts or pages via `{% include %}`.

# Source Reference

Directory Structure doc page; Layouts doc page. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Directory doc page and Layouts doc page
- Confidence rationale: High -- the `_layouts` directory and its purpose are explicitly documented with examples
- Uncertainties: None significant
- Cross-reference status: References to directory-structure, includes-directory, layout, liquid-template-language, template-variables, content-processing-pipeline verified against planned card slugs
