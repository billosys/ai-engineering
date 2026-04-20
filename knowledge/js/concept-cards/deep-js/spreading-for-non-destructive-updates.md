---
# === CORE IDENTIFICATION ===
concept: Spreading for Non-Destructive Updates
slug: spreading-for-non-destructive-updates

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
  - "spread update pattern"
  - "{...obj, key: value} pattern"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - non-destructive-update
  - spreading-objects
  - spreading-arrays
extends:
  - spreading-objects
related:
  - manual-deep-update
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does destructive updating differ from non-destructive updating?"
---

# Quick Definition

The spreading update pattern uses `{...obj, key: newValue}` for objects or `[...arr.slice(0, i), value, ...arr.slice(i+1)]` for arrays to create modified copies without mutating the originals.

# Core Definition

As described in "Deep JavaScript" Ch 8, spreading makes non-destructive updates concise. For objects, `{...obj, [key]: value}` copies all properties and overrides the specified key. For arrays, slicing and spreading can replace a specific element. Both approaches produce "shallow" updates -- only the top level is new.

# Prerequisites

- **Non-destructive update** -- the concept this pattern implements
- **Spreading objects** -- the syntax used for object updates
- **Spreading arrays** -- the syntax used for array updates

# Key Properties

1. Object pattern: `{...obj, [key]: value}` -- later properties override earlier ones.
2. Array pattern: `[...arr.slice(0, index), value, ...arr.slice(index+1)]`.
3. Both produce shallow updates (only top level is new).
4. Concise alternative to manual iteration.

# Construction / Recognition

## To Construct/Create:
1. Object: `return {...obj, [key]: value};`
2. Array: `return [...arr.slice(0, index), value, ...arr.slice(index+1)];`

## To Identify/Recognize:
1. Spread syntax followed by property overrides in an object literal.
2. Multiple spreads with `.slice()` in an array literal.

# Context & Application

This is the idiomatic pattern for non-destructive updates in modern JavaScript. It is the standard approach in React state updates and Redux reducers.

# Examples

**Example 1** (Ch 8): Concise non-destructive object update:
```js
function setPropertyNonDestructively(obj, key, value) {
  return {...obj, [key]: value};
}
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
- **Spreading objects** -- the underlying syntax mechanism
- **Non-destructive update** -- the concept this pattern implements

## Enables
- **Manual deep update** -- nested spreading extends this pattern to deep structures

## Related
- **Manual deep update** -- applies nested spreading for deep non-destructive updates

## Contrasts With
(none at this specificity)

# Common Errors

- **Error**: Placing the override property before the spread (`{key: value, ...obj}`) -- the spread will overwrite it.
  **Correction**: Place overrides after the spread: `{...obj, key: value}`.

# Common Confusions

- **Confusion**: This pattern deeply updates nested properties.
  **Clarification**: It only updates the top level. Nested objects are still shared references from the original.

# Source Reference

Chapter 8: "Updating data destructively and non-destructively", Sections 8.1-8.2, lines 3677-3810.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit concise versions provided in source for both objects and arrays.
- Cross-reference status: verified against Ch 8 sections 8.1 and 8.2
