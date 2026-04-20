---
concept: Bezier Curve
slug: bezier-curve
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
  - quadratic curve
  - cubic bezier
  - bezierCurveTo
  - quadraticCurveTo
prerequisites:
  - path-drawing
extends: []
related:
  - arc
  - canvas-context
contrasts_with: []
answers_questions:
  - "How do I draw curves on a canvas?"
---

# Quick Definition
Bezier curves are smooth curves defined by control points that "attract" the line, available as quadratic (one control point) and cubic (two control points) variants via `quadraticCurveTo` and `bezierCurveTo`.

# Core Definition
"The `quadraticCurveTo` method draws a curve to a given point. To determine the curvature of the line, the method is given a control point as well as a destination point. Imagine this control point as attracting the line, giving it its curve" (Ch. 17, "Curves"). `bezierCurveTo` uses two control points, one for each endpoint, giving more control over the curve shape.

# Prerequisites
- **Path drawing**: Curves are part of the path API

# Key Properties
1. `quadraticCurveTo(cpX, cpY, x, y)` -- one control point
2. `bezierCurveTo(cp1X, cp1Y, cp2X, cp2Y, x, y)` -- two control points
3. Control points determine the direction/curvature at endpoints
4. The curve does not pass through control points

# Construction / Recognition
```javascript
// Quadratic curve
cx.beginPath();
cx.moveTo(10, 90);
cx.quadraticCurveTo(60, 10, 90, 90);
cx.stroke();

// Bezier curve
cx.beginPath();
cx.moveTo(10, 90);
cx.bezierCurveTo(10, 10, 90, 10, 50, 90);
cx.stroke();
```

# Context & Application
Used for smooth curves in data visualization, UI elements, animation paths, and artistic drawing. Bezier curves are the mathematical foundation of fonts, vector graphics, and design tools.

# Examples
"The two control points specify the direction at both ends of the curve. The farther they are away from their corresponding point, the more the curve will 'bulge' in that direction."

# Relationships
## Builds Upon
- path-drawing, canvas-context
## Enables
- Complex shapes, smooth curves, rounded corners
## Related
- arc, fill-and-stroke
## Contrasts With
- arc (circular curves vs. polynomial curves)

# Common Errors
- **Error**: Expecting the curve to pass through the control points
  **Correction**: Control points influence direction, not position; the curve is "attracted" toward them

# Common Confusions
- **Confusion**: Quadratic and cubic bezier curves are the same
  **Clarification**: Quadratic has 1 control point (simpler); cubic has 2 (more flexibility)

# Source Reference
Chapter 17: Drawing on Canvas, Section "Curves", lines 288-365 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Both curve types explained with examples
- Cross-reference status: verified
