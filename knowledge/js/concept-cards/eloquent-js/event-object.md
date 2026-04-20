---
# === CORE IDENTIFICATION ===
concept: Event Object
slug: event-object

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
section: "Event objects"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - event parameter

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-handler
extends: []
related:
  - event-type
  - stoppropagation
  - preventdefault
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an event?"
---

# Quick Definition
The event object is passed as an argument to event handler functions, containing information about the event such as its type, target element, and event-specific data.

# Core Definition
"Event handler functions are passed an argument: the *event object*. This object holds additional information about the event." "The object's `type` property always holds a string identifying the event (such as `\"click\"` or `\"mousedown\"`)." (Eloquent JavaScript, Ch. 15, lines 147-148, 171-172)

# Prerequisites
- **Event handler**: Event objects are received by handlers

# Key Properties
1. `type` -- string identifying the event (e.g., `"click"`, `"keydown"`)
2. `target` -- the node where the event originated
3. `button` -- which mouse button was pressed (for mouse events)
4. `key` -- which key was pressed (for key events)
5. `clientX`/`clientY` -- mouse coordinates relative to viewport
6. `pageX`/`pageY` -- mouse coordinates relative to document
7. Methods: `stopPropagation()`, `preventDefault()`

# Construction / Recognition
```javascript
button.addEventListener("mousedown", event => {
  if (event.button == 0) {
    console.log("Left button");
  } else if (event.button == 1) {
    console.log("Middle button");
  } else if (event.button == 2) {
    console.log("Right button");
  }
});
```
(lines 156-165)

# Context & Application
Event objects provide all the context needed to understand and respond to an event -- what happened, where, and to what element.

# Examples
From the source: "The information stored in an event object differs per type of event." (lines 169-170)

"Most event objects have a `target` property that refers to the node where they originated." (lines 223-224)

# Relationships
## Builds Upon
- Event handlers that receive event objects
## Enables
- Detailed event handling based on event properties
## Related
- `stopPropagation`, `preventDefault` (methods on event objects)
## Contrasts With
- No-argument callbacks (which don't receive event info)

# Common Errors
- **Error**: Forgetting to declare the event parameter in the handler
  **Correction**: Include the parameter: `event => { ... }` rather than `() => { ... }`

# Common Confusions
- **Confusion**: All event objects have the same properties
  **Clarification**: Properties vary by event type (mouse events have coordinates, key events have `key`)

# Source Reference
Chapter 15: Handling Events, Section "Event objects", lines 143-172 of 15-handling-events.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with examples
- Cross-reference status: verified
