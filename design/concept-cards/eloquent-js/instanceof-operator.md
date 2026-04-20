---
# === CORE IDENTIFICATION ===
concept: The instanceof Operator
slug: instanceof-operator

# === CLASSIFICATION ===
category: object-oriented-programming
subcategory: type-checking
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "The Secret Life of Objects"
chapter_number: 6
pdf_page: null
section: "The instanceof operator"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - class-declaration
  - prototype-chain
  - constructor
extends: []
related:
  - inheritance
  - selective-catching
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I check if an object is an instance of a particular class?"
---

# Quick Definition
The `instanceof` binary operator tests whether an object was derived from a specific class, looking through the prototype chain to account for inheritance.

# Core Definition
Haverbeke explains: "It is occasionally useful to know whether an object was derived from a specific class. For this, JavaScript provides a binary operator called `instanceof`." The operator "will see through inherited types, so a `LengthList` is an instance of `List`." (Ch 6, "The instanceof operator")

# Prerequisites
- **Class declarations**: `instanceof` checks against class constructors
- **Prototype chain**: The operator traverses the chain to determine membership
- **Constructors**: `instanceof` checks the constructor's prototype property

# Key Properties
1. Returns `true` if the object's prototype chain includes the constructor's prototype
2. Works through inheritance hierarchies
3. Can be applied to standard constructors like `Array`
4. "Almost every object is an instance of `Object`"

# Construction / Recognition
```javascript
console.log(obj instanceof SomeClass);
```

# Context & Application
`instanceof` is particularly useful for selective exception catching (Ch 8), where you need to distinguish different error types.

# Examples
```javascript
console.log(
  new LengthList(1, null) instanceof LengthList);
// -> true
console.log(new LengthList(2, null) instanceof List);
// -> true
console.log(new List(3, null) instanceof LengthList);
// -> false
console.log([1] instanceof Array);
// -> true
```
(Ch 6, "The instanceof operator", lines 1047-1057)

# Relationships
## Builds Upon
- class-declaration, prototype-chain, constructor
## Enables
- selective-catching (checking error types)
## Related
- inheritance
## Contrasts With
- N/A

# Common Errors
- **Error**: Assuming `instanceof` checks only the immediate constructor
  **Correction**: `instanceof` traverses the entire prototype chain

# Common Confusions
- **Confusion**: `instanceof` is the same as checking the constructor property
  **Clarification**: `instanceof` checks the entire prototype chain, not just a single constructor reference

# Source Reference
Chapter 6: The Secret Life of Objects, Section "The instanceof operator", lines 1040-1063.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with examples
- Cross-reference status: verified against selective catching in Ch 8
