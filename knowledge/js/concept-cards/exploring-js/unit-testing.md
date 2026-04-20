---
# === CORE IDENTIFICATION ===
concept: Unit Testing with Mocha
slug: unit-testing

# === CLASSIFICATION ===
category: tooling
subcategory: testing
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Getting started with exercises"
chapter_number: 12
pdf_page: null
section: "12.2 Unit tests in JavaScript"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Mocha tests
  - test-driven exercises

# === TYPED RELATIONSHIPS ===
prerequisites:
  - assertions
  - assert-equal
extends: []
related:
  - assert-throws
  - assert-deep-equal
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are unit tests structured in JavaScript?"
---

# Quick Definition

Unit tests in JavaScript are structured using test frameworks like Mocha, with `suite()` grouping test files and `test()` defining individual test cases that use assertions to verify behavior.

# Core Definition

"All exercises in this book are tests that are run via the test framework Mocha." (Ch. 12, &sect;12.2). Test code consists of two parts: the code to be tested and the test file. Tests use `suite()` for titles, `test()` for individual cases, and `assert` methods for checks. Tests are run via `npm t path/to/test.mjs`.

# Prerequisites

- **assertions** -- tests use assertions for verification
- **assert-equal** -- primary assertion method in tests

# Key Properties

1. Framework: Mocha
2. Structure: `suite()` for grouping, `test()` for cases
3. Assertions via Node.js `assert` module in strict mode
4. Code to be tested must export its functions
5. Run via `npm test` or `npm t`
6. Supports async tests via Promises and async functions

# Construction / Recognition

```js
suite('id_test.mjs');
import * as assert from 'node:assert/strict';
import {id} from './id.mjs';

test('My test', () => {
  assert.equal(id('abc'), 'abc');
});
```

# Context & Application

Unit testing is the standard practice for verifying JavaScript code. Mocha is one of many test frameworks (others include Jest, Vitest).

# Examples

From the source text (Ch. 12, &sect;12.2.1):
```js
suite('id_test.mjs');
import * as assert from 'node:assert/strict';
import {id} from './id.mjs';

test('My test', () => {
  assert.equal(id('abc'), 'abc');
});
```

Run: `npm t demos/exercises/id_test.mjs`

Async test (Ch. 12, &sect;12.2.2):
```js
test('dividePromise 2', async () => {
  const result = await dividePromise(8, 4);
  assert.strictEqual(result, 2);
});
```

# Relationships

## Builds Upon
- **assertions** -- tests use assertions
- **assert-equal** -- primary assertion method

## Enables
- Test-driven development practices

## Related
- **assert-throws** -- testing exceptions
- **assert-deep-equal** -- testing compound values

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Forgetting to export functions from the module being tested.
  **Correction**: "Everything we want to test must be exported."

# Common Confusions

- **Confusion**: Thinking tests must be written from scratch for exercises.
  **Clarification**: The book provides tests; exercises require implementing the code to make tests pass.

# Source Reference

Chapter 12: Getting started with exercises, Section 12.2, lines 48-257.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Complete test structure documented
- Cross-reference status: verified
