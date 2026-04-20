---
concept: DOM-Canvas Integration
slug: dom-canvas-integration
category: application-architecture
subcategory: ui-patterns
tier: advanced
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Pixel Art Editor"
chapter_number: 19
pdf_page: null
section: "The canvas"
extraction_confidence: high
aliases:
  - canvas in application
  - mixed rendering
prerequisites:
  - canvas-element
  - document-object-model
  - form-element
extends: []
related:
  - component-pattern
  - canvas-vs-svg
contrasts_with: []
answers_questions:
  - "How do you combine canvas drawing with HTML form controls?"
---

# Quick Definition
DOM-canvas integration combines HTML form controls (select, input, button) with a canvas drawing surface in a single application, using the component pattern to coordinate updates between DOM controls and canvas rendering.

# Core Definition
The pixel art editor uses "a big `<canvas>` element on top, with a number of form fields below it" (Ch. 19, "Components"). The PictureCanvas component wraps the canvas element, while ToolSelect, ColorSelect, SaveButton, and UndoButton are DOM-based controls. All synchronize through the shared state management system.

# Prerequisites
- **Canvas element**: For the drawing surface
- **DOM**: For form controls
- **Form elements**: Select, input, button controls

# Key Properties
1. Canvas handles pixel-level rendering and pointer events
2. DOM elements handle form controls (tools, colors, buttons)
3. Both are managed as components with syncState methods
4. State flows uniformly to both canvas and DOM components
5. The `elt` helper creates DOM elements programmatically

# Construction / Recognition
```javascript
class PixelEditor {
  constructor(state, config) {
    this.canvas = new PictureCanvas(state.picture, pos => { /* ... */ });
    this.controls = controls.map(Control => new Control(state, config));
    this.dom = elt("div", {}, this.canvas.dom, elt("br"),
                   ...this.controls.reduce((a, c) => a.concat(" ", c.dom), []));
  }
}
```

# Context & Application
Most real-world canvas applications need HTML controls for settings, tools, and user input. The pixel art editor demonstrates how to structure an application using both technologies.

# Examples
"In some cases, you may want to combine several of these techniques. For example, you might draw a graph with SVG or canvas but show textual information by positioning an HTML element on top of the picture" (Ch. 17).

# Relationships
## Builds Upon
- canvas-element, document-object-model, form-element
## Enables
- Rich interactive applications, drawing tools, games with UI
## Related
- component-pattern, canvas-vs-svg
## Contrasts With
- Pure canvas apps (harder to provide accessible controls)

# Common Errors
- **Error**: Trying to put form controls inside a canvas
  **Correction**: Canvas is a single drawing surface; DOM controls go alongside it

# Common Confusions
- **Confusion**: Canvas replaces all HTML
  **Clarification**: Canvas is for graphics; HTML/DOM is better for text, forms, and interactive controls

# Source Reference
Chapter 19: Project: A Pixel Art Editor, Section "Components" and "The canvas", lines 50-310; Chapter 17, Section "Choosing a graphics interface", lines 1112-1115 of 17-drawing-on-canvas.md.

# Verification Notes
- Definition source: synthesized from implementation
- Confidence rationale: Core architecture of the pixel editor
- Cross-reference status: verified
