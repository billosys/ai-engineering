---
concept: Event Bubbling and Capturing
slug: event-bubbling-and-capturing
category: browser-apis
subcategory: events
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 452
section: "15.2.4 Event Propagation"
extraction_confidence: high
aliases:
  - event propagation
  - event phases
prerequisites:
  - event-types
  - addeventlistener
  - event-object-properties
extends: []
related:
  - event-delegation
contrasts_with: []
answers_questions:
  - "How does event bubbling relate to event capturing?"
---

# Quick Definition

Event propagation occurs in three phases: capturing (from Window down to the target's parent), target (handlers on the target itself), and bubbling (from the target back up to the Window). By default, handlers are registered for the bubbling phase.

# Core Definition

After event handlers on the target element are invoked, most events "bubble" up the DOM tree, invoking handlers on each ancestor up to the Document and then the Window object. Event capturing is the reverse: capturing handlers (registered with `{capture: true}` or `true` as the third argument to `addEventListener()`) are invoked first, from the Window down to the target's parent, before the target phase. The capturing phase is the first phase; target invocation is the second; bubbling is the third (Flanagan, Ch. 15, pp. 452-453).

# Prerequisites

- **event-types** — Must understand events to understand how they propagate.
- **addeventlistener** — The `capture` option controls the phase.
- **event-object-properties** — `target` vs `currentTarget` distinction matters during propagation.

# Key Properties

1. Most events bubble; notable exceptions are "focus", "blur", and "scroll".
2. Capturing handlers are invoked before target and bubbling handlers.
3. `stopPropagation()` stops the event from continuing to propagate.
4. `stopImmediatePropagation()` also prevents other handlers on the same element.
5. The `"load"` event on elements bubbles up to Document but not to Window.

# Construction / Recognition

```javascript
// Register a capturing handler
document.addEventListener("click", handler, true);
// Or with options object
document.addEventListener("click", handler, { capture: true });
```

# Context & Application

Event bubbling enables event delegation (handling events on a parent rather than each child). Event capturing is useful for intercepting events before they reach their targets, such as during drag-and-drop operations.

# Examples

From the source (p. 452): "If the user moves the mouse over a hyperlink, the mousemove event is first fired on the <a> element that defines that link. Then it is fired on the containing elements: perhaps a <p> element, a <section> element, and the Document object itself."

# Relationships

## Builds Upon
- **event-types** — Events propagate based on their type
- **addeventlistener** — The capture option controls which phase

## Enables
- **event-delegation** — Bubbling makes delegation possible

## Related
- **event-object-properties** — `target` identifies the origin; `currentTarget` identifies the handler location

## Contrasts With
- (None - this card describes the contrast between bubbling and capturing)

# Common Errors

- **Error**: Registering a capturing handler with `true` but forgetting to pass `true` to `removeEventListener()`.
  **Correction**: The `capture` value must match when removing: `removeEventListener("click", handler, true)`.

# Common Confusions

- **Confusion**: Capturing and bubbling are alternatives you must choose between.
  **Clarification**: Both phases always occur. By default, handlers are in the bubbling phase. You opt into capturing with the `capture` option.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.2.4, pages 452-453.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Three-phase model clearly explained
- Uncertainties: None
- Cross-reference status: Verified
