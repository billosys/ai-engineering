---
# === CORE IDENTIFICATION ===
concept: Tagged Template Use Cases
slug: tagged-template-use-cases

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
section: "Examples of tagged templates (as provided via libraries)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "domain-specific languages via tagged templates"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tagged-template
extends: []
related:
  - string-raw
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a template literal?"
---

# Quick Definition

Tagged templates are used by libraries to implement domain-specific languages: HTML templating (lit-html), regular expressions (regex library), GraphQL queries (graphql-tag), and more.

# Core Definition

"Tagged templates are great for supporting small embedded languages (so-called *domain-specific languages*)." Libraries use tag functions to parse and process template content with type safety and syntax support. Examples include lit-html for HTML components, the regex library for readable regular expressions with comments and insignificant whitespace, and graphql-tag for GraphQL queries (Ch. 23, Section 23.4).

# Prerequisites

- **tagged-template** -- these are applications of tagged templates

# Key Properties

1. lit-html: HTML templating for web components
2. regex: readable regular expressions with comments and free-spacing
3. graphql-tag: GraphQL query definitions
4. Static text and dynamic values are separated, enabling security features
5. Build-time plugins can pre-compile tagged templates

# Construction / Recognition

```js
// lit-html
html`<ul>${repeat(items, (item) => html`<li>${item.name}</li>`)}</ul>`

// regex
const RE_DATE = regex('g')`
  ${RE_YEAR} - ${RE_MONTH} - ${RE_DAY}
`;

// graphql-tag
const query = gql`{ user(id: 5) { firstName lastName } }`;
```

# Context & Application

Tagged templates provide a clean, readable way to embed structured text (HTML, SQL, GraphQL, regex) in JavaScript with the ability to validate and transform the content at the tag function level.

# Examples

From the source text:

```js
// lit-html for web components
render() {
  return html`
    <ul>
      ${repeat(this.items, (item) => item.id,
        (item, index) => html`<li>${index}: ${item.name}</li>`
      )}
    </ul>
  `;
}

// regex with comments and free-spacing
const RE_DATE = regex('g')`
  ${RE_YEAR} # 4 digits
  - ${RE_MONTH} # 2 digits
  - ${RE_DAY} # 2 digits
`;

// GraphQL
const query = gql`
  { user(id: 5) { firstName lastName } }
`;
```

# Relationships

## Builds Upon
- **tagged-template** — these are practical applications

## Enables
- Type-safe embedded DSLs
- Build-time optimization of templates

## Related
- **string-raw** — one of the simplest built-in tag functions

## Contrasts With
- None

# Common Errors

- **Error**: Using string concatenation for HTML/SQL instead of tagged templates
  **Correction**: Tagged templates can automatically escape user input, preventing injection attacks.

# Common Confusions

- **Confusion**: Thinking tagged templates are limited to string output
  **Clarification**: Tag functions can return anything -- DOM nodes, ASTs, query objects, etc.

# Source Reference

Chapter 23: Using template literals and tagged templates, Section 23.4, lines 266-357.

# Verification Notes

- Definition source: direct (library examples from source)
- Confidence rationale: Three concrete library examples provided
- Cross-reference status: verified
