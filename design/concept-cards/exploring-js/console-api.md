---
# === CORE IDENTIFICATION ===
concept: Console API
slug: console-api

# === CLASSIFICATION ===
category: tooling
subcategory: development-tools
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Consoles: interactive JavaScript command lines"
chapter_number: 10
pdf_page: null
section: "10.2 The console.* API: printing data and more"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - console.log
  - console.error

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-platforms
extends: []
related:
  - browser-console
  - nodejs-repl
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you print output in JavaScript?"
---

# Quick Definition

The `console.*` API provides methods for printing data in JavaScript: `console.log()` prints to standard output (stdout), and `console.error()` prints to standard error (stderr).

# Core Definition

"The full `console.*` API is documented on MDN web docs and on the Node.js website. It is not part of the JavaScript language standard, but much functionality is supported by both browsers and Node.js." (Ch. 10, &sect;10.2). The two primary methods: `console.log()` prints values to stdout with two variants (multiple values or string substitution), and `console.error()` prints to stderr. `JSON.stringify()` can be used for pretty-printing nested objects.

# Prerequisites

- **javascript-platforms** -- console API works on both platforms

# Key Properties

1. Not part of the JavaScript standard (but universally supported)
2. `console.log()`: prints to stdout
3. `console.error()`: prints to stderr
4. String substitution: `%s` (string), `%o` (object), `%j` (JSON), `%%` (literal %)
5. `console.log()` with zero arguments prints a newline
6. `JSON.stringify(obj, null, 2)` for pretty-printing nested objects

# Construction / Recognition

```js
console.log('abc', 123, true);  // abc 123 true
console.error('Something went wrong!');
console.log('Test: %s %j', 123, 'abc');  // Test: 123 "abc"
console.log(JSON.stringify({first: 'Jane'}, null, 2));
```

# Context & Application

`console.log()` is the most common debugging tool in JavaScript. Use `console.error()` for error messages that should go to stderr.

# Examples

From the source text (Ch. 10, &sect;10.2):
```js
console.log('abc', 123, true);
// Output: abc 123 true

console.log('Test: %s %j', 123, 'abc');
// Output: Test: 123 "abc"

console.log(JSON.stringify({first: 'Jane', last: 'Doe'}, null, 2));
// Output:
// {
//   "first": "Jane",
//   "last": "Doe"
// }
```

# Relationships

## Builds Upon
- **javascript-platforms** -- available on all platforms

## Enables
- Debugging and output in JavaScript programs

## Related
- **browser-console** -- where console output appears in browsers
- **nodejs-repl** -- where console output appears in Node.js

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Using `console.log()` for error messages.
  **Correction**: Use `console.error()` for errors; it goes to stderr.

# Common Confusions

- **Confusion**: Thinking the console API is part of the JavaScript language standard.
  **Clarification**: It's a platform API supported by browsers and Node.js but not formally part of ECMAScript.

# Source Reference

Chapter 10: Consoles, Section 10.2, lines 122-272.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Detailed with multiple examples and substitution directives
- Cross-reference status: verified
