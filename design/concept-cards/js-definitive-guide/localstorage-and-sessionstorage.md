---
concept: localStorage and sessionStorage
slug: localstorage-and-sessionstorage
category: browser-apis
subcategory: storage
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 554
section: "15.12.1 localStorage and sessionStorage"
extraction_confidence: high
aliases:
  - Web Storage API
  - Storage objects
prerequisites: []
extends: []
related:
  - cookies
  - indexeddb
contrasts_with: []
answers_questions:
  - "How do localStorage and sessionStorage differ?"
---

# Quick Definition

`localStorage` and `sessionStorage` are Storage objects that persist string key-value pairs: `localStorage` data survives browser restarts and is scoped to the document origin, while `sessionStorage` data is scoped to the browser tab and cleared when the tab closes.

# Core Definition

The `localStorage` and `sessionStorage` properties of Window refer to Storage objects that map string keys to string values. `localStorage` data is permanent (persists until explicitly deleted), scoped to the document origin (protocol + hostname + port). `sessionStorage` data has the lifetime of the browser tab and is scoped to both origin and window -- two tabs from the same origin have separate `sessionStorage`. Both support `getItem()`, `setItem()`, `deleteItem()`, `clear()`, and direct property access. Changes to `localStorage` trigger "storage" events on other windows of the same origin (Flanagan, Ch. 15, pp. 554-556).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Values must be strings; use `JSON.stringify()`/`JSON.parse()` for other types.
2. `localStorage` persists across browser restarts; `sessionStorage` does not.
3. Both are scoped to document origin (protocol + hostname + port).
4. `sessionStorage` is additionally scoped per-tab.
5. `localStorage` changes fire "storage" events on other same-origin windows.

# Construction / Recognition

```javascript
localStorage.username = "David";
let name = localStorage.username;
localStorage.clear();
```

# Context & Application

Use `localStorage` for user preferences and persistent state. Use `sessionStorage` for temporary per-tab state that should not survive tab closure.

# Examples

From the source (p. 554):
```javascript
let name = localStorage.username;
if (!name) {
  name = prompt("What is your name?");
  localStorage.username = name;
}
```

# Relationships

## Builds Upon
- (None - foundational)

## Enables
- Client-side state persistence
- Cross-tab communication via "storage" events

## Related
- **cookies** — Older storage mechanism
- **indexeddb** — More powerful structured storage

## Contrasts With
- (This card describes the contrast between localStorage and sessionStorage)

# Common Errors

- **Error**: Storing a number and expecting to get a number back.
  **Correction**: All values are stored as strings. Use `parseInt()` or `JSON.parse()` when retrieving.

# Common Confusions

- **Confusion**: `sessionStorage` is shared between tabs of the same origin.
  **Clarification**: Each tab has its own separate `sessionStorage`. Only `localStorage` is shared.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.12.1, pages 554-556.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clear distinction with detailed scoping rules
- Uncertainties: None
- Cross-reference status: Verified
