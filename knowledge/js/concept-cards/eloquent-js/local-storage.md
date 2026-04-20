---
concept: Local Storage
slug: local-storage
category: http-forms
subcategory: browser-api
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "HTTP and Forms"
chapter_number: 18
pdf_page: null
section: "Storing data client-side"
extraction_confidence: high
aliases:
  - localStorage
  - web storage
  - sessionStorage
prerequisites:
  - object
extends: []
related:
  - json-in-http
contrasts_with: []
answers_questions:
  - "How do I store data in the browser between page loads?"
  - "What is localStorage?"
---

# Quick Definition
`localStorage` is a browser API that stores key-value string pairs persistently across page reloads, scoped to the site's domain, accessible via `setItem`, `getItem`, and `removeItem`.

# Core Definition
"The `localStorage` object can be used to store data in a way that survives page reloads. This object allows you to file string values under names" (Ch. 18, "Storing data client-side"). Data persists until explicitly removed or cleared by the user. `sessionStorage` is similar but forgets data when the browser closes.

# Prerequisites
- **Objects**: localStorage has an object-like interface

# Key Properties
1. `localStorage.setItem(key, value)` -- store a value
2. `localStorage.getItem(key)` -- retrieve a value (returns null if missing)
3. `localStorage.removeItem(key)` -- delete a value
4. Values must be strings (use JSON.stringify/parse for objects)
5. Scoped to domain; size-limited by browser

# Construction / Recognition
```javascript
localStorage.setItem("username", "marijn");
console.log(localStorage.getItem("username")); // → marijn
localStorage.removeItem("username");
```

Storing objects:
```javascript
localStorage.setItem("Notes", JSON.stringify(state));
let state = JSON.parse(localStorage.getItem("Notes"));
```

# Context & Application
Used for remembering user preferences, caching data, saving application state in mini-applications. The skill-sharing project (Ch. 21) stores the user name in localStorage.

# Examples
The note-taking application in Ch. 18 persists state:
```javascript
setState(JSON.parse(localStorage.getItem("Notes")) ?? {
  notes: {"shopping list": "Carrots\nRaisins"},
  selected: "shopping list"
});
```

# Relationships
## Builds Upon
- object (key-value interface)
## Enables
- Persistent client-side state, user preferences, offline data
## Related
- json-in-http (JSON.stringify for complex values)
## Contrasts With
- sessionStorage (cleared when browser closes), cookies (sent to server), server-side storage

# Common Errors
- **Error**: Storing objects directly without JSON.stringify
  **Correction**: localStorage only stores strings; serialize with JSON.stringify

# Common Confusions
- **Confusion**: localStorage and sessionStorage are the same
  **Clarification**: localStorage persists indefinitely; sessionStorage is cleared when the browser session ends

# Source Reference
Chapter 18: HTTP and Forms, Section "Storing data client-side", lines 1022-1151 of 18-http-and-forms.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Complete API with practical example
- Cross-reference status: verified (used in Ch. 21)
