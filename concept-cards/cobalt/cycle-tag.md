---
# === CORE IDENTIFICATION ===
concept: Cycle Tag
slug: cycle-tag

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
section: "CycleTag"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "cycle through values"
  - "alternating values"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - logic-tags
  - for-block
extends: []
related:
  - forloop-object
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Liquid tag?"
---

# Quick Definition

The `cycle` tag rotates through a group of string values each time it is called, outputting the next value in sequence. It is commonly used inside `for` loops to alternate CSS classes (e.g., odd/even row styling).

# Core Definition

The `cycle` tag is implemented in the `liquid_lib` crate as `CycleTag` (source file: `stdlib/tags/cycle_tag/`). It accepts a list of string values and outputs them in order, cycling back to the first after reaching the last. Each call advances the position by one. An optional group name can be specified to maintain separate cycle states: `{% cycle "group": "a", "b", "c" %}`. Without a group name, all cycle tags with the same values share a counter. (Source: liquid_lib stdlib CycleTag)

# Prerequisites

- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax.
- **[For Block](/concept-cards/cobalt/for-block.md)** -- Cycle is typically used inside for loops.

# Key Properties

1. **Syntax**: `{% cycle "value1", "value2", "value3" %}`.
2. **Named groups**: `{% cycle "group_name": "value1", "value2" %}`.
3. **Auto-advancing**: Each call outputs the next value in the list.
4. **Wrapping**: After the last value, it wraps back to the first.
5. **Shared counter**: Unnamed cycles with the same values share state.

# Construction / Recognition

## To Construct/Create:
1. Place `{% cycle "value1", "value2" %}` inside a for loop.
2. Optionally name the cycle group: `{% cycle "group": "value1", "value2" %}`.

## To Identify/Recognize:
1. Look for `{% cycle ... %}` tags.
2. Typically found inside `{% for %}` blocks.

# Context & Application

- **Typical contexts**: Inside for loops for alternating styling.
- **Common applications**: Alternating row colors (zebra striping), rotating CSS classes, creating visual patterns.

# Examples

**Example 1** (source: Liquid Standard Library): Alternating CSS classes in a list:
```liquid
{% for item in site.data.items %}
  <div class="{% cycle 'odd', 'even' %}">
    {{ item.name }}
  </div>
{% endfor %}
```
Outputs: `odd`, `even`, `odd`, `even`, ...

# Relationships

## Builds Upon
- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax.
- **[For Block](/concept-cards/cobalt/for-block.md)** -- Typically used inside loops.

## Enables
- Alternating patterns in rendered output.

## Related
- **[Forloop Object](/concept-cards/cobalt/forloop-object.md)** -- Both provide loop-related functionality.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Expecting cycle to work outside of loops.
  **Correction**: While cycle technically works outside loops, its state advances on each call. It is most useful inside loops.

# Common Confusions

- **Confusion**: Not understanding shared vs. named cycle groups.
  **Clarification**: Unnamed cycles with the same values share a counter. Use named groups to maintain independent counters.

# Source Reference

Liquid Standard Library, CycleTag struct. Source: liquid_lib rustdoc (stdlib/tags/cycle_tag/).

# Verification Notes

- Definition source: liquid_lib CycleTag struct documentation
- Confidence rationale: Standard Liquid feature, well-documented.
- Uncertainties: None.
- Cross-reference status: Verified in liquid_lib stdlib.
