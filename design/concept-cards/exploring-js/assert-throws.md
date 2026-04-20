---
# === CORE IDENTIFICATION ===
concept: assert.throws()
slug: assert-throws

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
section: "11.4.3 Expecting exceptions: assert.throws()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - assertions
extends:
  - assertions
related:
  - assert-equal
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you test that code throws an exception?"
---

# Quick Definition

`assert.throws(callback)` verifies that its callback function throws an exception, optionally checking the exception's class, message pattern, or properties.

# Core Definition

"This function calls its first parameter, the function `callback`, and only succeeds if it throws an exception. Additional parameters can be used to specify what that exception must look like." (Ch. 11, &sect;11.4.3). Four overloads: callback only, callback + errorClass, callback + errorRegExp, callback + errorObject.

# Prerequisites

- **assertions** -- assert.throws is an assertion method

# Key Properties

1. Succeeds only if callback throws
2. Can match by error class: `assert.throws(fn, TypeError)`
3. Can match by regex: `assert.throws(fn, /pattern/)`
4. Can match by object properties: `assert.throws(fn, {name: 'TypeError', message: '...'})`

# Construction / Recognition

```js
assert.throws(
  () => { null.prop; },
  {
    name: 'TypeError',
    message: "Cannot read properties of null (reading 'prop')",
  }
);
```

# Context & Application

Used extensively in tests to verify error handling and that invalid operations produce expected exceptions.

# Examples

From the source text (Ch. 11, &sect;11.4.3):
```js
// Basic
assert.throws(() => { null.prop; });

// With class
assert.throws(() => { null.prop; }, TypeError);

// With regex
assert.throws(
  () => { null.prop; },
  /^TypeError: Cannot read properties of null/
);

// With object
assert.throws(
  () => { null.prop; },
  { name: 'TypeError', message: "Cannot read properties of null (reading 'prop')" }
);
```

# Relationships

## Builds Upon
- **assertions** -- a specific assertion method

## Enables
- Exception testing

## Related
- **assert-equal** -- another assertion method

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Passing a direct expression instead of a callback to `assert.throws()`.
  **Correction**: Wrap the throwing code in an arrow function: `() => { ... }`.

# Common Confusions

- **Confusion**: Thinking `assert.throws()` catches any exception.
  **Clarification**: When additional parameters are provided, the exception must match. Non-matching exceptions still cause test failure.

# Source Reference

Chapter 11: Assertion API, Section 11.4.3, lines 208-263.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: All four overloads documented with examples
- Cross-reference status: verified
