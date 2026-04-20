---
# === CORE IDENTIFICATION ===
concept: Template Literals
slug: template-literals

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: literals
tier: intermediate

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Types, Values, and Variables"
chapter_number: 3
pdf_page: 54
section: "3.3.4 Template Literals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - template strings
  - backtick strings
  - string interpolation
  - tagged template literals

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string-type
  - string-literals
  - ecmascript-versioning
extends:
  - string-literals
related:
  - escape-sequences
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a template literal?"
---

# Quick Definition

Template literals are ES6 backtick-delimited strings that support embedded JavaScript expressions via `${expression}` syntax, multi-line text without escape characters, and tagged template functions.

# Core Definition

"In ES6 and later, string literals can be delimited with backticks." These "template literals can include arbitrary JavaScript expressions. The final value of a string literal in backticks is computed by evaluating any included expressions, converting the values of those expressions to strings and combining those computed strings with the literal characters within the backticks." "Everything between the ${ and the matching } is interpreted as a JavaScript expression." (pp. 54-55)

# Prerequisites

- **string-type** — Template literals produce String values
- **string-literals** — Template literals are an advanced form of string literal
- **ecmascript-versioning** — Template literals are an ES6 feature

# Key Properties

1. Delimited by backticks (`` ` ``)
2. Expression interpolation: `${expression}` evaluates and inserts the expression's string value
3. Can include any number of expressions
4. Can span multiple lines — line breaks are included literally
5. Support all escape sequences that regular strings do
6. Tagged template literals: a function name before the backtick receives the template parts
7. `String.raw` is a built-in tag that returns text without processing backslash escapes

# Construction / Recognition

```javascript
let name = "Bill";
let greeting = `Hello ${ name }.`;      // greeting == "Hello Bill."

let errorMessage = `\
\u2718 Test failure at ${filename}:${linenumber}:
${exception.message}
Stack trace:
${exception.stack}
`;
```

# Context & Application

Template literals are the preferred way to build strings that include variable values, replacing string concatenation with `+`. They are also useful for multi-line strings and, with tags, for DSLs like HTML/SQL escaping.

# Examples

From the source text (pp. 54-55):
```javascript
let name = "Bill";
let greeting = `Hello ${ name }.`;  // greeting == "Hello Bill."
```

Multi-line with expressions (p. 55):
```javascript
let errorMessage = `\
\u2718 Test failure at ${filename}:${linenumber}:
${exception.message}
Stack trace:
${exception.stack}
`;
```

Tagged template literal (p. 55):
```javascript
`\n`.length              // => 1: the string has a single newline character
String.raw`\n`.length    // => 2: a backslash character and the letter n
```

# Relationships

## Builds Upon
- **string-type** — Template literals produce String values
- **string-literals** — Template literals extend string literal syntax

## Enables
- Tagged template literals for custom DSLs
- Readable string construction with embedded expressions

## Related
- **escape-sequences** — Template literals support the same escape sequences

## Contrasts With
- Regular string literals with `+` concatenation — template literals are more readable

# Common Errors

- **Error**: Using `${}` inside single or double-quoted strings.
  **Correction**: Expression interpolation only works in backtick-delimited template literals, not in `'...'` or `"..."` strings.

# Common Confusions

- **Confusion**: Tagged template literals call the function with the final string.
  **Clarification**: Tagged templates pass the literal text segments and expression values separately to the tag function, allowing custom processing before producing a result.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.3.4, pages 54-55.

# Verification Notes

- Definition source: Direct quotes from pp. 54-55
- Confidence rationale: High — thoroughly explained with examples
- Uncertainties: None
- Cross-reference status: Verified
