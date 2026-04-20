---
concept: Sprite
slug: sprite
category: graphics
subcategory: rendering
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
  - sprite sheet
  - game sprite
prerequisites:
  - drawimage
  - canvas-element
extends: []
related:
  - animation
  - bitmap-graphics
contrasts_with: []
answers_questions:
  - "What is a sprite in computer graphics?"
  - "How do you use sprite sheets in games?"
---

# Quick Definition
A sprite is a small image element used in games and graphics, often packed into a single sprite sheet image where `drawImage` extracts individual frames by specifying source rectangles.

# Core Definition
Haverbeke explains: "This can be used to pack multiple sprites (image elements) into a single image file and then draw only the part you need" (Ch. 17, "Images"). The nine-argument form of `drawImage` copies a rectangle from the source image to a rectangle on the canvas.

# Prerequisites
- **drawImage**: The canvas method used to render sprites
- **Canvas element**: The rendering surface

# Key Properties
1. Multiple sprites packed into a single image file (sprite sheet)
2. Individual sprites extracted via source rectangle coordinates
3. Each sprite has a fixed width and height (e.g., 24x30 pixels)
4. Animation cycles through different sprites in the sheet

# Construction / Recognition
```javascript
cx.drawImage(img,
             // source rectangle
             cycle * spriteW, 0, spriteW, spriteH,
             // destination rectangle
             0,               0, spriteW, spriteH);
```

# Context & Application
Sprites are fundamental to 2D game graphics. Using a single sprite sheet reduces HTTP requests and simplifies asset management. The technique applies to game characters, tiles, UI elements, and icons.

# Examples
The platform game uses two sprite images: `player.png` with 10 poses (8 walking + standing + jumping), and `sprites.png` with wall, lava, and coin tiles.

# Relationships
## Builds Upon
- drawimage, canvas-element
## Enables
- animation, game rendering
## Related
- bitmap-graphics, canvas-context
## Contrasts With
- vector-graphics (described by shapes, not pixels)

# Common Errors
- **Error**: Incorrect source rectangle coordinates producing garbled images
  **Correction**: Carefully calculate sprite positions: `spriteIndex * spriteWidth` for x offset

# Common Confusions
- **Confusion**: Each sprite needs its own image file
  **Clarification**: Sprite sheets combine many sprites into one file for efficiency

# Source Reference
Chapter 17: Drawing on Canvas, Section "Images", lines 555-606 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Clearly defined with code examples
- Cross-reference status: verified
