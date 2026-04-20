---
concept: Game State
slug: game-state
category: application-architecture
subcategory: state-management
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Platform Game"
chapter_number: 16
pdf_page: null
section: "Reading a level"
extraction_confidence: high
aliases:
  - state object
  - persistent state
prerequisites:
  - class-declaration
  - object
extends: []
related:
  - actor-pattern
  - game-loop
  - persistent-state
contrasts_with: []
answers_questions:
  - "How do you track the current state of a game?"
  - "What must I know before building a web application?"
---

# Quick Definition
Game state is an immutable object that captures the complete current situation of a game -- the level, all actors, and the play status -- updated each frame by producing a new state rather than mutating the existing one.

# Core Definition
The `State` class tracks a running game: "This is again a persistent data structure -- updating the game state creates a new state and leaves the old one intact" (Ch. 16, "Reading a level"). The state has `level`, `actors`, and `status` ("playing", "lost", or "won") properties. The `update` method returns a new State reflecting changes from one time step.

# Prerequisites
- **Classes**: State is a class with constructor and methods
- **Objects**: State is an immutable value object

# Key Properties
1. `level` -- the Level object (static, never changes)
2. `actors` -- array of current actor objects
3. `status` -- "playing", "lost", or "won"
4. `player` getter finds the player actor in the actors array
5. `update(time, keys)` returns a new State

# Construction / Recognition
```javascript
class State {
  constructor(level, actors, status) {
    this.level = level;
    this.actors = actors;
    this.status = status;
  }
  static start(level) {
    return new State(level, level.startActors, "playing");
  }
  get player() {
    return this.actors.find(a => a.type == "player");
  }
}
```

# Context & Application
Immutable state is a key pattern in application architecture. By treating state as a value rather than a mutable object, you gain simpler reasoning, easier undo/replay, and fewer bugs from shared mutation.

# Examples
The game loop updates state each frame:
```javascript
runAnimation(time => {
  state = state.update(time, arrowKeys);
  display.syncState(state);
  if (state.status == "playing") return true;
  // ...
});
```

# Relationships
## Builds Upon
- class-declaration, object, array
## Enables
- game-loop rendering, collision response, win/lose detection
## Related
- persistent-state, actor-pattern, state-management
## Contrasts With
- Mutable state (modifying objects in place)

# Common Errors
- **Error**: Mutating the state object directly
  **Correction**: Always create new State instances; the old state should remain unchanged

# Common Confusions
- **Confusion**: Creating new state objects every frame is wasteful
  **Clarification**: JavaScript is efficient with short-lived objects; the clarity benefits outweigh the minor cost

# Source Reference
Chapter 16: Project: A Platform Game, Section "Reading a level", lines 233-261 of 16-project-a-platform-game.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Explicitly described as persistent data structure
- Cross-reference status: verified
