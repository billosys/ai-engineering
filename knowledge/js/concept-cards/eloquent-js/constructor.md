---
# === CORE IDENTIFICATION ===
concept: Constructor
slug: constructor

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
  - constructor function

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
  - object
  - prototype
  - class-declaration
extends: []
related:
  - this-keyword
  - inheritance
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a class with methods and inheritance?"
  - "What is a constructor in JavaScript?"
---

# Quick Definition
A constructor is a function that creates and initializes new object instances, called with `new` to create a fresh object whose prototype is set from the constructor's `prototype` property.

# Core Definition
Haverbeke explains: "To create an instance of a given class, you have to make an object that derives from the proper prototype, but you *also* have to make sure it itself has the properties that instances of this class are supposed to have. This is what a *constructor* function does." Constructors "are called by putting the keyword `new` in front of them. Doing so creates a fresh instance object whose prototype is the object from the function's `prototype` property, then runs the function with `this` bound to the new object, and finally returns the object." (Ch 6, "Classes")

# Prerequisites
- **Functions**: Constructors are functions
- **Objects**: Constructors create objects
- **Prototypes**: The `new` operator uses the constructor's `prototype` property
- **Class declarations**: Modern constructors are defined inside `class` bodies

# Key Properties
1. Called with `new` keyword to create instances
2. `this` is bound to the newly created object
3. By convention, constructor names are capitalized
4. A class without a declared constructor gets an empty one automatically

# Construction / Recognition
```javascript
class Rabbit {
  constructor(type) {
    this.type = type;
  }
}
let killerRabbit = new Rabbit("killer");
```

# Context & Application
Constructors initialize per-instance properties. Shared behavior (methods) goes on the prototype, while constructors set up properties unique to each instance.

# Examples
```javascript
// Modern class constructor
class Rabbit {
  constructor(type) {
    this.type = type;
  }
  speak(line) {
    console.log(`The ${this.type} rabbit says '${line}'`);
  }
}
let killerRabbit = new Rabbit("killer");

// Pre-2015 constructor function
function ArchaicRabbit(type) {
  this.type = type;
}
ArchaicRabbit.prototype.speak = function(line) {
  console.log(`The ${this.type} rabbit says '${line}'`);
};
let oldSchoolRabbit = new ArchaicRabbit("old school");
```
(Ch 6, "Classes", lines 280-338)

# Relationships
## Builds Upon
- function, prototype, class-declaration
## Enables
- inheritance (via `super` calls in subclass constructors)
## Related
- this-keyword, static-method
## Contrasts With
- N/A

# Common Errors
- **Error**: Forgetting `new` when calling a pre-2015 constructor function
  **Correction**: Without `new`, `this` points to the global scope (or `undefined` in strict mode); class constructors always require `new`

# Common Confusions
- **Confusion**: A constructor's `prototype` property is the constructor's own prototype
  **Clarification**: "The actual prototype of a constructor is `Function.prototype` since constructors are functions. The constructor function's `prototype` *property* holds the prototype used for instances created through it." (Ch 6)

# Source Reference
Chapter 6: The Secret Life of Objects, Section "Classes", lines 273-367.

# Verification Notes
- Definition source: direct
- Confidence rationale: Extensively explained with both modern and archaic syntax
- Cross-reference status: verified
