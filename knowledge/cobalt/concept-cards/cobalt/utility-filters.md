---
# === CORE IDENTIFICATION ===
concept: Utility Filters
slug: utility-filters

# === CLASSIFICATION ===
category: liquid-filters
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Liquid API Reference"
chapter_number: null
pdf_page: null
section: "stdlib::filters (Default, Size)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "default filter"
  - "size filter"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - liquid-template-language
  - output-tags
extends:
  - liquid-template-language
related:
  - string-filters
  - html-url-filters
  - date-filter
  - array-filters
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Cobalt's Liquid from Ruby Liquid?"
---

# Quick Definition
The utility filters `default` and `size` are general-purpose Liquid filters: `default` provides a fallback value when a variable is nil, false, or empty, and `size` returns the length of a string or array.

# Core Definition
The `default` and `size` filters are general-purpose utility filters in the Liquid Rust standard library. The `default` filter (struct `Default`) returns the input value if it is truthy and non-empty, or the specified default value otherwise. The `size` filter (struct `Size`) returns the number of characters in a string or the number of elements in an array. Both are implemented in the `liquid-lib` crate at the top level of the `stdlib::filters` module, and are functionally equivalent to their Ruby Liquid counterparts (source: liquid-lib rustdoc, `stdlib::filters::Default` and `stdlib::filters::Size`).

# Prerequisites
- Understanding of Liquid template language and filter syntax (see `liquid-template-language`)
- Understanding of output tags (see `output-tags`)

# Key Properties

## `default` Filter
1. **Fallback behavior**: Returns the default value when the input is nil, false, or an empty string.
2. **Parameter**: Takes one required argument -- the default value to use as fallback.
3. **Truthy pass-through**: If the input is truthy and non-empty, it is returned unchanged.
4. **Rust struct**: Implemented as `struct Default` in `liquid_lib::stdlib::filters`.

## `size` Filter
5. **String length**: When applied to a string, returns the number of characters.
6. **Array length**: When applied to an array, returns the number of elements.
7. **No parameters**: Takes no arguments.
8. **Rust struct**: Implemented as `struct Size` in `liquid_lib::stdlib::filters`.

# Construction / Recognition
## To Use:

### `default` filter:
```liquid
{{ page.author | default: "Anonymous" }}
<!-- Output: page.author value if set, otherwise "Anonymous" -->

{{ undefined_var | default: "fallback" }}
<!-- Output: "fallback" -->

{{ "" | default: "empty string fallback" }}
<!-- Output: "empty string fallback" -->
```

### `size` filter:
```liquid
{{ "Hello, World!" | size }}
<!-- Output: 13 -->

{{ page.tags | size }}
<!-- Output: number of tags -->

{% if page.tags | size > 0 %}
  This post has tags.
{% endif %}
```

# Context & Application
- **Typical contexts for `default`**: Providing fallback values for optional frontmatter fields, ensuring template output is never blank.
- **Typical contexts for `size`**: Conditional logic based on collection sizes, displaying counts, checking for empty collections.
- **When to use `default`**: When a variable might be nil or empty and you want a guaranteed output.
- **When to use `size`**: When you need the length of a string or the count of items in an array.

# Examples
**Example 1** (source: liquid-lib rustdoc): Default author name

```liquid
<p>Written by {{ page.author | default: "Unknown Author" }}</p>
```

**Example 2** (source: liquid-lib rustdoc): Conditional based on size

```liquid
{% assign tag_count = page.tags | size %}
{% if tag_count > 0 %}
  <p>Tags ({{ tag_count }}): {{ page.tags | join: ", " }}</p>
{% endif %}
```

# Relationships
## Builds Upon
- `liquid-template-language`: These are standard Liquid filters.
- `output-tags`: Used within output tag expressions.

## Enables
- Robust templates that handle missing or empty values gracefully.
- Dynamic content decisions based on collection sizes.

## Related
- `string-filters`: Other string manipulation filters.
- `array-filters`: The `size` filter is often used with arrays alongside array-specific filters.
- `html-url-filters`: Other standard filter categories.
- `date-filter`: Another standard filter.

## Contrasts With
- `default` is unique among filters in providing fallback behavior rather than transforming values.

# Common Errors
1. **Using `default` with false-y values unintentionally**: The `default` filter triggers on `false`, not just nil and empty string. If your variable is legitimately `false`, the default value will replace it.
2. **Applying `size` to a non-iterable**: Using `size` on a scalar value that is not a string may produce unexpected results.

# Common Confusions
1. **`default` vs. `assign` with conditional**: The `default` filter is a concise alternative to `{% if var %}{{ var }}{% else %}fallback{% endif %}`.
2. **`size` on nil**: Applying `size` to a nil value may return 0 or cause an error depending on context.

# Source Reference
- liquid-lib rustdoc: `stdlib::filters::Default`, `stdlib::filters::Size`.

# Verification Notes
- Both filter structs confirmed from `sources-html/liquid_lib/stdlib/filters/struct.Default.html` and `sources-html/liquid_lib/stdlib/filters/struct.Size.html`.
