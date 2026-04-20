---
# === CORE IDENTIFICATION ===
concept: Reserved Words
slug: reserved-words

# === CLASSIFICATION ===
category: language-fundamentals
subcategory: lexical-structure
tier: foundational

# === PROVENANCE ===
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Lexical Structure"
chapter_number: 2
pdf_page: 34
section: "2.4.1 Reserved Words"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - keywords

# === TYPED RELATIONSHIPS ===
prerequisites:
  - identifiers
extends: []
related:
  - case-sensitivity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions: []
---

# Quick Definition

Reserved words are identifiers that JavaScript reserves for use by the language itself, which cannot be used as variable, function, or class names (though some can be used as object property names).

# Core Definition

"JavaScript reserves certain identifiers for use by the language itself. These 'reserved words' cannot be used as regular identifiers." Some are keywords that "must not be used as the names of constants, variables, functions, or classes (though they can all be used as the names of properties within an object)." Others like `from`, `of`, `get`, and `set` "are used in limited contexts with no syntactic ambiguity and are perfectly legal as identifiers." (pp. 33-34)

# Prerequisites

- **identifiers** — Reserved words are identifiers claimed by the language

# Key Properties

1. Include language keywords: `if`, `while`, `for`, `let`, `const`, `var`, `function`, `class`, `return`, etc.
2. Cannot be used as variable, constant, function, or class names
3. Can be used as property names within objects
4. Some words (`from`, `set`, `target`) are safe to use as identifiers
5. Future reserved words: `enum`, `implements`, `interface`, `package`, `private`, `protected`, `public`
6. `arguments` and `eval` should be avoided as identifiers
7. `let` has complex rules — cannot be used inside a class or with `const`

# Construction / Recognition

Reserved words include: `as`, `async`, `await`, `break`, `case`, `catch`, `class`, `const`, `continue`, `debugger`, `default`, `delete`, `do`, `else`, `export`, `extends`, `false`, `finally`, `for`, `from`, `function`, `get`, `if`, `import`, `in`, `instanceof`, `let`, `new`, `null`, `of`, `return`, `set`, `static`, `super`, `switch`, `target`, `this`, `throw`, `true`, `try`, `typeof`, `var`, `void`, `while`, `with`, `yield`.

# Context & Application

Knowing reserved words is essential to avoid syntax errors when naming variables and functions. The simplest approach is "to avoid using any of these words as identifiers, except for from, set, and target, which are safe to use and are already in common use" (p. 34).

# Examples

From the source text (p. 34):
- `while` is a reserved keyword — cannot be used as a variable name
- `from`, `set`, `target` are safe to use as identifiers
- `let` cannot be used as a variable name inside a class or with `const`, but can be with `var` outside a class
- Future reserved: `enum`, `implements`, `interface`, `package`, `private`, `protected`, `public`

# Relationships

## Builds Upon
- **identifiers** — Reserved words restrict what identifiers can be used

## Enables
- Correct variable and function naming

## Related
- **case-sensitivity** — Reserved words are case-sensitive (lowercase only)

## Contrasts With
- None within this source

# Common Errors

- **Error**: Using a reserved word like `class` or `return` as a variable name.
  **Correction**: Choose a different identifier name; reserved words cannot be used as variable names.

# Common Confusions

- **Confusion**: All reserved words are completely forbidden as identifiers everywhere.
  **Clarification**: Reserved words can be used as property names within objects, and some like `from`, `set`, and `target` are legal as identifiers.

# Source Reference

Chapter 2: Lexical Structure, Section 2.4.1, pages 33-35.

# Verification Notes

- Definition source: Direct quotes from pp. 33-34
- Confidence rationale: High — clearly listed and explained
- Uncertainties: None
- Cross-reference status: Verified
