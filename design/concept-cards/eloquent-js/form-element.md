---
concept: Form Element
slug: form-element
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
  - HTML form
  - form tag
prerequisites:
  - document-object-model
  - http-method
extends: []
related:
  - input-element
  - form-event
  - select-and-option
contrasts_with: []
answers_questions:
  - "How do HTML forms work?"
  - "What must I know before building a web application?"
---

# Quick Definition
The `<form>` element groups input fields and submits their values as an HTTP request when activated, either by navigating to a new page or by being intercepted with JavaScript.

# Core Definition
"Forms were originally designed for the pre-JavaScript web to allow websites to send user-submitted information in an HTTP request" (Ch. 18, "Form fields"). A form's `method` attribute (GET or POST) determines how data is sent, and its `action` attribute specifies the destination URL. The `elements` property provides access to contained fields.

# Prerequisites
- **DOM**: Forms are DOM elements
- **HTTP methods**: Forms submit using GET or POST

# Key Properties
1. `method` attribute -- GET (query string) or POST (request body)
2. `action` attribute -- destination URL
3. `elements` property -- array-like collection of fields (accessible by index or name)
4. Submit event fires before navigation
5. `preventDefault()` on submit event stops default behavior

# Construction / Recognition
```html
<form method="GET" action="example/message.html">
  <p>Name: <input type="text" name="name"></p>
  <p>Message:<br><textarea name="message"></textarea></p>
  <p><button type="submit">Send</button></p>
</form>
```

# Context & Application
Forms are the traditional way to collect and send user input. Modern applications often intercept submission with JavaScript to handle data without page navigation.

# Examples
Intercepting form submission:
```javascript
form.addEventListener("submit", event => {
  console.log("Saving value", form.elements.value.value);
  event.preventDefault();
});
```

# Relationships
## Builds Upon
- document-object-model, http-method
## Enables
- User data collection, form-event, fetch-based submission
## Related
- input-element, select-and-option, form-event
## Contrasts With
- Custom UI controls (not using native form elements)

# Common Errors
- **Error**: Forgetting preventDefault, causing page navigation on submit
  **Correction**: Call event.preventDefault() in the submit handler for JavaScript-handled forms

# Common Confusions
- **Confusion**: Form fields must be inside a form element
  **Clarification**: Fields can exist outside forms but cannot be submitted via the form mechanism

# Source Reference
Chapter 18: HTTP and Forms, Section "Form fields" and "The form as a whole", lines 464-728 of 18-http-and-forms.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Thorough coverage with multiple examples
- Cross-reference status: verified
