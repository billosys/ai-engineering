---
# === CORE IDENTIFICATION ===
concept: Array() Constructor
slug: array-constructor

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
pdf_page: 174
section: "7.1.3 The Array() Constructor"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "new Array()"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
extends: []
related:
  - array-of
  - array-from
contrasts_with:
  - array-literals

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create arrays in JavaScript?"
---

# Quick Definition

The Array() constructor creates arrays and can be invoked with no arguments (empty array), a single numeric argument (preallocated length), or multiple arguments (elements).

# Core Definition

The Array() constructor has three invocation modes: with no arguments it creates an empty array; with a single numeric argument it creates an array with that length but no elements; with two or more arguments (or one non-numeric) those arguments become the array elements. "Using an array literal is almost always simpler than this usage of the Array() constructor." (Flanagan, p. 174-175)

# Prerequisites

- **array-fundamentals** — Must understand array basics

# Key Properties

1. `new Array()` creates empty array equivalent to `[]`
2. `new Array(10)` creates array with length 10 but no defined elements
3. `new Array(5, 4, 3)` creates `[5, 4, 3]`
4. Single numeric argument is ambiguous (length vs. element)

# Construction / Recognition

```javascript
let a = new Array();           // []
let b = new Array(10);         // length 10, no elements
let c = new Array(5, 4, 3, 2, 1, "testing");  // [5,4,3,2,1,"testing"]
```

# Context & Application

Mainly used when preallocating array length. Array literals are preferred in most cases.

# Examples

```javascript
let a = new Array();    // equivalent to []
let a = new Array(10);  // length 10, no values stored
let a = new Array(5, 4, 3, 2, 1, "testing, testing");
```
(Flanagan, p. 174-175)

# Relationships

## Builds Upon
- **array-fundamentals** — Creates array instances

## Enables
- **array-of** — Array.of() was created to fix the constructor's single-argument ambiguity

## Related
- **array-from** — Another factory method for creating arrays

## Contrasts With
- **array-literals** — Literals are simpler and preferred

# Common Errors

- **Error**: Using `new Array(10)` expecting an array containing the number 10.
  **Correction**: A single numeric argument sets the length, not the content. Use `Array.of(10)` for an array containing the element 10.

# Common Confusions

- **Confusion**: `new Array(10)` creates an array with 10 undefined elements.
  **Clarification**: It creates a sparse array with length 10 but no defined index properties ("0", "1", etc. are not defined).

# Source Reference

Chapter 7: Arrays, Section 7.1.3, pages 174-175.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Clearly stated with examples
- Uncertainties: None
- Cross-reference status: Verified
