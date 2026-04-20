---
concept: Display Abstraction
slug: display-abstraction
category: application-architecture
subcategory: design-patterns
tier: advanced
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Platform Game"
chapter_number: 16
pdf_page: null
section: "Drawing"
extraction_confidence: high
aliases:
  - display interface
  - rendering abstraction
prerequisites:
  - class-declaration
  - interface
extends: []
related:
  - game-loop
  - game-state
  - canvas-element
contrasts_with: []
answers_questions:
  - "How do you separate rendering from game logic?"
  - "What must I know before building a web application?"
---

# Quick Definition
A display abstraction defines a common interface for rendering game state, allowing different implementations (DOM-based, canvas-based) to be swapped without changing the game logic.

# Core Definition
The game uses an interface-based approach to rendering: "We put the drawing logic behind an interface and pass it to the game as an argument. That way, we can use the same game program with different new display modules" (Ch. 16, "Drawing"). Both `DOMDisplay` and `CanvasDisplay` implement `syncState(state)` and `clear()` methods.

# Prerequisites
- **Classes**: Display modules are classes
- **Interfaces**: Both displays conform to the same interface

# Key Properties
1. `constructor(parent, level)` -- creates the display in a parent element
2. `syncState(state)` -- updates the display to match the current game state
3. `clear()` -- removes the display from the document
4. The game loop passes the display constructor, not an instance

# Construction / Recognition
```javascript
// DOMDisplay
class DOMDisplay {
  constructor(parent, level) { /* ... */ }
  clear() { this.dom.remove(); }
}
DOMDisplay.prototype.syncState = function(state) { /* ... */ };

// CanvasDisplay
class CanvasDisplay {
  constructor(parent, level) { /* ... */ }
  clear() { this.canvas.remove(); }
}
CanvasDisplay.prototype.syncState = function(state) { /* ... */ };

// Usage -- swap by passing different constructor
runGame(GAME_LEVELS, DOMDisplay);
runGame(GAME_LEVELS, CanvasDisplay);
```

# Context & Application
This is the Strategy pattern -- varying behavior by injecting different implementations of the same interface. Common in games, UI frameworks, and any system where rendering should be decoupled from logic.

# Examples
The `runLevel` function accepts a Display constructor:
```javascript
function runLevel(level, Display) {
  let display = new Display(document.body, level);
  let state = State.start(level);
  // ...
}
```

# Relationships
## Builds Upon
- class-declaration, interface
## Enables
- Multiple rendering backends, testability, separation of concerns
## Related
- game-loop, game-state, canvas-element
## Contrasts With
- Hard-coded rendering (single display implementation mixed with game logic)

# Common Errors
- **Error**: Making game logic depend on display implementation details
  **Correction**: Game logic should only call the display interface methods

# Common Confusions
- **Confusion**: The display class IS the game
  **Clarification**: The display is purely a view; all game logic lives in State and actor updates

# Source Reference
Chapter 16: Project: A Platform Game, Section "Drawing", lines 463-477 of 16-project-a-platform-game.md; Chapter 17 Section "Back to the game", lines 804-850.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Explicitly described design decision
- Cross-reference status: verified (DOMDisplay in Ch. 16, CanvasDisplay in Ch. 17)
