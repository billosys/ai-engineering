---
# === CORE IDENTIFICATION ===
concept: find() and findIndex()
slug: find-and-findindex

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
section: "7.8.1 Array Iterator Methods - find() and findIndex()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
  - filter-method
extends: []
related:
  - indexof-includes
  - every-and-some
contrasts_with:
  - filter-method

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I find a specific element in an array based on a condition?"
---

# Quick Definition

`find()` returns the first element for which a predicate returns truthy (or `undefined` if none); `findIndex()` returns the index of that element (or -1 if none). Both stop iterating on the first match.

# Core Definition

"The find() and findIndex() methods are like filter() in that they iterate through your array looking for elements for which your predicate function returns a truthy value. Unlike filter(), however, these two methods stop iterating the first time the predicate finds an element." (Flanagan, p. 184)

# Prerequisites

- **array-fundamentals** — Must understand arrays
- **filter-method** — find/findIndex are like filter but stop at first match

# Key Properties

1. Stop on first matching element (short-circuit)
2. find() returns the element value; findIndex() returns the index
3. find() returns `undefined` if no match; findIndex() returns -1
4. Predicate receives (value, index, array)

# Construction / Recognition

```javascript
let element = array.find(predicate);
let index = array.findIndex(predicate);
```

# Context & Application

Use when you need the first element matching a condition, rather than all matches (which filter() provides).

# Examples

```javascript
let a = [1,2,3,4,5];
a.findIndex(x => x === 3)  // => 2
a.findIndex(x => x < 0)    // => -1
a.find(x => x % 5 === 0)   // => 5
a.find(x => x % 7 === 0)   // => undefined
```
(Flanagan, p. 184)

# Relationships

## Builds Upon
- **array-fundamentals** — Method of Array.prototype
- **filter-method** — Same predicate pattern but returns only first match

## Enables
- Efficient single-element lookup by condition

## Related
- **indexof-includes** — Value-based search (equality) vs. predicate-based
- **every-and-some** — Also use predicates with short-circuit behavior

## Contrasts With
- **filter-method** — filter returns all matches; find returns only the first

# Common Errors

- **Error**: Using filter() when only the first match is needed.
  **Correction**: Use find() or findIndex() for better performance when only one result is needed.

# Common Confusions

- **Confusion**: findIndex() and indexOf() are the same.
  **Clarification**: findIndex() takes a predicate function; indexOf() searches for a specific value using ===.

# Source Reference

Chapter 7: Arrays, Section 7.8.1, page 184.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented
- Uncertainties: None
- Cross-reference status: Verified
