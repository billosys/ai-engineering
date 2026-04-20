---
# === CORE IDENTIFICATION ===
concept: Non-Destructive Update
slug: non-destructive-update

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
section: "Examples: updating an object destructively and non-destructively"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "immutable update"
  - "copy-on-write update"
  - "non-mutating update"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - destructive-update
  - shallow-copy
extends: []
related:
  - spreading-for-non-destructive-updates
  - non-destructive-update-as-defense
contrasts_with:
  - destructive-update

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does destructive updating differ from non-destructive updating?"
---

# Quick Definition

A non-destructive update creates a copy of data that has the desired new form, leaving the original data unchanged.

# Core Definition

As described in "Deep JavaScript" Ch 8: "A non-destructive update of data creates a copy of the data that has the desired form. The latter way is similar to first making a copy and then changing it destructively, but it does both at the same time." The original data remains unmodified, making non-destructive updates safe for shared data.

# Prerequisites

- **Destructive update** -- understanding what non-destructive updating avoids
- **Shallow copy** -- non-destructive updates typically create shallow copies with modifications

# Key Properties

1. Creates a new object/array with the desired modifications.
2. The original data is not changed.
3. Both versions of the data (old and new) coexist.
4. Typically performs a shallow update (only the top level is new).
5. Safe for shared data -- no risk of surprising other references.

# Construction / Recognition

## To Construct/Create:
1. For objects: `{...obj, [key]: value}` (spreading with override).
2. For arrays: `[...arr.slice(0, index), value, ...arr.slice(index+1)]`.
3. Manually by iterating and building a new structure.

## To Identify/Recognize:
1. A new variable is assigned the result.
2. The original variable remains unchanged after the operation.

# Context & Application

Non-destructive updates are the foundation of functional programming patterns in JavaScript. They are essential for avoiding shared mutable state problems and are the default approach in frameworks like React (state updates) and Redux (reducers).

# Examples

**Example 1** (Ch 8): Non-destructive object update (manual):
```js
function setPropertyNonDestructively(obj, key, value) {
  const updatedObj = {};
  for (const [k, v] of Object.entries(obj)) {
    updatedObj[k] = (k === key ? value : v);
  }
  return updatedObj;
}

const obj = {city: 'Berlin', country: 'Germany'};
const updatedObj = setPropertyNonDestructively(obj, 'city', 'Munich');

assert.deepEqual(updatedObj, {city: 'Munich', country: 'Germany'});
assert.deepEqual(obj, {city: 'Berlin', country: 'Germany'});
```

**Example 2** (Ch 8): Non-destructive object update (concise with spreading):
```js
function setPropertyNonDestructively(obj, key, value) {
  return {...obj, [key]: value};
}
```

**Example 3** (Ch 8): Non-destructive array update:
```js
function setElementNonDestructively(arr, index, value) {
  return [
    ...arr.slice(0, index), value, ...arr.slice(index+1)];
}

const arr = ['a', 'b', 'c', 'd', 'e'];
const updatedArr = setElementNonDestructively(arr, 2, 'x');
assert.deepEqual(updatedArr, ['a', 'b', 'x', 'd', 'e']);
assert.deepEqual(arr, ['a', 'b', 'c', 'd', 'e']);
```

# Relationships

## Builds Upon
- **Shallow copy** -- non-destructive updates create modified shallow copies
- **Spreading objects** -- the primary syntax for non-destructive object updates

## Enables
- **Non-destructive update as defense** -- safe sharing of data without mutation risks
- **Deep updating** -- non-destructive approach extends to nested structures

## Related
- **Spreading for non-destructive updates** -- the concise syntax pattern

## Contrasts With
- **Destructive update** -- mutates the original data in place

# Common Errors

- **Error**: Forgetting that non-destructive updates are shallow -- nested objects are still shared.
  **Correction**: For nested changes, use manual deep updating or a library like Immer.

# Common Confusions

- **Confusion**: Non-destructive updates are always less efficient than destructive updates.
  **Clarification**: While they do create new objects, structural sharing (copying references to unchanged nested values) makes them efficient. Libraries like Immer optimize this further.

# Source Reference

Chapter 8: "Updating data destructively and non-destructively", Sections 8.1-8.2, lines 3677-3810.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition at the start of Ch 8 with multiple worked examples.
- Cross-reference status: verified against Ch 8 sections 8.1, 8.2, and Ch 9 section 9.3
