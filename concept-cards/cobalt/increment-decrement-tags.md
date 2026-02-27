---
# === CORE IDENTIFICATION ===
concept: Increment and Decrement Tags
slug: increment-decrement-tags

# === CLASSIFICATION ===
category: liquid-tags
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Liquid Standard Library"
chapter_number: null
pdf_page: null
section: "IncrementTag / DecrementTag"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "counter tags"
  - "increment tag"
  - "decrement tag"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - logic-tags
extends: []
related:
  - assign-tag
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Liquid tag?"
---

# Quick Definition

The `increment` and `decrement` tags create and manage named counters. `{% increment counter %}` outputs the current counter value and then increments it; `{% decrement counter %}` outputs the current value and then decrements it.

# Core Definition

The `increment` tag is implemented as `IncrementTag` and the `decrement` tag as `DecrementTag` in the `liquid_lib` crate (source: `stdlib/tags/increment_tags/`). `{% increment variable_name %}` creates a counter (initialized to 0 on first use), outputs its current value, and then increments it by 1. `{% decrement variable_name %}` creates a counter (initialized to 0 on first use), decrements it by 1, and then outputs the resulting value (so the first output is -1). Importantly, increment/decrement counters have their own namespace separate from variables created with `assign` -- they do not interfere with each other. (Source: liquid_lib stdlib IncrementTag, DecrementTag)

# Prerequisites

- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax.

# Key Properties

1. **Increment syntax**: `{% increment counter_name %}`.
2. **Decrement syntax**: `{% decrement counter_name %}`.
3. **Initialization**: Counters start at 0 on first use.
4. **Output and modify**: The tag both outputs the value AND changes the counter.
5. **Separate namespace**: Independent from `assign` variables with the same name.
6. **Persistent**: Counter values persist across multiple calls within the same template.

# Construction / Recognition

## To Construct/Create:
1. Write `{% increment name %}` to create/advance a counter.
2. Write `{% decrement name %}` to create/decrease a counter.

## To Identify/Recognize:
1. Look for `{% increment ... %}` or `{% decrement ... %}` tags.

# Context & Application

- **Typical contexts**: Generating unique IDs, creating sequential numbering, tracking counts.
- **Common applications**: Creating unique element IDs in HTML, sequential numbering for footnotes or references.

# Examples

**Example 1** (source: Liquid Standard Library): Using increment for sequential IDs:
```liquid
{% increment my_counter %}
{% increment my_counter %}
{% increment my_counter %}
```
Outputs: `0`, `1`, `2`

**Example 2** (source: Liquid Standard Library): Using decrement:
```liquid
{% decrement my_counter %}
{% decrement my_counter %}
{% decrement my_counter %}
```
Outputs: `-1`, `-2`, `-3`

# Relationships

## Builds Upon
- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax.

## Enables
- Automatic counter management in templates.

## Related
- **[Assign Tag](/concept-cards/cobalt/assign-tag.md)** -- Alternative variable creation (but different namespace).

## Contrasts With
- None directly.

# Common Errors

- **Error**: Expecting increment/decrement to share a namespace with assign variables.
  **Correction**: Increment/decrement counters are independent from assign variables. `{% assign x = 5 %}` and `{% increment x %}` manage separate values.

# Common Confusions

- **Confusion**: Expecting increment to only change the value without outputting it.
  **Clarification**: Both increment and decrement both output a value AND modify the counter. If you only want to modify a counter without output, consider using `assign` with math filters.

# Source Reference

Liquid Standard Library, IncrementTag and DecrementTag structs. Source: liquid_lib rustdoc (stdlib/tags/increment_tags/).

# Verification Notes

- Definition source: liquid_lib IncrementTag and DecrementTag struct documentation
- Confidence rationale: Standard Liquid feature, well-documented.
- Uncertainties: None.
- Cross-reference status: Verified in liquid_lib stdlib.
