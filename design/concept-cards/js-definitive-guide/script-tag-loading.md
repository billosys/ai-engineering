---
# === CORE IDENTIFICATION ===
concept: Script Tag Loading
slug: script-tag-loading

# === CLASSIFICATION ===
category: browser-apis
subcategory: document-loading
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 426
section: "15.1.1 JavaScript in HTML <script> Tags"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "<script> tag"
  - script element

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - defer-and-async-scripts
  - dom-tree
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the DOM (Document Object Model)?"
---

# Quick Definition

The HTML `<script>` tag is the mechanism by which JavaScript code is included in or referenced from an HTML document, either inline or via the `src` attribute pointing to an external `.js` file.

# Core Definition

Web browsers display HTML documents, and to execute JavaScript code, that code must be included or referenced from an HTML document using the `<script>` tag. A `<script>` tag with a `src` attribute behaves exactly as if the contents of the specified JavaScript file appeared directly between the `<script>` and `</script>` tags (Flanagan, Ch. 15, p. 426).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. JavaScript code can appear inline between `<script>` and `</script>` tags.
2. The `src` attribute specifies the URL of an external JavaScript file.
3. A closing `</script>` tag is always required, even when `src` is specified.
4. The `type="module"` attribute loads the script as an ES6 module.
5. External scripts offer benefits: separation of concerns, caching, and code reuse across pages.

# Construction / Recognition

To include JavaScript in HTML, either embed code directly or reference an external file:
```html
<script src="scripts/app.js"></script>
```

# Context & Application

Every web application begins with a `<script>` tag that loads its JavaScript code. The tag determines when and how scripts execute in relation to HTML parsing.

# Examples

From the source text (p. 428): A digital clock example uses inline JavaScript within a `<script>` tag, calling `document.querySelector("#clock")` to find an element and `setInterval(displayTime, 1000)` to update it every second.

# Relationships

## Builds Upon
- (None - foundational)

## Enables
- **defer-and-async-scripts** — Script loading strategies build on the basic `<script>` mechanism
- **dom-tree** — Scripts interact with the DOM once loaded

## Related
- **dom-tree** — Scripts manipulate the document tree

## Contrasts With
- (None)

# Common Errors

- **Error**: Using a self-closing `<script/>` tag.
  **Correction**: HTML requires both the opening `<script>` and closing `</script>` tags.

# Common Confusions

- **Confusion**: Adding `type="application/javascript"` is necessary.
  **Clarification**: JavaScript is the default language; the `type` attribute is only needed for modules or embedded data.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.1.1, pages 428-430.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Extensively covered with clear examples
- Uncertainties: None
- Cross-reference status: Verified
