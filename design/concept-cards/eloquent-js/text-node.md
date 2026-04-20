---
# === CORE IDENTIFICATION ===
concept: Text Node
slug: text-node

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
section: "Trees"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - DOM text node

# === TYPED RELATIONSHIPS ===
prerequisites:
  - node
extends:
  - node
related:
  - element-node
  - createelement
contrasts_with:
  - element-node

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a text node?"
---

# Quick Definition
A text node represents a section of text in the DOM, with `nodeType` 3 (`Node.TEXT_NODE`). It is a leaf node with no children, and its `nodeValue` property holds the text content.

# Core Definition
"Text nodes, representing a section of text in the document, get code 3 (`Node.TEXT_NODE`)." "The `nodeValue` property of a text node holds the string of text that it represents." (Eloquent JavaScript, Ch. 14, lines 130-131, 243-244)

# Prerequisites
- **Node**: Understanding the base DOM node concept

# Key Properties
1. `nodeType` is 3 (`Node.TEXT_NODE`)
2. Always a leaf node (cannot have children)
3. `nodeValue` holds the text string
4. Created with `document.createTextNode(string)`
5. Whitespace between HTML tags creates text nodes

# Construction / Recognition
```javascript
let text = document.createTextNode("Hello");
```

Text nodes are created for all text content in HTML, including whitespace.

# Context & Application
Text nodes contain all visible text in the document. They are important for searching document content and for programmatically adding text.

# Examples
From the source: "The example document's `<body>` tag has not just three children (`<h1>` and two `<p>` elements), but seven: those three, plus the spaces before, after, and between them." (lines 256-258)

Creating text nodes:
```javascript
let text = document.createTextNode(image.alt);
image.parentNode.replaceChild(text, image);
```
(lines 357-358)

# Relationships
## Builds Upon
- DOM node concept
## Enables
- Text content display in the document
## Related
- `document.createTextNode()` for creation
## Contrasts With
- Element nodes (which define structure and can have children)

# Common Errors
- **Error**: Forgetting that whitespace in HTML source becomes text nodes
  **Correction**: Account for whitespace text nodes when traversing the DOM tree

# Common Confusions
- **Confusion**: Text nodes are the same as the `textContent` property
  **Clarification**: `textContent` is a convenience property on elements; text nodes are actual node objects in the tree

# Source Reference
Chapter 14: The Document Object Model, Sections "Trees" and "Creating nodes", lines 130-131, 243-244, 336-368 of 14-the-document-object-model.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined
- Cross-reference status: verified
