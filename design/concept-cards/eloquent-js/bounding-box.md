---
concept: Bounding Box
slug: bounding-box
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
  - AABB
  - axis-aligned bounding box
prerequisites:
  - vector
extends: []
related:
  - collision-detection
  - actor-pattern
contrasts_with: []
answers_questions:
  - "How are game object boundaries represented for collision detection?"
---

# Quick Definition
A bounding box is an axis-aligned rectangle defined by a position (upper-left corner) and size, used to represent an actor's physical extent for collision detection.

# Core Definition
Every actor in the game has `pos` and `size` properties (both Vec objects) defining its bounding box. The `overlap` function tests whether two such rectangles intersect by checking both axes simultaneously. The `touches` method tests whether a bounding box overlaps any grid cell of a given type.

# Prerequisites
- **Vector**: Position and size are Vec objects

# Key Properties
1. Defined by position (upper-left) and size (width, height)
2. Axis-aligned (sides parallel to coordinate axes)
3. Overlap test: two boxes overlap when they overlap on BOTH axes
4. Grid overlap uses floor/ceil to find affected tiles

# Construction / Recognition
```javascript
function overlap(actor1, actor2) {
  return actor1.pos.x + actor1.size.x > actor2.pos.x &&
         actor1.pos.x < actor2.pos.x + actor2.size.x &&
         actor1.pos.y + actor1.size.y > actor2.pos.y &&
         actor1.pos.y < actor2.pos.y + actor2.size.y;
}
```

# Context & Application
AABB collision is the simplest and most common form of collision detection in 2D games. Fast to compute and sufficient for rectangular entities.

# Examples
Actor sizes in the game: Player is 0.8 x 1.5 units, Lava and Coin are 1x1 and 0.6x0.6 respectively.

# Relationships
## Builds Upon
- vector
## Enables
- collision-detection
## Related
- actor-pattern, game-state
## Contrasts With
- Pixel-perfect collision, circle-based collision

# Common Errors
- **Error**: Using `>=` instead of `>` in overlap checks (touching edges count as overlap)
  **Correction**: The convention depends on game design; the source uses strict `>` for overlap

# Common Confusions
- **Confusion**: Bounding boxes match the visual shape of the sprite
  **Clarification**: They are rectangular approximations; the visual sprite may have irregular shapes

# Source Reference
Chapter 16: Project: A Platform Game, Section "Motion and collision", lines 888-900 of 16-project-a-platform-game.md.

# Verification Notes
- Definition source: synthesized from code and context
- Confidence rationale: Core mechanic with clear code
- Cross-reference status: verified
