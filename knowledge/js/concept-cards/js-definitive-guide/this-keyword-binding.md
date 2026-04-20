---
# === CORE IDENTIFICATION ===
concept: this Keyword Binding
slug: this-keyword-binding

# === CLASSIFICATION ===
category: functions
subcategory: this binding
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Functions"
chapter_number: 8
pdf_page: 204
section: "8.2.1-8.2.2"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "invocation context"
  - "this value"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - invocation-patterns
extends: []
related:
  - arrow-function-this-inheritance
  - method-invocation
  - call-and-apply
  - bind-method
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do arrow functions differ from regular functions regarding this?"
  - "What must I understand before learning about closures?"
---

# Quick Definition

The `this` keyword refers to the invocation context of a function. Its value depends on how the function is called: the global object or undefined for function calls, the owning object for method calls, the new object for constructor calls, or a specified object for call()/apply().

# Core Definition

"Each invocation has another value -- the invocation context -- that is the value of the this keyword." For regular function invocation, "the invocation context (the this value) is the global object. In strict mode, however, the invocation context is undefined." For method invocation, the object is the invocation context. "The this keyword is not scoped the way variables are, and, except for arrow functions, nested functions do not inherit the this value of the containing function." (Flanagan, p. 198, 204, 207)

# Prerequisites

- **invocation-patterns** — Must understand the five invocation modes

# Key Properties

1. `this` is a keyword, not a variable (cannot be assigned)
2. Function call: global object (non-strict) or undefined (strict)
3. Method call: the object before the dot
4. Constructor call: the newly created object
5. call()/apply(): explicitly specified
6. Nested non-arrow functions do NOT inherit outer `this`
7. Arrow functions DO inherit `this` from enclosing scope

# Construction / Recognition

The `this` value is determined at call time, not definition time (except for arrow functions).

# Context & Application

Understanding `this` is critical for object-oriented JavaScript, working with methods, and avoiding common bugs in callbacks.

# Examples

```javascript
let o = {
    m: function() {
        let self = this;           // Save "this" value
        this === o                 // => true: "this" is the object o
        f();
        function f() {
            this === o             // => false: "this" is global or undefined
            self === o             // => true: self is the outer "this" value
        }
    }
};
o.m();

// Arrow function workaround (ES6):
const f = () => {
    this === o  // true, since arrow functions inherit this
};
```
(Flanagan, p. 207-208)

# Relationships

## Builds Upon
- **invocation-patterns** — Each pattern determines `this` differently

## Enables
- **arrow-function-this-inheritance** — Understanding why arrow functions exist
- **bind-method** — bind() fixes `this` for a function
- **call-and-apply** — Explicitly set `this`

## Related
- **method-invocation** — Method calls set `this` to the object

## Contrasts With
- None (contrasts with itself across different invocation patterns)

# Common Errors

- **Error**: Assuming a nested function inside a method inherits the method's `this`.
  **Correction**: Non-arrow nested functions get their own `this` (global or undefined in strict mode). Use arrow functions, bind(), or save `this` to a variable (`let self = this`).

# Common Confusions

- **Confusion**: `this` is scoped like a variable.
  **Clarification**: `this` is a keyword determined by invocation pattern, not by lexical scope (except in arrow functions).

# Source Reference

Chapter 8: Functions, Sections 8.2.1-8.2.2, pages 204-208.

# Verification Notes

- Definition source: Direct quotes from source text
- Confidence rationale: Central concept, thoroughly documented
- Uncertainties: None
- Cross-reference status: Verified
