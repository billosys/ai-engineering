---
# === CORE IDENTIFICATION ===
concept: Defensive Copying
slug: defensive-copying

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
section: "Avoiding sharing by copying data"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "defensive copy"
  - "protective copying"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - shared-mutable-state
  - shallow-copy
extends: []
related:
  - defensive-copying-input
  - defensive-copying-output
  - non-destructive-update-as-defense
  - immutability-for-shared-state
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does defensive copying relate to immutability?"
  - "What is shared mutable state?"
---

# Quick Definition

Defensive copying is a technique of always copying potentially shared data to prevent one party's mutations from affecting another, protecting both the current entity and external parties.

# Core Definition

As described in "Deep JavaScript" Ch 9, Section 9.2.1: "Defensive copying is a technique to always copy when issues might arise. Its objective is to keep the current entity (function, class, etc.) safe." It has two directions: (1) **Input**: copying shared data passed to us, so we can use it without being disturbed by external changes. (2) **Output**: copying internal data before exposing it, so external parties cannot disrupt our internal state.

# Prerequisites

- **Shared mutable state** -- the problem defensive copying solves
- **Shallow copy** -- the mechanism typically used for defensive copies

# Key Properties

1. Two directions: input copying and output copying.
2. Input copying protects us from external modifications.
3. Output copying protects our internal state from external modifications.
4. "These measures protect us from other parties, but they also protect other parties from us."
5. Only needs to be as deep as necessary for the data being shared.

# Construction / Recognition

## To Construct/Create:
1. Input: copy parameters at the beginning of a function: `arr = [...arr];`
2. Output: copy internal data before returning it: `return [...this._data];`

## To Identify/Recognize:
1. A spread or copy operation at function entry (input defense).
2. A spread or copy operation before returning internal data (output defense).

# Context & Application

Defensive copying is one of three strategies for avoiding shared mutable state problems (alongside non-destructive updating and immutability). It is straightforward but can be expensive if deep copies are needed frequently.

# Examples

**Example 1** (Ch 9): Defensive input copying fixes the motivating example:
```js
function logElements(arr) {
  arr = [...arr]; // defensive copy
  while (arr.length > 0) {
    console.log(arr.shift());
  }
}
```

**Example 2** (Ch 9): Defensive output copying in a class:
```js
class StringBuilder {
  _data = [];
  add(str) {
    this._data.push(str);
  }
  getParts() {
    return [...this._data]; // defensive copy
  }
  toString() {
    return this._data.join('');
  }
}
```

# Relationships

## Builds Upon
- **Shared mutable state** -- the problem this technique addresses
- **Shallow copy** -- the mechanism typically used

## Enables
- **Safe function interfaces** -- functions that defensively copy can be called safely with shared data

## Related
- **Non-destructive update as defense** -- an alternative strategy
- **Immutability for shared state** -- another alternative strategy

## Contrasts With
(none at this specificity)

# Common Errors

- **Error**: Only defending inputs but not outputs (or vice versa).
  **Correction**: Consider both directions. A class that copies inputs but exposes internal references via getters is still vulnerable.

# Common Confusions

- **Confusion**: Defensive copying and deep copying are the same.
  **Clarification**: Defensive copying may be shallow or deep depending on the data structure. For flat arrays/objects, shallow copying is sufficient.

# Source Reference

Chapter 9: "The problems of shared mutable state and how to avoid them", Section 9.2.1, lines 3970-4100.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with both input and output examples provided in source.
- Cross-reference status: verified against Ch 9 section 9.2.1
