---
# === CORE IDENTIFICATION ===
concept: Secret Token Pattern
slug: secret-token-pattern

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
section: "14.3.1 Improvement: private constructor via secret token"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - private constructor via secret token
  - Symbol-based constructor guard

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
  - static-factory-method
  - javascript-symbols
extends:
  - static-factory-method
related:
  - private-constructor-pattern
  - prototype-borrowing-factory
  - inactive-by-default-pattern
contrasts_with:
  - prototype-borrowing-factory

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a class with async initialization?"
---

# Quick Definition

The secret token pattern uses a module-scoped Symbol to guard a constructor so that only an authorized factory method can create instances, effectively simulating a private constructor.

# Core Definition

As described in "Deep JavaScript" (Ch 14, Section 14.3.1): "If we want to ensure that instances are always correctly set up, we must ensure that only `DataContainer.create()` can invoke the constructor." A Symbol is created as a module-level constant. The constructor requires this Symbol as a parameter and throws if it is not provided. Since the Symbol is not exported, external code cannot call the constructor directly.

# Prerequisites

- **JavaScript classes** — Constructor mechanics.
- **Static factory method** — The pattern this improves upon.
- **JavaScript Symbols** — Used as unforgeable tokens since every Symbol is unique.

# Key Properties

1. A **module-scoped Symbol** serves as the secret token.
2. The constructor **checks** the first argument against the token.
3. The constructor **throws** if the token does not match.
4. Only the factory method (in the same module) has access to the token.
5. The class is exported, but the Symbol is **not exported**.

# Construction / Recognition

## To Construct/Create:
1. Create a Symbol: `const secretToken = Symbol('secretToken');`.
2. Constructor accepts a token parameter and throws if it doesn't match.
3. The static factory method passes the token when calling `new this(secretToken, data)`.
4. Export the class but not the Symbol.

## To Identify/Recognize:
1. A module-level Symbol that is not exported.
2. A constructor that checks its first argument against that Symbol.
3. A factory method that passes the Symbol to the constructor.

# Context & Application

This is the author's recommended approach when combining static factory methods with constructor protection. It is described as "safe and straightforward" though "slightly verbose." It is one of the two recommended solutions in the chapter conclusion.

# Examples

**Example 1** (Ch 14): Secret token pattern:
```js
const secretToken = Symbol('secretToken');
class DataContainer {
  #data;
  static async create() {
    const data = await Promise.resolve('downloaded');
    return new this(secretToken, data);
  }
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
DataContainer.create()
  .then(dc => assert.equal(
    dc.getData(), 'DATA: downloaded'));
```

# Relationships

## Builds Upon
- **Static factory method** — This pattern adds constructor protection to the factory method approach.
- **JavaScript Symbols** — The uniqueness guarantee of Symbols makes the token unforgeable.

## Enables
- **Safe async initialization** — Guarantees instances are always fully initialized.

## Related
- **Private constructor pattern** — The general concept; the secret token is one implementation.
- **Inactive-by-default pattern** — Another approach to the same goal.

## Contrasts With
- **Prototype borrowing factory** — An alternative that disables the constructor entirely and uses `Object.create()`.

# Common Errors

- **Error**: Accidentally exporting the secret token Symbol.
  **Correction**: Keep the Symbol as a module-level `const` that is never included in the module's exports.

# Common Confusions

- **Confusion**: Thinking a string could serve as the token.
  **Clarification**: Strings are not unique and could be guessed. Symbols are guaranteed unique, making them unforgeable from outside the module.

# Source Reference

Chapter 14: Techniques for instantiating classes, Section 14.3.1, lines 7194-7232.

# Verification Notes

- Definition source: direct (from source explanation and code)
- Confidence rationale: Explicitly presented pattern with pros/cons
- Cross-reference status: verified against Chapter 14 conclusion (Section 14.5)
