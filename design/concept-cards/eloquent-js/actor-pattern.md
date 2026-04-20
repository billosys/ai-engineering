---
concept: Actor Pattern
slug: actor-pattern
category: application-architecture
subcategory: game-design
tier: advanced
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Platform Game"
chapter_number: 16
pdf_page: null
section: "Actors"
extraction_confidence: high
aliases:
  - game actor
  - game entity
prerequisites:
  - class-declaration
  - object
extends: []
related:
  - game-state
  - collision-detection
contrasts_with: []
answers_questions:
  - "How do you represent moving game entities?"
  - "What interface should game objects share?"
---

# Quick Definition
The actor pattern represents moving game entities (players, enemies, items) as objects conforming to a shared interface with `pos`, `size`, `type`, `update`, and `collide` properties.

# Core Definition
As Haverbeke describes: "Actor objects represent the current position and state of a given moving element in our game. All actor objects conform to the same interface. They have `size` and `pos` properties holding the size and the coordinates of the upper-left corner of the rectangle representing this actor, and an `update` method" (Ch. 16, "Actors"). Each actor class also has a static `create` method for construction from level data.

# Prerequisites
- **Classes**: Actors are defined as classes (Player, Lava, Coin)
- **Objects**: Actors are objects with a defined interface

# Key Properties
1. `pos` -- Vec representing upper-left corner position
2. `size` -- Vec representing width and height
3. `type` -- string identifying the actor kind ("player", "coin", "lava")
4. `update(time, state, keys)` -- returns a new actor for the next frame
5. Static `create(pos, ch)` -- factory method for level parsing

# Construction / Recognition
```javascript
class Player {
  constructor(pos, speed) {
    this.pos = pos;
    this.speed = speed;
  }
  get type() { return "player"; }
  static create(pos) {
    return new Player(pos.plus(new Vec(0, -0.5)),
                      new Vec(0, 0));
  }
}
Player.prototype.size = new Vec(0.8, 1.5);
```

# Context & Application
Used in any game or simulation where multiple types of moving entities need to be managed uniformly. The shared interface allows the game loop to update and draw all actors generically.

# Examples
The `levelChars` object maps characters to actor classes:
```javascript
const levelChars = {
  ".": "empty", "#": "wall", "+": "lava",
  "@": Player, "o": Coin,
  "=": Lava, "|": Lava, "v": Lava
};
```

# Relationships
## Builds Upon
- class-declaration, prototype, object
## Enables
- collision-detection, game-state updates, display rendering
## Related
- vector, game-loop, display-abstraction
## Contrasts With
- Monolithic game object (single class handling all entity types)

# Common Errors
- **Error**: Mutating actor objects in the update method
  **Correction**: Return new actor instances; actors are treated as immutable values

# Common Confusions
- **Confusion**: Actors store their own rendering logic
  **Clarification**: Actors only hold state; rendering is handled by the display module

# Source Reference
Chapter 16: Project: A Platform Game, Section "Actors", lines 263-457 of 16-project-a-platform-game.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Thoroughly explained with multiple class examples
- Cross-reference status: verified
