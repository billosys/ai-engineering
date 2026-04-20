---
concept: Event Object Properties
slug: event-object-properties
category: browser-apis
subcategory: events
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 451
section: "15.2.3 Event Handler Invocation"
extraction_confidence: high
aliases:
  - Event object
  - event details
prerequisites:
  - event-types
  - addeventlistener
extends: []
related:
  - event-bubbling-and-capturing
contrasts_with: []
answers_questions:
  - "How does event bubbling relate to event capturing?"
---

# Quick Definition

Event handler functions receive a single Event object argument containing properties like `type`, `target`, `currentTarget`, `timeStamp`, and `isTrusted` that describe the event, with specific event types adding additional properties (e.g., `clientX`/`clientY` for mouse events).

# Core Definition

Event handlers are invoked with an Event object as their single argument. Key properties include: `type` (the event type string), `target` (the object on which the event occurred), `currentTarget` (the object on which the handler was registered), `timeStamp`, and `isTrusted` (true if dispatched by the browser, false if by JavaScript). Specific event types define additional properties, such as `clientX`/`clientY` for mouse events (Flanagan, Ch. 15, pp. 451-452).

# Prerequisites

- **event-types** — Must understand what events are.
- **addeventlistener** — Must register handlers to receive event objects.

# Key Properties

1. `type`: the event type string.
2. `target`: the object where the event originated.
3. `currentTarget`: the object where the current handler is registered.
4. `timeStamp`: when the event occurred (milliseconds).
5. `isTrusted`: whether the browser or JavaScript code dispatched the event.

# Construction / Recognition

```javascript
element.addEventListener("click", (event) => {
  console.log(event.type);    // "click"
  console.log(event.target);  // the clicked element
});
```

# Context & Application

Every event handler uses the event object to determine what happened, where it happened, and to control subsequent behavior (e.g., `preventDefault()`, `stopPropagation()`).

# Examples

From the source (p. 451): Mouse and pointer events have `clientX` and `clientY` properties specifying window coordinates. Keyboard events contain details about the pressed key and modifier keys.

# Relationships

## Builds Upon
- **event-types** — Each event type defines its own properties
- **addeventlistener** — Handlers receive the event object

## Enables
- **event-bubbling-and-capturing** — `target` vs `currentTarget` distinction
- **event-delegation** — Reading `target` to determine which child triggered the event

## Related
- **custom-events** — Custom events use the `detail` property

## Contrasts With
- (None)

# Common Errors

- **Error**: Confusing `target` with `currentTarget` during event bubbling.
  **Correction**: `target` is where the event originated; `currentTarget` is where the handler is registered.

# Common Confusions

- **Confusion**: Arrow function event handlers have `this` set to the event target.
  **Clarification**: Arrow functions retain the `this` of their enclosing scope. Use `event.currentTarget` instead.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.2.3, pages 451-452.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Core properties enumerated clearly
- Uncertainties: None
- Cross-reference status: Verified
