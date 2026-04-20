---
# === CORE IDENTIFICATION ===
concept: "Object.assign() for Copying"
slug: object-assign

# === CLASSIFICATION ===
category: data-management
subcategory: copying
tier: foundational

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Copying objects and Arrays"
chapter_number: 7
section: "Shallow copying via Object.assign() (optional)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Object.assign shallow copy"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - shallow-copy
extends: []
related:
  - spreading-objects
  - property-descriptor-copying
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do shallow copies relate to deep copies?"
---

# Quick Definition

`Object.assign({}, original)` creates a shallow copy of an object, working similarly to spreading but using assignment rather than definition to create properties.

# Core Definition

As described in "Deep JavaScript" Ch 7, Section 7.2.2: "`Object.assign()` works mostly like spreading into objects." The key difference is that `Object.assign()` uses property *assignment* to create properties in the target, while spreading uses property *definition*. Assignment invokes inherited setters; definition does not. The two approaches are "mostly equivalent" for typical use cases.

# Prerequisites

- **Shallow copy** -- `Object.assign()` performs shallow copying
- **Spreading objects** -- the primary alternative to `Object.assign()` for copying

# Key Properties

1. Creates a shallow copy, like spreading.
2. Uses property *assignment* (not definition) to create target properties.
3. Assignment invokes own and inherited setters.
4. Can be polyfilled on older JavaScript engines.
5. `Object.assign({}, original)` is mostly equivalent to `{...original}`.

# Construction / Recognition

## To Construct/Create:
1. `const copy = Object.assign({}, original);`

## To Identify/Recognize:
1. `Object.assign()` with an empty object as the first argument is a copy operation.

# Context & Application

`Object.assign()` was the standard way to shallow-copy objects before spreading syntax was introduced. It remains useful for environments that don't support spreading or when its assignment semantics are desired.

# Examples

**Example 1** (Ch 7): Equivalent copying:
```js
const copy1 = {...original};
const copy2 = Object.assign({}, original);
```

**Example 2** (Ch 7): Subtle difference with `__proto__`:
```js
const original = {['__proto__']: null};

const copy1 = {...original};
// copy1 has the own property '__proto__'
assert.deepEqual(Object.keys(copy1), ['__proto__']);

const copy2 = Object.assign({}, original);
// copy2 has the prototype null (setter was invoked)
assert.equal(Object.getPrototypeOf(copy2), null);
```

# Relationships

## Builds Upon
- **Shallow copy** -- `Object.assign()` is a shallow copy mechanism

## Enables
- **Polyfillable copying** -- usable in older engines via library polyfills

## Related
- **Spreading objects** -- the more modern, concise alternative
- **Property descriptor copying** -- the most faithful copying approach

## Contrasts With
(none at this specificity)

# Common Errors

- **Error**: Assuming `Object.assign()` and spreading are always identical.
  **Correction**: They differ in how properties are created (assignment vs definition), which can matter when inherited setters exist.

# Common Confusions

- **Confusion**: `Object.assign()` performs deep copying.
  **Clarification**: Like spreading, `Object.assign()` only performs shallow copying. Nested objects remain shared.

# Source Reference

Chapter 7: "Copying objects and Arrays", Section 7.2.2, lines 3158-3320.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit comparison with spreading provided in source including edge case.
- Cross-reference status: verified against Ch 7 section 7.2.2
