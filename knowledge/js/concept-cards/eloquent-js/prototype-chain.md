---
# === CORE IDENTIFICATION ===
concept: Prototype Chain
slug: prototype-chain

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
  - prototype lookup chain
  - delegation chain

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
  - prototype
extends:
  - prototype
related:
  - inheritance
  - object-create
  - overriding-derived-properties
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the prototype chain relate to inheritance?"
  - "How does JavaScript look up properties on objects?"
---

# Quick Definition
The prototype chain is the sequence of linked prototype objects that JavaScript traverses when looking up a property not found directly on an object, continuing until it reaches an object with a `null` prototype.

# Core Definition
Haverbeke describes: "When an object gets a request for a property that it doesn't have, its prototype will be searched for the property. If that doesn't have it, the *prototype's* prototype is searched, and so on until an object without prototype is reached (`Object.prototype` is such an object)." (Ch 6, "Prototypes")

# Prerequisites
- **Objects**: The chain consists of objects linked together
- **Prototypes**: Each link in the chain is a prototype relationship

# Key Properties
1. Property lookup traverses the chain from object to prototype to prototype's prototype
2. The chain terminates at `Object.prototype`, whose prototype is `null`
3. Setting a property on an object creates it directly on that object, regardless of prototypes
4. `Array.prototype` -> `Object.prototype` -> `null` is a typical chain

# Construction / Recognition
The chain is established at object creation time (via `Object.create`, `new`, or literal syntax) and can be inspected with `Object.getPrototypeOf()`.

# Context & Application
The prototype chain is the mechanism behind JavaScript's inheritance. When a method is called on an object, the engine searches the chain to find it, enabling shared behavior without duplication.

# Examples
```javascript
// Array chain: [] -> Array.prototype -> Object.prototype -> null
console.log(Object.getPrototypeOf([]) == Array.prototype);
// -> true

// Prototype objects have their own prototypes
// Array.prototype -> Object.prototype
// So arrays have access to both Array and Object methods
```

The chapter's diagram shows `killerRabbit` -> `Rabbit.prototype` (with `speak`) -> `Object.prototype` (with `toString`), illustrating how properties are looked up through the chain. (Ch 6, "Overriding derived properties", line 481)

# Relationships
## Builds Upon
- prototype, object
## Enables
- inheritance, overriding-derived-properties, instanceof-operator
## Related
- object-create, class-declaration
## Contrasts With
- N/A

# Common Errors
- **Error**: Assuming all properties found on an object belong to it
  **Correction**: Properties may come from anywhere in the prototype chain; use `Object.hasOwn()` to check ownership

# Common Confusions
- **Confusion**: The prototype chain is the same as class inheritance
  **Clarification**: JavaScript's prototype chain is a delegation mechanism; classes are syntactic sugar that set up prototype chains

# Source Reference
Chapter 6: The Secret Life of Objects, Section "Prototypes", lines 196-234.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly described with diagrams and examples
- Cross-reference status: verified
