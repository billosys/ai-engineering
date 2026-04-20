---
concept: Translate Transform
slug: translate-transform
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
  - canvas translate
prerequisites:
  - canvas-transformation
extends:
  - canvas-transformation
related:
  - rotate-transform
  - scale-transform
contrasts_with: []
answers_questions:
  - "How do I move the drawing origin on a canvas?"
---

# Quick Definition
`translate(x, y)` shifts the canvas coordinate system's origin, causing all subsequent drawing to happen relative to the new origin point.

# Core Definition
The translate method moves the coordinate system origin. "If we translate by 10 horizontal pixels twice, everything will be drawn 20 pixels to the right" (Ch. 17). Combined with rotate and scale, it enables drawing complex scenes where each element has its own local coordinate system.

# Prerequisites
- **Canvas transformation**: translate is one of three basic transformations

# Key Properties
1. Shifts origin by (x, y) pixels
2. Stacks with previous transformations
3. Used to set a local coordinate system for drawing operations
4. Combined with scale(-1,1) to mirror around a point

# Construction / Recognition
```javascript
cx.translate(300, 0); // move origin to (300, 0)
branch(60, 0.5, 0.8); // draw tree centered at new origin
```

# Context & Application
Used to draw at different positions without adjusting every coordinate, to set up local coordinate systems for components, and as part of flip/mirror operations.

# Examples
From the flipHorizontally helper:
```javascript
context.translate(around, 0);
context.scale(-1, 1);
context.translate(-around, 0);
```

# Relationships
## Builds Upon
- canvas-transformation, canvas-context
## Enables
- Local coordinate systems, hierarchical drawing
## Related
- rotate-transform, scale-transform, save-restore-state
## Contrasts With
- Manually adding offsets to every draw call

# Common Errors
- **Error**: Forgetting that translate is cumulative
  **Correction**: Use save/restore to contain the effect

# Common Confusions
- **Confusion**: translate moves existing drawings
  **Clarification**: It only affects future drawing operations

# Source Reference
Chapter 17: Drawing on Canvas, Section "Transformation", lines 658-670 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Used in multiple examples
- Cross-reference status: verified
