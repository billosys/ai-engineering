---
# === CORE IDENTIFICATION ===
concept: createElement
slug: createelement

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
section: "Creating nodes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - document.createElement

# === TYPED RELATIONSHIPS ===
prerequisites:
  - document-object-model
extends: []
related:
  - appendchild
  - text-node
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create new DOM elements?"
---

# Quick Definition
`document.createElement(tagName)` creates a new, empty element node of the specified type, which can then be populated with children and inserted into the document.

# Core Definition
"To create element nodes, you can use the `document.createElement` method. This method takes a tag name and returns a new empty node of the given type." (Eloquent JavaScript, Ch. 14, lines 393-395)

# Prerequisites
- **DOM**: Understanding the document object model

# Key Properties
1. Takes a tag name string as argument
2. Returns a new empty element node
3. The node is not yet part of the document -- must be inserted explicitly
4. Can be populated with children using `appendChild` or similar methods

# Construction / Recognition
```javascript
function elt(type, ...children) {
  let node = document.createElement(type);
  for (let child of children) {
    if (typeof child != "string") node.appendChild(child);
    else node.appendChild(document.createTextNode(child));
  }
  return node;
}
```
(lines 411-418)

# Context & Application
Used whenever new elements need to be created dynamically and added to the document.

# Examples
From the source, building an attribution for a blockquote:
```javascript
document.getElementById("quote").appendChild(
  elt("footer", "---",
      elt("strong", "Karl Popper"),
      ", preface to the second edition of ",
      elt("em", "The Open Society and Its Enemies"),
      ", 1950"));
```
(lines 420-425)

# Relationships
## Builds Upon
- DOM concept
## Enables
- Dynamic content creation
## Related
- `document.createTextNode()` for creating text nodes
- `appendChild` for inserting created nodes
## Contrasts With
- `innerHTML` (which creates elements from HTML strings)

# Common Errors
- **Error**: Creating an element and forgetting to add it to the document
  **Correction**: Use `appendChild`, `insertBefore`, or similar to insert the node into the tree

# Common Confusions
- **Confusion**: `createElement` adds the element to the page
  **Clarification**: It only creates the node in memory; you must explicitly insert it

# Source Reference
Chapter 14: The Document Object Model, Section "Creating nodes", lines 392-427 of 14-the-document-object-model.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with utility function example
- Cross-reference status: verified
