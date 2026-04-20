---
# === CORE IDENTIFICATION ===
concept: Layout
slug: layout

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
section: "Layout"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - browser layout
  - reflow

# === TYPED RELATIONSHIPS ===
prerequisites:
  - document-object-model
  - css
extends: []
related:
  - style-property
  - getboundingclientrect
  - offsetwidth-offsetheight
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the browser lay out elements?"
---

# Quick Definition
Layout is the process by which browsers compute the size and position of every element based on its type, content, and CSS styles, then use this information to draw the document.

# Core Definition
"For any given document, browsers are able to compute a layout, which gives each element a size and position based on its type and content. This layout is then used to actually draw the document." Elements are either *block* elements (taking full width, rendered on separate lines) or *inline* elements (rendered within the text flow). (Eloquent JavaScript, Ch. 14, lines 489-492, 481-486)

# Prerequisites
- **DOM**: Understanding the document structure
- **CSS**: Understanding styling properties

# Key Properties
1. Block elements take up full width and render on separate lines (e.g., `<p>`, `<h1>`)
2. Inline elements render within surrounding text (e.g., `<a>`, `<strong>`)
3. Layout is computed lazily -- browsers delay recomputation as long as possible
4. Reading layout properties (like `offsetHeight`) forces a recompute
5. Alternating between DOM changes and layout reads causes costly re-layouts

# Construction / Recognition
Layout is computed automatically by the browser. You observe it through properties like `offsetWidth`, `offsetHeight`, `clientWidth`, `clientHeight`.

# Context & Application
Understanding layout is essential for writing performant web code that avoids unnecessary re-layouts (reflows).

# Examples
From the source, demonstrating the performance cost of forced layouts:
```javascript
// Slow: forces layout on every iteration
time("naive", () => {
  let target = document.getElementById("one");
  while (target.offsetWidth < 2000) {
    target.appendChild(document.createTextNode("X"));
  }
});
// -> naive took 32 ms

// Fast: reads layout only once
time("clever", function() {
  let target = document.getElementById("two");
  target.appendChild(document.createTextNode("XXXXX"));
  let total = Math.ceil(2000 / (target.offsetWidth / 5));
  target.firstChild.nodeValue = "X".repeat(total);
});
// -> clever took 1 ms
```
(lines 568-583)

# Relationships
## Builds Upon
- DOM and CSS
## Enables
- Visual rendering of web pages
## Related
- `offsetWidth`/`offsetHeight`, `getBoundingClientRect`
## Contrasts With
- DOM structure (which is logical, not visual)

# Common Errors
- **Error**: Reading layout properties in a loop that also modifies the DOM
  **Correction**: Batch DOM modifications, then read layout properties once

# Common Confusions
- **Confusion**: Layout happens immediately after every DOM change
  **Clarification**: Browsers defer layout computation; it happens when needed (e.g., when reading layout properties or before screen paint)

# Source Reference
Chapter 14: The Document Object Model, Section "Layout", lines 477-584 of 14-the-document-object-model.md.

# Verification Notes
- Definition source: synthesized from source
- Confidence rationale: Clearly explained with performance example
- Cross-reference status: verified
