---
concept: Bitmap Graphics
slug: bitmap-graphics
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
  - raster graphics
  - pixel graphics
prerequisites:
  - canvas-element
extends: []
related:
  - vector-graphics
  - drawimage
  - sprite
contrasts_with:
  - vector-graphics
answers_questions:
  - "What are bitmap graphics?"
  - "What is the difference between bitmap and vector graphics?"
---

# Quick Definition
Bitmap (raster) graphics represent images as a grid of colored pixels, as opposed to vector graphics which describe shapes mathematically.

# Core Definition
"In computer graphics, a distinction is often made between vector graphics and bitmap graphics. [...] Bitmap graphics [...] don't specify actual shapes but rather work with pixel data (rasters of colored dots)" (Ch. 17, "Images"). Canvas is inherently a bitmap system -- once shapes are drawn, they become pixels.

# Prerequisites
- **Canvas element**: Canvas produces bitmap graphics

# Key Properties
1. Images stored as grids of pixels (colored dots)
2. Resolution-dependent (pixelate when zoomed)
3. Efficient for complex scenes with many colors
4. Canvas drawing produces bitmap output
5. File formats: PNG, JPEG, GIF

# Construction / Recognition
Bitmap graphics are produced whenever you draw on a canvas. The `getImageData` method reveals the underlying pixel array.

# Context & Application
Photos, game sprites, screenshots, and canvas output are all bitmap graphics. They are appropriate when exact pixel control matters.

# Examples
The pixel art editor in Ch. 19 works directly with pixel data:
```javascript
let {data} = cx.getImageData(0, 0, width, height);
// data contains [r, g, b, a, r, g, b, a, ...] for each pixel
```

# Relationships
## Builds Upon
- canvas-element
## Enables
- Image processing, pixel art, photo manipulation
## Related
- drawimage, sprite, canvas-element
## Contrasts With
- vector-graphics (mathematical shapes, resolution-independent)

# Common Errors
- **Error**: Scaling bitmap images up without considering quality loss
  **Correction**: Use vector graphics when scalability is needed

# Common Confusions
- **Confusion**: Canvas shapes are vectors because you describe them as shapes
  **Clarification**: Canvas immediately rasterizes shapes to pixels; the shape description is not preserved

# Source Reference
Chapter 17: Drawing on Canvas, Section "Images", lines 511-516 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Clearly defined in contrast with vector graphics
- Cross-reference status: verified
