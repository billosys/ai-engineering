---
concept: Picture Data
slug: picture-data
category: application-architecture
subcategory: data-model
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Pixel Art Editor"
chapter_number: 19
pdf_page: null
section: "The state"
extraction_confidence: high
aliases:
  - pixel data
  - Picture class
prerequisites:
  - class-declaration
  - array
extends: []
related:
  - persistent-state
  - pixel-manipulation
contrasts_with: []
answers_questions:
  - "How do you represent pixel image data in JavaScript?"
---

# Quick Definition
The Picture class stores image data as a flat array of color strings indexed by `x + y * width`, with an immutable `draw` method that returns a new Picture with updated pixels.

# Core Definition
"The pixels are stored in a single array, row by row, from top to bottom" (Ch. 19, "The state"). The `pixel(x, y)` method retrieves colors, and `draw(pixels)` creates a new Picture with specified pixels changed, treating images as immutable values.

# Prerequisites
- **Classes**: Picture is a class
- **Arrays**: Pixels stored in a flat array

# Key Properties
1. `width`, `height` -- image dimensions
2. `pixels` -- flat array of CSS color strings
3. `pixel(x, y)` -- retrieves color at position
4. `draw(pixels)` -- returns new Picture with changes applied
5. `empty(width, height, color)` -- static factory for blank images

# Construction / Recognition
```javascript
class Picture {
  constructor(width, height, pixels) {
    this.width = width; this.height = height; this.pixels = pixels;
  }
  pixel(x, y) { return this.pixels[x + y * this.width]; }
  draw(pixels) {
    let copy = this.pixels.slice();
    for (let {x, y, color} of pixels) {
      copy[x + y * this.width] = color;
    }
    return new Picture(this.width, this.height, copy);
  }
}
```

# Context & Application
This flat-array representation is standard for pixel data. The immutable design enables undo history and prevents bugs from shared references.

# Examples
Creating an empty picture:
```javascript
Picture.empty(60, 30, "#f0f0f0")
```

# Relationships
## Builds Upon
- class-declaration, array
## Enables
- pixel-manipulation, undo-functionality, canvas rendering
## Related
- persistent-state, bitmap-graphics
## Contrasts With
- 2D array representation (array of arrays)

# Common Errors
- **Error**: Modifying the pixels array directly
  **Correction**: Use the draw method to create a new Picture

# Common Confusions
- **Confusion**: Each pixel is stored as RGB numbers
  **Clarification**: Pixels are CSS color strings like "#ff00ff"

# Source Reference
Chapter 19: Project: A Pixel Art Editor, Section "The state", lines 145-232 of 19-project-a-pixel-art-editor.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Complete class definition provided
- Cross-reference status: verified
