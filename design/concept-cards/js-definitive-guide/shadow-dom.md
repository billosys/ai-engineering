---
concept: Shadow DOM
slug: shadow-dom
category: browser-apis
subcategory: web components
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 487
section: "15.6.4 Shadow DOM"
extraction_confidence: high
aliases:
  - shadow root
  - shadow tree
prerequisites:
  - custom-elements
extends:
  - web-components-overview
related:
  - html-templates
contrasts_with: []
answers_questions:
  - "What is a Web Component?"
  - "How do I create a custom DOM element (Web Component)?"
---

# Quick Definition

Shadow DOM provides encapsulation for web components by creating a private DOM tree (the "shadow root") attached to an element, whose internal elements are hidden from external JavaScript queries and whose styles are isolated from the main document.

# Core Definition

Shadow DOM allows a "shadow root" to be attached to a custom element (the "shadow host") via `attachShadow({mode: "open"})`. The shadow root is a DocumentFragment that serves as the root of a private tree. Three key encapsulations: (1) shadow elements are hidden from `querySelector()` on the main document, (2) styles defined in the shadow tree are private and do not affect the light DOM (and vice versa), and (3) events originating in the shadow DOM have their `target` changed to the shadow host when they cross the boundary (Flanagan, Ch. 15, pp. 487-491).

# Prerequisites

- **custom-elements** — Shadow DOM is attached to custom elements.

# Key Properties

1. Created with `element.attachShadow({mode: "open"})`.
2. Open mode: shadow root accessible via `element.shadowRoot`. Closed mode: inaccessible.
3. CSS scoping is the most important feature: styles are isolated.
4. `<slot>` elements distribute light DOM children into the shadow tree.
5. Named slots allow multiple distribution points via the `slot` attribute on children.

# Construction / Recognition

```javascript
this.attachShadow({mode: "open"});
this.shadowRoot.innerHTML = `<style>:host { display: block; }</style><slot></slot>`;
```

# Context & Application

Essential for creating truly encapsulated components whose styles and internal structure cannot be accidentally broken by external CSS or scripts.

# Examples

From the source (p. 491): The `<search-box>` example uses Shadow DOM with named slots for left and right icons, scoped CSS using the `:host` selector, and internal `<input>` styling isolated from the document.

# Relationships

## Builds Upon
- **custom-elements** — Shadow DOM is attached to custom elements

## Enables
- Complete style encapsulation for web components

## Related
- **html-templates** — Templates provide the initial shadow DOM content

## Contrasts With
- (None)

# Common Errors

- **Error**: Trying to style shadow DOM internals from external stylesheets.
  **Correction**: Shadow DOM styles are encapsulated. Use CSS custom properties (variables) to allow controlled customization.

# Common Confusions

- **Confusion**: Light DOM children disappear when shadow DOM is attached.
  **Clarification**: Light DOM children are only displayed if the shadow DOM contains a `<slot>` element for them.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.6.4, pages 487-491.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Detailed explanation of all three encapsulation types
- Uncertainties: None
- Cross-reference status: Verified
