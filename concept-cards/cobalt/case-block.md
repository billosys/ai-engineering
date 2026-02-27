---
# === CORE IDENTIFICATION ===
concept: Case Block
slug: case-block

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
section: "CaseBlock"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "switch block"
  - "case/when"
  - "case statement"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - logic-tags
extends: []
related:
  - if-block
  - unless-block
contrasts_with:
  - if-block

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Liquid block?"
---

# Quick Definition

The `case` block provides switch-like conditional rendering in Liquid, matching a variable's value against multiple `when` clauses. It is more readable than chained `if/elsif` blocks when comparing a single value against several options.

# Core Definition

The `case` block is implemented in the `liquid_lib` crate as `CaseBlock` (source file: `stdlib/blocks/case_block.rs`). It evaluates a variable and compares its value against one or more `when` clauses, rendering the content of the first matching clause. An optional `else` clause provides a default when no `when` matches. Multiple values can be specified in a single `when` using `or`. (Source: liquid_lib stdlib CaseBlock)

# Prerequisites

- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax.

# Key Properties

1. **Start tag**: `{% case variable %}`.
2. **Branch tags**: `{% when value %}`.
3. **Default branch**: `{% else %}` for unmatched cases.
4. **End tag**: `{% endcase %}`.
5. **Multiple values**: `{% when "a" or "b" %}` matches either value.
6. **Equality comparison**: Uses equality matching (not pattern matching).

# Construction / Recognition

## To Construct/Create:
1. Write `{% case variable %}` with the variable to match.
2. Add `{% when value %}` clauses with content for each case.
3. Optionally add `{% else %}` for a default case.
4. Close with `{% endcase %}`.

## To Identify/Recognize:
1. Look for `{% case ... %}` opening tags.
2. Contains `{% when ... %}` branches.
3. Closed by `{% endcase %}`.

# Context & Application

- **Typical contexts**: Rendering different content based on a page's collection, type, or category.
- **Common applications**: Switching layout sections based on page type, varying CSS classes based on categories.

# Examples

**Example 1** (source: Liquid Standard Library): Rendering different content based on page collection:
```liquid
{% case page.collection %}
  {% when "posts" %}
    <article class="post">{{ page.content }}</article>
  {% when "pages" %}
    <div class="page">{{ page.content }}</div>
  {% else %}
    <div>{{ page.content }}</div>
{% endcase %}
```

# Relationships

## Builds Upon
- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax.

## Enables
- Clean multi-branch conditional rendering.

## Related
- **[If Block](/concept-cards/cobalt/if-block.md)** -- Alternative conditional construct.
- **[Unless Block](/concept-cards/cobalt/unless-block.md)** -- Negative conditional.

## Contrasts With
- **[If Block](/concept-cards/cobalt/if-block.md)** -- `if/elsif` evaluates arbitrary conditions; `case/when` matches a single variable against specific values. Case is cleaner for value matching; if is more flexible for complex conditions.

# Common Errors

- **Error**: Forgetting `{% endcase %}` to close the block.
  **Correction**: Every `{% case %}` must have a matching `{% endcase %}`.

# Common Confusions

- **Confusion**: Expecting fall-through behavior like C/JavaScript switch statements.
  **Clarification**: Liquid's `case` does not fall through. Only the first matching `when` clause is rendered.

# Source Reference

Liquid Standard Library, CaseBlock struct. Source: liquid_lib rustdoc (stdlib/blocks/case_block.rs).

# Verification Notes

- Definition source: liquid_lib CaseBlock struct documentation
- Confidence rationale: Standard Liquid feature, well-documented.
- Uncertainties: None.
- Cross-reference status: Verified in liquid_lib stdlib.
