---
concept: Set Data Structure
slug: set-data-structure
category: collections
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Sets (Set)"
chapter_number: 38
pdf_page: null
section: "38.1 Basic Set operations"
extraction_confidence: high
aliases:
  - "Set"
  - "ES6 Set"
prerequisites:
  - iterable-interface
extends: []
related:
  - set-methods-overview
  - set-operations
  - set-element-equality
contrasts_with:
  - weakset-data-structure
answers_questions:
  - "How do `Map` and `Set` differ from plain objects and arrays as collections?"
---

# Quick Definition

A Set is an ES6 collection that manages a duplicate-free collection of values with fast membership checking, insertion-order iteration, and O(1) `.add()`, `.has()`, and `.delete()` operations.

# Core Definition

The data structure Set manages a duplicate-free collection of values and provides fast membership checks. Elements are compared via SameValueZero (like `===` but NaN equals NaN). Sets preserve insertion order and are iterable. They use `.size` (not `.length`) and support `.add()`, `.has()`, `.delete()`, `.clear()`.

# Prerequisites

- **iterable-interface** -- Sets accept iterables in constructor and are iterable

# Key Properties

1. Introduced in ES2015 (ES6)
2. No duplicate elements
3. O(1) membership checking via `.has()`
4. Preserves insertion order
5. `.size` property for element count
6. Elements compared via SameValueZero
7. Iterable -- works with for-of, spread, etc.

# Construction / Recognition

```js
const set = new Set(['red', 'green', 'blue']);
const set2 = new Set().add('red').add('green'); // chainable
```

# Context & Application

Use Sets when you need unique values, fast membership testing, or want to remove duplicates from arrays. Sets complement Maps: Maps store key-value pairs; Sets store unique values.

# Examples

```js
const set = new Set();
set.add('red');
assert.equal(set.has('red'), true);
assert.equal(set.delete('red'), true);
assert.equal(set.has('red'), false);

set.add('a').add('b');
assert.equal(set.size, 2);
set.clear();
assert.equal(set.size, 0);
```

(Chapter 38, Section 38.1, lines 82-158)

# Relationships

## Builds Upon
- **iterable-interface** -- constructor accepts iterables; Sets are iterable

## Enables
- **set-methods** -- CRUD operations
- **set-operations** -- union, intersection, difference (ES2025)
- Duplicate removal from arrays

## Related
- **set-element-equality** -- how elements are compared

## Contrasts With
- **weakset-data-structure** -- WeakSet has weak elements and no iteration

# Common Errors

- **Error**: Expecting Sets to deduplicate objects by value.
  **Correction**: Objects are compared by identity. Two `{}` are two different elements.

# Common Confusions

- **Confusion**: Sets are unordered.
  **Clarification**: Sets preserve insertion order, which helps with deterministic testing and ordered output.

# Source Reference

Chapter 38: Sets (Set), Section 38.1, lines 82-158.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined as chapter introduction
- Cross-reference status: verified
