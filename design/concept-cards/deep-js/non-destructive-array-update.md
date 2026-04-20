---
# === CORE IDENTIFICATION ===
concept: Non-Destructive Array Element Update
slug: non-destructive-array-update

# === CLASSIFICATION ===
category: data-management
subcategory: mutation
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Updating data destructively and non-destructively"
chapter_number: 8
section: "Examples: updating an Array destructively and non-destructively"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "immutable array update"
  - "array element replacement without mutation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - non-destructive-update
  - spreading-arrays
extends:
  - non-destructive-update
related:
  - spreading-for-non-destructive-updates
  - destructive-update
contrasts_with:
  - destructive-update

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does destructive updating differ from non-destructive updating?"
---

# Quick Definition

A non-destructive array element update replaces an element at a given index by constructing a new array from slices of the original, leaving the original array unchanged.

# Core Definition

As described in "Deep JavaScript" Ch 8, Section 8.2, non-destructive array updates produce a new array with the desired modification while leaving the original intact. The source shows two approaches: (1) iterating with `.entries()` and conditionally replacing the target index, and (2) using `.slice()` and spreading to construct a new array from the portions before and after the target index. Both are described as "shallow" -- only the top level is new.

# Prerequisites

- **Non-destructive update** -- the general concept this applies to arrays
- **Spreading arrays** -- the syntax mechanism for the concise version

# Key Properties

1. Produces a new array; the original is unchanged.
2. The concise pattern is `[...arr.slice(0, index), value, ...arr.slice(index+1)]`.
3. The update is shallow -- elements are copied by reference.
4. More verbose than destructive update (`arr[index] = value`) but safer for shared data.

# Construction / Recognition

## To Construct/Create:
1. Verbose: iterate with `.entries()`, push original or replacement conditionally.
2. Concise: `[...arr.slice(0, index), value, ...arr.slice(index+1)]`.

## To Identify/Recognize:
1. The `.slice()` + spread pattern in an array literal.
2. A new array variable assigned the result; the original array is unchanged.

# Context & Application

Used in React state updates and Redux reducers when array elements need to change without mutation. The `.slice()` + spread pattern is the standard idiom.

# Examples

**Example 1** (Ch 8): Verbose non-destructive array update:
```js
function setElementNonDestructively(arr, index, value) {
  const updatedArr = [];
  for (const [i, v] of arr.entries()) {
    updatedArr.push(i === index ? value : v);
  }
  return updatedArr;
}

const arr = ['a', 'b', 'c', 'd', 'e'];
const updatedArr = setElementNonDestructively(arr, 2, 'x');
assert.deepEqual(updatedArr, ['a', 'b', 'x', 'd', 'e']);
assert.deepEqual(arr, ['a', 'b', 'c', 'd', 'e']);
```

**Example 2** (Ch 8): Concise non-destructive array update:
```js
function setElementNonDestructively(arr, index, value) {
  return [
    ...arr.slice(0, index), value, ...arr.slice(index+1)];
}
```

# Relationships

## Builds Upon
- **Non-destructive update** -- applies the non-destructive principle to arrays
- **Spreading arrays** -- the syntax mechanism

## Enables
- **Immutable state management** -- safe array updates in state management libraries

## Related
- **Spreading for non-destructive updates** -- the general pattern this specializes

## Contrasts With
- **Destructive update** -- `arr[index] = value` mutates the original

# Common Errors

- **Error**: Using `arr.slice(index)` instead of `arr.slice(index+1)` for the portion after the replaced element.
  **Correction**: `arr.slice(index)` includes the element at `index`; use `arr.slice(index+1)` to skip it.

# Common Confusions

- **Confusion**: `.splice()` and `.slice()` are interchangeable for this pattern.
  **Clarification**: `.splice()` mutates the original array (destructive). `.slice()` returns a new sub-array without mutation (non-destructive). Always use `.slice()` for non-destructive patterns.

# Source Reference

Chapter 8: "Updating data destructively and non-destructively", Section 8.2, lines 3677-3810.

# Verification Notes

- Definition source: direct
- Confidence rationale: Both verbose and concise implementations provided in source with assertions.
- Cross-reference status: verified against Ch 8 section 8.2
