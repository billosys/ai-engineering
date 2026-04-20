---
# === CORE IDENTIFICATION ===
concept: Static Method
slug: static-method

# === CLASSIFICATION ===
category: object-oriented-programming
subcategory: class-syntax
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "The Secret Life of Objects"
chapter_number: 6
pdf_page: null
section: "Getters, setters, and statics"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - class method (in other languages)

# === TYPED RELATIONSHIPS ===
prerequisites:
  - class-declaration
  - constructor
extends: []
related:
  - method
  - class-declaration
contrasts_with:
  - method

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I attach methods to a class itself rather than its instances?"
---

# Quick Definition
Static methods are methods stored on the constructor function itself rather than on the prototype, meaning they are called on the class, not on instances.

# Core Definition
Haverbeke explains: "Inside a class declaration, methods or properties that have `static` written before their name are stored on the constructor. For example, the `Temperature` class allows you to write `Temperature.fromFahrenheit(100)` to create a temperature using degrees Fahrenheit." In a static method, `this` points at the constructor of the class, not an instance. (Ch 6, "Getters, setters, and statics")

# Prerequisites
- **Class declarations**: Static methods are defined within class bodies
- **Constructors**: Static methods are attached to the constructor

# Key Properties
1. Defined with the `static` keyword in a class body
2. Stored on the constructor, not the prototype
3. Called on the class itself, not on instances
4. `this` refers to the constructor (class) in static methods
5. Often used as factory methods or utility functions

# Construction / Recognition
```javascript
class Temperature {
  constructor(celsius) {
    this.celsius = celsius;
  }
  static fromFahrenheit(value) {
    return new Temperature((value - 32) / 1.8);
  }
}
```

# Context & Application
Static methods are commonly used for alternative constructors (factory methods), utility functions related to the class, or operations that don't require an instance.

# Examples
```javascript
let boil = Temperature.fromFahrenheit(212);
console.log(boil.celsius);
// -> 100
```

Also in the List class:
```javascript
class List {
  static fromArray(array) {
    let result = null;
    for (let i = array.length - 1; i >= 0; i--) {
      result = new this(array[i], result);
    }
    return result;
  }
}
```
Note: `this` in a static method refers to the class constructor. (Ch 6, lines 738-892)

# Relationships
## Builds Upon
- class-declaration, constructor
## Enables
- Factory pattern, alternative constructors
## Related
- method
## Contrasts With
- method (instance methods, stored on prototype)

# Common Errors
- **Error**: Trying to call a static method on an instance
  **Correction**: Static methods are called on the class: `Temperature.fromFahrenheit()`, not `temp.fromFahrenheit()`

# Common Confusions
- **Confusion**: Static methods have access to instance properties via `this`
  **Clarification**: In static methods, `this` refers to the constructor (class), not an instance; there is no instance available

# Source Reference
Chapter 6: The Secret Life of Objects, Section "Getters, setters, and statics", lines 725-742.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with examples
- Cross-reference status: verified
