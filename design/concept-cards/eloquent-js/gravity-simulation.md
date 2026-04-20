---
concept: Gravity Simulation
slug: gravity-simulation
category: application-architecture
subcategory: game-physics
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Platform Game"
chapter_number: 16
pdf_page: null
section: "Actor updates"
extraction_confidence: high
aliases:
  - gravity
  - falling physics
prerequisites:
  - velocity
  - vector
extends: []
related:
  - collision-detection
  - game-loop
contrasts_with: []
answers_questions:
  - "How do you simulate gravity in a 2D game?"
  - "How does jumping work in a platform game?"
---

# Quick Definition
Gravity simulation accelerates an object's vertical speed downward each frame by adding a constant (gravity) multiplied by the time step, creating realistic falling and jumping behavior.

# Core Definition
In the player update method, vertical speed is increased each frame: `let ySpeed = this.speed.y + time * gravity`. The gravity constant is 30 units/second^2. Jumping sets the vertical speed to a large negative value (`-jumpSpeed`), and gravity gradually decelerates then reverses it.

# Prerequisites
- **Velocity**: Gravity modifies the vertical component of velocity
- **Vector**: Positions and speeds are Vec objects

# Key Properties
1. Gravity is a constant downward acceleration (30 units/s^2)
2. Applied by adding `time * gravity` to vertical speed each frame
3. Jumping sets vertical speed to `-jumpSpeed` (17 units/s upward)
4. Player can only jump when touching the ground (ySpeed > 0 and hitting wall below)

# Construction / Recognition
```javascript
const gravity = 30;
const jumpSpeed = 17;

Player.prototype.update = function(time, state, keys) {
  // ... horizontal movement ...
  let ySpeed = this.speed.y + time * gravity;
  let movedY = pos.plus(new Vec(0, ySpeed * time));
  if (!state.level.touches(movedY, this.size, "wall")) {
    pos = movedY;
  } else if (keys.ArrowUp && ySpeed > 0) {
    ySpeed = -jumpSpeed;
  } else {
    ySpeed = 0;
  }
  return new Player(pos, new Vec(xSpeed, ySpeed));
};
```

# Context & Application
Gravity simulation is essential in platform games and physics simulations. The simple Euler integration approach (speed += acceleration * time) works well for games with small time steps.

# Examples
From Chapter 16: "The player's vertical speed (`ySpeed`) is first accelerated to account for gravity. We check for walls again. If we don't hit any, the new position is used. If there is a wall, there are two possible outcomes. When the up arrow is pressed and we are moving down (meaning the thing we hit is below us), the speed is set to a relatively large, negative value."

# Relationships
## Builds Upon
- velocity, vector, collision-detection
## Enables
- Jumping, falling, realistic platformer movement
## Related
- game-loop, actor-pattern
## Contrasts With
- Fixed-position movement (no acceleration)

# Common Errors
- **Error**: Applying gravity only when the player is not on the ground
  **Correction**: Gravity should always be applied; collision with the floor sets speed to 0

# Common Confusions
- **Confusion**: Gravity values were calculated from real physics
  **Clarification**: As Haverbeke notes, constants "were determined by simply trying out some numbers and seeing which ones felt right"

# Source Reference
Chapter 16: Project: A Platform Game, Section "Actor updates", lines 974-1031 of 16-project-a-platform-game.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Complete implementation with physics explanation
- Cross-reference status: verified
