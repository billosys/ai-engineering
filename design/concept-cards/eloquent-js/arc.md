---
concept: Arc
slug: arc
category: graphics
subcategory: canvas-api
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Drawing on Canvas"
chapter_number: 17
pdf_page: null
section: "Curves"
extraction_confidence: high
aliases:
  - circle arc
  - canvas arc
prerequisites:
  - path-drawing
extends: []
related:
  - bezier-curve
  - canvas-context
contrasts_with: []
answers_questions:
  - "How do I draw circles and arcs on a canvas?"
---

# Quick Definition
The `arc` method draws a circular arc or full circle as part of a path, taking a center point, radius, start angle, and end angle measured in radians.

# Core Definition
"The `arc` method is a way to draw a line that curves along the edge of a circle. It takes a pair of coordinates for the arc's center, a radius, and then a start angle and end angle" (Ch. 17, "Curves"). Angles are in radians (full circle = 2pi). A start of 0 and end greater than 2pi draws a complete circle.

# Prerequisites
- **Path drawing**: Arcs are added to the current path

# Key Properties
1. `arc(cx, cy, radius, startAngle, endAngle)` -- basic usage
2. Angles measured in radians, not degrees (full circle = 2 * Math.PI)
3. Angle 0 is at the rightmost point; goes clockwise
4. Connected to previous path segment (use moveTo to avoid connecting lines)

# Construction / Recognition
```javascript
cx.beginPath();
cx.arc(50, 50, 40, 0, 7); // full circle
cx.arc(150, 50, 40, 0, 0.5 * Math.PI); // quarter circle
cx.stroke();
```

# Context & Application
Used for circles, pie charts, rounded corners, clock faces, gauges, and any circular geometry.

# Examples
Pie chart slices:
```javascript
cx.beginPath();
cx.arc(100, 100, 100, currentAngle, currentAngle + sliceAngle);
cx.lineTo(100, 100);
cx.fillStyle = result.color;
cx.fill();
```

# Relationships
## Builds Upon
- path-drawing, canvas-context
## Enables
- Circles, pie charts, rounded shapes
## Related
- bezier-curve, fill-and-stroke
## Contrasts With
- bezier-curve (polynomial curve vs. circular arc)

# Common Errors
- **Error**: Using degrees instead of radians
  **Correction**: Convert with `degrees * Math.PI / 180` or use radians directly

# Common Confusions
- **Confusion**: Each arc call creates an independent shape
  **Clarification**: Arc segments are connected to the previous path position; use moveTo or beginPath to separate them

# Source Reference
Chapter 17: Drawing on Canvas, Section "Curves", lines 367-405 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Clear explanation with code
- Cross-reference status: verified
