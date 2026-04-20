---
concept: Animation
slug: animation
category: graphics
subcategory: rendering
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Drawing on Canvas"
chapter_number: 17
pdf_page: null
section: "Images"
extraction_confidence: high
aliases:
  - sprite animation
  - frame animation
prerequisites:
  - requestanimationframe
  - drawimage
extends: []
related:
  - game-loop
  - sprite
contrasts_with: []
answers_questions:
  - "How do I animate a character on a canvas?"
  - "How does sprite-sheet animation work?"
---

# Quick Definition
Animation creates the illusion of movement by rapidly displaying a sequence of images (frames or sprites), cycling through them at timed intervals and clearing the previous frame before drawing the next.

# Core Definition
Chapter 17 demonstrates animation by cycling through sprites: "By alternating which pose we draw, we can show an animation that looks like a walking character." The `clearRect` method removes the previous frame, and `drawImage` with source-rectangle arguments selects the current pose from a sprite sheet.

# Prerequisites
- **requestAnimationFrame**: Schedules frame updates
- **drawImage**: Draws sprite frames onto the canvas

# Key Properties
1. Each frame of animation is drawn from a different region of a sprite sheet
2. A cycle counter tracks the current frame and wraps using the remainder operator
3. `clearRect` removes the previous frame before drawing the new one
4. Frame timing determines animation speed (e.g., switch every 60ms)

# Construction / Recognition
```javascript
let cycle = 0;
setInterval(() => {
  cx.clearRect(0, 0, spriteW, spriteH);
  cx.drawImage(img,
               cycle * spriteW, 0, spriteW, spriteH,
               0,               0, spriteW, spriteH);
  cycle = (cycle + 1) % 8;
}, 120);
```

# Context & Application
Used in games, UI animations, loading indicators, and any visual content that changes over time. Canvas-based animation requires manual clearing and redrawing since canvas does not retain shape information.

# Examples
In the game's `CanvasDisplay`, the player sprite is selected based on movement state:
```javascript
let tile = 8; // standing still
if (player.speed.y != 0) {
  tile = 9; // jumping
} else if (player.speed.x != 0) {
  tile = Math.floor(Date.now() / 60) % 8; // walking cycle
}
```

# Relationships
## Builds Upon
- requestanimationframe, drawimage, canvas-element
## Enables
- Game character movement, visual feedback, interactive graphics
## Related
- sprite, game-loop, canvas-context
## Contrasts With
- CSS animations (declarative, handled by browser)

# Common Errors
- **Error**: Not clearing the canvas before drawing the next frame
  **Correction**: Use `clearRect` or redraw the entire background each frame

# Common Confusions
- **Confusion**: Animation requires a different image file for each frame
  **Clarification**: Sprite sheets pack all frames into one image; `drawImage` selects a region

# Source Reference
Chapter 17: Drawing on Canvas, Section "Images", lines 556-606 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Complete code example with explanation
- Cross-reference status: verified
