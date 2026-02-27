---
# === CORE IDENTIFICATION ===
concept: Unless Block
slug: unless-block

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
section: "UnlessBlock"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "negative conditional"
  - "unless statement"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - logic-tags
  - if-block
extends:
  - if-block
related:
  - case-block
contrasts_with:
  - if-block

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Liquid block?"
---

# Quick Definition

The `unless` block is a negative conditional in Liquid that renders its content only when the condition evaluates to false. It is the logical inverse of the `if` block.

# Core Definition

The `unless` block is implemented in the `liquid_lib` crate as `UnlessBlock` (defined in the same source file as `IfBlock`: `stdlib/blocks/if_block.rs`). It evaluates a condition and renders the enclosed content only when the condition is falsy (nil or false). The `unless` block supports `else` branches but does not support `elsif`. It provides a more readable alternative to `{% if condition == false %}` or `{% if condition != true %}`. (Source: liquid_lib stdlib UnlessBlock)

# Prerequisites

- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax.
- **[If Block](/concept-cards/cobalt/if-block.md)** -- Understanding conditional logic.

# Key Properties

1. **Start tag**: `{% unless condition %}`.
2. **End tag**: `{% endunless %}`.
3. **Inverse logic**: Renders when the condition is falsy.
4. **Else support**: Supports `{% else %}` for the truthy branch.
5. **No elsif**: Does not support `elsif` (use `if/elsif/else` for multi-branch logic).

# Construction / Recognition

## To Construct/Create:
1. Write `{% unless condition %}` with the condition to check.
2. Place content that should render when the condition is false.
3. Optionally add `{% else %}` for the true case.
4. Close with `{% endunless %}`.

## To Identify/Recognize:
1. Look for `{% unless ... %}` opening tags.
2. Closed by `{% endunless %}`.

# Context & Application

- **Typical contexts**: Hiding content when a condition is met, providing a more natural reading for negative conditions.
- **Common applications**: Hiding draft indicators on published pages, excluding content when a variable is set.

# Examples

**Example 1** (source: Liquid Standard Library): Rendering content unless the page is a draft:
```liquid
{% unless page.is_draft %}
  <span class="published">Published</span>
{% endunless %}
```

**Example 2** (source: Liquid Standard Library): Using unless with else:
```liquid
{% unless page.title %}
  <h1>Untitled</h1>
{% else %}
  <h1>{{ page.title }}</h1>
{% endunless %}
```

# Relationships

## Builds Upon
- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax.
- **[If Block](/concept-cards/cobalt/if-block.md)** -- Unless is the logical inverse.

## Enables
- Cleaner negative conditional expressions.

## Related
- **[Case Block](/concept-cards/cobalt/case-block.md)** -- Another conditional construct.

## Contrasts With
- **[If Block](/concept-cards/cobalt/if-block.md)** -- `if` renders on true; `unless` renders on false. `{% unless x %}` is equivalent to `{% if x == false %}` or `{% if x == nil %}`.

# Common Errors

- **Error**: Trying to use `{% elsif %}` inside an `unless` block.
  **Correction**: `unless` does not support `elsif`. Use `{% if %}` with `{% elsif %}` for multi-branch conditions.

# Common Confusions

- **Confusion**: Thinking `unless` is a simple alias for `if not`.
  **Clarification**: While logically equivalent to a negated `if`, `unless` only supports a simple condition and `else`, not `elsif`. For complex multi-branch logic, use `if/elsif/else`.

# Source Reference

Liquid Standard Library, UnlessBlock struct. Source: liquid_lib rustdoc (stdlib/blocks/if_block.rs).

# Verification Notes

- Definition source: liquid_lib UnlessBlock struct documentation
- Confidence rationale: Standard Liquid feature, implemented alongside IfBlock.
- Uncertainties: None.
- Cross-reference status: Verified in liquid_lib stdlib alongside IfBlock.
