---
# === CORE IDENTIFICATION ===
concept: Assign Tag
slug: assign-tag

# === CLASSIFICATION ===
category: liquid-tags
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Liquid Standard Library"
chapter_number: null
pdf_page: null
section: "AssignTag"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "variable assignment"
  - "assign statement"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - logic-tags
extends: []
related:
  - capture-block
  - template-variables
  - increment-decrement-tags
contrasts_with:
  - capture-block

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Liquid tag?"
  - "How do I use Liquid template variables in my pages?"
---

# Quick Definition

The `assign` tag creates a new variable or overwrites an existing one with a specified value. It is a self-closing tag that uses the syntax `{% assign variable_name = value %}`.

# Core Definition

The `assign` tag is implemented in the `liquid_lib` crate as `AssignTag` (source file: `stdlib/tags/assign_tag/`). It creates or updates a variable in the current template scope with a given value. The value can be a literal (string, number, boolean), another variable, or the result of applying filters to a value. Assign is a self-closing tag (no end tag needed). The assigned variable is available in the template scope from the point of assignment onward. (Source: liquid_lib stdlib AssignTag)

# Prerequisites

- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax.

# Key Properties

1. **Syntax**: `{% assign variable_name = value %}`.
2. **Self-closing**: No end tag required.
3. **Filter support**: Filters can be applied: `{% assign lower_title = page.title | downcase %}`.
4. **Scope**: Variables are available from the point of assignment onward.
5. **Overwrite**: Re-assigning a variable overwrites its previous value.
6. **Types preserved**: The assigned value retains its type (string, number, boolean, array, etc.).

# Construction / Recognition

## To Construct/Create:
1. Write `{% assign variable_name = value %}`.
2. Optionally apply filters: `{% assign x = value | filter %}`.
3. Use the variable later with `{{ variable_name }}`.

## To Identify/Recognize:
1. Look for `{% assign ... = ... %}` in templates.

# Context & Application

- **Typical contexts**: Creating computed variables, renaming variables for clarity, preparing values for later use.
- **Common applications**: Storing filtered values, creating boolean flags, simplifying complex expressions.

# Examples

**Example 1** (source: Liquid Standard Library): Simple variable assignment:
```liquid
{% assign site_name = site.title %}
<h1>{{ site_name }}</h1>
```

**Example 2** (source: Liquid Standard Library): Assigning with a filter:
```liquid
{% assign lower_title = page.title | downcase %}
<meta name="keywords" content="{{ lower_title }}">
```

# Relationships

## Builds Upon
- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax.

## Enables
- Creating reusable computed values in templates.

## Related
- **[Capture Block](/concept-cards/cobalt/capture-block.md)** -- Alternative for complex/multi-line assignments.
- **[Template Variables](/concept-cards/cobalt/template-variables.md)** -- Assigned variables join the template scope.
- **[Increment and Decrement Tags](/concept-cards/cobalt/increment-decrement-tags.md)** -- Other variable manipulation tags.

## Contrasts With
- **[Capture Block](/concept-cards/cobalt/capture-block.md)** -- `assign` sets a variable to a simple value or filter expression; `capture` renders a block of content and stores the string result. Assign preserves types; capture always produces a string.

# Common Errors

- **Error**: Forgetting the `=` sign in the assign syntax.
  **Correction**: The correct syntax is `{% assign name = value %}` with the equals sign.

# Common Confusions

- **Confusion**: Thinking assigned variables are available in included templates.
  **Clarification**: Variable scoping depends on the Liquid implementation. In general, variables assigned in a parent template may or may not be accessible in included partials depending on scope rules.

# Source Reference

Liquid Standard Library, AssignTag struct. Source: liquid_lib rustdoc (stdlib/tags/assign_tag/).

# Verification Notes

- Definition source: liquid_lib AssignTag struct documentation
- Confidence rationale: Standard Liquid feature, well-documented.
- Uncertainties: None.
- Cross-reference status: Verified in liquid_lib stdlib.
