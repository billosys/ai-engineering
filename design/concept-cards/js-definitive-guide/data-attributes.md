---
concept: Data Attributes
slug: data-attributes
category: browser-apis
subcategory: DOM
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 463
section: "15.3.3 Dataset attributes"
extraction_confidence: high
aliases:
  - dataset
  - "data-* attributes"
  - custom data attributes
prerequisites:
  - dom-tree
extends: []
related:
  - element-selection-queryselector
contrasts_with: []
answers_questions:
  - "What is the DOM (Document Object Model)?"
---

# Quick Definition

HTML data attributes (`data-*`) attach custom data to elements; in JavaScript, they are accessed via the `dataset` property, which maps `data-section-number` to `dataset.sectionNumber` using camelCase conversion.

# Core Definition

Any attribute whose name is lowercase and begins with the prefix "data-" is considered valid HTML and can be used for any purpose without affecting presentation. In the DOM, Element objects have a `dataset` property that refers to an object whose properties correspond to the data- attributes with their prefix removed. Hyphenated attribute names map to camelCase property names (Flanagan, Ch. 15, p. 463).

# Prerequisites

- **dom-tree** — Must understand element attributes in the DOM.

# Key Properties

1. `data-*` attributes do not affect the visual presentation of elements.
2. The `dataset` property provides a DOMStringMap object.
3. Hyphenated names are converted to camelCase: `data-section-number` becomes `dataset.sectionNumber`.

# Construction / Recognition

```html
<h2 id="title" data-section-number="16.1">Attributes</h2>
```
```javascript
let number = document.querySelector("#title").dataset.sectionNumber;
```

# Context & Application

Used to embed application-specific data in HTML elements that JavaScript can later read and act upon, without resorting to non-standard attributes.

# Examples

From the source (p. 463): Given `<h2 id="title" data-section-number="16.1">Attributes</h2>`, JavaScript accesses the value as `dataset.sectionNumber`.

# Relationships

## Builds Upon
- **dom-tree** — Extends the attribute system of DOM elements

## Enables
- **event-delegation** — Data attributes are commonly used to store information read by delegated event handlers

## Related
- **element-selection-queryselector** — Can select elements by data attributes using CSS selectors

## Contrasts With
- (None)

# Common Errors

- **Error**: Forgetting the camelCase conversion when accessing hyphenated data attributes.
  **Correction**: `data-my-value` becomes `dataset.myValue`, not `dataset["my-value"]`.

# Common Confusions

- **Confusion**: Data attributes are only for CSS styling.
  **Clarification**: Data attributes are specifically designed for JavaScript use and do not affect presentation.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.3.3, pages 463-464.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Concise, clear explanation with example
- Uncertainties: None
- Cross-reference status: Verified
