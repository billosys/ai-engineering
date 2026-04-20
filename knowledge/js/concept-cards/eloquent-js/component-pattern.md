---
concept: Component Pattern
slug: component-pattern
category: application-architecture
subcategory: ui-patterns
tier: advanced
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Pixel Art Editor"
chapter_number: 19
pdf_page: null
section: "Components"
extraction_confidence: high
aliases:
  - UI component
  - component architecture
prerequisites:
  - class-declaration
  - document-object-model
extends: []
related:
  - state-management
  - dispatch-pattern
contrasts_with: []
answers_questions:
  - "What is a UI component?"
  - "What must I know before building a web application?"
---

# Quick Definition
A component is a self-contained object responsible for a piece of the DOM, with a `dom` property for its element and a `syncState` method to update its appearance when application state changes.

# Core Definition
"We will structure the editor interface as a number of components, objects that are responsible for a piece of the DOM and that may contain other components inside them" (Ch. 19, "Components"). Each component's constructor builds its DOM, and `syncState(state)` synchronizes its view with updated state.

# Prerequisites
- **Classes**: Components are typically classes
- **DOM**: Components create and manage DOM elements

# Key Properties
1. Constructor creates DOM elements (stored in `dom` property)
2. `syncState(state)` updates the component to reflect new state
3. Components may contain child components
4. State flows down from parent to children

# Construction / Recognition
```javascript
class ToolSelect {
  constructor(state, {tools, dispatch}) {
    this.select = elt("select", {
      onchange: () => dispatch({tool: this.select.value})
    }, ...Object.keys(tools).map(name => elt("option", {
      selected: name == state.tool
    }, name)));
    this.dom = elt("label", null, "Tool: ", this.select);
  }
  syncState(state) { this.select.value = state.tool; }
}
```

# Context & Application
Components are the fundamental building block of modern UI frameworks (React, Vue, Angular). This chapter demonstrates the core concept without a framework, showing why libraries make components easier to manage.

# Examples
The PixelEditor composes multiple components:
```javascript
class PixelEditor {
  constructor(state, config) {
    this.canvas = new PictureCanvas(state.picture, pos => { /*...*/ });
    this.controls = controls.map(Control => new Control(state, config));
    this.dom = elt("div", {}, this.canvas.dom, elt("br"),
                   ...this.controls.reduce((a, c) => a.concat(" ", c.dom), []));
  }
  syncState(state) {
    this.canvas.syncState(state.picture);
    for (let ctrl of this.controls) ctrl.syncState(state);
  }
}
```

# Relationships
## Builds Upon
- class-declaration, document-object-model
## Enables
- Modular UI construction, reusable interface pieces
## Related
- state-management, dispatch-pattern
## Contrasts With
- Monolithic DOM manipulation (all UI in one place)

# Common Errors
- **Error**: Components directly modifying shared state
  **Correction**: Components should dispatch actions; state updates flow back through syncState

# Common Confusions
- **Confusion**: Components in this chapter work like React components
  **Clarification**: These are manual components without virtual DOM, reconciliation, or JSX

# Source Reference
Chapter 19: Project: A Pixel Art Editor, Section "Components", lines 50-143 of 19-project-a-pixel-art-editor.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Thorough explanation with interface definition
- Cross-reference status: verified
