---
# === CORE IDENTIFICATION ===
concept: Class Declaration
slug: class-declaration

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
section: "Classes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - class notation
  - class syntax

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
  - function
  - prototype
extends: []
related:
  - constructor
  - class-method
  - static-method
  - inheritance
contrasts_with:
  - object-create

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a class with methods and inheritance?"
  - "What is a prototype?"
---

# Quick Definition
The `class` keyword starts a class declaration that defines a constructor function and a prototype with methods in a single, clear notation.

# Core Definition
Haverbeke explains: "The `class` keyword starts a class declaration, which allows us to define a constructor and a set of methods together. Any number of methods may be written inside the declaration's braces. This code has the effect of defining a binding called `Rabbit`, which holds a function that runs the code in `constructor` and has a `prototype` property that holds the `speak` method." (Ch 6, "Classes")

# Prerequisites
- **Objects**: Classes create objects
- **Functions**: Class constructors are functions
- **Prototypes**: Classes set up prototype chains behind the scenes

# Key Properties
1. Defines a constructor and methods in a single declaration
2. Methods are placed on the prototype, not on each instance
3. Must be called with `new` (unlike pre-2015 constructor functions)
4. Can be used as both statements and expressions
5. Class body is automatically in strict mode
6. Can declare instance properties directly (e.g., `speed = 0;`)

# Construction / Recognition
```javascript
class Rabbit {
  constructor(type) {
    this.type = type;
  }
  speak(line) {
    console.log(`The ${this.type} rabbit says '${line}'`);
  }
}
```

# Context & Application
The `class` notation was introduced in ECMAScript 2015 as syntactic sugar over JavaScript's prototype system. It provides a cleaner way to define types compared to manually manipulating constructor functions and prototypes.

# Examples
```javascript
class Rabbit {
  constructor(type) {
    this.type = type;
  }
  speak(line) {
    console.log(`The ${this.type} rabbit says '${line}'`);
  }
}

let killerRabbit = new Rabbit("killer");

// Class as expression
let object = new class { getWord() { return "hello"; } };
console.log(object.getWord());
// -> hello

// Instance property declaration
class Particle {
  speed = 0;
  constructor(position) {
    this.position = position;
  }
}
```
(Ch 6, "Classes", lines 292-394)

# Relationships
## Builds Upon
- prototype, function, object
## Enables
- constructor, class-method, static-method, inheritance, private-property
## Related
- encapsulation, interface
## Contrasts With
- object-create (more manual prototype setup)

# Common Errors
- **Error**: Calling a class constructor without `new`
  **Correction**: Class constructors always require `new`; they will throw an error otherwise

# Common Confusions
- **Confusion**: Classes are a fundamentally different mechanism from prototypes
  **Clarification**: "In fact, `class` was only introduced in the 2015 edition of JavaScript. Any function can be used as a constructor, and before 2015, the way to define a class was to write a regular function and then manipulate its `prototype` property." (Ch 6)

# Source Reference
Chapter 6: The Secret Life of Objects, Section "Classes", lines 258-394.

# Verification Notes
- Definition source: direct
- Confidence rationale: Core topic with extensive explanation and examples
- Cross-reference status: verified against chapter summary
