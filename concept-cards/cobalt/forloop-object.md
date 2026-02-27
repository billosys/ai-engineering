---
# === CORE IDENTIFICATION ===
concept: Forloop Object
slug: forloop-object

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
section: "ForloopObject"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "forloop variable"
  - "loop metadata"
  - "loop context"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - for-block
extends: []
related:
  - cycle-tag
  - break-continue-tags
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Liquid block?"
---

# Quick Definition

The `forloop` object is automatically available inside `{% for %}` blocks and provides metadata about the current iteration, including the index, whether it is the first or last iteration, and the total length of the collection.

# Core Definition

The `forloop` object is implemented in the `liquid_lib` crate as `ForloopObject` (source: `stdlib/struct.ForloopObject.html`). It is automatically injected into the scope of every `{% for %}` block and provides properties that describe the current state of the iteration. The ForloopObject implements `ObjectView` and provides fields accessible via dot notation. Available properties include 0-based and 1-based indices, first/last flags, and the total collection length. These properties are essential for conditional formatting within loops (e.g., adding separators, special styling for first/last items). (Source: liquid_lib stdlib ForloopObject)

# Prerequisites

- **[For Block](/concept-cards/cobalt/for-block.md)** -- The forloop object only exists inside for blocks.

# Key Properties

1. **`forloop.index`**: 1-based index of the current iteration (starts at 1).
2. **`forloop.index0`**: 0-based index of the current iteration (starts at 0).
3. **`forloop.rindex`**: Reverse 1-based index (counts down to 1).
4. **`forloop.rindex0`**: Reverse 0-based index (counts down to 0).
5. **`forloop.first`**: Boolean, true on the first iteration.
6. **`forloop.last`**: Boolean, true on the last iteration.
7. **`forloop.length`**: Total number of items in the collection.

# Construction / Recognition

## To Construct/Create:
1. The forloop object is automatically available inside any `{% for %}` block.
2. No explicit construction is needed.
3. Access properties via `forloop.property_name`.

## To Identify/Recognize:
1. Any reference to `forloop.*` within a `{% for %}` block.

# Context & Application

- **Typical contexts**: Inside for loops where iteration-aware formatting is needed.
- **Common applications**: Adding commas between list items (skip last), special styling for first/last items, numbering items, tracking position within a collection.

# Examples

**Example 1** (source: Liquid Standard Library): Numbering items in a list:
```liquid
{% for item in site.data.items %}
  <div>{{ forloop.index }}. {{ item.name }}</div>
{% endfor %}
```

**Example 2** (source: Liquid Standard Library): Adding a separator between items:
```liquid
{% for tag in page.tags %}
  {{ tag }}{% unless forloop.last %}, {% endunless %}
{% endfor %}
```

**Example 3** (source: Liquid Standard Library): Special first-item styling:
```liquid
{% for post in collections.posts %}
  {% if forloop.first %}
    <div class="featured">{{ post.title }}</div>
  {% else %}
    <div>{{ post.title }}</div>
  {% endif %}
{% endfor %}
```

# Relationships

## Builds Upon
- **[For Block](/concept-cards/cobalt/for-block.md)** -- The forloop object is created by the for block.

## Enables
- Position-aware rendering within loops.

## Related
- **[Cycle Tag](/concept-cards/cobalt/cycle-tag.md)** -- Alternative for alternating values in loops.
- **[Break and Continue Tags](/concept-cards/cobalt/break-continue-tags.md)** -- Loop control used alongside forloop.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Accessing `forloop` outside of a `{% for %}` block.
  **Correction**: The `forloop` object only exists inside for blocks.

- **Error**: Using `forloop.index` expecting 0-based indexing.
  **Correction**: `forloop.index` is 1-based. Use `forloop.index0` for 0-based indexing.

# Common Confusions

- **Confusion**: Confusing `forloop.index` (1-based) with `forloop.index0` (0-based).
  **Clarification**: `index` starts at 1, `index0` starts at 0. Similarly, `rindex` counts down to 1, `rindex0` counts down to 0.

# Source Reference

Liquid Standard Library, ForloopObject struct. Source: liquid_lib rustdoc.

# Verification Notes

- Definition source: liquid_lib ForloopObject struct documentation
- Confidence rationale: Standard Liquid feature with clear property documentation.
- Uncertainties: None.
- Cross-reference status: Verified in liquid_lib stdlib.
