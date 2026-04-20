---
concept: Undo Functionality
slug: undo-functionality
category: application-architecture
subcategory: ui-patterns
tier: advanced
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Pixel Art Editor"
chapter_number: 19
pdf_page: null
section: "Undo history"
extraction_confidence: high
aliases:
  - undo history
  - undo/redo
prerequisites:
  - persistent-state
  - state-management
extends: []
related:
  - dispatch-pattern
  - application-state-update
contrasts_with: []
answers_questions:
  - "How do you implement undo in a web application?"
---

# Quick Definition
Undo functionality stores previous states in an array, enabling reversal of changes by replacing the current state with the most recent stored version, made easy by immutable (persistent) data structures.

# Core Definition
"To be able to undo changes, we need to store previous versions of the picture. Since pictures are immutable values, that's easy" (Ch. 19, "Undo history"). The `done` array holds previous pictures. An undo action pops the most recent version. Changes are only stored when more than a second has elapsed to avoid storing every single pixel drag.

# Prerequisites
- **Persistent state**: Immutable data makes storing previous versions trivial
- **State management**: Undo integrates into the state update cycle

# Key Properties
1. `done` array stores previous picture versions
2. `doneAt` timestamp throttles storage to once per second
3. Undo action replaces current picture with `done[0]`
4. Immutable data means "storing" a version is just keeping a reference

# Construction / Recognition
```javascript
function historyUpdateState(state, action) {
  if (action.undo == true) {
    if (state.done.length == 0) return state;
    return {
      ...state,
      picture: state.done[0],
      done: state.done.slice(1),
      doneAt: 0
    };
  } else if (action.picture && state.doneAt < Date.now() - 1000) {
    return {
      ...state, ...action,
      done: [state.picture, ...state.done],
      doneAt: Date.now()
    };
  } else {
    return {...state, ...action};
  }
}
```

# Context & Application
Undo is essential in any creative application. The immutable data approach makes it particularly elegant -- no need to compute reverse operations, just restore the previous state.

# Examples
The UndoButton component:
```javascript
class UndoButton {
  constructor(state, {dispatch}) {
    this.dom = elt("button", {
      onclick: () => dispatch({undo: true}),
      disabled: state.done.length == 0
    }, "Undo");
  }
  syncState(state) {
    this.dom.disabled = state.done.length == 0;
  }
}
```

# Relationships
## Builds Upon
- persistent-state, state-management, dispatch-pattern
## Enables
- Non-destructive editing, user confidence, experimentation
## Related
- application-state-update
## Contrasts With
- Command pattern undo (stores operations and their inverses)

# Common Errors
- **Error**: Storing state on every single change (memory issues)
  **Correction**: Throttle history storage with a time-based check (e.g., once per second)

# Common Confusions
- **Confusion**: Undo requires computing the reverse of each operation
  **Clarification**: With immutable data, you just store and restore previous state snapshots

# Source Reference
Chapter 19: Project: A Pixel Art Editor, Section "Undo history", lines 825-903 of 19-project-a-pixel-art-editor.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Complete implementation with rationale
- Cross-reference status: verified
