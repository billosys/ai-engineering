---
# === CORE IDENTIFICATION ===
concept: Promise-Based Constructor
slug: promise-based-constructor

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
section: "14.2 Solution: Promise-based constructor"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - constructor returning Promise
  - async constructor pattern

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
  - promises
  - async-property-initialization-problem
extends: []
related:
  - static-factory-method
  - immediately-invoked-async-arrow-function
contrasts_with:
  - static-factory-method
  - secret-token-pattern

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a class with async initialization?"
---

# Quick Definition

A Promise-based constructor returns a Promise (instead of the new instance) that resolves to the fully initialized instance once all asynchronous setup completes.

# Core Definition

As described in "Deep JavaScript" (Ch 14, Section 14.2): "By default, a constructor returns a new instance of the class that it is part of. We can override that if we explicitly return an object." By returning a Promise from the constructor that resolves to `this` after async initialization, callers receive the instance only when it is fully ready. The constructor uses `return Promise.resolve(...).then(() => { ...; return this; })`.

# Prerequisites

- **JavaScript classes** — Understanding that constructors can override their return value.
- **Promises** — The constructor returns a Promise chain.
- **Async property initialization problem** — The motivating problem this solves.

# Key Properties

1. The constructor **returns a Promise** instead of the instance directly.
2. Callers must use `.then()` or `await` to access the instance.
3. Only the **fully initialized instance** is accessible to callers.
4. Errors during async init become **Promise rejections**.
5. It may be **surprising** to callers that `new` returns a Promise, not an instance.

# Construction / Recognition

## To Construct/Create:
1. In the constructor, start the async operation.
2. Return a Promise that resolves to `this` after the async work completes.
3. Callers use `new MyClass().then(instance => ...)`.

## To Identify/Recognize:
1. A constructor contains an explicit `return` of a Promise.
2. The Promise chain ends with `return this`.
3. `new MyClass()` yields a thenable, not a plain instance.

# Context & Application

This pattern is one of the author's two recommended approaches (along with static factory method + secret token). It guarantees callers cannot access an incompletely initialized instance but has the drawback of surprising `new` semantics.

# Examples

**Example 1** (Ch 14): Promise-based constructor:
```js
class DataContainer {
  #data;
  constructor() {
    return Promise.resolve('downloaded')
      .then(data => {
        this.#data = data;
        return this;
      });
  }
  getData() {
    return 'DATA: '+this.#data;
  }
}
new DataContainer()
  .then(dc => assert.equal(
    dc.getData(), 'DATA: downloaded'));
```

# Relationships

## Builds Upon
- **Promises** — The mechanism for deferring instance delivery.
- **Constructor return override** — JavaScript allows constructors to return objects other than `this`.

## Enables
- **Subclassing promise-based constructor** — Subclasses can hook into the Promise chain (with limitations).

## Related
- **Immediately-invoked async arrow function** — A variant using `async/await` syntax inside the constructor.

## Contrasts With
- **Static factory method** — Keeps the constructor synchronous and simple; puts async logic in a separate method.

# Common Errors

- **Error**: Trying to use `instanceof` immediately on the result of `new DataContainer()`.
  **Correction**: The result of `new` is a Promise, not a DataContainer. Use `instanceof` on the resolved value.

- **Error**: Subclassing with private fields.
  **Correction**: When subclassing, `this` in the subconstructor is the Promise (not the instance), so private fields cannot be written. This approach fails if the subclass declares private fields.

# Common Confusions

- **Confusion**: Thinking this is the same as an `async` constructor.
  **Clarification**: JavaScript does not support `async` constructors. This pattern manually returns a Promise from a regular constructor.

# Source Reference

Chapter 14: Techniques for instantiating classes, Section 14.2, lines 7083-7147.

# Verification Notes

- Definition source: direct (from source explanation and code)
- Confidence rationale: Explicitly presented as a named solution with pros/cons
- Cross-reference status: verified against Section 14.4 (subclassing limitations)
