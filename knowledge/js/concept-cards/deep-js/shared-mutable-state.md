---
# === CORE IDENTIFICATION ===
concept: Shared Mutable State
slug: shared-mutable-state

# === CLASSIFICATION ===
category: data-management
subcategory: shared-state
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
  - "shared state problem"
  - "mutable shared data"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - destructive-update
extends: []
related:
  - aliasing
  - defensive-copying
  - non-destructive-update-as-defense
  - immutability-for-shared-state
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is shared mutable state?"
---

# Quick Definition

Shared mutable state occurs when two or more parties can change the same data during overlapping lifetimes, creating a risk that one party's modifications prevent others from working correctly.

# Core Definition

As described in "Deep JavaScript" Ch 9, Section 9.1, shared mutable state exists when: (1) two or more parties can change the same data (variables, objects, etc.), (2) their lifetimes overlap, and (3) there is a risk of one party's modifications preventing other parties from working correctly. This applies to function calls, cooperative multitasking (async functions), and similar scenarios.

# Prerequisites

- **Destructive update** -- shared mutable state problems arise from destructive (mutating) updates

# Key Properties

1. Requires data to be shared (referenced by multiple parties).
2. Requires data to be mutable (can be changed).
3. Requires overlapping lifetimes of the parties accessing the data.
4. Can occur in synchronous code (function calls), not only concurrency.
5. Three solutions: avoid sharing (copying), avoid mutation (non-destructive updates), prevent mutation (immutability).

# Construction / Recognition

## To Construct/Create:
(This is a problem to avoid, not a pattern to create.)

## To Identify/Recognize:
1. Multiple functions/modules reference the same object.
2. At least one of them mutates it.
3. The mutation affects the correctness of another party.

# Context & Application

Shared mutable state is one of the most common sources of bugs in JavaScript, particularly in larger applications with many interacting components. The three main defense strategies are: defensive copying, non-destructive updating, and immutability.

# Examples

**Example 1** (Ch 9): The motivating example -- `logElements()` destroys shared data:
```js
function logElements(arr) {
  while (arr.length > 0) {
    console.log(arr.shift());
  }
}

function main() {
  const arr = ['banana', 'orange', 'apple'];

  console.log('Before sorting:');
  logElements(arr);

  arr.sort();

  console.log('After sorting:');
  logElements(arr); // Prints nothing! arr is empty.
}
```

In this example, `logElements()` mutates the shared array by calling `.shift()`, emptying it before `main()` can sort and log it again.

# Relationships

## Builds Upon
- **Destructive update** -- mutations cause shared state problems

## Enables
- **Defensive copying** -- motivated by the need to avoid shared state problems
- **Non-destructive update as defense** -- an alternative defense strategy
- **Immutability for shared state** -- another defense strategy

## Related
- **Aliasing** -- multiple references to the same data create sharing

## Contrasts With
(none -- this is the problem that other concepts solve)

# Common Errors

- **Error**: Assuming shared mutable state only matters in concurrent/async code.
  **Correction**: It applies to ordinary function calls too, as the source example demonstrates with synchronous functions.

# Common Confusions

- **Confusion**: Shared data is always problematic.
  **Clarification**: Shared data is only problematic when it is also mutable. Shared read-only or immutable data is perfectly safe.

# Source Reference

Chapter 9: "The problems of shared mutable state and how to avoid them", Section 9.1, lines 3878-3970.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit three-part definition quoted from source with worked example.
- Cross-reference status: verified against Ch 9 section 9.1
