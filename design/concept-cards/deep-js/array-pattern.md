---
# === CORE IDENTIFICATION ===
concept: Array Pattern
slug: array-pattern

# === CLASSIFICATION ===
category: language-mechanics
subcategory: destructuring
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "The destructuring algorithm"
chapter_number: 3
section: "3.2.4 Rules for Array patterns"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - array destructuring pattern

# === TYPED RELATIONSHIPS ===
prerequisites:
  - destructuring-assignment
  - pattern-matching-algorithm
extends:
  - destructuring-assignment
related:
  - object-pattern
  - rest-element
  - default-values-in-destructuring
  - nested-destructuring
contrasts_with:
  - object-pattern

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is destructuring in JavaScript?"
  - "How do I destructure nested objects and arrays?"
---

# Quick Definition

An array pattern is a destructuring pattern that uses `[«elements»]` syntax to match against iterables, extracting values by position using the iteration protocol.

# Core Definition

As described in "Deep JavaScript" (Ch 3, Section 3.2.4): Array pattern destructuring begins by checking if the value is iterable (rule 3a throws `TypeError` if not). If iterable (rule 3b), an iterator is obtained via `iterable[Symbol.iterator]()`. Then elements are matched against iterator values: rule 3c for normal elements, rule 3d for elements with defaults, rule 3e for holes/elisions, rule 3f for rest elements (`...pattern`), and rule 3g terminates when no elements remain. "An iterator being finished is similar to missing properties in objects."

# Prerequisites

- **Destructuring assignment** — Array patterns are a type of destructuring.
- **Pattern matching algorithm** — Rules 3a-3g govern array patterns.

# Key Properties

1. Works with any **iterable**, not just arrays.
2. Throws `TypeError` for non-iterables (rule 3a).
3. Creates an iterator and advances it element by element.
4. Supports default values (rule 3d): used when iterator value is `undefined`.
5. Supports holes/elisions (rule 3e): skips an iterator value.
6. Supports rest elements `...pattern` (rule 3f): collects remaining values.
7. Exhausted iterators produce `undefined` (like missing object properties).

# Construction / Recognition

## To Construct/Create:
1. Use `[]` with elements on the left side of an assignment.
2. Elements can be variables, nested patterns, defaults, holes, or rest elements.

## To Identify/Recognize:
1. Square brackets on the left side of `=`, in a declaration, or in a parameter list.

# Context & Application

Array patterns are used for extracting values from arrays, strings, Sets, Maps, and any other iterable. They are commonly used for swapping variables (`[a, b] = [b, a]`), extracting first/rest elements, and working with iterator results.

# Examples

**Example 1** (Ch 3): Rules for array patterns (key rules):
```
- (3a) [«elements»] ← non_iterable (if !isIterable) → throw TypeError
- (3b) [«elements»] ← iterable (if isIterable)
    const iterator = iterable[Symbol.iterator]();
    «elements» ← iterator
- (3c) «pattern», «elements» ← iterator
    «pattern» ← getNext(iterator)
    «elements» ← iterator
- (3f) ...«pattern» ← iterator  (always last!)
    const tmp = [];
    for (const elem of iterator) { tmp.push(elem); }
    «pattern» ← tmp
```

**Example 2** (Ch 3): Empty array pattern as guard:
```js
const [] = 'abc'; // OK, iterable
assert.throws(
  () => { const [] = 123; },  // not iterable
  /^TypeError: 123 is not iterable$/);
```

**Example 3** (Ch 3): Helper function for iterator advancement:
```js
function getNext(iterator) {
  const {done, value} = iterator.next();
  return (done ? undefined : value);
}
```

# Relationships

## Builds Upon
- **Destructuring assignment** — Array patterns are a type of destructuring.
- **Pattern matching algorithm** — Rules 3a-3g govern array patterns.

## Enables
- **Rest element** — Rule 3f implements rest element collection.
- **Nested destructuring** — Array elements can be nested patterns.
- **Default values in destructuring** — Rule 3d adds default value support.

## Related
- **Iteration protocol** — Array patterns depend on `Symbol.iterator`.

## Contrasts With
- **Object pattern** — Object patterns access by key; array patterns access by position via iteration.

# Common Errors

- **Error**: Assuming array patterns only work with arrays.
  **Correction**: Array patterns work with any iterable (strings, Sets, Maps, generators, etc.).

- **Error**: Destructuring a non-iterable value like a number.
  **Correction**: `const [x] = 123` throws `TypeError` because numbers are not iterable.

# Common Confusions

- **Confusion**: Array patterns use numeric indices like `arr[0]`.
  **Clarification**: Array patterns use the iteration protocol, advancing through an iterator one element at a time. They do not use index-based access.

# Source Reference

Chapter 3: The destructuring algorithm, Section 3.2.4, lines 226-317.

# Verification Notes

- Definition source: direct (rules quoted from source)
- Confidence rationale: Complete rule set provided with helper functions
- Cross-reference status: verified
