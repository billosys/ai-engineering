---
# === CORE IDENTIFICATION ===
concept: querySelector
slug: queryselector

# === CLASSIFICATION ===
category: dom
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "The Document Object Model"
chapter_number: 14
pdf_page: null
section: "Query selectors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - document.querySelector

# === TYPED RELATIONSHIPS ===
prerequisites:
  - document-object-model
  - css
extends: []
related:
  - queryselectorall
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I find elements in the DOM?"
---

# Quick Definition
`querySelector` is a method on `document` and element nodes that returns the first element matching a CSS selector string, or `null` if no element matches.

# Core Definition
"The `querySelector` method (without the `All` part) works in a similar way. This one is useful if you want a specific single element. It will return only the first matching element, or `null` when no element matches." (Eloquent JavaScript, Ch. 14, lines 786-789)

# Prerequisites
- **DOM**: Understanding the document object model
- **CSS selectors**: Basic knowledge of selector syntax (tag names, classes, IDs)

# Key Properties
1. Takes a CSS selector string as argument
2. Returns the first matching element or `null`
3. Available on both `document` and element nodes
4. Uses the same selector syntax as CSS
5. More flexible than `getElementById` or `getElementsByTagName`

# Construction / Recognition
```javascript
let button = document.querySelector("button");
let para = document.querySelector("p");
let link = document.querySelector("a");
```

# Context & Application
`querySelector` is the most common way to find specific elements in the DOM, especially when you need a single element.

# Examples
From Ch. 15, used extensively:
```javascript
let button = document.querySelector("button");
button.addEventListener("click", () => {
  console.log("Button clicked.");
});
```

# Relationships
## Builds Upon
- DOM and CSS selector syntax
## Enables
- Finding specific elements for manipulation
## Related
- `querySelectorAll` (returns all matches)
## Contrasts With
- `getElementById` (finds by ID only)
- `getElementsByTagName` (finds by tag name, returns live collection)

# Common Errors
- **Error**: Expecting `querySelector` to return all matching elements
  **Correction**: Use `querySelectorAll` to get all matches

# Common Confusions
- **Confusion**: `querySelector` returns a live collection
  **Clarification**: `querySelector` returns a single element (or null); `querySelectorAll` returns a static NodeList

# Source Reference
Chapter 14: The Document Object Model, Section "Query selectors", lines 786-789 of 14-the-document-object-model.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined
- Cross-reference status: verified against Ch. 15 usage
