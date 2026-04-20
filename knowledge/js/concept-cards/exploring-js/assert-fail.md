---
# === CORE IDENTIFICATION ===
concept: assert.fail()
slug: assert-fail

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
section: "11.4.4 Always fail: assert.fail()"

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
  - assert-throws
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you mark unreachable code in tests?"
---

# Quick Definition

`assert.fail()` unconditionally throws an `AssertionError`, useful in tests to mark code paths that should never be reached.

# Core Definition

"By default, it throws an `AssertionError` when it is called. That is occasionally useful for unit testing." (Ch. 11, &sect;11.4.4). `messageOrError` can be a string (overrides error message) or an `Error` instance (throws that instead).

# Prerequisites

- **assertions** -- assert.fail is an assertion method

# Key Properties

1. Always throws when called
2. Optional parameter: string message or Error instance
3. Used to mark unreachable code paths in tests

# Construction / Recognition

```js
try {
  functionThatShouldThrow();
  assert.fail(); // should not reach here
} catch (_) {
  // Success
}
```

# Context & Application

Used in tests where code should throw but you want to verify the exception path.

# Examples

From the source text (Ch. 11, &sect;11.4.4):
```js
try {
  functionThatShouldThrow();
  assert.fail();
} catch (_) {
  // Success
}
```

# Relationships

## Builds Upon
- **assertions** -- a specific assertion method

## Enables
- Marking unreachable test paths

## Related
- **assert-throws** -- alternative for testing exceptions

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Using `assert.fail()` when `assert.throws()` would be cleaner.
  **Correction**: Prefer `assert.throws()` for testing that code throws exceptions.

# Common Confusions

- **Confusion**: Thinking assert.fail() is commonly needed.
  **Clarification**: It's for edge cases; `assert.throws()` handles most exception testing.

# Source Reference

Chapter 11: Assertion API, Section 11.4.4, lines 265-284.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit with use case example
- Cross-reference status: verified
