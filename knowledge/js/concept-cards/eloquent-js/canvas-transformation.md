---
concept: Canvas Transformation
slug: canvas-transformation
category: graphics
subcategory: canvas-api
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Drawing on Canvas"
chapter_number: 17
pdf_page: null
section: "Transformation"
extraction_confidence: high
aliases:
  - canvas transform
  - coordinate transformation
prerequisites:
  - canvas-context
extends: []
related:
  - translate-transform
  - rotate-transform
  - scale-transform
  - save-restore-state
contrasts_with: []
answers_questions:
  - "How do I transform drawings on a canvas?"
  - "How do canvas transformations stack?"
---

# Quick Definition
Canvas transformations modify the coordinate system used for subsequent drawing operations, using `translate`, `rotate`, and `scale` methods that stack (compose) with each other.

# Core Definition
"There are several other methods besides `scale` that influence the coordinate system for a canvas. You can rotate subsequently drawn shapes with the `rotate` method and move them with the `translate` method. The interesting -- and confusing -- thing is that these transformations stack, meaning that each one happens relative to the previous transformations" (Ch. 17, "Transformation").

# Prerequisites
- **Canvas context**: Transformations operate on the context's coordinate system

# Key Properties
1. `translate(x, y)` shifts the origin
2. `rotate(angle)` rotates around the current origin (radians)
3. `scale(x, y)` scales subsequent drawing
4. Transformations stack/compose -- order matters
5. Negative scale flips the drawing (e.g., `scale(-1, 1)` mirrors horizontally)

# Construction / Recognition
```javascript
// Flip horizontally around a point
function flipHorizontally(context, around) {
  context.translate(around, 0);
  context.scale(-1, 1);
  context.translate(-around, 0);
}
```

# Context & Application
Used for rotating sprites, mirroring characters, zooming, and building complex scenes from simpler parts. The stacking behavior enables hierarchical transformations (e.g., rotating a tree branch).

# Examples
The fractal tree example uses stacking transformations:
```javascript
function branch(length, angle, scale) {
  cx.fillRect(0, 0, 1, length);
  if (length < 8) return;
  cx.save();
  cx.translate(0, length);
  cx.rotate(-angle);
  branch(length * scale, angle, scale);
  cx.rotate(2 * angle);
  branch(length * scale, angle, scale);
  cx.restore();
}
```

# Relationships
## Builds Upon
- canvas-context
## Enables
- Sprite mirroring, scene composition, hierarchical animation
## Related
- save-restore-state, translate-transform, rotate-transform, scale-transform
## Contrasts With
- CSS transforms (applied to DOM elements, not drawing operations)

# Common Errors
- **Error**: Forgetting that transformations affect all subsequent drawing
  **Correction**: Use save/restore to isolate transformations

# Common Confusions
- **Confusion**: translate(50, 50) then rotate(0.1) is the same as rotate(0.1) then translate(50, 50)
  **Clarification**: Order matters -- the second transformation happens in the already-transformed coordinate system

# Source Reference
Chapter 17: Drawing on Canvas, Section "Transformation", lines 608-730 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Thorough explanation with diagrams referenced
- Cross-reference status: verified
