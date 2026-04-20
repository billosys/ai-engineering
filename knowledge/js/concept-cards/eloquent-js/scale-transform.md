---
concept: Scale Transform
slug: scale-transform
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
  - canvas scale
prerequisites:
  - canvas-transformation
extends:
  - canvas-transformation
related:
  - translate-transform
  - rotate-transform
contrasts_with: []
answers_questions:
  - "How do I scale or mirror drawings on a canvas?"
---

# Quick Definition
`scale(x, y)` multiplies all subsequent drawing coordinates by the given factors, allowing stretching, shrinking, and mirroring (via negative values).

# Core Definition
"Calling the `scale` method will cause anything drawn after it to be scaled. This method takes two parameters, one to set a horizontal scale and one to set a vertical scale" (Ch. 17). "Scaling by a negative amount will flip the picture around. The flipping happens around point (0, 0)."

# Prerequisites
- **Canvas transformation**: scale is a core transformation

# Key Properties
1. `scale(x, y)` affects all dimensions including line width
2. `scale(-1, 1)` mirrors horizontally
3. `scale(1, -1)` mirrors vertically
4. Flipping changes coordinate direction

# Construction / Recognition
```javascript
cx.scale(3, .5); // 3x wider, half as tall
cx.beginPath();
cx.arc(50, 50, 40, 0, 7);
cx.stroke(); // draws an ellipse
```

# Context & Application
Used for zooming, mirroring sprites (left-facing vs right-facing characters), creating reflections, and adapting drawing to different resolutions.

# Examples
Mirroring a character:
```javascript
function flipHorizontally(context, around) {
  context.translate(around, 0);
  context.scale(-1, 1);
  context.translate(-around, 0);
}
```

# Relationships
## Builds Upon
- canvas-transformation
## Enables
- Sprite mirroring, zoom, resolution independence
## Related
- translate-transform, rotate-transform, save-restore-state
## Contrasts With
- Drawing at different sizes manually

# Common Errors
- **Error**: Forgetting that scale affects line widths too
  **Correction**: Adjust lineWidth to compensate, or use save/restore around scaled drawing

# Common Confusions
- **Confusion**: scale(-1, 1) makes things invisible
  **Clarification**: It mirrors around (0,0), so content at positive x moves to negative x. Combine with translate to keep content visible.

# Source Reference
Chapter 17: Drawing on Canvas, Section "Transformation", lines 617-655 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Clear explanation with mirroring example
- Cross-reference status: verified
