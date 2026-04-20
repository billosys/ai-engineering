---
# === CORE IDENTIFICATION ===
concept: Method
slug: method

# === CLASSIFICATION ===
category: object-oriented-programming
subcategory: fundamentals
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "The Secret Life of Objects"
chapter_number: 6
pdf_page: null
section: "Methods"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - object method
  - instance method

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
  - function
extends:
  - function
related:
  - this-keyword
  - class-method
  - static-method
contrasts_with:
  - static-method

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a method from a function?"
  - "How are methods defined in JavaScript?"
---

# Quick Definition
In JavaScript, methods are properties that hold function values, and when called as a method on an object, the `this` binding automatically points at that object.

# Core Definition
Haverbeke states: "In JavaScript, methods are nothing more than properties that hold function values." When called as a method---"looked up as a property and immediately called, as in `object.method()`---the binding called `this` in its body automatically points at the object on which it was called." (Ch 6, "Methods")

# Prerequisites
- **Objects**: Methods are properties of objects
- **Functions**: Methods are function values stored as properties

# Key Properties
1. A method is a function stored as an object property
2. When called via `object.method()`, `this` refers to the object
3. Shorthand method syntax: `{ find(array) { ... } }`
4. Arrow functions do not bind their own `this`

# Construction / Recognition
```javascript
// Shorthand method in object literal
let finder = {
  find(array) {
    return array.some(v => v == this.value);
  },
  value: 5
};

// Function as property
let whiteRabbit = {type: "white", speak};
```

# Context & Application
Methods are the primary way objects expose behavior. The distinction between a method call (`obj.method()`) and a plain function call is crucial because it determines the `this` binding.

# Examples
```javascript
function speak(line) {
  console.log(`The ${this.type} rabbit says '${line}'`);
}
let whiteRabbit = {type: "white", speak};
let hungryRabbit = {type: "hungry", speak};

whiteRabbit.speak("Oh my fur and whiskers");
// -> The white rabbit says 'Oh my fur and whiskers'
hungryRabbit.speak("Got any carrots?");
// -> The hungry rabbit says 'Got any carrots?'
```
(Ch 6, "Methods", lines 99-110)

# Relationships
## Builds Upon
- function, object
## Enables
- this-keyword, polymorphism, interface
## Related
- class-method, prototype
## Contrasts With
- static-method (attached to constructor, not prototype)

# Common Errors
- **Error**: Using arrow functions for methods that need `this`
  **Correction**: Arrow functions inherit `this` from their enclosing scope; use regular function syntax for methods that need their own `this` binding

# Common Confusions
- **Confusion**: Methods and functions are fundamentally different
  **Clarification**: Methods ARE functions; the difference is how they're called (via property access), which affects the `this` binding

# Source Reference
Chapter 6: The Secret Life of Objects, Section "Methods", lines 93-162.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined in the source
- Cross-reference status: verified
