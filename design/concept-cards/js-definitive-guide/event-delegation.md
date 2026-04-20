---
concept: Event Delegation
slug: event-delegation
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
  - delegated event handling
prerequisites:
  - event-bubbling-and-capturing
  - event-object-properties
extends: []
related:
  - addeventlistener
contrasts_with: []
answers_questions:
  - "How does event bubbling relate to event capturing?"
---

# Quick Definition

Event delegation is a pattern where a single event handler is registered on a common ancestor element to handle events from its descendants, leveraging event bubbling and the `event.target` property to determine which child triggered the event.

# Core Definition

Event bubbling provides an alternative to registering handlers on individual document elements. Instead, a single handler on a common ancestor element can handle events from all descendants. For example, registering a "change" handler on a `<form>` element rather than on every individual form element. The `event.target` property identifies the actual element that triggered the event, and `closest()` can be used to find the nearest relevant ancestor (Flanagan, Ch. 15, pp. 452, 457).

# Prerequisites

- **event-bubbling-and-capturing** — Delegation depends on event bubbling.
- **event-object-properties** — Uses `event.target` to identify the source element.

# Key Properties

1. Reduces the number of event listeners in the document.
2. Automatically handles dynamically added child elements.
3. Uses `event.target` to determine which child triggered the event.
4. The `closest()` method finds the nearest matching ancestor of the target.

# Construction / Recognition

```javascript
// Instead of adding a handler to each <li>:
document.querySelector("ul").addEventListener("click", (event) => {
  let li = event.target.closest("li");
  if (li) { /* handle click on this list item */ }
});
```

# Context & Application

Essential for dynamic lists, tables, and any container where children are added/removed at runtime. A core pattern in frameworks and libraries.

# Examples

From the source (p. 457): The `closest()` method is described as useful for event delegation: "If you are handling a 'click' event, for example, you might want to know whether it is a click on a hyperlink. Your event handler could look for the nearest containing hyperlink like this: `let hyperlink = event.target.closest('a[href]');`"

# Relationships

## Builds Upon
- **event-bubbling-and-capturing** — Relies on events bubbling up from descendants
- **event-object-properties** — Uses `target` to identify the source

## Enables
- Efficient handling of dynamic content

## Related
- **addeventlistener** — The mechanism for registering the delegated handler

## Contrasts With
- (None)

# Common Errors

- **Error**: Not checking whether `event.target` or its ancestor matches the expected element.
  **Correction**: Always use `closest()` or a similar check since `target` might be a nested child element.

# Common Confusions

- **Confusion**: Delegation only works with "click" events.
  **Clarification**: Any event that bubbles can be delegated, including "change", "input", "keydown", etc.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Sections 15.2.4 and 15.3.1, pages 452, 457.

# Verification Notes

- Definition source: Synthesized from source discussion of bubbling and closest()
- Confidence rationale: Pattern clearly implied by source; `closest()` example is explicit
- Uncertainties: None
- Cross-reference status: Verified
