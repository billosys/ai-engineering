---
# === CORE IDENTIFICATION ===
concept: Array-Like Objects
slug: array-like-objects

# === CLASSIFICATION ===
category: arrays
subcategory: array-like objects
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Arrays"
chapter_number: 7
pdf_page: 194
section: "7.9 Array-Like Objects"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "pseudo-arrays"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
  - array-from
extends: []
related:
  - array-isarray
  - call-and-apply
contrasts_with:
  - array-fundamentals

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an array-like object and how do I work with it?"
---

# Quick Definition

An array-like object is any object with a numeric `length` property and corresponding nonnegative integer properties, but without inheriting from Array.prototype -- common in DOM APIs.

# Core Definition

Objects with "a numeric length property and corresponding non-negative integer properties" can be treated as arrays. "These 'array-like' objects actually do occasionally appear in practice, and although you cannot directly invoke array methods on them or expect special behavior from the length property, you can still iterate through them." Array methods can be invoked on them via `Function.call`, or they can be converted to true arrays via `Array.from()`. (Flanagan, p. 194-196)

# Prerequisites

- **array-fundamentals** — Must understand true arrays for contrast
- **array-from** — Primary way to convert array-like objects to arrays

# Key Properties

1. Have a numeric `length` property
2. Have integer-indexed properties (0, 1, 2, ...)
3. Do NOT inherit from Array.prototype
4. Cannot use array methods directly
5. Can be converted with `Array.from()`
6. Array methods can be called on them via `Array.prototype.method.call()`

# Construction / Recognition

```javascript
// Test function for array-like objects:
function isArrayLike(o) {
    if (o && typeof o === "object" && Number.isFinite(o.length) &&
        o.length >= 0 && Number.isInteger(o.length) && o.length < 4294967295) {
        return true;
    }
    return false;
}
```

# Context & Application

DOM methods like `document.querySelectorAll()` return array-like objects. The `arguments` object is array-like. Converting them to true arrays with `Array.from()` makes them easier to work with.

# Examples

```javascript
let a = {"0": "a", "1": "b", "2": "c", length: 3};  // array-like
Array.prototype.join.call(a, "+")                      // => "a+b+c"
Array.prototype.map.call(a, x => x.toUpperCase())     // => ["A","B","C"]
Array.prototype.slice.call(a, 0)                       // => ["a","b","c"]
Array.from(a)                                          // => ["a","b","c"] (easier)
```
(Flanagan, p. 195-196)

# Relationships

## Builds Upon
- **array-fundamentals** — Mimics array structure without being a true array
- **array-from** — Array.from() converts array-like objects to true arrays

## Enables
- Working with DOM API return values
- Working with the arguments object

## Related
- **array-isarray** — Returns false for array-like objects
- **call-and-apply** — Used to invoke array methods on array-like objects

## Contrasts With
- **array-fundamentals** — True arrays inherit from Array.prototype; array-like objects don't

# Common Errors

- **Error**: Calling array methods directly on array-like objects.
  **Correction**: Convert with Array.from() first, or use Array.prototype.method.call().

# Common Confusions

- **Confusion**: Array-like objects are arrays.
  **Clarification**: They lack Array.prototype methods and the special length behavior of true arrays.

# Source Reference

Chapter 7: Arrays, Section 7.9, pages 194-196.

# Verification Notes

- Definition source: Synthesized from source text
- Confidence rationale: Well-documented with examples and test function
- Uncertainties: None
- Cross-reference status: Verified
