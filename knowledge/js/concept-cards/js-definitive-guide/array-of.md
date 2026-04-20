---
# === CORE IDENTIFICATION ===
concept: Array.of()
slug: array-of

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
section: "7.1.4 Array.of()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-constructor
extends: []
related:
  - array-from
contrasts_with:
  - array-constructor

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create an array with a single numeric element?"
---

# Quick Definition

Array.of() is an ES6 factory method that creates a new array using its arguments as elements, regardless of how many there are, solving the Array() constructor's single-numeric-argument ambiguity.

# Core Definition

"In ES6, the Array.of() function addresses this problem: it is a factory method that creates and returns a new array, using its argument values (regardless of how many of them there are) as the array elements." (Flanagan, p. 175)

# Prerequisites

- **array-constructor** — Array.of() exists to fix the constructor's ambiguity

# Key Properties

1. Always treats arguments as elements, never as a length
2. ES6 addition
3. Factory method (static method on Array)

# Construction / Recognition

```javascript
Array.of()        // => []
Array.of(10)      // => [10]
Array.of(1,2,3)   // => [1, 2, 3]
```

# Context & Application

Use when you need to create an array from arguments and cannot be sure whether a single numeric argument is intended as an element.

# Examples

```javascript
Array.of()        // => []; returns empty array with no arguments
Array.of(10)      // => [10]; creates array with single numeric element
Array.of(1,2,3)   // => [1, 2, 3]
```
(Flanagan, p. 175)

# Relationships

## Builds Upon
- **array-constructor** — Solves the constructor's ambiguity problem

## Enables
- None specific

## Related
- **array-from** — Another static factory method for arrays

## Contrasts With
- **array-constructor** — `new Array(10)` creates length-10 array; `Array.of(10)` creates `[10]`

# Common Errors

- **Error**: Using `new Array(n)` when you want an array containing the number `n`.
  **Correction**: Use `Array.of(n)` instead.

# Common Confusions

- **Confusion**: Array.of() is the same as Array().
  **Clarification**: They differ when called with a single numeric argument.

# Source Reference

Chapter 7: Arrays, Section 7.1.4, page 175.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Concise, clearly stated
- Uncertainties: None
- Cross-reference status: Verified
