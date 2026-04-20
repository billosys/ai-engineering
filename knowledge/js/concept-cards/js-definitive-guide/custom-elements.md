---
concept: Custom Elements
slug: custom-elements
category: browser-apis
subcategory: web components
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 485
section: "15.6.3 Custom Elements"
extraction_confidence: high
aliases:
  - customElements.define
  - autonomous custom elements
prerequisites:
  - web-components-overview
  - dom-tree
extends:
  - web-components-overview
related:
  - shadow-dom
  - html-templates
contrasts_with: []
answers_questions:
  - "What is a Web Component?"
  - "How do I create a custom DOM element (Web Component)?"
---

# Quick Definition

Custom elements associate a JavaScript class (extending HTMLElement) with an HTML tag name via `customElements.define()`, enabling lifecycle callbacks like `connectedCallback()` and `attributeChangedCallback()` that run when the element is used in a document.

# Core Definition

The `customElements.define()` method takes a tag name (with hyphen) as its first argument and a subclass of HTMLElement as its second. The class may define lifecycle methods: `connectedCallback()` (invoked when inserted into the document), `disconnectedCallback()` (when removed), and `attributeChangedCallback(name, oldValue, newValue)` (when observed attributes change). A static `observedAttributes` property lists which attributes trigger the callback (Flanagan, Ch. 15, pp. 485-487).

# Prerequisites

- **web-components-overview** — Must understand the web components concept.
- **dom-tree** — Custom elements are DOM elements.

# Key Properties

1. Class must extend HTMLElement and call `super()` in the constructor.
2. `connectedCallback()` is invoked when the element enters the DOM.
3. `attributeChangedCallback()` only fires for attributes listed in `observedAttributes`.
4. Getter/setter pairs commonly mirror HTML attributes as JavaScript properties.
5. Existing elements are "upgraded" when the component definition loads.

# Construction / Recognition

```javascript
customElements.define("inline-circle", class InlineCircle extends HTMLElement {
  connectedCallback() { /* initialization */ }
  static get observedAttributes() { return ["diameter", "color"]; }
  attributeChangedCallback(name, oldValue, newValue) { /* react to changes */ }
});
```

# Context & Application

The fundamental mechanism for defining new HTML elements. Every web component starts with a custom element definition.

# Examples

From the source (p. 486): The `<inline-circle>` custom element renders as an inline circle with configurable `diameter` and `color` attributes, using `connectedCallback()` to set styles and `attributeChangedCallback()` to respond to attribute changes.

# Relationships

## Builds Upon
- **web-components-overview** — Core mechanism of web components

## Enables
- **shadow-dom** — Custom elements typically attach a shadow root

## Related
- **html-templates** — Templates provide the internal markup structure

## Contrasts With
- (None)

# Common Errors

- **Error**: Not calling `super()` in the constructor.
  **Correction**: The constructor must call `super()` before using `this`.

# Common Confusions

- **Confusion**: You can extend specific element types like HTMLButtonElement.
  **Clarification**: While the spec allows this, Safari does not support it. Always extend HTMLElement for cross-browser compatibility.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.6.3, pages 485-487.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Complete example with lifecycle callbacks
- Uncertainties: None
- Cross-reference status: Verified
