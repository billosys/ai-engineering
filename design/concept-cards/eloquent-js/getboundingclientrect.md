---
# === CORE IDENTIFICATION ===
concept: getBoundingClientRect
slug: getboundingclientrect

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
  - bounding client rect

# === TYPED RELATIONSHIPS ===
prerequisites:
  - layout
  - element-node
extends: []
related:
  - offsetwidth-offsetheight
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I find an element's position on screen?"
---

# Quick Definition
`getBoundingClientRect` returns an object with `top`, `bottom`, `left`, and `right` properties indicating the pixel positions of an element's sides relative to the viewport.

# Core Definition
"The most effective way to find the precise position of an element on the screen is the `getBoundingClientRect` method. It returns an object with `top`, `bottom`, `left`, and `right` properties, indicating the pixel positions of the sides of the element relative to the upper left of the screen." (Eloquent JavaScript, Ch. 14, lines 529-533)

# Prerequisites
- **Layout**: Understanding browser layout computation
- **Element node**: Method available on element nodes

# Key Properties
1. Returns positions relative to the viewport (upper-left corner)
2. For document-relative positions, add `pageXOffset`/`pageYOffset`
3. Forces layout computation if the DOM has changed
4. Returns an object with `top`, `bottom`, `left`, `right` (and `width`, `height`)

# Construction / Recognition
```javascript
let rect = element.getBoundingClientRect();
// rect.top, rect.bottom, rect.left, rect.right
```

# Context & Application
Used for precise element positioning, implementing drag and drop, tooltips, and determining if elements are visible in the viewport.

# Examples
From the source: "If you want pixel positions relative to the whole document, you must add the current scroll position, which you can find in the `pageXOffset` and `pageYOffset` bindings." (lines 534-536)

# Relationships
## Builds Upon
- Browser layout computation
## Enables
- Precise positioning, hit testing, viewport visibility checks
## Related
- `offsetWidth`/`offsetHeight` (size without position)
## Contrasts With
- CSS position properties (which are set values, not computed)

# Common Errors
- **Error**: Assuming returned positions are relative to the document
  **Correction**: They are relative to the viewport; add scroll offsets for document-relative positions

# Common Confusions
- **Confusion**: The returned values are static
  **Clarification**: Each call recomputes based on the current layout state

# Source Reference
Chapter 14: The Document Object Model, Section "Layout", lines 529-536 of 14-the-document-object-model.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined
- Cross-reference status: verified
