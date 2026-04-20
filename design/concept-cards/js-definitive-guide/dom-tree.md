---
concept: Document Object Model (DOM) Tree
slug: dom-tree
category: browser-apis
subcategory: DOM
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 432
section: "15.1.2 The Document Object Model"
extraction_confidence: high
aliases:
  - DOM
  - DOM tree
  - Document Object Model
prerequisites: []
extends: []
related:
  - element-selection-queryselector
  - dom-traversal
  - creating-inserting-deleting-nodes
contrasts_with: []
answers_questions:
  - "What is the DOM (Document Object Model)?"
---

# Quick Definition

The Document Object Model (DOM) is a tree-structured representation of an HTML document where each HTML tag corresponds to a JavaScript Element object and each run of text to a Text object, all descending from the Document object.

# Core Definition

The DOM API mirrors the tree structure of an HTML document. For each HTML tag in the document, there is a corresponding JavaScript Element object, and for each run of text, a corresponding Text object. The Element and Text classes, as well as the Document class itself, are all subclasses of the more general Node class, and Node objects are organized into a tree structure that JavaScript can query and traverse using the DOM API (Flanagan, Ch. 15, p. 433).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The tree uses parent-child-sibling terminology borrowed from family trees.
2. There is a JavaScript class corresponding to each HTML tag type (e.g., HTMLBodyElement, HTMLTableElement).
3. JavaScript element objects have properties corresponding to their HTML attributes.
4. The Document object represents the entire HTML document and is the root of the tree.
5. The DOM API includes methods for creating, inserting, moving, and removing nodes.

# Construction / Recognition

The DOM is automatically created by the browser when it parses an HTML document. Access it via the global `document` object.

# Context & Application

The DOM is the central API for client-side JavaScript. All document manipulation goes through the DOM.

# Examples

From the source (p. 433): A simple HTML document with `<html>`, `<head>`, `<body>`, `<h1>`, `<p>`, and `<i>` tags is represented as a tree where the `<html>` element contains `<head>` and `<body>` children, with text and element nodes beneath them.

# Relationships

## Builds Upon
- (None - foundational)

## Enables
- **element-selection-queryselector** — Selecting elements from the DOM tree
- **dom-traversal** — Walking the tree structure
- **creating-inserting-deleting-nodes** — Modifying the tree

## Related
- **innerhtml-vs-textcontent** — Different ways to read/write DOM content

## Contrasts With
- (None)

# Common Errors

- **Error**: Assuming the DOM tree only contains Element nodes.
  **Correction**: The DOM tree also contains Text nodes (for text content) and Comment nodes.

# Common Confusions

- **Confusion**: The DOM is the same as the HTML source code.
  **Clarification**: The DOM is a live, in-memory representation that scripts can modify independently of the source HTML.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.1.2, pages 432-434.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Core concept, thoroughly explained
- Uncertainties: None
- Cross-reference status: Verified
