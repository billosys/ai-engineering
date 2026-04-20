---
# === CORE IDENTIFICATION ===
concept: Function Invocation Patterns
slug: invocation-patterns

# === CLASSIFICATION ===
category: functions
subcategory: invocation
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Functions"
chapter_number: 8
pdf_page: 203
section: "8.2 Invoking Functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "five invocation modes"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-declarations
extends: []
related:
  - this-keyword-binding
  - method-invocation
  - constructor-invocation
  - call-and-apply
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "In how many ways can JavaScript functions be invoked?"
---

# Quick Definition

JavaScript functions can be invoked in five ways: as functions, as methods, as constructors, indirectly via call()/apply(), and implicitly via language features. Each mode affects the `this` value differently.

# Core Definition

"JavaScript functions can be invoked in five ways: As functions, As methods, As constructors, Indirectly through their call() and apply() methods, Implicitly, via JavaScript language features that do not appear like normal function invocations." (Flanagan, p. 203-204)

# Prerequisites

- **function-declarations** — Must understand functions

# Key Properties

1. **Function invocation**: `this` is global object (non-strict) or undefined (strict)
2. **Method invocation**: `this` is the object the method is called on
3. **Constructor invocation**: `this` is the newly created object
4. **Indirect invocation**: `this` is specified as first argument to call()/apply()
5. **Implicit invocation**: getters/setters, toString(), iterators, tagged templates, proxies

# Construction / Recognition

```javascript
f(x);           // function invocation
o.m(x);         // method invocation
new F(x);       // constructor invocation
f.call(o, x);   // indirect invocation
// implicit: getters, setters, toString(), iterators
```

# Context & Application

Understanding invocation patterns is essential for predicting the value of `this` in any context.

# Examples

```javascript
printprops({x: 1});                    // function invocation
calculator.add();                       // method invocation
let o = new Object();                   // constructor invocation
f.call(o, 1, 2);                       // indirect invocation
// Implicit: obj.toString() called when object used in string context
```
(Flanagan, p. 203-210)

# Relationships

## Builds Upon
- **function-declarations** — Functions must be defined to be invoked

## Enables
- **this-keyword-binding** — Each invocation pattern determines `this`
- **method-invocation** — Method pattern explained in detail
- **constructor-invocation** — Constructor pattern for creating objects

## Related
- **call-and-apply** — Indirect invocation methods

## Contrasts With
- None specific (the five patterns contrast with each other)

# Common Errors

- **Error**: Assuming `this` is always the same regardless of how a function is called.
  **Correction**: The value of `this` depends entirely on the invocation pattern used.

# Common Confusions

- **Confusion**: There are only two or three ways to invoke functions.
  **Clarification**: There are five distinct invocation patterns, each with different `this` semantics.

# Source Reference

Chapter 8: Functions, Section 8.2, pages 203-210.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly enumerated
- Uncertainties: None
- Cross-reference status: Verified
