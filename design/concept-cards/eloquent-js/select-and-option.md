---
concept: Select and Option Elements
slug: select-and-option
category: http-forms
subcategory: html-forms
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "HTTP and Forms"
chapter_number: 18
pdf_page: null
section: "Select fields"
extraction_confidence: high
aliases:
  - dropdown
  - select field
prerequisites:
  - form-element
extends: []
related:
  - input-element
  - form-event
contrasts_with: []
answers_questions:
  - "How do I create a dropdown menu in HTML?"
  - "How do I read the selected value from a select element?"
---

# Quick Definition
The `<select>` element creates a dropdown (or multi-select list) from `<option>` child elements, with the selected value accessible via the `value` property and individual options via the `options` collection.

# Core Definition
"Select fields are conceptually similar to radio buttons -- they also allow the user to choose from a set of options" (Ch. 18, "Select fields"). Each option has a `value` and `selected` property. With the `multiple` attribute, users can select multiple options.

# Prerequisites
- **Form element**: Select is a form field

# Key Properties
1. `value` property -- the currently selected option's value
2. `options` property -- array-like collection of option elements
3. Each option has `value`, `selected`, and text content
4. `multiple` attribute enables multi-select
5. Fires "change" event when selection changes

# Construction / Recognition
```html
<select>
  <option>Pancakes</option>
  <option>Pudding</option>
  <option>Ice cream</option>
</select>
```

Multiple select:
```javascript
for (let option of Array.from(select.options)) {
  if (option.selected) {
    number += Number(option.value);
  }
}
```

# Context & Application
Used for choosing from predefined options in forms, filters, settings, and navigation. The tool selector in the pixel art editor (Ch. 19) uses a select element.

# Examples
From Ch. 18, binary number builder:
```html
<select multiple>
  <option value="1">0001</option>
  <option value="2">0010</option>
  <option value="4">0100</option>
  <option value="8">1000</option>
</select>
```

# Relationships
## Builds Upon
- form-element
## Enables
- User choice, tool selection, filtering
## Related
- input-element, form-event
## Contrasts With
- Radio buttons (visible choices, not dropdown)

# Common Errors
- **Error**: Using `value` property to get all selections from a multiple select
  **Correction**: For multiple selects, iterate over options and check each `selected` property

# Common Confusions
- **Confusion**: Option value is always the same as its text content
  **Clarification**: If no `value` attribute is given, the text is used; otherwise the `value` attribute is used

# Source Reference
Chapter 18: HTTP and Forms, Section "Select fields", lines 866-926 of 18-http-and-forms.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Both single and multiple select explained
- Cross-reference status: verified
