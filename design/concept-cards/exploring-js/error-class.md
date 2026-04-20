---
concept: Error Class
slug: error-class
category: error-handling
subcategory: error-types
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Exception handling"
chapter_number: 26
pdf_page: null
section: "26.4 The superclass of all built-in exception classes: `Error`"
extraction_confidence: high
aliases:
  - "Error object"
  - "Error constructor"
prerequisites:
  - throw-statement
extends: []
related:
  - error-subclasses
  - error-chaining
  - stack-trace
contrasts_with: []
answers_questions:
  - "What is the base class for errors in JavaScript?"
---

# Quick Definition

`Error` is the superclass of all built-in exception classes, providing `message`, `stack`, and `cause` properties, and serving as the recommended type for thrown values.

# Core Definition

As described in "Exploring JavaScript" Ch. 26, the `Error` class constructor accepts a `message` string and an optional `options` object (ES2022) with a `cause` property. Instances have three key properties: `.message` (the error description), `.stack` (non-standard but widely supported stack trace string), and `.cause` (ES2022, the error that caused this one). Each built-in error class has a `name` property on its prototype.

# Prerequisites

- Throw statement

# Key Properties

1. Constructor: `new Error(message, options?)` where `options.cause` is supported since ES2022.
2. `.message` -- the error description string.
3. `.stack` -- non-standard but widely supported; shows the call stack at creation time.
4. `.cause` -- ES2022; links to the error that caused this one.
5. `.name` is a prototype property (returns `'Error'` for the base class).

# Construction / Recognition

```js
const err = new Error('Something failed');
console.log(err.message); // 'Something failed'
console.log(err.stack);   // stack trace string
```

# Context & Application

Use `Error` or its subclasses for all thrown exceptions to get stack traces and error chaining. Custom properties can be added to instances.

# Examples

From the source text (Ch. 26, section 26.4.2-26.4.3):

```js
const err = new Error('Hello!');
assert.equal(String(err), 'Error: Hello!');
assert.equal(err.message, 'Hello!');
```

# Relationships

## Enables
- **Error Subclasses** -- `TypeError`, `RangeError`, etc. extend `Error`
- **Error Chaining** -- `.cause` property links errors

## Related
- **Stack Trace** -- `.stack` property provides debugging information

# Common Errors

- **Error**: Omitting the `message` parameter.
  **Correction**: An empty string is used as default, but providing a descriptive message aids debugging.

# Common Confusions

- **Confusion**: Thinking `.stack` is standardized.
  **Clarification**: `.stack` is not part of the ECMAScript specification but is widely supported. Its format varies between engines.

# Source Reference

Chapter 26: Exception handling, Section 26.4, lines 340-458.

# Verification Notes

- Definition source: direct
- Confidence rationale: Detailed class definition with TypeScript-style signature
- Cross-reference status: verified
