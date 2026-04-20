---
# === CORE IDENTIFICATION ===
concept: preventDefault
slug: preventdefault

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
section: "Default actions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - prevent default

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-object
extends: []
related:
  - stoppropagation
contrasts_with:
  - stoppropagation

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I prevent the browser's default behavior for an event?"
---

# Quick Definition
`preventDefault()` is a method on event objects that stops the browser's default behavior for that event, such as following a link or scrolling on key press.

# Core Definition
"For most types of events, the JavaScript event handlers are called *before* the default behavior takes place. If the handler doesn't want this normal behavior to happen, typically because it has already taken care of handling the event, it can call the `preventDefault` method on the event object." (Eloquent JavaScript, Ch. 15, lines 259-263)

# Prerequisites
- **Event object**: `preventDefault` is called on the event object

# Key Properties
1. Stops the browser's default action (following links, scrolling, form submission)
2. Called before the default behavior occurs
3. Does not stop event propagation
4. Some events cannot be intercepted (e.g., closing a tab)
5. Should be used judiciously -- breaking expected behavior frustrates users

# Construction / Recognition
```javascript
let link = document.querySelector("a");
link.addEventListener("click", event => {
  console.log("Nope.");
  event.preventDefault();
});
```
(lines 274-279)

# Context & Application
Used to implement custom keyboard shortcuts, override link navigation, prevent form submission for validation, and implement custom scrolling behavior.

# Examples
From the source: "Try not to do such things without a really good reason. It'll be unpleasant for people who use your page when expected behavior is broken." (lines 283-285)

"Calling `preventDefault` on a scroll event does not prevent the scrolling from happening. In fact, the event handler is called only *after* the scrolling takes place." (lines 651-653)

# Relationships
## Builds Upon
- Event objects
## Enables
- Custom behavior that replaces browser defaults
## Related
- `stopPropagation` (stops propagation, not default action)
## Contrasts With
- `stopPropagation` (which affects handler execution, not browser behavior)

# Common Errors
- **Error**: Using `preventDefault` for scroll events expecting to prevent scrolling
  **Correction**: Scroll event handlers run after scrolling occurs; `preventDefault` has no effect

# Common Confusions
- **Confusion**: `preventDefault` and `stopPropagation` do the same thing
  **Clarification**: `preventDefault` stops default browser behavior; `stopPropagation` stops event propagation to parent handlers

# Source Reference
Chapter 15: Handling Events, Section "Default actions", lines 250-291 of 15-handling-events.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with examples and caveats
- Cross-reference status: verified
