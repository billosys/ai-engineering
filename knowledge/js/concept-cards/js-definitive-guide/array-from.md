---
# === CORE IDENTIFICATION ===
concept: Array.from()
slug: array-from

# === CLASSIFICATION ===
category: arrays
subcategory: array creation
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Arrays"
chapter_number: 7
pdf_page: 175
section: "7.1.5 Array.from()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
extends: []
related:
  - array-of
  - array-like-objects
  - spread-operator-in-arrays
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I convert an array-like object to a true array?"
---

# Quick Definition

Array.from() is an ES6 factory method that creates a new array from an iterable or array-like object, with an optional mapping function applied during creation.

# Core Definition

"Array.from is another array factory method introduced in ES6. It expects an iterable or array-like object as its first argument and returns a new array that contains the elements of that object." It also "accepts an optional second argument. If you pass a function as the second argument, then as the new array is being built, each element from the source object will be passed to the function you specify, and the return value of the function will be stored in the array instead of the original value." (Flanagan, p. 175-176)

# Prerequisites

- **array-fundamentals** — Must understand arrays

# Key Properties

1. Accepts iterables or array-like objects as first argument
2. Optional mapping function as second argument (more efficient than separate map)
3. Creates true array copies from array-like objects
4. ES6 addition

# Construction / Recognition

```javascript
let copy = Array.from(original);
let truearray = Array.from(arraylike);
let mapped = Array.from(source, mappingFn);
```

# Context & Application

Critical for converting array-like objects (e.g., DOM NodeLists, arguments objects) to true arrays. Also useful for copying arrays with a simultaneous transformation.

# Examples

```javascript
let copy = Array.from(original);      // copy an array
let truearray = Array.from(arraylike); // convert array-like to true array
```
(Flanagan, p. 175-176)

# Relationships

## Builds Upon
- **array-fundamentals** — Creates array instances

## Enables
- Working with array-like objects using array methods

## Related
- **array-like-objects** — Primary use case is converting these to true arrays
- **spread-operator-in-arrays** — `Array.from(iterable)` works like `[...iterable]`

## Contrasts With
- None specific

# Common Errors

- **Error**: Using Array.from() only for copying when spread would suffice.
  **Correction**: Array.from() shines when converting array-like (non-iterable) objects or when using the mapping function for efficiency.

# Common Confusions

- **Confusion**: Array.from() and the spread operator are identical.
  **Clarification**: Array.from() also works with array-like objects that are not iterable, whereas spread requires iterables.

# Source Reference

Chapter 7: Arrays, Section 7.1.5, pages 175-176.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Well-documented with clear examples
- Uncertainties: None
- Cross-reference status: Verified
