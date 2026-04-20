---
concept: Persistent Data Structure
slug: persistent-state
category: application-architecture
subcategory: state-management
tier: advanced
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Platform Game"
chapter_number: 16
pdf_page: null
section: "Reading a level"
extraction_confidence: high
aliases:
  - immutable state
  - persistent data
prerequisites:
  - object
  - game-state
extends: []
related:
  - state-management
  - undo-functionality
contrasts_with: []
answers_questions:
  - "What is a persistent data structure?"
  - "Why use immutable state in applications?"
---

# Quick Definition
A persistent data structure preserves its previous version when modified, so updates create new versions while leaving old ones intact, enabling features like undo and simplifying reasoning about state changes.

# Core Definition
Haverbeke introduces this pattern: "This is again a persistent data structure -- updating the game state creates a new state and leaves the old one intact" (Ch. 16). The game's State, actors, and Vec objects all follow this pattern -- methods like `update` and `plus` return new instances rather than modifying existing ones.

# Prerequisites
- **Objects**: Understanding that objects can be treated as values
- **Game state**: The primary use case in the book

# Key Properties
1. Updates return new objects instead of mutating existing ones
2. Old versions remain accessible and unchanged
3. Shared structure is safe because nothing is mutated
4. Enables time-travel debugging, undo, and replay

# Construction / Recognition
The pattern is recognized by methods that return new instances:
```javascript
// Vec returns new instances
plus(other) {
  return new Vec(this.x + other.x, this.y + other.y);
}

// State update returns new State
State.prototype.update = function(time, keys) {
  let actors = this.actors.map(actor => actor.update(time, this, keys));
  let newState = new State(this.level, actors, this.status);
  // ...
  return newState;
};
```

# Context & Application
Used extensively in functional programming, React/Redux, and game development. The pixel art editor in Chapter 19 also uses this pattern for its Picture class, enabling undo history.

# Examples
In Chapter 19, immutable pictures enable undo:
```javascript
class Picture {
  draw(pixels) {
    let copy = this.pixels.slice();
    for (let {x, y, color} of pixels) {
      copy[x + y * this.width] = color;
    }
    return new Picture(this.width, this.height, copy);
  }
}
```

# Relationships
## Builds Upon
- object, array
## Enables
- undo-functionality, state-management, time-travel debugging
## Related
- game-state, application-state-update
## Contrasts With
- Mutable data structures (modify in place, overwrite previous state)

# Common Errors
- **Error**: Accidentally mutating a "persistent" object via property assignment
  **Correction**: Use methods that return new instances; consider Object.freeze in development

# Common Confusions
- **Confusion**: Persistent means "saved to disk"
  **Clarification**: In data structure terminology, persistent means previous versions are preserved in memory

# Source Reference
Chapter 16: Project: A Platform Game, Section "Reading a level", line 259-261; Chapter 19, Section "The state" and "Undo history".

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Explicitly named and used across multiple chapters
- Cross-reference status: verified (Ch. 16, 19)
