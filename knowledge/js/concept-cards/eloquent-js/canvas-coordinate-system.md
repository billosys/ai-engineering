---
concept: Canvas Coordinate System
slug: canvas-coordinate-system
category: graphics
subcategory: canvas-api
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Drawing on Canvas"
chapter_number: 17
pdf_page: null
section: "The canvas element"
extraction_confidence: high
aliases:
  - screen coordinates
prerequisites:
  - canvas-element
extends: []
related:
  - canvas-transformation
  - vector
contrasts_with: []
answers_questions:
  - "How does the canvas coordinate system work?"
  - "Where is (0,0) on a canvas?"
---

# Quick Definition
The canvas coordinate system places (0, 0) at the upper-left corner, with the positive x-axis extending right and the positive y-axis extending down, measured in pixels.

# Core Definition
"Just like in HTML (and SVG), the coordinate system that the canvas uses puts (0, 0) at the upper-left corner, and the positive y-axis goes down from there. This means (10, 10) is 10 pixels below and to the right of the upper-left corner" (Ch. 17, "The canvas element").

# Prerequisites
- **Canvas element**: The coordinate system applies to the canvas

# Key Properties
1. Origin (0,0) at upper-left corner
2. X increases rightward
3. Y increases downward (opposite of math convention)
4. Units are pixels by default
5. Transformations (translate, rotate, scale) modify the system

# Construction / Recognition
```javascript
context.fillRect(10, 10, 100, 50);
// Draws at 10 pixels right and 10 pixels down from upper-left
```

# Context & Application
Understanding the coordinate system is essential for all canvas drawing. The y-axis direction can be counterintuitive for those accustomed to mathematical coordinate systems.

# Examples
Default canvas size: "When no `width` or `height` attribute is specified, a canvas element gets a default width of 300 pixels and height of 150 pixels."

# Relationships
## Builds Upon
- canvas-element
## Enables
- All drawing operations, canvas-transformation
## Related
- vector, translate-transform
## Contrasts With
- Mathematical coordinates (y up), geographic coordinates

# Common Errors
- **Error**: Drawing with y-up assumption (shapes appear upside down)
  **Correction**: Remember y increases downward on canvas

# Common Confusions
- **Confusion**: Canvas pixels and CSS pixels are the same
  **Clarification**: On high-DPI displays they may differ; canvas width/height set the drawing resolution

# Source Reference
Chapter 17: Drawing on Canvas, Section "The canvas element", lines 160-163 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Explicitly stated
- Cross-reference status: verified
