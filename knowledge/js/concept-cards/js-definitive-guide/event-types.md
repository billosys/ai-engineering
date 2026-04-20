---
concept: Event Types
slug: event-types
category: browser-apis
subcategory: events
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 444
section: "15.2 Events"
extraction_confidence: high
aliases:
  - browser events
  - DOM events
prerequisites: []
extends: []
related:
  - addeventlistener
  - event-object-properties
  - event-bubbling-and-capturing
contrasts_with: []
answers_questions:
  - "How does event bubbling relate to event capturing?"
---

# Quick Definition

Browser events are typed notifications (like "click", "load", "keydown") triggered on specific targets (elements, windows, documents) that JavaScript programs can respond to by registering handler functions.

# Core Definition

In client-side JavaScript, events occur on any element within an HTML document. Key concepts include the event type (a string like "mousemove" or "keydown"), the event target (the object on which the event occurred), and the event handler (a function registered to respond). Events are categorized as device-dependent input events, device-independent input events, user interface events, state-change events, and API-specific events (Flanagan, Ch. 15, pp. 443-447).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Event type is a string (e.g., "click", "keydown", "load").
2. Event target is typically a Window, Document, or Element object.
3. Events can propagate (bubble) up the DOM tree.
4. Some events have default actions that can be prevented.
5. Categories include device-dependent, device-independent, UI, state-change, and API-specific events.

# Construction / Recognition

Events are identified by their type string. Common types: "click", "mousedown", "keydown", "load", "DOMContentLoaded", "focus", "submit", "change".

# Context & Application

Events are the fundamental mechanism for making web pages interactive. The event-driven programming model defines the second phase of JavaScript program execution.

# Examples

From the source (p. 444-447): "mousemove" indicates the user moved the mouse; "keydown" means a key was pressed; "load" means a resource finished loading. The "DOMContentLoaded" and "load" events mark the transition to the event-driven phase of execution.

# Relationships

## Builds Upon
- (None - foundational)

## Enables
- **addeventlistener** — Registration of event handlers
- **event-object-properties** — Event details passed to handlers
- **event-bubbling-and-capturing** — How events propagate

## Related
- **custom-events** — User-defined event types

## Contrasts With
- (None)

# Common Errors

- **Error**: Using uppercase event names (e.g., "Click" instead of "click").
  **Correction**: Event type strings are case-sensitive and typically lowercase.

# Common Confusions

- **Confusion**: All events bubble up the DOM tree.
  **Clarification**: Most events bubble, but notable exceptions include "focus", "blur", and "scroll".

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.2, pages 443-447.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Comprehensive taxonomy from source
- Uncertainties: None
- Cross-reference status: Verified
