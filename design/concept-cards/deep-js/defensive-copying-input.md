---
# === CORE IDENTIFICATION ===
concept: Defensive Copying of Input
slug: defensive-copying-input

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
section: "Copying shared input"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "input defense"
  - "parameter copying"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - defensive-copying
  - shared-mutable-state
extends:
  - defensive-copying
related:
  - defensive-copying-output
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does defensive copying relate to immutability?"
  - "What is shared mutable state?"
---

# Quick Definition

Defensive copying of input means copying data that is passed into a function or method before using it, so that the function can freely mutate the copy without affecting the caller's data.

# Core Definition

As described in "Deep JavaScript" Ch 9, Section 9.2.1.1: "Copying (potentially) shared data passed to us, lets us use that data without being disturbed by an external entity." By copying the input at the function boundary, the function operates on its own private copy and cannot accidentally mutate the caller's data.

# Prerequisites

- **Defensive copying** -- input copying is one direction of defensive copying
- **Shared mutable state** -- the problem motivating the copy

# Key Properties

1. The copy is made at the beginning of the function/method.
2. The function then operates on the copy, not the original.
3. Protects the function from external changes to the original.
4. Also protects the caller from the function's internal mutations.

# Construction / Recognition

## To Construct/Create:
1. At the beginning of a function, reassign the parameter to a copy: `arr = [...arr];`

## To Identify/Recognize:
1. A copy operation on a parameter at the beginning of a function body.

# Context & Application

Use when a function needs to mutate its input (e.g., sorting, shifting elements) but the caller may still need the original data.

# Examples

**Example 1** (Ch 9): Fixing `logElements()` with input defense:
```js
function logElements(arr) {
  arr = [...arr]; // defensive copy
  while (arr.length > 0) {
    console.log(arr.shift());
  }
}
```

Now `logElements()` does not destroy the caller's array:
```js
function main() {
  const arr = ['banana', 'orange', 'apple'];
  console.log('Before sorting:');
  logElements(arr);
  arr.sort();
  console.log('After sorting:');
  logElements(arr); // Works correctly now!
}
// Output includes both sorted and unsorted listings
```

# Relationships

## Builds Upon
- **Defensive copying** -- this is the input direction

## Enables
- **Safe mutation within functions** -- functions can freely mutate their local copy

## Related
- **Defensive copying output** -- the complementary direction

## Contrasts With
(none at this specificity)

# Common Errors

- **Error**: Copying the input but then accidentally using the original parameter name before the copy.
  **Correction**: Reassign the parameter variable itself: `arr = [...arr];` so all subsequent code uses the copy.

# Common Confusions

- **Confusion**: Input defense is unnecessary if the function does not modify the data.
  **Clarification**: Correct -- defensive copying is only needed if the function might mutate the input. Read-only operations on shared data are safe.

# Source Reference

Chapter 9: "The problems of shared mutable state and how to avoid them", Section 9.2.1.1, lines 3970-4050.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit example showing the fix to the motivating problem.
- Cross-reference status: verified against Ch 9 section 9.2.1.1
