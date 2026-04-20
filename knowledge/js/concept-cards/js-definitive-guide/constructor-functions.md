---
# === CORE IDENTIFICATION ===
concept: Constructor Functions
slug: constructor-functions

# === CLASSIFICATION ===
category: classes
subcategory: constructors
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Classes"
chapter_number: 9
pdf_page: 241
section: "9.2 Classes and Constructors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "constructor pattern"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - classes-and-prototypes
  - constructor-invocation
extends: []
related:
  - instanceof-operator
  - constructor-property
  - class-keyword-syntax
contrasts_with:
  - factory-function-pattern

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about class inheritance with extends?"
  - "How does the prototype chain relate to class inheritance?"
---

# Quick Definition

A constructor function is a function designed to initialize newly created objects when invoked with `new`. The constructor's `prototype` property is automatically used as the prototype of instances.

# Core Definition

"A constructor is a function designed for the initialization of newly created objects. Constructors are invoked using the new keyword. Constructor invocations using new automatically create the new object, so the constructor itself only needs to initialize the state of that new object. The critical feature of constructor invocations is that the prototype property of the constructor is used as the prototype of the new object." Convention: constructor names begin with a capital letter. (Flanagan, p. 241-242)

# Prerequisites

- **classes-and-prototypes** — Must understand prototype-based classes
- **constructor-invocation** — Must understand the `new` keyword

# Key Properties

1. Invoked with `new` keyword
2. `this` refers to the newly created object
3. Constructor.prototype becomes the prototype of new instances
4. Convention: names start with uppercase
5. Do not need to call Object.create() or return the object
6. Arrow functions cannot be constructors (no prototype)

# Construction / Recognition

```javascript
function Range(from, to) {
    this.from = from;
    this.to = to;
}
Range.prototype = {
    includes(x) { return this.from <= x && x <= this.to; },
    toString() { return "(" + this.from + "..." + this.to + ")"; }
};
let r = new Range(1, 3);
```

# Context & Application

The idiomatic pre-ES6 way to define classes. Understanding constructors is essential for understanding how ES6 class syntax works under the hood.

# Examples

```javascript
function Range(from, to) {
    this.from = from;
    this.to = to;
}
Range.prototype = {
    includes: function(x) { return this.from <= x && x <= this.to; },
    toString: function() { return "(" + this.from + "..." + this.to + ")"; }
};
let r = new Range(1,3);
r.includes(2)   // => true
r.toString()     // => "(1...3)"
```
(Flanagan, p. 241-242, Example 9-2)

# Relationships

## Builds Upon
- **classes-and-prototypes** — Constructor pattern is the idiomatic prototype-based class
- **constructor-invocation** — Constructors are invoked with `new`

## Enables
- **instanceof-operator** — instanceof checks prototype chain
- **class-keyword-syntax** — ES6 class is syntactic sugar for constructors

## Related
- **constructor-property** — Prototype's back-reference to constructor

## Contrasts With
- **factory-function-pattern** — Factories don't use `new`; constructors do

# Common Errors

- **Error**: Calling a constructor without `new`.
  **Correction**: Without `new`, `this` is the global object (or undefined in strict mode). Always use `new` with constructors.

# Common Confusions

- **Confusion**: The constructor creates the new object.
  **Clarification**: `new` creates the object; the constructor only initializes it.

# Source Reference

Chapter 9: Classes, Section 9.2, pages 241-243.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Well-documented with complete Example 9-2
- Uncertainties: None
- Cross-reference status: Verified
