---
concept: Finally Clause
slug: finally-clause
category: error-handling
subcategory: exceptions
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Exception handling"
chapter_number: 26
pdf_page: null
section: "26.3.3 The `finally` clause"
extraction_confidence: high
aliases:
  - "finally"
  - "finally block"
prerequisites:
  - try-catch-finally
extends: []
related:
  - error-class
contrasts_with: []
answers_questions:
  - "How do I ensure cleanup code always runs?"
---

# Quick Definition

The `finally` clause of a `try` statement always executes when the `try` statement completes, regardless of whether an exception was thrown, a `return` was executed, or execution was normal.

# Core Definition

As described in "Exploring JavaScript" Ch. 26, the code inside the `finally` clause is always executed at the end of a `try` statement, no matter what happens in the `try` block or `catch` clause. This includes after `throw`, `return`, or `break`. The primary use case is resource cleanup.

# Prerequisites

- Try-catch-finally

# Key Properties

1. Always executes: after normal completion, after throw, after return, after break.
2. Primary use case: resource cleanup (closing files, connections, etc.).
3. Can be used with `try-finally` (no catch) for guaranteed cleanup.

# Construction / Recognition

```js
const resource = createResource();
try {
  // work with resource
} finally {
  resource.destroy(); // always runs
}
```

# Context & Application

Essential for resource management, ensuring cleanup code runs regardless of errors.

# Examples

From the source text (Ch. 26, section 26.3.3.1):

```js
let finallyWasExecuted = false;
function func() {
  try {
    return; // even with return...
  } finally {
    finallyWasExecuted = true; // ...finally runs
  }
}
func();
assert.equal(finallyWasExecuted, true);
```

# Relationships

## Builds Upon
- **Try-Catch-Finally** -- finally is a clause of the try statement

# Common Confusions

- **Confusion**: Thinking `finally` doesn't run after `return`.
  **Clarification**: `finally` ALWAYS runs, even after `return` or `throw`.

# Source Reference

Chapter 26: Exception handling, Section 26.3.3, lines 269-327.

# Verification Notes

- Definition source: direct
- Confidence rationale: Proven with multiple edge cases
- Cross-reference status: verified
