---
# === CORE IDENTIFICATION ===
concept: appendChild
slug: appendchild

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
section: "Changing the document"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - append child

# === TYPED RELATIONSHIPS ===
prerequisites:
  - element-node
extends: []
related:
  - createelement
  - removechild
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I add elements to the DOM?"
---

# Quick Definition
`appendChild` adds a node as the last child of an element, and if the node is already in the document, it is moved from its current position.

# Core Definition
"To add a child node to an element node, we can use `appendChild`, which puts it at the end of the list of children, or `insertBefore`, which inserts the node given as the first argument before the node given as the second argument." "A node can exist in the document in only one place. Thus, inserting paragraph *Three* in front of paragraph *One* will first remove it from the end of the document and then insert it at the front." (Eloquent JavaScript, Ch. 14, lines 304-306, 321-324)

# Prerequisites
- **Element node**: Nodes that can contain children

# Key Properties
1. Adds a node to the end of the parent's child list
2. If the node already exists elsewhere in the document, it is moved (not copied)
3. Returns the appended child node
4. Works with both element nodes and text nodes

# Construction / Recognition
```javascript
document.body.insertBefore(paragraphs[2], paragraphs[0]);
```
Moves the third paragraph before the first. (lines 316-317)

# Context & Application
Used for building up DOM structures programmatically, adding dynamically created content, and rearranging existing elements.

# Examples
From the source:
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

"All operations that insert a node somewhere will, as a side effect, cause it to be removed from its current position (if it has one)." (lines 325-326)

# Relationships
## Builds Upon
- Element nodes that can contain children
## Enables
- Building DOM trees programmatically
## Related
- `createElement`, `createTextNode` (create nodes to append)
- `insertBefore` (insert at a specific position)
## Contrasts With
- `remove()` (removes a node from the tree)

# Common Errors
- **Error**: Expecting `appendChild` to copy a node rather than move it
  **Correction**: A node can only exist in one place; appending moves it

# Common Confusions
- **Confusion**: `appendChild` adds HTML text
  **Clarification**: It adds a node object, not a string; use `createTextNode` for text

# Source Reference
Chapter 14: The Document Object Model, Section "Changing the document", lines 298-334 of 14-the-document-object-model.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with examples
- Cross-reference status: verified
