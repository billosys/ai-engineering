---
concept: SVG
slug: svg
category: graphics
subcategory: web-graphics
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Drawing on Canvas"
chapter_number: 17
pdf_page: null
section: "SVG"
extraction_confidence: high
aliases:
  - Scalable Vector Graphics
prerequisites:
  - document-object-model
extends: []
related:
  - canvas-element
  - canvas-vs-svg
  - vector-graphics
contrasts_with:
  - canvas-element
answers_questions:
  - "What is SVG?"
  - "How do SVG and canvas differ?"
---

# Quick Definition
SVG (Scalable Vector Graphics) is an XML-based markup language for describing two-dimensional graphics, embedded in HTML documents, where shapes are DOM elements that can be manipulated with JavaScript.

# Core Definition
"Think of SVG as a document-markup dialect that focuses on shapes rather than text. You can embed an SVG document directly in an HTML document or include it with an `<img>` tag" (Ch. 17, "SVG"). SVG elements like `<circle>` and `<rect>` are DOM nodes that "scripts can interact with."

# Prerequisites
- **DOM**: SVG elements are part of the DOM tree

# Key Properties
1. XML-based format using tags like `<circle>`, `<rect>`, `<path>`
2. Uses `xmlns` attribute for the SVG namespace
3. Shapes are DOM elements (can be styled, animated, event-handled)
4. Resolution-independent (scales without pixelation)
5. Shape descriptions are preserved (not rasterized)

# Construction / Recognition
```html
<svg xmlns="http://www.w3.org/2000/svg">
  <circle r="50" cx="50" cy="50" fill="red"/>
  <rect x="120" y="5" width="90" height="90"
        stroke="blue" fill="none"/>
</svg>
```

# Context & Application
Best for graphics that need to scale, be interactive, or be modified after creation. Icons, charts, maps, and diagrams are common SVG use cases.

# Examples
Modifying SVG with JavaScript:
```javascript
let circle = document.querySelector("circle");
circle.setAttribute("fill", "cyan");
```

# Relationships
## Builds Upon
- document-object-model
## Enables
- Scalable graphics, interactive diagrams, data visualization
## Related
- canvas-element, vector-graphics
## Contrasts With
- canvas-element (pixel-based, immediate mode, no DOM for shapes)

# Common Errors
- **Error**: Forgetting the xmlns attribute on the SVG element
  **Correction**: Always include `xmlns="http://www.w3.org/2000/svg"`

# Common Confusions
- **Confusion**: SVG is just an image format
  **Clarification**: SVG elements are live DOM nodes that can be styled, animated, and scripted

# Source Reference
Chapter 17: Drawing on Canvas, Section "SVG", lines 64-107 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Clearly introduced with example
- Cross-reference status: verified
