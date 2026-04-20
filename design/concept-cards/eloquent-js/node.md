---
# === CORE IDENTIFICATION ===
concept: Node (DOM)
slug: node

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
  - DOM node

# === TYPED RELATIONSHIPS ===
prerequisites:
  - document-object-model
extends: []
related:
  - element-node
  - text-node
  - document-tree
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a DOM node?"
---

# Quick Definition
A DOM node is an individual object in the document tree, identified by a `nodeType` property that indicates whether it is an element, text, comment, or other type.

# Core Definition
"Each DOM node object has a `nodeType` property, which contains a code (number) that identifies the type of node. Elements have code 1, which is also defined as the constant property `Node.ELEMENT_NODE`. Text nodes, representing a section of text in the document, get code 3 (`Node.TEXT_NODE`). Comments have code 8 (`Node.COMMENT_NODE`)." (Eloquent JavaScript, Ch. 14, lines 127-133)

# Prerequisites
- **DOM**: Understanding the document object model

# Key Properties
1. `nodeType` property identifies the type (1 = element, 3 = text, 8 = comment)
2. `parentNode` points to the parent node
3. `childNodes` holds an array-like `NodeList` of children
4. `firstChild`, `lastChild`, `previousSibling`, `nextSibling` for navigation
5. Element nodes have a `children` property containing only element children
6. `nodeValue` holds the text content for text nodes

# Construction / Recognition
Nodes are accessed by traversing the DOM tree from `document.body` or by using query methods like `querySelector`.

# Context & Application
Nodes are the fundamental building blocks of the DOM tree. All DOM manipulation operates on nodes.

# Examples
From the source, a recursive function that processes different node types:
```javascript
function talksAbout(node, string) {
  if (node.nodeType == Node.ELEMENT_NODE) {
    for (let child of node.childNodes) {
      if (talksAbout(child, string)) {
        return true;
      }
    }
    return false;
  } else if (node.nodeType == Node.TEXT_NODE) {
    return node.nodeValue.indexOf(string) > -1;
  }
}
```
(lines 225-236)

# Relationships
## Builds Upon
- Document Object Model
## Enables
- Tree traversal and document manipulation
## Related
- Element nodes (type 1), text nodes (type 3)
## Contrasts With
- JavaScript objects in general (DOM nodes have a specific API)

# Common Errors
- **Error**: Treating `childNodes` as a real array
  **Correction**: `childNodes` is a `NodeList`, not an array; use `Array.from()` to convert it

# Common Confusions
- **Confusion**: All nodes are elements
  **Clarification**: Element nodes are one type; text nodes, comment nodes are also nodes

# Source Reference
Chapter 14: The Document Object Model, Section "Trees", lines 127-143 of 14-the-document-object-model.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with type codes
- Cross-reference status: verified
