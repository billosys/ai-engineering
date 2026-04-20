---
# === CORE IDENTIFICATION ===
concept: keydown Event
slug: keydown-event

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
section: "Key events"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - keyboard event
  - key press event

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-handler
  - event-object
extends: []
related:
  - keyup-event
  - mouse-event
contrasts_with:
  - keyup-event

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I respond to keyboard input?"
---

# Quick Definition
The `"keydown"` event fires when a keyboard key is pressed (and repeats while held), with the event's `key` property indicating which key was pressed.

# Core Definition
"When a key on the keyboard is pressed, your browser fires a `\"keydown\"` event." "Despite its name, `\"keydown\"` fires not only when the key is physically pushed down. When a key is pressed and held, the event fires again every time the key *repeats*." (Eloquent JavaScript, Ch. 15, lines 296-297, 317-319)

# Prerequisites
- **Event handler**: Registering keyboard event handlers
- **Event object**: Using event properties for key identification

# Key Properties
1. `event.key` -- string identifying the key (e.g., `"v"`, `"Enter"`, `"ArrowUp"`)
2. Fires repeatedly when a key is held down
3. Shift modifies the key name (`"v"` becomes `"V"`)
4. Modifier key states available via `shiftKey`, `ctrlKey`, `altKey`, `metaKey`
5. Fires on the element with focus, or `document.body` if nothing focused

# Construction / Recognition
```javascript
window.addEventListener("keydown", event => {
  if (event.key == "v") {
    document.body.style.background = "violet";
  }
});
```
(lines 303-307)

Key combination detection:
```javascript
window.addEventListener("keydown", event => {
  if (event.key == " " && event.ctrlKey) {
    console.log("Continuing!");
  }
});
```
(lines 348-352)

# Context & Application
Used for keyboard shortcuts, game controls, text input handling, and accessibility features.

# Examples
From the source: "The previous example looks at the `key` property of the event object to see which key the event is about. This property holds a string that, for most keys, corresponds to the thing that pressing that key would type. For special keys such as [enter], it holds a string that names the key (`\"Enter\"`)." (lines 326-330)

# Relationships
## Builds Upon
- Event handling system
## Enables
- Keyboard-driven interaction
## Related
- `keyup` event (fires on key release)
## Contrasts With
- `keyup` (which fires once when the key is released)

# Common Errors
- **Error**: Not accounting for key repeat when a key is held
  **Correction**: "You might accidentally add hundreds of buttons when the key is held down longer." (lines 321-323)

# Common Confusions
- **Confusion**: Using key events to track text input
  **Clarification**: "To notice when something was typed... it is best to directly read it from the focused field." Use `"input"` events instead. (lines 376-381)

# Source Reference
Chapter 15: Handling Events, Section "Key events", lines 293-381 of 15-handling-events.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Thoroughly explained with multiple examples
- Cross-reference status: verified
