---
# === CORE IDENTIFICATION ===
concept: Shorthand Methods
slug: shorthand-methods

# === CLASSIFICATION ===
category: objects
subcategory: extended-literal-syntax
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Objects"
chapter_number: 6
pdf_page: 166
section: "6.10.5 Shorthand Methods"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "method shorthand"
  - "concise methods"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object-literals
  - function-definition-expressions
extends:
  - object-literals
related:
  - getters-and-setters
  - computed-property-names
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

ES6 shorthand method syntax allows defining methods in object literals by omitting the `function` keyword and colon: `{ area() { ... } }` instead of `{ area: function() { ... } }`.

# Core Definition

"In ES6, however, the object literal syntax has been extended to allow a shortcut where the function keyword and the colon are omitted." The property name can be any form legal in object literals: identifiers, string literals, computed property names, or Symbol names. (Ch. 6, §6.10.5)

# Prerequisites

- **object-literals** — Shorthand methods extend object literal syntax.
- **function-definition-expressions** — Methods are functions defined as property values.

# Key Properties

1. `{ method() { ... } }` is equivalent to `{ method: function() { ... } }`.
2. Shorthand makes it clearer that the property is a method, not a data property.
3. Works with computed property names: `{ [symbol](x) { ... } }`.
4. Works with string literals: `{ "method With Spaces"(x) { ... } }`.

# Construction / Recognition

```js
let square = {
    area() { return this.side * this.side; },
    side: 10
};
```

# Context & Application

Shorthand methods are the standard way to define methods in object literals and are also used in class definitions (Ch. 9). They improve readability by distinguishing methods from data properties.

# Examples

From the source text (§6.10.5, pp. 166-167):

```js
// Pre-ES6:
let square = {
    area: function() { return this.side * this.side; },
    side: 10
};

// ES6 shorthand:
let square = {
    area() { return this.side * this.side; },
    side: 10
};
square.area()  // => 100

// With computed property names and Symbols:
const METHOD_NAME = "m";
const symbol = Symbol();
let weirdMethods = {
    "method With Spaces"(x) { return x + 1; },
    [METHOD_NAME](x) { return x + 2; },
    [symbol](x) { return x + 3; }
};
```

# Relationships

## Builds Upon
- **object-literals** — Extends literal syntax
- **function-definition-expressions** — Methods are function values

## Enables
- Cleaner method definitions in objects and classes

## Related
- **getters-and-setters** — Also use shorthand-like syntax with `get`/`set` prefix
- **computed-property-names** — Can be combined with shorthand methods

## Contrasts With
- No direct contrast (old syntax still works)

# Common Errors

- **Error**: None specific — shorthand is purely syntactic sugar.

# Common Confusions

- **Confusion**: Believing shorthand methods and arrow functions are the same.
  **Clarification**: Shorthand methods have their own `this` binding. Arrow functions inherit `this` from the enclosing scope.

# Source Reference

Chapter 6: Objects, Section 6.10.5, pages 166-167.

# Verification Notes

- Definition source: Direct quote from §6.10.5
- Confidence rationale: High — clear comparison of old and new syntax
- Uncertainties: None
- Cross-reference status: Verified
