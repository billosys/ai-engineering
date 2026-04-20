---
# === CORE IDENTIFICATION ===
concept: Timer (setTimeout / setInterval)
slug: timer

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
section: "Timers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - setTimeout
  - setInterval
  - clearTimeout
  - clearInterval

# === TYPED RELATIONSHIPS ===
prerequisites:
  - callback
  - event-loop
extends: []
related:
  - debouncing
  - asynchronous-programming
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I schedule code to run later?"
---

# Quick Definition
`setTimeout` schedules a function to run after a delay, while `setInterval` schedules a function to run repeatedly at a given interval. Both return IDs that can be used with `clearTimeout`/`clearInterval` to cancel them.

# Core Definition
"The `setTimeout` function... schedules another function to be called later, after a given number of milliseconds. Sometimes you need to cancel a function you have scheduled. You can do this by storing the value returned by `setTimeout` and calling `clearTimeout` on it." "A similar set of functions, `setInterval` and `clearInterval`, are used to set timers that should repeat every *X* milliseconds." (Eloquent JavaScript, Ch. 15, lines 802-806, 826-828)

# Prerequisites
- **Callbacks**: Timer functions take callback functions
- **Event loop**: Timers are processed by the event loop

# Key Properties
1. `setTimeout(fn, ms)` -- runs `fn` once after `ms` milliseconds
2. `setInterval(fn, ms)` -- runs `fn` repeatedly every `ms` milliseconds
3. Returns an ID for cancellation
4. `clearTimeout(id)` / `clearInterval(id)` to cancel
5. `cancelAnimationFrame` works similarly for `requestAnimationFrame`

# Construction / Recognition
```javascript
let bombTimer = setTimeout(() => {
  console.log("BOOM!");
}, 500);

if (Math.random() < 0.5) {
  console.log("Defused.");
  clearTimeout(bombTimer);
}
```
(lines 809-816)

```javascript
let ticks = 0;
let clock = setInterval(() => {
  console.log("tick", ticks++);
  if (ticks == 10) {
    clearInterval(clock);
    console.log("stop.");
  }
}, 200);
```
(lines 831-838)

# Context & Application
Used for animations, polling, delayed actions, debouncing, and scheduling work.

# Examples
From the source (both examples shown above).

# Relationships
## Builds Upon
- Callbacks and the event loop
## Enables
- Delayed execution, periodic tasks, animations
## Related
- Debouncing (uses setTimeout/clearTimeout)
- `requestAnimationFrame` (for visual animations)
## Contrasts With
- Synchronous code (which runs immediately)

# Common Errors
- **Error**: Forgetting to clear intervals, causing memory leaks
  **Correction**: Always store the interval ID and clear it when no longer needed

# Common Confusions
- **Confusion**: `setTimeout(fn, 0)` runs the callback immediately
  **Clarification**: It runs after the current script finishes and pending events are processed

# Source Reference
Chapter 15: Handling Events, Section "Timers", lines 799-838 of 15-handling-events.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with examples
- Cross-reference status: verified against Ch. 11 usage
