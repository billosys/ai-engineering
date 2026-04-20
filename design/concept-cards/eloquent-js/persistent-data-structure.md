---
# === CORE IDENTIFICATION ===
concept: Persistent Data Structure
slug: persistent-data-structure

# === CLASSIFICATION ===
category: application-architecture
subcategory: data-structures
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Robot"
chapter_number: 7
pdf_page: null
section: "Persistent data"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - immutable data structure

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
  - array
extends: []
related:
  - immutable-state
  - state-modeling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a persistent data structure?"
  - "Why use data structures that don't change?"
---

# Quick Definition
Persistent (or immutable) data structures are data structures that don't change; they behave like strings and numbers, staying the same rather than containing different things at different times.

# Core Definition
Haverbeke defines: "Data structures that don't change are called *immutable* or *persistent*. They behave a lot like strings and numbers in that they are who they are and stay that way, rather than containing different things at different times." (Ch 7, "Persistent data")

# Prerequisites
- **Objects**: Understanding mutable vs immutable object usage
- **Arrays**: Arrays can be used persistently with `slice` and `concat`

# Key Properties
1. Operations return new values rather than modifying existing ones
2. Previous states remain intact after operations
3. `Object.freeze` can prevent writes but is not commonly used
4. Easier to reason about because operations can be considered in isolation
5. Requires more memory/computation but reduces complexity

# Construction / Recognition
Persistent usage is recognized when methods return new instances rather than modifying `this`:
```javascript
move(destination) {
  // Returns a NEW VillageState instead of modifying this one
  return new VillageState(destination, parcels);
}
```

# Context & Application
Persistent data structures help manage complexity. As Haverbeke explains: "When the objects in my system are fixed, stable things, I can consider operations on them in isolation... When objects change over time, that adds a whole new dimension of complexity to this kind of reasoning." (Ch 7)

# Examples
```javascript
let first = new VillageState(
  "Post Office",
  [{place: "Post Office", address: "Alice's House"}]
);
let next = first.move("Alice's House");

console.log(next.place);
// -> Alice's House
console.log(next.parcels);
// -> []
console.log(first.place);
// -> Post Office
```
The original state is unchanged after the move. (Ch 7, "The task", lines 193-206)

```javascript
let object = Object.freeze({value: 5});
object.value = 10;
console.log(object.value);
// -> 5
```
(Ch 7, "Persistent data", lines 234-239)

# Relationships
## Builds Upon
- object, array
## Enables
- immutable-state, easier testing, simpler reasoning
## Related
- state-modeling
## Contrasts With
- N/A

# Common Errors
- **Error**: Assuming `Object.freeze` makes nested objects immutable
  **Correction**: `Object.freeze` is shallow; nested objects remain mutable unless also frozen

# Common Confusions
- **Confusion**: Persistent data structures are always more efficient
  **Clarification**: They may use more memory and computation, but they reduce conceptual complexity, which matters more for program correctness

# Source Reference
Chapter 7: Project: A Robot, Section "Persistent data", lines 214-263.

# Verification Notes
- Definition source: direct
- Confidence rationale: Explicitly defined with rationale and examples
- Cross-reference status: verified against testing discussion in Ch 8
