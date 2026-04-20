---
concept: HTML Templates
slug: html-templates
category: browser-apis
subcategory: web components
tier: advanced
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 484
section: "15.6.2 HTML Templates"
extraction_confidence: high
aliases:
  - "<template> tag"
  - HTMLTemplateElement
prerequisites:
  - dom-tree
  - creating-inserting-deleting-nodes
extends: []
related:
  - shadow-dom
  - custom-elements
contrasts_with: []
answers_questions:
  - "What is a Web Component?"
---

# Quick Definition

The HTML `<template>` element holds markup that is never rendered by the browser but can be cloned via JavaScript and inserted into the document efficiently, avoiding repeated HTML parsing.

# Core Definition

A `<template>` tag and its children are never rendered by the browser. In JavaScript, an HTMLTemplateElement has a `content` property that is a DocumentFragment of all child nodes. This DocumentFragment can be cloned with `cloneNode(true)` and inserted into the document. Templates can also be created programmatically in JavaScript and initialized with `innerHTML`, providing a way to parse markup once and clone it many times (Flanagan, Ch. 15, pp. 484-485).

# Prerequisites

- **dom-tree** — Templates create DOM fragments.
- **creating-inserting-deleting-nodes** — Cloned templates are inserted into the DOM.

# Key Properties

1. `<template>` content is not rendered by the browser.
2. The `content` property is a DocumentFragment.
3. `cloneNode(true)` creates a deep clone for insertion.
4. When a DocumentFragment is inserted, only its children are added (not the fragment itself).

# Construction / Recognition

```javascript
let template = document.querySelector("#row");
let clone = template.content.cloneNode(true);
tableBody.append(clone);
```

# Context & Application

Used in web components to define the internal markup structure once and clone it for each instance, avoiding the overhead of re-parsing `innerHTML` for every component instance.

# Examples

From the source (p. 485): A table row template is cloned and populated for each data row, and the `<search-box>` web component creates its template in JavaScript using `innerHTML` on a programmatically created `<template>` element.

# Relationships

## Builds Upon
- **dom-tree** — Templates produce DOM fragments
- **creating-inserting-deleting-nodes** — Cloned content is inserted into the document

## Enables
- **web-components-overview** — Templates provide efficient component markup

## Related
- **shadow-dom** — Template content is typically cloned into a shadow root

## Contrasts With
- (None)

# Common Errors

- **Error**: Expecting template content to be visible in the rendered page.
  **Correction**: `<template>` content is inert and invisible; it must be cloned and inserted programmatically.

# Common Confusions

- **Confusion**: Templates are the same as hidden elements.
  **Clarification**: Template content is not in the document tree at all. Scripts inside templates do not execute, and images do not load.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.6.2, pages 484-485.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clear explanation with practical example
- Uncertainties: None
- Cross-reference status: Verified
