---
# === CORE IDENTIFICATION ===
concept: Private Constructor Pattern
slug: private-constructor-pattern

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
section: "14.3.1-14.3.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - constructor restriction
  - enforced factory construction

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
  - static-factory-method
extends: []
related:
  - secret-token-pattern
  - prototype-borrowing-factory
  - inactive-by-default-pattern
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a class with async initialization?"
---

# Quick Definition

The private constructor pattern encompasses several techniques that prevent direct instantiation of a class via `new`, forcing callers to use an authorized factory method instead.

# Core Definition

As explored across "Deep JavaScript" (Ch 14, Sections 14.3.1-14.3.3): JavaScript does not natively support private constructors (unlike Java or TypeScript). The chapter presents three workarounds: (1) a secret token Symbol checked in the constructor, (2) a constructor that always throws, with instances created via `Object.create()`, and (3) an inactive-by-default flag that a private `#init()` method activates. All three ensure that only the factory method produces correctly initialized instances.

# Prerequisites

- **JavaScript classes** — Understanding constructor behavior.
- **Static factory method** — The companion pattern that creates instances.

# Key Properties

1. JavaScript has **no native private constructor** syntax.
2. Three approaches: **secret token**, **throwing constructor + Object.create()**, **inactive-by-default flag**.
3. Each approach trades off **verbosity**, **safety**, and **compatibility with private fields**.
4. Goal: ensure instances are **always fully initialized** before use.

# Construction / Recognition

## To Construct/Create:
1. Choose one of the three approaches based on your needs.
2. Implement a static factory method as the authorized creation path.
3. Make the constructor reject or neutralize unauthorized calls.

## To Identify/Recognize:
1. A constructor that throws, checks a token, or produces inactive instances.
2. A static factory method as the intended creation path.
3. Direct `new MyClass()` calls are prevented or produce unusable instances.

# Context & Application

The private constructor pattern is needed whenever a class requires controlled construction, such as async initialization, validation, caching, or singleton enforcement. In JavaScript, where constructors cannot be marked `private`, these workarounds fill the gap.

# Examples

**Example 1** (Ch 14): Three approaches summarized:
```js
// Approach 1: Secret token
const secretToken = Symbol('secretToken');
class A {
  constructor(token, data) {
    if (token !== secretToken) throw new Error('Constructor is private');
    this.data = data;
  }
}

// Approach 2: Throwing constructor + Object.create()
class B {
  constructor() { throw new Error('Constructor is private'); }
  _init(data) { this._data = data; return this; }
  static async create() {
    const data = await Promise.resolve('downloaded');
    return Object.create(this.prototype)._init(data);
  }
}

// Approach 3: Inactive by default
class C {
  #active = false;
  constructor() {}
  #init(data) { this.#active = true; this.#data = data; return this; }
  #check() { if (!this.#active) throw new Error('Not created by factory'); }
}
```

# Relationships

## Builds Upon
- **Static factory method** — All private constructor variants pair with a factory method.

## Enables
- **Async class initialization** — Private constructors ensure async setup completes before access.

## Related
- **Secret token pattern** — The recommended implementation.
- **Prototype borrowing factory** — The `Object.create()` variant.
- **Inactive-by-default pattern** — The flag-based variant.

## Contrasts With
- **Open constructors** — Standard classes where anyone can call `new`.

# Common Errors

- **Error**: Using the `Object.create()` approach with private fields.
  **Correction**: Private fields are only set up correctly by the actual constructor. The `Object.create()` approach cannot use private fields or methods.

# Common Confusions

- **Confusion**: Thinking JavaScript supports `private constructor()` syntax like TypeScript.
  **Clarification**: TypeScript's `private constructor` is a compile-time check only. At runtime, JavaScript has no native mechanism, so one of these workarounds is needed.

# Source Reference

Chapter 14: Techniques for instantiating classes, Sections 14.3.1-14.3.3, lines 7194-7329.

# Verification Notes

- Definition source: synthesized (across three subsections presenting different approaches)
- Confidence rationale: Each variant is explicitly presented; the synthesis is well-supported
- Cross-reference status: verified across Sections 14.3.1-14.3.3
