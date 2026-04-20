---
concept: getComputedStyle
slug: getcomputedstyle
category: browser-apis
subcategory: CSS scripting
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 472
section: "15.4.3 Computed Styles"
extraction_confidence: high
aliases:
  - computed styles
  - window.getComputedStyle
prerequisites:
  - element-style-property
extends: []
related:
  - getboundingclientrect
contrasts_with:
  - element-style-property
answers_questions:
  - "What is the DOM (Document Object Model)?"
---

# Quick Definition

`window.getComputedStyle()` returns a read-only CSSStyleDeclaration representing the final set of CSS property values the browser actually uses to render an element, including values from all stylesheets.

# Core Definition

The computed style for an element is the set of property values the browser derives from the element's inline style plus all applicable style rules in all stylesheets. The return value of `getComputedStyle()` is a CSSStyleDeclaration object. Unlike inline styles, computed styles are read-only, use absolute values (pixels for sizes, rgb() for colors), and do not support shortcut properties (Flanagan, Ch. 15, pp. 472-474).

# Prerequisites

- **element-style-property** — Must understand inline styles to contrast with computed styles.

# Key Properties

1. Read-only -- cannot be used to set styles.
2. Relative units are converted to absolute values (pixels).
3. Shortcut properties (e.g., `margin`) are not computed; use individual properties (e.g., `marginLeft`).
4. The optional second argument specifies a CSS pseudo-element (e.g., `"::before"`).

# Construction / Recognition

```javascript
let title = document.querySelector("#section1title");
let styles = window.getComputedStyle(title);
let beforeStyles = window.getComputedStyle(title, "::before");
```

# Context & Application

Used when you need to know the actual rendered styles of an element, such as its computed font size, color, or dimensions.

# Examples

From the source (p. 473): Computed style properties return absolute values like pixel measurements and rgb() color strings, unlike the potentially relative values in stylesheets.

# Relationships

## Builds Upon
- **element-style-property** — Extends beyond inline styles to full computed result

## Enables
- **getboundingclientrect** — Both reveal computed visual properties of elements

## Related
- **getboundingclientrect** — Preferred for querying element size and position

## Contrasts With
- **element-style-property** — Inline `style` is writable and only shows inline styles; computed style is read-only and shows final values

# Common Errors

- **Error**: Querying shorthand properties like `margin` from computed styles.
  **Correction**: Query individual properties like `marginLeft`, `marginTop`, etc.

# Common Confusions

- **Confusion**: `getComputedStyle()` returns the same values as `element.style`.
  **Clarification**: `element.style` only contains inline styles. `getComputedStyle()` includes all applicable CSS rules.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.4.3, pages 472-474.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clearly documented with key differences listed
- Uncertainties: None
- Cross-reference status: Verified
