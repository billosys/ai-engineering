---
# === CORE IDENTIFICATION ===
concept: Destructuring Function Parameters
slug: destructuring-parameters

# === CLASSIFICATION ===
category: functions
subcategory: parameters
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Functions"
chapter_number: 8
pdf_page: 214
section: "8.3.5 Destructuring Function Arguments into Parameters"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "parameter destructuring"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-declarations
  - default-parameters
extends: []
related:
  - rest-parameters
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I unpack object or array arguments into named parameters?"
---

# Quick Definition

Destructuring syntax in parameter lists unpacks array or object arguments into individually named parameters, combining with defaults for named/optional parameter patterns.

# Core Definition

"If you define a function that has parameter names within square brackets, you are telling the function to expect an array value to be passed for each pair of square brackets." Similarly, curly braces destructure object arguments. "You can define parameter defaults with destructured parameters." Destructuring an object argument enables Python-like named parameters. (Flanagan, p. 214-216)

# Prerequisites

- **function-declarations** — Must understand function parameters
- **default-parameters** — Destructured params can have defaults

# Key Properties

1. Array destructuring: `function f([x, y]) {}`
2. Object destructuring: `function f({x, y}) {}`
3. Can combine with defaults: `function f({x, y, z=0}) {}`
4. Enables named parameter patterns
5. Can use rest syntax within destructured params

# Construction / Recognition

```javascript
function vectorAdd([x1,y1], [x2,y2]) {
    return [x1 + x2, y1 + y2];
}

function f({from, to=from, n=from.length}) { ... }
```

# Context & Application

Object destructuring enables named parameters (like Python's keyword args). Array destructuring simplifies working with tuple-like data.

# Examples

```javascript
// Array destructuring:
function vectorAdd([x1,y1], [x2,y2]) {
    return [x1 + x2, y1 + y2];
}
vectorAdd([1,2], [3,4])  // => [4,6]

// Object destructuring with defaults:
function vectorMultiply({x, y, z=0}, scalar) {
    return { x: x*scalar, y: y*scalar, z: z*scalar };
}
vectorMultiply({x: 1, y: 2}, 2)  // => {x: 2, y: 4, z: 0}

// Named parameters pattern:
function arraycopy({from, to=from, n=from.length, fromIndex=0, toIndex=0}) {
    let valuesToCopy = from.slice(fromIndex, fromIndex + n);
    to.splice(toIndex, 0, ...valuesToCopy);
    return to;
}
arraycopy({from: a, n: 3, to: b, toIndex: 4})
```
(Flanagan, p. 214-216)

# Relationships

## Builds Upon
- **function-declarations** — Extends parameter syntax
- **default-parameters** — Combined with defaults

## Enables
- Named parameter patterns (simulating keyword arguments)

## Related
- **rest-parameters** — Can use rest within destructured params

## Contrasts With
- None specific

# Common Errors

- **Error**: Confusing property names with parameter names in `{x: x1, y: y1}` syntax.
  **Correction**: In destructuring, property names are on the left of the colon, parameter names on the right (opposite of object literals).

# Common Confusions

- **Confusion**: Destructuring parameter objects is always clearer than regular parameters.
  **Clarification**: Complex destructuring can become harder to read than explicit property access.

# Source Reference

Chapter 8: Functions, Section 8.3.5, pages 214-216.

# Verification Notes

- Definition source: Direct quote and synthesis from source text
- Confidence rationale: Well-documented with multiple examples
- Uncertainties: None
- Cross-reference status: Verified
