---
# === CORE IDENTIFICATION ===
concept: every() and some()
slug: every-and-some

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
section: "7.8.1 Array Iterator Methods - every() and some()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "array predicates"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
extends: []
related:
  - find-and-findindex
  - filter-method
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I test whether all or any elements of an array satisfy a condition?"
---

# Quick Definition

`every()` returns true if the predicate returns true for all elements (universal quantifier); `some()` returns true if the predicate returns true for at least one element (existential quantifier). Both short-circuit.

# Core Definition

"The every() method is like the mathematical 'for all' quantifier: it returns true if and only if your predicate function returns true for all elements in the array." "The some() method is like the mathematical 'there exists' quantifier: it returns true if there exists at least one element in the array for which the predicate returns true." Both stop early when the result is determined. "By mathematical convention, every() returns true and some returns false when invoked on an empty array." (Flanagan, p. 184-185)

# Prerequisites

- **array-fundamentals** — Must understand arrays

# Key Properties

1. every() short-circuits on first false; some() short-circuits on first true
2. On empty arrays: every() returns true; some() returns false
3. Predicate receives (value, index, array)

# Construction / Recognition

```javascript
array.every(predicate)
array.some(predicate)
```

# Context & Application

Used for validation, condition checking, and testing array properties before processing.

# Examples

```javascript
let a = [1,2,3,4,5];
a.every(x => x < 10)      // => true: all values are < 10
a.every(x => x % 2 === 0) // => false: not all values are even
a.some(x => x%2===0)      // => true; a has some even numbers
a.some(isNaN)              // => false; a has no non-numbers
```
(Flanagan, p. 184-185)

# Relationships

## Builds Upon
- **array-fundamentals** — Method of Array.prototype

## Enables
- Validation and precondition checks

## Related
- **find-and-findindex** — Similar short-circuit behavior with predicates
- **filter-method** — Returns matching elements instead of boolean

## Contrasts With
- None specific (every and some contrast with each other)

# Common Errors

- **Error**: Expecting every() to return false on an empty array.
  **Correction**: By mathematical convention, every() returns true on an empty array (vacuous truth).

# Common Confusions

- **Confusion**: every() iterates all elements even after finding a false result.
  **Clarification**: every() short-circuits on the first false; some() short-circuits on the first true.

# Source Reference

Chapter 7: Arrays, Section 7.8.1, pages 184-185.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented
- Uncertainties: None
- Cross-reference status: Verified
