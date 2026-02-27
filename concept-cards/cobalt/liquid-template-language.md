---
# === CORE IDENTIFICATION ===
concept: Liquid Template Language
slug: liquid-template-language

# === CLASSIFICATION ===
category: liquid-basics
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
  - "Liquid"
  - "Liquid markup"
  - "Liquid templates"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - layout
  - template-variables
  - output-tags
  - logic-tags
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Liquid templating language?"
  - "What must I know before writing Liquid templates?"
  - "What distinguishes {{ }} from {% %}?"
---

# Quick Definition

Liquid is an open-source template language originally created by Shopify, used by Cobalt to process layouts, pages, and includes. It provides two primary syntax forms: output tags (`{{ }}`) for rendering values and logic tags (`{% %}`) for control flow and execution.

# Core Definition

Liquid is the templating engine that Cobalt uses for processing all template files. In the Cobalt/Rust ecosystem, Liquid is implemented as a native Rust crate (`liquid` v0.26.11, with its standard library in `liquid_lib`), providing a safe, sandboxed template rendering environment. Layouts in Cobalt are "compiled as liquid templates" (source: Cobalt Layouts documentation). Liquid templates consist of three main elements: objects/output tags (`{{ }}`), logic/tag statements (`{% %}`), and filters (transformations applied via the pipe `|` character within output tags). (Source: Cobalt Layouts documentation, liquid crate rustdoc)

# Prerequisites

Foundational concept with no prerequisites. Basic understanding of HTML and static site generation is helpful but not required.

# Key Properties

1. **Dual syntax**: Uses `{{ }}` for outputting values and `{% %}` for logic and control flow.
2. **Rust implementation**: Cobalt uses a native Rust implementation of Liquid (`liquid` crate v0.26.11), not the original Ruby implementation.
3. **Standard library**: The `liquid_lib` crate provides a standard library of blocks (if, for, case, unless, capture, comment, raw), tags (assign, cycle, include, increment, decrement, break, continue), and filters (string, array, math, HTML, URL).
4. **Safe rendering**: Templates are parsed and compiled before rendering, catching syntax errors early.
5. **Filter chaining**: Filters can be chained using the pipe character (`|`) to transform output values.

# Construction / Recognition

## To Construct/Create:
1. Create a file with a `.liquid` extension (or `.md` for Markdown pages).
2. Use `{{ variable }}` syntax to output dynamic values.
3. Use `{% tag %}` syntax for control flow (conditionals, loops, assignments).
4. Apply filters with the pipe syntax: `{{ variable | filter }}`.

## To Identify/Recognize:
1. Look for `{{ }}` and `{% %}` delimiters in template files.
2. Check for `.liquid` file extensions in `_layouts` and `_includes` directories.
3. Look for filter chains using the `|` character within output tags.

# Context & Application

- **Typical contexts**: Writing layouts, page templates, includes, and any file with a template extension in a Cobalt project.
- **Common applications**: Rendering page titles, inserting page content into layouts, iterating over collections, conditionally displaying content, formatting data with filters.

# Examples

**Example 1** (source: Cobalt Layouts documentation): A layout file using Liquid to render page content:
```html
<html>
  <head>
    <title>{{ page.title }}</title>
  </head>
  <body>
    {{ page.content }}
  </body>
</html>
```

**Example 2** (source: liquid crate rustdoc): Using a filter in Liquid:
```
Liquid! {{ num | minus: 2 }}
```
With `num` set to 4, this renders: `Liquid! 2`.

# Relationships

## Builds Upon
- No prerequisites -- Liquid is the foundational templating concept.

## Enables
- **[Output Tags](/concept-cards/cobalt/output-tags.md)** -- The `{{ }}` syntax for rendering values.
- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- The `{% %}` syntax for control flow.
- **[Layout](/concept-cards/cobalt/layout.md)** -- Layouts are Liquid templates.
- **[Template Variables](/concept-cards/cobalt/template-variables.md)** -- Variables are accessed through Liquid syntax.

## Related
- **[Page](/concept-cards/cobalt/page.md)** -- Pages are processed through Liquid.
- **[Post](/concept-cards/cobalt/post.md)** -- Posts are processed through Liquid.
- **[Include](/concept-cards/cobalt/include.md)** -- Includes are Liquid partials.

## Contrasts With
- None within Cobalt (Liquid is the only supported template language).

# Common Errors

- **Error**: Using Ruby Liquid syntax features not supported by the Rust implementation.
  **Correction**: Consult the `liquid_lib` crate documentation for the specific set of supported blocks, tags, and filters in Cobalt's Rust-based Liquid.

- **Error**: Forgetting that Liquid processing occurs before Markdown rendering.
  **Correction**: Liquid template syntax is processed first, then the result is passed through Markdown rendering (for `.md` files).

# Common Confusions

- **Confusion**: Thinking `{{ }}` and `{% %}` are interchangeable.
  **Clarification**: `{{ }}` outputs a value to the page; `{% %}` executes logic without producing output (unless the enclosed block renders content).

- **Confusion**: Assuming Cobalt's Liquid is identical to Shopify's Ruby Liquid.
  **Clarification**: While the syntax is largely compatible, Cobalt uses a Rust implementation that may have minor differences in available filters or behavior.

# Source Reference

Layouts documentation, "Layouts" section; liquid crate v0.26.11 rustdoc. Source: Cobalt documentation.

# Verification Notes

- Definition source: Cobalt Layouts documentation and liquid crate rustdoc
- Confidence rationale: The documentation explicitly states layouts are "compiled as liquid templates" and links to the Liquid reference.
- Uncertainties: None for the core definition.
- Cross-reference status: Verified across layouts.md, variables.md, and liquid crate rustdoc.
