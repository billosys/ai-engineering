---
concept: Input Element
slug: input-element
category: http-forms
subcategory: html-forms
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "HTTP and Forms"
chapter_number: 18
pdf_page: null
section: "Form fields"
extraction_confidence: high
aliases:
  - input tag
  - form input
  - text field
  - checkbox
  - radio button
prerequisites:
  - document-object-model
extends: []
related:
  - form-element
  - form-event
  - focus-and-blur
contrasts_with: []
answers_questions:
  - "What types of input fields does HTML provide?"
  - "How do I read form field values in JavaScript?"
---

# Quick Definition
The `<input>` element creates various form controls (text, password, checkbox, radio, color, date, file) determined by its `type` attribute, with a `value` property for reading and writing content.

# Core Definition
"A lot of field types use the `<input>` tag. This tag's `type` attribute is used to select the field's style" (Ch. 18). Common types include text, password, checkbox, color, date, radio, and file. Text fields use the `value` property; checkboxes and radio buttons use the `checked` property.

# Prerequisites
- **DOM**: Input elements are DOM nodes

# Key Properties
1. `type` attribute determines field kind (text, checkbox, radio, file, etc.)
2. `value` property holds current text content
3. `checked` property for checkboxes and radio buttons (boolean)
4. `name` attribute identifies the field in form submission
5. `disabled` attribute prevents interaction

# Construction / Recognition
```html
<input type="text" value="abc">
<input type="checkbox" checked>
<input type="radio" value="A" name="choice">
<input type="file">
```

# Context & Application
Input elements are the building blocks of web forms and interactive applications. They provide native, accessible controls for user data entry.

# Examples
Reading/writing text field:
```javascript
let text = document.querySelector("input");
text.addEventListener("input", () => {
  output.textContent = text.value.length;
});
```

Checkbox handling:
```javascript
checkbox.addEventListener("change", () => {
  document.body.style.background =
    checkbox.checked ? "mediumpurple" : "";
});
```

# Relationships
## Builds Upon
- document-object-model
## Enables
- User input, form-element, form-event
## Related
- select-and-option, focus-and-blur, file-reader
## Contrasts With
- Custom controls built from divs/spans (less accessible)

# Common Errors
- **Error**: Using `value` instead of `checked` for checkboxes
  **Correction**: Checkboxes use `checked` (boolean); `value` is the submission value

# Common Confusions
- **Confusion**: The "change" event fires on every keystroke in text fields
  **Clarification**: "change" fires when the field loses focus; use "input" for immediate updates

# Source Reference
Chapter 18: HTTP and Forms, Section "Form fields", lines 464-520 of 18-http-and-forms.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Multiple input types explained
- Cross-reference status: verified
