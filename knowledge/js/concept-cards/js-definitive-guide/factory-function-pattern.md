---
# === CORE IDENTIFICATION ===
concept: Factory Function Pattern
slug: factory-function-pattern

# === CLASSIFICATION ===
category: classes
subcategory: class creation
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Classes"
chapter_number: 9
pdf_page: 239
section: "9.1 Classes and Prototypes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "factory pattern"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - classes-and-prototypes
extends: []
related:
  - constructor-functions
contrasts_with:
  - constructor-functions

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can I create objects with shared behavior without using constructors?"
---

# Quick Definition

A factory function creates and returns new objects by using Object.create() to set up prototype inheritance and then initializing instance-specific properties, without requiring the `new` keyword.

# Core Definition

The factory function pattern "defines a prototype object and then use Object.create() to create objects that inherit from it." The factory function "creates and initializes the new object." Unlike constructors, factory functions are called without `new` and explicitly create and return the object. (Flanagan, p. 239-240)

# Prerequisites

- **classes-and-prototypes** — Must understand prototype-based classes

# Key Properties

1. Called without `new` keyword
2. Explicitly creates object with Object.create()
3. Sets prototype manually
4. Returns the new object
5. Prototype can be stored anywhere (e.g., as a property of the factory function)

# Construction / Recognition

```javascript
function range(from, to) {
    let r = Object.create(range.methods);
    r.from = from;
    r.to = to;
    return r;
}
range.methods = { /* shared methods */ };
```

# Context & Application

A simpler alternative to constructors for creating objects with shared behavior. Less idiomatic than constructors but still valid.

# Examples

```javascript
function range(from, to) {
    let r = Object.create(range.methods);
    r.from = from;
    r.to = to;
    return r;
}
range.methods = {
    includes(x) { return this.from <= x && x <= this.to; },
    toString() { return "(" + this.from + "..." + this.to + ")"; }
};
let r = range(1,3);
r.includes(2)  // => true
```
(Flanagan, p. 239-240, Example 9-1)

# Relationships

## Builds Upon
- **classes-and-prototypes** — Uses prototype-based inheritance

## Enables
- Simple object creation without constructor overhead

## Related
- **constructor-functions** — More idiomatic alternative

## Contrasts With
- **constructor-functions** — Constructors use `new`; factories don't. Constructors use `this`; factories create and return objects explicitly.

# Common Errors

- **Error**: Calling a factory function with `new`.
  **Correction**: Factory functions are not designed for `new` invocation. Use them as regular function calls.

# Common Confusions

- **Confusion**: Factory functions and constructors produce fundamentally different objects.
  **Clarification**: Both can produce objects with prototype-based inheritance; they differ in invocation style.

# Source Reference

Chapter 9: Classes, Section 9.1, pages 239-241.

# Verification Notes

- Definition source: Synthesized from source text
- Confidence rationale: Example 9-1 provides a complete implementation
- Uncertainties: None
- Cross-reference status: Verified
