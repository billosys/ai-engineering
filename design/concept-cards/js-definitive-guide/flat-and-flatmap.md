---
# === CORE IDENTIFICATION ===
concept: flat() and flatMap()
slug: flat-and-flatmap

# === CLASSIFICATION ===
category: arrays
subcategory: array methods
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Arrays"
chapter_number: 7
pdf_page: 186
section: "7.8.2 Flattening arrays with flat() and flatMap()"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "flatMap method"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - array-fundamentals
  - map-method
extends:
  - map-method
related:
  - concat-method
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I flatten nested arrays in JavaScript?"
---

# Quick Definition

`flat()` creates a new array with nested arrays flattened to a specified depth (default 1). `flatMap()` maps each element then flattens the result by one level, equivalent to `a.map(f).flat()` but more efficient.

# Core Definition

"In ES2019, the flat() method creates and returns a new array that contains the same elements as the array it is called on, except that any elements that are themselves arrays are 'flattened' into the returned array." Pass a numeric depth argument for deeper flattening. "The flatMap() method works just like the map() method except that the returned array is automatically flattened as if passed to flat()." (Flanagan, p. 186-187)

# Prerequisites

- **array-fundamentals** — Must understand arrays
- **map-method** — flatMap extends map with flattening

# Key Properties

1. flat() defaults to depth 1
2. flat(n) flattens n levels deep
3. flatMap(f) is equivalent to a.map(f).flat() but more efficient
4. flatMap allows one-to-many or one-to-zero element mappings

# Construction / Recognition

```javascript
array.flat()       // flatten one level
array.flat(n)      // flatten n levels
array.flatMap(fn)  // map then flatten one level
```

# Context & Application

flat() is useful for normalizing nested data. flatMap() is particularly powerful for operations where each input element maps to zero or more output elements.

# Examples

```javascript
[1, [2, 3]].flat()     // => [1, 2, 3]
[1, [2, [3]]].flat()   // => [1, 2, [3]]

let a = [1, [2, [3, [4]]]];
a.flat(1)   // => [1, 2, [3, [4]]]
a.flat(2)   // => [1, 2, 3, [4]]
a.flat(3)   // => [1, 2, 3, 4]

let phrases = ["hello world", "the definitive guide"];
let words = phrases.flatMap(phrase => phrase.split(" "));
words  // => ["hello", "world", "the", "definitive", "guide"]

// Map to empty array to filter:
[-2, -1, 1, 2].flatMap(x => x < 0 ? [] : Math.sqrt(x))  // => [1, 2**0.5]
```
(Flanagan, p. 186-187)

# Relationships

## Builds Upon
- **array-fundamentals** — Method of Array.prototype
- **map-method** — flatMap extends map

## Enables
- One-to-many and one-to-zero element transformations

## Related
- **concat-method** — Also flattens one level when concatenating arrays

## Contrasts With
- None specific

# Common Errors

- **Error**: Expecting flat() to deeply flatten by default.
  **Correction**: flat() only flattens one level by default. Pass Infinity for full flattening.

# Common Confusions

- **Confusion**: flatMap flattens to arbitrary depth.
  **Clarification**: flatMap only flattens one level, like flat() with no arguments.

# Source Reference

Chapter 7: Arrays, Section 7.8.2, pages 186-187.

# Verification Notes

- Definition source: Direct quote from source text
- Confidence rationale: Well-documented with examples
- Uncertainties: None
- Cross-reference status: Verified
