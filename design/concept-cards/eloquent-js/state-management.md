---
concept: State Management
slug: state-management
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
  - centralized state
  - single source of truth
prerequisites:
  - object
  - component-pattern
extends: []
related:
  - dispatch-pattern
  - application-state-update
  - persistent-state
contrasts_with: []
answers_questions:
  - "How do you manage application state?"
  - "What must I know before building a web application?"
---

# Quick Definition
State management centralizes application data in a single state object, with interface components reading from it and dispatching actions to update it, avoiding distributed state that creates synchronization problems.

# Core Definition
"The state of the application consists of the current picture, the selected tool, and the selected color. We'll set things up so that the state lives in a single value and the interface components always base the way they look on the current state" (Ch. 19, "Components"). This avoids the problem where "each part of the interface needs to know about all other parts, which is not very modular."

# Prerequisites
- **Objects**: State is an object
- **Components**: Components consume and update state

# Key Properties
1. State is a single value (object) that components read from
2. Components may dispatch actions but never modify state directly
3. State changes go through a single well-defined channel
4. After update, all components synchronize to the new state
5. "There are many variants of this approach [...] but their central idea is the same"

# Construction / Recognition
```javascript
function startPixelEditor({state = startState, tools, controls}) {
  let app = new PixelEditor(state, {
    tools, controls,
    dispatch(action) {
      state = historyUpdateState(state, action);
      app.syncState(state);
    }
  });
  return app.dom;
}
```

# Context & Application
This is the pattern behind Redux, Vuex, and other state management libraries. The chapter demonstrates it from scratch to explain why such libraries exist.

# Examples
"In effect, this creates a problem where each part of the interface needs to know about all other parts [...] To avoid this nightmare on principle, we're going to be strict about data flow."

# Relationships
## Builds Upon
- object, component-pattern
## Enables
- Predictable UI updates, undo-functionality, debugging
## Related
- dispatch-pattern, application-state-update, persistent-state
## Contrasts With
- Distributed state (each component manages its own piece)

# Common Errors
- **Error**: Components modifying state objects directly
  **Correction**: All state changes must go through the dispatch/update cycle

# Common Confusions
- **Confusion**: Centralized state is always better
  **Clarification**: "For small applications [...] that may not be a problem. For bigger projects, it can turn into a real nightmare."

# Source Reference
Chapter 19: Project: A Pixel Art Editor, Section "Components", lines 60-128 of 19-project-a-pixel-art-editor.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Core architectural concept thoroughly explained
- Cross-reference status: verified
