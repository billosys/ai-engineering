---
# === CORE IDENTIFICATION ===
concept: Separate Factory Function
slug: separate-factory-function

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
section: "14.3.4 Variant: separate factory function"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - standalone factory function
  - external factory function

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
  - promises
  - secret-token-pattern
extends: []
related:
  - static-factory-method
contrasts_with:
  - static-factory-method

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a class with async initialization?"
---

# Quick Definition

A separate factory function is a standalone `async` function (not a class method) that creates and returns instances of a class, using a shared secret token to access the private constructor.

# Core Definition

As described in "Deep JavaScript" (Ch 14, Section 14.3.4): "Instead of using a static method as a factory you can also use a separate stand-alone function." The factory function and the class share a module-scoped secret token. The function is `async`, performs the data fetching, and returns `new DataContainer(secretToken, data)`.

# Prerequisites

- **JavaScript classes** — Constructor mechanics.
- **Promises** — The factory is async.
- **Secret token pattern** — Used to guard the constructor.

# Key Properties

1. The factory is a **standalone function**, not a class method.
2. Shares a **module-scoped secret token** with the class.
3. **Cannot access private members** of the class (unlike static methods).
4. The author **prefers static methods** over standalone functions for this use case.

# Construction / Recognition

## To Construct/Create:
1. Define the class and a secret token Symbol in the same module.
2. Define an `async function createMyClass()` in the same module.
3. The function calls `new MyClass(secretToken, data)`.
4. Export both the class and the factory function (but not the token).

## To Identify/Recognize:
1. A free-standing async function that calls `new` on a class.
2. The function and class share a module-scoped token.
3. The function is not a method on the class.

# Context & Application

This variant is "occasionally useful" but the author prefers static methods because they can access private members and the API reads more naturally (`DataContainer.create()` vs `createDataContainer()`).

# Examples

**Example 1** (Ch 14): Separate factory function:
```js
const secretToken = Symbol('secretToken');
class DataContainer {
  #data;
  constructor(token, data) {
    if (token !== secretToken) {
      throw new Error('Constructor is private');
    }
    this.#data = data;
  }
  getData() {
    return 'DATA: '+this.#data;
  }
}

async function createDataContainer() {
  const data = await Promise.resolve('downloaded');
  return new DataContainer(secretToken, data);
}

createDataContainer()
  .then(dc => assert.equal(
    dc.getData(), 'DATA: downloaded'));
```

# Relationships

## Builds Upon
- **Secret token pattern** — Provides the constructor guard.
- **Module scope** — The token is shared between function and class within the module.

## Enables
- **Decoupled factory logic** — The factory can live in a different part of the module from the class.

## Related
- **Static factory method** — The class-method equivalent.

## Contrasts With
- **Static factory method** — A static method can access private members; a standalone function cannot.

# Common Errors

- **Error**: Trying to access `#data` from the factory function.
  **Correction**: Private fields are only accessible from within the class body. The standalone function must use the public constructor interface.

# Common Confusions

- **Confusion**: Thinking standalone factories and static factory methods are equivalent.
  **Clarification**: Static methods have access to private class members; standalone functions do not. The author prefers `DataContainer.create()` over `createDataContainer()`.

# Source Reference

Chapter 14: Techniques for instantiating classes, Section 14.3.4, lines 7331-7369.

# Verification Notes

- Definition source: direct (from source explanation and code)
- Confidence rationale: Explicitly presented with clear comparison to static methods
- Cross-reference status: verified against Section 14.3 static factory methods
