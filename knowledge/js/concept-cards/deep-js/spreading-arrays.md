---
# === CORE IDENTIFICATION ===
concept: Spreading Into Array Literals
slug: spreading-arrays

# === CLASSIFICATION ===
category: data-management
subcategory: copying
tier: foundational

# === PROVENANCE ===
source: "Deep JavaScript"
source_slug: deep-js
authors: "Dr. Axel Rauschmayer"
chapter: "Copying objects and Arrays"
chapter_number: 7
section: "Copying plain objects and Arrays via spreading"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "array spread"
  - "spread syntax for arrays"
  - "[...arr]"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - shallow-copy
extends: []
related:
  - spreading-objects
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do shallow copies relate to deep copies?"
---

# Quick Definition

Array spreading (`[...arr]`) creates a shallow copy of an array's elements into a new array literal.

# Core Definition

As described in "Deep JavaScript" Ch 7, Section 7.2.1, spreading into array literals (`[...originalArray]`) creates a shallow copy of an array. Each element is copied by reference; nested objects or arrays within the original are shared with the copy.

# Prerequisites

- **Shallow copy** -- array spreading produces a shallow copy

# Key Properties

1. Creates a new array with the same elements.
2. The copy is shallow: nested objects/arrays are shared references.
3. The resulting array is a plain Array (prototype is `Array.prototype`).

# Construction / Recognition

## To Construct/Create:
1. `const copy = [...originalArray];`

## To Identify/Recognize:
1. The `[...x]` syntax in an array literal context.

# Context & Application

Array spreading is the standard way to shallow-copy arrays in modern JavaScript. It is commonly used in defensive copying (e.g., `arr = [...arr]`) and non-destructive array updates.

# Examples

**Example 1** (Ch 7): Basic array copy:
```js
const copyOfArray = [...originalArray];
```

**Example 2** (Ch 8, related): Using spreading for non-destructive array element update:
```js
function setElementNonDestructively(arr, index, value) {
  return [
    ...arr.slice(0, index), value, ...arr.slice(index+1)];
}
```

# Relationships

## Builds Upon
- **Shallow copy** -- array spreading is a mechanism for shallow copying

## Enables
- **Non-destructive array update** -- combine with `.slice()` for non-destructive element replacement
- **Defensive copying** -- `arr = [...arr]` creates a defensive copy of input arrays

## Related
- **Spreading objects** -- the object equivalent: `{...obj}`

## Contrasts With
(none at this specificity)

# Common Errors

- **Error**: Assuming `[...arr]` produces a deep copy of nested arrays.
  **Correction**: Only top-level elements are copied. Nested arrays/objects remain shared references.

# Common Confusions

- **Confusion**: Array spreading and `Array.from()` are fundamentally different.
  **Clarification**: For arrays, `[...arr]` and `Array.from(arr)` produce equivalent shallow copies, though they differ for non-array iterables.

# Source Reference

Chapter 7: "Copying objects and Arrays", Section 7.2.1, lines 3158-3270.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit syntax shown in source alongside object spreading.
- Cross-reference status: verified against Ch 7 section 7.2.1
