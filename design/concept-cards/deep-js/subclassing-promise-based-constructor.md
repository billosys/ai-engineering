---
# === CORE IDENTIFICATION ===
concept: Subclassing a Promise-Based Constructor
slug: subclassing-promise-based-constructor

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
section: "14.4 Subclassing a Promise-based constructor (optional)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - promise-based-constructor
  - javascript-classes
  - javascript-private-fields
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

Subclassing a Promise-based constructor fails when the subclass declares private fields, because `this` in the subconstructor is the Promise returned by the superconstructor, not the actual instance.

# Core Definition

As explained in "Deep JavaScript" (Ch 14, Section 14.4): "A constructor always adds its private fields to its `this`. However, here, `this` in the subconstructor is the Promise returned by the superconstructor (and not the instance of `SubDataContainer` delivered via the Promise)." The subclass can hook into the returned Promise chain, but writing private fields to it produces a `TypeError`. The approach "still works if SubDataContainer does not have any private fields."

# Prerequisites

- **Promise-based constructor** — The pattern being subclassed.
- **JavaScript classes** — `extends`, `super()` mechanics.
- **JavaScript private fields** — Understanding of how `#field` declarations work.

# Key Properties

1. `super()` in a subclass of a Promise-based constructor returns a **Promise**, not the instance.
2. `this` in the subconstructor is that **Promise**.
3. Attempting to write **private fields** to the Promise throws a `TypeError`.
4. The pattern **works** if the subclass has **no private fields**.
5. This is a significant **limitation** of Promise-based constructors.

# Construction / Recognition

## To Construct/Create:
1. Define a superclass with a Promise-based constructor.
2. Define a subclass that extends it and calls `super()`.
3. Attempt to add `#privateField` in the subconstructor.
4. Observe the TypeError.

## To Identify/Recognize:
1. A subclass of a class with a Promise-based constructor.
2. The subclass declares private fields.
3. A `TypeError: Cannot write private member` error at runtime.

# Context & Application

This limitation is a key consideration when choosing between Promise-based constructors and static factory methods. If subclassing with private fields is needed, static factory methods are the better choice.

# Examples

**Example 1** (Ch 14): Failed subclassing:
```js
class DataContainer {
  #data;
  constructor() {
    return Promise.resolve('downloaded')
      .then(data => { this.#data = data; return this; });
  }
}

class SubDataContainer extends DataContainer {
  #moreData;
  constructor() {
    super();
    const promise = this;
    return promise.then(_this => {
      return Promise.resolve('more')
        .then(moreData => {
          _this.#moreData = moreData; // TypeError!
          return _this;
        });
    });
  }
}

assert.rejects(
  () => new SubDataContainer(),
  {
    name: 'TypeError',
    message: 'Cannot write private member #moreData ' +
      'to an object whose class did not declare it',
  }
);
```

# Relationships

## Builds Upon
- **Promise-based constructor** — The pattern this extends (and reveals a limitation of).

## Enables
- **Informed pattern selection** — Understanding this limitation helps choose between Promise-based constructors and static factory methods.

## Related
- **Async class initialization** — The broader topic.

## Contrasts With
- **Static factory method subclassing** — Factory methods don't have this limitation because the constructor is synchronous.

# Common Errors

- **Error**: Assuming Promise-based constructors can be freely subclassed.
  **Correction**: Subclasses with private fields will fail. Use static factory methods instead when subclassing is needed.

# Common Confusions

- **Confusion**: Thinking the TypeError is a bug in the subclass code.
  **Clarification**: It is a fundamental limitation: `this` in the subconstructor is the Promise, not the DataContainer instance, so private fields cannot be written to it.

# Source Reference

Chapter 14: Techniques for instantiating classes, Section 14.4, lines 7372-7441.

# Verification Notes

- Definition source: direct (from source explanation and error demonstration)
- Confidence rationale: Explicitly demonstrated with code and error output
- Cross-reference status: verified against Section 14.2 Promise-based constructor
