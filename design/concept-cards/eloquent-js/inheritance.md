---
# === CORE IDENTIFICATION ===
concept: Inheritance
slug: inheritance

# === CLASSIFICATION ===
category: object-oriented-programming
subcategory: class-hierarchy
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
  - class inheritance
  - subclassing

# === TYPED RELATIONSHIPS ===
prerequisites:
  - class-declaration
  - prototype
  - constructor
extends: []
related:
  - extends-keyword
  - polymorphism
  - encapsulation
contrasts_with:
  - encapsulation
  - polymorphism

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the prototype chain relate to inheritance?"
  - "How do I define a class with methods and inheritance?"
---

# Quick Definition
Inheritance allows creating a new class that derives properties and behavior from an existing class, with the ability to add or override specific features.

# Core Definition
Haverbeke explains: "JavaScript's prototype system makes it possible to create a *new* class, much like the old class, but with new definitions for some of its properties. The prototype for the new class derives from the old prototype but adds a new definition for, say, the `length` getter. In object-oriented programming terms, this is called *inheritance*. The new class inherits properties and behavior from the old class." (Ch 6, "Inheritance")

# Prerequisites
- **Class declarations**: Inheritance builds on the class system
- **Prototypes**: Inheritance works through the prototype chain
- **Constructors**: Subclass constructors must call `super()`

# Key Properties
1. The `extends` keyword creates a subclass
2. `super()` calls the parent class constructor
3. `super.method()` calls parent class methods
4. The subclass is called a *subclass*, the parent a *superclass*
5. Inheritance ties classes together, creating more coupling

# Construction / Recognition
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
```

# Context & Application
Inheritance is useful for creating specialized versions of existing types. However, Haverbeke cautions: "inheritance fundamentally ties classes together, creating *more* tangle... it shouldn't be the first tool you reach for, and you probably shouldn't actively go looking for opportunities to construct class hierarchies." (Ch 6, "Inheritance")

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
- class-declaration, prototype, constructor
## Enables
- extends-keyword, instanceof-operator
## Related
- polymorphism, encapsulation
## Contrasts With
- encapsulation and polymorphism ("can be used to *separate* pieces of code from one another" while inheritance "fundamentally ties classes together")

# Common Errors
- **Error**: Forgetting to call `super()` in a subclass constructor
  **Correction**: Subclass constructors must call `super()` before using `this`

# Common Confusions
- **Confusion**: Inheritance is always the right way to share behavior
  **Clarification**: "Inheritance can be a useful tool to make some types of programs more succinct, but it shouldn't be the first tool you reach for." Prefer composition and polymorphism when possible.

# Source Reference
Chapter 6: The Secret Life of Objects, Section "Inheritance", lines 961-1038.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with clear examples and caveats
- Cross-reference status: verified against chapter summary
