---
# === CORE IDENTIFICATION ===
concept: Tagged Template
slug: tagged-template

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
section: "Tagged templates"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "tag function"
  - "tagged template literal"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - template-literal
extends:
  - template-literal
related:
  - string-raw
  - cooked-vs-raw-template-strings
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a template literal?"
---

# Quick Definition

A tagged template is a template literal preceded by a function (the "tag function"), which receives the template's static strings and interpolated values as separate arguments, enabling custom processing of template literal content.

# Core Definition

"Syntactically, a *tagged template* is a template literal that follows a function (or rather, an expression that evaluates to a function). That leads to the function being called. Its arguments are derived from the contents of the template literal." The tag function receives: (1) an array of template strings (the static text fragments), and (2) the interpolated values as remaining arguments. A tag function can return arbitrary values, not just strings (Ch. 23, Section 23.3).

# Prerequisites

- **template-literal** -- tagged templates are built on template literals

# Key Properties

1. Syntax: `` tagFunc`text ${expr} text` `` (ES6)
2. Tag function receives template strings array and substitution values
3. Template strings array has a `.raw` property with unescaped versions
4. Tag function can return any value (not limited to strings)
5. Static text and dynamic values are kept separate

# Construction / Recognition

```js
function tagFunc(templateStrings, ...substitutions) {
  return {templateStrings, substitutions};
}

const setting = 'dark mode';
const value = true;

tagFunc`Setting ${setting} is ${value}!`
// {
//   templateStrings: ['Setting ', ' is ', '!'],
//   substitutions: ['dark mode', true]
// }
```

# Context & Application

Tagged templates are used for domain-specific languages: HTML templating (lit-html), SQL query builders, GraphQL queries, regex construction, and internationalization.

# Examples

From the source text:

```js
function tagFunc(templateStrings, ...substitutions) {
  return {templateStrings, substitutions};
}

const setting = 'dark mode';
const value = true;

assert.deepEqual(
  tagFunc`Setting ${setting} is ${value}!`,
  {
    templateStrings: ['Setting ', ' is ', '!'],
    substitutions: ['dark mode', true],
  }
);

// Library examples: lit-html, regex, graphql-tag
const query = gql`
  { user(id: 5) { firstName lastName } }
`;
```

# Relationships

## Builds Upon
- **template-literal** — tagged templates extend template literal syntax

## Enables
- Domain-specific languages (DSLs)
- Safe HTML templating
- SQL injection prevention

## Related
- **string-raw** — `String.raw` is a built-in tag function
- **cooked-vs-raw-template-strings** — tag functions receive both interpretations

## Contrasts With
- None

# Common Errors

- **Error**: Expecting a tagged template to always return a string
  **Correction**: Tag functions can return any value -- objects, arrays, DOM nodes, etc.

# Common Confusions

- **Confusion**: Thinking the tag function is called with a single string
  **Clarification**: The tag function receives the template strings array and each substitution as separate arguments.

# Source Reference

Chapter 23: Using template literals and tagged templates, Section 23.3, lines 145-265.

# Verification Notes

- Definition source: direct
- Confidence rationale: Explicit definition with argument structure
- Cross-reference status: verified
