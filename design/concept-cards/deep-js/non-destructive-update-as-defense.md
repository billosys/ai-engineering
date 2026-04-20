---
# === CORE IDENTIFICATION ===
concept: Non-Destructive Updates as Defense Against Shared Mutable State
slug: non-destructive-update-as-defense

# === CLASSIFICATION ===
category: data-management
subcategory: defensive-patterns
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "The problems of shared mutable state and how to avoid them"
chapter_number: 9
section: "Avoiding mutations by updating non-destructively"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "copy-on-write defense"
  - "non-mutating shared data"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - shared-mutable-state
  - non-destructive-update
extends:
  - non-destructive-update
related:
  - defensive-copying
  - immutability-for-shared-state
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is shared mutable state?"
  - "How does defensive copying relate to immutability?"
---

# Quick Definition

When all parties agree to only update data non-destructively, sharing data becomes safe because the shared data is never mutated -- each update creates a new copy.

# Core Definition

As described in "Deep JavaScript" Ch 9, Section 9.3.1: "With non-destructive updating, sharing data becomes unproblematic, because we never mutate the shared data. (This only works if everyone that accesses the data does that!)" The key insight is that copying becomes trivially simple -- `const copy = original` -- because the "copy" never needs to be independent since neither party will mutate the original.

# Prerequisites

- **Shared mutable state** -- the problem this strategy addresses
- **Non-destructive update** -- the updating approach used

# Key Properties

1. Shared data is never mutated; updates create new objects.
2. "Copying" becomes trivially simple: `const copy = original` is sufficient.
3. Requires ALL parties to follow the non-destructive discipline.
4. If any party breaks the convention and mutates, the protection fails.

# Construction / Recognition

## To Construct/Create:
1. Always use non-destructive updates: `const updated = {...original, key: newValue}`.
2. Never mutate the original: no `original.key = newValue`.
3. "Copying" is just reference assignment: `const copy = original`.

## To Identify/Recognize:
1. No mutation operations on shared data.
2. All updates produce new objects via spreading or similar.

# Context & Application

This is the second of three strategies for avoiding shared mutable state. It is the approach used by React (state updates via `setState` or `useState`) and functional programming. It requires discipline from all code that touches the shared data.

# Examples

**Example 1** (Ch 9): Trivial copying under non-destructive discipline:
```js
const original = {city: 'Berlin', country: 'Germany'};
const copy = original; // This is safe!
// Because we only update non-destructively:
const updated = {...original, city: 'Munich'};
// original is unchanged, copy is unchanged
```

# Relationships

## Builds Upon
- **Non-destructive update** -- the mechanism that makes sharing safe

## Enables
- **Efficient data sharing** -- no need to deep-copy; references are shared freely

## Related
- **Defensive copying** -- an alternative strategy that does not require discipline from all parties
- **Immutability for shared state** -- an alternative that enforces non-mutation via runtime constraints

## Contrasts With
(none at this specificity)

# Common Errors

- **Error**: Assuming one party's non-destructive discipline protects against another party's mutations.
  **Correction**: ALL parties must follow the convention. If any party mutates, the shared data is corrupted.

# Common Confusions

- **Confusion**: Non-destructive updating eliminates the need for copying entirely.
  **Clarification**: It eliminates the need for *defensive* copying, but updates still create new objects (which is a form of copying at the update site).

# Source Reference

Chapter 9: "The problems of shared mutable state and how to avoid them", Section 9.3, lines 4100-4140.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit discussion with the key caveat about universal discipline quoted from source.
- Cross-reference status: verified against Ch 9 section 9.3.1
