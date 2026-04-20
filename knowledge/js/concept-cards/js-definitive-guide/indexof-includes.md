---
# === CORE IDENTIFICATION ===
concept: indexOf(), lastIndexOf(), and includes()
slug: indexof-includes

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
pdf_page: 191
section: "7.8.6 Array Searching and Sorting Methods"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
extends: []
related:
  - find-and-findindex
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I check if a value exists in an array?"
---

# Quick Definition

`indexOf()` and `lastIndexOf()` search for a value using `===` and return its index (or -1). `includes()` (ES2016) returns a boolean and correctly handles NaN.

# Core Definition

"indexOf() and lastIndexOf() search an array for an element with a specified value and return the index of the first such element found, or -1 if none is found." They use `===` comparison. "The ES2016 includes() method takes a single argument and returns true if the array contains that value." includes() "uses a slightly different version of equality that does consider NaN to be equal to itself." (Flanagan, p. 191-192)

# Prerequisites

- **array-fundamentals** — Must understand arrays

# Key Properties

1. indexOf() searches beginning to end; lastIndexOf() searches end to beginning
2. Both use `===` equality (cannot find NaN)
3. includes() uses a NaN-aware equality check
4. Optional second argument specifies starting search index
5. All search for specific values (not predicates; use find/findIndex for predicates)

# Construction / Recognition

```javascript
array.indexOf(value)
array.lastIndexOf(value)
array.includes(value)
```

# Context & Application

Use includes() for set membership testing. Use indexOf() when you need the position. Use find()/findIndex() for predicate-based searches.

# Examples

```javascript
let a = [0,1,2,1,0];
a.indexOf(1)       // => 1
a.lastIndexOf(1)   // => 3
a.indexOf(3)       // => -1

let a = [1,true,3,NaN];
a.includes(true)   // => true
a.includes(NaN)    // => true
a.indexOf(NaN)     // => -1; indexOf can't find NaN
```
(Flanagan, p. 191-192)

# Relationships

## Builds Upon
- **array-fundamentals** — Methods of Array.prototype

## Enables
- Value-based array searching

## Related
- **find-and-findindex** — Predicate-based search (more flexible)

## Contrasts With
- None specific

# Common Errors

- **Error**: Using indexOf() to check for NaN.
  **Correction**: indexOf() uses `===` which considers NaN !== NaN. Use includes() instead.

# Common Confusions

- **Confusion**: indexOf() and includes() use the same equality algorithm.
  **Clarification**: indexOf() uses `===`; includes() uses a variant that treats NaN as equal to itself.

# Source Reference

Chapter 7: Arrays, Section 7.8.6, pages 191-193.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly documented
- Uncertainties: None
- Cross-reference status: Verified
