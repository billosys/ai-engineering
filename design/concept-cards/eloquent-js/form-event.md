---
concept: Form Events
slug: form-event
category: http-forms
subcategory: html-forms
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "HTTP and Forms"
chapter_number: 18
pdf_page: null
section: "The form as a whole"
extraction_confidence: high
aliases:
  - submit event
  - change event
  - input event
prerequisites:
  - event-handler
  - form-element
extends: []
related:
  - input-element
  - focus-and-blur
contrasts_with: []
answers_questions:
  - "What events do form fields fire?"
  - "How do I intercept form submission?"
---

# Quick Definition
Form events include "submit" (fired on the form when submitted), "change" (fired when a field's value changes and it loses focus), and "input" (fired immediately on every keystroke or content change).

# Core Definition
"Submitting a form normally means that the browser navigates to the page indicated by the form's `action` attribute. [...] But before that happens, a `'submit'` event is fired" (Ch. 18). "The `'change'` event for a text field does not fire every time something is typed. Rather, it fires when the field loses focus after its content was changed. To respond immediately to changes in a text field, you should register a handler for the `'input'` event instead."

# Prerequisites
- **Event handlers**: Events are handled via addEventListener
- **Form elements**: Events fire on form and field elements

# Key Properties
1. "submit" -- fires on form before navigation; preventDefault() stops it
2. "change" -- fires when value changes AND field loses focus
3. "input" -- fires immediately on every content change
4. Submit triggered by submit button click or pressing Enter in a field

# Construction / Recognition
```javascript
form.addEventListener("submit", event => {
  console.log("Saving value", form.elements.value.value);
  event.preventDefault();
});

text.addEventListener("input", () => {
  output.textContent = text.value.length;
});
```

# Context & Application
Form events are essential for validation, dynamic UI updates, and JavaScript-controlled form handling without page navigation.

# Examples
Real-time character count:
```html
<input type="text"> length: <span id="length">0</span>
<script>
  let text = document.querySelector("input");
  let output = document.querySelector("#length");
  text.addEventListener("input", () => {
    output.textContent = text.value.length;
  });
</script>
```

# Relationships
## Builds Upon
- event-handler, form-element, input-element
## Enables
- Form validation, live search, auto-save, SPA navigation
## Related
- focus-and-blur, fetch-api
## Contrasts With
- Polling for changes (checking values on a timer)

# Common Errors
- **Error**: Using "change" for real-time text validation
  **Correction**: Use "input" for immediate feedback; "change" only fires on blur

# Common Confusions
- **Confusion**: The submit event is redundant with button click handlers
  **Clarification**: Submit also fires when Enter is pressed in a field; it's the canonical way to handle submission

# Source Reference
Chapter 18: HTTP and Forms, Section "The form as a whole" and "Text fields", lines 661-806 of 18-http-and-forms.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: All three events explicitly described
- Cross-reference status: verified
