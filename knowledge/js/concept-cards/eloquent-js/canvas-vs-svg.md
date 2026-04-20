---
concept: Canvas vs SVG
slug: canvas-vs-svg
category: graphics
subcategory: web-graphics
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Drawing on Canvas"
chapter_number: 17
pdf_page: null
section: "Choosing a graphics interface"
extraction_confidence: high
aliases:
  - graphics tradeoffs
prerequisites:
  - canvas-element
  - svg
extends: []
related:
  - bitmap-graphics
  - vector-graphics
contrasts_with: []
answers_questions:
  - "When should I use canvas vs SVG?"
  - "What are the tradeoffs between canvas and SVG?"
---

# Quick Definition
Canvas and SVG are two browser graphics technologies with different strengths: canvas excels at pixel-level operations and many small elements, while SVG excels at scalable, interactive shapes that need to be moved or resized.

# Core Definition
"When you need to generate graphics in the browser, you can choose between plain HTML, SVG, and canvas. There is no single best approach that works in all situations" (Ch. 17, "Choosing a graphics interface"). Key tradeoffs: SVG retains shape descriptions and supports per-element mouse events; canvas has lower per-shape cost and enables pixel-level effects.

# Prerequisites
- **Canvas element**: Pixel-based drawing
- **SVG**: Shape-based, DOM-integrated drawing

# Key Properties
1. SVG: crisp at any zoom, shapes are DOM elements, supports per-element events
2. Canvas: lower per-shape cost, pixel manipulation, no retained mode
3. SVG: better for partial updates to large scenes
4. Canvas: must clear and redraw to update
5. Both: can be combined with HTML for text

# Construction / Recognition
Choose SVG when: scalability matters, shapes need interaction, partial scene updates.
Choose canvas when: many tiny elements, pixel effects, games with full-screen redraws.

# Context & Application
"SVG can be used to produce crisp graphics that look good at any zoom level." "Canvas's pixel-oriented approach can be an advantage when drawing a huge number of tiny elements."

# Examples
The game could use either: "The display we built for our game in this chapter could have been implemented using any of these three graphics technologies."

# Relationships
## Builds Upon
- canvas-element, svg
## Enables
- Informed technology choice for graphics projects
## Related
- bitmap-graphics, vector-graphics
## Contrasts With
- N/A (this card IS about the contrast)

# Common Errors
- **Error**: Always choosing canvas because it seems more "powerful"
  **Correction**: SVG is often simpler and more appropriate for non-game graphics

# Common Confusions
- **Confusion**: You must choose one technology for the whole application
  **Clarification**: "You may want to combine several of these techniques" -- e.g., SVG graph with HTML labels

# Source Reference
Chapter 17: Drawing on Canvas, Section "Choosing a graphics interface", lines 1071-1123 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Dedicated section comparing approaches
- Cross-reference status: verified
