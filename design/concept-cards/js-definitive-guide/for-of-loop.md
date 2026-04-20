---
# === CORE IDENTIFICATION ===
concept: for/of Loop
slug: for-of-loop

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: statements
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Statements"
chapter_number: 5
pdf_page: 125
section: "5.4.4 for/of"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "for-of loop"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - for-loop
extends: []
related:
  - for-in-loop
  - enumerating-properties
contrasts_with:
  - for-in-loop
  - for-loop

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Object.keys() from for/in?"
---

# Quick Definition

The `for/of` loop (ES6) iterates over the values of any iterable object (arrays, strings, Sets, Maps), assigning each value to the loop variable in turn.

# Core Definition

"ES6 defines a new loop statement: for/of. This new kind of loop uses the for keyword but is a completely different kind of loop than the regular for loop." It works with *iterable* objects: "arrays, strings, sets, and maps are iterable: they represent a sequence or set of elements that you can loop or iterate through using a for/of loop." (Ch. 5, §5.4.4)

# Prerequisites

- **for-loop** — `for/of` uses the `for` keyword but with different semantics.

# Key Properties

1. Works with any iterable: arrays, strings, Sets, Maps, and custom iterables.
2. Array elements are iterated in order from first to last.
3. Arrays are iterated "live" — modifications during iteration affect the outcome.
4. Objects are NOT iterable by default; `for/of` on a plain object throws TypeError.
5. Use `Object.keys()`, `Object.values()`, or `Object.entries()` to iterate object properties with `for/of`.
6. Strings are iterated by Unicode codepoint, not UTF-16 character.
7. Maps iterate key/value pairs; destructuring can unpack them: `for(let [k,v] of map)`.

# Construction / Recognition

```js
for (let variable of iterable)
    statement
```

# Context & Application

`for/of` is the preferred loop for iterating arrays and other iterable collections in modern JavaScript. Combined with `Object.keys()`, it is the recommended alternative to `for/in` for objects.

# Examples

From the source text (§5.4.4, pp. 125-128):

```js
let data = [1, 2, 3, 4, 5, 6, 7, 8, 9], sum = 0;
for(let element of data) {
    sum += element;
}
sum // => 45

// Iterating object properties via Object.keys()
let o = { x: 1, y: 2, z: 3 };
for(let k of Object.keys(o)) {
    // k is "x", "y", "z"
}

// Object.entries() with destructuring
for(let [k, v] of Object.entries(o)) {
    // k is key, v is value
}

// Strings iterate by Unicode codepoint
let frequency = {};
for(let letter of "mississippi") {
    if (frequency[letter]) frequency[letter]++;
    else frequency[letter] = 1;
}
// frequency => {m: 1, i: 4, s: 4, p: 2}
```

# Relationships

## Builds Upon
- **for-loop** — Uses `for` keyword but with iterable semantics

## Enables
- Modern idiomatic iteration over collections

## Related
- **enumerating-properties** — `for/of` with `Object.keys()` is the preferred way to enumerate

## Contrasts With
- **for-in-loop** — `for/in` iterates property names (including inherited); `for/of` iterates values
- **for-loop** — `for` uses numeric indices; `for/of` uses the iterable protocol

# Common Errors

- **Error**: Using `for/of` directly on a plain object.
  **Correction**: Plain objects are not iterable. Use `for/of` with `Object.keys(o)`, `Object.values(o)`, or `Object.entries(o)`.

# Common Confusions

- **Confusion**: Confusing `for/of` with `for/in`.
  **Clarification**: `for/of` iterates *values* of iterables; `for/in` iterates *property names* of objects (including inherited enumerable properties).

# Source Reference

Chapter 5: Statements, Section 5.4.4, pages 125-128.

# Verification Notes

- Definition source: Direct quote from §5.4.4
- Confidence rationale: High — extensive coverage with multiple data type examples
- Uncertainties: None
- Cross-reference status: Verified against §6.6
