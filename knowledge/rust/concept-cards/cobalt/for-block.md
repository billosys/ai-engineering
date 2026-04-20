---
# === CORE IDENTIFICATION ===
concept: For Block
slug: for-block

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
section: "ForBlock"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "for loop"
  - "iteration block"
  - "for/endfor"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - logic-tags
extends: []
related:
  - forloop-object
  - break-continue-tags
  - cycle-tag
  - data-files
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Liquid block?"
  - "How do I use data files in templates?"
  - "What must I know before writing Liquid templates?"
---

# Quick Definition

The `for` block iterates over an array or range, rendering its enclosed content once for each element. The current element is assigned to a loop variable that can be used within the block body.

# Core Definition

The `for` block is a standard Liquid iteration construct implemented in the `liquid_lib` crate as `ForBlock` (source file: `stdlib/blocks/for_block.rs`). It iterates over arrays or ranges, rendering the enclosed content for each item. The loop variable is bound to each element in turn. The block supports an optional `else` clause (rendered when the collection is empty), `limit` and `offset` parameters for controlling the iteration range, and `reversed` for reverse iteration. A special `forloop` object is available inside the block providing loop metadata. The `for` block also supports the `break` and `continue` tags for loop control. (Source: liquid_lib stdlib ForBlock)

# Prerequisites

- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax.

# Key Properties

1. **Start tag**: `{% for item in collection %}`.
2. **End tag**: `{% endfor %}`.
3. **Loop variable**: The variable name before `in` receives each element.
4. **Empty handling**: `{% else %}` renders when the collection is empty.
5. **Limit**: `{% for item in array limit:3 %}` limits iterations.
6. **Offset**: `{% for item in array offset:2 %}` skips initial elements.
7. **Reversed**: `{% for item in array reversed %}` iterates in reverse order.
8. **Range support**: `{% for i in (1..5) %}` iterates over a numeric range.
9. **Forloop object**: `forloop.index`, `forloop.first`, `forloop.last`, etc. are available inside.

# Construction / Recognition

## To Construct/Create:
1. Write `{% for variable in collection %}` with a variable name and collection.
2. Place the content to repeat inside the block, using the loop variable.
3. Optionally add `{% else %}` for empty collection handling.
4. Close with `{% endfor %}`.

## To Identify/Recognize:
1. Look for `{% for ... in ... %}` opening tags.
2. Closed by `{% endfor %}`.

# Context & Application

- **Typical contexts**: Iterating over lists of posts, data file arrays, page tags, page categories.
- **Common applications**: Rendering blog post lists, navigation menus from data, tag clouds, list displays.

# Examples

**Example 1** (source: Cobalt Data Files documentation): Iterating over data file content:
```html
<ul>
{% for breed in site.data.animals.dogs %}
  <li>{{ breed.name }}</li>
{% endfor %}
</ul>
```

**Example 2** (source: Liquid Standard Library): Using limit, offset, and else:
```liquid
{% for post in collections.posts limit:5 offset:2 %}
  <h2>{{ post.title }}</h2>
{% else %}
  <p>No posts found.</p>
{% endfor %}
```

**Example 3** (source: Liquid Standard Library): Iterating over a range:
```liquid
{% for i in (1..5) %}
  {{ i }}
{% endfor %}
```

# Relationships

## Builds Upon
- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax.

## Enables
- **[Forloop Object](/concept-cards/cobalt/forloop-object.md)** -- Loop metadata available inside for blocks.
- **[Break and Continue Tags](/concept-cards/cobalt/break-continue-tags.md)** -- Loop control within for blocks.
- **[Cycle Tag](/concept-cards/cobalt/cycle-tag.md)** -- Often used within for blocks.

## Related
- **[Data Files](/concept-cards/cobalt/data-files.md)** -- Data file arrays are commonly iterated with for blocks.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Forgetting `{% endfor %}` to close the loop.
  **Correction**: Every `{% for %}` must have a matching `{% endfor %}`.

- **Error**: Using a nonexistent collection, resulting in no output and no error.
  **Correction**: Verify the collection path exists. Use `{% else %}` to handle empty/missing collections gracefully.

# Common Confusions

- **Confusion**: Expecting the `else` clause to execute when the variable is undefined vs. when the array is empty.
  **Clarification**: The `else` clause in a `for` block executes when the iterable is empty (has zero elements). If the variable is undefined/nil, the block simply produces no output.

# Source Reference

Liquid Standard Library, ForBlock struct. Source: liquid_lib rustdoc (stdlib/blocks/for_block.rs).

# Verification Notes

- Definition source: liquid_lib ForBlock struct and Cobalt Data Files documentation
- Confidence rationale: Standard Liquid feature with Cobalt-specific example in data.md.
- Uncertainties: None.
- Cross-reference status: Verified against data.md for usage patterns.
