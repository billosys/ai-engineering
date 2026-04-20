---
# === CORE IDENTIFICATION ===
concept: Destructive Update
slug: destructive-update

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
  - "in-place update"
  - "mutation"
  - "mutating update"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - shared-mutable-state
contrasts_with:
  - non-destructive-update

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does destructive updating differ from non-destructive updating?"
---

# Quick Definition

A destructive update mutates existing data in place so that it takes on the desired new form, modifying the original object or array directly.

# Core Definition

As described in "Deep JavaScript" Ch 8: "A destructive update of data mutates the data so that it has the desired form." The original data is changed; no copy is created. Any other references to the same data will see the changes, which is both the utility and the danger of destructive updates.

# Prerequisites

- **Object references** -- understanding that multiple variables can reference the same object

# Key Properties

1. Modifies the original data in place.
2. No new object or array is created.
3. All references to the data see the changes.
4. More memory-efficient than non-destructive updates (no copying).
5. Can cause problems with shared mutable state.

# Construction / Recognition

## To Construct/Create:
1. For objects: `obj[key] = value;`
2. For arrays: `arr[index] = value;`

## To Identify/Recognize:
1. The original variable is modified; no new variable is assigned the result.
2. Assignment directly to a property or index of an existing object/array.

# Context & Application

Destructive updates are the default mutation pattern in JavaScript. They are efficient but dangerous when data is shared between multiple parties (functions, modules, async tasks). They are the counterpart to non-destructive updates.

# Examples

**Example 1** (Ch 8): Destructive object property update:
```js
function setPropertyDestructively(obj, key, value) {
  obj[key] = value;
  return obj;
}

const obj = {city: 'Berlin', country: 'Germany'};
setPropertyDestructively(obj, 'city', 'Munich');
assert.deepEqual(obj, {city: 'Munich', country: 'Germany'});
```

**Example 2** (Ch 8): Destructive array element update:
```js
function setElementDestructively(arr, index, value) {
  arr[index] = value;
}

const arr = ['a', 'b', 'c', 'd', 'e'];
setElementDestructively(arr, 2, 'x');
assert.deepEqual(arr, ['a', 'b', 'x', 'd', 'e']);
```

# Relationships

## Builds Upon
- **Object references** -- destructive updates affect all references to the same object

## Enables
- **Shared mutable state** -- destructive updates on shared data create shared mutable state problems

## Related
- **Shared mutable state** -- the problem that arises from destructive updates on shared data

## Contrasts With
- **Non-destructive update** -- creates a modified copy instead of mutating the original

# Common Errors

- **Error**: Destructively updating shared data without realizing other code depends on it.
  **Correction**: Use non-destructive updates or defensive copying when data might be shared.

# Common Confusions

- **Confusion**: Destructive updates are always bad.
  **Clarification**: They are efficient and appropriate when data is not shared. The problems arise specifically from shared mutable state.

# Source Reference

Chapter 8: "Updating data destructively and non-destructively", Sections 8.1-8.2, lines 3677-3810.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition at the start of Ch 8 with worked examples.
- Cross-reference status: verified against Ch 8 sections 8.1 and 8.2
