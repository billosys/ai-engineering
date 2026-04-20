---
concept: WeakSet Data Structure
slug: weakset-data-structure
category: collections
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "WeakSets (WeakSet) (advanced)"
chapter_number: 39
pdf_page: null
section: "39.1 How are WeakSets different from Sets?"
extraction_confidence: high
aliases:
  - "WeakSet"
prerequisites:
  - set-data-structure
  - weakmap-data-structure
extends: []
related:
  - weakset-use-cases
contrasts_with:
  - set-data-structure
answers_questions:
  - "How do `WeakMap`/`WeakSet` relate to `Map`/`Set` regarding garbage collection?"
---

# Quick Definition

A WeakSet holds objects (or non-registered symbols) without preventing their garbage collection, acting as a black box that only supports `.add()`, `.has()`, and `.delete()` -- no iteration, no `.size`, no `.clear()`.

# Core Definition

WeakSets are similar to Sets with key differences: they can hold objects without preventing garbage collection; they are black boxes (only `.add()`, `.has()`, `.delete()` are supported -- no iteration, no size, no clearing). The restrictions match those of WeakMaps for the same security and GC reasons.

# Prerequisites

- **set-data-structure** -- WeakSets are a constrained variant
- **weakmap-data-structure** -- shares black-box and weak semantics

# Key Properties

1. Introduced in ES2015 (ES6)
2. Elements must have identity semantics (objects, non-registered symbols)
3. Elements are weakly held -- garbage-collectable
4. No iteration, no `.size`, no `.clear()`
5. Only `.add()`, `.has()`, `.delete()`
6. Black box security property

# Construction / Recognition

```js
const ws = new WeakSet();
const obj = {};
ws.add(obj);
ws.has(obj); // true
// After obj is GC'd, it's automatically removed from ws
```

# Context & Application

WeakSets are primarily used for marking or tagging objects (e.g., tracking which objects have been processed, validating instance identity).

# Examples

```js
const isSaved = new WeakSet();
{
  const obj = {};
  isSaved.add(obj);
  assert.equal(isSaved.has(obj), true);
}
// obj can be garbage-collected
```

(Chapter 39, Section 39.1, lines 24-62)

# Relationships

## Builds Upon
- **set-data-structure** -- WeakSet is a constrained variant
- **weakmap-data-structure** -- shares weak/black-box semantics

## Enables
- **weakset-use-cases** -- marking objects

## Related
- **weakly-held-keys** -- same GC semantics

## Contrasts With
- **set-data-structure** -- Sets have strong elements and support iteration

# Common Errors

- **Error**: Trying to iterate over a WeakSet.
  **Correction**: WeakSets don't support iteration. Track elements separately if enumeration is needed.

# Common Confusions

- **Confusion**: WeakSets and Sets are interchangeable for small collections.
  **Clarification**: WeakSets lack iteration, size, and clearing. Use them only when weak references are needed.

# Source Reference

Chapter 39: WeakSets (WeakSet) (advanced), Section 39.1, lines 24-62.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined as chapter introduction
- Cross-reference status: verified
