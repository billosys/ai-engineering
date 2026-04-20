---
concept: Error Subclasses
slug: error-subclasses
category: error-handling
subcategory: error-types
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Exception handling"
chapter_number: 26
pdf_page: null
section: "26.6 Subclasses of `Error`"
extraction_confidence: high
aliases:
  - "built-in error types"
  - "TypeError"
  - "RangeError"
  - "SyntaxError"
  - "ReferenceError"
prerequisites:
  - error-class
extends:
  - error-class
related:
  - subclassing
contrasts_with: []
answers_questions:
  - "What built-in error types does JavaScript provide?"
  - "How do I create custom error classes?"
---

# Quick Definition

JavaScript provides built-in `Error` subclasses (`TypeError`, `RangeError`, `SyntaxError`, `ReferenceError`, `URIError`, `AggregateError`) for common error categories, and developers can create custom subclasses.

# Core Definition

As described in "Exploring JavaScript" Ch. 26, `Error` has several built-in subclasses: `RangeError` (value not in allowable range), `ReferenceError` (invalid reference), `SyntaxError` (parsing error), `TypeError` (unsuccessful operation), `URIError` (invalid URI usage), and `AggregateError` (ES2021, multiple errors). Custom subclasses can extend `Error`, calling `super(message, options)` in the constructor.

# Prerequisites

- Error class

# Key Properties

1. `TypeError` -- most commonly used; indicates type-related failures.
2. `RangeError` -- value outside allowable range.
3. `ReferenceError` -- accessing an undeclared variable.
4. `SyntaxError` -- invalid code syntax.
5. `AggregateError` (ES2021) -- wraps multiple errors (used by `Promise.any()`).
6. Custom subclasses: `class MyError extends Error {}`.

# Construction / Recognition

```js
// Built-in
throw new TypeError('Expected a string');
throw new RangeError('Index out of bounds');

// Custom
class MyCustomError extends Error {
  constructor(message, options) {
    super(message, options);
  }
}
```

# Context & Application

Use specific error subclasses to communicate the nature of failures. Custom subclasses allow `instanceof` checks in catch clauses for fine-grained error handling.

# Examples

From the source text (Ch. 26, section 26.6.2):

```js
class MyCustomError extends Error {
  constructor(message, options) {
    super(message, options);
  }
}
```

# Relationships

## Builds Upon
- **Error Class** -- all subclasses extend `Error`

## Related
- **Subclassing** -- uses `extends` keyword (Ch. 31)

# Common Errors

- **Error**: Not calling `super(message, options)` in a custom error constructor.
  **Correction**: Always call `super()` to properly initialize `message`, `stack`, and `cause`.

# Common Confusions

- **Confusion**: When to use `TypeError` vs. `RangeError`.
  **Clarification**: `TypeError` is for wrong types or unsuccessful operations; `RangeError` is for values outside a set or range of allowable values.

# Source Reference

Chapter 26: Exception handling, Section 26.6, lines 581-618.

# Verification Notes

- Definition source: direct
- Confidence rationale: Enumerated directly from ECMAScript specification quotes
- Cross-reference status: verified
