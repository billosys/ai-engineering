---
# === CORE IDENTIFICATION ===
concept: stopPropagation
slug: stoppropagation

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
section: "Propagation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - stop propagation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-propagation
  - event-object
extends: []
related:
  - preventdefault
contrasts_with:
  - preventdefault

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I stop event propagation?"
---

# Quick Definition
`stopPropagation()` is a method on event objects that prevents the event from continuing to propagate to parent elements' handlers.

# Core Definition
"At any point, an event handler can call the `stopPropagation` method on the event object to prevent handlers further up from receiving the event." (Eloquent JavaScript, Ch. 15, lines 192-194)

# Prerequisites
- **Event propagation**: Understanding how events travel up the DOM
- **Event object**: The method is called on the event object

# Key Properties
1. Prevents parent handlers from receiving the event
2. Does not prevent other handlers on the same element from running
3. Does not prevent the browser's default action
4. Useful for preventing unintended handling by ancestor elements

# Construction / Recognition
```javascript
button.addEventListener("mousedown", event => {
  console.log("Handler for button.");
  if (event.button == 2) event.stopPropagation();
});
```
(lines 215-218)

# Context & Application
Used when a child element handles an event and wants to prevent parent elements from also handling it, such as a button inside a clickable container.

# Examples
From the source: "This can be useful when, for example, you have a button inside another clickable element and you don't want clicks on the button to activate the outer element's click behavior." (lines 194-197)

# Relationships
## Builds Upon
- Event propagation mechanism
## Enables
- Preventing unwanted handler execution on ancestor elements
## Related
- `preventDefault` (prevents default browser action, different concept)
## Contrasts With
- `preventDefault` (stops default action, not propagation)

# Common Errors
- **Error**: Using `stopPropagation` when `preventDefault` is needed
  **Correction**: `stopPropagation` stops parent handlers; `preventDefault` stops browser default behavior

# Common Confusions
- **Confusion**: `stopPropagation` prevents the browser's default action
  **Clarification**: It only stops other handlers from receiving the event; use `preventDefault` for default actions

# Source Reference
Chapter 15: Handling Events, Section "Propagation", lines 192-220 of 15-handling-events.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with example
- Cross-reference status: verified
