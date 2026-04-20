---
concept: Creating, Inserting, and Deleting DOM Nodes
slug: creating-inserting-deleting-nodes
category: browser-apis
subcategory: DOM
tier: foundational
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "JavaScript in Web Browsers"
chapter_number: 15
pdf_page: 465
section: "15.3.5 Creating, Inserting, and Deleting Nodes"
extraction_confidence: high
aliases:
  - DOM manipulation
  - createElement
  - append and prepend
prerequisites:
  - dom-tree
  - element-selection-queryselector
extends: []
related:
  - innerhtml-vs-textcontent
contrasts_with: []
answers_questions:
  - "What is the DOM (Document Object Model)?"
---

# Quick Definition

The DOM API provides methods to programmatically create new elements with `document.createElement()`, insert them with `append()`, `prepend()`, `before()`, and `after()`, and remove them with `remove()` or replace them with `replaceWith()`.

# Core Definition

New elements are created with `document.createElement()`. Elements are inserted using `append()` and `prepend()` (which add to the end or start of children) or `before()` and `after()` (which insert relative to siblings). String arguments are automatically converted to Text nodes. Elements can only exist at one position; inserting an element that is already in the document moves it. Use `cloneNode(true)` to copy an element. `remove()` detaches an element from the document (Flanagan, Ch. 15, pp. 465-468).

# Prerequisites

- **dom-tree** — Must understand the tree to modify it.
- **element-selection-queryselector** — Need to select elements before modifying them.

# Key Properties

1. `document.createElement(tagName)` creates a new empty element.
2. `append()` and `prepend()` accept any number of Node or string arguments.
3. `before()` and `after()` work on both Elements and Text nodes.
4. Inserting an already-inserted element moves it (no automatic copy).
5. `cloneNode(true)` performs a deep copy of an element and its descendants.

# Construction / Recognition

```javascript
let paragraph = document.createElement("p");
let emphasis = document.createElement("em");
emphasis.append("World");
paragraph.append("Hello ", emphasis, "!");
paragraph.prepend("!");
```

# Context & Application

Used whenever a web application needs to dynamically add, remove, or rearrange content in response to user actions or data loading.

# Examples

From the source (p. 466):
```javascript
paragraph.innerHTML // => "!Hello <em>World</em>!"
greetings.after(paragraph, document.createElement("hr"));
greetings.replaceWith(paragraph);
paragraph.remove();
```

# Relationships

## Builds Upon
- **dom-tree** — Modifies the tree structure
- **element-selection-queryselector** — Finds elements to modify

## Enables
- **web-components-overview** — Custom elements use these methods internally

## Related
- **innerhtml-vs-textcontent** — Alternative ways to modify content

## Contrasts With
- (None)

# Common Errors

- **Error**: Expecting `append()` to copy an element when it is already in the document.
  **Correction**: `append()` moves the element. Use `cloneNode(true)` first to make a copy.

# Common Confusions

- **Confusion**: The older methods (`appendChild`, `insertBefore`, `removeChild`) are required.
  **Clarification**: The modern methods (`append`, `prepend`, `before`, `after`, `remove`, `replaceWith`) are simpler and should be preferred.

# Source Reference

Chapter 15: JavaScript in Web Browsers, Section 15.3.5, pages 465-468.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: Clear examples and complete API coverage
- Uncertainties: None
- Cross-reference status: Verified
