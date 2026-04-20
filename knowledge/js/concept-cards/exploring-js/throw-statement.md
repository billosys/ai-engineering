---
concept: Throw Statement
slug: throw-statement
category: error-handling
subcategory: exceptions
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Exception handling"
chapter_number: 26
pdf_page: null
section: "26.2 `throw`"
extraction_confidence: high
aliases:
  - "throw"
  - "throwing exceptions"
prerequisites: []
extends: []
related:
  - try-catch-finally
  - error-class
contrasts_with: []
answers_questions:
  - "How do I signal an error condition in JavaScript?"
---

# Quick Definition

The `throw` statement signals an error by throwing a value, which unwinds the call stack until caught by a `try-catch` or terminates the program.

# Core Definition

As described in "Exploring JavaScript" Ch. 26, the `throw` statement has the syntax `throw value`. Any value can be thrown, but it is best to use instances of `Error` or its subclasses because they support stack traces and error chaining. When thrown, execution exits nested constructs one by one until a `try` statement with a `catch` clause is found.

# Prerequisites

- Foundational concept with no prerequisites

# Key Properties

1. Any value can be thrown, but `Error` instances are recommended.
2. Thrown values unwind the call stack until caught by a `catch` clause.
3. Custom properties can be added to `Error` instances before throwing.

# Construction / Recognition

```js
throw new Error('Something went wrong');
```

# Context & Application

Used to signal errors that cannot be handled at the current level of the call stack, delegating error handling to a higher-level caller.

# Examples

From the source text (Ch. 26, section 26.2.1):

```js
const err = new Error('Could not find the file');
err.filePath = filePath;
throw err;
```

# Relationships

## Enables
- **Try-Catch-Finally** -- catches thrown values

## Related
- **Error Class** -- recommended type for thrown values

# Common Errors

- **Error**: Throwing a plain string instead of an `Error` instance.
  **Correction**: Use `new Error('message')` to get stack traces and error chaining support.

# Common Confusions

- **Confusion**: Thinking only `Error` objects can be thrown.
  **Clarification**: Any value can be thrown, but `Error` instances provide additional features.

# Source Reference

Chapter 26: Exception handling, Section 26.2, lines 122-172.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition and recommendation in source
- Cross-reference status: verified
