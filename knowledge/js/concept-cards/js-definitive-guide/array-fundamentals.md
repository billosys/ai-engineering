---
# === CORE IDENTIFICATION ===
concept: Array Fundamentals
slug: array-fundamentals

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
pdf_page: 172
section: "7 (introduction)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "JavaScript arrays"
  - "Array type"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - array-literals
  - sparse-arrays
  - array-length
  - array-like-objects
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the basic characteristics of JavaScript arrays?"
---

# Quick Definition

An array is an ordered collection of values where each value (element) has a numeric position (index). JavaScript arrays are untyped, zero-based, dynamic, and may be sparse.

# Core Definition

"An array is an ordered collection of values. Each value is called an element, and each element has a numeric position in the array, known as its index. JavaScript arrays are untyped: an array element may be of any type, and different elements of the same array may be of different types." Arrays are "zero-based and use 32-bit indexes: the index of the first element is 0, and the highest possible index is 4294967294 (2^32-2)." They are "dynamic: they grow or shrink as needed" and may be "sparse: the elements need not have contiguous indexes." (Flanagan, p. 172)

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. **Untyped** — elements may be of any type, including objects and other arrays
2. **Zero-based** — first element is at index 0
3. **Dynamic** — grow or shrink as needed without preallocation
4. **Sparse** — elements need not have contiguous indexes
5. **32-bit indexes** — maximum size of 4,294,967,295 elements
6. **Specialized objects** — array indexes are really property names that happen to be integers

# Construction / Recognition

Arrays can be created via array literals, the spread operator, the Array() constructor, or Array.of()/Array.from() factory methods.

# Context & Application

Arrays are a fundamental datatype used in virtually all JavaScript programs for ordered collections of data. They inherit methods from Array.prototype.

# Examples

```javascript
let empty = [];                  // An array with no elements
let primes = [2, 3, 5, 7, 11];  // An array with 5 numeric elements
let misc = [1.1, true, "a"];     // 3 elements of various types
```
(Flanagan, p. 172)

# Relationships

## Builds Upon
- No prerequisites within this source.

## Enables
- **array-literals** — Primary way to create arrays
- **array-methods** — Rich set of methods inherited from Array.prototype
- **array-iteration** — Multiple ways to iterate through array elements

## Related
- **array-like-objects** — Objects that behave like arrays but aren't true arrays

## Contrasts With
- None within this scope.

# Common Errors

- **Error**: Assuming arrays have a fixed size that must be declared upfront.
  **Correction**: JavaScript arrays are dynamic and grow/shrink automatically.

# Common Confusions

- **Confusion**: Arrays are a distinct type separate from objects.
  **Clarification**: Arrays are a specialized form of JavaScript object; array indexes are really property names that happen to be integers.

# Source Reference

Chapter 7: Arrays, introduction, pages 172-173.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Opening definition of the chapter; clearly stated
- Uncertainties: None
- Cross-reference status: Verified
