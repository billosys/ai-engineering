---
concept: Path Drawing
slug: path-drawing
category: graphics
subcategory: canvas-api
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Drawing on Canvas"
chapter_number: 17
pdf_page: null
section: "Paths"
extraction_confidence: high
aliases:
  - canvas path
  - beginPath
  - lineTo
  - moveTo
prerequisites:
  - canvas-context
  - fill-and-stroke
extends: []
related:
  - bezier-curve
  - arc
contrasts_with: []
answers_questions:
  - "How do I draw custom shapes on a canvas?"
  - "How does path-based drawing work?"
---

# Quick Definition
Path drawing creates custom shapes on a canvas by calling methods like `beginPath`, `moveTo`, `lineTo`, and `closePath` to define a sequence of lines and curves, then rendering with `fill()` or `stroke()`.

# Core Definition
"A path is a sequence of lines. The 2D canvas interface takes a peculiar approach to describing such a path. It is done entirely through side effects. Paths are not values that can be stored and passed around. Instead, if you want to do something with a path, you make a sequence of method calls to describe its shape" (Ch. 17, "Paths").

# Prerequisites
- **Canvas context**: Paths are described on the context
- **Fill and stroke**: Paths are rendered via fill() or stroke()

# Key Properties
1. `beginPath()` starts a new path
2. `moveTo(x, y)` moves the "pen" without drawing
3. `lineTo(x, y)` draws a line to the given point
4. `closePath()` draws a line back to the path's start
5. `fill()` fills the enclosed shape; `stroke()` draws the outline
6. For fill, paths are auto-closed (implicit line to start)

# Construction / Recognition
```javascript
cx.beginPath();
cx.moveTo(50, 10);
cx.lineTo(10, 70);
cx.lineTo(90, 70);
cx.fill(); // draws a filled triangle
```

# Context & Application
Used for any shape that isn't a simple rectangle. Triangles, polygons, pie charts, and complex outlines all use the path API.

# Examples
Drawing horizontal lines:
```javascript
cx.beginPath();
for (let y = 10; y < 100; y += 10) {
  cx.moveTo(10, y);
  cx.lineTo(90, y);
}
cx.stroke();
```

# Relationships
## Builds Upon
- canvas-context, fill-and-stroke
## Enables
- Custom shapes, bezier-curve, arc, pie charts
## Related
- canvas-coordinate-system
## Contrasts With
- SVG path elements (declarative, stored in DOM)

# Common Errors
- **Error**: Forgetting to call `beginPath()` before a new shape
  **Correction**: Always start with beginPath() or the new path connects to the previous one

# Common Confusions
- **Confusion**: Paths are stored as objects you can reuse
  **Clarification**: Paths are side-effect-based; they exist only as current state on the context

# Source Reference
Chapter 17: Drawing on Canvas, Section "Paths", lines 218-286 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Thorough explanation with multiple examples
- Cross-reference status: verified
