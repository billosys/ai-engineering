---
# === CORE IDENTIFICATION ===
concept: Prototype Borrowing Factory
slug: prototype-borrowing-factory

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
section: "14.3.2 Improvement: constructor throws, factory method borrows the class prototype"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Object.create() factory pattern"
  - throwing constructor pattern

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
  - static-factory-method
  - javascript-prototypes
extends:
  - static-factory-method
related:
  - private-constructor-pattern
  - secret-token-pattern
contrasts_with:
  - secret-token-pattern
  - inactive-by-default-pattern

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a class with async initialization?"
---

# Quick Definition

The prototype borrowing factory disables a class constructor by making it always throw, then creates instances via `Object.create(MyClass.prototype)` followed by an `_init()` method call.

# Core Definition

As described in "Deep JavaScript" (Ch 14, Section 14.3.2): This variant "disables the constructor of DataContainer and uses a trick to create instances of it another way." The factory method uses `Object.create(this.prototype)._init(data)` to create an object with the correct prototype chain without invoking the constructor. "Internally, an instance of DataContainer is any object whose prototype is DataContainer.prototype."

# Prerequisites

- **JavaScript classes** — Constructor and prototype chain understanding.
- **Static factory method** — The pattern this is a variant of.
- **JavaScript prototypes** — `Object.create()` and prototype chain mechanics.

# Key Properties

1. The constructor **always throws**, preventing any direct use.
2. `Object.create(this.prototype)` creates an object with the right prototype chain.
3. `instanceof` checks **still work** because they check the prototype chain.
4. **Cannot use private fields** — private fields are only set up by the actual constructor.
5. The `_init()` method must be public (not private), reducing encapsulation.

# Construction / Recognition

## To Construct/Create:
1. Make the constructor throw unconditionally.
2. Define an `_init(data)` method that sets properties and returns `this`.
3. In the static factory: `Object.create(this.prototype)._init(data)`.

## To Identify/Recognize:
1. A constructor that always throws.
2. An `_init()` or similar setup method.
3. `Object.create(ClassName.prototype)` in the factory method.

# Context & Application

This approach is described as "elegant" with the benefit that `instanceof` works correctly. However, its inability to use private fields is a significant limitation. The author presents it as one of several options but does not recommend it as the primary choice.

# Examples

**Example 1** (Ch 14): Prototype borrowing factory:
```js
class DataContainer {
  static async create() {
    const data = await Promise.resolve('downloaded');
    return Object.create(this.prototype)._init(data);
  }
  constructor() {
    throw new Error('Constructor is private');
  }
  _init(data) {
    this._data = data;
    return this;
  }
  getData() {
    return 'DATA: '+this._data;
  }
}
DataContainer.create()
  .then(dc => {
    assert.equal(dc instanceof DataContainer, true);
    assert.equal(dc.getData(), 'DATA: downloaded');
  });
```

# Relationships

## Builds Upon
- **Object.create()** — Creates objects with a specified prototype.
- **Prototype chain** — `instanceof` checks rely on the prototype chain, not the constructor.

## Enables
- **Constructor-free instantiation** — Shows that instances are defined by their prototype, not how they were constructed.

## Related
- **Private constructor pattern** — The general category this belongs to.

## Contrasts With
- **Secret token pattern** — Allows the constructor to run (with the right token), so private fields work.
- **Inactive-by-default pattern** — Also runs the constructor, supporting private fields.

# Common Errors

- **Error**: Using private fields (`#field`) with this pattern.
  **Correction**: Private fields "are only set up correctly for instances that were created via the constructor." Use public properties or the secret token pattern instead.

# Common Confusions

- **Confusion**: Thinking `Object.create()` calls the constructor.
  **Clarification**: `Object.create()` only sets up the prototype chain. It does not invoke the constructor at all.

# Source Reference

Chapter 14: Techniques for instantiating classes, Section 14.3.2, lines 7234-7283.

# Verification Notes

- Definition source: direct (from source explanation and code)
- Confidence rationale: Explicitly presented pattern with detailed pros/cons
- Cross-reference status: verified against private field limitations noted in source
