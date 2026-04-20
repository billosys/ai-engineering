---
# === CORE IDENTIFICATION ===
concept: Event Handler
slug: event-handler

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
section: "Event handlers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - handler
  - event listener

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
  - document-object-model
extends: []
related:
  - addeventlistener
  - event-object
  - event-type
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an event?"
  - "How do I add an event listener to a DOM element?"
---

# Quick Definition
An event handler is a function registered to be called when a specific event occurs on a DOM element, enabling programs to respond to user interactions.

# Core Definition
"A better mechanism is for the system to actively notify the code when an event occurs. Browsers do this by allowing us to register functions as *handlers* for specific events." (Eloquent JavaScript, Ch. 15, lines 61-63)

# Prerequisites
- **Functions**: Handlers are functions
- **DOM**: Events occur on DOM elements

# Key Properties
1. Registered using `addEventListener` on DOM nodes or `window`
2. Called only when the event happens in the registered context
3. Multiple handlers can be registered for the same event
4. Handlers receive an event object as their argument
5. Process asynchronously via the event loop

# Construction / Recognition
```javascript
window.addEventListener("click", () => {
  console.log("You knocked?");
});
```
(lines 68-70)

# Context & Application
Event handlers are the primary mechanism for making web pages interactive, responding to clicks, keyboard input, scrolling, and other user actions.

# Examples
From the source, a button-specific handler:
```javascript
let button = document.querySelector("button");
button.addEventListener("click", () => {
  console.log("Button clicked.");
});
```
(lines 95-98)

"Event listeners are called only when the event happens in the context of the object on which they are registered." (lines 88-89)

# Relationships
## Builds Upon
- Functions as first-class values, DOM
## Enables
- Interactive web pages
## Related
- `addEventListener` (registration method)
- Event objects (data about the event)
## Contrasts With
- Polling (the alternative to event-driven input, described as inferior)

# Common Errors
- **Error**: Using `onclick` attribute when you need multiple handlers
  **Correction**: "A node can have only one `onclick` attribute, so you can register only one handler per node that way." Use `addEventListener` instead. (lines 114-115)

# Common Confusions
- **Confusion**: Event handlers run immediately when registered
  **Clarification**: They are called only when the event actually occurs

# Source Reference
Chapter 15: Handling Events, Section "Event handlers", lines 36-141 of 15-handling-events.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Central concept of the chapter
- Cross-reference status: verified against chapter summary
