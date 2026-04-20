---
# === CORE IDENTIFICATION ===
concept: concat() Method
slug: concat-method

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
pdf_page: 187
section: "7.8.3 Adding arrays with concat()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
extends: []
related:
  - spread-operator-in-arrays
  - push-pop-shift-unshift
contrasts_with:
  - push-pop-shift-unshift

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I combine multiple arrays in JavaScript?"
---

# Quick Definition

`concat()` creates and returns a new array containing the elements of the original array followed by its arguments, flattening array arguments by one level but not modifying the original.

# Core Definition

"The concat() method creates and returns a new array that contains the elements of the original array on which concat() was invoked, followed by each of the arguments to concat(). If any of these arguments is itself an array, then it is the array elements that are concatenated, not the array itself. Note, however, that concat() does not recursively flatten arrays of arrays. concat() does not modify the array on which it is invoked." (Flanagan, p. 187)

# Prerequisites

- **array-fundamentals** — Must understand arrays

# Key Properties

1. Returns a new array (does not mutate original)
2. Flattens array arguments by one level
3. Does not recursively flatten nested arrays
4. Creates a new copy (can be expensive)

# Construction / Recognition

```javascript
let combined = a.concat(b, c);
```

# Context & Application

Use for combining arrays immutably. For in-place modification, prefer push() or splice().

# Examples

```javascript
let a = [1,2,3];
a.concat(4, 5)           // => [1,2,3,4,5]
a.concat([4,5],[6,7])    // => [1,2,3,4,5,6,7]; arrays are flattened
a.concat(4, [5,[6,7]])   // => [1,2,3,4,5,[6,7]]; nested arrays not flattened
a                        // => [1,2,3]; the original array is unmodified
```
(Flanagan, p. 187)

# Relationships

## Builds Upon
- **array-fundamentals** — Method of Array.prototype

## Enables
- Immutable array combination

## Related
- **spread-operator-in-arrays** — Alternative way to combine arrays

## Contrasts With
- **push-pop-shift-unshift** — push() modifies in place; concat() creates new array

# Common Errors

- **Error**: Expecting concat() to deeply flatten nested arrays.
  **Correction**: concat() only flattens one level of array arguments.

# Common Confusions

- **Confusion**: concat() is efficient for repeated accumulation (`a = a.concat(x)`).
  **Clarification**: This pattern creates a new copy each time. Consider push() or splice() for in-place modification.

# Source Reference

Chapter 7: Arrays, Section 7.8.3, page 187.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented
- Uncertainties: None
- Cross-reference status: Verified
