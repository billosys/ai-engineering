---
# === CORE IDENTIFICATION ===
concept: Layout
slug: layout

# === CLASSIFICATION ===
category: templating
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Layouts"
chapter_number: null
pdf_page: null
section: "Layouts"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "page layout"
  - "template layout"
  - "layout template"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - liquid-template-language
extends: []
related:
  - include
  - template-variables
  - page-variable
  - frontmatter
  - directory-structure
contrasts_with:
  - include

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a layout in Cobalt?"
  - "How does a layout relate to page content?"
  - "How do I create and use layouts?"
  - "What distinguishes a layout from an include?"
  - "How do includes relate to layouts?"
---

# Quick Definition

A layout is a Liquid template file stored in the `_layouts` directory that provides the common structural formatting (HTML skeleton, headers, footers) for pages. The page's rendered content is inserted into the layout via the `{{ page.content }}` variable.

# Core Definition

Layouts in Cobalt are templates stored in the `_layouts` directory that "contain the common formatting for your pages" (source: Cobalt Layouts documentation). They are compiled as Liquid templates and serve as wrappers around page content. When a page specifies a layout in its frontmatter (e.g., `layout: default.liquid`), Cobalt renders the page's body content and then injects it into the layout at the point where `{{ page.content }}` appears. This separation of content from presentation allows multiple pages to share the same structural template while having unique content. (Source: Cobalt Layouts documentation)

# Prerequisites

- **[Liquid Template Language](/concept-cards/cobalt/liquid-template-language.md)** -- Layouts are Liquid templates and require understanding of Liquid syntax.

# Key Properties

1. **Location**: Stored in the `_layouts` directory.
2. **Format**: Compiled as Liquid templates.
3. **Content insertion**: The rendered page content is available as `{{ page.content }}` within the layout.
4. **Excerpt access**: The page excerpt is available as `{{ page.excerpt }}` within the layout.
5. **Variable access**: All site, page, and collection variables are accessible within layouts.
6. **Include support**: Layouts can use `{% include %}` to pull in reusable snippets from `_includes`.
7. **Frontmatter reference**: Pages specify their layout via the `layout` field in frontmatter.

# Construction / Recognition

## To Construct/Create:
1. Create a `.liquid` file in the `_layouts` directory (e.g., `_layouts/default.liquid`).
2. Write the HTML structure with Liquid template syntax.
3. Use `{{ page.content }}` where the page's body content should be inserted.
4. Optionally use `{% include %}` tags to pull in shared components.
5. Reference the layout from a page's frontmatter: `layout: default.liquid`.

## To Identify/Recognize:
1. Files located in the `_layouts` directory.
2. Typically contain `{{ page.content }}` to mark where page content is inserted.
3. Usually contain the overall HTML structure (`<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`).

# Context & Application

- **Typical contexts**: Defining the HTML skeleton shared across pages, wrapping page content with navigation, headers, and footers.
- **Common applications**: Site-wide layouts for consistent appearance, specialized layouts for different page types (blog posts vs. regular pages).

# Examples

**Example 1** (source: Cobalt Layouts documentation): A complete layout template:
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

# Relationships

## Builds Upon
- **[Liquid Template Language](/concept-cards/cobalt/liquid-template-language.md)** -- Layouts are compiled as Liquid templates.

## Enables
- **[Page](/concept-cards/cobalt/page.md)** -- Pages specify and use layouts for their presentation.
- **[Post](/concept-cards/cobalt/post.md)** -- Posts use layouts like any other page.

## Related
- **[Include](/concept-cards/cobalt/include.md)** -- Layouts use includes for shared components.
- **[Template Variables](/concept-cards/cobalt/template-variables.md)** -- Variables are accessible in layouts.
- **[Page Variable](/concept-cards/cobalt/page-variable.md)** -- `page.content` and `page.excerpt` are layout-specific variables.
- **[Frontmatter](/concept-cards/cobalt/frontmatter.md)** -- Pages specify their layout in frontmatter.
- **[Directory Structure](/concept-cards/cobalt/directory-structure.md)** -- Layouts live in the `_layouts` directory.

## Contrasts With
- **[Include](/concept-cards/cobalt/include.md)** -- Layouts wrap entire page content and define the page structure; includes are reusable snippets inserted within layouts or pages. A layout is the outer shell; an include is a component within it.

# Common Errors

- **Error**: Forgetting `{{ page.content }}` in the layout, causing page content to not appear.
  **Correction**: Always include `{{ page.content }}` in the layout where the page body should render.

- **Error**: Placing layout files outside the `_layouts` directory.
  **Correction**: Layouts must be in the `_layouts` directory to be found by Cobalt.

# Common Confusions

- **Confusion**: Thinking layouts and includes serve the same purpose.
  **Clarification**: Layouts are outer wrappers that define overall page structure. Includes are inner components pulled into layouts or pages for code reuse. A layout contains `{{ page.content }}`; an include is inserted via `{% include %}`.

# Source Reference

Layouts documentation, "Layouts" and "Reusing Formatting" sections. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Layouts documentation
- Confidence rationale: The documentation explicitly defines layouts with a complete example.
- Uncertainties: None.
- Cross-reference status: Verified against Variables documentation which documents layout-specific variables (page.content, page.excerpt).
