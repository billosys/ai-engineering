---
# === CORE IDENTIFICATION ===
concept: Immediately-Invoked Async Arrow Function
slug: immediately-invoked-async-arrow-function

# === CLASSIFICATION ===
category: class-patterns
subcategory: instantiation
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Techniques for instantiating classes"
chapter_number: 14
section: "14.2.1 Using an immediately-invoked asynchronous arrow function"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - IIAFE
  - immediately-invoked async function expression
  - async IIFE

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promises
  - async-await
  - promise-based-constructor
extends:
  - promise-based-constructor
related:
  - async-class-initialization
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a class with async initialization?"
---

# Quick Definition

An immediately-invoked async arrow function is an `async () => {}` expression that is defined and called in one step, enabling `await` syntax inside a constructor that returns a Promise.

# Core Definition

As shown in "Deep JavaScript" (Ch 14, Section 14.2.1): Instead of using the Promise API directly, you can use "an asynchronous arrow function that we invoke immediately" inside a constructor. The pattern `return (async () => { ...; return this; })()` produces the same Promise-based constructor behavior but with cleaner `async/await` syntax.

# Prerequisites

- **Promises** — The underlying mechanism.
- **async/await** — The syntax used inside the arrow function.
- **Promise-based constructor** — The pattern this is a variant of.

# Key Properties

1. Uses `async () => {}` syntax for cleaner code than raw Promise chains.
2. Must be **immediately invoked** with trailing `()`.
3. Returns a Promise that resolves to `this`.
4. Allows use of `await` inside the constructor body.

# Construction / Recognition

## To Construct/Create:
1. In the constructor, write `return (async () => { ... })();`.
2. Use `await` for async operations inside the arrow function.
3. End with `return this;`.

## To Identify/Recognize:
1. A constructor contains `(async () => { ... })()`.
2. The pattern returns a Promise wrapping `this`.

# Context & Application

This is a syntactic variant of the Promise-based constructor that trades the `.then()` chain for `async/await` syntax. It is useful when the async initialization logic is complex enough that `await` improves readability.

# Examples

**Example 1** (Ch 14): IIAFE in a constructor:
```js
constructor() {
  return (async () => {
    this.#data = await Promise.resolve('downloaded');
    return this;
  })();
}
```

# Relationships

## Builds Upon
- **Promise-based constructor** — This is a syntactic variant of that pattern.
- **async/await** — The syntax feature that makes this cleaner than raw Promises.

## Enables
- **Complex async initialization** — Multiple `await` steps can be chained cleanly.

## Related
- **IIFE (Immediately-Invoked Function Expression)** — The general pattern of defining and calling a function in one step.

## Contrasts With
- **Raw Promise chain in constructor** — The `.then()` equivalent achieves the same result with different syntax.

# Common Errors

- **Error**: Forgetting the outer parentheses and trailing `()`.
  **Correction**: The pattern requires `(async () => { ... })()` — the wrapping parens and the invocation parens are both essential.

- **Error**: Forgetting to `return` the IIAFE from the constructor.
  **Correction**: Without `return`, the constructor returns the default `this` (not the Promise), and callers get an uninitialized instance.

# Common Confusions

- **Confusion**: Thinking this makes the constructor itself async.
  **Clarification**: The constructor is still synchronous. It creates and returns a Promise produced by the immediately-invoked async function.

# Source Reference

Chapter 14: Techniques for instantiating classes, Section 14.2.1, lines 7130-7146.

# Verification Notes

- Definition source: direct (code example from source)
- Confidence rationale: Explicitly shown as a variant with clear code
- Cross-reference status: verified as variant of Section 14.2
