---
concept: getBoundingClientRect
slug: getboundingclientrect
category: browser-apis
subcategory: document geometry
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 478
section: "15.5.2 Querying the Geometry of an Element"
extraction_confidence: high
aliases:
  - bounding client rect
  - element geometry
prerequisites:
  - dom-tree
extends: []
related:
  - getcomputedstyle
contrasts_with: []
answers_questions:
  - "What is the DOM (Document Object Model)?"
---

# Quick Definition

`getBoundingClientRect()` returns an object with `left`, `right`, `top`, `bottom`, `width`, and `height` properties that describe an element's size and position in viewport coordinates, including CSS border and padding but not margins.

# Core Definition

You can determine the size and position (in viewport coordinates) of an element by calling its `getBoundingClientRect()` method. It takes no arguments and returns an object with properties `left`, `right`, `top`, `bottom`, `width`, and `height`. The `left` and `top` properties give the x and y coordinates of the upper-left corner, and `right` and `bottom` give the lower-right corner coordinates. Inline elements spanning multiple lines can use `getClientRects()` to get individual rectangles (Flanagan, Ch. 15, pp. 478-479).

# Prerequisites

- **dom-tree** — Must understand elements to query their geometry.

# Key Properties

1. Returns viewport coordinates, not document coordinates.
2. Includes border and padding, but not margins.
3. For inline elements spanning multiple lines, use `getClientRects()` for per-line rectangles.
4. Preferred over querying computed styles for element size and position.

# Construction / Recognition

```javascript
let rect = element.getBoundingClientRect();
console.log(rect.left, rect.top, rect.width, rect.height);
```

# Context & Application

Essential for positioning tooltips, popovers, and other elements relative to their targets. Also used for scroll-based effects and intersection detection.

# Examples

From the source (p. 478-479): Block elements like `<div>` are always rectangular. Inline elements like `<span>` may return a bounding rectangle encompassing multiple lines.

# Relationships

## Builds Upon
- **dom-tree** — Queries geometry of DOM elements

## Enables
- Dynamic positioning of tooltips, menus, and overlays

## Related
- **getcomputedstyle** — Both reveal visual properties; `getBoundingClientRect()` is preferred for geometry

## Contrasts With
- (None)

# Common Errors

- **Error**: Assuming coordinates are document-relative.
  **Correction**: Coordinates are viewport-relative. Add scroll offsets (`window.scrollX`, `window.scrollY`) for document coordinates.

# Common Confusions

- **Confusion**: This method includes margins in the returned size.
  **Clarification**: It includes border and padding but not margins.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.5.2, pages 478-479.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clearly specified properties and behavior
- Uncertainties: None
- Cross-reference status: Verified
