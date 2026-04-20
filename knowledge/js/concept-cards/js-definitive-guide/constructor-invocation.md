---
# === CORE IDENTIFICATION ===
concept: Constructor Invocation
slug: constructor-invocation

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
pdf_page: 208
section: "8.2.3 Constructor Invocation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "new keyword invocation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-declarations
  - invocation-patterns
extends: []
related:
  - constructor-functions
  - new-target
contrasts_with:
  - method-invocation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the new keyword work with functions?"
---

# Quick Definition

Constructor invocation uses the `new` keyword before a function call, creating a new empty object that inherits from the constructor's `prototype` property and becomes the `this` value inside the constructor.

# Core Definition

"A constructor invocation creates a new, empty object that inherits from the object specified by the prototype property of the constructor. Constructor functions are intended to initialize objects, and this newly created object is used as the invocation context, so the constructor function can refer to it with the this keyword." Constructors typically don't use `return`; the new object is returned implicitly. If a constructor returns an object, that object is used; if it returns a primitive, the return is ignored. (Flanagan, p. 208-209)

# Prerequisites

- **function-declarations** — Constructors are functions
- **invocation-patterns** — Constructor invocation is one of five patterns

# Key Properties

1. `new` creates a new empty object before the constructor runs
2. New object inherits from constructor's `prototype` property
3. `this` inside constructor refers to the new object
4. Implicit return of the new object (no `return` needed)
5. Explicit `return` of an object overrides the default; primitive `return` is ignored
6. Empty parens can be omitted: `new Object` is valid

# Construction / Recognition

```javascript
let obj = new Constructor(args);
let obj = new Constructor;  // parens optional with no args
```

# Context & Application

Constructor invocation is the mechanism behind both pre-ES6 constructor functions and ES6 classes.

# Examples

```javascript
o = new Object();
o = new Object;     // equivalent (no args, parens optional)

function Range(from, to) {
    this.from = from;
    this.to = to;
}
let r = new Range(1, 3);
```
(Flanagan, p. 208-209)

# Relationships

## Builds Upon
- **function-declarations** — Constructors are functions
- **invocation-patterns** — One of five invocation patterns

## Enables
- **constructor-functions** — The pre-ES6 class creation pattern
- **class-keyword-syntax** — ES6 classes use constructor invocation internally

## Related
- **new-target** — Detecting whether a function was called with `new`

## Contrasts With
- **method-invocation** — Method calls use existing object as `this`; constructor creates new one

# Common Errors

- **Error**: Calling a constructor without `new`, expecting it to work correctly.
  **Correction**: Without `new`, `this` is the global object (or undefined in strict mode), not a new object. Always use `new` with constructors.

# Common Confusions

- **Confusion**: Constructors must have a `return` statement.
  **Clarification**: Constructors typically omit `return`; the new object is returned automatically.

# Source Reference

Chapter 8: Functions, Section 8.2.3, pages 208-209.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented
- Uncertainties: None
- Cross-reference status: Verified
