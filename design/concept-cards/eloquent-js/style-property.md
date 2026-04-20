---
# === CORE IDENTIFICATION ===
concept: Style Property
slug: style-property

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
section: "Styling"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - element.style
  - inline style

# === TYPED RELATIONSHIPS ===
prerequisites:
  - element-node
extends: []
related:
  - css
  - layout
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I change an element's style with JavaScript?"
---

# Quick Definition
The `style` property on DOM elements is an object whose properties correspond to CSS style properties, allowing JavaScript to directly manipulate an element's inline styles.

# Core Definition
"JavaScript code can directly manipulate the style of an element through the element's `style` property. This property holds an object that has properties for all possible style properties. The values of these properties are strings, which we can write to in order to change a particular aspect of the element's style." (Eloquent JavaScript, Ch. 14, lines 641-646)

# Prerequisites
- **Element node**: Style is a property of element nodes

# Key Properties
1. Properties are strings (e.g., `"purple"`, `"10px"`)
2. Hyphenated CSS properties become camelCase (`font-family` -> `fontFamily`)
3. Numbers require units (e.g., `"10px"` not `10`), except for `0`
4. Setting a style property changes only that element's inline style
5. Inline styles have the highest specificity in CSS

# Construction / Recognition
```javascript
let para = document.getElementById("para");
console.log(para.style.color);
para.style.color = "magenta";
```
(lines 654-657)

# Context & Application
Used for dynamic style changes in response to user interaction, animations, or state changes.

# Examples
From the source: "Some style property names contain hyphens, such as `font-family`. Because such property names are awkward to work with in JavaScript (you'd have to say `style[\"font-family\"]`), the property names in the `style` object for such properties have their hyphens removed and the letters after them capitalized (`style.fontFamily`)." (lines 661-666)

# Relationships
## Builds Upon
- Element nodes
## Enables
- Dynamic visual updates, animations
## Related
- CSS (the styling system)
- Layout properties
## Contrasts With
- CSS stylesheets (which apply styles declaratively)

# Common Errors
- **Error**: Setting a numeric style value without units
  **Correction**: "Using numbers without units will result in your style being ignored---unless the number is 0." (lines 907-909)

# Common Confusions
- **Confusion**: The `style` property reflects all computed styles
  **Clarification**: It only reflects inline styles set via the `style` attribute, not styles from CSS classes or stylesheets

# Source Reference
Chapter 14: The Document Object Model, Section "Styling", lines 586-666 of 14-the-document-object-model.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined with examples
- Cross-reference status: verified
