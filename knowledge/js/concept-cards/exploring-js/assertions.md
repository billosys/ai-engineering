---
# === CORE IDENTIFICATION ===
concept: Assertions
slug: assertions

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
section: "11.1 Assertions in software development"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - assert
  - assertion checks

# === TYPED RELATIONSHIPS ===
prerequisites:
  - expressions
extends: []
related:
  - assert-equal
  - assert-deep-equal
  - assert-throws
  - unit-testing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are assertions and how are they used in JavaScript?"
---

# Quick Definition

Assertions are statements that verify expected facts about values, throwing exceptions if the expectations are not met. Node.js provides a built-in `assert` module.

# Core Definition

"In software development, *assertions* state facts about values or pieces of code that must be true. If they aren't, an exception is thrown." (Ch. 11, &sect;11.1). Node.js supports assertions via its built-in module `assert`. The book uses assertions both to document expected results in code examples and to implement test-driven exercises.

# Prerequisites

- **expressions** -- assertions compare expression results

# Key Properties

1. State facts that must be true; throw on failure
2. Node.js built-in: `import assert from 'node:assert/strict'`
3. Strict mode (`assert/strict`) recommended
4. Used for documenting results and test-driven development
5. Code examples become automatically testable via assertions

# Construction / Recognition

```js
import assert from 'node:assert/strict';
assert.equal(3 + 5, 8);
```

# Context & Application

Assertions serve dual purposes: documenting expected behavior in code examples and implementing unit tests.

# Examples

From the source text (Ch. 11, &sect;11.1):
```js
import assert from 'node:assert/strict';
assert.equal(3 + 5, 8);
```

# Relationships

## Builds Upon
- **expressions** -- assertions evaluate expressions

## Enables
- **assert-equal** -- specific assertion method
- **assert-deep-equal** -- deep comparison assertion
- **unit-testing** -- assertions power test frameworks

## Related
- No additional

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Forgetting to use the strict version of assert.
  **Correction**: Always import `'node:assert/strict'` for strict comparison behavior.

# Common Confusions

- **Confusion**: Thinking assertions are only for testing.
  **Clarification**: Assertions can also document expected behavior in code examples and serve as runtime checks.

# Source Reference

Chapter 11: Assertion API, Section 11.1, lines 35-53.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Explicit definition and usage description
- Cross-reference status: verified
