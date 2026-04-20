---
concept: Canvas 2D Context
slug: canvas-2d-context
category: browser-apis
subcategory: canvas
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 501
section: "15.8 Graphics in a <canvas>"
extraction_confidence: high
aliases:
  - CanvasRenderingContext2D
  - "<canvas> API"
  - 2D canvas
prerequisites:
  - dom-tree
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What is the DOM (Document Object Model)?"
---

# Quick Definition

The Canvas 2D API allows JavaScript to draw graphics programmatically on a `<canvas>` element by calling methods on a CanvasRenderingContext2D object obtained via `canvas.getContext("2d")`.

# Core Definition

The `<canvas>` element creates a drawing surface. Most of the Canvas drawing API is defined on the CanvasRenderingContext2D object obtained via `getContext("2d")`. Drawing is done through method calls: `beginPath()` starts a path, `moveTo()`/`lineTo()` define segments, `arc()` adds curves, and `fill()`/`stroke()` render the path. Graphics state properties like `fillStyle`, `strokeStyle`, and `lineWidth` control appearance (Flanagan, Ch. 15, pp. 501-503).

# Prerequisites

- **dom-tree** — The `<canvas>` element exists in the DOM.

# Key Properties

1. Obtain the context with `canvas.getContext("2d")`.
2. Drawing model uses paths: `beginPath()`, `moveTo()`, `lineTo()`, `arc()`, `closePath()`.
3. `fill()` and `stroke()` render the current path.
4. Graphics state includes `fillStyle`, `strokeStyle`, `lineWidth`, gradients, and transforms.
5. Canvas dimensions determine pixel resolution; CSS dimensions determine display size.

# Construction / Recognition

```javascript
let canvas = document.querySelector("#my_canvas");
let c = canvas.getContext("2d");
c.fillStyle = "#f00";
c.fillRect(0, 0, 10, 10);
```

# Context & Application

Used for charts, data visualization, image manipulation, simple games, and any dynamic graphics that need per-pixel control. SVG is preferred for resolution-independent graphics.

# Examples

From the source (p. 502): Drawing a red square and a blue circle:
```javascript
context.fillStyle = "#f00";
context.fillRect(0, 0, 10, 10);
context.beginPath();
context.arc(5, 5, 5, 0, 2*Math.PI, true);
context.fillStyle = "#00f";
context.fill();
```

# Relationships

## Builds Upon
- **dom-tree** — Canvas is a DOM element

## Enables
- Data visualization, charting, game graphics

## Related
- (SVG as an alternative)

## Contrasts With
- (None)

# Common Errors

- **Error**: Forgetting to call `beginPath()` before starting a new shape.
  **Correction**: Without `beginPath()`, new subpaths are added to the existing path, causing the old shapes to be redrawn.

# Common Confusions

- **Confusion**: Canvas and SVG are interchangeable.
  **Clarification**: Canvas is pixel-based and drawn via method calls; SVG is element-based and described as a tree of XML tags. Canvas is better for many small shapes; SVG is better for scalable, interactive graphics.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.8, pages 501-524.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Extensive section with multiple examples
- Uncertainties: None
- Cross-reference status: Verified
