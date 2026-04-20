---
# === CORE IDENTIFICATION ===
concept: map() Method
slug: map-method

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
pdf_page: 183
section: "7.8.1 Array Iterator Methods - map()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
  - foreach-method
extends: []
related:
  - filter-method
  - flatmap-method
contrasts_with:
  - foreach-method

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes map() from forEach()?"
---

# Quick Definition

`map()` passes each element to a function and returns a new array containing the return values, without modifying the original array.

# Core Definition

"The map() method passes each element of the array on which it is invoked to the function you specify and returns an array containing the values returned by your function." The callback is invoked identically to forEach() (with value, index, array). "map() returns a new array: it does not modify the array it is invoked on. If that array is sparse, your function will not be called for the missing elements, but the returned array will be sparse in the same way." (Flanagan, p. 183)

# Prerequisites

- **array-fundamentals** — Must understand arrays
- **foreach-method** — Same callback signature; map adds return value semantics

# Key Properties

1. Returns a new array of transformed values
2. Does not modify the original array
3. Callback receives (value, index, array)
4. Preserves sparseness (sparse input produces sparse output)
5. Returned array has same length as input

# Construction / Recognition

```javascript
let result = array.map(element => transformedElement);
```

# Context & Application

map() is the primary tool for transforming arrays. It is central to functional programming patterns in JavaScript.

# Examples

```javascript
let a = [1, 2, 3];
a.map(x => x*x)  // => [1, 4, 9]: the function takes input x and returns x*x
```
(Flanagan, p. 183)

```javascript
let squares = [1,2,3,4].map(x => x*x);  // squares == [1,4,9,16]
```
(Flanagan, p. 203)

# Relationships

## Builds Upon
- **array-fundamentals** — Method of Array.prototype
- **foreach-method** — Same iteration pattern, but with return values

## Enables
- **flatmap-method** — flatMap combines map and flat
- Functional programming patterns with arrays

## Related
- **filter-method** — Another non-mutating iterator method

## Contrasts With
- **foreach-method** — forEach returns undefined; map returns new array

# Common Errors

- **Error**: Expecting map() to modify the original array.
  **Correction**: map() always returns a new array; the original is unchanged.

# Common Confusions

- **Confusion**: Using map() when you only need side effects.
  **Clarification**: Use forEach() for side effects; map() is for transformations that produce a new array.

# Source Reference

Chapter 7: Arrays, Section 7.8.1, page 183.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Core method, clearly documented
- Uncertainties: None
- Cross-reference status: Verified
