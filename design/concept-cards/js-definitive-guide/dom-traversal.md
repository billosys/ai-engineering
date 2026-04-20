---
concept: DOM Traversal
slug: dom-traversal
category: browser-apis
subcategory: DOM
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 459
section: "15.3.2 Document Structure and Traversal"
extraction_confidence: high
aliases:
  - DOM navigation
  - tree traversal
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

DOM traversal is the process of navigating between related nodes in the document tree using properties like `parentNode`, `children`, `firstElementChild`, `nextElementSibling`, and their Node-level equivalents.

# Core Definition

The DOM provides two traversal APIs. The Element-based API (`children`, `firstElementChild`, `lastElementChild`, `nextElementSibling`, `previousElementSibling`, `parentNode`) treats the document as a tree of Element objects, ignoring Text nodes. The Node-based API (`childNodes`, `firstChild`, `lastChild`, `nextSibling`, `previousSibling`) includes all node types including Text and Comment nodes (Flanagan, Ch. 15, pp. 459-461).

# Prerequisites

- **dom-tree** — Must understand the tree structure to traverse it.

# Key Properties

1. `parentNode` refers to the parent Element or Document.
2. `children` is a NodeList of Element children only (no Text nodes).
3. `childElementCount` returns the number of Element children.
4. `firstElementChild` / `lastElementChild` return null if no Element children.
5. The Node-based API (`childNodes`, `firstChild`, etc.) includes Text and Comment nodes.

# Construction / Recognition

```javascript
document.children[0].children[1] // The <body> element
document.firstElementChild.firstElementChild.nextElementSibling
```

# Context & Application

Used when you need to navigate relative to a known element, such as finding a parent container, iterating over children, or accessing siblings.

# Examples

From the source (p. 460): A recursive depth-first traversal function:
```javascript
function traverse(e, f) {
  f(e);
  for(let child of e.children) {
    traverse(child, f);
  }
}
```

# Relationships

## Builds Upon
- **dom-tree** — Navigates the tree structure

## Enables
- **creating-inserting-deleting-nodes** — Traversal helps locate insertion points

## Related
- **element-selection-queryselector** — Alternative to traversal for finding elements

## Contrasts With
- (None)

# Common Errors

- **Error**: Using the Node-based API (`firstChild`) when you want Element children, and getting unexpected Text nodes (whitespace).
  **Correction**: Use the Element-based API (`firstElementChild`) to skip Text nodes.

# Common Confusions

- **Confusion**: `children` and `childNodes` return the same thing.
  **Clarification**: `children` returns only Element children; `childNodes` includes Text and Comment nodes.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.3.2, pages 459-461.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Two distinct APIs clearly explained
- Uncertainties: None
- Cross-reference status: Verified
