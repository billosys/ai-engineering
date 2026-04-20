---
# === CORE IDENTIFICATION ===
concept: String Literals
slug: string-literals

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
pdf_page: 50
section: "3.3.1 String Literals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - string-type
  - literals
extends:
  - literals
related:
  - template-literals
  - escape-sequences
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

String literals are text values enclosed in matched pairs of single quotes (`'`), double quotes (`"`), or backticks (`` ` ``), with backtick-delimited strings being template literals that support expression interpolation.

# Core Definition

"To include a string in a JavaScript program, simply enclose the characters of the string within a matched pair of single or double quotes or backticks (' or \" or `). Double-quote characters and backticks may be contained within strings delimited by single-quote characters, and similarly for strings delimited by double quotes and backticks." Backtick-delimited strings are template literals (ES6) that allow expression interpolation. (p. 50)

# Prerequisites

- **string-type** — String literals produce String values
- **literals** — String literals are a type of literal

# Key Properties

1. Three delimiter types: single quotes, double quotes, backticks
2. Each delimiter can contain the other two unescaped
3. ES5+: strings can span multiple lines with trailing backslash
4. Backtick strings (ES6): can span multiple lines natively, with line breaks included
5. Single/double quoted strings must use `\n` for newlines
6. Mixing quote styles is recommended when combining JavaScript and HTML

# Construction / Recognition

```javascript
""                                  // The empty string
'testing'
"3.14"
'name="myform"'
"Wouldn't you prefer O'Reilly's book?"
`"She said 'hi'", he said.`
```

# Context & Application

String literals are used constantly in JavaScript. Convention is to pick one quote style and use it consistently, switching only when the string content requires it.

# Examples

From the source text (pp. 50-51):
```javascript
""                                        // The empty string
'testing'
"3.14"
'name="myform"'
"Wouldn't you prefer O'Reilly's book?"
`"She said 'hi'", he said.`

// Multi-line strings
'two\nlines'                              // A string representing 2 lines
"one\
 long\
 line"                                    // ES5: backslash line continuation
`the newline character at the end of this line
is included literally in this string`     // ES6: template literal
```

HTML mixing (p. 51):
```html
<button onclick="alert('Thank you')">Click Me</button>
```

# Relationships

## Builds Upon
- **string-type** — String literals create String values
- **literals** — A specific kind of literal

## Enables
- **template-literals** — Backtick strings with expression interpolation
- **escape-sequences** — Special characters within strings

## Related
- **template-literals** — Backtick-delimited strings are template literals

## Contrasts With
- None within this source

# Common Errors

- **Error**: Using an apostrophe in a single-quoted string without escaping.
  **Correction**: Use `\'` to escape: `'can\'t'`, or switch to double quotes: `"can't"`.

# Common Confusions

- **Confusion**: Single and double quotes have different semantic meaning.
  **Clarification**: Single and double quotes are functionally identical in JavaScript — the choice is purely stylistic.

# Source Reference

Chapter 3: Types, Values, and Variables, Section 3.3.1, pages 50-51.

# Verification Notes

- Definition source: Direct quote from p. 50
- Confidence rationale: High — clearly defined
- Uncertainties: None
- Cross-reference status: Verified
