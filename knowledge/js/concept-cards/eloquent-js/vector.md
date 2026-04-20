---
concept: Vector (2D)
slug: vector
category: graphics
subcategory: math
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Platform Game"
chapter_number: 16
pdf_page: null
section: "Actors"
extraction_confidence: high
aliases:
  - Vec
  - 2D vector
  - position vector
prerequisites:
  - class-declaration
  - object
extends: []
related:
  - actor-pattern
  - velocity
  - gravity-simulation
contrasts_with: []
answers_questions:
  - "How do you represent positions and movements in 2D space?"
  - "How do you do vector arithmetic in JavaScript?"
---

# Quick Definition
A 2D vector is an object with `x` and `y` properties representing a point or direction in two-dimensional space, with methods for addition (`plus`) and scalar multiplication (`times`).

# Core Definition
The `Vec` class used throughout the platform game stores two-dimensional values such as positions and sizes. As Haverbeke notes: "This is the `Vec` class that we'll use for our two-dimensional values, such as the position and size of actors" (Ch. 16, "Actors"). The `times` method "scales a vector by a given number. It will be useful when we need to multiply a speed vector by a time interval to get the distance traveled during that time."

# Prerequisites
- **Classes**: Vec is defined as a class
- **Objects**: Vectors are objects with x and y properties

# Key Properties
1. Immutable operations -- `plus` and `times` return new Vec instances
2. `plus(other)` adds two vectors component-wise
3. `times(factor)` multiplies both components by a scalar
4. Used for position, size, speed, and distance calculations

# Construction / Recognition
```javascript
class Vec {
  constructor(x, y) {
    this.x = x; this.y = y;
  }
  plus(other) {
    return new Vec(this.x + other.x, this.y + other.y);
  }
  times(factor) {
    return new Vec(this.x * factor, this.y * factor);
  }
}
```

# Context & Application
Used throughout game programming, physics simulations, and graphics. The immutable design (returning new vectors) fits with the persistent data approach used in the game's state management.

# Examples
Computing a player's center position:
```javascript
let center = player.pos.plus(player.size.times(0.5))
                       .times(scale);
```
Computing new position from speed and time:
```javascript
let newPos = this.pos.plus(this.speed.times(time));
```

# Relationships
## Builds Upon
- class-declaration, object
## Enables
- actor-pattern, collision-detection, gravity-simulation, canvas-transformation
## Related
- velocity, canvas-coordinate-system
## Contrasts With
- Using separate x/y variables (less composable)

# Common Errors
- **Error**: Modifying vector properties in place instead of creating new instances
  **Correction**: Always use `plus` and `times` which return new Vec objects

# Common Confusions
- **Confusion**: Vectors and points are different things
  **Clarification**: In this context they use the same Vec class; the interpretation depends on usage

# Source Reference
Chapter 16: Project: A Platform Game, Section "Actors", lines 294-314 of 16-project-a-platform-game.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Complete class definition with usage examples
- Cross-reference status: verified (referenced in Ch. 6 exercises)
