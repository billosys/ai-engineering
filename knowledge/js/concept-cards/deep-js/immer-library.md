---
# === CORE IDENTIFICATION ===
concept: Immer Library
slug: immer-library

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
section: "Immer"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Immer"
  - "immer.js"
  - "produce function"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - shared-mutable-state
  - non-destructive-update
  - immutability-for-shared-state
extends: []
related:
  - immutable-js-library
  - generic-deep-update
contrasts_with:
  - immutable-js-library

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does defensive copying relate to immutability?"
---

# Quick Definition

Immer is a JavaScript library that enables non-destructive updating of plain objects, Arrays, Sets, and Maps by intercepting mutation-style operations on a draft proxy, producing an immutable result.

# Core Definition

As described in "Deep JavaScript" Ch 9, Section 9.5.2, Immer is described in its repository as: "Create the next immutable state by mutating the current one." It works with plain JavaScript data structures (no custom types needed). The `produce()` function provides a `draft` parameter that looks like the original data. Mutation-style operations on the draft are intercepted and translated into non-destructive updates. The result is "deeply immutable" as a bonus.

# Prerequisites

- **Shared mutable state** -- the problem Immer addresses
- **Non-destructive update** -- the underlying technique Immer uses
- **Immutability for shared state** -- the guarantee Immer provides

# Key Properties

1. Works with plain objects, Arrays, Sets, and Maps (no custom data structures).
2. Uses a `produce(original, recipe)` API where `recipe` receives a mutable `draft`.
3. Mutations to the draft are intercepted; the original is not modified.
4. The result is deeply immutable.
5. `assert.deepEqual()` works on the results because they are plain objects.
6. More ergonomic than manual nested spreading for deep updates.

# Construction / Recognition

## To Construct/Create:
1. Import: `import {produce} from 'immer';`
2. Use: `const updated = produce(original, draft => { draft.key = newValue; });`

## To Identify/Recognize:
1. The `produce()` function from Immer.
2. A callback that mutates a `draft` parameter.

# Context & Application

Immer is widely used in React/Redux applications for state management. It provides the ergonomics of mutation with the safety of immutability. Unlike Immutable.js, it does not require learning new data structures.

# Examples

**Example 1** (Ch 9): Deep non-destructive update with Immer:
```js
import {produce} from 'immer/dist/immer.module.js';

const people = [
  {name: 'Jane', work: {employer: 'Acme'}},
];

const modifiedPeople = produce(people, (draft) => {
  draft[0].work.employer = 'Cyberdyne';
  draft.push({name: 'John', work: {employer: 'Spectre'}});
});

assert.deepEqual(modifiedPeople, [
  {name: 'Jane', work: {employer: 'Cyberdyne'}},
  {name: 'John', work: {employer: 'Spectre'}},
]);
// Original is unchanged:
assert.deepEqual(people, [
  {name: 'Jane', work: {employer: 'Acme'}},
]);
```

# Relationships

## Builds Upon
- **Non-destructive update** -- Immer performs non-destructive updates under the hood
- **Immutability for shared state** -- the result is deeply immutable

## Enables
- **Ergonomic immutable state management** -- write mutation-style code, get immutable results

## Related
- **Generic deep update** -- Immer is a more ergonomic alternative

## Contrasts With
- **Immutable.js** -- Immutable.js uses custom data structures; Immer uses plain objects/arrays

# Common Errors

- **Error**: Trying to use the draft outside the `produce` callback.
  **Correction**: The draft is only valid within the callback. The return value of `produce()` is the new immutable state.

# Common Confusions

- **Confusion**: Immer actually mutates the original data.
  **Clarification**: Immer intercepts mutations on the draft proxy. The original data is never modified; a new immutable structure is produced.

# Source Reference

Chapter 9: "The problems of shared mutable state and how to avoid them", Section 9.5.2, lines 4240-4300.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit description, repository quote, and complete code example from source.
- Cross-reference status: verified against Ch 9 section 9.5.2
