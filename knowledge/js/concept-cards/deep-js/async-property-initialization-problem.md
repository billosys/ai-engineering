---
# === CORE IDENTIFICATION ===
concept: Async Property Initialization Problem
slug: async-property-initialization-problem

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
section: "14.1 The problem: initializing a property asynchronously"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - asynchronous constructor initialization
  - async init problem

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
  - promises
extends: []
related:
  - promise-based-constructor
  - static-factory-method
  - async-class-initialization
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a class with async initialization?"
  - "Why can't I use await directly in a constructor?"
---

# Quick Definition

The async property initialization problem arises when a class constructor needs to set a property whose value is only available asynchronously, resulting in an incompletely initialized instance.

# Core Definition

As presented in "Deep JavaScript" (Ch 14, Section 14.1): When a constructor uses a Promise to initialize a property, the property is initially `undefined` because the Promise settles asynchronously. The instance is not completely initialized when first seen by the caller. This is the motivating problem for all the instantiation techniques explored in Chapter 14.

# Prerequisites

- **JavaScript classes** — Understanding of ES6 class syntax and constructors.
- **Promises** — Understanding of asynchronous operations and Promise-based APIs.

# Key Properties

1. Constructors in JavaScript are **synchronous** — they cannot use `await` directly.
2. Asynchronous operations inside a constructor settle **after** the constructor returns.
3. The instance is returned in an **incomplete state**, with the async property set to `undefined`.
4. Callers have no way to know **when** initialization completes.

# Construction / Recognition

## To Construct/Create:
1. Define a class with a constructor that starts an asynchronous operation.
2. Attempt to use the result of that async operation to set a property.
3. The property will be `undefined` when the constructor returns.

## To Identify/Recognize:
1. A constructor contains a Promise or async call.
2. A property is assigned inside a `.then()` callback or after an `await` that isn't directly accessible.
3. Instance properties are `undefined` when first accessed after `new`.

# Context & Application

This problem arises whenever class instances need data from external sources (network requests, file reads, database queries) during construction. It is the fundamental motivation for the various instantiation patterns presented in Chapter 14.

# Examples

**Example 1** (Ch 14): A broken async constructor:
```js
class DataContainer {
  #data;
  constructor() {
    Promise.resolve('downloaded')
      .then(data => this.#data = data);
  }
  getData() {
    return 'DATA: '+this.#data;
  }
}

const dc = new DataContainer();
assert.equal(dc.getData(), 'DATA: undefined');
setTimeout(() => assert.equal(
  dc.getData(), 'DATA: downloaded'), 0);
```

# Relationships

## Builds Upon
- **Promises** — The async operation that causes the problem.
- **JavaScript classes** — The constructor mechanism that constrains the solution.

## Enables
- **Promise-based constructor** — One solution to this problem.
- **Static factory method** — Another solution to this problem.
- **Async class initialization** — The general category of solutions.

## Related
- **Secret token pattern** — A way to enforce correct initialization.

## Contrasts With
- **Synchronous construction** — Normal constructors that complete all initialization before returning.

# Common Errors

- **Error**: Assuming the instance is fully initialized immediately after `new`.
  **Correction**: When a constructor contains async operations, properties may not be set yet. Use one of the patterns from Chapter 14 to guarantee complete initialization.

# Common Confusions

- **Confusion**: Thinking `async constructor()` is valid JavaScript syntax.
  **Clarification**: Constructors cannot be declared `async`. An `async` constructor would return a Promise rather than the instance, which conflicts with `new` semantics.

# Source Reference

Chapter 14: Techniques for instantiating classes, Section 14.1, lines 7007-7081.

# Verification Notes

- Definition source: direct (from source example and explanation)
- Confidence rationale: Explicitly described problem with complete code example
- Cross-reference status: verified against Chapter 14 solutions
