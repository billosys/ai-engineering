---
# === CORE IDENTIFICATION ===
concept: Multiline Template Literals
slug: multiline-template-literals

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
section: "Multiline template literals and indentation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - template-literal
extends: []
related:
  - tagged-template
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Multiline template literals naturally include indentation from the source code, creating a conflict between code formatting and desired output. Solutions include the `dedent` tag function or `.trim()`.

# Core Definition

Template literals can span multiple lines, but indentation intended for source code readability becomes part of the string content. Two fixes: (1) use a custom template tag like `dedent` that removes common leading indentation, or (2) start content at the left column and use `.trim()` to remove leading/trailing whitespace (Ch. 23, Section 23.6).

# Prerequisites

- **template-literal** -- multiline is a feature of template literals

# Key Properties

1. Template literals preserve all whitespace including indentation
2. Problem: source code indentation bleeds into the string content
3. Fix 1: `dedent` tag function removes common indentation
4. Fix 2: `.trim()` removes leading/trailing whitespace (but content cannot be indented)

# Construction / Recognition

```js
// Problem: unwanted indentation
function div(text) {
  return `
    <div>
      ${text}
    </div>
  `;
}

// Fix with dedent
function divDedented(text) {
  return dedent`
    <div>
      ${text}
    </div>
  `;
}

// Fix with trim
function divTrimmed(text) {
  return `
<div>
  ${text}
</div>
  `.trim();
}
```

# Context & Application

This is a practical concern when embedding HTML, SQL, or other text blocks in JavaScript code. The `dedent` library is widely used.

# Examples

From the source text:

```js
import dedent from 'dedent';
function divDedented(text) {
  return dedent`
    <div>
      ${text}
    </div>
  `;
}
console.log(divDedented('Hello!'));
// Output:
// <div>
//   Hello!
// </div>
```

# Relationships

## Builds Upon
- **template-literal** — multiline is a template literal feature

## Enables
- Readable multiline string embedding in code

## Related
- **tagged-template** — `dedent` is a tag function

## Contrasts With
- None

# Common Errors

- **Error**: Including unwanted leading whitespace in multiline template literals
  **Correction**: Use `dedent` or `.trim()` to remove unwanted indentation.

# Common Confusions

- **Confusion**: Thinking template literals automatically strip indentation
  **Clarification**: All whitespace is preserved. Indentation removal must be done explicitly.

# Source Reference

Chapter 23: Using template literals and tagged templates, Section 23.6, lines 399-508.

# Verification Notes

- Definition source: direct
- Confidence rationale: Two solutions presented with examples
- Cross-reference status: verified
