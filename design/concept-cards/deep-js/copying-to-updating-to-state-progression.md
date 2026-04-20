---
# === CORE IDENTIFICATION ===
concept: "Copying -> Updating -> State Management Progression"
slug: copying-to-updating-to-state-progression

# === CLASSIFICATION ===
category: data-management
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Copying objects and Arrays"
chapter_number: 7
section: null

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - "data management progression"
  - "Ch 7-9 concept chain"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - shallow-copy
  - deep-copy
extends: []
related:
  - non-destructive-update
  - shared-mutable-state
  - defensive-copying
  - immutability-for-shared-state
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do shallow copies relate to deep copies?"
  - "How does destructive updating differ from non-destructive updating?"
  - "What is shared mutable state?"
  - "How does defensive copying relate to immutability?"
---

# Quick Definition

Chapters 7-9 form a natural progression: copying (Ch 7) enables non-destructive updating (Ch 8), which is one of three defenses against shared mutable state (Ch 9).

# Core Definition

As structured in "Deep JavaScript" Chapters 7-9, the concepts build progressively: Ch 7 establishes how to copy data (shallow and deep), Ch 8 uses copying as the basis for non-destructive updating patterns, and Ch 9 identifies shared mutable state as the core problem and presents copying, non-destructive updates, and immutability as the three defense strategies. Each chapter builds on the previous: you cannot understand non-destructive updates without understanding copying, and you cannot appreciate the defense strategies without understanding both.

# Prerequisites

- **Shallow copy** -- the starting concept in Ch 7
- **Deep copy** -- the advanced copying concept in Ch 7

# Key Properties

1. **Ch 7 (Copying)**: Shallow vs deep, spreading, Object.assign(), JSON, recursive.
2. **Ch 8 (Updating)**: Destructive vs non-destructive, shallow vs deep updating.
3. **Ch 9 (State)**: Shared mutable state, three defenses (copy, non-destructive, immutable).
4. Each chapter's concepts are prerequisites for the next.
5. The progression mirrors how real applications evolve from simple data manipulation to state management.

# Construction / Recognition

## To Construct/Create:
1. Master copying mechanisms (Ch 7).
2. Apply copying to build non-destructive update patterns (Ch 8).
3. Use non-destructive updates as one strategy in a comprehensive state management approach (Ch 9).

## To Identify/Recognize:
1. When a state management bug occurs, trace it back through the chain: Is it a copying issue? An update pattern issue? A sharing issue?

# Context & Application

This progression provides the conceptual foundation for state management in JavaScript applications. It is the theoretical underpinning of patterns used in React, Redux, and functional JavaScript.

# Examples

**Example 1** (Ch 7-9): The progression in action:
```js
// Ch 7: Copy
const copy = {...original};

// Ch 8: Non-destructive update (uses copying)
const updated = {...original, key: newValue};

// Ch 9: Defense against shared state (uses non-destructive updates)
const state = produce(currentState, draft => {
  draft.key = newValue;
});
```

# Relationships

## Builds Upon
- **Shallow copy** -- the foundation of the progression
- **Deep copy** -- extended copying for nested data

## Enables
- **Comprehensive state management** -- understanding the full chain from copying to state management

## Related
- **Non-destructive update** -- the middle link
- **Shared mutable state** -- the problem at the end of the chain
- **Defensive copying** -- a strategy that directly uses Ch 7 concepts
- **Immutability for shared state** -- the culminating strategy

## Contrasts With
(none -- this card describes a conceptual progression)

# Common Errors

- **Error**: Jumping to state management patterns (Ch 9) without understanding copying (Ch 7) and updating (Ch 8).
  **Correction**: Master each concept layer before advancing. Bugs in state management often stem from misunderstanding shallow vs deep copying.

# Common Confusions

- **Confusion**: These are three independent topics.
  **Clarification**: They form a deliberate progression where each chapter builds on the previous. The book structures them this way intentionally.

# Source Reference

Chapters 7-9: "Copying objects and Arrays", "Updating data destructively and non-destructively", "The problems of shared mutable state and how to avoid them", lines 3158-4300.

# Verification Notes

- Definition source: synthesized from chapter structure and cross-references
- Confidence rationale: The progression is evident from the chapter organization and explicit cross-references between chapters.
- Cross-reference status: verified via chapter cross-references (Ch 9 references Ch 7 and Ch 8)
