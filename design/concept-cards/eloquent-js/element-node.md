---
# === CORE IDENTIFICATION ===
concept: Element Node
slug: element-node

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
  - DOM element
  - element

# === TYPED RELATIONSHIPS ===
prerequisites:
  - node
extends:
  - node
related:
  - text-node
  - html-attributes
  - queryselector
contrasts_with:
  - text-node

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the DOM (Document Object Model)?"
---

# Quick Definition
An element node represents an HTML tag in the DOM tree, with `nodeType` 1 (`Node.ELEMENT_NODE`), and determines the document's structure by containing child nodes.

# Core Definition
"Nodes for *elements*, which represent HTML tags, determine the structure of the document. These can have child nodes. An example of such a node is `document.body`. Some of these children can be leaf nodes, such as pieces of text or comment nodes." (Eloquent JavaScript, Ch. 14, lines 120-124)

# Prerequisites
- **Node**: Understanding the base DOM node concept

# Key Properties
1. `nodeType` is 1 (`Node.ELEMENT_NODE`)
2. Can contain child nodes (other elements, text, comments)
3. Have properties like `childNodes`, `children`, `firstChild`, `lastChild`
4. Have methods like `getElementsByTagName`, `querySelector`
5. Have attributes accessible as properties or via `getAttribute`/`setAttribute`
6. `nodeName` returns the tag name in uppercase

# Construction / Recognition
Element nodes are created with `document.createElement(tagName)` or found via query methods.

# Context & Application
Element nodes are the primary structural components of the DOM. Most DOM manipulation involves creating, finding, modifying, or removing element nodes.

# Examples
From the source: "Every element node (node type 1) has a `childNodes` property that points to an array-like object holding its children." (lines 197-199)

"There's also the `children` property, which is like `childNodes` but contains only element (type 1) children, not other types of child nodes." (lines 213-215)

# Relationships
## Builds Upon
- DOM node concept
## Enables
- Document structure, containment of other nodes
## Related
- HTML attributes, text nodes
## Contrasts With
- Text nodes (which are leaf nodes containing only text)

# Common Errors
- **Error**: Confusing `childNodes` (all nodes) with `children` (elements only)
  **Correction**: Use `children` when you want only element children, `childNodes` for all including text

# Common Confusions
- **Confusion**: Element nodes and HTML tags are the same
  **Clarification**: HTML tags are text syntax; element nodes are the in-memory objects the browser creates from them

# Source Reference
Chapter 14: The Document Object Model, Section "Trees", lines 120-124 of 14-the-document-object-model.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined
- Cross-reference status: verified
