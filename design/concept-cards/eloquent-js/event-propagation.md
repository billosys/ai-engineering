---
# === CORE IDENTIFICATION ===
concept: Event Propagation
slug: event-propagation

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
  - event flow
  - event bubbling

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-handler
  - document-tree
extends: []
related:
  - event-bubbling
  - stoppropagation
  - event-delegation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is event propagation?"
  - "How does event bubbling relate to event delegation?"
---

# Quick Definition
Event propagation is the process by which an event travels from the target node outward through parent nodes to the document root, triggering handlers at each level.

# Core Definition
"For most event types, handlers registered on nodes with children will also receive events that happen in the children. If a button inside a paragraph is clicked, event handlers on the paragraph will also see the click event." "The event is said to *propagate* outward from the node where it happened to that node's parent node and on to the root of the document." (Eloquent JavaScript, Ch. 15, lines 177-180, 185-187)

# Prerequisites
- **Event handlers**: Understanding handler registration
- **Document tree**: Understanding the parent-child hierarchy

# Key Properties
1. Events propagate outward (bottom-up) through the DOM tree
2. More specific handlers (closer to target) run first
3. After specific handlers, parent handlers run, up to the window
4. `stopPropagation()` prevents further propagation
5. Some events (focus, blur) do NOT propagate

# Construction / Recognition
```javascript
para.addEventListener("mousedown", () => {
  console.log("Handler for paragraph.");
});
button.addEventListener("mousedown", event => {
  console.log("Handler for button.");
  if (event.button == 2) event.stopPropagation();
});
```
(lines 212-219)

# Context & Application
Understanding propagation is essential for event delegation patterns, handling events at parent level, and preventing unwanted handler execution.

# Examples
From the source: "If both the paragraph and the button have a handler, the more specific handler---the one on the button---gets to go first." (lines 183-185)

"Finally, after all handlers registered on a specific node have had their turn, handlers registered on the whole window get a chance to respond to the event." (lines 187-189)

# Relationships
## Builds Upon
- Event handlers and DOM tree hierarchy
## Enables
- Event delegation pattern
- Handling events at ancestor level
## Related
- `stopPropagation` (stops propagation)
- Event delegation (leverages propagation)
## Contrasts With
- Events that don't propagate (focus, blur, load)

# Common Errors
- **Error**: Expecting all events to propagate
  **Correction**: Focus-related events and load events do not propagate

# Common Confusions
- **Confusion**: Events propagate downward
  **Clarification**: In the bubbling phase (the default), events propagate upward from target to root

# Source Reference
Chapter 15: Handling Events, Section "Propagation", lines 174-248 of 15-handling-events.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Thoroughly explained with examples
- Cross-reference status: verified
