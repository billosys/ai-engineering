---
# === CORE IDENTIFICATION ===
concept: Templating via Template Literals
slug: template-as-templating

# === CLASSIFICATION ===
category: primitive-types
subcategory: strings
tier: advanced

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Using template literals and tagged templates"
chapter_number: 23
pdf_page: null
section: "Simple templating via template literals (advanced)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - template-literal
  - string-interpolation
extends: []
related:
  - tagged-template
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a template literal?"
---

# Quick Definition

Template literals can be used for text templating by wrapping them in a function that receives data as a parameter, turning the function into a reusable template.

# Core Definition

"A text template gets its data from an object, while a template literal gets its data from variables. The solution is to use a template literal in the body of a function whose parameter receives the templating data" (Ch. 23, Section 23.7). This creates a simple but effective templating mechanism without external libraries.

# Prerequisites

- **template-literal** -- the syntax used for templating
- **string-interpolation** -- the mechanism for inserting data

# Key Properties

1. Wrap template literal in a function
2. Function parameter provides the template data
3. HTML special characters should be escaped
4. Can nest template literals for sub-templates (e.g., table rows)

# Construction / Recognition

```js
const tmpl = (data) => `Hello ${data.name}!`;
assert.equal(tmpl({name: 'Jane'}), 'Hello Jane!');
```

# Context & Application

This pattern is useful for simple HTML generation, email templates, or any text generation where a full template engine is not needed.

# Examples

From the source text:

```js
const tmpl = (data) => `Hello ${data.name}!`;
assert.equal(tmpl({name: 'Jane'}), 'Hello Jane!');

// More complex: HTML table from array
const tmpl = (addrs) => `
<table>
  ${addrs.map(
    (addr) => `
      <tr>
        <td>${escapeHtml(addr.first)}</td>
        <td>${escapeHtml(addr.last)}</td>
      </tr>
    `.trim()
  ).join('')}
</table>
`.trim();
```

# Relationships

## Builds Upon
- **template-literal** — uses template literal syntax
- **string-interpolation** — uses `${}` for data insertion

## Enables
- Simple text templating without libraries

## Related
- **tagged-template** — more advanced templating approach

## Contrasts With
- None

# Common Errors

- **Error**: Not escaping HTML special characters in user data
  **Correction**: Always use an `escapeHtml()` function when generating HTML from user data.

# Common Confusions

- **Confusion**: Thinking template literals ARE text templates
  **Clarification**: They are similar but distinct. Template literals evaluate immediately; text templates are typically stored and compiled separately.

# Source Reference

Chapter 23: Using template literals and tagged templates, Section 23.7, lines 510-618.

# Verification Notes

- Definition source: direct
- Confidence rationale: Complete example with HTML generation
- Cross-reference status: verified
