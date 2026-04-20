---
# === CORE IDENTIFICATION ===
concept: Classes and Prototypes
slug: classes-and-prototypes

# === CLASSIFICATION ===
category: classes
subcategory: prototypes
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
  - "prototype-based classes"
  - "prototype-based inheritance"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - functions-as-values
extends: []
related:
  - constructor-functions
  - class-keyword-syntax
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the prototype chain relate to class inheritance?"
---

# Quick Definition

In JavaScript, a class is a set of objects that inherit properties from the same prototype object. The prototype defines shared methods (behavior) while each instance holds its own state.

# Core Definition

"In JavaScript, a class is a set of objects that inherit properties from the same prototype object. The prototype object, therefore, is the central feature of a class." "JavaScript prototypes and inheritance were covered in 6.2.3 and 6.3.2." Classes use prototype-based inheritance: "if two objects inherit properties (generally function-valued properties, or methods) from the same prototype, then we say that those objects are instances of the same class." (Flanagan, p. 238-240)

# Prerequisites

- **functions-as-values** — Methods are function-valued properties

# Key Properties

1. A class is defined by its prototype object
2. Objects sharing a prototype are instances of the same class
3. Prototype defines shared methods (behavior)
4. Each instance has its own properties (state)
5. Factory functions + Object.create() can create classes without constructors

# Construction / Recognition

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
```

# Context & Application

Understanding prototype-based classes is essential for understanding JavaScript's class mechanism, even when using ES6 class syntax.

# Examples

```javascript
// Factory function pattern (Example 9-1):
function range(from, to) {
    let r = Object.create(range.methods);
    r.from = from;
    r.to = to;
    return r;
}
range.methods = {
    includes(x) { return this.from <= x && x <= this.to; },
    *[Symbol.iterator]() {
        for (let x = Math.ceil(this.from); x <= this.to; x++) yield x;
    },
    toString() { return "(" + this.from + "..." + this.to + ")"; }
};
let r = range(1,3);
r.includes(2)   // => true
[...r]           // => [1, 2, 3]
```
(Flanagan, p. 239-240)

# Relationships

## Builds Upon
- **functions-as-values** — Methods are functions stored as properties

## Enables
- **constructor-functions** — The idiomatic pre-ES6 class pattern
- **class-keyword-syntax** — ES6 sugar over prototype-based classes

## Related
- None specific

## Contrasts With
- None specific

# Common Errors

- **Error**: Thinking prototypes and classes are entirely separate concepts in JavaScript.
  **Correction**: Classes in JavaScript ARE prototype-based. The class keyword is syntactic sugar.

# Common Confusions

- **Confusion**: JavaScript classes work like Java or C++ classes.
  **Clarification**: JavaScript's prototype-based inheritance is fundamentally different from class-based inheritance in languages like Java.

# Source Reference

Chapter 9: Classes, Section 9.1, pages 239-241.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Foundational concept, thoroughly explained
- Uncertainties: None
- Cross-reference status: References Ch. 6 prototypes
