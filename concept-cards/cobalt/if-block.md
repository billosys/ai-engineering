---
# === CORE IDENTIFICATION ===
concept: If Block
slug: if-block

# === CLASSIFICATION ===
category: liquid-blocks
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Liquid Standard Library"
chapter_number: null
pdf_page: null
section: "IfBlock"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "if/elsif/else"
  - "conditional block"
  - "if statement"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - logic-tags
extends: []
related:
  - unless-block
  - case-block
  - template-variables
contrasts_with:
  - unless-block

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Liquid block?"
  - "What must I know before writing Liquid templates?"
---

# Quick Definition

The `if` block provides conditional rendering in Liquid templates. Content between `{% if condition %}` and `{% endif %}` is only rendered when the condition evaluates to true. It supports `elsif` and `else` branches for multi-path logic.

# Core Definition

The `if` block is a standard Liquid block implemented in the `liquid_lib` crate as `IfBlock` (source file: `stdlib/blocks/if_block.rs`). It evaluates a condition and renders the enclosed content only if the condition is truthy. The block supports `elsif` for additional conditions and `else` for a fallback branch. Conditions can use comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`), logical operators (`and`, `or`), and the `contains` keyword. Truthy values include any non-nil, non-false value; empty strings and 0 are truthy in Liquid. (Source: liquid_lib stdlib IfBlock)

# Prerequisites

- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- The if block uses `{% %}` syntax.

# Key Properties

1. **Start tag**: `{% if condition %}`.
2. **End tag**: `{% endif %}`.
3. **Optional branches**: `{% elsif condition %}` and `{% else %}`.
4. **Truthiness**: nil and false are falsy; everything else (including 0 and empty string) is truthy.
5. **Operators**: `==`, `!=`, `<`, `>`, `<=`, `>=`, `and`, `or`, `contains`.
6. **Nesting**: If blocks can be nested inside other if blocks.

# Construction / Recognition

## To Construct/Create:
1. Write `{% if condition %}` with the condition to evaluate.
2. Place the content to conditionally render between if and endif.
3. Optionally add `{% elsif condition %}` and `{% else %}` branches.
4. Close with `{% endif %}`.

## To Identify/Recognize:
1. Look for `{% if ... %}` opening tags.
2. Closed by `{% endif %}`.

# Context & Application

- **Typical contexts**: Conditionally displaying page elements, checking for variable existence, showing/hiding content based on page properties.
- **Common applications**: Showing draft indicators, conditional navigation highlighting, checking if a variable has a value before rendering.

# Examples

**Example 1** (source: Liquid Standard Library): Basic conditional rendering:
```liquid
{% if page.is_draft %}
  <span class="draft">DRAFT</span>
{% endif %}
```

**Example 2** (source: Liquid Standard Library): Using elsif and else:
```liquid
{% if page.collection == "posts" %}
  <article>{{ page.content }}</article>
{% elsif page.title %}
  <div>{{ page.content }}</div>
{% else %}
  {{ page.content }}
{% endif %}
```

# Relationships

## Builds Upon
- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax.

## Enables
- Conditional template rendering based on data.

## Related
- **[Unless Block](/concept-cards/cobalt/unless-block.md)** -- Inverse conditional.
- **[Case Block](/concept-cards/cobalt/case-block.md)** -- Multi-branch conditional.
- **[Template Variables](/concept-cards/cobalt/template-variables.md)** -- Variables used in conditions.

## Contrasts With
- **[Unless Block](/concept-cards/cobalt/unless-block.md)** -- `unless` renders when the condition is false; `if` renders when the condition is true.

# Common Errors

- **Error**: Forgetting `{% endif %}` to close the block.
  **Correction**: Every `{% if %}` must have a matching `{% endif %}`.

- **Error**: Expecting empty strings or 0 to be falsy (as in many programming languages).
  **Correction**: In Liquid, only `nil` and `false` are falsy. Empty strings and 0 are truthy.

# Common Confusions

- **Confusion**: Using `{% if variable %}` to check if a variable has content vs. exists.
  **Clarification**: `{% if variable %}` checks truthiness. An empty string is truthy. To check for empty strings, use `{% if variable != "" %}` or `{% if variable.size > 0 %}`.

# Source Reference

Liquid Standard Library, IfBlock struct. Source: liquid_lib rustdoc (stdlib/blocks/if_block.rs).

# Verification Notes

- Definition source: liquid_lib IfBlock struct documentation
- Confidence rationale: Standard Liquid feature, well-documented in rustdoc.
- Uncertainties: None.
- Cross-reference status: Verified in liquid_lib stdlib.
