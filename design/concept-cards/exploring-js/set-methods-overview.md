---
concept: Set Methods Overview
slug: set-methods-overview
category: collections
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Sets (Set)"
chapter_number: 38
pdf_page: null
section: "38.8 Quick reference: Set"
extraction_confidence: high
aliases:
  - "Set.prototype.add"
  - "Set.prototype.has"
  - "Set.prototype.delete"
  - "Set.prototype.clear"
prerequisites:
  - set-data-structure
extends: []
related:
  - set-operations
  - set-iteration
contrasts_with: []
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

Set provides `.add(value)` (chainable), `.has(value)`, `.delete(value)` (returns boolean), `.size` getter, `.clear()`, and iteration via `.values()`, `[Symbol.iterator]()`, `.forEach()`, `.keys()`, and `.entries()`.

# Core Definition

Set's API: `.add(value)` adds an element and returns `this` (chainable); `.has(value)` returns boolean; `.delete(value)` removes and returns true/false; `.size` is a getter for element count; `.clear()` removes all elements. Iteration: `.values()` and `[Symbol.iterator]()` iterate over elements; `.keys()` is an alias for `.values()`; `.entries()` yields `[value, value]` pairs (for Map symmetry). Verb methods mutate `this` (add, clear); noun methods return new data (values, union).

# Prerequisites

- **set-data-structure** -- the collection these methods operate on

# Key Properties

1. `.add()` is chainable (returns `this`)
2. `.delete()` returns boolean
3. `.size` is a getter (not a property)
4. `.keys()` === `.values()` (for Map symmetry)
5. `.entries()` yields `[v, v]` pairs
6. Verb methods mutate; noun methods return new data

# Construction / Recognition

```js
const set = new Set().add('a').add('b'); // chainable
set.has('a'); // true
set.delete('a'); // true
set.size; // 1
set.clear(); // empty
```

# Context & Application

These methods provide the complete CRUD interface for Sets, plus iteration support for processing all elements.

# Examples

```js
const set = new Set(['red']);
set.add('green').add('blue');
Array.from(set); // ['red', 'green', 'blue']
set.delete('red'); // true
set.has('red'); // false
```

(Chapter 38, Section 38.8, lines 673-872)

# Relationships

## Builds Upon
- **set-data-structure** -- methods of the Set

## Enables
- Complete CRUD for Set elements

## Related
- **set-operations** -- ES2025 combination methods
- **set-iteration** -- iteration methods

## Contrasts With
- None

# Common Errors

- **Error**: Using `.add()` like `.push()` expecting the new size.
  **Correction**: `.add()` returns `this` (for chaining), not the new size.

# Common Confusions

- **Confusion**: `.keys()` returns different values than `.values()` for Sets.
  **Clarification**: They return the same thing. `.keys()` exists only for symmetry with the Map API.

# Source Reference

Chapter 38: Sets (Set), Section 38.8, lines 673-872.

# Verification Notes

- Definition source: direct
- Confidence rationale: Complete API reference
- Cross-reference status: verified
