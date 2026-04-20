---
# === CORE IDENTIFICATION ===
concept: Inactive-by-Default Pattern
slug: inactive-by-default-pattern

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
section: "14.3.3 Improvement: instances are inactive by default, activated by factory method"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - activation flag pattern
  - guarded instance pattern

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
  - static-factory-method
  - javascript-private-fields
extends:
  - static-factory-method
related:
  - private-constructor-pattern
  - secret-token-pattern
contrasts_with:
  - secret-token-pattern
  - prototype-borrowing-factory

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a class with async initialization?"
---

# Quick Definition

The inactive-by-default pattern creates instances in a disabled state (via a private `#active` flag), with only the factory method able to activate them through a private `#init()` method.

# Core Definition

As described in "Deep JavaScript" (Ch 14, Section 14.3.3): "By default, instances are switched off via the flag `.#active`. The initialization method `.#init()` that switches them on cannot be accessed externally, but `DataContainer.create()` can invoke it." Every public method must check the `#active` flag via a `#check()` helper before proceeding.

# Prerequisites

- **JavaScript classes** — Constructor and method mechanics.
- **Static factory method** — The factory that activates instances.
- **JavaScript private fields** — The `#active` flag and `#init()` method rely on private class features.

# Key Properties

1. Instances start with `#active = false`.
2. A private `#init()` method sets `#active = true` and initializes data.
3. Every public method must call `#check()` to verify activation.
4. The factory method calls `new this().#init(data)` — this works because the factory is inside the class.
5. **Verbose**: requires a check at the start of every method.

# Construction / Recognition

## To Construct/Create:
1. Declare `#active = false` as a private field.
2. Define a private `#init(data)` method that sets `#active = true`, initializes state, and returns `this`.
3. Define a private `#check()` method that throws if `!this.#active`.
4. Call `this.#check()` at the start of every public method.
5. The static factory calls `new this().#init(data)`.

## To Identify/Recognize:
1. A private boolean flag that gates method access.
2. A private initialization method separate from the constructor.
3. Guard checks at the beginning of public methods.

# Context & Application

This is the most verbose of the private constructor approaches. Its main advantage over the secret token is that the constructor takes no arguments, making it harder to misuse. Its major downside is the risk of forgetting to invoke `#check()` in a method.

# Examples

**Example 1** (Ch 14): Inactive-by-default pattern:
```js
class DataContainer {
  #data;
  static async create() {
    const data = await Promise.resolve('downloaded');
    return new this().#init(data);
  }

  #active = false;
  constructor() {}
  #init(data) {
    this.#active = true;
    this.#data = data;
    return this;
  }
  getData() {
    this.#check();
    return 'DATA: '+this.#data;
  }
  #check() {
    if (!this.#active) {
      throw new Error('Not created by factory');
    }
  }
}
```

# Relationships

## Builds Upon
- **Private fields** — Both `#active` and `#init()` rely on private class features.
- **Static factory method** — The factory is the only authorized activation path.

## Enables
- **Fail-fast uninitialized access** — Any method call on an unactivated instance throws immediately.

## Related
- **Private constructor pattern** — The general category.

## Contrasts With
- **Secret token pattern** — Simpler, checks once at construction rather than on every method call.
- **Prototype borrowing factory** — Avoids the constructor entirely rather than gating methods.

# Common Errors

- **Error**: Forgetting to call `this.#check()` in a new public method.
  **Correction**: Every public method must begin with `this.#check()`. Consider linting or code review to catch omissions.

# Common Confusions

- **Confusion**: Thinking the factory method can access `#init()` from outside the class.
  **Clarification**: The factory is a `static` method defined inside the class body, so it has access to private members via instances of the class.

# Source Reference

Chapter 14: Techniques for instantiating classes, Section 14.3.3, lines 7285-7329.

# Verification Notes

- Definition source: direct (from source explanation and code)
- Confidence rationale: Explicitly presented pattern with code and pros/cons
- Cross-reference status: verified against other Section 14.3 variants
