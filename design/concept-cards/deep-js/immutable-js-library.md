---
# === CORE IDENTIFICATION ===
concept: Immutable.js Library
slug: immutable-js-library

# === CLASSIFICATION ===
category: data-management
subcategory: immutability
tier: intermediate

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "The problems of shared mutable state and how to avoid them"
chapter_number: 9
section: "Immutable.js"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Immutable.js"
  - "immutable-js"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - shared-mutable-state
  - immutability-for-shared-state
extends: []
related:
  - immer-library
  - non-destructive-update-as-defense
contrasts_with:
  - immer-library

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does defensive copying relate to immutability?"
---

# Quick Definition

Immutable.js is a JavaScript library that provides persistent immutable data structures (List, Stack, Set, Map, etc.) where "destructive" operations return modified copies instead of mutating the original.

# Core Definition

As described in "Deep JavaScript" Ch 9, Section 9.5.1, Immutable.js is described in its repository as providing "Immutable persistent data collections for JavaScript which increase efficiency and simplicity." It offers data structures such as `List`, `Stack`, `Set`, and `Map` (distinct from JavaScript's built-in `Set` and `Map`). "Destructive" operations like `.set()` return modified copies rather than mutating the receiver. Equality can be checked via the built-in `.equals()` method.

# Prerequisites

- **Shared mutable state** -- the problem Immutable.js addresses
- **Immutability for shared state** -- the strategy Immutable.js implements

# Key Properties

1. Provides its own data structures (not plain objects/arrays).
2. "Destructive" methods return new instances; originals are unchanged.
3. Includes `.equals()` for structural equality comparison.
4. `Set` and `Map` are different from JavaScript's built-in `Set` and `Map`.
5. Uses structural sharing internally for efficiency.

# Construction / Recognition

## To Construct/Create:
1. Import from the library: `import {Map} from 'immutable';`
2. Create instances: `Map([[key, value], ...])`.
3. "Mutate" by calling methods that return new instances.

## To Identify/Recognize:
1. Data structures from the `immutable` package.
2. Methods that return new instances instead of modifying in place.

# Context & Application

Immutable.js is suited for applications that need immutable data with efficient updates. The tradeoff is that it uses custom data structures, not plain JavaScript objects/arrays, which can complicate interoperability and debugging.

# Examples

**Example 1** (Ch 9): Using an immutable Map:
```js
import {Map} from 'immutable/dist/immutable.es.js';
const map0 = Map([
  [false, 'no'],
  [true, 'yes'],
]);

// "Mutation" returns a new instance:
const map1 = map0.set(true, 'maybe');
assert.ok(map1 !== map0);
assert.equal(map1.equals(map0), false);

// Undoing the change produces equal (but not identical) content:
const map2 = map1.set(true, 'yes');
assert.ok(map2 !== map0);
assert.equal(map2.equals(map0), true);
```

# Relationships

## Builds Upon
- **Immutability for shared state** -- Immutable.js is a library implementation of this strategy

## Enables
- **Efficient immutable state management** -- structural sharing makes updates performant

## Related
- **Non-destructive update as defense** -- the underlying principle

## Contrasts With
- **Immer library** -- Immer uses plain JavaScript objects; Immutable.js uses custom data structures

# Common Errors

- **Error**: Using `===` to compare Immutable.js values for structural equality.
  **Correction**: Use `.equals()` for structural equality. `===` checks reference identity.

# Common Confusions

- **Confusion**: Immutable.js `Map` is the same as JavaScript's built-in `Map`.
  **Clarification**: They are different data structures. Immutable.js `Map` is immutable and has different APIs.

# Source Reference

Chapter 9: "The problems of shared mutable state and how to avoid them", Section 9.5.1, lines 4180-4240.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit description and code example provided in source.
- Cross-reference status: verified against Ch 9 section 9.5.1
