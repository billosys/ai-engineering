---
concept: Fill and Stroke
slug: fill-and-stroke
category: graphics
subcategory: canvas-api
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Drawing on Canvas"
chapter_number: 17
pdf_page: null
section: "Lines and surfaces"
extraction_confidence: high
aliases:
  - fillStyle
  - strokeStyle
  - fillRect
  - strokeRect
prerequisites:
  - canvas-context
extends: []
related:
  - path-drawing
  - canvas-text
contrasts_with: []
answers_questions:
  - "How do I draw filled or outlined shapes on a canvas?"
  - "How do I set colors for canvas drawing?"
---

# Quick Definition
Fill colors the interior area of a shape, while stroke draws its outline. Both are controlled by context properties (`fillStyle`, `strokeStyle`, `lineWidth`) rather than method arguments.

# Core Definition
"In the canvas interface, a shape can be filled, meaning its area is given a certain color or pattern, or it can be stroked, which means a line is drawn along its edge" (Ch. 17, "Lines and surfaces"). The `fillStyle` and `strokeStyle` properties accept CSS color strings. `fillRect` and `strokeRect` are convenience methods for rectangles.

# Prerequisites
- **Canvas context**: Fill and stroke are context operations

# Key Properties
1. `fillStyle` -- color/pattern for filled shapes (CSS color notation)
2. `strokeStyle` -- color for outlines
3. `lineWidth` -- thickness of stroked lines
4. `fillRect(x, y, w, h)` and `strokeRect(x, y, w, h)` for rectangles
5. `fill()` and `stroke()` for paths

# Construction / Recognition
```javascript
cx.fillStyle = "red";
cx.fillRect(10, 10, 100, 50);
cx.strokeStyle = "blue";
cx.lineWidth = 5;
cx.strokeRect(135, 5, 50, 50);
```

# Context & Application
Every visible canvas drawing uses either fill, stroke, or both. This is the fundamental rendering mechanism for the canvas API.

# Examples
From the pie chart example:
```javascript
cx.fillStyle = result.color;
cx.fill();
```

# Relationships
## Builds Upon
- canvas-context
## Enables
- All visible canvas drawing
## Related
- path-drawing, canvas-text, drawimage
## Contrasts With
- SVG fill/stroke attributes (set per element, not globally)

# Common Errors
- **Error**: Setting fillStyle after calling fillRect
  **Correction**: Set style properties BEFORE drawing operations

# Common Confusions
- **Confusion**: Each drawing call specifies its own color
  **Clarification**: Colors are state on the context; they persist until changed

# Source Reference
Chapter 17: Drawing on Canvas, Section "Lines and surfaces", lines 165-216 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Clearly explained with examples
- Cross-reference status: verified
