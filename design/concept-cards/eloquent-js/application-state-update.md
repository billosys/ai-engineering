---
concept: Application State Update
slug: application-state-update
category: application-architecture
subcategory: ui-patterns
tier: advanced
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Pixel Art Editor"
chapter_number: 19
pdf_page: null
section: "The state"
extraction_confidence: high
aliases:
  - state reducer
  - update function
prerequisites:
  - state-management
  - dispatch-pattern
extends: []
related:
  - persistent-state
  - undo-functionality
contrasts_with: []
answers_questions:
  - "How do you compute new application state from actions?"
---

# Quick Definition
The state update function takes the current state and an action object, returning a new state by merging the action's properties into the existing state using object spread syntax.

# Core Definition
"This pattern, in which object spread is used to first add the properties of an existing object and then override some of those, is common in JavaScript code that uses immutable objects" (Ch. 19, "The state"). The basic update function is `{...state, ...action}`; the history-aware version adds undo tracking.

# Prerequisites
- **State management**: Update function is the core of state management
- **Dispatch pattern**: Actions are dispatched to the update function

# Key Properties
1. Pure function: (state, action) => newState
2. Uses object spread to merge action into state
3. Never mutates the input state
4. Can be extended for undo, validation, etc.

# Construction / Recognition
```javascript
function updateState(state, action) {
  return {...state, ...action};
}

// Extended with undo:
function historyUpdateState(state, action) {
  if (action.undo == true) {
    // restore from history
  } else if (action.picture && state.doneAt < Date.now() - 1000) {
    // save to history, then apply
  } else {
    return {...state, ...action};
  }
}
```

# Context & Application
This is equivalent to a Redux reducer. The simple spread-merge pattern works for flat state; more complex applications need specialized logic.

# Examples
Action: `{color: "#ff0000"}` → new state has color changed, everything else preserved.

# Relationships
## Builds Upon
- state-management, dispatch-pattern
## Enables
- Predictable state transitions, undo-functionality, state history
## Related
- persistent-state, component-pattern
## Contrasts With
- Direct mutation (modifying state properties in place)

# Common Errors
- **Error**: Returning the same object reference after mutation
  **Correction**: Always create new objects; components may use reference equality to skip updates

# Common Confusions
- **Confusion**: The update function must handle every possible action type
  **Clarification**: The spread merge `{...state, ...action}` handles any property update generically

# Source Reference
Chapter 19: Project: A Pixel Art Editor, Section "The state", lines 222-232 of 19-project-a-pixel-art-editor.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Pattern explicitly described
- Cross-reference status: verified
