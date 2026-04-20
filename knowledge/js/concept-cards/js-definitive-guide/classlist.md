---
concept: classList
slug: classlist
category: browser-apis
subcategory: CSS scripting
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 463
section: "15.3.3 The class attribute"
extraction_confidence: high
aliases:
  - class list
  - DOMTokenList
prerequisites:
  - dom-tree
extends: []
related:
  - element-style-property
contrasts_with: []
answers_questions:
  - "What is the DOM (Document Object Model)?"
---

# Quick Definition

The `classList` property of an Element provides an iterable, set-like interface for adding, removing, checking, and toggling CSS class names on that element, with methods `add()`, `remove()`, `contains()`, and `toggle()`.

# Core Definition

Element objects define a `classList` property that allows treating the HTML `class` attribute as a set of CSS classes rather than a single string. The `classList` value is an iterable Array-like object that behaves like a set of classes, providing `add()`, `remove()`, `contains()`, and `toggle()` methods (Flanagan, Ch. 15, p. 463).

# Prerequisites

- **dom-tree** — Must understand elements and their attributes.

# Key Properties

1. `add(className)` adds a class if not already present.
2. `remove(className)` removes a class.
3. `contains(className)` tests for presence of a class.
4. `toggle(className)` adds if absent, removes if present.
5. The `className` property provides the raw string value of the `class` attribute.

# Construction / Recognition

```javascript
let spinner = document.querySelector("#spinner");
spinner.classList.remove("hidden");
spinner.classList.add("animated");
```

# Context & Application

The simplest way to dynamically change element styling. Adding and removing classes triggers CSS-defined transitions and animations.

# Examples

From the source (p. 463): Showing and hiding a spinner by manipulating classes that control CSS display and animation properties.

# Relationships

## Builds Upon
- **dom-tree** — Manipulates the class attribute of DOM elements

## Enables
- **css-animations-and-events** — Adding/removing classes triggers CSS transitions

## Related
- **element-style-property** — Alternative for per-element styling

## Contrasts With
- (None)

# Common Errors

- **Error**: Using `className` to add a class, which overwrites all existing classes.
  **Correction**: Use `classList.add()` to add without overwriting existing classes.

# Common Confusions

- **Confusion**: `classList` is an Array.
  **Clarification**: It is an Array-like iterable (DOMTokenList), not a true Array.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.3.3, pages 462-463.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clear, concise explanation
- Uncertainties: None
- Cross-reference status: Verified
