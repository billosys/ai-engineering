---
concept: Dispatch Pattern
slug: dispatch-pattern
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
  - action dispatch
  - dispatch function
prerequisites:
  - state-management
  - function
extends: []
related:
  - application-state-update
  - component-pattern
contrasts_with: []
answers_questions:
  - "How do UI components communicate state changes?"
---

# Quick Definition
The dispatch pattern passes a function to UI components that accepts action objects describing intended state changes, which are processed by a central update function to produce new state.

# Core Definition
"Updates to the state are represented as objects, which we'll call actions. Components may create such actions and dispatch them -- give them to a central state management function. That function computes the next state, after which the interface components update themselves to this new state" (Ch. 19, "Components").

# Prerequisites
- **State management**: Dispatch is part of the state management cycle
- **Functions**: dispatch is a function passed to components

# Key Properties
1. Actions are plain objects describing what changed (e.g., `{color: "#ff0000"}`)
2. Components receive a dispatch function at construction
3. The dispatch function calls the update function and triggers re-sync
4. "The only way DOM events can change the state is by dispatching actions to the state"

# Construction / Recognition
```javascript
function updateState(state, action) {
  return {...state, ...action};
}

// dispatch function
dispatch(action) {
  state = historyUpdateState(state, action);
  app.syncState(state);
}

// component using dispatch
onchange: () => dispatch({tool: this.select.value})
```

# Context & Application
This is the pattern used by Redux (dispatch + reducer), Flux, and similar architectures. It creates a clear, traceable flow from user interaction to state change to UI update.

# Examples
Color change dispatch:
```javascript
class ColorSelect {
  constructor(state, {dispatch}) {
    this.input = elt("input", {
      type: "color",
      value: state.color,
      onchange: () => dispatch({color: this.input.value})
    });
  }
}
```

# Relationships
## Builds Upon
- state-management, function
## Enables
- Traceable state changes, undo-functionality, middleware
## Related
- application-state-update, component-pattern
## Contrasts With
- Direct mutation (components modifying state objects directly)

# Common Errors
- **Error**: Dispatching before the component is initialized
  **Correction**: Ensure dispatch setup is complete before event handlers fire

# Common Confusions
- **Confusion**: Actions must have a "type" property
  **Clarification**: In this book's approach, actions are plain objects merged with state; "type" is a Redux convention

# Source Reference
Chapter 19: Project: A Pixel Art Editor, Section "Components" and "The state", lines 110-232 of 19-project-a-pixel-art-editor.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Clearly defined pattern with examples
- Cross-reference status: verified
