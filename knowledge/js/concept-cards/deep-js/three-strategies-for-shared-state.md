---
# === CORE IDENTIFICATION ===
concept: Three Strategies for Avoiding Shared Mutable State
slug: three-strategies-for-shared-state

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
section: "What is shared mutable state and why is it problematic?"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "shared state defenses"
  - "shared mutable state solutions"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - shared-mutable-state
extends: []
related:
  - defensive-copying
  - non-destructive-update-as-defense
  - immutability-for-shared-state
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is shared mutable state?"
  - "How does defensive copying relate to immutability?"
---

# Quick Definition

The three strategies for avoiding shared mutable state problems are: (1) avoiding sharing by copying data, (2) avoiding mutations by updating non-destructively, and (3) preventing mutations by making data immutable.

# Core Definition

As described in "Deep JavaScript" Ch 9, Section 9.1, the chapter identifies three approaches to the shared mutable state problem: "Avoiding sharing by copying data" (Section 9.2), "Avoiding mutations by updating non-destructively" (Section 9.3), and "Preventing mutations by making data immutable" (Section 9.4). Each targets a different component of the problem: sharing, mutation, or the combination. They can also be combined for stronger guarantees.

# Prerequisites

- **Shared mutable state** -- the problem all three strategies address

# Key Properties

1. **Avoid sharing** (defensive copying): copy data at boundaries so parties operate on independent copies.
2. **Avoid mutation** (non-destructive updates): never mutate shared data; create new copies for changes. Requires discipline from all parties.
3. **Prevent mutation** (immutability): make data immutable so mutation is impossible. Strongest guarantee but requires non-destructive updates for changes.
4. The strategies can be combined (e.g., immutable data with non-destructive updates).
5. Each has different tradeoffs in terms of performance, ergonomics, and enforcement strength.

# Construction / Recognition

## To Construct/Create:
1. Choose one or more strategies based on the application's needs.
2. Apply consistently across the codebase.

## To Identify/Recognize:
1. Defensive copying: copy operations at function/class boundaries.
2. Non-destructive updates: spreading patterns, no direct assignment to shared data.
3. Immutability: `Object.freeze()`, Immutable.js, Immer, or TypeScript `readonly`.

# Context & Application

These three strategies form the complete toolkit for managing shared mutable state in JavaScript. Most production applications use a combination (e.g., Immer for immutability + non-destructive updates, defensive copying at API boundaries).

# Examples

**Example 1** (Ch 9): Strategy 1 -- Defensive copying:
```js
function logElements(arr) {
  arr = [...arr]; // Avoid sharing
  while (arr.length > 0) { console.log(arr.shift()); }
}
```

**Example 2** (Ch 9): Strategy 2 -- Non-destructive updates:
```js
const copy = original; // Sharing is safe because we never mutate
const updated = {...original, city: 'Munich'};
```

**Example 3** (Ch 9): Strategy 3 -- Immutability:
```js
const data = Object.freeze({city: 'Berlin'});
// data.city = 'Munich'; // TypeError in strict mode
```

# Relationships

## Builds Upon
- **Shared mutable state** -- the problem these strategies address

## Enables
- **Robust application architecture** -- systematic application of these strategies prevents a major class of bugs

## Related
- **Defensive copying** -- Strategy 1
- **Non-destructive update as defense** -- Strategy 2
- **Immutability for shared state** -- Strategy 3

## Contrasts With
(none -- this card describes the landscape of solutions)

# Common Errors

- **Error**: Applying only one strategy inconsistently across a codebase.
  **Correction**: Choose a strategy and apply it systematically. Strategy 2 (non-destructive updates) requires ALL parties to comply. Strategy 3 (immutability) is self-enforcing.

# Common Confusions

- **Confusion**: These strategies are mutually exclusive.
  **Clarification**: They complement each other. Immutability + non-destructive updates is a particularly powerful combination. Defensive copying can be used at boundaries even within an otherwise immutable architecture.

# Source Reference

Chapter 9: "The problems of shared mutable state and how to avoid them", Sections 9.1-9.4, lines 3878-4180.

# Verification Notes

- Definition source: direct
- Confidence rationale: The three strategies are explicitly listed and structured as the chapter's main sections.
- Cross-reference status: verified against Ch 9 sections 9.1-9.4
