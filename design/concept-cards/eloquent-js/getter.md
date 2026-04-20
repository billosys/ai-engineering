---
# === CORE IDENTIFICATION ===
concept: Getter
slug: getter

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
  - accessor property
  - get method

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
  - class-declaration
extends: []
related:
  - setter
  - method
  - encapsulation
contrasts_with:
  - setter

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can property access trigger a computation?"
  - "How do getters work in JavaScript?"
---

# Quick Definition
A getter is a method defined with the `get` keyword that is called automatically when a property is read, allowing computed values to appear as simple property accesses.

# Core Definition
Haverbeke explains: "Even properties that are accessed directly may hide a method call. Such methods are called *getters* and are defined by writing `get` in front of the method name in an object expression or class declaration." (Ch 6, "Getters, setters, and statics")

# Prerequisites
- **Objects**: Getters are defined on objects or classes
- **Class declarations**: Getters are commonly used in class bodies

# Key Properties
1. Defined with the `get` keyword before the method name
2. Called automatically when the property is accessed (no parentheses needed)
3. Can compute values on the fly
4. Appears as a regular property to external code

# Construction / Recognition
```javascript
let varyingSize = {
  get size() {
    return Math.floor(Math.random() * 100);
  }
};
console.log(varyingSize.size); // -> 73
console.log(varyingSize.size); // -> 49
```

# Context & Application
Getters are useful for computed properties that should look like regular properties to callers. They support encapsulation by hiding computation behind a property-access interface.

# Examples
```javascript
class Temperature {
  constructor(celsius) {
    this.celsius = celsius;
  }
  get fahrenheit() {
    return this.celsius * 1.8 + 32;
  }
  set fahrenheit(value) {
    this.celsius = (value - 32) / 1.8;
  }
}

let temp = new Temperature(22);
console.log(temp.fahrenheit);
// -> 71.6
```
(Ch 6, "Getters, setters, and statics", lines 695-717)

# Relationships
## Builds Upon
- object, class-declaration
## Enables
- encapsulation, computed properties
## Related
- setter, method
## Contrasts With
- setter (writes instead of reads)

# Common Errors
- **Error**: Calling a getter with parentheses like a regular method
  **Correction**: Getters are accessed like properties: `obj.prop`, not `obj.prop()`

# Common Confusions
- **Confusion**: Getters store a value
  **Clarification**: Getters compute and return a value each time they are accessed; they do not store anything themselves

# Source Reference
Chapter 6: The Secret Life of Objects, Section "Getters, setters, and statics", lines 662-687.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with examples
- Cross-reference status: verified
