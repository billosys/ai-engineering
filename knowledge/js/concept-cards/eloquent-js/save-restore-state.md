---
concept: Save and Restore State
slug: save-restore-state
category: graphics
subcategory: canvas-api
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Drawing on Canvas"
chapter_number: 17
pdf_page: null
section: "Storing and clearing transformations"
extraction_confidence: high
aliases:
  - canvas save
  - canvas restore
  - transformation stack
prerequisites:
  - canvas-transformation
extends: []
related:
  - translate-transform
  - rotate-transform
  - scale-transform
contrasts_with: []
answers_questions:
  - "How do I temporarily change canvas transformations?"
  - "How do I undo canvas transformation changes?"
---

# Quick Definition
`save()` pushes the current canvas state (transformations, styles) onto a stack, and `restore()` pops the most recent state, allowing temporary transformations that are cleanly reverted.

# Core Definition
"The `save` and `restore` methods on the 2D canvas context do this transformation management. They conceptually keep a stack of transformation states. When you call `save`, the current state is pushed onto the stack, and when you call `restore`, the state on top of the stack is taken off and used as the context's current transformation" (Ch. 17).

# Prerequisites
- **Canvas transformation**: save/restore manage the transformation state

# Key Properties
1. `save()` pushes current state onto stack
2. `restore()` pops and applies the top state
3. Saves include transformations, fillStyle, strokeStyle, lineWidth, font, etc.
4. Can nest multiple save/restore pairs
5. `resetTransform()` fully resets without the stack

# Construction / Recognition
```javascript
cx.save();
cx.translate(0, length);
cx.rotate(-angle);
branch(length * scale, angle, scale);
cx.restore(); // reverts translate and rotate
```

# Context & Application
Essential for any complex canvas drawing where multiple transformations are used. Without save/restore, each transformation would permanently affect all subsequent drawing.

# Examples
The fractal tree would break without save/restore: "If the calls to `save` and `restore` were not there, the second recursive call to `branch` would end up with the position and rotation created by the first call."

# Relationships
## Builds Upon
- canvas-transformation
## Enables
- Isolated transformations, hierarchical drawing, clean composition
## Related
- translate-transform, rotate-transform, scale-transform
## Contrasts With
- resetTransform() (fully resets rather than restoring previous state)

# Common Errors
- **Error**: Mismatched save/restore calls (more restores than saves)
  **Correction**: Always pair each save with exactly one restore

# Common Confusions
- **Confusion**: save/restore only saves transformations
  **Clarification**: They also save fillStyle, strokeStyle, lineWidth, font, and other context properties

# Source Reference
Chapter 17: Drawing on Canvas, Section "Storing and clearing transformations", lines 732-802 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Clearly explained with practical example
- Cross-reference status: verified
