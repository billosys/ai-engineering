---
# === CORE IDENTIFICATION ===
concept: Include
slug: include

# === CLASSIFICATION ===
category: templating
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Layouts"
chapter_number: null
pdf_page: null
section: "Reusing Formatting"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "partial"
  - "include tag"
  - "template include"
  - "snippet"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - liquid-template-language
  - logic-tags
extends: []
related:
  - layout
  - directory-structure
contrasts_with:
  - layout

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an include in Cobalt?"
  - "How do includes relate to layouts?"
  - "What distinguishes a layout from an include?"
---

# Quick Definition

An include is a reusable Liquid template snippet stored in the `_includes` directory that can be inserted into layouts or pages using the `{% include %}` tag. Includes enable DRY (Don't Repeat Yourself) template composition.

# Core Definition

Includes in Cobalt are template fragments stored in the `_includes` directory that provide shared formatting components. As the Cobalt documentation states: "You can use the `include` Liquid tag to pull in shared formatting from the `_includes` directory." Includes are referenced by filename (e.g., `{% include "header.liquid" %}`) and are rendered inline at the point of inclusion. The `include` tag is implemented in the liquid_lib crate as `IncludeTag`. (Source: Cobalt Layouts documentation, liquid_lib stdlib)

# Prerequisites

- **[Liquid Template Language](/concept-cards/cobalt/liquid-template-language.md)** -- Includes are Liquid template files.
- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- The `{% include %}` syntax uses logic tag delimiters.

# Key Properties

1. **Location**: Stored in the `_includes` directory.
2. **Syntax**: Invoked with `{% include "filename.liquid" %}`.
3. **Inline rendering**: The include's content is rendered at the point of the tag.
4. **Reusability**: The same include can be used in multiple layouts and pages.
5. **Variable access**: Includes have access to the same variables as the template that includes them.
6. **File naming**: Include files are referenced by their filename (with extension).

# Construction / Recognition

## To Construct/Create:
1. Create a `.liquid` file in the `_includes` directory (e.g., `_includes/header.liquid`).
2. Write the reusable HTML/Liquid content in the file.
3. Reference the include from a layout or page: `{% include "header.liquid" %}`.

## To Identify/Recognize:
1. Files located in the `_includes` directory.
2. Typically contain HTML fragments (not complete HTML documents).
3. Referenced via `{% include "..." %}` in other templates.

# Context & Application

- **Typical contexts**: Shared navigation menus, headers, footers, sidebars, metadata blocks, and any repeated template fragment.
- **Common applications**: Separating layout components into maintainable files, reusing common HTML structures across multiple layouts.

# Examples

**Example 1** (source: Cobalt Layouts documentation): A layout using three includes for head, header, and footer:
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
- **[Liquid Template Language](/concept-cards/cobalt/liquid-template-language.md)** -- Includes are Liquid template files.
- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- The include tag uses `{% %}` syntax.

## Enables
- Modular template design -- breaking complex layouts into manageable components.

## Related
- **[Layout](/concept-cards/cobalt/layout.md)** -- Layouts commonly use includes for shared components.
- **[Directory Structure](/concept-cards/cobalt/directory-structure.md)** -- Includes live in the `_includes` directory.

## Contrasts With
- **[Layout](/concept-cards/cobalt/layout.md)** -- A layout wraps an entire page's content and defines overall structure; an include is a fragment inserted into a layout or page. Layouts are referenced from frontmatter; includes are referenced from within templates via `{% include %}`.

# Common Errors

- **Error**: Placing include files outside the `_includes` directory.
  **Correction**: Include files must be in the `_includes` directory to be found by the `{% include %}` tag.

- **Error**: Omitting the file extension in the include tag.
  **Correction**: Use the full filename including extension: `{% include "header.liquid" %}`.

# Common Confusions

- **Confusion**: Thinking includes are the same as layouts.
  **Clarification**: Layouts wrap page content (they contain `{{ page.content }}`). Includes are fragments pulled into layouts or pages. Layouts are specified in frontmatter; includes are called from within templates.

# Source Reference

Layouts documentation, "Reusing Formatting" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Cobalt Layouts documentation
- Confidence rationale: The documentation explicitly describes includes with a clear example.
- Uncertainties: None.
- Cross-reference status: Verified against the liquid_lib IncludeTag struct documentation.
