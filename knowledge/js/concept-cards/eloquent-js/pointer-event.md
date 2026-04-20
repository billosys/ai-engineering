---
# === CORE IDENTIFICATION ===
concept: Pointer Event
slug: pointer-event

# === CLASSIFICATION ===
category: events
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Handling Events"
chapter_number: 15
pdf_page: null
section: "Pointer events"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - touch event
  - touchstart
  - touchmove
  - touchend

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-handler
extends: []
related:
  - mouse-event
contrasts_with:
  - mouse-event

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I handle touch and pointer input?"
---

# Quick Definition
Touch/pointer events (`touchstart`, `touchmove`, `touchend`) fire for touchscreen interactions, supporting multiple simultaneous touch points through the `touches` property.

# Core Definition
"There are specific event types fired by touch interaction. When a finger starts touching the screen, you get a `\"touchstart\"` event. When it is moved while touching, `\"touchmove\"` events fire. Finally, when it stops touching the screen, you'll see a `\"touchend\"` event." (Eloquent JavaScript, Ch. 15, lines 546-550)

# Prerequisites
- **Event handler**: Understanding event registration

# Key Properties
1. `touchstart` -- finger touches the screen
2. `touchmove` -- finger moves while touching
3. `touchend` -- finger lifts from screen
4. `event.touches` -- array-like of all current touch points
5. Each touch point has `clientX`, `clientY`, `pageX`, `pageY`
6. Supports multiple simultaneous fingers
7. Browsers simulate mouse events for basic touch interactions

# Construction / Recognition
```javascript
function update(event) {
  for (let i = 0; i < event.touches.length; i++) {
    let {pageX, pageY} = event.touches[i];
    // position elements at touch points
  }
}
window.addEventListener("touchstart", update);
window.addEventListener("touchmove", update);
window.addEventListener("touchend", update);
```
(lines 571-586)

# Context & Application
Essential for mobile web development and cross-device interaction handling.

# Examples
From the source: "Because many touchscreens can detect multiple fingers at the same time, these events don't have a single set of coordinates associated with them. Rather, their event objects have a `touches` property, which holds an array-like object of points." (lines 553-557)

"You'll often want to call `preventDefault` in touch event handlers to override the browser's default behavior (which may include scrolling the page on swiping) and to prevent the mouse events from being fired." (lines 590-594)

# Relationships
## Builds Upon
- Event handling system
## Enables
- Mobile-friendly interactions
## Related
- Mouse events (similar but for mouse/trackpad)
## Contrasts With
- Mouse events (single pointer, no multi-touch)

# Common Errors
- **Error**: Relying only on mouse events for touch devices
  **Correction**: Use touch events for interactions that don't map well to mouse events (multi-touch, gestures)

# Common Confusions
- **Confusion**: Touch events are the same as mouse events
  **Clarification**: "A touchscreen doesn't work like a mouse: it doesn't have multiple buttons, you can't track the finger when it isn't on the screen, and it allows multiple fingers." (lines 534-537)

# Source Reference
Chapter 15: Handling Events, Section "Pointer events / Touch events", lines 522-594 of 15-handling-events.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Medium -- covers touch events; the "pointer" event API is not discussed separately
- Cross-reference status: verified
