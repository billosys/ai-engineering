---
concept: Canvas Text
slug: canvas-text
category: graphics
subcategory: canvas-api
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Drawing on Canvas"
chapter_number: 17
pdf_page: null
section: "Text"
extraction_confidence: high
aliases:
  - fillText
  - strokeText
prerequisites:
  - canvas-context
  - fill-and-stroke
extends: []
related:
  - canvas-element
contrasts_with: []
answers_questions:
  - "How do I draw text on a canvas?"
---

# Quick Definition
Canvas text is drawn using `fillText` or `strokeText` methods, with font, size, alignment, and baseline controlled by context properties like `font`, `textAlign`, and `textBaseline`.

# Core Definition
"A 2D canvas drawing context provides the methods `fillText` and `strokeText`. The latter can be useful for outlining letters, but usually `fillText` is what you need. It will fill the outline of the given text with the current `fillStyle`" (Ch. 17, "Text").

# Prerequisites
- **Canvas context**: Text methods are on the 2D context
- **Fill and stroke**: Text uses fillStyle for color

# Key Properties
1. `fillText(text, x, y)` draws filled text
2. `strokeText(text, x, y)` draws outlined text
3. `font` property sets size and family (e.g., "28px Georgia")
4. `textAlign` -- "start", "end", or "center"
5. `textBaseline` -- "top", "middle", "bottom", "alphabetic"

# Construction / Recognition
```javascript
cx.font = "28px Georgia";
cx.fillStyle = "fuchsia";
cx.fillText("I can draw text, too!", 10, 50);
```

# Context & Application
Used for labels, scores, titles, and annotations in canvas-based graphics and games.

# Examples
From the pie chart exercise, labels would be added with fillText positioned near each slice.

# Relationships
## Builds Upon
- canvas-context, fill-and-stroke
## Enables
- Labels, annotations, game UI text
## Related
- canvas-element
## Contrasts With
- HTML/CSS text (automatically wraps, selectable, accessible)

# Common Errors
- **Error**: Expecting canvas text to wrap automatically
  **Correction**: Canvas text does not wrap; you must handle line breaks manually

# Common Confusions
- **Confusion**: The x,y position is the top-left of the text
  **Clarification**: By default, position is at the start of the alphabetic baseline

# Source Reference
Chapter 17: Drawing on Canvas, Section "Text", lines 468-500 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Clear explanation with properties listed
- Cross-reference status: verified
