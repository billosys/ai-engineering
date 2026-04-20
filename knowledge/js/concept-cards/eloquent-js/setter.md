---
# === CORE IDENTIFICATION ===
concept: Setter
slug: setter

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
  - set method
  - mutator

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
  - class-declaration
  - getter
extends: []
related:
  - encapsulation
  - method
contrasts_with:
  - getter

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can property assignment trigger a computation?"
---

# Quick Definition
A setter is a method defined with the `set` keyword that is called automatically when a property is assigned to, allowing custom logic to execute on property writes.

# Core Definition
Haverbeke states: "You can do a similar thing when a property is written to, using a *setter*." Setters allow property assignment syntax to trigger method calls. (Ch 6, "Getters, setters, and statics")

# Prerequisites
- **Objects**: Setters are defined on objects or classes
- **Class declarations**: Setters are commonly used in class bodies
- **Getters**: Setters are typically paired with getters

# Key Properties
1. Defined with the `set` keyword before the method name
2. Called automatically when the property is assigned to
3. Takes exactly one parameter (the assigned value)
4. Typically paired with a getter for the same property name

# Construction / Recognition
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
```

# Context & Application
Setters enable controlled mutation of object state, allowing validation, conversion, or side effects when properties are modified.

# Examples
```javascript
let temp = new Temperature(22);
console.log(temp.fahrenheit);
// -> 71.6
temp.fahrenheit = 86;
console.log(temp.celsius);
// -> 30
```
The `Temperature` class allows reading and writing temperature in Fahrenheit but internally stores only Celsius. (Ch 6, "Getters, setters, and statics", lines 695-717)

# Relationships
## Builds Upon
- object, class-declaration, getter
## Enables
- encapsulation, controlled mutation
## Related
- method
## Contrasts With
- getter (reads instead of writes)

# Common Errors
- **Error**: Defining a setter without a corresponding getter (or vice versa)
  **Correction**: If external code should both read and write a computed property, provide both getter and setter

# Common Confusions
- **Confusion**: Setters directly store the value in the named property
  **Clarification**: Setters run custom code; they may transform the value and store it in a different property

# Source Reference
Chapter 6: The Secret Life of Objects, Section "Getters, setters, and statics", lines 689-723.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with Temperature example
- Cross-reference status: verified
