---
concept: Canvas Element
slug: canvas-element
category: graphics
subcategory: html-elements
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
  - canvas tag
  - HTML canvas
prerequisites:
  - document-object-model
extends: []
related:
  - canvas-context
  - svg
  - canvas-vs-svg
contrasts_with:
  - svg
answers_questions:
  - "What is the HTML canvas element?"
  - "How do I draw graphics in the browser?"
---

# Quick Definition
The `<canvas>` element is an HTML element that provides a pixel-based drawing surface, accessed through a context object whose methods draw shapes, text, and images onto the canvas.

# Core Definition
Haverbeke explains: "A canvas is a single DOM element that encapsulates a picture. It provides a programming interface for drawing shapes onto the space taken up by the node. The main difference between a canvas and an SVG picture is that in SVG the original description of the shapes is preserved so that they can be moved or resized at any time. A canvas, on the other hand, converts the shapes to pixels (colored dots on a raster) as soon as they are drawn and does not remember what these pixels represent" (Ch. 17, "The canvas element").

# Prerequisites
- **DOM**: The canvas is a DOM element

# Key Properties
1. `width` and `height` attributes set size in pixels (default 300x150)
2. Drawing is done through a context object, not directly on the element
3. Content is pixel-based (rasterized immediately)
4. Supports "2d", "webgl", and "webgpu" context types

# Construction / Recognition
```html
<canvas width="120" height="60"></canvas>
<script>
  let canvas = document.querySelector("canvas");
  let context = canvas.getContext("2d");
  context.fillStyle = "red";
  context.fillRect(10, 10, 100, 50);
</script>
```

# Context & Application
Used for games, data visualization, image processing, and any application needing direct pixel manipulation. Preferred over DOM manipulation for complex or performance-sensitive graphics.

# Examples
A new canvas starts transparent and empty: "A new canvas is empty, meaning it is entirely transparent and thus shows up as empty space in the document."

# Relationships
## Builds Upon
- document-object-model
## Enables
- canvas-context, fill-and-stroke, path-drawing, drawimage, canvas-transformation
## Related
- svg, bitmap-graphics
## Contrasts With
- SVG (vector-based, retains shape information, DOM-based)

# Common Errors
- **Error**: Drawing on the canvas element directly instead of using the context
  **Correction**: Always call `getContext("2d")` first and draw via the returned context object

# Common Confusions
- **Confusion**: Canvas and SVG are interchangeable
  **Clarification**: Canvas is pixel-based (immediate mode); SVG is shape-based (retained mode). Each has different strengths.

# Source Reference
Chapter 17: Drawing on Canvas, Section "The canvas element", lines 109-163 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Thoroughly explained with comparison to SVG
- Cross-reference status: verified
