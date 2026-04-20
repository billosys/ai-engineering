---
# === CORE IDENTIFICATION ===
concept: Reserved Words
slug: reserved-words

# === CLASSIFICATION ===
category: syntax-fundamentals
subcategory: naming
tier: foundational

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Syntax"
chapter_number: 9
pdf_page: null
section: "9.4.2 Reserved words"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - keywords
  - reserved identifiers

# === TYPED RELATIONSHIPS ===
prerequisites:
  - identifiers
extends: []
related:
  - strict-mode
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Which words cannot be used as variable names in JavaScript?"
---

# Quick Definition

Reserved words are identifiers with special meaning in JavaScript (like `if`, `const`, `class`) that cannot be used as variable names but can be used as property names.

# Core Definition

"Reserved words can't be variable names, but they can be property names." (Ch. 9, &sect;9.4.2). All JavaScript keywords are reserved: `await`, `break`, `case`, `catch`, `class`, `const`, `continue`, `debugger`, `default`, `delete`, `do`, `else`, `export`, `extends`, `finally`, `for`, `function`, `if`, `import`, `in`, `instanceof`, `let`, `new`, `return`, `static`, `super`, `switch`, `this`, `throw`, `try`, `typeof`, `var`, `void`, `while`, `with`, `yield`. Unused keywords: `enum`, `implements`, `package`, `protected`, `interface`, `private`, `public`. Reserved literals: `true`, `false`, `null`. Effectively reserved: `Infinity`, `NaN`, `undefined`, `async`.

# Prerequisites

- **identifiers** -- reserved words are special identifiers

# Key Properties

1. Cannot be used as variable names
2. Can be used as property names (e.g., `obj.if`)
3. Includes all keywords, unused keywords, and reserved literals
4. `Infinity`, `NaN`, `undefined`, `async` are technically not reserved but should be avoided
5. Global variable names (`String`, `Math`) should also be avoided

# Construction / Recognition

Using a reserved word as a variable name produces a `SyntaxError`:
```js
const if = 123; // SyntaxError: Unexpected token if
```

# Context & Application

When naming variables, avoid all reserved words and effectively-reserved global names.

# Examples

From the source text (Ch. 9, &sect;9.4.2):
```js
const if = 123;
  // SyntaxError: Unexpected token if

// But property names are fine:
const obj = { if: 123 };
obj.if // 123
```

# Relationships

## Builds Upon
- **identifiers** -- reserved words restrict which identifiers can be variable names

## Enables
- Proper variable naming

## Related
- **strict-mode** -- some words are only reserved in strict mode

## Contrasts With
- No direct contrast

# Common Errors

- **Error**: Using `class`, `return`, or other keywords as variable names.
  **Correction**: Choose alternative names; these are reserved.

# Common Confusions

- **Confusion**: Thinking reserved words can't be used anywhere.
  **Clarification**: They can be property names: `obj.class`, `obj.return`, etc.

# Source Reference

Chapter 9: Syntax, Section 9.4.2, lines 622-653.

# Verification Notes

- Definition source: direct from source
- Confidence rationale: Comprehensive list provided
- Cross-reference status: verified
