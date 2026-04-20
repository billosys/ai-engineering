---
# === CORE IDENTIFICATION ===
concept: Property Access Expressions
slug: property-access-expressions

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: expressions
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Expressions and Operators"
chapter_number: 4
pdf_page: 81
section: "4.4 Property Access Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "dot notation"
  - "bracket notation"
  - "member access"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primary-expressions
  - object-and-array-initializers
extends: []
related:
  - optional-chaining
  - objects-as-associative-arrays
  - property-access-patterns
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

A property access expression evaluates to the value of an object property or array element using either dot notation (`expression.identifier`) or bracket notation (`expression[expression]`).

# Core Definition

"A *property access expression* evaluates to the value of an object property or an array element. JavaScript defines two syntaxes for property access: `expression . identifier` and `expression [ expression ]`." (Ch. 4, §4.4)

# Prerequisites

- **primary-expressions** — The base expression being accessed must evaluate to an object.
- **object-and-array-initializers** — Property access is meaningful on objects and arrays.

# Key Properties

1. Dot notation requires the property name to be a legal identifier known at write time.
2. Bracket notation accepts any expression that evaluates to a string (or value convertible to string, or Symbol).
3. If the value is `null` or `undefined`, the expression throws a TypeError.
4. If the named property does not exist, the result is `undefined`.
5. Property access and invocation have higher precedence than any operator.

# Construction / Recognition

```js
expression.identifier       // Dot notation
expression[expression]      // Bracket notation
```

# Context & Application

Property access is one of the most frequent operations in JavaScript. Dot notation is used for known, static property names. Bracket notation is required when property names contain spaces, punctuation, or are computed at runtime.

# Examples

From the source text (§4.4, pp. 81-82):

```js
let o = {x: 1, y: {z: 3}};
let a = [o, 4, [5, 6]];
o.x        // => 1: property x of expression o
o.y.z      // => 3: property z of expression o.y
o["x"]     // => 1: property x of object o
a[1]       // => 4: element at index 1 of expression a
a[2]["1"]  // => 6: element at index 1 of expression a[2]
a[0].x     // => 1: property x of expression a[0]
```

# Relationships

## Builds Upon
- **primary-expressions** — The object being accessed is typically a primary expression or variable reference

## Enables
- **optional-chaining** — A safer form of property access for nullable values
- **objects-as-associative-arrays** — Bracket notation enables dynamic property access
- **invocation-expressions** — Method invocation is property access followed by ()

## Related
- **property-access-patterns** — Ch. 6 elaborates on querying and setting properties

## Contrasts With
- No direct contrast — dot and bracket are two forms of the same operation

# Common Errors

- **Error**: Using dot notation with property names that contain spaces, hyphens, or are numbers.
  **Correction**: Use bracket notation for non-identifier property names: `book["main title"]`.

- **Error**: Accessing a property on `null` or `undefined` without guarding.
  **Correction**: Use optional chaining (`?.`) or explicit null checks to avoid TypeError.

# Common Confusions

- **Confusion**: Believing dot and bracket notation are fundamentally different operations.
  **Clarification**: `object.property` and `object["property"]` evaluate to the same value. The difference is syntactic: dot requires a static identifier, brackets accept any expression.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.4, pages 81-83.

# Verification Notes

- Definition source: Direct quote from §4.4
- Confidence rationale: High — clear definition with extensive examples
- Uncertainties: None
- Cross-reference status: Verified against §6.3
