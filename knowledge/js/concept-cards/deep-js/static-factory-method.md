---
# === CORE IDENTIFICATION ===
concept: Static Factory Method
slug: static-factory-method

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
section: "14.3 Solution: static factory method"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - factory method
  - ".create() pattern"
  - ".from() pattern"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
  - promises
  - async-property-initialization-problem
extends: []
related:
  - secret-token-pattern
  - static-from-factory
  - separate-factory-function
contrasts_with:
  - promise-based-constructor

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a class with async initialization?"
---

# Quick Definition

A static factory method is a `static async` class method that creates and returns fully initialized instances, keeping the constructor simple and synchronous.

# Core Definition

As defined in "Deep JavaScript" (Ch 14, Section 14.3): "A static factory method of a class C creates instances of C and is an alternative to using `new C()`." Common naming conventions include `.create()` (new instance), `.from()` (copy/convert from another object), and `.of()` (assemble from argument values). The method is `async`, performs all asynchronous work, then calls `new this(data)` with the result.

# Prerequisites

- **JavaScript classes** — Static methods and constructors.
- **Promises** — The factory method is `async` and returns a Promise.
- **Async property initialization problem** — The motivating problem.

# Key Properties

1. The constructor remains **synchronous and simple**.
2. All async logic lives in the **static method**.
3. Common names: `.create()`, `.from()`, `.of()`.
4. Returns a **Promise** that resolves to a fully initialized instance.
5. Disadvantage: the constructor is still **publicly callable**, allowing incorrectly initialized instances.

# Construction / Recognition

## To Construct/Create:
1. Define a synchronous constructor that accepts pre-fetched data.
2. Define a `static async` method that fetches data and calls `new this(data)`.
3. Callers use `await MyClass.create()` instead of `new MyClass()`.

## To Identify/Recognize:
1. A class has a `static` method that calls `new this(...)` or `new ClassName(...)`.
2. The static method handles async operations; the constructor does not.

# Context & Application

This is one of the author's two recommended approaches for async initialization (the other being Promise-based constructors). It produces cleaner separation of concerns but may need additional protection to prevent direct constructor use. Can be combined with the secret token pattern for safety.

# Examples

**Example 1** (Ch 14): Static factory method:
```js
class DataContainer {
  #data;
  static async create() {
    const data = await Promise.resolve('downloaded');
    return new this(data);
  }
  constructor(data) {
    this.#data = data;
  }
  getData() {
    return 'DATA: '+this.#data;
  }
}
DataContainer.create()
  .then(dc => assert.equal(
    dc.getData(), 'DATA: downloaded'));
```

# Relationships

## Builds Upon
- **JavaScript static methods** — The factory is a static class method.
- **Promises / async-await** — The factory method is async.

## Enables
- **Secret token pattern** — Combines with this to protect the constructor.
- **Private constructor pattern** — Various ways to restrict direct construction.

## Related
- **Static `.from()` factory** — A naming convention for copy-based factories.
- **Separate factory function** — A standalone function variant.

## Contrasts With
- **Promise-based constructor** — Puts async logic in the constructor itself rather than a separate method.

# Common Errors

- **Error**: Calling the constructor directly without the factory method, yielding an incomplete instance.
  **Correction**: Combine with the secret token pattern or another private constructor technique to enforce factory usage.

# Common Confusions

- **Confusion**: Thinking `.create()`, `.from()`, and `.of()` are interchangeable names.
  **Clarification**: Each name signals a different intent: `.create()` for new instances, `.from()` for conversion/copying, `.of()` for assembly from arguments.

# Source Reference

Chapter 14: Techniques for instantiating classes, Section 14.3, lines 7149-7192.

# Verification Notes

- Definition source: direct (quoted definition and code from source)
- Confidence rationale: Explicitly defined with naming conventions and pros/cons
- Cross-reference status: verified against related patterns in Sections 14.3.1-14.3.4
