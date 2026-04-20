---
# === CORE IDENTIFICATION ===
concept: Prototype
slug: prototype

# === CLASSIFICATION ===
category: object-oriented-programming
subcategory: inheritance-mechanism
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "The Secret Life of Objects"
chapter_number: 6
pdf_page: null
section: "Prototypes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - prototype object

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
extends: []
related:
  - prototype-chain
  - object-create
  - class-declaration
  - constructor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a prototype?"
  - "What must I know before learning about prototypes and classes?"
---

# Quick Definition
A prototype is an object from which other objects inherit properties; when an object is asked for a property it doesn't have, its prototype is searched, then the prototype's prototype, and so on.

# Core Definition
Haverbeke writes: "In JavaScript, *prototypes* are the way to do that. Objects can be linked to other objects, to magically get all the properties that other object has. Plain old objects created with `{}` notation are linked to an object called `Object.prototype`." (Ch 6, "Prototypes")

# Prerequisites
- **Objects**: Prototypes are objects that serve as fallback property sources for other objects

# Key Properties
1. Every object has a prototype (except `Object.prototype`, whose prototype is `null`)
2. Plain objects derive from `Object.prototype`
3. Functions derive from `Function.prototype`
4. Arrays derive from `Array.prototype`
5. Properties looked up on an object fall through to its prototype if not found

# Construction / Recognition
Use `Object.getPrototypeOf()` to inspect an object's prototype. Use `Object.create()` to create an object with a specific prototype.

# Context & Application
Prototypes are the foundation of JavaScript's inheritance model. They allow shared behavior among objects without duplicating methods on each instance.

# Examples
```javascript
let empty = {};
console.log(empty.toString);
// -> function toString(){...}
console.log(empty.toString());
// -> [object Object]

console.log(Object.getPrototypeOf({}) == Object.prototype);
// -> true
console.log(Object.getPrototypeOf(Object.prototype));
// -> null

console.log(Object.getPrototypeOf(Math.max) ==
            Function.prototype);
// -> true
console.log(Object.getPrototypeOf([]) == Array.prototype);
// -> true
```
(Ch 6, "Prototypes", lines 183-228)

# Relationships
## Builds Upon
- object
## Enables
- prototype-chain, class-declaration, inheritance, polymorphism
## Related
- object-create, constructor
## Contrasts With
- N/A

# Common Errors
- **Error**: Confusing a constructor's `prototype` property with the constructor's own prototype
  **Correction**: "The actual prototype of a constructor is `Function.prototype` since constructors are functions. The constructor function's `prototype` *property* holds the prototype used for instances created through it." (Ch 6)

# Common Confusions
- **Confusion**: Every property on an object belongs to the object itself
  **Clarification**: Properties may be inherited from the prototype chain; use `Object.hasOwn()` to check if a property belongs directly to an object

# Source Reference
Chapter 6: The Secret Life of Objects, Section "Prototypes", lines 163-257.

# Verification Notes
- Definition source: direct
- Confidence rationale: Core concept of the chapter, extensively explained
- Cross-reference status: verified against chapter summary
