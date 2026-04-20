---
concept: drawImage
slug: drawimage
category: graphics
subcategory: canvas-api
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
  - canvas drawImage
prerequisites:
  - canvas-context
extends: []
related:
  - sprite
  - animation
  - bitmap-graphics
contrasts_with: []
answers_questions:
  - "How do I draw images on a canvas?"
  - "How do I use sprite sheets with canvas?"
---

# Quick Definition
`drawImage` is a canvas context method that draws an image (from an `<img>`, another canvas, or video) onto the canvas, with optional source and destination rectangle parameters for cropping and scaling.

# Core Definition
"The `drawImage` method allows us to draw pixel data onto a canvas" (Ch. 17, "Images"). It has three forms: basic (3 args: image, x, y), scaled (5 args: adds width, height), and cropped (9 args: source rect + destination rect). The 9-argument form is key for sprite sheets.

# Prerequisites
- **Canvas context**: drawImage is a context method

# Key Properties
1. 3 arguments: `drawImage(img, x, y)` -- draw at position
2. 5 arguments: `drawImage(img, x, y, w, h)` -- draw scaled
3. 9 arguments: `drawImage(img, sx, sy, sw, sh, dx, dy, dw, dh)` -- draw cropped region
4. Image must be loaded before drawing (use "load" event)
5. Source can be `<img>`, `<canvas>`, or `<video>` element

# Construction / Recognition
```javascript
let img = document.createElement("img");
img.src = "img/hat.png";
img.addEventListener("load", () => {
  for (let x = 10; x < 200; x += 30) {
    cx.drawImage(img, x, 10);
  }
});
```

# Context & Application
Essential for games (sprites, backgrounds), image editors, photo manipulation, and any canvas application using pre-existing images.

# Examples
9-argument form for sprite animation:
```javascript
cx.drawImage(img,
             cycle * spriteW, 0, spriteW, spriteH, // source rect
             0,               0, spriteW, spriteH); // dest rect
```

# Relationships
## Builds Upon
- canvas-context
## Enables
- sprite, animation, image compositing
## Related
- bitmap-graphics, canvas-element
## Contrasts With
- HTML `<img>` tag (declarative, part of document flow)

# Common Errors
- **Error**: Calling drawImage before the image has loaded
  **Correction**: Wait for the "load" event or accept that early frames may be blank

# Common Confusions
- **Confusion**: drawImage can only draw `<img>` elements
  **Clarification**: It works with any image source including other canvases and video elements

# Source Reference
Chapter 17: Drawing on Canvas, Section "Images", lines 508-606 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: All three forms explained with examples
- Cross-reference status: verified
