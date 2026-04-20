---
# === CORE IDENTIFICATION ===
concept: Focus Event
slug: focus-event

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
section: "Focus events"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - focus
  - blur

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-handler
extends: []
related:
  - event-propagation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I detect focus changes?"
---

# Quick Definition
Focus events (`"focus"` and `"blur"`) fire when an element gains or loses focus, but unlike most events, they do not propagate to parent elements.

# Core Definition
"When an element gains focus, the browser fires a `\"focus\"` event on it. When it loses focus, the element gets a `\"blur\"` event." "Unlike the events discussed earlier, these two events do not propagate." (Eloquent JavaScript, Ch. 15, lines 658-660, 663-664)

# Prerequisites
- **Event handler**: Registering focus event handlers

# Key Properties
1. `focus` fires when an element gains focus
2. `blur` fires when an element loses focus
3. Do NOT propagate to parent elements
4. Window also receives focus/blur when the browser tab/window gains or loses focus
5. Focusable elements include links, buttons, and form fields (or elements with `tabindex`)

# Construction / Recognition
```javascript
let fields = document.querySelectorAll("input");
for (let field of Array.from(fields)) {
  field.addEventListener("focus", event => {
    let text = event.target.getAttribute("data-help");
    help.textContent = text;
  });
  field.addEventListener("blur", event => {
    help.textContent = "";
  });
}
```
(lines 678-688)

# Context & Application
Used for form validation, help text display, accessibility features, and tracking user attention.

# Examples
From the source, displaying help text for the focused field (lines 678-688 shown above).

"The window object will receive `\"focus\"` and `\"blur\"` events when the user moves from or to the browser tab or window in which the document is shown." (lines 698-700)

# Relationships
## Builds Upon
- Event handling system
## Enables
- Form interaction feedback, accessibility features
## Related
- Event propagation (focus events are an exception -- they don't propagate)
## Contrasts With
- Most other events (which do propagate)

# Common Errors
- **Error**: Expecting focus events to bubble up to parent elements
  **Correction**: Focus and blur events do not propagate; register handlers directly on the target elements

# Common Confusions
- **Confusion**: All elements can receive focus
  **Clarification**: Only links, buttons, form fields, and elements with `tabindex` attribute can receive focus

# Source Reference
Chapter 15: Handling Events, Section "Focus events", lines 655-700 of 15-handling-events.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with example
- Cross-reference status: verified
