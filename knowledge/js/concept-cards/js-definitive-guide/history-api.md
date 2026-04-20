---
concept: History API (pushState/popstate)
slug: history-api
category: browser-apis
subcategory: navigation
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 530
section: "15.10.4 History Management with pushState()"
extraction_confidence: high
aliases:
  - pushState
  - popstate event
  - History object
prerequisites:
  - addeventlistener
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What is the DOM (Document Object Model)?"
---

# Quick Definition

`history.pushState()` adds an entry (with a serialized state object and optional URL) to the browser's history without loading a new page, and the "popstate" event fires with a copy of the saved state when the user navigates with Back/Forward buttons.

# Core Definition

The `history.pushState(stateObject, title, url)` method saves a structured-cloned state object to the browser's history and optionally updates the displayed URL without triggering a page load. When the user navigates Back or Forward, the browser fires a "popstate" event on the Window object with a `state` property containing a clone of the saved state object. `history.replaceState()` updates the current entry instead of adding a new one (Flanagan, Ch. 15, pp. 530-534).

# Prerequisites

- **addeventlistener** — Must register "popstate" event handlers.

# Key Properties

1. First argument is a state object (serialized via structured clone algorithm).
2. Second argument is a title (mostly ignored by browsers; pass empty string).
3. Third argument is an optional URL displayed in the location bar.
4. "popstate" event fires on Back/Forward navigation with the saved state.
5. `replaceState()` modifies the current history entry.

# Construction / Recognition

```javascript
history.pushState(gameState, "", gameState.toURL());
window.addEventListener("popstate", (event) => {
  if (event.state) { restoreState(event.state); }
});
```

# Context & Application

Essential for single-page applications (SPAs) that need to support browser Back/Forward navigation without full page reloads.

# Examples

From the source (p. 531-534): A number-guessing game uses `pushState()` to save each guess to history, allowing the user to "go back" to review previous guesses.

# Relationships

## Builds Upon
- **addeventlistener** — Listening for "popstate" events

## Enables
- Single-page application navigation
- Bookmarkable application states

## Related
- (None)

## Contrasts With
- (None)

# Common Errors

- **Error**: Expecting "popstate" to fire when `pushState()` is called.
  **Correction**: "popstate" only fires on Back/Forward navigation, not on `pushState()` calls.

# Common Confusions

- **Confusion**: `pushState()` loads a new page from the server.
  **Clarification**: `pushState()` only updates the URL and history; it does not trigger a page load or network request.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.10.4, pages 530-534.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Complete example with game application
- Uncertainties: None
- Cross-reference status: Verified
