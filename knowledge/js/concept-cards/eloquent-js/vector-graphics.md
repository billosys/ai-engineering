---
concept: Vector Graphics
slug: vector-graphics
category: graphics
subcategory: concepts
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Drawing on Canvas"
chapter_number: 17
pdf_page: null
section: "Images"
extraction_confidence: high
aliases:
  - scalable graphics
prerequisites: []
extends: []
related:
  - bitmap-graphics
  - svg
contrasts_with:
  - bitmap-graphics
answers_questions:
  - "What are vector graphics?"
---

# Quick Definition
Vector graphics describe images using mathematical shapes (lines, curves, polygons) rather than pixels, allowing them to scale to any size without quality loss.

# Core Definition
"The first is what we have been doing so far in this chapter -- specifying a picture by giving a logical description of shapes" (Ch. 17, "Images"). SVG is the web's vector graphics format. Vector descriptions are preserved and can be resized, unlike bitmap pixels.

# Prerequisites
- None (foundational concept)

# Key Properties
1. Described by shapes, not pixels
2. Resolution-independent (scale without pixelation)
3. SVG is the primary vector format for the web
4. Shapes can be individually modified after creation
5. File formats: SVG, PDF (partially)

# Construction / Recognition
SVG is the web standard for vector graphics:
```html
<svg xmlns="http://www.w3.org/2000/svg">
  <circle r="50" cx="50" cy="50" fill="red"/>
</svg>
```

# Context & Application
Logos, icons, diagrams, maps, and charts benefit from vector graphics. Content that needs to look sharp at any screen size or zoom level.

# Examples
"SVG can be used to produce crisp graphics that look good at any zoom level" (Ch. 17).

# Relationships
## Builds Upon
- (foundational concept)
## Enables
- Scalable UI, resolution-independent graphics
## Related
- svg, bitmap-graphics
## Contrasts With
- bitmap-graphics (pixel-based, resolution-dependent)

# Common Errors
- **Error**: Using vector graphics for photographic content
  **Correction**: Photos are inherently raster; vector is for geometric shapes

# Common Confusions
- **Confusion**: Canvas path drawing creates vector graphics
  **Clarification**: Canvas paths are immediately rasterized; only SVG retains the vector description

# Source Reference
Chapter 17: Drawing on Canvas, Section "Images", lines 511-516, and Section "Choosing a graphics interface", lines 1071-1123 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Defined in contrast with bitmap
- Cross-reference status: verified
