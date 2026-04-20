---
# === CORE IDENTIFICATION ===
concept: Method Invocation
slug: method-invocation

# === CLASSIFICATION ===
category: functions
subcategory: invocation
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Functions"
chapter_number: 8
pdf_page: 205
section: "8.2.2 Method Invocation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-declarations
  - invocation-patterns
extends: []
related:
  - this-keyword-binding
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a method in JavaScript?"
  - "How does this work in method invocations?"
---

# Quick Definition

A method is a function stored as a property of an object. When invoked via property access (`obj.method()`), the object becomes the invocation context (`this` value) for the function.

# Core Definition

"A method is nothing more than a JavaScript function that is stored in a property of an object." When invoked as `o.m()`, the object `o` becomes the invocation context and the `this` keyword refers to it inside the function body. "Methods and the this keyword are central to the object-oriented programming paradigm." Method chaining is possible when methods return `this`. (Flanagan, p. 205-207)

# Prerequisites

- **function-declarations** — Must understand functions
- **invocation-patterns** — Method invocation is one of five patterns

# Key Properties

1. The object before the dot becomes `this`
2. Bracket notation also works: `o["m"]()`
3. Chained property access: `customer.surname.toUpperCase()`
4. Method chaining: methods that return `this` allow `obj.a().b().c()`
5. Nested non-arrow functions inside methods do NOT inherit the method's `this`

# Construction / Recognition

```javascript
let calculator = {
    operand1: 1,
    operand2: 1,
    add() {
        this.result = this.operand1 + this.operand2;
    }
};
calculator.add();
calculator.result  // => 2
```

# Context & Application

Method invocation is the core of object-oriented JavaScript. Understanding that `this` is the object the method is called on is essential.

# Examples

```javascript
let calculator = {
    operand1: 1, operand2: 1,
    add() { this.result = this.operand1 + this.operand2; }
};
calculator.add();
calculator.result  // => 2

o["m"](x,y);   // bracket notation method call
a[0](z)         // also a method invocation if a[0] is a function
```
(Flanagan, p. 205-206)

# Relationships

## Builds Upon
- **function-declarations** — Methods are functions stored on objects
- **invocation-patterns** — One of five invocation modes

## Enables
- **this-keyword-binding** — Method calls define `this` as the object
- Object-oriented programming patterns

## Related
- None specific

## Contrasts With
- None specific

# Common Errors

- **Error**: Extracting a method from an object and calling it as a standalone function, losing `this`.
  **Correction**: Use bind() to preserve the `this` binding: `const fn = obj.method.bind(obj)`.

# Common Confusions

- **Confusion**: `this` inside a nested function within a method refers to the same object.
  **Clarification**: Non-arrow nested functions get their own `this` (global/undefined). Use arrow functions or `self = this` to access the outer `this`.

# Source Reference

Chapter 8: Functions, Section 8.2.2, pages 205-208.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Well-documented with clear examples
- Uncertainties: None
- Cross-reference status: Verified
