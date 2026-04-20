---
concept: Canvas Context
slug: canvas-context
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
  - 2D rendering context
  - drawing context
  - CanvasRenderingContext2D
prerequisites:
  - canvas-element
extends: []
related:
  - fill-and-stroke
  - path-drawing
  - canvas-transformation
contrasts_with: []
answers_questions:
  - "How do I get a drawing interface for a canvas?"
  - "What is a canvas context?"
---

# Quick Definition
A canvas context is an object obtained via `canvas.getContext("2d")` that provides methods and properties for drawing shapes, text, and images onto a canvas element.

# Core Definition
"The `<canvas>` tag is intended to allow different styles of drawing. To get access to an actual drawing interface, we first need to create a context, an object whose methods provide the drawing interface" (Ch. 17). The 2D context provides methods like `fillRect`, `strokeRect`, `beginPath`, `fill`, `stroke`, `drawImage`, and transformation methods.

# Prerequisites
- **Canvas element**: The context is obtained from a canvas element

# Key Properties
1. Created via `canvas.getContext("2d")`
2. Drawing state includes fillStyle, strokeStyle, lineWidth, font
3. State is set via properties, not method arguments
4. Supports "2d", "webgl", and "webgpu" context types

# Construction / Recognition
```javascript
let canvas = document.querySelector("canvas");
let cx = canvas.getContext("2d");
cx.fillStyle = "red";
cx.fillRect(10, 10, 100, 50);
```

# Context & Application
The context is the primary interface for all canvas drawing operations. All shapes, text, images, and transformations go through the context object.

# Examples
Drawing with different styles:
```javascript
let cx = document.querySelector("canvas").getContext("2d");
cx.strokeStyle = "blue";
cx.strokeRect(5, 5, 50, 50);
cx.lineWidth = 5;
cx.strokeRect(135, 5, 50, 50);
```

# Relationships
## Builds Upon
- canvas-element
## Enables
- fill-and-stroke, path-drawing, canvas-text, drawimage, canvas-transformation
## Related
- canvas-coordinate-system, save-restore-state
## Contrasts With
- SVG DOM manipulation (set attributes on elements instead)

# Common Errors
- **Error**: Expecting drawing method arguments to set colors or line widths
  **Correction**: Colors and line properties are set via context properties (fillStyle, strokeStyle), not as arguments

# Common Confusions
- **Confusion**: The canvas element itself has drawing methods
  **Clarification**: Drawing methods belong to the context, not the canvas element

# Source Reference
Chapter 17: Drawing on Canvas, Section "The canvas element", lines 120-163 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Explicitly explained
- Cross-reference status: verified
