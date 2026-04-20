---
# === CORE IDENTIFICATION ===
concept: Structural Sharing
slug: structural-sharing

# === CLASSIFICATION ===
category: data-management
subcategory: copying
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Updating data destructively and non-destructively"
chapter_number: 8
section: "Implementing generic deep updating"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - "shared structure"
  - "copy-on-write sharing"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - non-destructive-update
  - deep-copy
extends: []
related:
  - generic-deep-update
  - immer-library
  - immutable-js-library
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does destructive updating differ from non-destructive updating?"
  - "What distinguishes shallow copying from deep copying?"
---

# Quick Definition

Structural sharing is the technique where a non-destructive update creates new objects only along the modified branch of a data tree, while unchanged branches retain references to the original objects.

# Core Definition

As described in "Deep JavaScript" Ch 8, Section 8.4, the `deepUpdate()` function "only deeply changes a single branch" while "all other branches are copied shallowly." This is structural sharing: rather than deep-copying the entire tree for each update, only the path from the root to the changed leaf gets new objects. All sibling branches are shared by reference with the original. This makes non-destructive updates efficient even for large data trees.

# Prerequisites

- **Non-destructive update** -- structural sharing is a property of non-destructive updates
- **Deep copy** -- understanding why full deep copying would be wasteful

# Key Properties

1. Only the modified path through the tree gets new objects.
2. Unchanged subtrees are shared (same references) between old and new versions.
3. Memory-efficient: proportional to the depth of the change, not the size of the tree.
4. Time-efficient: only the path is traversed and copied.
5. Used by Immutable.js, Immer, and manual nested spreading.

# Construction / Recognition

## To Construct/Create:
1. When performing a non-destructive update, only create new objects at each level along the path of the change.
2. Copy references (not values) for all unchanged siblings.

## To Identify/Recognize:
1. After a non-destructive update: `updated.unchanged === original.unchanged` (same reference).
2. But `updated.changed !== original.changed` (new object along modified path).

# Context & Application

Structural sharing is what makes non-destructive updating practical for large data structures. Without it, every update would require a full deep copy. Libraries like Immutable.js use advanced persistent data structures to maximize structural sharing.

# Examples

**Example 1** (Ch 8): In `deepUpdate()`, lines B and D share unchanged branches:
```js
// In deepUpdate(original, ['work', 'employer'], 'Spectre'):
// - original.name is shared (not copied, just referenced)
// - original.work is recreated (new object)
// - original.work.employer is the new value
const original = {name: 'Jane', work: {employer: 'Acme'}};
const copy = deepUpdate(original, ['work', 'employer'], 'Spectre');
// copy.name is the same reference as original.name (structural sharing)
```

# Relationships

## Builds Upon
- **Non-destructive update** -- structural sharing is an efficiency property of non-destructive updates

## Enables
- **Efficient immutable data structures** -- makes immutability practical for large data

## Related
- **Generic deep update** -- demonstrates structural sharing explicitly
- **Immer library** -- uses structural sharing internally
- **Immutable.js library** -- uses persistent data structures with structural sharing

## Contrasts With
(none at this specificity)

# Common Errors

- **Error**: Deep copying the entire tree for each non-destructive update.
  **Correction**: Only create new objects along the modified path. Reuse references for unchanged branches.

# Common Confusions

- **Confusion**: Structural sharing means the old and new versions are entangled.
  **Clarification**: Since shared branches are never mutated (in a non-destructive regime), sharing is safe. The old and new versions are independent in behavior.

# Source Reference

Chapter 8: "Updating data destructively and non-destructively", Section 8.4, lines 3860-3895.

# Verification Notes

- Definition source: synthesized from the deepUpdate() implementation description
- Confidence rationale: The concept is clearly demonstrated in the source code and described ("only deeply changes a single branch... all other branches are copied shallowly"), but the term "structural sharing" itself is not used in the source.
- Cross-reference status: verified against Ch 8 section 8.4
