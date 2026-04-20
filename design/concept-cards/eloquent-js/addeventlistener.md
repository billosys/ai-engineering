---
# === CORE IDENTIFICATION ===
concept: addEventListener
slug: addeventlistener

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
section: "Events and DOM nodes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - add event listener

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-handler
  - element-node
extends: []
related:
  - removeeventlistener
  - event-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I add an event listener to a DOM element?"
---

# Quick Definition
`addEventListener` registers a function to be called whenever a specified event type occurs on the target element, allowing multiple handlers per event.

# Core Definition
"The `window` binding refers to a built-in object provided by the browser. It represents the browser window that contains the document. Calling its `addEventListener` method registers the second argument to be called whenever the event described by its first argument occurs." "The `addEventListener` method allows you to add any number of handlers, meaning it's safe to add handlers even if there is already another handler on the element." (Eloquent JavaScript, Ch. 15, lines 75-79, 116-118)

# Prerequisites
- **Event handler**: Understanding what event handlers are
- **Element node**: Target of event registration

# Key Properties
1. First argument: event type string (e.g., `"click"`, `"keydown"`)
2. Second argument: handler function
3. Can register multiple handlers for the same event
4. Available on DOM elements, `window`, and `document`
5. Safer than `onclick` attributes (supports multiple handlers)

# Construction / Recognition
```javascript
let button = document.querySelector("button");
button.addEventListener("click", () => {
  console.log("Button clicked.");
});
```
(lines 95-98)

# Context & Application
The standard and recommended way to register event handlers in modern JavaScript.

# Examples
From the source, registering on `window`:
```javascript
window.addEventListener("click", () => {
  console.log("You knocked?");
});
```
(lines 68-70)

# Relationships
## Builds Upon
- Event handler concept and DOM elements
## Enables
- Interactive web applications
## Related
- `removeEventListener` (unregisters handlers)
## Contrasts With
- `onclick` and other attribute-based handlers (only one per element)

# Common Errors
- **Error**: Passing the result of a function call instead of the function itself
  **Correction**: Pass the function reference, not `myFunction()` (which calls it immediately)

# Common Confusions
- **Confusion**: `addEventListener` replaces existing handlers
  **Clarification**: It adds to them; use `removeEventListener` to remove specific handlers

# Source Reference
Chapter 15: Handling Events, Section "Events and DOM nodes", lines 81-118 of 15-handling-events.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with examples
- Cross-reference status: verified
