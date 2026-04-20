---
# === CORE IDENTIFICATION ===
concept: Nested Destructuring
slug: nested-destructuring

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: variables
tier: advanced

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 76
section: "3.10.3 Destructuring Assignment"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - complex destructuring
  - deep destructuring

# === TYPED RELATIONSHIPS ===
prerequisites:
  - destructuring-assignment
extends:
  - destructuring-assignment
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I destructure nested objects and arrays?"
  - "What is destructuring assignment?"
---

# Quick Definition

Nested destructuring extends basic destructuring to extract values from nested arrays, objects within arrays, or arrays within objects, using correspondingly nested literal syntax on the left side of the assignment.

# Core Definition

"Destructuring assignment becomes even more complicated when it is used with nested objects, or arrays of objects, or objects of arrays, but it is legal." The lefthand side of nested destructuring "should look like a nested array literal" for nested arrays. A useful regularity: "The lefthand side of a destructuring assignment looks like an array literal or an object literal. After the assignment has been done, the lefthand side will actually work as a valid array literal or object literal elsewhere in your code." (pp. 76-77)

# Prerequisites

- **destructuring-assignment** — Must understand basic destructuring

# Key Properties

1. Nested arrays: `[a, [b, c]] = [1, [2, 2.5], 3]`
2. Array of objects: `[{x: x1, y: y1}, {x: x2, y: y2}] = points`
3. Object of arrays: `{p1: [x1, y1], p2: [x2, y2]} = points`
4. Verification trick: the left side should work as a valid literal on the right side of another assignment
5. Can become "hard to write and hard to read" — sometimes explicit property access is clearer

# Construction / Recognition

```javascript
// Nested arrays
let [a, [b, c]] = [1, [2, 2.5], 3];    // a==1; b==2; c==2.5

// Array of objects
let [{x: x1, y: y1}, {x: x2, y: y2}] = [{x:1,y:2}, {x:3,y:4}];

// Object of arrays
let {p1: [x1, y1], p2: [x2, y2]} = {p1: [1,2], p2: [3,4]};
```

# Context & Application

Nested destructuring is used when working with complex API responses, configuration objects, and data structures. However, the source cautions that "complex destructuring syntax like this can be hard to write and hard to read, and you may be better off just writing out your assignments explicitly" (p. 77).

# Examples

From the source text (pp. 76-77):

Nested arrays:
```javascript
let [a, [b, c]] = [1, [2,2.5], 3];   // a == 1; b == 2; c == 2.5
```

Array of objects:
```javascript
let points = [{x: 1, y: 2}, {x: 3, y: 4}];
let [{x: x1, y: y1}, {x: x2, y: y2}] = points;
(x1 === 1 && y1 === 2 && x2 === 3 && y2 === 4)  // => true
```

Object of arrays:
```javascript
let points = { p1: [1,2], p2: [3,4] };
let { p1: [x1, y1], p2: [x2, y2] } = points;
(x1 === 1 && y1 === 2 && x2 === 3 && y2 === 4)  // => true
```

Verification technique (p. 77):
```javascript
// Check your destructuring by flipping the assignment:
let [{x: x1, y: y1}, {x: x2, y: y2}] = points;
// Verify: the left side works as a literal on the right:
let points2 = [{x: x1, y: y1}, {x: x2, y: y2}];  // points2 == points
```

# Relationships

## Builds Upon
- **destructuring-assignment** — Extends basic destructuring to nested structures

## Enables
- Working with complex nested data (API responses, configurations)

## Related
- None additional

## Contrasts With
- Explicit property access: `let x1 = points.p1[0]` — sometimes clearer

# Common Errors

- **Error**: Getting the nesting structure wrong, leading to undefined values.
  **Correction**: Use the verification technique: the left side should work as a valid literal on the right side of another assignment.

# Common Confusions

- **Confusion**: Nested destructuring is always better than explicit access.
  **Clarification**: "Complex destructuring syntax like this can be hard to write and hard to read, and you may be better off just writing out your assignments explicitly with traditional code like `let x1 = points.p1[0]`" (p. 77).

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.10.3, pages 76-77.

# Verification Notes

- Definition source: Direct quotes from pp. 76-77
- Confidence rationale: High — clearly explained with examples and verification technique
- Uncertainties: None
- Cross-reference status: Verified
