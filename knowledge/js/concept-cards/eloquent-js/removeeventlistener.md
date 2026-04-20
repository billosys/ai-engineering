---
# === CORE IDENTIFICATION ===
concept: removeEventListener
slug: removeeventlistener

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
section: "Events and DOM nodes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - remove event listener

# === TYPED RELATIONSHIPS ===
prerequisites:
  - addeventlistener
extends: []
related:
  - event-handler
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I remove an event listener?"
---

# Quick Definition
`removeEventListener` unregisters a previously registered event handler, requiring the same function reference that was passed to `addEventListener`.

# Core Definition
"The `removeEventListener` method, called with arguments similar to `addEventListener`, removes a handler." "The function given to `removeEventListener` has to be the same function value given to `addEventListener`." (Eloquent JavaScript, Ch. 15, lines 121-122, 137-139)

# Prerequisites
- **addEventListener**: Must have registered a handler first

# Key Properties
1. Requires the exact same function reference used in `addEventListener`
2. Anonymous functions cannot be removed (no reference to pass)
3. Named functions must be used when removal is needed

# Construction / Recognition
```javascript
let button = document.querySelector("button");
function once() {
  console.log("Done.");
  button.removeEventListener("click", once);
}
button.addEventListener("click", once);
```
(lines 127-133)

# Context & Application
Used to clean up event handlers when they are no longer needed, such as one-time handlers or when UI components are destroyed.

# Examples
From the source: "When you need to unregister a handler, you'll want to give the handler function a name (`once`, in the example) to be able to pass the same function value to both methods." (lines 139-141)

# Relationships
## Builds Upon
- `addEventListener`
## Enables
- One-time handlers, cleanup, preventing memory leaks
## Related
- Event handler lifecycle
## Contrasts With
- `addEventListener` (adds rather than removes)

# Common Errors
- **Error**: Passing a different function reference (e.g., a new anonymous function)
  **Correction**: Store the handler in a variable or give it a name so the same reference can be passed

# Common Confusions
- **Confusion**: `removeEventListener` can remove anonymous functions
  **Clarification**: Without a reference to the exact same function object, it cannot be removed

# Source Reference
Chapter 15: Handling Events, Section "Events and DOM nodes", lines 120-141 of 15-handling-events.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with example
- Cross-reference status: verified
