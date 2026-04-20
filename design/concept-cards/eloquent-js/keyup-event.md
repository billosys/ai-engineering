---
# === CORE IDENTIFICATION ===
concept: keyup Event
slug: keyup-event

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-handler
extends: []
related:
  - keydown-event
contrasts_with:
  - keydown-event

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I detect when a key is released?"
---

# Quick Definition
The `"keyup"` event fires when a keyboard key is released, complementing `"keydown"` for tracking key press and release pairs.

# Core Definition
"When a key on the keyboard is pressed, your browser fires a `\"keydown\"` event. When it is released, you get a `\"keyup\"` event." (Eloquent JavaScript, Ch. 15, lines 296-298)

# Prerequisites
- **Event handler**: Registering keyboard event handlers

# Key Properties
1. Fires once when the key is physically released
2. Does not repeat (unlike `keydown`)
3. Has the same `key` and modifier properties as `keydown`
4. Paired with `keydown` for tracking key-hold states

# Construction / Recognition
```javascript
window.addEventListener("keyup", event => {
  if (event.key == "v") {
    document.body.style.background = "";
  }
});
```
(lines 308-312)

# Context & Application
Used together with `keydown` to track the duration of key presses, implement key-hold behaviors, or clean up state when a key is released.

# Examples
From the source, turning the page violet while V is held:
```javascript
window.addEventListener("keydown", event => {
  if (event.key == "v") {
    document.body.style.background = "violet";
  }
});
window.addEventListener("keyup", event => {
  if (event.key == "v") {
    document.body.style.background = "";
  }
});
```
(lines 303-312)

# Relationships
## Builds Upon
- Keyboard event handling
## Enables
- Tracking key-hold duration, releasing visual states
## Related
- `keydown` event (fires on press and repeat)
## Contrasts With
- `keydown` (which fires on press and repeats while held)

# Common Errors
- **Error**: Using `keyup` for real-time key tracking (it fires only on release)
  **Correction**: Use `keydown` for immediate detection; `keyup` for release detection

# Common Confusions
- **Confusion**: `keyup` fires for each `keydown` repeat
  **Clarification**: `keyup` fires only once when the key is physically released, regardless of how many `keydown` repeats occurred

# Source Reference
Chapter 15: Handling Events, Section "Key events", lines 296-312 of 15-handling-events.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clear example showing keydown/keyup pair
- Cross-reference status: verified
