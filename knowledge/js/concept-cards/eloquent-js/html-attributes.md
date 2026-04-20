---
# === CORE IDENTIFICATION ===
concept: HTML Attributes
slug: html-attributes

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
section: "Attributes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - element attributes
  - getAttribute/setAttribute

# === TYPED RELATIONSHIPS ===
prerequisites:
  - element-node
extends: []
related:
  - style-property
  - classList
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I access element attributes in the DOM?"
---

# Quick Definition
HTML attributes are name-value pairs on elements that can be accessed as DOM properties for standard attributes, or via `getAttribute`/`setAttribute` for custom attributes.

# Core Definition
"Some element attributes, such as `href` for links, can be accessed through a property of the same name on the element's DOM object." "To read or change custom attributes, which aren't available as regular object properties, you have to use the `getAttribute` and `setAttribute` methods." (Eloquent JavaScript, Ch. 14, lines 438-448)

# Prerequisites
- **Element node**: Attributes belong to element nodes

# Key Properties
1. Standard attributes map to DOM properties (e.g., `href`, `src`, `id`)
2. Custom attributes use `getAttribute`/`setAttribute`
3. Custom attributes should be prefixed with `data-`
4. The `class` attribute is accessed via `className` property (keyword conflict)
5. Can also use `getAttribute("class")` for the class attribute

# Construction / Recognition
```javascript
let paras = document.body.getElementsByTagName("p");
for (let para of Array.from(paras)) {
  if (para.getAttribute("data-classified") == "secret") {
    para.remove();
  }
}
```
(lines 455-461)

# Context & Application
Attributes are used to configure elements, store custom data, and control behavior and appearance.

# Examples
From the source: "It is recommended to prefix the names of such made-up attributes with `data-` to ensure they do not conflict with any other attributes." (lines 465-467)

"The property used to access this attribute is called `className`. You can also access it under its real name, `\"class\"`, with the `getAttribute` and `setAttribute` methods." (lines 473-475)

# Relationships
## Builds Upon
- Element nodes
## Enables
- Configuring elements, storing custom data
## Related
- Style property (one specific attribute)
- classList (working with the class attribute)
## Contrasts With
- DOM properties (which are not always one-to-one with attributes)

# Common Errors
- **Error**: Using `element.class` to access the class attribute
  **Correction**: Use `element.className` or `element.getAttribute("class")`

# Common Confusions
- **Confusion**: DOM properties and HTML attributes are always the same
  **Clarification**: Standard attributes have corresponding properties, but custom attributes require `getAttribute`/`setAttribute`

# Source Reference
Chapter 14: The Document Object Model, Section "Attributes", lines 435-475 of 14-the-document-object-model.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly explained with examples
- Cross-reference status: verified
