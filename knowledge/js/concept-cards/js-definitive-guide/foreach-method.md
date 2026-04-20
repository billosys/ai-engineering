---
# === CORE IDENTIFICATION ===
concept: forEach() Method
slug: foreach-method

# === CLASSIFICATION ===
category: arrays
subcategory: array methods
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Arrays"
chapter_number: 7
pdf_page: 182
section: "7.8.1 Array Iterator Methods - forEach()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
  - array-iteration
extends: []
related:
  - map-method
  - filter-method
contrasts_with:
  - map-method

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes map() from forEach()?"
---

# Quick Definition

`forEach()` iterates through an array, invoking a callback function once for each element with three arguments (value, index, array), but always returns `undefined` and cannot be terminated early.

# Core Definition

"The forEach() method iterates through an array, invoking a function you specify for each element." The callback receives three arguments: value, index, and the array itself. "forEach() does not provide a way to terminate iteration before all elements have been passed to the function. That is, there is no equivalent of the break statement." It is aware of sparse arrays and does not invoke the callback for nonexistent elements. (Flanagan, p. 182-183)

# Prerequisites

- **array-fundamentals** — Must understand arrays
- **array-iteration** — One of several iteration approaches

# Key Properties

1. Invokes callback with (value, index, array) for each element
2. Always returns `undefined` (no return value)
3. Cannot break or return early
4. Skips nonexistent elements in sparse arrays
5. Accepts optional second argument as `this` value for callback

# Construction / Recognition

```javascript
array.forEach(callback);
array.forEach((value, index, array) => { ... });
```

# Context & Application

Use forEach() when you want to perform side effects for each element. Use map() when you need to transform elements into a new array.

# Examples

```javascript
let data = [1,2,3,4,5], sum = 0;
data.forEach(value => { sum += value; });  // sum == 15

data.forEach(function(v, i, a) { a[i] = v + 1; });  // data == [2,3,4,5,6]
```
(Flanagan, p. 182-183)

# Relationships

## Builds Upon
- **array-fundamentals** — Method of Array.prototype
- **array-iteration** — Functional iteration approach

## Enables
- Side-effect based array processing

## Related
- **map-method** — Similar iteration but returns new array
- **filter-method** — Similar iteration but returns subset

## Contrasts With
- **map-method** — forEach returns undefined; map returns new array with transformed values

# Common Errors

- **Error**: Trying to use `break` or `return` to exit forEach() early.
  **Correction**: forEach() cannot be terminated early. Use a `for/of` loop with `break`, or use `find()`/`some()` for early termination.

# Common Confusions

- **Confusion**: forEach() and map() are interchangeable.
  **Clarification**: forEach() is for side effects and returns undefined; map() is for transformation and returns a new array.

# Source Reference

Chapter 7: Arrays, Section 7.8.1, pages 182-183.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented with examples
- Uncertainties: None
- Cross-reference status: Verified
