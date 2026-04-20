---
# === CORE IDENTIFICATION ===
concept: Debouncing
slug: debouncing

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
  - debounce

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-handler
extends: []
related:
  - throttling
  - scroll-event
contrasts_with:
  - throttling

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I handle rapidly firing events efficiently?"
---

# Quick Definition
Debouncing is a technique that delays executing a handler until a pause in rapid events occurs, preventing expensive operations from running on every single event.

# Core Definition
"If you do need to do something nontrivial in such a handler, you can use `setTimeout` to make sure you are not doing it too often. This is usually called *debouncing* the event." The approach: "Instead of immediately performing an action in the event handler, we set a timeout. We also clear the previous timeout (if any) so that when events occur close together (closer than our timeout delay), the timeout from the previous event will be canceled." (Eloquent JavaScript, Ch. 15, lines 851-864)

# Prerequisites
- **Event handler**: Understanding event handling and rapid-fire events

# Key Properties
1. Uses `setTimeout` and `clearTimeout` to delay execution
2. Each new event resets the delay timer
3. Handler only runs after events stop for the specified duration
4. Useful for events that fire many times per second (scroll, mousemove, input)

# Construction / Recognition
```javascript
let textarea = document.querySelector("textarea");
let timeout;
textarea.addEventListener("input", () => {
  clearTimeout(timeout);
  timeout = setTimeout(() => console.log("Typed!"), 500);
});
```
(lines 869-874)

# Context & Application
Used for search-as-you-type, auto-save, window resize handlers, and any situation where responding to every individual event would be wasteful.

# Examples
From the source: "Suppose we want to react when the user has typed something, but we don't want to do it immediately for every input event. When they are typing quickly, we just want to wait until a pause occurs." (lines 857-860)

"Giving an undefined value to `clearTimeout` or calling it on a timeout that has already fired has no effect. Thus, we don't have to be careful about when to call it." (lines 879-881)

# Relationships
## Builds Upon
- `setTimeout` and `clearTimeout`
## Enables
- Efficient handling of high-frequency events
## Related
- Throttling (similar concept but fires during events, not after)
## Contrasts With
- Throttling (which fires at regular intervals during a stream of events)

# Common Errors
- **Error**: Not clearing the previous timeout, causing multiple delayed executions
  **Correction**: Always `clearTimeout` before setting a new one

# Common Confusions
- **Confusion**: Debouncing and throttling are the same
  **Clarification**: Debouncing waits until events stop; throttling fires at regular intervals during events

# Source Reference
Chapter 15: Handling Events, Section "Debouncing", lines 841-906 of 15-handling-events.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with example
- Cross-reference status: verified
