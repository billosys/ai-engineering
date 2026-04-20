---
# === CORE IDENTIFICATION ===
concept: Symbol
slug: symbol

# === CLASSIFICATION ===
category: object-oriented-programming
subcategory: language-primitives
tier: advanced

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "The Secret Life of Objects"
chapter_number: 6
pdf_page: null
section: "Symbols"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Symbol type

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
  - interface
extends: []
related:
  - iterator-protocol
  - polymorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are symbols in JavaScript?"
  - "How do symbols prevent property name conflicts?"
---

# Quick Definition
Symbols are unique, immutable values created with the `Symbol` function that can be used as property names, preventing conflicts between different interfaces on the same object.

# Core Definition
Haverbeke explains: "Symbols are values created with the `Symbol` function. Unlike strings, newly created symbols are unique---you cannot create the same symbol twice." They were added in 2015 because "the language designers needed a type of property that *really* doesn't conflict with any others." (Ch 6, "Symbols")

# Prerequisites
- **Objects**: Symbols are used as property names on objects
- **Interfaces**: Symbols solve the problem of interface name conflicts

# Key Properties
1. Created with `Symbol("description")` --- the description is for debugging only
2. Every symbol is unique, even with the same description
3. Can be used as property names using square bracket notation
4. `Symbol.iterator` is a well-known symbol used by the iterator protocol
5. Multiple symbols can have the same name but are never equal

# Construction / Recognition
```javascript
let sym = Symbol("name");
console.log(sym == Symbol("name"));
// -> false
```

# Context & Application
Symbols are used when an interface property needs to coexist with other properties without risk of naming collision. The iterator protocol uses `Symbol.iterator` for this reason.

# Examples
```javascript
let sym = Symbol("name");
console.log(sym == Symbol("name"));
// -> false
Rabbit.prototype[sym] = 55;
console.log(killerRabbit[sym]);
// -> 55

// Using a symbol to avoid conflicts
const length = Symbol("length");
Array.prototype[length] = 0;
console.log([1, 2].length);
// -> 2
console.log([1, 2][length]);
// -> 0

// In object expressions
let myTrip = {
  length: 2,
  0: "Lankwitz",
  1: "Babelsberg",
  [length]: 21500
};
console.log(myTrip[length], myTrip.length);
// -> 21500 2
```
(Ch 6, "Symbols", lines 778-825)

# Relationships
## Builds Upon
- object, interface
## Enables
- iterator-protocol (via Symbol.iterator)
## Related
- polymorphism
## Contrasts With
- N/A

# Common Errors
- **Error**: Expecting `Symbol("name") == Symbol("name")` to be true
  **Correction**: Every `Symbol()` call creates a unique value, regardless of the description string

# Common Confusions
- **Confusion**: The string passed to Symbol is the symbol's identity
  **Clarification**: "The string you pass to `Symbol` is included when you convert it to a string and can make it easier to recognize a symbol... But it has no meaning beyond that---multiple symbols may have the same name." (Ch 6)

# Source Reference
Chapter 6: The Secret Life of Objects, Section "Symbols", lines 744-825.

# Verification Notes
- Definition source: direct
- Confidence rationale: Extensively explained with multiple examples
- Cross-reference status: verified
