---
# === CORE IDENTIFICATION ===
concept: Reserved Words
slug: reserved-words

# === CLASSIFICATION ===
category: core-idioms
subcategory: language-syntax
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Introduction"
chapter_number: null
pdf_page: null
section: "Reserved Words"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "keywords"
  - "reserved identifiers"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - erlang-reference-manual-overview
  - if-expression
  - case-expression
  - maybe-expression
  - function-declaration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the reserved words in Erlang?"
  - "Can I use 'maybe' as a variable or atom name?"
  - "Which reserved words are not currently used by the language?"
---

# Quick Definition

Reserved words are identifiers that have special meaning in Erlang and cannot be used as atom or variable names without quoting. Erlang defines 29 reserved words.

# Core Definition

The Erlang Reference Manual provides a complete enumeration of reserved words: `after`, `and`, `andalso`, `band`, `begin`, `bnot`, `bor`, `bsl`, `bsr`, `bxor`, `case`, `catch`, `cond`, `div`, `else`, `end`, `fun`, `if`, `let`, `maybe`, `not`, `of`, `or`, `orelse`, `receive`, `rem`, `try`, `when`, `xor`. Two of these -- `cond` and `let` -- are reserved but not currently used by the language. The word `maybe` is conditionally reserved depending on the `maybe_expr` feature flag (Erlang Reference Manual, Introduction, "Reserved Words").

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. There are 29 reserved words in Erlang
2. Reserved words cannot be used as unquoted atoms or variable names
3. `cond` and `let` are reserved but currently unused by the language
4. `maybe` is a reserved word only when the `maybe_expr` feature is enabled
5. In Erlang/OTP 25 and 26, `maybe_expr` is disabled by default
6. Starting from Erlang/OTP 27, `maybe_expr` is enabled by default
7. Reserved words include control flow (`if`, `case`, `receive`, `try`, `catch`, `maybe`), logical operators (`and`, `or`, `not`, `andalso`, `orelse`, `xor`), bitwise operators (`band`, `bor`, `bxor`, `bnot`, `bsl`, `bsr`), arithmetic operators (`div`, `rem`), and block delimiters (`begin`, `end`, `fun`, `of`, `when`, `after`, `else`)

# Construction / Recognition

## To Identify/Recognize:
1. Check whether a token appears in the reserved word list
2. Reserved words are all lowercase
3. If using `maybe`, check whether the `maybe_expr` feature is enabled in your OTP version

# Context & Application

Reserved words define the syntactic backbone of the Erlang language. They are used for control flow, operators, and block structure. Understanding which words are reserved prevents naming conflicts when defining atoms, functions, or variables. The conditional reservation of `maybe` reflects Erlang's feature-flag system for introducing new language constructs gradually.

# Examples

**Example 1** (Introduction, Reserved Words): The complete list: `after and andalso band begin bnot bor bsl bsr bxor case catch cond div else end fun if let maybe not of or orelse receive rem try when xor`

**Example 2** (Introduction, Reserved Words): "`cond` and `let`, while reserved, are currently not used by the language."

**Example 3** (Introduction, Reserved Words): "`maybe` is a reserved word only if feature `maybe_expr` is enabled. In Erlang/OTP 25 and 26, `maybe_expr` is disabled by default. Starting from Erlang/OTP 27, `maybe_expr` is enabled by default."

# Relationships

## Enables
- **if-expression** -- `if` is a reserved word that introduces conditional guard evaluation
- **case-expression** -- `case` is a reserved word for pattern-matching expressions
- **maybe-expression** -- `maybe` is a conditionally reserved word for conditional match chains
- **function-declaration** -- `when` is used in guard sequences in function clauses

## Related
- **block-expression** -- `begin` and `end` are reserved words for block expressions
- **erlang-reference-manual-overview** -- Reserved words are listed in the Introduction chapter

# Common Errors

- **Error**: Using a reserved word as an unquoted atom (e.g., `catch` as a function name)
  **Correction**: Either choose a different name or quote the atom (e.g., `'catch'`), though quoting reserved words is discouraged

# Common Confusions

- **Confusion**: Assuming `maybe` is always a reserved word
  **Clarification**: `maybe` is only reserved when the `maybe_expr` feature is enabled; in OTP 25-26 it is off by default, from OTP 27 onward it is on by default

- **Confusion**: Assuming `cond` and `let` introduce language constructs
  **Clarification**: These words are reserved for possible future use but currently have no meaning in the language

# Source Reference

Introduction chapter of the Erlang Reference Manual, section "Reserved Words."

# Verification Notes

- Definition source: Direct enumeration from source text
- Confidence rationale: HIGH -- explicit, complete list provided in source
- Uncertainties: None
- Cross-reference status: Related slugs are planned for extraction
