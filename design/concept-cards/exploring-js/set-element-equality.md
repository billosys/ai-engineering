---
concept: Set Element Equality
slug: set-element-equality
category: collections
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Sets (Set)"
chapter_number: 38
pdf_page: null
section: "38.7.1 What Set elements are considered equal?"
extraction_confidence: high
aliases:
  - "Set SameValueZero"
prerequisites:
  - set-data-structure
extends: []
related:
  - map-key-equality
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

Set elements are compared using SameValueZero (like `===` but `NaN === NaN`), meaning `NaN` can be stored once in a Set, and different objects are always distinct elements.

# Core Definition

As with Map keys, Set elements are compared similarly to `===`, with the exception of `NaN` being equal to itself. Two different objects are never considered equal (identity comparison), and there is currently no way to customize this.

# Prerequisites

- **set-data-structure** -- governs element uniqueness

# Key Properties

1. SameValueZero algorithm (same as Maps)
2. NaN equals NaN (unlike ===)
3. Objects compared by identity
4. No customization available (yet)

# Construction / Recognition

```js
const set = new Set([NaN, NaN, NaN]);
set.size; // 1 -- NaN deduped

const set2 = new Set();
set2.add({});
set2.add({});
set2.size; // 2 -- different objects
```

# Context & Application

Understanding element equality prevents surprises when adding objects to Sets and when using NaN.

# Examples

```js
new Set([NaN, NaN]).size; // 1
new Set([NaN]).has(NaN);  // true

new Set().add({}).add({}).size; // 2
```

(Chapter 38, Section 38.7.1, lines 626-656)

# Relationships

## Builds Upon
- **set-data-structure** -- element equality

## Enables
- Predictable Set behavior

## Related
- **map-key-equality** -- same algorithm

## Contrasts With
- None

# Common Errors

- **Error**: Adding multiple object literals to a Set expecting deduplication.
  **Correction**: Each `{}` creates a new object with a new identity. They won't be deduplicated.

# Common Confusions

- **Confusion**: Sets use strict equality (`===`).
  **Clarification**: Almost, but `NaN === NaN` is `false` while Sets treat `NaN` as equal to itself.

# Source Reference

Chapter 38: Sets (Set), Section 38.7.1, lines 626-656.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly explained
- Cross-reference status: verified (same as Map key equality)
