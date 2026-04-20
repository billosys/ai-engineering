---
# === CORE IDENTIFICATION ===
concept: Generic Deep Update Implementation
slug: generic-deep-update

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
section: "Implementing generic deep updating"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "deepUpdate() function"
  - "path-based deep update"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - non-destructive-update
  - manual-deep-update
  - generic-deep-copy
extends:
  - manual-deep-update
related:
  - immer-library
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does destructive updating differ from non-destructive updating?"
---

# Quick Definition

A generic `deepUpdate()` function takes a value, a path (array of keys), and a new value, then non-destructively updates the single branch of the object tree specified by the path while shallowly copying all other branches.

# Core Definition

As described in "Deep JavaScript" Ch 8, Section 8.4, the `deepUpdate(original, keys, value)` function recursively follows the key path, creating new objects/arrays along the modified branch via `Object.fromEntries()` and `.map()`. Unchanged branches (lines B and D in the source) are copied shallowly (by reference), while the changed branch (lines A and C) is recursively updated.

# Prerequisites

- **Non-destructive update** -- the pattern being applied recursively
- **Manual deep update** -- the manual approach this generalizes
- **Generic deep copy** -- similar recursive structure

# Key Properties

1. Takes a path (array of keys) to identify the property to update.
2. Only deeply changes a single branch of the tree.
3. All other branches are copied shallowly (structural sharing).
4. Handles both arrays (by index) and objects (by key).
5. Base case: when key path is empty, return the new value.

# Construction / Recognition

## To Construct/Create:
1. ```js
   function deepUpdate(original, keys, value) {
     if (keys.length === 0) {
       return value;
     }
     const currentKey = keys[0];
     if (Array.isArray(original)) {
       return original.map(
         (v, index) => index === currentKey
           ? deepUpdate(v, keys.slice(1), value)
           : v);
     } else if (typeof original === 'object' && original !== null) {
       return Object.fromEntries(
         Object.entries(original).map(
           (keyValuePair) => {
             const [k, v] = keyValuePair;
             if (k === currentKey) {
               return [k, deepUpdate(v, keys.slice(1), value)];
             } else {
               return keyValuePair;
             }
           }));
     } else {
       return original;
     }
   }
   ```

## To Identify/Recognize:
1. A function that accepts a key path and recursively follows it to apply a change.

# Context & Application

Generic deep updating is useful when the path to the property being changed is dynamic (not known at coding time). It is the programmatic equivalent of nested spreading. Libraries like Immer provide a more ergonomic approach to the same problem.

# Examples

**Example 1** (Ch 8): Using deepUpdate:
```js
const original = {name: 'Jane', work: {employer: 'Acme'}};

const copy = deepUpdate(original, ['work', 'employer'], 'Spectre');
assert.deepEqual(copy, {name: 'Jane', work: {employer: 'Spectre'}});
assert.deepEqual(original, {name: 'Jane', work: {employer: 'Acme'}});
```

# Relationships

## Builds Upon
- **Manual deep update** -- this function generalizes the manual nested-spread pattern

## Enables
- **Dynamic state management** -- update deeply nested state using runtime-determined paths

## Related
- **Immer library** -- provides a more ergonomic API for the same deep non-destructive updating

## Contrasts With
(none at this specificity)

# Common Errors

- **Error**: Passing string indices for array updates instead of numeric indices.
  **Correction**: For arrays, keys must be numeric indices since the comparison is `index === currentKey`.

# Common Confusions

- **Confusion**: `deepUpdate` creates deep copies of all branches.
  **Clarification**: Only the branch along the key path is deeply updated. All other branches are shallowly copied (structural sharing for efficiency).

# Source Reference

Chapter 8: "Updating data destructively and non-destructively", Section 8.4, lines 3860-3895.

# Verification Notes

- Definition source: direct
- Confidence rationale: Complete implementation with usage example and assertions provided in source.
- Cross-reference status: verified against Ch 8 section 8.4
