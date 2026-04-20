---
concept: Focus and Blur
slug: focus-and-blur
category: http-forms
subcategory: html-forms
tier: intermediate
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "HTTP and Forms"
chapter_number: 18
pdf_page: null
section: "Focus"
extraction_confidence: high
aliases:
  - keyboard focus
  - activeElement
prerequisites:
  - input-element
extends: []
related:
  - form-event
  - form-element
contrasts_with: []
answers_questions:
  - "How does focus work with form fields?"
  - "How do I programmatically focus a form field?"
---

# Quick Definition
Focus determines which element receives keyboard input; `focus()` and `blur()` methods control it programmatically, while `document.activeElement` reveals the currently focused element.

# Core Definition
"Unlike most elements in HTML documents, form fields can get keyboard focus. When clicked, moved to with tab, or activated in some other way, they become the currently active element and the recipient of keyboard input" (Ch. 18, "Focus"). The `focus()` method moves focus to an element; `blur()` removes it.

# Prerequisites
- **Input elements**: Form fields are the primary focusable elements

# Key Properties
1. `element.focus()` -- gives focus to the element
2. `element.blur()` -- removes focus
3. `document.activeElement` -- the currently focused element
4. `autofocus` attribute -- focuses element on page load
5. `tabindex` attribute -- controls tab order and makes non-form elements focusable

# Construction / Recognition
```javascript
document.querySelector("input").focus();
console.log(document.activeElement.tagName); // → INPUT
document.querySelector("input").blur();
console.log(document.activeElement.tagName); // → BODY
```

# Context & Application
Essential for accessibility, keyboard navigation, and user experience. Auto-focusing the right field on page load, managing focus during form validation, and keyboard-driven interfaces all depend on focus management.

# Examples
```html
<input type="text" tabindex=1> <a href=".">(help)</a>
<button onclick="console.log('ok')" tabindex=2>OK</button>
```
"By default, most types of HTML elements cannot be focused. You can add a `tabindex` attribute to any element to make it focusable."

# Relationships
## Builds Upon
- input-element
## Enables
- Keyboard navigation, accessibility, form validation UX
## Related
- form-event, form-element
## Contrasts With
- Mouse-only interaction (ignores keyboard users)

# Common Errors
- **Error**: Calling focus() before the element is in the DOM
  **Correction**: Ensure the element is attached to the document first

# Common Confusions
- **Confusion**: Only form elements can receive focus
  **Clarification**: Any element with tabindex can receive focus

# Source Reference
Chapter 18: HTTP and Forms, Section "Focus", lines 570-632 of 18-http-and-forms.md.

# Verification Notes
- Definition source: direct from source text
- Confidence rationale: Complete explanation with code examples
- Cross-reference status: verified
