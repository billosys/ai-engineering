---
# === CORE IDENTIFICATION ===
concept: Scroll Event
slug: scroll-event

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
section: "Scroll events"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - scroll handler

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-handler
extends: []
related:
  - debouncing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I detect scrolling?"
---

# Quick Definition
The `"scroll"` event fires whenever an element is scrolled, useful for tracking scroll position, but `preventDefault` cannot prevent scrolling because the handler runs after the scroll occurs.

# Core Definition
"Whenever an element is scrolled, a `\"scroll\"` event is fired on it." "Calling `preventDefault` on a scroll event does not prevent the scrolling from happening. In fact, the event handler is called only *after* the scrolling takes place." (Eloquent JavaScript, Ch. 15, lines 599-600, 651-653)

# Prerequisites
- **Event handler**: Registering scroll handlers

# Key Properties
1. Fires when an element is scrolled
2. Handler runs after scrolling has occurred
3. `preventDefault` has no effect on scrolling
4. `pageYOffset` / `pageXOffset` give current scroll position
5. Can fire rapidly -- consider debouncing

# Construction / Recognition
```javascript
window.addEventListener("scroll", () => {
  let max = document.body.scrollHeight - innerHeight;
  bar.style.width = `${(pageYOffset / max) * 100}%`;
});
```
(lines 626-629)

# Context & Application
Used for scroll-based animations, infinite scrolling, progress indicators, and lazy loading.

# Examples
From the source, a scroll progress bar:
```javascript
let bar = document.querySelector("#progress");
window.addEventListener("scroll", () => {
  let max = document.body.scrollHeight - innerHeight;
  bar.style.width = `${(pageYOffset / max) * 100}%`;
});
```
(lines 625-629)

# Relationships
## Builds Upon
- Event handling system
## Enables
- Scroll-based UI features
## Related
- Debouncing (to limit handler frequency)
## Contrasts With
- Other events where `preventDefault` works

# Common Errors
- **Error**: Trying to prevent scrolling with `preventDefault` on scroll events
  **Correction**: The scroll has already happened; use other techniques to control scrolling

# Common Confusions
- **Confusion**: Scroll events fire before scrolling
  **Clarification**: They fire after the scroll has taken place

# Source Reference
Chapter 15: Handling Events, Section "Scroll events", lines 596-653 of 15-handling-events.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with practical example
- Cross-reference status: verified
