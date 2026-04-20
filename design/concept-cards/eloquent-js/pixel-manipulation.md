---
concept: Pixel Manipulation
slug: pixel-manipulation
category: graphics
subcategory: canvas-api
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Pixel Art Editor"
chapter_number: 19
pdf_page: null
section: "Saving and loading"
extraction_confidence: high
aliases:
  - getImageData
  - pixel access
prerequisites:
  - canvas-context
extends: []
related:
  - picture-data
  - drawimage
contrasts_with: []
answers_questions:
  - "How do I read individual pixel colors from a canvas?"
---

# Quick Definition
The `getImageData` method reads pixel data from a canvas as a flat array of RGBA values (4 numbers per pixel: red, green, blue, alpha, each 0-255), enabling direct pixel-level reading and manipulation.

# Core Definition
"The canvas context has a `getImageData` method that allows a script to read its pixels" (Ch. 19, "Saving and loading"). The returned data is a flat array where each pixel takes 4 entries (R, G, B, A). This is used to convert loaded images into the application's Picture format.

# Prerequisites
- **Canvas context**: getImageData is a context method

# Key Properties
1. `getImageData(x, y, width, height)` returns an object with `data` property
2. `data` is a flat array: [r, g, b, a, r, g, b, a, ...]
3. Each component is 0-255
4. Alpha 0 = transparent, 255 = opaque
5. Pixels are row-by-row, left-to-right, top-to-bottom

# Construction / Recognition
```javascript
let {data} = cx.getImageData(0, 0, width, height);
for (let i = 0; i < data.length; i += 4) {
  let [r, g, b] = data.slice(i, i + 3);
  pixels.push("#" + hex(r) + hex(g) + hex(b));
}
```

# Context & Application
Used for image analysis, color picking, filters, and converting between canvas and application data formats.

# Examples
Converting canvas pixels to color strings:
```javascript
function hex(n) {
  return n.toString(16).padStart(2, "0");
}
```

# Relationships
## Builds Upon
- canvas-context
## Enables
- Image loading, color analysis, pixel art editing
## Related
- picture-data, drawimage, bitmap-graphics
## Contrasts With
- Drawing operations (write-only vs. read access)

# Common Errors
- **Error**: Forgetting the alpha channel (every 4th value)
  **Correction**: Stride through data by 4, not 3

# Common Confusions
- **Confusion**: getImageData returns a 2D array
  **Clarification**: It returns a flat 1D array; calculate offset as (x + y * width) * 4

# Source Reference
Chapter 19: Project: A Pixel Art Editor, Section "Saving and loading", lines 770-819 of 19-project-a-pixel-art-editor.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Used in complete example
- Cross-reference status: verified
