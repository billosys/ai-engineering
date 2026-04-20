---
concept: Parameter Destructuring
slug: destructuring-parameters
category: destructuring
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Destructuring"
chapter_number: 40
pdf_page: null
section: "40.11 Parameter definitions are similar to destructuring"
extraction_confidence: high
aliases:
  - "destructured parameters"
prerequisites:
  - destructuring
extends: []
related:
  - rest-elements
contrasts_with: []
answers_questions:
  - "How do I use destructuring to extract values from objects and arrays?"
---

# Quick Definition

Function parameter definitions work like Array destructuring patterns, supporting rest elements, default values, and nested patterns, making `function f(pattern1, pattern2)` equivalent to `function f(...args) { const [pattern1, pattern2] = args; }`.

# Core Definition

Parameter definitions have much in common with an Array pattern (rest elements, default values, etc.). The two function declarations `function f1(p1, p2) {}` and `function f2(...args) { const [p1, p2] = args; }` are equivalent. This means destructuring patterns can be used directly in parameter positions.

# Prerequisites

- **destructuring** -- parameters are destructuring patterns

# Key Properties

1. Parameters behave like array destructuring of the arguments
2. Supports default values in parameters
3. Supports rest parameters (`...args`)
4. Supports nested patterns in parameters
5. Object destructuring in parameters enables named options

# Construction / Recognition

```js
function f({first, last}) {
  return `${first} ${last}`;
}
f({first: 'Jane', last: 'Doe'}); // 'Jane Doe'
```

# Context & Application

Parameter destructuring is extremely common for function options objects, callback parameters, and React component props.

# Examples

```js
// Object parameter destructuring
function greet({name, greeting = 'Hello'}) {
  return `${greeting}, ${name}!`;
}
greet({name: 'World'}); // 'Hello, World!'

// Array parameter destructuring
const getFirst = ([x]) => x;
getFirst(['a', 'b']); // 'a'
```

(Chapter 40, Section 40.11, lines 699-716)

# Relationships

## Builds Upon
- **destructuring** -- parameters are destructuring patterns

## Enables
- Named options pattern
- Clean API design

## Related
- **rest-elements** -- rest parameters

## Contrasts With
- None

# Common Errors

- **Error**: Calling a function with destructured parameters without an argument.
  **Correction**: `f()` when `f({x})` expects an object will throw. Add a default: `f({x} = {})`.

# Common Confusions

- **Confusion**: Destructured parameters require exact argument shapes.
  **Clarification**: Extra properties in object arguments are simply ignored (unless rest is used).

# Source Reference

Chapter 40: Destructuring, Section 40.11, lines 699-716.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicitly defined with equivalence
- Cross-reference status: verified
