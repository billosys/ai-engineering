---
# === CORE IDENTIFICATION ===
concept: filter() Method
slug: filter-method

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
pdf_page: 184
section: "7.8.1 Array Iterator Methods - filter()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
  - map-method
extends: []
related:
  - find-and-findindex
  - every-and-some
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I select a subset of array elements?"
---

# Quick Definition

`filter()` returns a new array containing only the elements for which a predicate function returns a truthy value, always producing a dense array.

# Core Definition

"The filter() method returns an array containing a subset of the elements of the array on which it is invoked. The function you pass to it should be predicate: a function that returns true or false." It skips missing elements in sparse arrays, and "its return value is always dense." (Flanagan, p. 184)

# Prerequisites

- **array-fundamentals** — Must understand arrays
- **map-method** — Similar iteration pattern

# Key Properties

1. Returns a new dense array (never sparse)
2. Does not modify the original array
3. Predicate receives (value, index, array)
4. Skips missing elements in sparse arrays
5. Can close gaps in sparse arrays: `sparse.filter(() => true)`

# Construction / Recognition

```javascript
let result = array.filter(predicate);
```

# Context & Application

Used to select subsets of data, remove unwanted values (null, undefined), and close gaps in sparse arrays.

# Examples

```javascript
let a = [5, 4, 3, 2, 1];
a.filter(x => x < 3)          // => [2, 1]
a.filter((x,i) => i%2 === 0)  // => [5, 3, 1]; every other value

// Close gaps in sparse array:
let dense = sparse.filter(() => true);

// Remove undefined and null:
a = a.filter(x => x !== undefined && x !== null);
```
(Flanagan, p. 184)

# Relationships

## Builds Upon
- **array-fundamentals** — Method of Array.prototype
- **map-method** — Similar non-mutating pattern

## Enables
- Data selection and cleaning patterns

## Related
- **find-and-findindex** — Similar predicate-based search but returns first match
- **every-and-some** — Predicate-based testing

## Contrasts With
- None specific

# Common Errors

- **Error**: Expecting filter() to modify the original array.
  **Correction**: filter() always returns a new array.

# Common Confusions

- **Confusion**: filter() preserves sparseness like map().
  **Clarification**: Unlike map(), filter() always returns a dense array.

# Source Reference

Chapter 7: Arrays, Section 7.8.1, page 184.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented
- Uncertainties: None
- Cross-reference status: Verified
