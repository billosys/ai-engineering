---
# === CORE IDENTIFICATION ===
concept: Async Class Initialization
slug: async-class-initialization

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
section: "14.5 Conclusion"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - asynchronous instance creation
  - async instantiation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
  - promises
extends: []
related:
  - promise-based-constructor
  - static-factory-method
  - secret-token-pattern
  - async-property-initialization-problem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a class with async initialization?"
---

# Quick Definition

Async class initialization is the general challenge of creating class instances that require asynchronous operations to be fully set up, solved via either a Promise-based constructor or a static factory method with constructor protection.

# Core Definition

As concluded in "Deep JavaScript" (Ch 14, Section 14.5): "For the scenario examined in this chapter, I prefer either a Promise-based constructor or a static factory method plus a private constructor via a secret token." The chapter examines several techniques for instantiating classes when asynchronous data is required, presenting two recommended solutions and several alternatives.

# Prerequisites

- **JavaScript classes** — Class syntax, constructors.
- **Promises** — Async operation handling.

# Key Properties

1. Constructors are **synchronous** — they cannot use `await`.
2. Two **recommended solutions**: Promise-based constructor, and static factory + secret token.
3. Other viable approaches: prototype borrowing, inactive-by-default, separate factory function.
4. Key concern: preventing access to **incompletely initialized** instances.
5. Subclassing a Promise-based constructor has **limitations with private fields**.

# Construction / Recognition

## To Construct/Create:
1. Identify that a class needs async data during initialization.
2. Choose between a Promise-based constructor or a static factory method.
3. If using a factory method, add constructor protection (secret token recommended).

## To Identify/Recognize:
1. A class that needs data from Promises, APIs, or I/O during construction.
2. The use of one of the patterns from Chapter 14.

# Context & Application

This is the overarching topic of Chapter 14. It applies whenever classes need data from network requests, file I/O, database queries, or any other asynchronous source during initialization. The choice between approaches depends on factors like subclassing needs, private field usage, and API design preferences.

# Examples

**Example 1** (Ch 14): The two recommended approaches side by side:
```js
// Approach 1: Promise-based constructor
class A {
  #data;
  constructor() {
    return Promise.resolve('downloaded')
      .then(data => { this.#data = data; return this; });
  }
}

// Approach 2: Static factory + secret token
const secretToken = Symbol('secretToken');
class B {
  #data;
  static async create() {
    const data = await Promise.resolve('downloaded');
    return new this(secretToken, data);
  }
  constructor(token, data) {
    if (token !== secretToken) throw new Error('Private');
    this.#data = data;
  }
}
```

# Relationships

## Builds Upon
- **JavaScript classes** — The class system being extended.
- **Promises / async-await** — The async mechanisms used.

## Enables
- **Safe async services** — Classes that encapsulate async resources (database connections, API clients, etc.).

## Related
- **Promise-based constructor** — Recommended solution 1.
- **Static factory method** — Recommended solution 2 (with secret token).

## Contrasts With
- **Synchronous construction** — Standard constructors that complete all setup immediately.

# Common Errors

- **Error**: Using `async constructor()` syntax.
  **Correction**: JavaScript does not support async constructors. Use one of the patterns from Chapter 14.

# Common Confusions

- **Confusion**: Thinking there is a single "right" way to do async initialization.
  **Clarification**: The author recommends two approaches and notes that "the other techniques presented here can still be useful in other scenarios."

# Source Reference

Chapter 14: Techniques for instantiating classes, Section 14.5, lines 7443-7451.

# Verification Notes

- Definition source: synthesized (from chapter conclusion and overall structure)
- Confidence rationale: Directly stated recommendations in Section 14.5
- Cross-reference status: verified across all Chapter 14 sections
