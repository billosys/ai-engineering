---
# === CORE IDENTIFICATION ===
concept: Object and Array Initializers
slug: object-and-array-initializers

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
pdf_page: 80
section: "4.2 Object and Array Initializers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "object literals"
  - "array literals"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - primary-expressions
extends: []
related:
  - object-literals
  - shorthand-properties
  - computed-property-names
  - spread-operator-in-object-literals
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before learning about closures? (scope, statements)"
---

# Quick Definition

Object and array initializers are expressions that create and initialize new objects or arrays. They are sometimes called object literals and array literals, though they contain subexpressions and are not true primary expressions.

# Core Definition

"*Object* and *array initializers* are expressions whose value is a newly created object or array. These initializer expressions are sometimes called *object literals* and *array literals*. Unlike true literals, however, they are not primary expressions, because they include a number of subexpressions that specify property and element values." (Ch. 4, §4.2)

# Prerequisites

- **primary-expressions** — Initializers are built from primary expressions as subexpressions for property values and array elements.

# Key Properties

1. Array initializers are comma-separated expressions within square brackets; they create a new array each time evaluated.
2. Object initializers are comma-separated name:value pairs within curly braces.
3. Undefined elements can be included in arrays by omitting values between commas (sparse arrays).
4. A trailing comma is legal in both array and object literals.
5. Each evaluation of an initializer creates a new, distinct object or array.
6. Element/property expressions are evaluated each time the initializer is evaluated.

# Construction / Recognition

```js
// Array initializer
[1+2, 3+4]           // A 2-element array
let sparseArray = [1,,,,5];  // Five elements, three undefined

// Object initializer
let p = { x: 2.3, y: -1.2 };
let rectangle = {
    upperLeft: { x: 2, y: 2 },
    lowerRight: { x: 4, y: 5 }
};
```

# Context & Application

Initializers are the most common way to create objects and arrays inline in JavaScript code. When an initializer appears in a loop or a repeatedly-called function, it creates a new object/array each time, potentially with different values.

# Examples

From the source text (§4.2, pp. 80-81):

```js
[]                    // An empty array
[1+2, 3+4]          // A 2-element array. First element is 3, second is 7
let matrix = [[1,2,3], [4,5,6], [7,8,9]];  // Nested arrays
let sparseArray = [1,,,,5];  // Five elements including three undefined

let p = { x: 2.3, y: -1.2 };
let q = {};
q.x = 2.3; q.y = -1.2;     // Now q has the same properties as p
```

# Relationships

## Builds Upon
- **primary-expressions** — Subexpressions within initializers are often primary expressions

## Enables
- **object-literals** — The object initializer syntax is the foundation for object literal creation in Ch. 6
- **shorthand-properties** — ES6 extensions to object initializer syntax
- **computed-property-names** — ES6 extensions to object initializer syntax
- **spread-operator-in-object-literals** — ES2018 extension for spreading into object literals

## Related
- **property-access-expressions** — Access properties/elements created by initializers

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Expecting a trailing comma to create an extra undefined element in an array.
  **Correction**: A single trailing comma after the last expression does not create an undefined element.

# Common Confusions

- **Confusion**: Believing object/array literals are true primary expressions like number or string literals.
  **Clarification**: They are not primary expressions because they contain subexpressions. They create a new object each time they are evaluated.

# Source Reference

Chapter 4: Expressions and Operators, Section 4.2, pages 80-81.

# Verification Notes

- Definition source: Direct quote from §4.2
- Confidence rationale: High — clearly described with multiple examples
- Uncertainties: None
- Cross-reference status: Verified against Ch. 6 and Ch. 7 references
