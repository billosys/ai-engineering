---
# === CORE IDENTIFICATION ===
concept: CSS (Cascading Style Sheets)
slug: css

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
section: "Cascading styles"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Cascading Style Sheets
  - stylesheets

# === TYPED RELATIONSHIPS ===
prerequisites:
  - html
extends: []
related:
  - style-property
  - queryselector
  - layout
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is CSS?"
---

# Quick Definition
CSS (Cascading Style Sheets) is a styling system for HTML that uses rules to define how elements should be displayed, with multiple rules cascading and combining to produce the final style.

# Core Definition
"The styling system for HTML is called *CSS*, for *Cascading Style Sheets*. A *style sheet* is a set of rules for how to style elements in a document." "The *cascading* in the name refers to the fact that multiple such rules are combined to produce the final style for an element." (Eloquent JavaScript, Ch. 14, lines 671-672, 687-689)

# Prerequisites
- **HTML**: CSS styles HTML documents

# Key Properties
1. Rules target elements using selectors (tag name, `.class`, `#id`)
2. Multiple rules cascade -- later rules override earlier ones at same specificity
3. More specific selectors take precedence over less specific ones
4. Inline styles (`style` attribute) have highest precedence
5. Rules can target direct children (`p > a`) or any descendants (`p a`)

# Construction / Recognition
```css
.subtle {
  color: gray;
  font-size: 80%;
}
#header {
  background: blue;
  color: white;
}
```
(lines 709-716)

# Context & Application
CSS is essential for visual presentation of web pages. Understanding CSS selectors is also important because `querySelector` and `querySelectorAll` use the same syntax.

# Examples
From the source: "A rule for `.abc` applies to all elements with `\"abc\"` in their `class` attribute. A rule for `#xyz` applies to the element with an `id` attribute of `\"xyz\"`." (lines 703-706)

"A rule's specificity is a measure of how precisely it describes matching elements, determined by the number and kind (tag, class, or ID) of element aspects it requires." (lines 726-728)

# Relationships
## Builds Upon
- HTML documents
## Enables
- Visual styling and layout of web pages
## Related
- `style` property (inline CSS via JavaScript)
- `querySelector` (uses CSS selector syntax)
## Contrasts With
- Inline styles (applied directly to elements)

# Common Errors
- **Error**: Expecting a less specific but later rule to override a more specific earlier rule
  **Correction**: Specificity takes precedence over source order

# Common Confusions
- **Confusion**: CSS class selectors and JavaScript class declarations
  **Clarification**: They are completely different concepts with the same name

# Source Reference
Chapter 14: The Document Object Model, Section "Cascading styles", lines 668-737 of 14-the-document-object-model.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined
- Cross-reference status: verified
