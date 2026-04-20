---
# === CORE IDENTIFICATION ===
concept: Manual Deep Updating
slug: manual-deep-update

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
  - "nested non-destructive update"
  - "deep spread update"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - non-destructive-update
  - spreading-for-non-destructive-updates
  - nested-spreading-deep-copy
extends:
  - spreading-for-non-destructive-updates
related:
  - generic-deep-update
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does destructive updating differ from non-destructive updating?"
---

# Quick Definition

Manual deep updating uses nested spreading to non-destructively change properties at multiple levels of a nested object, creating new objects at each modified level.

# Core Definition

As described in "Deep JavaScript" Ch 8, Section 8.3, manual deep updating applies spreading at each nesting level where a change is needed. Each level that is modified gets a new object; unchanged branches remain shared with the original. This requires knowing the object structure in advance.

# Prerequisites

- **Non-destructive update** -- manual deep updating is a multi-level non-destructive update
- **Spreading for non-destructive updates** -- the pattern applied at each level
- **Nested spreading deep copy** -- the same technique used for copying, here applied for updating

# Key Properties

1. Each modified level gets a new object via spreading.
2. Unchanged nested objects are shared (structural sharing).
3. Requires knowing the structure at coding time.
4. Verbose for deeply nested structures.

# Construction / Recognition

## To Construct/Create:
1. Spread the top-level object with overrides.
2. For nested properties being changed, spread the nested object with its overrides.
3. Repeat for deeper levels.

## To Identify/Recognize:
1. Nested spread patterns: `{...obj, nested: {...obj.nested, prop: value}}`.

# Context & Application

Used in React state updates and Redux reducers when nested state needs to change. For complex structures, libraries like Immer simplify the syntax.

# Examples

**Example 1** (Ch 8): Updating name and nested employer:
```js
const original = {name: 'Jane', work: {employer: 'Acme'}};
const updatedOriginal = {
  ...original,
  name: 'John',
  work: {
    ...original.work,
    employer: 'Spectre'
  },
};

assert.deepEqual(
  original, {name: 'Jane', work: {employer: 'Acme'}});
assert.deepEqual(
  updatedOriginal, {name: 'John', work: {employer: 'Spectre'}});
```

# Relationships

## Builds Upon
- **Spreading for non-destructive updates** -- applies the spread-override pattern at multiple levels

## Enables
- **Generic deep update** -- motivates a generic recursive approach for arbitrary paths

## Related
- **Generic deep update** -- the programmatic alternative for dynamic paths

## Contrasts With
(none at this specificity)

# Common Errors

- **Error**: Forgetting to spread an intermediate level, accidentally replacing the entire nested object.
  **Correction**: Every level that needs to preserve existing properties must be spread: `{...original.work, employer: 'New'}` not `{employer: 'New'}`.

# Common Confusions

- **Confusion**: Manual deep updating creates entirely new objects at every level.
  **Clarification**: Only the levels along the path of the change get new objects. Unchanged branches are shared (structural sharing), which is efficient.

# Source Reference

Chapter 8: "Updating data destructively and non-destructively", Section 8.3, lines 3810-3860.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit example with assertions proving both original preservation and nested update.
- Cross-reference status: verified against Ch 8 section 8.3
