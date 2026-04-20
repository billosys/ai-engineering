---
concept: Callback Function
slug: callback-function
category: functions
subcategory: parameters
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Callable values"
chapter_number: 27
pdf_page: null
section: "27.6.2 Terminology: callback"
extraction_confidence: high
aliases:
  - "callback"
prerequisites:
  - arrow-function
extends: []
related:
  - ordinary-function
contrasts_with: []
answers_questions:
  - "What is a callback function in JavaScript?"
---

# Quick Definition

A callback is a function passed as an argument to another function or method call, to be invoked later.

# Core Definition

As described in "Exploring JavaScript" Ch. 27, a callback or callback function is a function that is an argument of a function or method call. Callbacks are fundamental to JavaScript's patterns for iteration, event handling, and asynchronous programming.

# Prerequisites

- Arrow function (preferred for inline callbacks)

# Key Properties

1. A function passed as an argument to another function.
2. Arrow functions are the preferred syntax for inline callbacks.
3. Used extensively in array methods (`.map()`, `.filter()`, `.forEach()`), event handlers, and async operations.

# Construction / Recognition

```js
const myArray = ['a', 'b'];
const callback = (x) => console.log(x);
myArray.forEach(callback);
```

# Context & Application

Callbacks are ubiquitous in JavaScript: array iteration methods, event listeners, timers, and Promise handlers all accept callbacks.

# Examples

From the source text (Ch. 27, section 27.6.2):

```js
const myArray = ['a', 'b'];
const callback = (x) => console.log(x);
myArray.forEach(callback);
// Output: a, b
```

# Relationships

## Related
- **Arrow Function** -- preferred for inline callbacks due to concise syntax and lexical `this`

# Common Errors

- **Error**: Using an ordinary function as a callback inside a method, causing `this` to be `undefined`.
  **Correction**: Use an arrow function to preserve the enclosing `this`.

# Source Reference

Chapter 27: Callable values, Section 27.6.2, lines 1151-1171.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit terminology definition
- Cross-reference status: verified
