---
# === CORE IDENTIFICATION ===
concept: Throttling
slug: throttling

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
section: "Debouncing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - throttle
  - rate limiting

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-handler
extends: []
related:
  - debouncing
contrasts_with:
  - debouncing

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I handle rapidly firing events efficiently?"
---

# Quick Definition
Throttling ensures that a handler fires at most once per specified time interval during a stream of events, allowing periodic responses during continuous interaction.

# Core Definition
"We can use a slightly different pattern if we want to space responses so that they're separated by at least a certain length of time but want to fire them *during* a series of events, not just afterward." (Eloquent JavaScript, Ch. 15, lines 885-888)

# Prerequisites
- **Event handler**: Understanding event handling

# Key Properties
1. Fires the handler at regular intervals during a stream of events
2. Stores the latest event and processes it when the interval fires
3. Uses a `scheduled` flag or timer to track whether a response is pending
4. Unlike debouncing, does respond during ongoing events

# Construction / Recognition
```javascript
let scheduled = null;
window.addEventListener("mousemove", event => {
  if (!scheduled) {
    setTimeout(() => {
      document.body.textContent =
        `Mouse at ${scheduled.pageX}, ${scheduled.pageY}`;
      scheduled = null;
    }, 250);
  }
  scheduled = event;
});
```
(lines 894-905)

# Context & Application
Used for mouse position tracking, scroll-based animations, and any situation where you want periodic updates during continuous user interaction.

# Examples
From the source: "For example, we might want to respond to `\"mousemove\"` events by showing the current coordinates of the mouse, but only every 250 milliseconds." (lines 889-890)

# Relationships
## Builds Upon
- `setTimeout` and event handlers
## Enables
- Periodic updates during continuous events
## Related
- Debouncing (fires after events stop instead)
## Contrasts With
- Debouncing (which delays until a pause in events)

# Common Errors
- **Error**: Using debouncing when throttling is needed (nothing happens during the event stream)
  **Correction**: Use throttling for real-time feedback during continuous events

# Common Confusions
- **Confusion**: Throttling and debouncing are interchangeable
  **Clarification**: Throttling fires periodically during events; debouncing waits for events to stop

# Source Reference
Chapter 15: Handling Events, Section "Debouncing", lines 884-906 of 15-handling-events.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly shown with code example
- Cross-reference status: verified
