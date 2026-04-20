---
# === CORE IDENTIFICATION ===
concept: Shallow Copy
slug: shallow-copy

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
section: "Shallow copying vs. deep copying"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "shallow clone"
  - "top-level copy"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - spreading-objects
  - spreading-arrays
  - object-assign
  - property-descriptor-copying
contrasts_with:
  - deep-copy

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do shallow copies relate to deep copies?"
  - "What distinguishes shallow copying from deep copying?"
---

# Quick Definition

Shallow copying duplicates only the top-level entries of an object or Array; nested values are shared (referenced) between the original and the copy.

# Core Definition

As described in "Deep JavaScript" Ch 7, Section 7.1: "Shallow copying only copies the top-level entries of objects and Arrays. The entry values are still the same in original and copy." This means primitive values at the top level are effectively duplicated, but object/array values remain shared references. Modifying a nested object in the copy also modifies it in the original.

# Prerequisites

- **Object references** -- understanding that objects are accessed via references, not copied by value

# Key Properties

1. Only top-level properties/elements are duplicated.
2. Nested objects and arrays are shared between original and copy.
3. Changing a top-level property in the copy does not affect the original.
4. Changing a nested object's property in the copy DOES affect the original.
5. JavaScript has built-in support for shallow copying (spreading, `Object.assign()`).

# Construction / Recognition

## To Construct/Create:
1. Use spreading: `{...obj}` or `[...arr]`.
2. Use `Object.assign({}, obj)`.
3. Use `Object.defineProperties({}, Object.getOwnPropertyDescriptors(obj))` for faithful attribute copying.

## To Identify/Recognize:
1. After copying, `copy !== original` (different object identity).
2. But `copy.nested === original.nested` (nested values are the same reference).

# Context & Application

Shallow copying is the default copying behavior in JavaScript. It is sufficient when the data structure is flat (no nested objects) or when shared nested references are acceptable. For nested data that must be independently mutable, deep copying is required.

# Examples

**Example 1** (Ch 7): Shallow copy shares nested objects:
```js
const original = {name: 'Jane', work: {employer: 'Acme'}};
const copy = {...original};

// Top-level property: independent
copy.name = 'John';
assert.deepEqual(original, {name: 'Jane', work: {employer: 'Acme'}});

// Nested object: shared
copy.work.employer = 'Spectre';
assert.deepEqual(original, {name: 'Jane', work: {employer: 'Spectre'}});
```

# Relationships

## Builds Upon
- **Object references** -- shallow copy creates new references at the top level but shares nested references

## Enables
- **Defensive copying** -- shallow copies are often sufficient for defensive copying of flat structures

## Related
- **Spreading objects** -- one mechanism for shallow copying
- **Object.assign()** -- another mechanism for shallow copying

## Contrasts With
- **Deep copy** -- deep copy also duplicates nested values, producing fully independent copies

# Common Errors

- **Error**: Assuming a spread copy is fully independent from the original.
  **Correction**: Only top-level entries are independent. Nested objects are shared references.

# Common Confusions

- **Confusion**: Shallow copy means no copy is made at all.
  **Clarification**: A shallow copy does create a new top-level object/array. It just doesn't recursively copy nested structures.

# Source Reference

Chapter 7: "Copying objects and Arrays", Section 7.1, lines 3158-3200.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition quoted directly from source section 7.1.
- Cross-reference status: verified against Ch 7 section 7.1 and 7.2.1.6
