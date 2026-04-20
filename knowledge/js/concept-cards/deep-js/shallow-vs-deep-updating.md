---
# === CORE IDENTIFICATION ===
concept: Shallow vs Deep Updating
slug: shallow-vs-deep-updating

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
section: "Manual deep updating"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "top-level vs nested updating"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - non-destructive-update
  - shallow-copy
  - deep-copy
extends: []
related:
  - spreading-for-non-destructive-updates
  - manual-deep-update
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does destructive updating differ from non-destructive updating?"
  - "What distinguishes shallow copying from deep copying?"
---

# Quick Definition

Shallow updating modifies only top-level properties of an object or array, while deep updating also modifies properties at nested levels -- a distinction that parallels shallow vs deep copying.

# Core Definition

As described in "Deep JavaScript" Ch 8, both `setPropertyNonDestructively()` and `setElementNonDestructively()` "update shallowly: They only change the top level." For nested changes, "manual deep updating" (Section 8.3) or generic deep updating (Section 8.4) is required. The distinction mirrors shallow vs deep copying: shallow operations affect the first level only; deep operations recurse into nested structures.

# Prerequisites

- **Non-destructive update** -- the context in which the shallow/deep distinction applies
- **Shallow copy** -- the analogous distinction in copying
- **Deep copy** -- the analogous distinction in copying

# Key Properties

1. Shallow non-destructive updates create a new top-level object but share nested objects.
2. Deep non-destructive updates create new objects along the entire path of change.
3. Unchanged branches in deep updates are still shared (structural sharing).
4. The same shallow/deep distinction applies to both destructive and non-destructive updates.

# Construction / Recognition

## To Construct/Create:
1. Shallow update: `{...obj, key: value}` (top-level only).
2. Deep update: `{...obj, nested: {...obj.nested, key: value}}` (each modified level).

## To Identify/Recognize:
1. If only one spread is used, it is a shallow update.
2. If nested spreads are used along a path, it is a deep update.

# Context & Application

Most non-destructive update patterns in JavaScript (spreading) are shallow by default. Developers must explicitly handle nesting for deep updates. This is a key source of bugs in state management.

# Examples

**Example 1** (Ch 8): Shallow update -- nested object is shared:
```js
const obj = {name: 'Jane', work: {employer: 'Acme'}};
const updated = {...obj, name: 'John'};
// updated.work === obj.work (shared reference!)
```

**Example 2** (Ch 8): Deep update -- nested object is also new:
```js
const original = {name: 'Jane', work: {employer: 'Acme'}};
const updated = {
  ...original,
  name: 'John',
  work: {...original.work, employer: 'Spectre'},
};
// updated.work !== original.work (independent)
```

# Relationships

## Builds Upon
- **Non-destructive update** -- the update approach being examined at different depths

## Enables
- **Correct state management** -- understanding the distinction prevents bugs with nested state

## Related
- **Shallow copy** -- the copying parallel
- **Deep copy** -- the copying parallel

## Contrasts With
(none -- this card describes the contrast itself)

# Common Errors

- **Error**: Using a shallow spread update and expecting nested properties to be independent.
  **Correction**: Nested objects in a shallow update share references. Use nested spreading for deep updates.

# Common Confusions

- **Confusion**: `{...obj, nested: {key: value}}` deeply updates `nested`.
  **Clarification**: This replaces the entire `nested` object. To preserve other properties of `nested`, use `{...obj, nested: {...obj.nested, key: value}}`.

# Source Reference

Chapter 8: "Updating data destructively and non-destructively", Sections 8.1-8.3, lines 3677-3860.

# Verification Notes

- Definition source: synthesized from explicit statements in sections 8.1, 8.2, and 8.3
- Confidence rationale: The source explicitly notes that both update functions "update shallowly" and dedicates section 8.3 to deep updating.
- Cross-reference status: verified against Ch 8 sections 8.1-8.3
