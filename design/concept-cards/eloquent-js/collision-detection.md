---
concept: Collision Detection
slug: collision-detection
category: application-architecture
subcategory: game-mechanics
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Platform Game"
chapter_number: 16
pdf_page: null
section: "Motion and collision"
extraction_confidence: high
aliases:
  - hit detection
  - overlap detection
prerequisites:
  - vector
  - bounding-box
extends: []
related:
  - game-state
  - actor-pattern
contrasts_with: []
answers_questions:
  - "How do games detect when objects touch each other?"
  - "How is collision detection implemented for rectangular objects?"
---

# Quick Definition
Collision detection determines whether game objects overlap or touch, enabling the game to respond to interactions like a player hitting a wall or collecting a coin.

# Core Definition
The platform game uses two forms of collision detection: grid-based (testing whether a moving rectangle overlaps wall or lava tiles) and actor-based (testing whether two actors overlap). As Haverbeke describes: "Before moving the player or a block of lava, we test whether the motion would take it inside of a wall. If it does, we simply cancel the motion altogether" (Ch. 16, "Motion and collision").

# Prerequisites
- **Vectors**: Positions and sizes are represented as Vec objects
- **Bounding boxes**: Actors are represented as axis-aligned rectangles

# Key Properties
1. Grid collision uses `Math.floor` and `Math.ceil` to find overlapping tiles
2. Actor overlap checks both x-axis and y-axis simultaneously
3. Collision response depends on actor type (stop, bounce, collect, lose)
4. Areas outside the level are treated as walls

# Construction / Recognition
Grid-based collision:
```javascript
Level.prototype.touches = function(pos, size, type) {
  let xStart = Math.floor(pos.x);
  let xEnd = Math.ceil(pos.x + size.x);
  let yStart = Math.floor(pos.y);
  let yEnd = Math.ceil(pos.y + size.y);
  for (let y = yStart; y < yEnd; y++) {
    for (let x = xStart; x < xEnd; x++) {
      let isOutside = x < 0 || x >= this.width ||
                      y < 0 || y >= this.height;
      let here = isOutside ? "wall" : this.rows[y][x];
      if (here == type) return true;
    }
  }
  return false;
};
```

Actor overlap:
```javascript
function overlap(actor1, actor2) {
  return actor1.pos.x + actor1.size.x > actor2.pos.x &&
         actor1.pos.x < actor2.pos.x + actor2.size.x &&
         actor1.pos.y + actor1.size.y > actor2.pos.y &&
         actor1.pos.y < actor2.pos.y + actor2.size.y;
}
```

# Context & Application
Essential for any game or interactive simulation with physical objects. The grid-based approach is efficient for tile-based levels, while axis-aligned bounding box (AABB) overlap is the simplest form of actor collision.

# Examples
From the `State.update` method:
```javascript
if (this.level.touches(player.pos, player.size, "lava")) {
  return new State(this.level, actors, "lost");
}
for (let actor of actors) {
  if (actor != player && overlap(actor, player)) {
    newState = actor.collide(newState);
  }
}
```

# Relationships
## Builds Upon
- vector, bounding-box, level-representation
## Enables
- Game mechanics (collecting coins, dying from lava, walking on floors)
## Related
- game-state, actor-pattern, gravity-simulation
## Contrasts With
- Pixel-perfect collision (more precise but much more expensive)

# Common Errors
- **Error**: Using large time steps that cause objects to pass through each other
  **Correction**: Keep time steps small or use swept collision detection

# Common Confusions
- **Confusion**: Collision detection and collision response are the same thing
  **Clarification**: Detection finds overlaps; response determines what happens (stop, bounce, destroy)

# Source Reference
Chapter 16: Project: A Platform Game, Section "Motion and collision", lines 759-919 of 16-project-a-platform-game.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Two complete code examples with thorough explanation
- Cross-reference status: verified
