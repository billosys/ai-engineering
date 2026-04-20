---
concept: Velocity
slug: velocity
category: application-architecture
subcategory: game-physics
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
  - speed vector
prerequisites:
  - vector
extends: []
related:
  - gravity-simulation
  - collision-detection
  - game-loop
contrasts_with: []
answers_questions:
  - "How is movement represented in a game?"
  - "How do you calculate distance from speed and time?"
---

# Quick Definition
Velocity is a vector representing an object's speed and direction of movement, measured in game units per second and multiplied by the time step to compute displacement each frame.

# Core Definition
In the platform game, actors have a `speed` property (a Vec) representing their velocity. As Haverbeke explains: "We'll measure time in seconds, so speeds are expressed in units per second" (Ch. 16, "Motion and collision"). Displacement per frame is calculated as `speed.times(time)`, where `time` is the elapsed seconds since the last frame.

# Prerequisites
- **Vector**: Velocity is stored as a Vec with x and y components

# Key Properties
1. Expressed in units per second (not per frame)
2. Multiplied by time step to get frame displacement
3. Can be modified by gravity (vertical acceleration)
4. Different actors have different speed constants (playerXSpeed = 7, jumpSpeed = 17)

# Construction / Recognition
```javascript
const playerXSpeed = 7;
const gravity = 30;
const jumpSpeed = 17;

// Computing new position
let newPos = this.pos.plus(this.speed.times(time));

// Applying gravity to vertical speed
let ySpeed = this.speed.y + time * gravity;
```

# Context & Application
Fundamental to any physics-based game. Time-based velocity ensures consistent movement regardless of frame rate.

# Examples
Lava movement:
```javascript
Lava.prototype.update = function(time, state) {
  let newPos = this.pos.plus(this.speed.times(time));
  if (!state.level.touches(newPos, this.size, "wall")) {
    return new Lava(newPos, this.speed, this.reset);
  } else if (this.reset) {
    return new Lava(this.reset, this.speed, this.reset);
  } else {
    return new Lava(this.pos, this.speed.times(-1));
  }
};
```

# Relationships
## Builds Upon
- vector
## Enables
- Movement, gravity-simulation, collision-detection
## Related
- game-loop, actor-pattern
## Contrasts With
- Frame-based movement (moves fixed amount per frame regardless of time)

# Common Errors
- **Error**: Using velocity as pixels-per-frame instead of units-per-second
  **Correction**: Always multiply by the time step to get frame-rate-independent movement

# Common Confusions
- **Confusion**: Speed and velocity are interchangeable
  **Clarification**: Velocity includes direction (it's a vector); speed is the magnitude

# Source Reference
Chapter 16: Project: A Platform Game, Section "Motion and collision" and "Actor updates", lines 759-1005 of 16-project-a-platform-game.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Multiple code examples showing velocity usage
- Cross-reference status: verified
