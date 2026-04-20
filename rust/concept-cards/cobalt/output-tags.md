---
# === CORE IDENTIFICATION ===
concept: Output Tags
slug: output-tags

# === CLASSIFICATION ===
category: liquid-basics
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Variables"
chapter_number: null
pdf_page: null
section: "Variables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "object tags"
  - "double curly braces"
  - "output markup"
  - "{{ }}"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - liquid-template-language
extends: []
related:
  - template-variables
  - string-filters
  - array-filters
  - math-filters
contrasts_with:
  - logic-tags

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes {{ }} from {% %}?"
  - "How do I use Liquid template variables in my pages?"
---

# Quick Definition

Output tags use the `{{ }}` (double curly brace) syntax to render the value of a variable or expression into the template output. They are the primary mechanism for displaying dynamic content in Liquid templates.

# Core Definition

In Liquid, output tags are delimited by double curly braces (`{{ }}`). When the template engine encounters an output tag, it evaluates the expression inside and inserts the resulting value into the rendered output. Output tags can contain variable references (e.g., `{{ page.title }}`), and can include filters applied via the pipe (`|`) character to transform the value before rendering (e.g., `{{ page.title | upcase }}`). Output tags never execute logic -- they only produce textual output. (Source: Cobalt Variables documentation)

# Prerequisites

- **[Liquid Template Language](/concept-cards/cobalt/liquid-template-language.md)** -- Understanding the overall Liquid syntax framework.

# Key Properties

1. **Syntax**: Delimited by `{{` and `}}`.
2. **Evaluation**: The expression inside is evaluated and its string representation is inserted into the output.
3. **Filter support**: Filters can be applied using the pipe `|` character: `{{ value | filter }}`.
4. **Filter chaining**: Multiple filters can be chained: `{{ value | filter1 | filter2 }}`.
5. **No side effects**: Output tags only produce output; they do not modify variables or control flow.
6. **Whitespace**: Leading/trailing whitespace inside the delimiters is ignored.

# Construction / Recognition

## To Construct/Create:
1. Place a variable name or expression between `{{` and `}}`.
2. Optionally append one or more filters using the pipe character.

## To Identify/Recognize:
1. Look for text enclosed in `{{ }}` delimiters.
2. The content will be a variable name, a dotted property path, or an expression with filters.

# Context & Application

- **Typical contexts**: Rendering page titles, descriptions, content, dates, and any dynamic data in layouts and pages.
- **Common applications**: Inserting `page.title` into HTML `<title>` tags, rendering `page.content` in layouts, displaying site-wide configuration values.

# Examples

**Example 1** (source: Cobalt Variables documentation): Rendering the page title and content in a layout:
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

**Example 2** (source: Liquid Standard Library): Using a filter with an output tag:
```
{{ "hello world" | capitalize }}
```
Renders: `Hello world`

# Relationships

## Builds Upon
- **[Liquid Template Language](/concept-cards/cobalt/liquid-template-language.md)** -- Output tags are one of Liquid's two primary syntax forms.

## Enables
- **[String Filters](/concept-cards/cobalt/string-filters.md)** -- Filters are applied within output tags.
- **[Array Filters](/concept-cards/cobalt/array-filters.md)** -- Filters are applied within output tags.
- **[Math Filters](/concept-cards/cobalt/math-filters.md)** -- Filters are applied within output tags.

## Related
- **[Template Variables](/concept-cards/cobalt/template-variables.md)** -- Variables are the most common content of output tags.
- **[Site Variable](/concept-cards/cobalt/site-variable.md)** -- Accessed via output tags.
- **[Page Variable](/concept-cards/cobalt/page-variable.md)** -- Accessed via output tags.

## Contrasts With
- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Logic tags use `{% %}` and execute control flow without directly producing output, while output tags use `{{ }}` and produce rendered text.

# Common Errors

- **Error**: Using `{% %}` when trying to output a variable value (e.g., `{% page.title %}`).
  **Correction**: Use `{{ page.title }}` to render a value. `{% %}` is for logic, not output.

- **Error**: Forgetting the closing `}}`, resulting in raw text appearing in the output.
  **Correction**: Ensure every `{{` has a matching `}}`.

# Common Confusions

- **Confusion**: Thinking output tags can contain assignment or conditional logic.
  **Clarification**: Output tags only evaluate and render values. For logic, use `{% %}` logic tags.

# Source Reference

Variables documentation, "Variables" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Cobalt Variables documentation examples
- Confidence rationale: The documentation consistently uses `{{ }}` for variable output with clear examples.
- Uncertainties: None.
- Cross-reference status: Verified across variables.md, layouts.md, and data.md examples.
