---
# === CORE IDENTIFICATION ===
concept: Break and Continue Tags
slug: break-continue-tags

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
section: "BreakTag / ContinueTag"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "loop control tags"
  - "break tag"
  - "continue tag"

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

The `break` tag immediately exits a `for` loop, stopping all further iterations. The `continue` tag skips the rest of the current iteration and proceeds to the next element in the loop.

# Core Definition

The `break` tag is implemented as `BreakTag` and the `continue` tag as `ContinueTag` in the `liquid_lib` crate (source: `stdlib/tags/interrupt_tags/`). When `{% break %}` is encountered inside a `for` block, the loop terminates immediately and no further iterations are executed. When `{% continue %}` is encountered, the remaining content for the current iteration is skipped, and the loop advances to the next element. Both tags are typically used inside conditional blocks within a for loop to implement early termination or selective processing. (Source: liquid_lib stdlib BreakTag, ContinueTag)

# Prerequisites

- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax.
- **[For Block](/concept-cards/cobalt/for-block.md)** -- Only meaningful inside for loops.

# Key Properties

1. **Break syntax**: `{% break %}`.
2. **Continue syntax**: `{% continue %}`.
3. **Self-closing**: No end tag required for either.
4. **Loop context only**: Only meaningful inside `{% for %}` blocks.
5. **Immediate effect**: Both take effect at the point they are encountered.
6. **Typically conditional**: Usually placed inside `{% if %}` blocks within loops.

# Construction / Recognition

## To Construct/Create:
1. Place `{% break %}` or `{% continue %}` inside a `{% for %}` block.
2. Typically wrap in an `{% if %}` condition.

## To Identify/Recognize:
1. Look for `{% break %}` or `{% continue %}` inside for loops.

# Context & Application

- **Typical contexts**: Stopping iteration after finding a match, skipping draft posts, limiting output based on conditions.
- **Common applications**: Finding the first matching item, filtering items within a loop, implementing search-like behavior.

# Examples

**Example 1** (source: Liquid Standard Library): Breaking out of a loop after finding an item:
```liquid
{% for item in site.data.items %}
  {% if item.featured %}
    <div class="featured">{{ item.name }}</div>
    {% break %}
  {% endif %}
{% endfor %}
```

**Example 2** (source: Liquid Standard Library): Skipping draft items:
```liquid
{% for post in collections.posts %}
  {% if post.is_draft %}
    {% continue %}
  {% endif %}
  <li>{{ post.title }}</li>
{% endfor %}
```

# Relationships

## Builds Upon
- **[Logic Tags](/concept-cards/cobalt/logic-tags.md)** -- Uses `{% %}` syntax.
- **[For Block](/concept-cards/cobalt/for-block.md)** -- Only meaningful inside for loops.

## Enables
- Fine-grained loop control.

## Related
- **[Forloop Object](/concept-cards/cobalt/forloop-object.md)** -- Provides context about the current iteration.

## Contrasts With
- None directly.

# Common Errors

- **Error**: Using `{% break %}` or `{% continue %}` outside of a for loop.
  **Correction**: These tags only work inside `{% for %}` blocks.

# Common Confusions

- **Confusion**: Confusing `break` and `continue`.
  **Clarification**: `break` exits the entire loop. `continue` skips only the current iteration and moves to the next one.

# Source Reference

Liquid Standard Library, BreakTag and ContinueTag structs. Source: liquid_lib rustdoc (stdlib/tags/interrupt_tags/).

# Verification Notes

- Definition source: liquid_lib BreakTag and ContinueTag struct documentation
- Confidence rationale: Standard Liquid feature, well-documented.
- Uncertainties: None.
- Cross-reference status: Verified in liquid_lib stdlib.
