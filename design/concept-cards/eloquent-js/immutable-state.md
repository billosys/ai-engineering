---
# === CORE IDENTIFICATION ===
concept: Immutable State
slug: immutable-state

# === CLASSIFICATION ===
category: application-architecture
subcategory: state-management
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Robot"
chapter_number: 7
pdf_page: null
section: "The task"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - immutability
  - state immutability

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
  - persistent-data-structure
extends:
  - persistent-data-structure
related:
  - state-modeling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why should state not be mutated directly?"
  - "How does immutable state simplify programs?"
---

# Quick Definition
Immutable state is an approach where state changes produce new state objects rather than modifying existing ones, leaving previous states intact for simpler reasoning and debugging.

# Core Definition
Haverbeke advocates: "let's make it so that we don't *change* this state when the robot moves but rather compute a *new* state for the situation after the move." The key insight is that "When the objects in my system are fixed, stable things, I can consider operations on them in isolation---moving to Alice's house from a given start state always produces the same new state." (Ch 7, "The task" and "Persistent data")

# Prerequisites
- **Objects**: State is typically represented as objects
- **Persistent data structures**: The mechanism for achieving immutability

# Key Properties
1. State transitions produce new state objects
2. Old state remains unchanged and inspectable
3. Operations are deterministic (same input always gives same output)
4. Makes programs easier to understand and test
5. Avoids the complexity of tracking changes over time

# Construction / Recognition
```javascript
class VillageState {
  constructor(place, parcels) {
    this.place = place;
    this.parcels = parcels;
  }
  move(destination) {
    // Returns NEW state, doesn't modify this
    let parcels = this.parcels.map(p => {
      if (p.place != this.place) return p;
      return {place: destination, address: p.address};
    }).filter(p => p.place != p.address);
    return new VillageState(destination, parcels);
  }
}
```

# Context & Application
Immutable state is especially valuable when state is shared or when you need to reason about state transitions. The chapter warns against reflexively making everything mutable objects: "Reflexively writing classes for every concept in your application tends to leave you with a collection of interconnected objects that each have their own internal, changing state. Such programs are often hard to understand and thus easy to break." (Ch 7)

# Examples
```javascript
let first = new VillageState(
  "Post Office",
  [{place: "Post Office", address: "Alice's House"}]
);
let next = first.move("Alice's House");

console.log(next.place);   // -> Alice's House
console.log(first.place);  // -> Post Office (unchanged!)
```
(Ch 7, "The task", lines 193-212)

# Relationships
## Builds Upon
- persistent-data-structure, object
## Enables
- Easier testing, simpler debugging, deterministic behavior
## Related
- state-modeling
## Contrasts With
- N/A

# Common Errors
- **Error**: Mutating state objects directly rather than creating new ones
  **Correction**: Always return new objects from state transitions; use `map`, `filter`, and spread syntax to create modified copies

# Common Confusions
- **Confusion**: Immutable state means nothing ever changes
  **Clarification**: The system progresses through a sequence of different state values; each individual value is immutable, but you keep producing new ones

# Source Reference
Chapter 7: Project: A Robot, Sections "The task" and "Persistent data", lines 147-263.

# Verification Notes
- Definition source: synthesized from multiple passages
- Confidence rationale: Central design principle of the chapter, extensively argued for
- Cross-reference status: verified against testing discussion in Ch 8
