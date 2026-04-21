---
# === CORE IDENTIFICATION ===
concept: Logic Tags
slug: logic-tags

# === CLASSIFICATION ===
category: liquid-basics
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Liquid Standard Library"
chapter_number: null
pdf_page: null
section: "Tags and Blocks"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "tag markup"
  - "curly-percent tags"
  - "{% %}"
  - "control tags"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - liquid-template-language
extends: []
related:
  - if-block
  - for-block
  - assign-tag
  - include
contrasts_with:
  - output-tags

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Liquid tag?"
  - "What distinguishes {{ }} from {% %}?"
  - "What must I know before writing Liquid templates?"
---

# Quick Definition

Logic tags use the `{% %}` (curly-percent) syntax to execute control flow, assignments, includes, and other operations in Liquid templates. Unlike output tags, logic tags do not directly render values into the output.

# Core Definition

In Liquid, logic tags (also called tag statements) are delimited by `{% %}`. They provide the control flow and execution capabilities of the template language: conditionals (`if`, `unless`, `case`), loops (`for`), variable assignment (`assign`, `capture`), template composition (`include`), and other operations (`cycle`, `increment`, `decrement`, `break`, `continue`, `comment`, `raw`). Logic tags are divided into two subcategories in the Liquid implementation: tags (self-closing, like `{% assign %}`) and blocks (paired with an end tag, like `{% if %}...{% endif %}`). (Source: liquid_lib stdlib rustdoc, Cobalt Layouts and Data Files documentation)

# Prerequisites

- **[Liquid Template Language](/concept-cards/cobalt/liquid-template-language.md)** -- Understanding the overall Liquid syntax framework.

# Key Properties

1. **Syntax**: Delimited by `{%` and `%}`.
2. **No direct output**: Logic tags execute operations but do not directly insert text (though blocks like `if` and `for` control which content is rendered).
3. **Tags vs. blocks**: Self-closing tags (e.g., `{% assign x = 1 %}`) vs. block tags that require an end tag (e.g., `{% if %}...{% endif %}`).
4. **Standard library**: The liquid_lib crate provides the full set of standard tags and blocks.
5. **Whitespace control**: Logic tags can control whitespace in the output.

# Construction / Recognition

## To Construct/Create:
1. Place the tag name and any arguments between `{%` and `%}`.
2. For block tags, include the corresponding end tag (e.g., `{% endif %}`, `{% endfor %}`).

## To Identify/Recognize:
1. Look for text enclosed in `{% %}` delimiters.
2. The first word after `{%` is the tag or block name.

# Context & Application

- **Typical contexts**: Controlling which content appears on a page, iterating over data collections, assigning computed values to variables, including partial templates.
- **Common applications**: Conditional navigation menus, blog post loops, variable assignment for reuse, including shared headers/footers.

# Examples

**Example 1** (source: Cobalt Data Files documentation): Using a `for` loop to iterate over data:
```html
<ul>
{% for breed in site.data.animals.dogs %}
  <li>{{ breed.name }}</li>
{% endfor %}
</ul>
```

**Example 2** (source: Cobalt Layouts documentation): Using `include` to pull in shared formatting:
```html
{% include "head.liquid" %}
```

# Relationships

## Builds Upon
- **[Liquid Template Language](/concept-cards/cobalt/liquid-template-language.md)** -- Logic tags are one of Liquid's two primary syntax forms.

## Enables
- **[If Block](/concept-cards/cobalt/if-block.md)** -- Conditional rendering.
- **[For Block](/concept-cards/cobalt/for-block.md)** -- Iteration.
- **[Assign Tag](/concept-cards/cobalt/assign-tag.md)** -- Variable assignment.
- **[Include](/concept-cards/cobalt/include.md)** -- Template composition.

## Related
- **[Comment Block](/concept-cards/cobalt/comment-block.md)** -- Non-rendered comments.
- **[Raw Block](/concept-cards/cobalt/raw-block.md)** -- Disabling Liquid processing.
- **[Capture Block](/concept-cards/cobalt/capture-block.md)** -- Capturing rendered content.

## Contrasts With
- **[Output Tags](/concept-cards/cobalt/output-tags.md)** -- Output tags use `{{ }}` and render values, while logic tags use `{% %}` and execute operations.

# Common Errors

- **Error**: Using `{{ }}` for control flow (e.g., `{{ if page.title }}`).
  **Correction**: Use `{% if page.title %}` for conditional logic.

- **Error**: Forgetting the end tag for a block (e.g., writing `{% if %}` without `{% endif %}`).
  **Correction**: Always close block tags with the corresponding end tag.

# Common Confusions

- **Confusion**: Not understanding the distinction between self-closing tags and block tags.
  **Clarification**: Self-closing tags like `{% assign %}` stand alone. Block tags like `{% if %}...{% endif %}` wrap content and require an end tag.

# Source Reference

Liquid Standard Library, "Tags and Blocks" section. Source: liquid_lib rustdoc, Cobalt documentation.

# Verification Notes

- Definition source: liquid_lib stdlib rustdoc and Cobalt documentation examples
- Confidence rationale: The syntax is consistently demonstrated across all documentation sources.
- Uncertainties: None.
- Cross-reference status: Verified across layouts.md, variables.md, data.md, and liquid_lib rustdoc.
