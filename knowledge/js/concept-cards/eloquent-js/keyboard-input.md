---
concept: Keyboard Input Tracking
slug: keyboard-input
category: application-architecture
subcategory: input-handling
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Platform Game"
chapter_number: 16
pdf_page: null
section: "Tracking keys"
extraction_confidence: high
aliases:
  - key tracking
  - input handling
prerequisites:
  - event-handler
  - addeventlistener
extends: []
related:
  - game-loop
  - game-state
contrasts_with: []
answers_questions:
  - "How do you handle continuous keyboard input in a game?"
---

# Quick Definition
Keyboard input tracking maintains a live map of which keys are currently held down, using `keydown` and `keyup` event handlers, so the game loop can poll key states each frame rather than reacting to individual key events.

# Core Definition
Haverbeke explains: "For a game like this, we do not want keys to take effect once per keypress. Rather, we want their effect (moving the player figure) to stay active as long as they are held" (Ch. 16, "Tracking keys"). The `trackKeys` function registers handlers for both `keydown` and `keyup`, maintaining an object where tracked key names map to boolean values.

# Prerequisites
- **Event handlers**: keydown and keyup events
- **addEventListener**: Used to register the key handlers

# Key Properties
1. Returns an object mapping key names to booleans (pressed or not)
2. Uses a single handler for both keydown and keyup events
3. Calls `preventDefault` on tracked keys to prevent page scrolling
4. Polled by the game loop each frame, not event-driven

# Construction / Recognition
```javascript
function trackKeys(keys) {
  let down = Object.create(null);
  function track(event) {
    if (keys.includes(event.key)) {
      down[event.key] = event.type == "keydown";
      event.preventDefault();
    }
  }
  window.addEventListener("keydown", track);
  window.addEventListener("keyup", track);
  return down;
}
const arrowKeys = trackKeys(["ArrowLeft", "ArrowRight", "ArrowUp"]);
```

# Context & Application
Used in games and interactive applications where continuous input matters more than discrete events. The polling approach decouples input from the game loop timing.

# Examples
The player update reads from the keys object:
```javascript
if (keys.ArrowLeft) xSpeed -= playerXSpeed;
if (keys.ArrowRight) xSpeed += playerXSpeed;
```

# Relationships
## Builds Upon
- event-handler, addeventlistener
## Enables
- Player movement, game controls
## Related
- game-loop, game-state
## Contrasts With
- Event-driven input (one action per keypress)

# Common Errors
- **Error**: Forgetting to handle keyup, so keys appear "stuck"
  **Correction**: Always register both keydown (true) and keyup (false) handlers

# Common Confusions
- **Confusion**: Key events fire continuously while held
  **Clarification**: keydown fires repeatedly (with auto-repeat), but tracking down/up state is more reliable

# Source Reference
Chapter 16: Project: A Platform Game, Section "Tracking keys", lines 1033-1075 of 16-project-a-platform-game.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Complete implementation shown
- Cross-reference status: verified
