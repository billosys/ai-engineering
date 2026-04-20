---
# === CORE IDENTIFICATION ===
concept: Manual Deep Copying via Nested Spreading
slug: nested-spreading-deep-copy

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
section: "Manual deep copying via nested spreading"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "nested spread copy"
  - "manual deep copy"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - shallow-copy
  - spreading-objects
  - deep-copy
extends:
  - spreading-objects
related:
  - json-deep-copy
  - generic-deep-copy
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a deep copy of an object?"
  - "What distinguishes shallow copying from deep copying?"
---

# Quick Definition

Nested spreading manually applies the spread operator at every level of a nested object to produce a deep copy of a known structure.

# Core Definition

As described in "Deep JavaScript" Ch 7, Section 7.3.1: "If we nest spreading, we get deep copies." Each nested level of the original is explicitly spread into a new object or array literal. This requires knowing the structure in advance and is only practical for objects with a known, manageable nesting depth.

# Prerequisites

- **Spreading objects** -- the mechanism used at each level
- **Deep copy** -- the goal this technique achieves
- **Shallow copy** -- understanding why single-level spreading is insufficient

# Key Properties

1. Produces a true deep copy for the explicitly spread levels.
2. Requires knowledge of the object's structure at coding time.
3. Verbose for deeply nested structures.
4. No runtime overhead of generic algorithms.

# Construction / Recognition

## To Construct/Create:
1. Spread the top-level object.
2. For each nested object/array property, spread it as well.
3. Repeat for all nesting levels.

## To Identify/Recognize:
1. Nested `{...obj.prop}` or `[...arr]` patterns in object/array literals.

# Context & Application

Use when you have a known, small structure and want a quick deep copy without importing a library or implementing a recursive function. Common in Redux reducers and React state updates.

# Examples

**Example 1** (Ch 7): Nested spreading for a two-level object:
```js
const original = {name: 'Jane', work: {employer: 'Acme'}};
const copy = {name: original.name, work: {...original.work}};

// Successful deep copy:
assert.deepEqual(original, copy);
// Nested objects are independent:
assert.ok(original.work !== copy.work);
```

# Relationships

## Builds Upon
- **Spreading objects** -- applies spreading recursively at each level

## Enables
- **Non-destructive deep update** -- manual nested spreading is also used for deep updates

## Related
- **JSON deep copy** -- a generic alternative
- **Generic deep copy** -- a recursive function alternative

## Contrasts With
(none at this specificity)

# Common Errors

- **Error**: Forgetting to spread at one nesting level, leaving a shared reference.
  **Correction**: Every nested object that needs to be independent must be explicitly spread.

# Common Confusions

- **Confusion**: A single spread at the top level deep-copies everything.
  **Clarification**: Only the level where spreading is applied gets a new copy. Every nested level needs its own spread.

# Source Reference

Chapter 7: "Copying objects and Arrays", Section 7.3.1, lines 3365-3380.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit example with assertion proving deep independence.
- Cross-reference status: verified against Ch 7 section 7.3.1
