---
# === CORE IDENTIFICATION ===
concept: The extends Keyword
slug: extends-keyword

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
section: "Inheritance"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - class extension
  - subclass declaration

# === TYPED RELATIONSHIPS ===
prerequisites:
  - class-declaration
  - inheritance
  - prototype
extends: []
related:
  - constructor
  - instanceof-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define a class with methods and inheritance?"
  - "How do I create a subclass in JavaScript?"
---

# Quick Definition
The `extends` keyword in a class declaration indicates that the class inherits from another class (its superclass), setting up the prototype chain so the subclass has access to the superclass's methods.

# Core Definition
Haverbeke states: "The use of the word `extends` indicates that this class shouldn't be directly based on the default `Object` prototype but on some other class. This is called the *superclass*. The derived class is the *subclass*." (Ch 6, "Inheritance")

# Prerequisites
- **Class declarations**: `extends` is used within class syntax
- **Inheritance**: Understanding why one class would derive from another
- **Prototypes**: `extends` sets up the prototype chain

# Key Properties
1. Establishes a prototype chain from subclass to superclass
2. Subclass constructor must call `super()` to invoke the parent constructor
3. `super.method()` accesses methods on the superclass prototype
4. Static methods are also inherited

# Construction / Recognition
```javascript
class LengthList extends List {
  // ...
}
```

# Context & Application
`extends` is the syntax for establishing class inheritance in JavaScript, introduced in ES2015.

# Examples
```javascript
class LengthList extends List {
  #length;
  constructor(value, rest) {
    super(value, rest);
    this.#length = super.length;
  }
  get length() {
    return this.#length;
  }
}

console.log(LengthList.fromArray([1, 2, 3]).length);
// -> 3
```
(Ch 6, "Inheritance", lines 982-998)

# Relationships
## Builds Upon
- class-declaration, inheritance, prototype
## Enables
- instanceof-operator, method overriding
## Related
- constructor
## Contrasts With
- N/A

# Common Errors
- **Error**: Using `extends` without calling `super()` in the constructor
  **Correction**: If a subclass has a constructor, it must call `super()` before accessing `this`

# Common Confusions
- **Confusion**: `extends` copies methods from the parent class
  **Clarification**: `extends` sets up prototype delegation; methods are looked up through the chain, not copied

# Source Reference
Chapter 6: The Secret Life of Objects, Section "Inheritance", lines 1001-1004.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined
- Cross-reference status: verified
