---
# === CORE IDENTIFICATION ===
concept: Rest Parameters
slug: rest-parameters

# === CLASSIFICATION ===
category: data-structures
subcategory: function-inputs
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Data Structures: Objects and Arrays"
chapter_number: 4
pdf_page: null
section: "Rest parameters"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - rest operator
  - variadic parameters

# === TYPED RELATIONSHIPS ===
prerequisites:
  - parameters
  - array
  - function-definition
extends:
  - parameters
related:
  - spread-operator
  - optional-arguments
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define and call a function?"
---

# Quick Definition

A rest parameter, written with three dots before the last parameter name, collects all remaining arguments into an array, allowing a function to accept any number of arguments.

# Core Definition

As described in "Eloquent JavaScript" (Ch 4, lines 1034-1056 of 04-data-structures-objects-and-arrays.md): "It can be useful for a function to accept any number of arguments. For example, `Math.max` computes the maximum of *all* the arguments it is given. To write such a function, you put three dots before the function's last parameter." And: "When such a function is called, the *rest parameter* is bound to an array containing all further arguments."

# Prerequisites

- **parameters**: Rest parameters extend the parameter concept.
- **array**: The rest parameter is bound to an array.
- **function-definition**: Rest parameters are part of function definitions.

# Key Properties

1. Written as `...parameterName` in the function's parameter list.
2. Must be the **last** parameter.
3. Bound to an array containing all arguments not captured by preceding parameters.
4. If it is the only parameter, it holds all arguments.

# Construction / Recognition

## To Construct/Create:
```javascript
function max(...numbers) {
  let result = -Infinity;
  for (let number of numbers) {
    if (number > result) result = number;
  }
  return result;
}
```

## To Identify/Recognize:
- Three dots (`...`) before a parameter name in a function definition.

# Context & Application

Rest parameters provide a clean way to write functions that accept variable numbers of arguments. They replace the older `arguments` object pattern.

# Examples

**Example 1** (Ch 4, lines 1039-1049 of 04-data-structures-objects-and-arrays.md):
```javascript
function max(...numbers) {
  let result = -Infinity;
  for (let number of numbers) {
    if (number > result) result = number;
  }
  return result;
}
console.log(max(4, 1, 9, -2));
// → 9
```

# Relationships

## Builds Upon
- **parameters** -- Rest parameters extend regular parameters.
- **array** -- The collected arguments form an array.

## Enables
- Variadic functions (accepting any number of arguments).

## Related
- **spread-operator** -- Uses the same `...` syntax but in call/array/object contexts.
- **optional-arguments** -- Another form of flexible argument handling.

## Contrasts With
- None within this source.

# Common Errors

- **Error**: Placing a rest parameter before other parameters.
  **Correction**: The rest parameter must be the last parameter in the list.

# Common Confusions

- **Confusion**: Rest parameters and the spread operator are the same thing.
  **Clarification**: They use the same `...` syntax but in different contexts. Rest parameters collect arguments into an array; the spread operator expands an array into individual elements.

# Source Reference

Chapter 4: Data Structures: Objects and Arrays, Section "Rest parameters", lines 1031-1094 of 04-data-structures-objects-and-arrays.md (book.md line 3312).

# Verification Notes

- Definition source: direct (quoted from lines 1034-1056)
- Confidence rationale: Explicit section with italicized term "rest parameter"
- Cross-reference status: verified within chapter
