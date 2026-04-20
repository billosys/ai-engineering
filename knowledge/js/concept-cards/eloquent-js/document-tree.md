---
# === CORE IDENTIFICATION ===
concept: Document Tree
slug: document-tree

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
  - DOM tree

# === TYPED RELATIONSHIPS ===
prerequisites:
  - document-object-model
extends: []
related:
  - element-node
  - text-node
  - node
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the DOM (Document Object Model)?"
  - "How does the DOM relate to HTML?"
---

# Quick Definition
The document tree is the hierarchical, tree-shaped structure of DOM nodes, where each node may have child nodes and a parent, with `document.documentElement` as the root.

# Core Definition
"We call a data structure a *tree* when it has a branching structure, no cycles (a node may not contain itself, directly or indirectly), and a single, well-defined *root*. In the case of the DOM, `document.documentElement` serves as the root." (Eloquent JavaScript, Ch. 14, lines 99-103)

# Prerequisites
- **DOM**: Understanding what the DOM represents

# Key Properties
1. Has a single root node (`document.documentElement`)
2. No cycles -- nodes cannot contain themselves
3. Each node has at most one parent
4. Nodes can have zero or more children
5. Leaf nodes (text nodes, comments) have no children
6. The tree mirrors the nesting structure of HTML

# Construction / Recognition
Navigation properties:
- `parentNode` -- the node's parent
- `childNodes` -- array-like list of children
- `firstChild` / `lastChild` -- first and last children
- `previousSibling` / `nextSibling` -- adjacent siblings

# Context & Application
Understanding the tree structure is essential for DOM traversal, element finding, and document manipulation.

# Examples
From the source: "Each *node* may refer to other nodes, *children*, which in turn may have their own children. This shape is typical of nested structures, where elements can contain subelements that are similar to themselves." (lines 94-96)

"The example document's `<body>` tag has not just three children (`<h1>` and two `<p>` elements), but seven: those three, plus the spaces before, after, and between them." (lines 256-258)

# Relationships
## Builds Upon
- DOM concept
## Enables
- Tree traversal and node manipulation
## Related
- Element nodes, text nodes
## Contrasts With
- Flat data structures (arrays, lists)

# Common Errors
- **Error**: Forgetting that whitespace between tags creates text nodes in the tree
  **Correction**: Text nodes exist for all text content, including whitespace between elements

# Common Confusions
- **Confusion**: The tree only contains element nodes
  **Clarification**: Text nodes, comment nodes, and other node types also appear in the tree

# Source Reference
Chapter 14: The Document Object Model, Section "Trees", lines 88-143 of 14-the-document-object-model.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with diagrams
- Cross-reference status: verified
