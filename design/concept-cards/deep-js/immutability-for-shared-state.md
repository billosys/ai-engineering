---
# === CORE IDENTIFICATION ===
concept: Immutability as Defense Against Shared Mutable State
slug: immutability-for-shared-state

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
section: "Preventing mutations by making data immutable"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "immutable shared data"
  - "frozen objects for sharing"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - shared-mutable-state
extends: []
related:
  - defensive-copying
  - non-destructive-update-as-defense
  - object-freeze
  - immutable-js-library
  - immer-library
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is shared mutable state?"
  - "How does defensive copying relate to immutability?"
---

# Quick Definition

Making shared data immutable eliminates the "mutable" condition of shared mutable state, allowing data to be freely shared without risk of unintended modification.

# Core Definition

As described in "Deep JavaScript" Ch 9, Section 9.4.1: "If data is immutable, it can be shared without any risks. In particular, there is no need to copy defensively." The source also notes: "Non-destructive updating is an important complement to immutable data. If we combine the two, immutable data becomes virtually as versatile as mutable data but without the associated risks."

# Prerequisites

- **Shared mutable state** -- the problem this strategy solves

# Key Properties

1. Immutable data can be freely shared -- no defensive copying needed.
2. Mutations are prevented at runtime, not just by convention.
3. Non-destructive updating complements immutability to maintain versatility.
4. Combining immutability with non-destructive updates provides safety without losing functionality.

# Construction / Recognition

## To Construct/Create:
1. Use `Object.freeze()` for native JavaScript immutability.
2. Use Immutable.js for persistent immutable data structures.
3. Use Immer for immutability with familiar mutation-style syntax.

## To Identify/Recognize:
1. Attempting to modify a property throws an error (in strict mode) or silently fails.
2. Data structures from immutability libraries return new instances from "mutation" methods.

# Context & Application

This is the third strategy for avoiding shared mutable state. It provides the strongest guarantee: mutations are impossible, not just avoided by convention. The tradeoff is that updates must create new objects, which can be mitigated by libraries with structural sharing.

# Examples

**Example 1** (Ch 9): The principle:
```js
// Immutable data can be shared freely
const config = Object.freeze({host: 'example.com', port: 8080});
// Any attempt to mutate will fail:
// config.port = 9090; // TypeError in strict mode
```

**Example 2** (Ch 9): Combining immutability with non-destructive updating:
```js
const original = Object.freeze({city: 'Berlin', country: 'Germany'});
// Non-destructive update creates a new object:
const updated = Object.freeze({...original, city: 'Munich'});
// original is unchanged and immutable; updated is also immutable
```

# Relationships

## Builds Upon
- **Shared mutable state** -- the problem this strategy eliminates

## Enables
- **Safe data sharing** -- no defensive copying overhead needed

## Related
- **Object.freeze()** -- the native JavaScript mechanism
- **Immutable.js** -- library for persistent immutable data structures
- **Immer** -- library for ergonomic immutability
- **Non-destructive update as defense** -- complementary strategy

## Contrasts With
(none at this specificity)

# Common Errors

- **Error**: Assuming `Object.freeze()` is deep.
  **Correction**: `Object.freeze()` is shallow -- nested objects remain mutable. Deep freezing requires recursive application.

# Common Confusions

- **Confusion**: Immutability makes data impossible to "change."
  **Clarification**: Immutability prevents mutation of existing objects, but non-destructive updates allow creating new objects with different values. The combination is "virtually as versatile as mutable data."

# Source Reference

Chapter 9: "The problems of shared mutable state and how to avoid them", Section 9.4, lines 4140-4180.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit statement and principle quoted from source, with note about complementary non-destructive updates.
- Cross-reference status: verified against Ch 9 section 9.4
