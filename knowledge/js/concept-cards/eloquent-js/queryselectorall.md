---
# === CORE IDENTIFICATION ===
concept: querySelectorAll
slug: queryselectorall

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
section: "Query selectors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - document.querySelectorAll

# === TYPED RELATIONSHIPS ===
prerequisites:
  - document-object-model
  - css
extends: []
related:
  - queryselector
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I find elements in the DOM?"
---

# Quick Definition
`querySelectorAll` returns a static `NodeList` of all elements matching a CSS selector string, unlike live collections returned by methods like `getElementsByTagName`.

# Core Definition
"The `querySelectorAll` method, which is defined both on the `document` object and on element nodes, takes a selector string and returns a `NodeList` containing all the elements that it matches." "Unlike methods such as `getElementsByTagName`, the object returned by `querySelectorAll` is *not* live. It won't change when you change the document." (Eloquent JavaScript, Ch. 14, lines 750-753, 779-781)

# Prerequisites
- **DOM**: Understanding the DOM
- **CSS selectors**: Selector syntax

# Key Properties
1. Returns a `NodeList` (not a live collection, not a real array)
2. Matches use CSS selector syntax
3. Available on both `document` and element nodes
4. The returned collection is static (doesn't update when DOM changes)
5. Need `Array.from()` to use array methods like `map`

# Construction / Recognition
```javascript
function count(selector) {
  return document.querySelectorAll(selector).length;
}
console.log(count("p"));           // All <p> elements -> 4
console.log(count(".animal"));     // Class animal -> 2
console.log(count("p .animal"));   // Animal inside of <p> -> 2
console.log(count("p > .animal")); // Direct child of <p> -> 1
```
(lines 764-775)

# Context & Application
Used when you need to find and operate on multiple matching elements in the document.

# Examples
From the source, demonstrating various selectors (lines 764-775 shown above).

# Relationships
## Builds Upon
- DOM and CSS selector syntax
## Enables
- Batch operations on matching elements
## Related
- `querySelector` (single element version)
## Contrasts With
- `getElementsByTagName` (returns a live collection)

# Common Errors
- **Error**: Treating the returned `NodeList` as an array
  **Correction**: "You need to call `Array.from` if you want to treat it like one." (lines 782-783)

# Common Confusions
- **Confusion**: `querySelectorAll` returns a live collection like `getElementsByTagName`
  **Clarification**: The NodeList from `querySelectorAll` is static; it does not update when the DOM changes

# Source Reference
Chapter 14: The Document Object Model, Section "Query selectors", lines 738-789 of 14-the-document-object-model.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with examples
- Cross-reference status: verified
