---
# === CORE IDENTIFICATION ===
concept: Subclassing with extends and super
slug: subclassing-with-extends

# === CLASSIFICATION ===
category: classes
subcategory: inheritance
tier: advanced

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Classes"
chapter_number: 9
pdf_page: 256
section: "9.5.2 Subclasses with extends and super"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "class inheritance"
  - "ES6 subclassing"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - class-keyword-syntax
  - classes-and-prototypes
  - constructor-functions
extends: []
related:
  - super-in-constructors
  - super-method-calls
  - delegation-vs-inheritance
contrasts_with:
  - delegation-vs-inheritance

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about class inheritance with extends?"
  - "How does the prototype chain relate to class inheritance?"
---

# Quick Definition

The `extends` keyword creates a subclass that inherits both instance methods (via prototype chain) and static methods from a superclass. `super()` invokes the superclass constructor; `super.method()` calls overridden superclass methods.

# Core Definition

"In ES6 and later, you can create a superclass simply by adding an extends clause to a class declaration, and you can do this even for built-in classes." Subclasses inherit instance methods via prototype chain AND static methods (a new ES6 feature). "Not only are instance methods like pop() inherited, but static methods like Array.isArray are also inherited." (Flanagan, p. 256-258)

# Prerequisites

- **class-keyword-syntax** — Must understand class syntax
- **classes-and-prototypes** — Must understand prototype-based inheritance
- **constructor-functions** — Understanding the underlying mechanism

# Key Properties

1. `class B extends A {}` creates B as subclass of A
2. B.prototype inherits from A.prototype (instance methods)
3. B inherits from A (static methods -- new in ES6)
4. `super()` must be called in subclass constructor before using `this`
5. `super.method()` calls overridden superclass methods
6. If no constructor is defined, one is implicitly created that calls super()
7. Can extend built-in classes (Array, Map, etc.)

# Construction / Recognition

```javascript
class Subclass extends Superclass {
    constructor(...args) {
        super(...args);
        // subclass initialization
    }
}
```

# Context & Application

The standard way to create class hierarchies in modern JavaScript. Can extend user-defined and built-in classes.

# Examples

```javascript
class EZArray extends Array {
    get first() { return this[0]; }
    get last() { return this[this.length-1]; }
}
let a = new EZArray();
a instanceof EZArray  // => true
a instanceof Array    // => true
a.push(1,2,3,4);
a.first               // => 1
a.last                // => 4
Array.isArray(a)       // => true
EZArray.isArray(a)     // => true (static methods inherited!)

// With super:
class Span extends Range {
    constructor(start, length) {
        if (length >= 0) {
            super(start, start + length);
        } else {
            super(start + length, start);
        }
    }
}
```
(Flanagan, p. 256-258)

# Relationships

## Builds Upon
- **class-keyword-syntax** — extends is part of class syntax
- **classes-and-prototypes** — Prototype chain is the inheritance mechanism
- **constructor-functions** — Understanding what's under the hood

## Enables
- **super-in-constructors** — super() for superclass initialization
- **super-method-calls** — super.method() for calling overridden methods
- Class hierarchies

## Related
- **delegation-vs-inheritance** — Alternative to inheritance

## Contrasts With
- **delegation-vs-inheritance** — Composition may be simpler than extends

# Common Errors

- **Error**: Using `this` before calling `super()` in a subclass constructor.
  **Correction**: `super()` must be called first. This enforces that superclasses initialize before subclasses.

# Common Confusions

- **Confusion**: Pre-ES6, static methods were inherited.
  **Clarification**: Static method inheritance is a new feature of ES6 class syntax, not available with the old constructor pattern.

# Source Reference

Chapter 9: Classes, Section 9.5.2, pages 256-259.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Thoroughly documented with examples
- Uncertainties: None
- Cross-reference status: Verified
