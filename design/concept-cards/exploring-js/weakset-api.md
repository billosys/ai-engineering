---
concept: WeakSet API
slug: weakset-api
category: collections
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "WeakSets (WeakSet) (advanced)"
chapter_number: 39
pdf_page: null
section: "39.3 WeakSet API"
extraction_confidence: high
aliases:
  - "WeakSet methods"
prerequisites:
  - weakset-data-structure
extends: []
related:
  - set-methods-overview
contrasts_with:
  - set-methods-overview
answers_questions:
  - "How do `WeakMap`/`WeakSet` relate to `Map`/`Set` regarding garbage collection?"
---

# Quick Definition

WeakSet provides only three methods (`.add()`, `.has()`, `.delete()`) and a constructor -- no `.size`, `.clear()`, or iteration methods -- matching its black-box design.

# Core Definition

The WeakSet API consists of: constructor `new WeakSet(values?)`, `.add(value)` (returns `this`), `.has(value)`, and `.delete(value)`. No iteration, no size, no clearing. The methods work the same as their Set equivalents.

# Prerequisites

- **weakset-data-structure** -- the collection these methods operate on

# Key Properties

1. `new WeakSet(values?)` -- accepts iterable of values
2. `.add(value)` -- returns `this` (chainable)
3. `.has(value)` -- boolean
4. `.delete(value)` -- boolean
5. No other methods

# Construction / Recognition

```js
const ws = new WeakSet();
const obj = {};
ws.add(obj);
ws.has(obj);    // true
ws.delete(obj); // true
```

# Context & Application

The minimal API supports the primary use case: marking objects as having a boolean property.

# Examples

```js
const ws = new WeakSet([{}, {}]);
// Two entries, but no way to inspect or enumerate them
```

(Chapter 39, Section 39.3, lines 114-123)

# Relationships

## Builds Upon
- **weakset-data-structure** -- API for WeakSets

## Enables
- CRUD on WeakSet elements

## Related
- **set-methods-overview** -- WeakSet methods are a subset

## Contrasts With
- **set-methods-overview** -- Set has iteration, size, clear, and ES2025 operations

# Common Errors

- **Error**: Looking for `.size` on a WeakSet.
  **Correction**: WeakSets don't support `.size`. The element count is unknowable by design.

# Common Confusions

- **Confusion**: WeakSet has a `.clear()` method.
  **Clarification**: WeakSets don't support `.clear()`. Create a new WeakSet instead.

# Source Reference

Chapter 39: WeakSets (WeakSet) (advanced), Section 39.3, lines 114-123.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly listed
- Cross-reference status: verified
