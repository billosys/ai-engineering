---
concept: Rotate Transform
slug: rotate-transform
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
  - canvas rotate
prerequisites:
  - canvas-transformation
extends:
  - canvas-transformation
related:
  - translate-transform
  - scale-transform
contrasts_with: []
answers_questions:
  - "How do I rotate drawings on a canvas?"
---

# Quick Definition
`rotate(angle)` rotates all subsequent canvas drawing operations around the current origin by the specified angle in radians.

# Core Definition
The `rotate` method rotates the coordinate system around the current origin. To rotate around a specific point, first translate to that point, then rotate. "If we first move the center of the coordinate system to (50, 50) and then rotate by 20 degrees (about 0.1pi radians), that rotation will happen around point (50, 50)" (Ch. 17).

# Prerequisites
- **Canvas transformation**: rotate is a core transformation method

# Key Properties
1. Angle is in radians (not degrees)
2. Rotation is around the current origin (0,0 after any translations)
3. Stacks with other transformations
4. To rotate around a point P: translate to P, rotate, translate back

# Construction / Recognition
```javascript
cx.save();
cx.translate(0, length);
cx.rotate(-angle);
branch(length * scale, angle, scale);
cx.restore();
```

# Context & Application
Used for rotating sprites, drawing clocks, creating radial patterns, and building fractal structures.

# Examples
The fractal tree rotates branches:
```javascript
cx.rotate(-angle);
branch(length * scale, angle, scale);
cx.rotate(2 * angle);
branch(length * scale, angle, scale);
```

# Relationships
## Builds Upon
- canvas-transformation
## Enables
- Rotated sprites, radial layouts, fractals
## Related
- translate-transform, scale-transform, save-restore-state
## Contrasts With
- CSS rotate (declarative, applied to element)

# Common Errors
- **Error**: Using degrees instead of radians
  **Correction**: Convert with `degrees * Math.PI / 180`

# Common Confusions
- **Confusion**: rotate(angle) rotates existing drawings
  **Clarification**: It only rotates the coordinate system for future drawings

# Source Reference
Chapter 17: Drawing on Canvas, Section "Transformation", lines 658-670 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Used in fractal tree example
- Cross-reference status: verified
