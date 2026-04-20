---
# === CORE IDENTIFICATION ===
concept: offsetWidth / offsetHeight
slug: offsetwidth-offsetheight

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
  - offsetWidth
  - offsetHeight
  - clientWidth
  - clientHeight

# === TYPED RELATIONSHIPS ===
prerequisites:
  - layout
  - element-node
extends: []
related:
  - getboundingclientrect
  - style-property
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I get an element's size?"
---

# Quick Definition
`offsetWidth` and `offsetHeight` give the total space an element occupies in pixels (including borders), while `clientWidth` and `clientHeight` give the inner size (excluding borders).

# Core Definition
"The `offsetWidth` and `offsetHeight` properties give you the space the element takes up in *pixels*." "Similarly, `clientWidth` and `clientHeight` give you the size of the space *inside* the element, ignoring border width." (Eloquent JavaScript, Ch. 14, lines 496-497, 504-506)

# Prerequisites
- **Layout**: Understanding how browsers compute element sizes
- **Element node**: These are properties of element nodes

# Key Properties
1. `offsetWidth`/`offsetHeight`: total space including borders
2. `clientWidth`/`clientHeight`: inner space excluding borders
3. Values are in pixels
4. Reading these properties forces a layout computation if the DOM has changed

# Construction / Recognition
```javascript
let para = document.body.getElementsByTagName("p")[0];
console.log("clientHeight:", para.clientHeight);
// -> 19
console.log("offsetHeight:", para.offsetHeight);
// -> 25
```
(lines 514-519)

# Context & Application
Used for measuring element dimensions for layout calculations, animations, and responsive behavior.

# Examples
From the source, a `<p>` element with a 3px border:
- `clientHeight: 19` (content only)
- `offsetHeight: 25` (content + 2 x 3px border)
(lines 514-519)

# Relationships
## Builds Upon
- Browser layout computation
## Enables
- Size-dependent calculations and responsive layouts
## Related
- `getBoundingClientRect` (for position as well as size)
## Contrasts With
- CSS width/height properties (which are set values, not computed values)

# Common Errors
- **Error**: Reading these properties repeatedly in a loop that modifies the DOM
  **Correction**: This forces expensive layout recomputations; batch reads and writes separately

# Common Confusions
- **Confusion**: `offsetWidth` equals the CSS `width` property
  **Clarification**: `offsetWidth` includes padding, borders, and scrollbars in addition to CSS width

# Source Reference
Chapter 14: The Document Object Model, Section "Layout", lines 495-520 of 14-the-document-object-model.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with example
- Cross-reference status: verified
