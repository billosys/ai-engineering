---
# === CORE IDENTIFICATION ===
concept: Event Delegation
slug: event-delegation

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
  - delegated events

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-propagation
  - event-object
extends:
  - event-propagation
related:
  - event-bubbling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does event bubbling relate to event delegation?"
---

# Quick Definition
Event delegation is a pattern where a single event handler is registered on a parent element and uses the event's `target` property to determine which child element triggered the event.

# Core Definition
"It is also possible to use the `target` property to cast a wide net for a specific type of event. For example, if you have a node containing a long list of buttons, it may be more convenient to register a single click handler on the outer node and have it use the `target` property to figure out whether a button was clicked, rather than registering individual handlers on all of the buttons." (Eloquent JavaScript, Ch. 15, lines 229-235)

# Prerequisites
- **Event propagation**: Delegation relies on events bubbling up
- **Event object**: Uses the `target` property to identify the source

# Key Properties
1. Single handler on a parent rather than many handlers on children
2. Uses `event.target` to identify the actual source element
3. Works because events propagate up from the target
4. More memory-efficient for many child elements
5. Automatically works for dynamically added child elements

# Construction / Recognition
```javascript
document.body.addEventListener("click", event => {
  if (event.target.nodeName == "BUTTON") {
    console.log("Clicked", event.target.textContent);
  }
});
```
(lines 242-247)

# Context & Application
Used for lists of similar elements (buttons, list items, table rows) where registering individual handlers would be wasteful, and for dynamically generated content.

# Examples
From the source, handling clicks on multiple buttons with one handler:
```html
<button>A</button>
<button>B</button>
<button>C</button>
<script>
  document.body.addEventListener("click", event => {
    if (event.target.nodeName == "BUTTON") {
      console.log("Clicked", event.target.textContent);
    }
  });
</script>
```
(lines 238-248)

# Relationships
## Builds Upon
- Event propagation (bubbling)
## Enables
- Efficient handling of many similar elements
- Handling events on dynamically created elements
## Related
- Event bubbling (the mechanism that makes delegation possible)
## Contrasts With
- Individual handlers on each child element

# Common Errors
- **Error**: Not checking `event.target` before acting, causing unintended handling of clicks on non-target elements
  **Correction**: Always verify `event.target` matches expected elements

# Common Confusions
- **Confusion**: Event delegation requires special API calls
  **Clarification**: It's a pattern, not a browser API -- just register on a parent and check `target`

# Source Reference
Chapter 15: Handling Events, Section "Propagation", lines 228-248 of 15-handling-events.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clear example and explanation
- Cross-reference status: verified
