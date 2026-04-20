---
# === CORE IDENTIFICATION ===
concept: The this Keyword
slug: this-keyword

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
  - this binding
  - this context

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
  - object
  - method
extends: []
related:
  - arrow-function
  - class-declaration
  - constructor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does 'this' refer to in a method?"
  - "How does the this binding work differently in arrow functions?"
---

# Quick Definition
The `this` keyword is an implicit parameter in function calls that, when a function is called as a method, automatically points at the object on which it was called.

# Core Definition
Haverbeke explains: "When a function is called as a method---looked up as a property and immediately called, as in `object.method()`---the binding called `this` in its body automatically points at the object on which it was called." He adds: "You can think of `this` as an extra parameter that is passed to the function in a different way than regular parameters." (Ch 6, "Methods")

# Prerequisites
- **Functions**: `this` is a binding within function bodies
- **Objects**: `this` typically refers to the object a method is called on
- **Methods**: Understanding method calls is essential for understanding `this`

# Key Properties
1. In method calls, `this` refers to the object before the dot
2. Can be explicitly set using `Function.prototype.call`
3. Arrow functions do NOT bind their own `this`; they inherit it from the surrounding scope
4. In strict mode, `this` is `undefined` in non-method function calls

# Construction / Recognition
`this` appears in function bodies and refers to the calling context. Its value depends on HOW the function is called, not where it is defined.

# Context & Application
Understanding `this` is essential for OOP in JavaScript. Arrow functions are particularly useful when you need to reference the outer `this` inside a callback.

# Examples
```javascript
function speak(line) {
  console.log(`The ${this.type} rabbit says '${line}'`);
}
let whiteRabbit = {type: "white", speak};
whiteRabbit.speak("Hurry");
// -> The white rabbit says 'Hurry'

// Using call to set this explicitly
speak.call(whiteRabbit, "Hurry");
// -> The white rabbit says 'Hurry'

// Arrow functions inherit this
let finder = {
  find(array) {
    return array.some(v => v == this.value);
  },
  value: 5
};
console.log(finder.find([4, 5]));
// -> true
```
(Ch 6, "Methods", lines 99-153)

# Relationships
## Builds Upon
- function, object, method
## Enables
- class-declaration, constructor, method
## Related
- arrow-function, strict-mode
## Contrasts With
- N/A

# Common Errors
- **Error**: Using a regular `function` keyword for callbacks that need the outer `this`
  **Correction**: Use arrow functions for callbacks that need to access the enclosing `this`

# Common Confusions
- **Confusion**: `this` always refers to the object where a function is defined
  **Clarification**: `this` depends on how the function is called, not where it is defined; arrow functions are the exception, inheriting `this` from their lexical scope

# Source Reference
Chapter 6: The Secret Life of Objects, Section "Methods", lines 93-162.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly explained with multiple examples
- Cross-reference status: verified against strict mode discussion in Ch 8
