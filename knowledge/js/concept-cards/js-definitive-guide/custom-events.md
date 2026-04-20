---
concept: Custom Events
slug: custom-events
category: browser-apis
subcategory: events
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 454
section: "15.2.6 Dispatching Custom Events"
extraction_confidence: high
aliases:
  - CustomEvent
  - dispatchEvent
prerequisites:
  - addeventlistener
  - event-object-properties
extends: []
related:
  - event-bubbling-and-capturing
contrasts_with: []
answers_questions:
  - "How does event bubbling relate to event capturing?"
---

# Quick Definition

Custom events allow JavaScript code to define and dispatch its own event types using the `CustomEvent()` constructor and `dispatchEvent()` method, with arbitrary data passed via the `detail` property.

# Core Definition

Any object that has an `addEventListener()` method is an event target and also has a `dispatchEvent()` method. Custom events are created with the `CustomEvent()` constructor, which takes an event type string and an options object. The `detail` property of the options object carries arbitrary data. Setting `bubbles: true` in the options allows the event to propagate up the DOM tree (Flanagan, Ch. 15, pp. 454-455).

# Prerequisites

- **addeventlistener** — Must register handlers to receive custom events.
- **event-object-properties** — Custom events extend the standard event object.

# Key Properties

1. `CustomEvent()` constructor takes a type string and options object.
2. The `detail` property carries custom event data.
3. `bubbles: true` enables DOM propagation.
4. Dispatched synchronously via `dispatchEvent()`.

# Construction / Recognition

```javascript
document.dispatchEvent(new CustomEvent("busy", { detail: true }));
document.addEventListener("busy", (e) => {
  if (e.detail) { showSpinner(); } else { hideSpinner(); }
});
```

# Context & Application

Used to decouple modules: one module dispatches events, another listens for them. Common in web component communication and application-level event buses.

# Examples

From the source (p. 454): A module dispatches a "busy" custom event with `detail: true` before a network operation and `detail: false` after, allowing a UI module to show/hide a spinner without direct coupling.

# Relationships

## Builds Upon
- **addeventlistener** — Listeners handle custom events
- **event-object-properties** — Custom events use the same object model

## Enables
- **web-components-overview** — Web components dispatch custom events

## Related
- **event-bubbling-and-capturing** — Custom events can bubble with `bubbles: true`

## Contrasts With
- (None)

# Common Errors

- **Error**: Forgetting to set `bubbles: true` when the custom event needs to propagate.
  **Correction**: Include `{ bubbles: true }` in the options if ancestor elements need to hear the event.

# Common Confusions

- **Confusion**: Custom events are dispatched asynchronously.
  **Clarification**: `dispatchEvent()` is synchronous; it invokes all handlers before returning.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.2.6, pages 454-455.

# Verification Notes

- Definition source: Direct from source text with code example
- Confidence rationale: Clear example demonstrating the full pattern
- Uncertainties: None
- Cross-reference status: Verified
