---
concept: addEventListener and removeEventListener
slug: addeventlistener
category: browser-apis
subcategory: events
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 449
section: "15.2.2 addEventListener()"
extraction_confidence: high
aliases:
  - event listener registration
  - addEventListener
  - removeEventListener
prerequisites:
  - event-types
  - dom-tree
extends: []
related:
  - event-object-properties
  - event-bubbling-and-capturing
contrasts_with: []
answers_questions:
  - "How does event bubbling relate to event capturing?"
---

# Quick Definition

`addEventListener()` registers a function to be called when a specified event type occurs on a target object; `removeEventListener()` removes a previously registered handler. Multiple handlers can be registered for the same event type.

# Core Definition

`addEventListener()` takes three arguments: the event type string (without the "on" prefix), the handler function, and an optional third argument (boolean or options object). Unlike setting event handler properties (e.g., `onclick`), `addEventListener()` allows multiple handlers for the same event type, invoked in registration order. The options object supports `capture`, `once`, and `passive` properties (Flanagan, Ch. 15, pp. 449-451).

# Prerequisites

- **event-types** — Must understand event types to register handlers for them.
- **dom-tree** — Must access elements to register handlers on them.

# Key Properties

1. Event type string omits the "on" prefix (e.g., "click" not "onclick").
2. Multiple handlers can be registered; they execute in registration order.
3. The third argument can be `true` (capturing), or an options object with `capture`, `once`, and `passive`.
4. `removeEventListener()` requires the same function reference and capture value.
5. The `passive: true` option indicates the handler will not call `preventDefault()`.

# Construction / Recognition

```javascript
document.addEventListener("click", handleClick, {
  capture: true,
  once: true,
  passive: true
});
document.removeEventListener("mousemove", handleMouseMove);
```

# Context & Application

The standard way to register event handlers in modern JavaScript. Preferred over setting `on*` properties because it supports multiple handlers and provides more options.

# Examples

From the source (p. 449):
```javascript
let b = document.querySelector("#mybutton");
b.onclick = function() { console.log("Thanks for clicking me!"); };
b.addEventListener("click", () => { console.log("Thanks again!"); });
```
Both handlers fire on click, in registration order.

# Relationships

## Builds Upon
- **event-types** — Specifies which events to listen for
- **dom-tree** — Registers handlers on DOM elements

## Enables
- **event-bubbling-and-capturing** — The capture option controls event phase
- **event-delegation** — Registering handlers on ancestor elements

## Related
- **event-object-properties** — Handler receives an event object

## Contrasts With
- (None)

# Common Errors

- **Error**: Trying to remove a handler registered with an anonymous function.
  **Correction**: Store the function reference in a variable so you can pass the same reference to `removeEventListener()`.

# Common Confusions

- **Confusion**: Setting `onclick` and calling `addEventListener("click", ...)` are equivalent.
  **Clarification**: Setting `onclick` can only have one handler; `addEventListener()` allows multiple. Both work, but `addEventListener()` is more flexible.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.2.2, pages 448-451.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Detailed explanation with clear examples
- Uncertainties: None
- Cross-reference status: Verified
