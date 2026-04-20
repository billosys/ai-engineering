---
# === CORE IDENTIFICATION ===
concept: assert.deepEqual()
slug: assert-deep-equal

# === CLASSIFICATION ===
category: tooling
subcategory: testing
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Assertion API"
chapter_number: 11
pdf_page: null
section: "11.4.2 Deep equality: assert.deepEqual()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - assert.notDeepEqual()
  - deep equality assertion
  - deep comparison

# === TYPED RELATIONSHIPS ===
prerequisites:
  - assertions
  - assert-equal
extends:
  - assertions
related:
  - objects-compared-by-identity
contrasts_with:
  - assert-equal

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you compare objects and arrays by content in JavaScript tests?"
---

# Quick Definition

`assert.deepEqual(actual, expected)` compares objects and arrays by their contents (recursively), unlike `assert.equal()` which compares by identity.

# Core Definition

"`deepEqual()` is a better choice for comparing objects" than `equal()` (Ch. 11, &sect;11.3). It recursively compares the contents of objects and arrays rather than their identities. Signature: `assert.deepEqual(actual, expected, message?)`. Complemented by `assert.notDeepEqual()`.

# Prerequisites

- **assertions** -- deepEqual is an assertion method
- **assert-equal** -- understanding why equal() is insufficient for objects

# Key Properties

1. Compares object/array contents recursively
2. Works for nested objects and arrays
3. Two different objects with same content are deeply equal
4. Complemented by `assert.notDeepEqual()`

# Construction / Recognition

```js
assert.deepEqual({foo: 1}, {foo: 1});  // passes!
assert.deepEqual(['a', 'b', 'c'], ['a', 'b', 'c']);  // passes!

// Compare with assert.equal():
assert.notEqual({foo: 1}, {foo: 1});  // passes (different identity)
```

# Context & Application

Use `assert.deepEqual()` whenever comparing objects, arrays, or any compound data structures in tests.

# Examples

From the source text (Ch. 11, &sect;11.3, 11.4.2):
```js
assert.deepEqual({foo: 1}, {foo: 1});
assert.deepEqual([1,2,3], [1,2,3]);
assert.deepEqual([], []);
assert.notDeepEqual([1,2,3], [1,2]);

// Contrast with equal:
assert.notEqual([], []);  // different identities
```

# Relationships

## Builds Upon
- **assertions** -- a specific assertion method
- **assert-equal** -- deepEqual addresses equal's limitations with objects

## Enables
- Testing compound data structure equality

## Related
- **objects-compared-by-identity** -- why deepEqual is needed

## Contrasts With
- **assert-equal** -- compares by identity, not content

# Common Errors

- **Error**: Using `assert.deepEqual()` for primitive comparisons where `assert.equal()` suffices.
  **Correction**: Use `assert.equal()` for primitives; `assert.deepEqual()` for objects/arrays.

# Common Confusions

- **Confusion**: Thinking `assert.deepEqual()` and `assert.equal()` work the same for primitives.
  **Clarification**: For primitives they behave the same; the difference only matters for objects.

# Source Reference

Chapter 11: Assertion API, Section 11.4.2, lines 182-206.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit with comparison to assert.equal
- Cross-reference status: verified
