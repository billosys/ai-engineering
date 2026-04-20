---
# === CORE IDENTIFICATION ===
concept: Capture Block
slug: capture-block

# === CLASSIFICATION ===
category: liquid-blocks
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Liquid Standard Library"
chapter_number: null
pdf_page: null
section: "CaptureBlock"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "capture tag"
  - "capture variable"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - logic-tags
extends: []
related:
  - assign-tag
  - template-variables
contrasts_with:
  - assign-tag

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Liquid block?"
---

# Quick Definition

The `capture` block renders its enclosed content and stores the result as a string in a named variable, rather than outputting it directly. This allows complex content to be computed once and reused later in the template.

# Core Definition

The `capture` block is implemented in the `liquid_lib` crate as `CaptureBlock` (source file: `stdlib/blocks/capture_block.rs`). It renders all content between `{% capture variable_name %}` and `{% endcapture %}` and assigns the rendered string to the named variable. The captured content can include other Liquid tags, output tags, and HTML. Unlike `assign` (which assigns simple values or expressions), `capture` can store multi-line rendered content including the results of loops, conditionals, and includes. (Source: liquid_lib stdlib CaptureBlock)

# Prerequisites

- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax.

# Key Properties

1. **Start tag**: `{% capture variable_name %}`.
2. **End tag**: `{% endcapture %}`.
3. **Rendered content**: The enclosed content is fully rendered (Liquid processed) before being stored.
4. **String result**: The captured value is always a string.
5. **Scope**: The variable is available in the current template scope after capture.

# Construction / Recognition

## To Construct/Create:
1. Write `{% capture variable_name %}` with the desired variable name.
2. Place content (HTML, Liquid tags, output tags) inside the block.
3. Close with `{% endcapture %}`.
4. Use the variable later as `{{ variable_name }}`.

## To Identify/Recognize:
1. Look for `{% capture ... %}` opening tags.
2. Closed by `{% endcapture %}`.

# Context & Application

- **Typical contexts**: Building complex strings from multiple parts, creating reusable content fragments within a template.
- **Common applications**: Constructing URLs from multiple parts, building meta tags with computed content, creating variables that depend on conditionals or loops.

# Examples

**Example 1** (source: Liquid Standard Library): Capturing a constructed URL:
```liquid
{% capture full_url %}{{ site.base_url }}{{ page.permalink }}{% endcapture %}
<a href="{{ full_url }}">{{ page.title }}</a>
```

**Example 2** (source: Liquid Standard Library): Capturing content with conditionals:
```liquid
{% capture page_class %}
  {% if page.is_draft %}draft{% else %}published{% endif %}
{% endcapture %}
<div class="{{ page_class | strip }}">{{ page.content }}</div>
```

# Relationships

## Builds Upon
- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax.

## Enables
- Complex variable construction from rendered content.

## Related
- **[Assign Tag](/concept-cards/cobalt/assign-tag.md)** -- Simpler variable assignment.
- **[Template Variables](/concept-cards/cobalt/template-variables.md)** -- Captured values become template variables.

## Contrasts With
- **[Assign Tag](/concept-cards/cobalt/assign-tag.md)** -- `assign` sets a variable to a simple value or expression. `capture` renders a block of content and stores the result as a string. Use `assign` for simple values; use `capture` for complex rendered content.

# Common Errors

- **Error**: Expecting captured content to preserve its original type (e.g., array or number).
  **Correction**: Capture always produces a string. For non-string assignments, use `assign`.

# Common Confusions

- **Confusion**: Thinking capture outputs content directly.
  **Clarification**: Capture stores content in a variable without rendering it to the page. You must explicitly output the variable with `{{ variable_name }}` later.

# Source Reference

Liquid Standard Library, CaptureBlock struct. Source: liquid_lib rustdoc (stdlib/blocks/capture_block.rs).

# Verification Notes

- Definition source: liquid_lib CaptureBlock struct documentation
- Confidence rationale: Standard Liquid feature, well-documented.
- Uncertainties: None.
- Cross-reference status: Verified in liquid_lib stdlib.
