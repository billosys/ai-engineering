---
concept: Try-Catch-Finally
slug: try-catch-finally
category: error-handling
subcategory: exceptions
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Exception handling"
chapter_number: 26
pdf_page: null
section: "26.3 The `try` statement"
extraction_confidence: high
aliases:
  - "try statement"
  - "try-catch"
  - "exception handling"
prerequisites:
  - throw-statement
extends: []
related:
  - error-class
  - finally-clause
contrasts_with: []
answers_questions:
  - "How do I handle errors using try/catch/finally?"
---

# Quick Definition

The `try` statement executes code that might throw, catches exceptions in its `catch` clause, and optionally runs cleanup code in its `finally` clause that executes regardless of whether an exception occurred.

# Core Definition

As described in "Exploring JavaScript" Ch. 26, the maximal `try` statement has three parts: `try { ... } catch (error) { ... } finally { ... }`. The clauses can be combined as `try-catch`, `try-finally`, or `try-catch-finally`. The `catch` clause receives the thrown value as its parameter. Since ES2019, the catch binding can be omitted. The `finally` clause always executes, even after `return`, `break`, or `throw`.

# Prerequisites

- Throw statement

# Key Properties

1. Three clause combinations: `try-catch`, `try-finally`, `try-catch-finally`.
2. The catch parameter receives the thrown exception value.
3. Since ES2019, the catch binding can be omitted: `catch { ... }`.
4. The `finally` clause always executes -- even after `return` or `throw`.
5. `finally` is ideal for resource cleanup.

# Construction / Recognition

```js
try {
  // code that might throw
} catch (error) {
  // handle the error
} finally {
  // cleanup (always runs)
}
```

# Context & Application

Essential for handling runtime errors gracefully, managing resources (files, connections), and preventing application crashes from unexpected exceptions.

# Examples

From the source text (Ch. 26, section 26.3.2):

```js
const errorObject = new Error();
function func() {
  throw errorObject;
}
try {
  func();
} catch (err) {
  assert.equal(err, errorObject);
}
```

Resource cleanup pattern (Ch. 26, section 26.3.3):

```js
const resource = createResource();
try {
  // Work with resource. Errors may be thrown.
} finally {
  resource.destroy();
}
```

# Relationships

## Builds Upon
- **Throw Statement** -- catches values thrown by `throw`

## Enables
- **Error Chaining** -- catch and re-throw with additional context

## Related
- **Error Class** -- the type typically caught
- **Finally Clause** -- guaranteed cleanup

# Common Errors

- **Error**: Assuming `finally` does not run after a `return` statement.
  **Correction**: `finally` always runs, even when `return` or `throw` is executed inside `try` or `catch`.

- **Error**: Catching all exceptions without distinguishing error types.
  **Correction**: Check the type of the caught error (e.g., via `instanceof`) and re-throw unexpected ones.

# Common Confusions

- **Confusion**: Thinking `catch` is always required with `try`.
  **Clarification**: `try-finally` (without `catch`) is valid and useful for cleanup without error handling.

# Source Reference

Chapter 26: Exception handling, Section 26.3, lines 174-337.

# Verification Notes

- Definition source: direct
- Confidence rationale: Comprehensive coverage with all combinations shown
- Cross-reference status: verified
