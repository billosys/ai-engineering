---
concept: Awaiting Is Shallow
slug: awaiting-is-shallow
category: async-programming
subcategory: null
tier: advanced
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Async functions"
chapter_number: 44
pdf_page: null
section: "44.3.2 Awaiting is shallow"
extraction_confidence: high
aliases: []
prerequisites:
  - await-operator
  - async-function
extends: []
related:
  - async-map-pattern
contrasts_with: []
answers_questions:
  - "How do I use async/await to write asynchronous code?"
---

# Quick Definition

Awaiting is "shallow": `await` only pauses the immediately surrounding async function, not any outer function. It cannot be used inside nested non-async functions like regular callbacks.

# Core Definition

"Exploring JavaScript" Ch. 44: "If we are inside an async function and want to pause it via await, we must do so directly within that function; we can't use it inside a nested function, such as a callback. That is, pausing is shallow." Using `await` in a nested non-async function is a SyntaxError. Making the nested function async causes `await` to pause only that inner function.

# Prerequisites

- **Await operator** -- this is a constraint on `await` usage
- **Async function** -- `await` is scoped to the nearest async function

# Key Properties

1. `await` only pauses its immediately enclosing async function
2. `await` in a non-async nested function is a SyntaxError
3. Making nested function async means await pauses only that function
4. Affects patterns like `.map()` with async callbacks

# Construction / Recognition

```js
async function f() {
  const nestedFunc = async () => {
    const result = await Promise.resolve('abc'); // pauses nestedFunc, NOT f
    return 'RESULT: ' + result;
  };
  return [ await nestedFunc() ]; // need await here too
}
```

(Ch. 44, Section 44.3.2, lines 406-417)

# Context & Application

Critical for understanding why async callbacks in `.map()`, `.forEach()`, etc. don't behave as expected and why `Promise.all()` is needed with async `.map()` callbacks.

# Examples

`.map()` with async callback returns Array of Promises:
```js
const array = await Promise.all(
  arr.map(async (x) => { /* ... */ })
);
```

(Ch. 44, Section 44.3.3, lines 459-465)

# Relationships

## Builds Upon
- **Await operator** -- this is a fundamental constraint

## Related
- **Async map pattern** -- consequence of shallow awaiting

# Common Errors

- **Error**: Using `await` inside a `.forEach()` callback expecting sequential execution
  **Correction**: Use a `for...of` loop instead, or `Promise.all()` with `.map()`

# Common Confusions

- **Confusion**: `await` in a nested async callback pauses the outer function
  **Clarification**: It only pauses the nested function; the outer function continues

# Source Reference

Chapter 44: Async functions, Section 44.3.2, lines 380-441.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with detailed examples
- Cross-reference status: verified
