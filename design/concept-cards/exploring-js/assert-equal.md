---
# === CORE IDENTIFICATION ===
concept: assert.equal()
slug: assert-equal

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
section: "11.4.1 Normal equality: assert.equal()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - assert.notEqual()
  - normal equality assertion

# === TYPED RELATIONSHIPS ===
prerequisites:
  - assertions
extends:
  - assertions
related:
  - assert-deep-equal
  - strict-equality
contrasts_with:
  - assert-deep-equal

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you check if two values are equal in JavaScript tests?"
---

# Quick Definition

`assert.equal(actual, expected)` checks that `actual === expected` using strict equality, throwing an `AssertionError` if they differ. It compares by identity for objects.

# Core Definition

"The strict `equal()` uses `===` to compare values. Therefore, an object is only equal to itself -- even if another object has the same content (because `===` does not compare the contents of objects, only their identities)." (Ch. 11, &sect;11.3). Signature: `assert.equal(actual, expected, message?)`. Complemented by `assert.notEqual()`.

# Prerequisites

- **assertions** -- assert.equal is an assertion method

# Key Properties

1. Uses strict equality (`===`)
2. Throws `AssertionError` on failure
3. Objects compared by identity (not content)
4. Optional `message` parameter for error description
5. Complemented by `assert.notEqual()`

# Construction / Recognition

```js
assert.equal(3+3, 6);
assert.notEqual(3+3, 22);

// Objects: only equal to themselves
assert.notEqual({foo: 1}, {foo: 1}); // different objects!
```

# Context & Application

Use `assert.equal()` for primitive comparisons. For object/array content comparison, use `assert.deepEqual()`.

# Examples

From the source text (Ch. 11, &sect;11.4.1):
```js
assert.equal(3+3, 6);
assert.notEqual(3+3, 22);
```

With message:
```js
const x = 3;
assert.equal(x, 8, 'x must be 8');
// AssertionError [ERR_ASSERTION]: x must be 8
```

# Relationships

## Builds Upon
- **assertions** -- a specific assertion method

## Enables
- Testing primitive value equality

## Related
- **strict-equality** -- the underlying comparison mechanism

## Contrasts With
- **assert-deep-equal** -- compares object contents, not identity

# Common Errors

- **Error**: Using `assert.equal()` to compare objects or arrays.
  **Correction**: Use `assert.deepEqual()` for content comparison: `assert.notEqual({}, {})` is true.

# Common Confusions

- **Confusion**: Expecting `assert.equal([1,2], [1,2])` to pass.
  **Clarification**: Arrays are objects; `assert.equal()` compares identity. Use `assert.deepEqual()` instead.

# Source Reference

Chapter 11: Assertion API, Section 11.4.1, lines 143-179.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Full API documented with examples
- Cross-reference status: verified
