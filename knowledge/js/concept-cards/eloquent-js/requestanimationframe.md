---
concept: requestAnimationFrame
slug: requestanimationframe
category: graphics
subcategory: animation
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Project: A Platform Game"
chapter_number: 16
pdf_page: null
section: "Running the game"
extraction_confidence: high
aliases:
  - rAF
  - animation frame
prerequisites:
  - function
  - closure
extends: []
related:
  - game-loop
  - animation
contrasts_with: []
answers_questions:
  - "How do I animate something smoothly in the browser?"
  - "What is the preferred way to schedule rendering updates?"
---

# Quick Definition
`requestAnimationFrame` is a browser API that schedules a function to be called before the next screen repaint, providing the foundation for smooth, efficient animations.

# Core Definition
As described in Chapter 16: "The `requestAnimationFrame` function [...] provides a good way to animate a game. But its interface is quite primitive -- using it requires us to track the time at which our function was called the last time around and call `requestAnimationFrame` again after every frame." The function receives a timestamp argument indicating when the callback was invoked.

# Prerequisites
- **Functions**: Callback function passed to requestAnimationFrame
- **Closures**: Used to track state between frames

# Key Properties
1. Called approximately 60 times per second (matching typical display refresh)
2. Automatically pauses when the tab/window is hidden
3. Receives a high-resolution timestamp as its argument
4. Must be called again within the callback to continue the animation

# Construction / Recognition
```javascript
function frame(time) {
  // update and draw
  requestAnimationFrame(frame);
}
requestAnimationFrame(frame);
```

# Context & Application
Used for any browser animation -- games, UI transitions, data visualizations. Preferred over `setInterval` or `setTimeout` because it synchronizes with the display's refresh rate and pauses when not visible.

# Examples
From the `runAnimation` wrapper in Chapter 16:
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

# Relationships
## Builds Upon
- Browser event loop, callback functions
## Enables
- game-loop, smooth animation, canvas rendering
## Related
- game-state, animation
## Contrasts With
- setInterval (not synced with display, runs in background tabs)

# Common Errors
- **Error**: Forgetting to call `requestAnimationFrame` again inside the callback
  **Correction**: Each frame must schedule the next one to keep the animation running

# Common Confusions
- **Confusion**: `requestAnimationFrame` runs at exactly 60fps
  **Clarification**: It matches the display refresh rate, which may vary; time-based movement is essential

# Source Reference
Chapter 16: Project: A Platform Game, Section "Running the game", lines 1080-1106 of 16-project-a-platform-game.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Explicitly discussed with usage example
- Cross-reference status: verified (referenced from Ch. 14)
