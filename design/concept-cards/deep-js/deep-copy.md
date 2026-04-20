---
# === CORE IDENTIFICATION ===
concept: Deep Copy
slug: deep-copy

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
  - "deep clone"
  - "recursive copy"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - shallow-copy
extends:
  - shallow-copy
related:
  - nested-spreading-deep-copy
  - json-deep-copy
  - generic-deep-copy
contrasts_with:
  - shallow-copy

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do shallow copies relate to deep copies?"
  - "How do I create a deep copy of an object?"
  - "What distinguishes shallow copying from deep copying?"
---

# Quick Definition

Deep copying duplicates an entire object tree, recursively copying all nested values so that the original and copy share no references.

# Core Definition

As described in "Deep JavaScript" Ch 7, Section 7.1: "Deep copying also copies the entries of the values of the entries, etc. That is, it traverses the complete tree whose root is the value to be copied and makes copies of all nodes." JavaScript does not have built-in support for deep copying; it must be implemented manually.

# Prerequisites

- **Shallow copy** -- understanding what shallow copy does and doesn't copy
- **Object references** -- understanding reference sharing in nested structures

# Key Properties

1. Recursively copies all levels of nesting.
2. Original and copy share no object references.
3. Modifying nested values in the copy does not affect the original.
4. JavaScript has no built-in deep copy (must be implemented).
5. Implementing generic deep copy is generally impossible for all cases (prototypes, special objects, non-enumerable properties, circular references).

# Construction / Recognition

## To Construct/Create:
1. Use nested spreading for known structures.
2. Use `JSON.parse(JSON.stringify(obj))` as a hack (with limitations).
3. Implement a recursive deep copy function.
4. Use `structuredClone()` (modern environments).

## To Identify/Recognize:
1. After deep copying, `copy.nested !== original.nested` for all nested objects.
2. Modifying any level of the copy leaves the original unchanged.

# Context & Application

Deep copying is needed when you have nested data structures and need a fully independent copy. It is essential for avoiding shared mutable state with complex objects.

# Examples

**Example 1** (Ch 7): Verifying deep independence:
```js
const original = {a: 1, b: {c: 2, d: {e: 3}}};
const copy = deepCopy(original);

assert.deepEqual(copy, original);
assert.ok(copy     !== original);
assert.ok(copy.b   !== original.b);
assert.ok(copy.b.d !== original.b.d);
```

# Relationships

## Builds Upon
- **Shallow copy** -- deep copy extends shallow copy to all nesting levels

## Enables
- **Defensive copying** -- deep copies provide full isolation from shared mutable state

## Related
- **Nested spreading deep copy** -- manual approach for known structures
- **JSON deep copy** -- hack-based approach with limitations
- **Generic deep copy** -- recursive implementation

## Contrasts With
- **Shallow copy** -- shallow copy only duplicates top-level entries

# Common Errors

- **Error**: Assuming `{...obj}` produces a deep copy.
  **Correction**: Spreading is always shallow. Use nested spreading, JSON round-tripping, or a recursive function for deep copies.

# Common Confusions

- **Confusion**: Deep copy can handle any JavaScript value.
  **Clarification**: Generic deep copy has limitations: prototypes may not be copied, special objects (Date, RegExp) may lose data, and non-enumerable properties are typically ignored.

# Source Reference

Chapter 7: "Copying objects and Arrays", Sections 7.1 and 7.3, lines 3158-3510.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition in source section 7.1 with detailed implementation in 7.3.
- Cross-reference status: verified against Ch 7 sections 7.1 and 7.3
