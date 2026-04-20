---
# === CORE IDENTIFICATION ===
concept: Game Loop
slug: game-loop

# === CLASSIFICATION ===
category: application-architecture
subcategory: animation
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Platform Game"
chapter_number: 16
pdf_page: null
section: "Running the game"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - animation loop
  - frame loop
  - update loop

# === TYPED RELATIONSHIPS ===
prerequisites:
  - requestanimationframe
  - function
extends: []
related:
  - game-state
  - animation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a game continuously update and render?"
  - "What is the basic structure of a game loop?"
---

# Quick Definition
A game loop is a programming pattern that repeatedly updates game state and redraws the display, typically synchronized with the browser's refresh rate via `requestAnimationFrame`.

# Core Definition
In the platform game project, the game loop splits time into small steps and, for each step, moves actors by a distance corresponding to their speed multiplied by the size of the time step. As Haverbeke explains: "The basic approach taken by most games like this is to split time into small steps and, for each step, move the actors by a distance corresponding to their speed multiplied by the size of the time step" (Ch. 16, "Motion and collision"). The `runAnimation` helper wraps `requestAnimationFrame` to provide time-difference-based frame updates.

# Prerequisites
- **requestAnimationFrame**: The browser API that schedules the next frame callback
- **Functions/Closures**: The loop is built from nested functions that close over state

# Key Properties
1. Each frame receives the elapsed time since the last frame
2. Time steps are capped to prevent large jumps (max 100ms)
3. The loop continues until the frame function returns `false`
4. Time is converted to seconds for easier reasoning about speeds

# Construction / Recognition
```javascript
function runAnimation(frameFunc) {
  let lastTime = null;
  function frame(time) {
    if (lastTime != null) {
      let timeStep = Math.min(time - lastTime, 100) / 1000;
      if (frameFunc(timeStep) === false) return;
    }
    lastTime = time;
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
}
```

# Context & Application
Used whenever continuous animation or simulation is needed in the browser. Games, physics simulations, and interactive visualizations all rely on this pattern. The time-step approach allows frame-rate-independent movement.

# Examples
From Chapter 16, the `runLevel` function uses the game loop:
```javascript
function runLevel(level, Display) {
  let display = new Display(document.body, level);
  let state = State.start(level);
  let ending = 1;
  return new Promise(resolve => {
    runAnimation(time => {
      state = state.update(time, arrowKeys);
      display.syncState(state);
      if (state.status == "playing") {
        return true;
      } else if (ending > 0) {
        ending -= time;
        return true;
      } else {
        display.clear();
        resolve(state.status);
        return false;
      }
    });
  });
}
```

# Relationships
## Builds Upon
- requestAnimationFrame, closure, promise
## Enables
- Smooth animation, physics simulation, interactive games
## Related
- game-state, animation, display-abstraction
## Contrasts With
- setInterval-based animation (less precise, not synced with display refresh)

# Common Errors
- **Error**: Not capping the time step, causing huge jumps after tab switches
  **Correction**: Use `Math.min(time - lastTime, 100)` to cap the maximum step

# Common Confusions
- **Confusion**: The game loop runs at a fixed interval
  **Clarification**: It runs synchronized with the browser's repaint cycle; the time step varies between frames

# Source Reference
Chapter 16: Project: A Platform Game, Section "Running the game", lines 1077-1195 of 16-project-a-platform-game.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Explicitly described with full code example
- Cross-reference status: verified against requestAnimationFrame in Ch. 14
