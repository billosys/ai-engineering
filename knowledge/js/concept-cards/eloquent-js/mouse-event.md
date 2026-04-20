---
# === CORE IDENTIFICATION ===
concept: Mouse Event
slug: mouse-event

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
extraction_confidence: high

# === VARIANTS ===
aliases:
  - click event
  - mousedown event
  - mouseup event
  - mousemove event

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-handler
  - event-object
extends: []
related:
  - pointer-event
  - keydown-event
contrasts_with:
  - keydown-event

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I handle mouse interactions?"
---

# Quick Definition
Mouse events (`mousedown`, `mouseup`, `click`, `dblclick`, `mousemove`) fire in response to mouse button presses, releases, and pointer movement, with coordinates available via `clientX`/`clientY` or `pageX`/`pageY`.

# Core Definition
"Pressing a mouse button causes a number of events to fire. The `\"mousedown\"` and `\"mouseup\"` events are similar to `\"keydown\"` and `\"keyup\"` and fire when the button is pressed and released. These happen on the DOM nodes that are immediately below the mouse pointer when the event occurs." After `mouseup`, a `"click"` event fires. (Eloquent JavaScript, Ch. 15, lines 394-407)

# Prerequisites
- **Event handler**: Registering event handlers
- **Event object**: Accessing event properties

# Key Properties
1. `mousedown`/`mouseup` -- button press and release
2. `click` -- fires on most specific node containing both press and release
3. `dblclick` -- fires after two close-together clicks
4. `mousemove` -- fires every time the mouse pointer moves
5. `event.button` -- which button (0=left, 1=middle, 2=right)
6. `event.buttons` -- bitmask of currently held buttons (1=left, 2=right, 4=middle)
7. `clientX`/`clientY` -- coordinates relative to window
8. `pageX`/`pageY` -- coordinates relative to document

# Construction / Recognition
```javascript
window.addEventListener("click", event => {
  let dot = document.createElement("div");
  dot.className = "dot";
  dot.style.left = (event.pageX - 4) + "px";
  dot.style.top = (event.pageY - 4) + "px";
  document.body.appendChild(dot);
});
```
(lines 440-447)

# Context & Application
Mouse events are fundamental for interactive web applications, drawing applications, drag-and-drop, and custom UI controls.

# Examples
From the source, implementing a draggable bar:
```javascript
bar.addEventListener("mousedown", event => {
  if (event.button == 0) {
    lastX = event.clientX;
    window.addEventListener("mousemove", moved);
    event.preventDefault();
  }
});
```
(lines 474-480)

"Note that the order of these codes is different from the one used by `button`, where the middle button came before the right one. As mentioned, consistency isn't a strong point of the browser's programming interface." (lines 517-520)

# Relationships
## Builds Upon
- Event handling system
## Enables
- Click handling, drag and drop, drawing, custom controls
## Related
- Pointer events (unified mouse/touch)
- Touch events (mobile-specific)
## Contrasts With
- Key events (keyboard input)

# Common Errors
- **Error**: Confusing `event.button` (single button) with `event.buttons` (bitmask of held buttons)
  **Correction**: `button` tells you which button triggered the event; `buttons` tells you all currently held buttons

# Common Confusions
- **Confusion**: `click` fires where the mouse currently is
  **Clarification**: `click` fires on "the most specific node that contained both the press and the release of the button"

# Source Reference
Chapter 15: Handling Events, Section "Pointer events", lines 383-520 of 15-handling-events.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Thoroughly covered with multiple examples
- Cross-reference status: verified
