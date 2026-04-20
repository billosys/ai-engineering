---
# === CORE IDENTIFICATION ===
concept: Document Object Model
slug: document-object-model

# === CLASSIFICATION ===
category: dom
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "The Document Object Model"
chapter_number: 14
pdf_page: null
section: "Document structure"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - DOM

# === TYPED RELATIONSHIPS ===
prerequisites:
  - html
  - javascript-in-browser
extends: []
related:
  - document-tree
  - element-node
  - text-node
  - queryselector
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the DOM (Document Object Model)?"
  - "How does the DOM relate to HTML?"
  - "What must I know before working with the DOM?"
---

# Quick Definition
The Document Object Model (DOM) is a live, tree-shaped data structure that represents an HTML document in the browser, allowing JavaScript to read and modify the page.

# Core Definition
"This representation is called the *Document Object Model*, or *DOM* for short." The browser "builds up a model of the document's structure and uses this model to draw the page on the screen." "It is a data structure that you can read or modify. It acts as a *live* data structure: when it's modified, the page on the screen is updated to reflect the changes." (Eloquent JavaScript, Ch. 14, lines 78-79, 35-36, 41-43)

# Prerequisites
- **HTML**: The DOM is the browser's representation of an HTML document
- **JavaScript in the browser**: JavaScript accesses the DOM to manipulate pages

# Key Properties
1. Tree-shaped structure mirroring HTML nesting
2. Live -- modifications are immediately reflected on screen
3. Accessed through the global `document` binding
4. `document.documentElement` refers to the `<html>` element
5. `document.head` and `document.body` point to those sections
6. Designed as a language-neutral interface (not JavaScript-specific)

# Construction / Recognition
The DOM is created automatically by the browser when it parses an HTML document. JavaScript accesses it through the `document` object.

# Context & Application
The DOM is the primary interface for JavaScript to interact with web pages, enabling dynamic content updates, user interaction handling, and single-page applications.

# Examples
From the source: "For each box, there is an object, which we can interact with to find out things such as what HTML tag it represents and which boxes and text it contains." (lines 76-78)

"The global binding `document` gives us access to these objects. Its `documentElement` property refers to the object representing the `<html>` tag." (lines 82-84)

# Relationships
## Builds Upon
- HTML documents (the DOM represents their structure)
## Enables
- Dynamic web page manipulation
- Event handling
- Single-page applications
## Related
- Document tree, element nodes, text nodes
- Query selectors for finding elements
## Contrasts With
- Static HTML text (which is not interactive)

# Common Errors
- **Error**: Assuming the DOM is an exact mirror of the HTML source
  **Correction**: The browser normalizes HTML (adding missing tags, etc.) when building the DOM

# Common Confusions
- **Confusion**: The DOM and HTML are the same thing
  **Clarification**: HTML is a text format; the DOM is the live in-memory object representation the browser creates from it

# Source Reference
Chapter 14: The Document Object Model, Section "Document structure", lines 31-86 of 14-the-document-object-model.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Central topic of the chapter
- Cross-reference status: verified against chapter summary
