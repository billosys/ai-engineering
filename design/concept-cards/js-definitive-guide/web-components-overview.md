---
concept: Web Components
slug: web-components-overview
category: browser-apis
subcategory: web components
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 481
section: "15.6 Web Components"
extraction_confidence: high
aliases:
  - custom elements
  - web component
prerequisites:
  - dom-tree
  - addeventlistener
  - classlist
extends: []
related:
  - custom-elements
  - shadow-dom
  - html-templates
contrasts_with: []
answers_questions:
  - "What is a Web Component?"
  - "How do I create a custom DOM element (Web Component)?"
---

# Quick Definition

Web Components are a browser-native set of technologies (custom elements, Shadow DOM, and HTML templates) that allow developers to create reusable, encapsulated UI components with custom HTML tag names that must contain a hyphen.

# Core Definition

Web Components is a browser-native alternative to frameworks like React and Angular, based on three standards: custom elements (associating a JavaScript class with an HTML tag name), Shadow DOM (encapsulating component internals), and HTML templates (efficient reusable markup). Custom tag names must include a hyphen to avoid conflicts with future HTML elements. Components can have attributes, properties, methods, and slots for composable content (Flanagan, Ch. 15, pp. 481-484).

# Prerequisites

- **dom-tree** — Web components extend the DOM.
- **addeventlistener** — Components use events for communication.
- **classlist** — Components often use CSS classes internally.

# Key Properties

1. Tag names must contain a hyphen (e.g., `<search-box>`).
2. Cannot use self-closing tags; both opening and closing tags required.
3. Slots allow children to be distributed into named positions.
4. Components are registered via `customElements.define()`.
5. Before definition, custom elements appear as generic HTMLElement instances that are later "upgraded".

# Construction / Recognition

```html
<search-box placeholder="Search..."></search-box>
```

# Context & Application

Web Components provide framework-free, browser-native component encapsulation. They are particularly useful for design systems and shared component libraries that need to work across frameworks.

# Examples

From the source (p. 482): A `<search-box>` component displays an input field with magnifying glass and cancel icons, using slots for customizable icons:
```html
<search-box>
  <img src="images/search-icon.png" slot="left"/>
  <img src="images/cancel-icon.png" slot="right"/>
</search-box>
```

# Relationships

## Builds Upon
- **dom-tree** — Extends the DOM with custom elements
- **addeventlistener** — Components dispatch and listen for events

## Enables
- **custom-elements** — The JavaScript class mechanism
- **shadow-dom** — Encapsulation for component internals
- **html-templates** — Efficient markup patterns

## Related
- **custom-events** — Components communicate via custom events

## Contrasts With
- (None)

# Common Errors

- **Error**: Defining a custom element tag name without a hyphen.
  **Correction**: Tag names must include a hyphen (e.g., "my-component", not "mycomponent").

# Common Confusions

- **Confusion**: Web Components replace JavaScript frameworks entirely.
  **Clarification**: Web Components provide low-level building blocks. Frameworks like LitElement build on top of them for productivity.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.6, pages 481-484.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Extensive section with complete example
- Uncertainties: None
- Cross-reference status: Verified
