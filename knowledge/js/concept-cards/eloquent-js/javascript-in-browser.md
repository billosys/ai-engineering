---
# === CORE IDENTIFICATION ===
concept: JavaScript in the Browser
slug: javascript-in-browser

# === CLASSIFICATION ===
category: web-platform
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "JavaScript and the Browser"
chapter_number: 13
pdf_page: null
section: "HTML and JavaScript"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - client-side JavaScript
  - browser JavaScript

# === TYPED RELATIONSHIPS ===
prerequisites:
  - html
extends: []
related:
  - document-object-model
  - event-handler
  - sandbox
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before working with the DOM?"
---

# Quick Definition
JavaScript runs in the browser via `<script>` tags in HTML documents, executing as the browser parses the page and providing dynamic interactivity.

# Core Definition
"The most important HTML tag is `<script>`, which allows us to include a piece of JavaScript in a document." "Such a script will run as soon as its `<script>` tag is encountered while the browser reads the HTML." Scripts can also be loaded from external files using the `src` attribute. (Eloquent JavaScript, Ch. 13, lines 330-361)

# Prerequisites
- **HTML**: JavaScript is embedded in HTML documents

# Key Properties
1. Scripts run as soon as their `<script>` tag is encountered during parsing
2. External scripts are loaded via `<script src="..."></script>`
3. ES modules can be loaded with `type="module"` attribute
4. Script tags must always be closed with `</script>`
5. Inline event handlers can be placed in HTML attributes like `onclick`
6. JavaScript runs in a sandboxed environment

# Construction / Recognition
```html
<h1>Testing alert</h1>
<script>alert("hello!");</script>
```

External script:
```html
<script src="code/hello.js"></script>
```

# Context & Application
Browser JavaScript is the primary way to add interactivity, dynamic content, and application logic to web pages.

# Examples
From the source:
```html
<button onclick="alert('Boom!');">DO NOT PRESS</button>
```
(lines 383-384)

"You can load ES modules in the browser by giving your script tag a `type=\"module\"` attribute." (lines 370-373)

# Relationships
## Builds Upon
- HTML documents
## Enables
- DOM manipulation, event handling, dynamic web pages
## Related
- DOM (the JavaScript interface to the document)
- Event handlers, sandbox
## Contrasts With
- Server-side JavaScript (Node.js)

# Common Errors
- **Error**: Forgetting to close a `<script>` tag
  **Correction**: "A script tag must always be closed with `</script>`, even if it refers to a script file and doesn't contain any code. If you forget this, the rest of the page will be interpreted as part of the script." (lines 364-367)

# Common Confusions
- **Confusion**: JavaScript and HTML are the same technology
  **Clarification**: HTML is a document format; JavaScript is a programming language that can be embedded in HTML

# Source Reference
Chapter 13: JavaScript and the Browser, Section "HTML and JavaScript", lines 326-390 of 13-javascript-and-the-browser.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly explained
- Cross-reference status: verified
