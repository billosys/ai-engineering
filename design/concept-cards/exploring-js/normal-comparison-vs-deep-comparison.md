---
# === CORE IDENTIFICATION ===
concept: Normal vs. Deep Comparison
slug: normal-comparison-vs-deep-comparison

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
section: "11.3 Normal comparison vs. deep comparison"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - shallow vs deep equality

# === TYPED RELATIONSHIPS ===
prerequisites:
  - assert-equal
  - assert-deep-equal
  - objects-compared-by-identity
extends: []
related:
  - primitives-compared-by-value
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes primitive values from objects?"
---

# Quick Definition

Normal comparison (`assert.equal`, using `===`) compares objects by identity; deep comparison (`assert.deepEqual`) recursively compares object contents. For primitives, both behave the same.

# Core Definition

"The strict `equal()` uses `===` to compare values. Therefore, an object is only equal to itself -- even if another object has the same content (because `===` does not compare the contents of objects, only their identities). `deepEqual()` is a better choice for comparing objects." (Ch. 11, &sect;11.3).

# Prerequisites

- **assert-equal** -- normal comparison method
- **assert-deep-equal** -- deep comparison method
- **objects-compared-by-identity** -- why normal comparison fails for objects

# Key Properties

1. Normal (`===`): compares identity for objects, value for primitives
2. Deep: recursively compares contents for objects
3. For primitives, both approaches give the same result
4. Deep comparison works for nested objects and arrays

# Construction / Recognition

```js
assert.notEqual({foo: 1}, {foo: 1});    // normal: different identities
assert.deepEqual({foo: 1}, {foo: 1});   // deep: same content

assert.notEqual(['a','b'], ['a','b']);   // normal: different identities
assert.deepEqual(['a','b'], ['a','b']); // deep: same content
```

# Context & Application

Choosing the right comparison is critical in tests. Use `equal` for primitives; `deepEqual` for objects and arrays.

# Examples

From the source text (Ch. 11, &sect;11.3):
```js
assert.notEqual({foo: 1}, {foo: 1});
assert.deepEqual({foo: 1}, {foo: 1});

assert.notEqual(['a', 'b', 'c'], ['a', 'b', 'c']);
assert.deepEqual(['a', 'b', 'c'], ['a', 'b', 'c']);
```

# Relationships

## Builds Upon
- **assert-equal** -- normal comparison
- **assert-deep-equal** -- deep comparison
- **objects-compared-by-identity** -- explains the difference

## Enables
- Correct testing of complex data structures

## Related
- **primitives-compared-by-value** -- both methods work the same for primitives

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Using `assert.equal()` for arrays/objects and being surprised when it fails.
  **Correction**: Use `assert.deepEqual()` for content comparison of compound values.

# Common Confusions

- **Confusion**: Thinking deep comparison is always needed.
  **Clarification**: For primitives, `assert.equal()` is sufficient and preferred for clarity.

# Source Reference

Chapter 11: Assertion API, Section 11.3, lines 109-134.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit comparison with examples for both cases
- Cross-reference status: verified
