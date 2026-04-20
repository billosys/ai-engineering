---
concept: Tool Abstraction
slug: tool-abstraction
category: application-architecture
subcategory: design-patterns
tier: advanced
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Pixel Art Editor"
chapter_number: 19
pdf_page: null
section: "Drawing tools"
extraction_confidence: high
aliases:
  - tool pattern
  - drawing tool
prerequisites:
  - function
  - dispatch-pattern
extends: []
related:
  - component-pattern
  - state-management
contrasts_with: []
answers_questions:
  - "How do you make a tool system where different tools have different behaviors?"
---

# Quick Definition
Tools are functions that receive a position, application state, and dispatch function, and return an optional move handler, allowing different drawing behaviors (draw, fill, rectangle, pick) to be selected at runtime.

# Core Definition
"The set of available tools is provided as an object that maps the names that appear in the drop-down field to functions that implement the tools. Such functions get a picture position, a current application state, and a `dispatch` function as arguments. They may return a move handler function" (Ch. 19, "The application").

# Prerequisites
- **Functions**: Tools are plain functions
- **Dispatch pattern**: Tools dispatch state changes

# Key Properties
1. Tool signature: `(pos, state, dispatch) => moveHandler?`
2. Move handler: `(newPos, state) => void`
3. Tools are stored in an object mapping names to functions
4. New tools can be added without changing the framework

# Construction / Recognition
```javascript
function draw(pos, state, dispatch) {
  function drawPixel({x, y}, state) {
    let drawn = {x, y, color: state.color};
    dispatch({picture: state.picture.draw([drawn])});
  }
  drawPixel(pos, state);
  return drawPixel;
}

const baseTools = {draw, fill, rectangle, pick};
```

# Context & Application
This pattern allows extensible behavior selection -- the same framework supports drawing, filling, rectangle selection, and color picking, each as a simple function with the same interface.

# Examples
The pick tool is the simplest:
```javascript
function pick(pos, state, dispatch) {
  dispatch({color: state.picture.pixel(pos.x, pos.y)});
}
```

# Relationships
## Builds Upon
- function, dispatch-pattern
## Enables
- Extensible tool systems, plugin architectures
## Related
- component-pattern, state-management
## Contrasts With
- Switch statements in a single handler

# Common Errors
- **Error**: Forgetting to return the move handler from tool functions
  **Correction**: Return the move handler for tools that support dragging; return nothing for click-only tools

# Common Confusions
- **Confusion**: Tools must be classes
  **Clarification**: Tools are plain functions -- the simplest possible interface

# Source Reference
Chapter 19: Project: A Pixel Art Editor, Section "Drawing tools", lines 537-660 of 19-project-a-pixel-art-editor.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Multiple tool implementations shown
- Cross-reference status: verified
