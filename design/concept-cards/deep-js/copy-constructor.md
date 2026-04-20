---
# === CORE IDENTIFICATION ===
concept: Copy Constructor
slug: copy-constructor

# === CLASSIFICATION ===
category: class-patterns
subcategory: cloning
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Copying instances of classes: .clone() vs. copy constructors"
chapter_number: 15
section: "15.2 Static factory methods"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - overloaded constructor for copying

# === TYPED RELATIONSHIPS ===
prerequisites:
  - javascript-classes
extends: []
related:
  - clone-method
  - static-from-factory
contrasts_with:
  - clone-method
  - static-from-factory

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I implement the .clone() pattern for class instances?"
---

# Quick Definition

A copy constructor is a constructor overload that accepts an existing instance of the same class and uses it to initialize a new instance, but in JavaScript this pattern leads to inelegant code due to the lack of static overloading.

# Core Definition

As described in "Deep JavaScript" (Ch 15, Section 15.2): "A copy constructor is a constructor that uses another instance of the current class to set up the current instance. Copy constructors are popular in static languages such as C++ and Java, where you can provide multiple versions of a constructor via static overloading. Here, static means that the choice which version to use, is made at compile time. In JavaScript, we must make that decision at runtime and that leads to inelegant code."

# Prerequisites

- **JavaScript classes** — Constructor overloading attempted via runtime checks.

# Key Properties

1. The constructor uses **runtime `instanceof` checks** to distinguish copy calls from normal calls.
2. Requires **rest parameters** (`...args`) to handle different signatures.
3. Considered **inelegant** in JavaScript due to lack of static overloading.
4. The author recommends **static factory methods** (`.from()`) instead.
5. Popular in **C++ and Java** but not idiomatic in JavaScript.

# Construction / Recognition

## To Construct/Create:
1. Define a constructor that accepts `...args`.
2. Check if `args[0] instanceof ClassName`.
3. If so, copy properties from the existing instance.
4. Otherwise, treat arguments as normal construction parameters.

## To Identify/Recognize:
1. A constructor with `instanceof` checks to distinguish copy vs. normal construction.
2. Multiple code paths in the constructor for different argument patterns.

# Context & Application

The copy constructor pattern is presented primarily to explain why it is not recommended in JavaScript. The author uses it as motivation for introducing static factory methods (`.from()`), which provide a cleaner API for the same functionality.

# Examples

**Example 1** (Ch 15): Copy constructor in JavaScript:
```js
class Point {
  constructor(...args) {
    if (args[0] instanceof Point) {
      // Copy constructor
      const [other] = args;
      this.x = other.x;
      this.y = other.y;
    } else {
      const [x, y] = args;
      this.x = x;
      this.y = y;
    }
  }
}

const original = new Point(-1, 4);
const copy = new Point(original);
assert.deepEqual(copy, original);
```

# Relationships

## Builds Upon
- **JavaScript classes** — Constructor mechanics.
- **instanceof operator** — Used for runtime type checking.

## Enables
- **Instance copying** — Creates copies of existing instances.

## Related
- **Static `.from()` factory** — The recommended alternative in JavaScript.

## Contrasts With
- **`.clone()` method** — Puts copying on the instance, not in the constructor.
- **Static `.from()` factory** — Cleaner API without constructor overloading.

# Common Errors

- **Error**: Assuming JavaScript supports static overloading like C++ or Java.
  **Correction**: JavaScript has no compile-time overloading. Runtime `instanceof` checks are needed, making the code verbose and fragile.

# Common Confusions

- **Confusion**: Thinking copy constructors are the idiomatic way to copy in JavaScript.
  **Clarification**: The author explicitly recommends static factory methods (`.from()`) over copy constructors for JavaScript.

# Source Reference

Chapter 15: Copying instances of classes, Section 15.2, lines 7569-7606.

# Verification Notes

- Definition source: direct (quoted definition from source)
- Confidence rationale: Explicitly defined with comparison to other languages
- Cross-reference status: verified against static factory method recommendation
