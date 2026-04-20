---
# === CORE IDENTIFICATION ===
concept: State Modeling
slug: state-modeling

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
  - state representation
  - domain modeling

# === TYPED RELATIONSHIPS ===
prerequisites:
  - object
  - class-declaration
extends: []
related:
  - immutable-state
  - persistent-data-structure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How should I represent state in a program?"
  - "Why is minimal state important?"
---

# Quick Definition
State modeling is the practice of condensing a system's state to the minimal set of values that define it, choosing data representations that make the program easier to understand and work with.

# Core Definition
Haverbeke advises: "let's condense the village's state down to the minimal set of values that define it. There's the robot's current location and the collection of undelivered parcels, each of which has a current location and a destination address. That's it." He warns against the OOP reflex of "defining objects for the various elements in the world" when simpler representations suffice. (Ch 7, "The task")

# Prerequisites
- **Objects**: State is represented using objects
- **Class declarations**: Classes can encapsulate state and transitions

# Key Properties
1. Identify the minimal set of values that define the state
2. Resist creating classes for every real-world concept
3. Prefer simple data over complex object hierarchies
4. State transitions should produce new state values, not mutate existing ones

# Construction / Recognition
Good state modeling is recognized by minimal, focused state classes:
```javascript
class VillageState {
  constructor(place, parcels) {
    this.place = place;       // robot's location
    this.parcels = parcels;   // undelivered parcels with place and address
  }
}
```

# Context & Application
The chapter explicitly warns against over-modeling: "The fact that something sounds like an object does not automatically mean that it should be an object in your program. Reflexively writing classes for every concept in your application tends to leave you with a collection of interconnected objects that each have their own internal, changing state. Such programs are often hard to understand and thus easy to break." (Ch 7)

# Examples
Instead of separate Robot, Parcel, and Place classes with mutable state, the chapter models the entire world as two values:
```javascript
class VillageState {
  constructor(place, parcels) {
    this.place = place;
    this.parcels = parcels;
  }
  move(destination) {
    // ...returns new VillageState
  }
}
```
(Ch 7, "The task", lines 152-169)

# Relationships
## Builds Upon
- object, class-declaration
## Enables
- immutable-state, persistent-data-structure
## Related
- graph-data-structure
## Contrasts With
- N/A

# Common Errors
- **Error**: Creating a class for every noun in the problem domain
  **Correction**: Focus on the minimal state that defines the system; use simple data structures where possible

# Common Confusions
- **Confusion**: More classes means better organization
  **Clarification**: Unnecessary classes create coupling and complexity; choose the simplest representation that works

# Source Reference
Chapter 7: Project: A Robot, Section "The task", lines 117-169.

# Verification Notes
- Definition source: synthesized from the chapter's design approach
- Confidence rationale: Central design lesson of the chapter, explicitly argued
- Cross-reference status: verified against module design discussion in Ch 10
