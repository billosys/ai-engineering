---
concept: Element Style Property
slug: element-style-property
category: browser-apis
subcategory: CSS scripting
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 470
section: "15.4.2 Inline Styles"
extraction_confidence: high
aliases:
  - inline styles
  - CSSStyleDeclaration
prerequisites:
  - dom-tree
extends: []
related:
  - classlist
  - getcomputedstyle
contrasts_with:
  - getcomputedstyle
answers_questions:
  - "What is the DOM (Document Object Model)?"
---

# Quick Definition

The `style` property of an Element is a CSSStyleDeclaration object that allows reading and setting inline CSS styles directly in JavaScript, with hyphenated CSS property names converted to camelCase.

# Core Definition

The DOM defines a `style` property on all Element objects. Unlike most properties that mirror HTML attributes as strings, the `style` property is a CSSStyleDeclaration object -- a parsed representation of CSS styles. CSS property names with hyphens are converted to camelCase in JavaScript: `font-size` becomes `fontSize`, `border-left-width` becomes `borderLeftWidth`. All values must be specified as strings, including units (Flanagan, Ch. 15, pp. 470-472).

# Prerequisites

- **dom-tree** — Must understand elements in the DOM.

# Key Properties

1. Values must be strings with proper CSS units (e.g., `"300px"`, not `300`).
2. Hyphenated CSS names map to camelCase: `background-color` to `backgroundColor`.
3. The `cssText` property allows setting all inline styles as a single string.
4. Only represents inline styles, not computed styles from stylesheets.

# Construction / Recognition

```javascript
tooltip.style.display = "block";
tooltip.style.position = "absolute";
tooltip.style.left = `${x}px`;
```

# Context & Application

Used for dynamic positioning (tooltips, modals), animations, and any case where per-element styles must be set programmatically at runtime.

# Examples

From the source (p. 471): A function to position and display a tooltip:
```javascript
function displayAt(tooltip, x, y) {
  tooltip.style.display = "block";
  tooltip.style.position = "absolute";
  tooltip.style.left = `${x}px`;
  tooltip.style.top = `${y}px`;
}
```

# Relationships

## Builds Upon
- **dom-tree** — Accesses style properties of elements

## Enables
- (Dynamic positioning and visual effects)

## Related
- **classlist** — Alternative approach using CSS classes
- **getcomputedstyle** — For reading the final computed styles

## Contrasts With
- **getcomputedstyle** — `style` only reads/writes inline styles; `getComputedStyle()` reads the final computed result of all stylesheets

# Common Errors

- **Error**: Setting a numeric value without units: `e.style.marginLeft = 300`.
  **Correction**: Include units: `e.style.marginLeft = "300px"`.

# Common Confusions

- **Confusion**: Reading `element.style` returns the actual displayed styles.
  **Clarification**: `element.style` only contains inline styles. Use `getComputedStyle()` to see the actual rendered styles.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.4.2, pages 470-472.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Detailed with multiple examples
- Uncertainties: None
- Cross-reference status: Verified
