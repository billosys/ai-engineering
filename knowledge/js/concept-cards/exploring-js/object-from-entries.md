---
concept: Object.fromEntries()
slug: object-from-entries
category: objects
subcategory: creation
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Objects"
chapter_number: 30
pdf_page: null
section: "30.9.10 Assembling objects via `Object.fromEntries()`"
extraction_confidence: high
aliases:
  - "Object.fromEntries"
prerequisites:
  - object-keys-values-entries
extends: []
related:
  - object-keys-values-entries
contrasts_with: []
answers_questions:
  - "How do I create an object from key-value pairs?"
---

# Quick Definition

`Object.fromEntries()` (ES2019) creates an object from an iterable of `[key, value]` pairs, serving as the inverse of `Object.entries()`.

# Core Definition

As described in "Exploring JavaScript" Ch. 30, `Object.fromEntries()` takes an iterable of `[key, value]` pairs and creates a new object from them. It is the inverse of `Object.entries()`. Introduced in ES2019.

# Prerequisites

- Object.keys/values/entries

# Key Properties

1. Introduced in ES2019.
2. Accepts any iterable of `[key, value]` pairs.
3. Inverse of `Object.entries()`.
4. Works with Map instances (which are iterables of entries).

# Construction / Recognition

```js
const entries = [['a', 1], ['b', 2]];
const obj = Object.fromEntries(entries);
// {a: 1, b: 2}
```

# Context & Application

Useful for transforming objects (filter, map via entries), converting Maps to objects, and building objects from dynamic key-value data.

# Examples

```js
const obj = {a: 1, b: 2, c: 3};
const filtered = Object.fromEntries(
  Object.entries(obj).filter(([k, v]) => v > 1)
);
// {b: 2, c: 3}
```

# Relationships

## Related
- **Object.keys/values/entries** -- `fromEntries()` is the inverse of `entries()`

# Source Reference

Chapter 30: Objects, Section 30.9.10.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit inverse relationship stated
- Cross-reference status: verified
