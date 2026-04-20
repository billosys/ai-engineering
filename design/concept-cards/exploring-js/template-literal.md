---
# === CORE IDENTIFICATION ===
concept: Template Literal
slug: template-literal

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
section: "Template literals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "template string"
  - "backtick string"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string-type
extends: []
related:
  - tagged-template
  - string-interpolation
  - string-raw
contrasts_with:
  - string-literals

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a template literal?"
---

# Quick Definition

A template literal is a string literal delimited by backticks (`` ` ``) that supports string interpolation via `${expression}` and can span multiple lines. Introduced in ES6.

# Core Definition

"A *template literal* is similar to a string literal, but has additional features -- for example, interpolation." Template literals are delimited by backticks. They support *string interpolation*: `${expression}` evaluates the expression, converts it to string, and inserts it. They also support multiple lines. Template literals always produce strings (Ch. 23, Section 23.2).

# Prerequisites

- **string-type** -- template literals produce strings

# Key Properties

1. Delimited by backticks (`` ` ``) (ES6)
2. String interpolation: `${expression}` inserts converted-to-string values
3. Multiline: can span multiple lines without escape sequences
4. Always produces strings
5. Expressions inside `${}` can be any JavaScript expression

# Construction / Recognition

```js
const num = 5;
assert.equal(`Count: ${num}!`, 'Count: 5!');

const str = `this is
a text with
multiple lines`;
```

# Context & Application

Template literals are the modern preferred way to build strings with dynamic content, replacing string concatenation with `+`. They are also used for multiline strings and as the basis for tagged templates.

# Examples

From the source text:

```js
const num = 5;
assert.equal(`Count: ${num}!`, 'Count: 5!');

const MAX = 100;
function doSomeWork(x) {
  if (x > MAX) {
    throw new Error(`At most ${MAX} allowed: ${x}!`);
  }
}
assert.throws(
  () => doSomeWork(101),
  {message: 'At most 100 allowed: 101!'}
);

// Multiline
const str = `this is
a text with
multiple lines`;
```

# Relationships

## Builds Upon
- **string-type** — template literals produce strings

## Enables
- **tagged-template** — tagged templates are template literals preceded by a function
- Readable string interpolation

## Related
- **string-interpolation** — the `${}` feature
- **string-raw** — raw template literals via `String.raw`

## Contrasts With
- **string-literals** — plain string literals lack interpolation and multiline

# Common Errors

- **Error**: Using `\n` in a template literal when wanting an actual newline
  **Correction**: Template literals support literal newlines -- just press Enter. `\n` still works as an escape sequence.

# Common Confusions

- **Confusion**: Thinking template literals and "text templates" (like Handlebars) are the same
  **Clarification**: Template literals are JavaScript syntax for string creation. Text templates are a separate concept for data-driven HTML generation.

# Source Reference

Chapter 23: Using template literals and tagged templates, Section 23.2, lines 109-143.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with disambiguation
- Cross-reference status: verified
